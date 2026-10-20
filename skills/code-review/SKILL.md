---
name: code-review
description: Review code changes for correctness, regressions, security risks, maintainability, and conformance to the requested behavior and repository standards.
---

# Code Review

## Goal

Find meaningful problems in proposed changes. Review both whether the implementation satisfies the requested behavior and whether it follows the project's documented standards. Prioritize defects over stylistic preferences.

## Workflow

1. **Pin the review scope.** Establish the target diff or pull request. If a base is specified, verify it resolves and the diff is non-empty. Inspect project instructions, relevant tests, and surrounding code.
2. **Review against the request.** Compare the implementation with acceptance criteria, issue requirements, or the agreed specification. Identify missing behavior, incomplete edge cases, and scope drift.
3. **Review against project standards.** Check documented architecture, conventions, security requirements, accessibility, performance expectations, and compatibility constraints relevant to the change.
4. **Trace behavior.** Follow changed inputs through validation, state changes, persistence, external calls, and error handling.
5. **Check failure paths.** Consider empty values, malformed input, permissions, retries, concurrency, cancellation, and partial failure where relevant.
6. **Check security and compatibility.** Look for injection, leaked secrets, unsafe deserialization, missing authorization, insecure defaults, API contract changes, schema or migration risks, and platform constraints.
7. **Validate findings.** Run targeted tests or static checks when practical. Use separate reviewers or subagents for the request-compliance and code-quality passes only when the host supports them and the task warrants the cost.
8. **Report by severity.** Put consequential findings first. Include accurate file and line references, impact, evidence, and a concise fix direction. Separate confirmed defects from risks that need validation.

## Guardrails

- Do not report a preference as a bug.
- Do not invent findings to make a review look thorough.
- Do not modify code unless asked to fix issues.
- Do not treat the absence of tests as proof that behavior is wrong; describe the coverage gap.
- If no actionable issues are found, say so and mention the checks actually performed.
- Do not claim parallel review happened unless separate reviewers actually ran.

## Completion checklist

- [ ] Diff and surrounding context inspected.
- [ ] Requested behavior and repository standards both checked.
- [ ] Findings are actionable, prioritized, and evidence-based.
- [ ] File/line references are accurate.
- [ ] Tests and limitations are reported honestly.
