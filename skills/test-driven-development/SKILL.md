---
name: test-driven-development
description: Implement behavior changes with a red-green-refactor loop and regression tests where practical.
---

# Test-Driven Development

## When to use

Use for bug fixes, behavior changes, and new logic where expected behavior can be expressed as a test. For visual, exploratory, or infrastructure tasks where a useful automated test is not practical, choose an appropriate verification method instead.

## Workflow

1. **Understand the behavior.** Inspect project instructions, current implementation, existing tests, and the failure or acceptance criteria.
2. **Choose the smallest testable seam.** Prefer existing interfaces and test conventions over introducing new abstractions just to enable a test.
3. **Write a focused failing test.** Cover the expected behavior or regression. Run it and confirm it fails for the intended reason.
4. **Implement the minimum change.** Make the test pass without unrelated refactoring or speculative features.
5. **Run the focused test again.** Confirm the original failure is resolved and the test now passes.
6. **Refactor if useful.** Keep behavior covered, improve clarity, and avoid abstraction without a concrete benefit.
7. **Run nearby regression checks.** Expand to related tests, typechecks, lint, or build based on the change's risk.
8. **Report evidence.** State which tests ran and their actual results. Do not imply full-suite coverage if only a focused test ran.

## Guardrails

- Follow the repository's test framework and conventions.
- Do not change or weaken a test merely to make the implementation pass unless the expectation itself is demonstrably wrong.
- Avoid brittle tests coupled to implementation details when observable behavior can be tested.
- If a failing test cannot reasonably be created, explain why and use the strongest practical alternative.
- Never claim a test passed without running it.

## Completion checklist

- [ ] Expected behavior is explicit.
- [ ] A focused test failed for the expected reason, when practical.
- [ ] The implementation makes the test pass.
- [ ] Relevant regression checks ran.
- [ ] Test limitations are reported honestly.
