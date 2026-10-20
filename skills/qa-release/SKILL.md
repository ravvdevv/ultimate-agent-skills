---
name: qa-release
description: Verify a feature or release with risk-based tests, regression checks, and explicit evidence before claiming it is ready. Use before shipping changes, cutting a release, or closing implementation work.
---

# QA and Release

A portable quality gate inspired by common engineering workflows, including gstack and selected engineering practices from ECC. It does not bundle their runtime tools.

## Workflow

1. **Establish the change.** Inspect the diff, project instructions, release notes, versioning rules, and deployment or packaging scripts.
2. **List the risks.** Identify changed user flows, APIs, schemas, authentication boundaries, platform-specific behavior, and destructive operations.
3. **Choose focused checks.** Run the smallest relevant unit, integration, type, lint, build, and end-to-end checks available. Add regression coverage for fixed bugs.
4. **Exercise critical paths.** Test normal, invalid, empty, permission-denied, offline, and failure states when relevant.
5. **Inspect the final diff.** Look for accidental files, secrets, generated artifacts, unrelated edits, debug code, and mismatched version or changelog entries.
6. **Verify release artifacts.** If producing a build, confirm the expected file exists, has plausible size/type, and matches the intended version and platform. Test installation or launch when feasible.
7. **Report evidence.** List each command/check and its actual result. Separate passed, failed, skipped, and not-applicable checks.
8. **Ship only within scope.** Do not publish, deploy, tag, or create a release unless requested or already authorized by the user's explicit task.

## Guardrails

- A successful build is not proof that runtime behavior works.
- Do not say "tested" when only reading code; do not say "released" when only preparing artifacts.
- Never expose secrets in logs, screenshots, or reports.
- For failed checks, provide the failure and next diagnostic step rather than hiding it.

## Completion checklist

- [ ] Relevant tests and build checks were attempted.
- [ ] Final diff and release metadata were reviewed.
- [ ] Artifact verification is reported accurately.
- [ ] Deployment or publication status is explicit.
