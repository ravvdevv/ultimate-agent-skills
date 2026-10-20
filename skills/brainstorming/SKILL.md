---
name: brainstorming
description: Resolve material product or technical choices before implementation. Skip for small, clear, reversible tasks.
---

# Brainstorming

## When to use

Use only when important choices remain unresolved, multiple approaches would lead to meaningfully different outcomes, or the cost of building the wrong thing is high. Skip it for small, clear, reversible tasks.

## Workflow

1. Inspect the conversation, repository instructions, and relevant code before asking questions.
2. Separate the desired outcome from the user's proposed solution and identify only uncertainties that change the design.
3. Resolve facts through inspection. Ask the user only about decisions they own or details that cannot be inferred safely.
4. Compare at most a few credible approaches, focusing on trade-offs that affect cost, risk, compatibility, or user experience.
5. Recommend the simplest reversible option that meets the goal; state assumptions, important failure states, security implications, and non-goals.
6. Summarize the proposed behavior and acceptance criteria in a compact, reviewable design.
7. Pause for approval before implementing a substantial or risky design that has not been approved. For clear, low-risk work, state assumptions and proceed when implementation was requested.

## Boundary with product planning

Use this skill to resolve **which approach to take**. Use product-planning when the user needs a **scoped implementation plan** with ordered work, affected areas, risks, and acceptance criteria. Do not run both as separate mandatory ceremonies: combine their useful outputs when a task genuinely needs both.

## Guardrails

- Do not ask questions that repository inspection can answer.
- Do not turn a typo, small bug, or explicit low-risk change into a design workshop.
- A proposed design is not permission for destructive, external, or irreversible actions.
- Do not invent constraints or plan infrastructure for hypothetical future scale.
- Keep depth proportional to the consequences of getting the design wrong.

## Completion checklist

- [ ] Material decisions and trade-offs are visible.
- [ ] Proposed behavior and non-goals are clear.
- [ ] Acceptance criteria can be verified.
- [ ] Confirmation is obtained when risk warrants it.
