# Skills

A skill is a focused set of instructions that helps an agent perform a repeatable task consistently.

## Available skills

### Engineering

- [Code Review](code-review/SKILL.md): review changes for correctness, regressions, security, and maintainability.
- [Debugging](debugging/SKILL.md): reproduce, isolate, fix, and verify a failure.
- [QA and Release](qa-release/SKILL.md): perform risk-based verification and report release evidence.
- [Product Planning](product-planning/SKILL.md): scope substantial work and define acceptance criteria.

### Research and writing

- [Research](research/SKILL.md): answer research questions using credible sources and transparent uncertainty.
- [Humanizer](humanizer/SKILL.md): improve naturalness without inventing or dropping facts.

### Frontend and agent workflow

- [Frontend Design Review](frontend-design-review/SKILL.md): review design quality, responsive behavior, accessibility, and interaction states.
- [Attention-Friendly](attention-friendly/SKILL.md): reduce cognitive overhead and make long work easier to resume.

## External workflow references

See [../UPSTREAMS.md](../UPSTREAMS.md) for integration notes on UI/UX Pro Max, Impeccable, gstack, ECC, Humanizer, and separate behavior skills. External CLIs and assets are linked, not silently vendored.

## Adding a skill

Create a directory with a descriptive kebab-case name and add a `SKILL.md` containing frontmatter, triggers, workflow, guardrails, and a completion checklist. Keep it concise enough to follow and specific enough to change the agent's behavior.
