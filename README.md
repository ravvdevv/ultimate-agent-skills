# Ultimate Agent Skills

Reusable workflows for coding agents: code review, debugging, research, humanizing prose, product planning, frontend review, QA/release, and attention-friendly execution.

**Repository:** https://github.com/ravvdevv/ultimate-agent-skills

## Install with your AI agent

Copy this prompt into the coding agent you want to configure:

```text
Install the skills from https://github.com/ravvdevv/ultimate-agent-skills into the correct skills directory for the AI agent and current project.

1. Identify the agent/runtime and check its current official documentation or existing project conventions to find the correct skills directory.
2. Clone or download the repository into a temporary location. Do not put the entire repository inside the target skills directory.
3. Install all skills from its `skills/*/SKILL.md` files into the current project, preserving each skill's folder name and placing each file at <target-skills-directory>/<skill-name>/SKILL.md.
4. Do not overwrite existing skills silently. If a destination already exists, compare it and explain the conflict before replacing anything.
5. Verify every copied skill and report the destination, installed skill names, and any steps needed to reload or restart the agent.
6. Keep the change limited to skill installation. Do not install unrelated tools, run arbitrary scripts, or claim success without verifying the files.

If this runtime does not support this skill format, explain the limitation and give the closest supported installation method instead.
```

## Install manually

Read **[INSTALLATION.md](INSTALLATION.md)** for copy-paste commands for Claude Code, OpenAI Codex, OpenCode, Cursor, and Windows PowerShell.

## Included skills

- [Code Review](skills/code-review/SKILL.md)
- [Debugging](skills/debugging/SKILL.md)
- [Research](skills/research/SKILL.md)
- [Humanizer](skills/humanizer/SKILL.md)
- [Product Planning](skills/product-planning/SKILL.md)
- [Frontend Design Review](skills/frontend-design-review/SKILL.md)
- [QA and Release](skills/qa-release/SKILL.md)
- [Attention-Friendly](skills/attention-friendly/SKILL.md)

See [UPSTREAMS.md](UPSTREAMS.md) for related projects, integrations, and licensing notes. These skills do not automatically install upstream tools or separate behavior skills such as Caveman Ultra, Ponytail Ultra, or i-have-adhd.

## Contributing and license

See [CONTRIBUTING.md](CONTRIBUTING.md). Original repository content is MIT-licensed; third-party projects retain their own licenses. See [LICENSE.md](LICENSE.md).
