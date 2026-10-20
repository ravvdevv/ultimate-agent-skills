#!/usr/bin/env python3
"""Validate skill metadata, directory layout, and local Markdown file links."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FIELD_RE = re.compile(r"^([a-zA-Z][a-zA-Z0-9_-]*):\s*(.*?)\s*$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
ERRORS: list[str] = []


def error(path: Path, message: str) -> None:
    try:
        display_path = path.relative_to(ROOT)
    except ValueError:
        display_path = path
    ERRORS.append(f"{display_path}: {message}")


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        error(path, f"cannot read UTF-8 skill file: {exc}")
        return None
    if not lines or lines[0].strip() != "---":
        error(path, "missing YAML frontmatter opening delimiter")
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        error(path, "missing YAML frontmatter closing delimiter")
        return None

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:end], 2):
        match = FIELD_RE.fullmatch(line)
        if not match:
            error(path, f"unsupported or malformed frontmatter at line {line_number}")
            continue
        key, value = match.groups()
        if key in fields:
            error(path, f"duplicate frontmatter field {key!r}")
            continue
        fields[key] = value.strip().strip('"').strip("'")
    return fields


def validate_skill(path: Path) -> None:
    try:
        path.resolve(strict=True).relative_to(SKILLS_DIR.resolve())
    except (OSError, ValueError):
        error(path, "skill file resolves outside the skills directory or is missing")
        return
    fields = parse_frontmatter(path)
    if fields is None:
        return

    folder_name = path.parent.name
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not name:
        error(path, "frontmatter requires name")
    elif not NAME_RE.fullmatch(name):
        error(path, f"name must be lowercase kebab-case: {name!r}")
    elif name != folder_name:
        error(path, f"name {name!r} does not match directory {folder_name!r}")
    if len(description) < 20:
        error(path, "frontmatter description must be at least 20 characters")
    if len(description) > 1024:
        error(path, "frontmatter description exceeds 1024 characters")

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
        end = lines.index("---", 1)
    except (OSError, UnicodeError, ValueError):
        return
    body = "\n".join(lines[end + 1 :])
    checks = (
        (r"^#\s+\S", "missing top-level Markdown title"),
        (r"^##\s+(Workflow|Steps|Response rules)\b", "missing a Workflow, Steps, or Response rules section"),
        (r"^##\s+Guardrails\b", "missing Guardrails section"),
        (r"^##\s+Completion checklist\b", "missing Completion checklist section"),
    )
    for pattern, message in checks:
        if not re.search(pattern, body, re.MULTILINE | re.IGNORECASE):
            error(path, message)


def strip_fenced_code(content: str) -> str:
    output: list[str] = []
    fence_char = ""
    fence_length = 0
    backtick = chr(96)
    for line in content.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(backtick * 3):
            fence, length = backtick, len(stripped) - len(stripped.lstrip(backtick))
        elif stripped.startswith("~~~"):
            fence, length = "~", len(stripped) - len(stripped.lstrip("~"))
        else:
            fence, length = "", 0
        if fence:
            if not fence_char:
                fence_char, fence_length = fence, length
            elif fence == fence_char and length >= fence_length:
                fence_char, fence_length = "", 0
            continue
        if not fence_char:
            output.append(line)
    return "\n".join(output)


def validate_local_links(path: Path) -> None:
    try:
        content = strip_fenced_code(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        error(path, f"cannot inspect Markdown links: {exc}")
        return
    for match in LINK_RE.finditer(content):
        target = match.group(1).strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        local_path = (path.parent / unquote(parsed.path)).resolve()
        try:
            local_path.relative_to(ROOT.resolve())
        except ValueError:
            error(path, f"local link escapes repository: {target!r}")
            continue
        if not local_path.exists():
            error(path, f"broken local link: {target!r}")


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("ERROR: skills directory is missing", file=sys.stderr)
        return 1
    directories = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not directories:
        print("ERROR: no skill directories found", file=sys.stderr)
        return 1

    names: dict[str, Path] = {}
    for directory in directories:
        path = directory / "SKILL.md"
        if not path.is_file():
            error(directory, "skill directory is missing SKILL.md")
            continue
        validate_skill(path)
        fields = parse_frontmatter(path)
        if fields is None:
            continue
        name = fields.get("name", "")
        if name:
            if name in names:
                error(path, f"duplicate skill name {name!r} also used by {names[name].relative_to(ROOT)}")
            else:
                names[name] = path

    markdown_files = sorted(
        path for path in ROOT.rglob("*.md")
        if ".git" not in path.relative_to(ROOT).parts
    )
    for path in markdown_files:
        validate_local_links(path)

    if ERRORS:
        print("\n".join(f"ERROR: {item}" for item in ERRORS), file=sys.stderr)
        print(f"Validation failed: {len(ERRORS)} issue(s) across {len(directories)} skill director(ies).", file=sys.stderr)
        return 1
    print(f"Validated {len(directories)} skills and local links in {len(markdown_files)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
