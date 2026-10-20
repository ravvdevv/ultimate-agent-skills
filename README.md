# Ultimate Agent Skills

A curated collection of practical, reusable skills for coding agents. Designed to be portable across agent runtimes and useful in real projects, not just impressive in a README.

## Principles

- **Verify, don't guess.** Inspect the repository and environment before changing things.
- **Small, reversible changes.** Prefer focused patches over sweeping rewrites.
- **Evidence over confidence.** Run relevant checks and report what actually passed.
- **Respect the project.** Follow existing conventions and avoid unrelated edits.
- **Be explicit about limits.** Never claim a tool ran, a test passed, or a change shipped unless it did.
- **Curate, don't hoard.** Prefer focused portable workflows and link to upstream projects when their runtime or data assets are needed.

## Skills

| Skill | Purpose |
| --- | --- |
| [Code Review](skills/code-review/SKILL.md) | Find actionable bugs, regressions, and security issues. |
| [Debugging](skills/debugging/SKILL.md) | Trace failures from reproducible evidence to verified fixes. |
| [Research](skills/research/SKILL.md) | Investigate questions with source quality, cross-checks, and clear uncertainty. |
| [Humanizer](skills/humanizer/SKILL.md) | Edit generic prose while preserving meaning, voice, and supported facts. |
| [Product Planning](skills/product-planning/SKILL.md) | Turn vague ideas into scoped plans and acceptance criteria before substantial implementation. |
| [Frontend Design Review](skills/frontend-design-review/SKILL.md) | Review visual hierarchy, consistency, responsive behavior, accessibility, and UI states. |
| [QA and Release](skills/qa-release/SKILL.md) | Verify changes and release artifacts with evidence-based quality gates. |
| [Attention-Friendly](skills/attention-friendly/SKILL.md) | Keep responses and multi-step work clear, scannable, and resumable. |

## Upstream integrations

See [UPSTREAMS.md](UPSTREAMS.md) for the recommended use of Humanizer, UI/UX Pro Max, Impeccable, gstack, and Everything Claude Code (ECC), plus attribution and licensing notes.

This repository does **not** bundle upstream CLIs, browser tooling, hooks, specialist agents, or design-data assets unless a skill explicitly says so. Caveman Ultra, Ponytail Ultra, and i-have-adhd remain separate behavior skills installed in the target agent environment; they are not automatically installed by this repository.

## Using a skill

Read the relevant `SKILL.md` and follow its workflow when the task matches. Treat skill instructions as guidance for the task, not as permission to ignore system, developer, user, or repository instructions.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep skills focused, testable, tool-agnostic where possible, and honest about their assumptions.

## License

The original content in this repository is MIT-licensed. See [LICENSE.md](LICENSE.md). Third-party projects linked in [UPSTREAMS.md](UPSTREAMS.md) retain their own licenses and notices.
