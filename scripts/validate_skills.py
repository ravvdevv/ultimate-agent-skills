#!/usr/bin/env python3
"""Validate skill names and required SKILL.md structure using only the Python stdlib."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ERRORS: list[str] = []


def error(path: Path, message: str) -> None:
    ERRORS.append(f"{path.relative_to(ROOT)}: {message}")


def validate(path: Path) -> None:
    folder_name = path.parent.name
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        error(path, "missing YAML frontmatter opening delimiter")
        return

    try:
        end = lines.index("---", 1)
    except ValueError:
        error(path, "missing YAML frontmatter closing delimiter")
        return

    frontmatter = lines[1:end]
    fields: dict[str, str] = {}
    for line in frontmatter:
        match = re.match(r"^([a-zA-Z][a-zA-Z0-9_-]*):\s*(.*?)\s*$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip('"').strip("'")

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

    body = "\n".join(lines[end + 1 :])
    if not re.search(r"^#\s+\S", body, re.MULTILINE):
        error(path, "missing top-level Markdown title")
    if not re.search(r"^##\s+(Workflow|Steps|Response rules)\b", body, re.MULTILINE | re.IGNORECASE):
        error(path, "missing a Workflow, Steps, or Response rules section")
    if not re.search(r"^##\s+Guardrails\b", body, re.MULTILINE | re.IGNORECASE):
        error(path, "missing Guardrails section")
    if not re.search(r"^##\s+Completion checklist\b", body, re.MULTILINE | re.IGNORECASE):
        error(path, "missing Completion checklist section")


def main() -> int:
    paths = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not paths:
        print("ERROR: no skills/*/SKILL.md files found", file=sys.stderr)
        return 1

    names: dict[str, Path] = {}
    for path in paths:
        validate(path)
        lines = path.read_text(encoding="utf-8").splitlines()
        if lines and lines[0].strip() == "---":
            try:
                end = lines.index("---", 1)
            except ValueError:
                end = 1
            for line in lines[1:end]:
                match = re.match(r"^name:\s*(.*?)\s*$", line)
                if match:
                    name = match.group(1).strip().strip('"').strip("'")
                    if name in names:
                        error(path, f"duplicate skill name {name!r} also used by {names[name].relative_to(ROOT)}")
                    else:
                        names[name] = path

    if ERRORS:
        print("\n".join(f"ERROR: {item}" for item in ERRORS), file=sys.stderr)
        print(f"Validation failed: {len(ERRORS)} issue(s) across {len(paths)} skill(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(paths)} skills successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
