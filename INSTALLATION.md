# Installation

These are portable `SKILL.md` workflows, not a standalone application. Install only the skills you want into the directory your coding agent scans. Project-level installs are shared with that project; user-level installs are available across projects.

## 1. Get the repository

```bash
git clone https://github.com/ravvdevv/ultimate-agent-skills.git
cd ultimate-agent-skills
```

## 2. Choose your agent

### Claude Code

Project-level:

```bash
mkdir -p .claude/skills
for src in skills/*; do
  [ -f "$src/SKILL.md" ] || continue
  name="$(basename "$src")"
  mkdir -p ".claude/skills/$name"
  cp "$src/SKILL.md" ".claude/skills/$name/SKILL.md"
done
```

User-level destination: `~/.claude/skills/<skill-name>/SKILL.md`.

### OpenAI Codex

Project-level:

```bash
mkdir -p .agents/skills
for src in skills/*; do
  [ -f "$src/SKILL.md" ] || continue
  name="$(basename "$src")"
  mkdir -p ".agents/skills/$name"
  cp "$src/SKILL.md" ".agents/skills/$name/SKILL.md"
done
```

User-level destination: `~/.agents/skills/<skill-name>/SKILL.md`.

### OpenCode

Project-level:

```bash
mkdir -p .opencode/skill
for src in skills/*; do
  [ -f "$src/SKILL.md" ] || continue
  name="$(basename "$src")"
  mkdir -p ".opencode/skill/$name"
  cp "$src/SKILL.md" ".opencode/skill/$name/SKILL.md"
done
```

User-level destination: `~/.config/opencode/skill/<skill-name>/SKILL.md`.

### Cursor

Project-level:

```bash
mkdir -p .cursor/skills
for src in skills/*; do
  [ -f "$src/SKILL.md" ] || continue
  name="$(basename "$src")"
  mkdir -p ".cursor/skills/$name"
  cp "$src/SKILL.md" ".cursor/skills/$name/SKILL.md"
done
```

User-level destination: `~/.cursor/skills/<skill-name>/SKILL.md`.

## 3. Install only selected skills

Instead of copying every skill, copy just the directory you need. For example, to install Code Review into Codex for the current project:

```bash
mkdir -p .agents/skills/code-review
cp skills/code-review/SKILL.md .agents/skills/code-review/SKILL.md
```

Replace `code-review` with `debugging`, `research`, `humanizer`, `product-planning`, `frontend-design-review`, `qa-release`, or `attention-friendly`.

## Windows PowerShell example

This example installs all skills into the current project's Codex directory. Change `.agents/skills` to the target path for your agent if needed.

```powershell
$target = ".agents/skills"
Get-ChildItem .\skills -Directory | ForEach-Object {
  $source = Join-Path $_.FullName "SKILL.md"
  if (Test-Path $source) {
    $destination = Join-Path (Join-Path $target $_.Name) "SKILL.md"
    New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
    Copy-Item $source $destination -Force
  }
}
```

## 4. Verify installation

Confirm the destination contains one folder per installed skill, each with a `SKILL.md` file. Restart or reload your agent if it does not discover new skills automatically. Ask it to list the skills it can access, then try a task that clearly matches one.

## Notes

- Install skills into the host's documented directory. Similar-looking paths are not interchangeable; for example, OpenCode uses `skill` (singular) in its documented directory.
- These files provide instructions. They do not install upstream CLIs, browser automation, hooks, specialist agents, or design-data assets referenced in [UPSTREAMS.md](UPSTREAMS.md).
- Caveman Ultra, Ponytail Ultra, and i-have-adhd remain separate third-party behavior skills and must be installed/configured separately in the host that supports them.
- Review [UPSTREAMS.md](UPSTREAMS.md) and each upstream project's license before installing or redistributing external tooling.
- To update your installed copies, pull the latest repository changes and copy the relevant `SKILL.md` files again.
