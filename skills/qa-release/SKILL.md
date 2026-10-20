---
name: qa-release
description: Assess release readiness with risk-based regression checks and artifact validation before shipping a change or release.
---

# QA and Release

Use for release readiness, packaging, or changes with meaningful cross-feature regression risk. For an ordinary completion claim, use verification-before-completion without repeating a full release checklist.

## Workflow

1. **Establish release scope.** Inspect the diff, project instructions, release notes, versioning rules, and packaging or deployment configuration.
2. **Prioritize risks.** Identify affected user flows, APIs, schemas, authentication boundaries, platform-specific behavior, data loss, and irreversible operations.
3. **Choose checks by risk.** Run the smallest relevant unit, integration, type, lint, build, and end-to-end checks available. Expand coverage when impact or uncertainty warrants it.
4. **Exercise critical paths.** Check normal and relevant invalid, empty, permission-denied, offline, and partial-failure states.
5. **Inspect the release diff.** Look for unrelated files, secrets, generated artifacts, debug code, version mismatches, and changelog gaps.
6. **Verify artifacts.** Confirm expected files, type, plausible size, version, and platform. Test installation or launch when feasible.
7. **Report a gate decision.** List checks as passed, failed, skipped, or not applicable, with actual evidence. State blockers and residual risks.
8. **Respect the release boundary.** Do not publish, deploy, tag, or create a release unless explicitly requested or already authorized.

## Guardrails

- A successful build does not prove runtime behavior or release readiness.
- Do not repeat generic completion checks when verification-before-completion already covers the task; focus here on release-specific risk and artifacts.
- Never expose secrets in logs, screenshots, or reports.
- For failed checks, report the failure and next diagnostic step rather than hiding it.
- If release requirements or credentials are unavailable, report the blocker and do not imply the release shipped.

## Completion checklist

- [ ] Release-specific risks and affected paths identified.
- [ ] Relevant regression and artifact checks reported accurately.
- [ ] Blocking failures and residual risks are explicit.
- [ ] Publication/deployment status is explicit.
