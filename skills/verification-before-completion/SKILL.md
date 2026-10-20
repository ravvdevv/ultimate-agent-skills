---
name: verification-before-completion
description: Verify claimed work with fresh, relevant evidence before saying a task is fixed, complete, tested, or ready to ship.
---

# Verification Before Completion

## When to use

Use before reporting a coding task as complete, claiming a bug is fixed, summarizing test results, or saying a build or release is ready.

## Workflow

1. **Translate claims into checks.** Identify what must be true for each completion claim, including the user's acceptance criteria.
2. **Choose direct evidence.** Prefer running the relevant test, build, typecheck, lint, command, or user-visible flow over reasoning from the code alone.
3. **Run checks after the final change.** Evidence from before the latest edit does not verify the current result.
4. **Inspect actual outcomes.** Read exit codes and meaningful output. Distinguish a passing check from a command that never ran, timed out, or was skipped.
5. **Cover the changed surface.** Run focused checks first, then broader checks when risk and time justify them. Inspect the final diff for accidental changes.
6. **Report precisely.** Separate verified, failed, skipped, and unverified items. Mention environment limitations and remaining risks.

## Guardrails

- Never fabricate command output, test results, screenshots, or tool execution.
- Do not claim a test passed because it was added or because the implementation looks correct.
- A successful build does not prove runtime behavior; choose evidence appropriate to the claim.
- Do not run destructive checks or publish/deploy artifacts without authorization.
- If verification is blocked, say what was attempted and what evidence is still missing.

## Completion checklist

- [ ] Acceptance criteria map to observable checks.
- [ ] Relevant checks ran after the final change.
- [ ] Results and failures were inspected.
- [ ] Claims match the evidence actually collected.
- [ ] Remaining uncertainty is explicit.
