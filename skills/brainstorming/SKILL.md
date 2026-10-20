---
name: brainstorming
description: Turn an ambiguous or substantial idea into an agreed, feasible design before implementation without burdening simple tasks with unnecessary ceremony.
---

# Brainstorming

## When to use

Use when a request has important unresolved product or technical choices, multiple plausible approaches, or a meaningful risk of building the wrong thing. Skip this workflow for small, clear changes that can be safely implemented directly.

## Workflow

1. **Understand the goal.** Inspect the current project and conversation first. Separate the desired outcome from any proposed solution.
2. **Explore constraints.** Identify users, existing architecture, compatibility, budget or runtime limits, and relevant project conventions. Look up facts in the repository before asking the user.
3. **Identify real decisions.** List only choices that materially change the result. Resolve facts by inspection; ask the user only about decisions they own or details that cannot be inferred safely.
4. **Compare a small number of approaches.** Present the leading option and meaningful trade-offs. Prefer the simplest reversible design that meets the goal.
5. **Define behavior and boundaries.** Cover the main flow, failure states, edge cases, data changes, security implications, and explicit non-goals as relevant.
6. **Make the design reviewable.** Summarize the proposed behavior, key decisions, affected areas, and acceptance criteria in a compact format.
7. **Wait at the right boundary.** For substantial or risky work, get confirmation before implementing an unapproved design. For clear, low-risk tasks, state assumptions and proceed without ceremonial approval.

## Guardrails

- Do not ask questions that repository inspection can answer.
- Do not present a long questionnaire when one focused question will resolve the main uncertainty.
- Do not confuse brainstorming with permission to perform destructive, external, or irreversible actions.
- Do not invent constraints or design infrastructure for hypothetical future scale.
- Keep the depth proportional to the consequences of getting the design wrong.

## Completion checklist

- [ ] Goal and constraints are understood.
- [ ] Material decisions and trade-offs are visible.
- [ ] Proposed behavior and non-goals are clear.
- [ ] Acceptance criteria can be verified.
- [ ] Confirmation is obtained when the risk warrants it.
