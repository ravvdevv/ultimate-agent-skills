# Installation

The recommended method is the open-source `skills` CLI, which discovers skills in this repository and installs them to supported coding agents. Manual copy instructions are available below if you cannot use the CLI.

## Recommended: skills CLI

Requires Node.js/npm and internet access.

```bash
# List the available skills before installing
npx skills add ravvdevv/ultimate-agent-skills --list

# Install interactively and choose the agent(s) and scope
npx skills add ravvdevv/ultimate-agent-skills

# Install a specific skill
npx skills add ravvdevv/ultimate-agent-skills --skill debugging

# Install all skills for one agent (example: Codex)
npx skills add ravvdevv/ultimate-agent-skills --skill '*' --agent codex

# Install all skills across all detected/supported agents
npx skills add ravvdevv/ultimate-agent-skills --all

# Check for updates to installed skills
npx skills check
npx skills update
```

The CLI's supported agent identifiers and options can change; check its current help with `npx skills --help`. Use interactive installation if you are unsure which identifier to use. Review skills before installing them in sensitive environments.

## Install through your coding agent

Paste this prompt into the agent you want to configure:

```text
Install skills from https://github.com/ravvdevv/ultimate-agent-skills.

1. Identify this agent and inspect its current official skills documentation.
2. Prefer the supported `skills` CLI and show me the proposed target agent and scope before making changes. If the CLI is unavailable, follow the manual instructions in INSTALLATION.md.
3. List the available skills and install only the ones requested, unless I explicitly ask for all.
4. Do not overwrite existing skill files silently. Compare conflicts and ask before replacing custom content.
5. Verify installed paths and report exact skill names, destination, and any reload/restart steps.
6. Do not run unrelated scripts or claim success without checking the resulting files.
```

## Manual installation

These examples install files into the current project's root. Clone this repository beside the project first, or adjust `SKILLS_REPO` to the actual path. Run commands from the project root.

### Claude Code

```bash
SKILLS_REPO="../ultimate-agent-skills"
mkdir -p .claude/skills
for src in "$SKILLS_REPO"/skills/*; do
  [ -f "$src/SKILL.md" ] || continue
  name="$(basename "$src")"
  dest=".claude/skills/$name/SKILL.md"
  mkdir -p "$(dirname "$dest")"
  if [ -e "$dest" ]; then echo "Skipping existing file: $dest"; continue; fi
  cp "$src/SKILL.md" "$dest"
done
```

### OpenAI Codex

```bash
SKILLS_REPO="../ultimate-agent-skills"
mkdir -p .agents/skills
for src in "$SKILLS_REPO"/skills/*; do
  [ -f "$src/SKILL.md" ] || continue
  name="$(basename "$src")"
  dest=".agents/skills/$name/SKILL.md"
  mkdir -p "$(dirname "$dest")"
  if [ -e "$dest" ]; then echo "Skipping existing file: $dest"; continue; fi
  cp "$src/SKILL.md" "$dest"
done
```

### OpenCode

```bash
SKILLS_REPO="../ultimate-agent-skills"
mkdir -p .opencode/skill
for src in "$SKILLS_REPO"/skills/*; do
  [ -f "$src/SKILL.md" ] || continue
  name="$(basename "$src")"
  dest=".opencode/skill/$name/SKILL.md"
  mkdir -p "$(dirname "$dest")"
  if [ -e "$dest" ]; then echo "Skipping existing file: $dest"; continue; fi
  cp "$src/SKILL.md" "$dest"
done
```

### Cursor

```bash
SKILLS_REPO="../ultimate-agent-skills"
mkdir -p .cursor/skills
for src in "$SKILLS_REPO"/skills/*; do
  [ -f "$src/SKILL.md" ] || continue
  name="$(basename "$src")"
  dest=".cursor/skills/$name/SKILL.md"
  mkdir -p "$(dirname "$dest")"
  if [ -e "$dest" ]; then echo "Skipping existing file: $dest"; continue; fi
  cp "$src/SKILL.md" "$dest"
done
```

### Windows PowerShell (Codex example)

```powershell
$skillsRepo = "..\ultimate-agent-skills"
$target = ".agents/skills"
Get-ChildItem (Join-Path $skillsRepo "skills") -Directory | ForEach-Object {
  $source = Join-Path $_.FullName "SKILL.md"
  if (-not (Test-Path $source)) { return }
  $destination = Join-Path (Join-Path $target $_.Name) "SKILL.md"
  if (Test-Path $destination) {
    Write-Host "Skipping existing file: $destination"
    return
  }
  New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
  Copy-Item $source $destination
}
```

For user-level installations, use the agent's documented user skills directory instead of a project-local directory. Verify the exact path against current official documentation before installing; agent conventions are not interchangeable.

## Verify and update

- Confirm each installed skill has a `SKILL.md` file in the expected destination.
- Ask the agent to list the skills it can access and try a task matching one.
- Reload or restart the agent if required by its documentation.
- With the CLI, use `npx skills check` and `npx skills update` to inspect and apply available updates.
- With manual copies, pull the latest repository changes and copy only the intended files. The manual examples skip existing files to protect local edits.

## Scope and upstream notes

These are portable instruction files. They do not automatically install external CLIs, browser automation, hooks, specialist agents, or design-data assets mentioned in [UPSTREAMS.md](UPSTREAMS.md). Caveman Ultra, Ponytail Ultra, and i-have-adhd remain separate behavior skills and must be installed/configured separately in a compatible host.
