# Ultimate Agent Skills

A curated set of reusable workflows that help coding agents plan, implement, debug, review, and verify real work.

## Install

**Recommended: use the open skills CLI.** It handles supported agent destinations and lets you select which skills to install.

```bash
# List available skills first
npx skills add ravvdevv/ultimate-agent-skills --list

# Install interactively
npx skills add ravvdevv/ultimate-agent-skills

# Install all skills for a specific agent
npx skills add ravvdevv/ultimate-agent-skills --skill '*' --agent codex

# Install one skill
npx skills add ravvdevv/ultimate-agent-skills --skill verification-before-completion
```

Replace `codex` with the agent identifier supported by the CLI. Run `npx skills --help` for current options. Review a skill before installing it, especially in work environments with sensitive code or credentials.

Want an agent to handle setup? Paste this into your coding agent:

```text
Install skills from https://github.com/ravvdevv/ultimate-agent-skills.

First inspect the repository and the current official installation instructions for this agent. Prefer the supported skills CLI when available; otherwise use the repository's INSTALLATION.md. Ask before overwriting existing skills, install only into the intended project or user scope, and verify the resulting files. Do not install unrelated tools or claim success without checking the result.
```

Manual and Windows instructions: [INSTALLATION.md](INSTALLATION.md).

## Included skills

### Engineering
- [Test-Driven Development](skills/test-driven-development/SKILL.md): use a red-green-refactor loop for behavior changes.
- [Debugging](skills/debugging/SKILL.md): reproduce failures and isolate root causes.
- [Code Review](skills/code-review/SKILL.md): find actionable correctness, security, and regression issues.
- [Verification Before Completion](skills/verification-before-completion/SKILL.md): ground completion claims in fresh evidence.
- [QA and Release](skills/qa-release/SKILL.md): verify changes and release readiness with risk-based checks.

### Planning and product
- [Brainstorming](skills/brainstorming/SKILL.md): clarify important decisions before substantial implementation.
- [Product Planning](skills/product-planning/SKILL.md): turn feature ideas into scoped, testable plans.

### Research, writing, and design
- [Research](skills/research/SKILL.md): answer research questions with credible sources and explicit uncertainty.
- [Humanizer](skills/humanizer/SKILL.md): improve naturalness without changing meaning.
- [Frontend Design Review](skills/frontend-design-review/SKILL.md): review responsive behavior, accessibility, and visual quality.
- [Attention-Friendly](skills/attention-friendly/SKILL.md): make long tasks easier to resume and manage.

## Design principles

- Focused workflows, not a pile of generic instructions.
- Inspect the existing project before proposing or changing it.
- Prefer evidence over confident guesses.
- Keep steps proportional to task size and risk.
- Preserve user changes, avoid destructive actions, and report limitations honestly.

See [skills/README.md](skills/README.md) for the catalog, [UPSTREAMS.md](UPSTREAMS.md) for related projects and licensing notes, and [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines. Original repository content is MIT-licensed; upstream projects retain their own licenses. See [LICENSE.md](LICENSE.md).
