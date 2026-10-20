---
name: debugging
description: Diagnose a software failure systematically, identify its root cause, implement a focused fix when requested, and verify the result.
---

# Debugging

## Workflow

1. **Capture the failure.** Record the exact error, expected behavior, actual behavior, environment, and steps to reproduce.
2. **Inspect before editing.** Read project instructions, relevant code, recent changes, logs, and configuration. Avoid speculative rewrites.
3. **Form a testable hypothesis.** Identify the smallest explanation that fits the evidence and a check that could disprove it.
4. **Narrow the cause.** Reproduce the failure and isolate the responsible layer. Change one meaningful variable at a time when feasible.
5. **Fix the root cause.** Prefer the smallest robust change. Avoid swallowing exceptions, disabling checks, or hardcoding a workaround without justification.
6. **Verify.** Run the reproduction and relevant tests. Add a regression test when appropriate.
7. **Review the patch.** Inspect the final diff for unrelated edits, resource leaks, unsafe behavior, and new edge cases.
8. **Summarize.** Explain cause, change, verification, and anything still unverified.

## Guardrails

- Never claim a fix works solely because it looks plausible.
- Preserve user changes and existing project conventions.
- Do not delete data, reset state, or run destructive commands without explicit authorization.
- If reproduction is impossible, state the evidence and uncertainty rather than pretending otherwise.

## Completion checklist

- [ ] Root cause supported by evidence, or uncertainty clearly stated.
- [ ] Focused fix made only when requested.
- [ ] Relevant checks run and results captured.
- [ ] Remaining risks communicated.
