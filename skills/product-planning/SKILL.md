---
name: product-planning
description: Turn an unclear product idea or feature request into a scoped, testable implementation plan before coding. Use when starting a project, making a substantial feature, or deciding what not to build.
---

# Product Planning

A portable planning workflow inspired by public agent-development practices, including gstack. It does not require gstack's scripts or runtime.

## Workflow

1. **Restate the outcome.** Identify the user, their problem, the expected behavior, and how success will be observed.
2. **Challenge the premise.** Check whether the request solves the actual problem. Surface the highest-impact assumption instead of generating a giant questionnaire.
3. **Define the smallest useful version.** Separate must-haves, later improvements, and explicit non-goals.
4. **Map the current system.** Inspect repository instructions, architecture, relevant files, existing patterns, tests, dependencies, and deployment constraints before proposing changes.
5. **Design the behavior.** Cover the primary flow, empty/loading/error states, permissions, persistence, accessibility, and relevant edge cases.
6. **Choose a reversible approach.** Prefer the smallest design that fits existing conventions. Call out migrations, public API changes, and irreversible operations.
7. **Define verification.** Specify tests, commands, and observable outcomes that would prove the work is done.
8. **Write the plan.** List ordered steps, likely files or modules, risks, dependencies, and acceptance criteria. For a small task, skip ceremony and act directly.

## Guardrails

- Ask only for information that materially changes the plan; otherwise state a reasonable assumption.
- Do not plan speculative infrastructure for hypothetical future scale.
- Do not treat planning as permission to change files. Follow the user's requested execution scope.
- Keep the plan proportional to task size.

## Completion checklist

- [ ] Outcome and acceptance criteria are concrete.
- [ ] Scope and non-goals are explicit.
- [ ] Existing codebase was inspected where available.
- [ ] Risks and verification steps are included.
