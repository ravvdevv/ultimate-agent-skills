# Curated skill bundles

Bundles are recommendations, not a separate installer or a promise that every agent will load every skill identically. Use the interactive [skills CLI](https://github.com/vercel-labs/skills) to select the skills you want, then verify the destination and behavior in your agent.

## Build and change code

Use when implementing a feature or fixing a bug:

- `brainstorming` — clarify material choices before substantial work.
- `product-planning` — scope larger changes and define acceptance criteria.
- `test-driven-development` — drive behavior changes through tests.
- `debugging` — isolate causes before applying fixes.
- `verification-before-completion` — verify the final state before reporting completion.

For small, well-specified changes, skip planning steps that add no value. These skills should guide judgment, not create ceremony.

## Review and release

Use when reviewing changes or preparing a release:

- `code-review` — find actionable correctness, security, and regression issues.
- `qa-release` — run risk-based checks and assess release readiness.
- `verification-before-completion` — ensure claims match fresh evidence.

## Frontend quality

Use when building or polishing user interfaces:

- `frontend-design-review` — assess responsive behavior, accessibility, interaction states, and visual quality.
- `code-review` — catch implementation-level regressions.
- `verification-before-completion` — verify the resulting UI and report limitations.

For deeper design-system generation or specialized UI commands, use the linked upstream tools in [UPSTREAMS.md](UPSTREAMS.md); this repository does not bundle their external data or runtimes.

## Research and writing

Use when investigating a question or refining user-facing prose:

- `research` — use credible sources and communicate uncertainty.
- `humanizer` — improve naturalness without changing meaning.
- `verification-before-completion` — check factual claims and distinguish verified details from assumptions.

## Focus and resumability

Use for longer tasks that are easy to lose track of:

- `attention-friendly` — break work into manageable steps and make it easy to resume.
- `product-planning` — maintain a clear scope and definition of done.
- `verification-before-completion` — leave a concise, evidence-based handoff.

## Selection rules

- Install only what fits your workflow. More skills can add conflicting or redundant instructions.
- Prefer one primary workflow skill for the task and add specialist skills only when needed.
- Review the skills before installing them in a sensitive repository.
- Confirm the agent actually discovers the installed skills; file placement alone does not prove runtime compatibility.
