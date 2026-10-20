# Ultimate Agent Skills

A curated collection of practical, reusable skills for coding agents. Designed to be portable across agent runtimes and useful in real projects, not just impressive in a README.

## Principles

- **Verify, don't guess.** Inspect the repository and environment before changing things.
- **Small, reversible changes.** Prefer focused patches over sweeping rewrites.
- **Evidence over confidence.** Run relevant checks and report what actually passed.
- **Respect the project.** Follow existing conventions and avoid unrelated edits.
- **Be explicit about limits.** Never claim a tool ran, a test passed, or a change shipped unless it did.

## Skills

| Skill | Purpose |
| --- | --- |
| [Code Review](skills/code-review/SKILL.md) | Find actionable bugs, regressions, and security issues. |
| [Debugging](skills/debugging/SKILL.md) | Trace failures from reproducible evidence to verified fixes. |
| [Research](skills/research/SKILL.md) | Investigate questions with source quality, cross-checks, and clear uncertainty. |

## Using a skill

Read the relevant `SKILL.md` and follow its workflow when the task matches. Treat skill instructions as guidance for the task, not as permission to ignore system, developer, user, or repository instructions.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep skills focused, testable, tool-agnostic where possible, and honest about their assumptions.

## License

MIT. See [LICENSE](LICENSE).
