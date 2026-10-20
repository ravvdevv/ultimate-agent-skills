---
name: code-review
description: Review code changes for correctness, regressions, security risks, and maintainability. Use when asked to review a diff, pull request, patch, or implementation.
---

# Code Review

## Goal

Find meaningful problems in the proposed changes. Prioritize defects over stylistic preferences.

## Workflow

1. **Establish scope.** Inspect the diff, surrounding code, project instructions, and relevant tests. Do not assume the diff tells the whole story.
2. **Trace behavior.** Follow changed inputs through validation, state changes, persistence, external calls, and error handling.
3. **Check failure paths.** Consider empty values, malformed input, permissions, retries, concurrency, cancellation, and partial failure where relevant.
4. **Check security.** Look for injection, leaked secrets, unsafe deserialization, missing authorization, insecure defaults, and sensitive data in logs.
5. **Check compatibility.** Inspect callers, API contracts, schema changes, migrations, and platform constraints.
6. **Validate findings.** Run targeted tests or static checks when practical. Do not claim a defect without a concrete path or evidence.
7. **Report by severity.** Put the most consequential findings first. Include file and line references, impact, and a concise reproduction or fix direction.

## Guardrails

- Do not report a preference as a bug.
- Do not invent findings to make a review look thorough.
- Do not modify code unless asked to fix issues.
- If no actionable issues are found, say so and mention the checks actually performed.
- Clearly distinguish confirmed defects from risks that need validation.

## Completion checklist

- [ ] Diff and surrounding context inspected.
- [ ] Findings are actionable and prioritized.
- [ ] File/line references are accurate.
- [ ] Tests and limitations are reported honestly.
