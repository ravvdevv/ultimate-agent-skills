# Skills

A skill is a focused set of instructions that helps an agent perform a repeatable task consistently. Install through the [skills CLI](https://github.com/vercel-labs/skills) where supported, or follow the manual steps in [../INSTALLATION.md](../INSTALLATION.md).

## Available skills

### Engineering
- [Test-Driven Development](test-driven-development/SKILL.md): use a red-green-refactor loop for testable behavior changes.
- [Debugging](debugging/SKILL.md): reproduce, isolate, fix, and verify a failure.
- [Code Review](code-review/SKILL.md): review changes for correctness, regressions, security, and maintainability.
- [Verification Before Completion](verification-before-completion/SKILL.md): require fresh evidence before claiming work is done.
- [QA and Release](qa-release/SKILL.md): perform risk-based verification and report release evidence.

### Planning and product
- [Brainstorming](brainstorming/SKILL.md): clarify material decisions before substantial work.
- [Product Planning](product-planning/SKILL.md): scope work and define acceptance criteria.

### Research, writing, and design
- [Research](research/SKILL.md): answer research questions using credible sources and transparent uncertainty.
- [Humanizer](humanizer/SKILL.md): improve naturalness without inventing or dropping facts.
- [Frontend Design Review](frontend-design-review/SKILL.md): review design quality, responsive behavior, accessibility, and interaction states.
- [Attention-Friendly](attention-friendly/SKILL.md): reduce cognitive overhead and make long work easier to resume.

## Adding a skill

Create a directory with a descriptive kebab-case name and a `SKILL.md` file containing frontmatter, triggers, a concise workflow, guardrails, and a completion checklist. Prefer original, focused workflows; avoid copying upstream content wholesale. Validate links, metadata, and examples before submitting.

## Related projects

See [../UPSTREAMS.md](../UPSTREAMS.md) for integration notes on UI/UX Pro Max, Impeccable, gstack, ECC, Humanizer, and separate behavior skills. External CLIs and assets are linked, not silently vendored.
