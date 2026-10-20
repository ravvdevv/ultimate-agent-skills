---
name: frontend-design-review
description: Plan or review a frontend for visual hierarchy, coherent design tokens, responsive behavior, accessibility, and interaction quality. Use when building or polishing a web or app interface.
---

# Frontend Design Review

Use this as a portable review workflow. For richer design-system selection, consult UI/UX Pro Max; for visual critique and implementation-specific polish, consult Impeccable. Their full assets and commands are not bundled here.

## Workflow

1. **Understand the product.** Identify users, primary task, platform, existing brand, and the page's main action. Inspect the current UI before replacing it.
2. **Set visual direction.** Define a small palette, type scale, spacing rhythm, density, surface treatment, and interaction states. Reuse existing tokens unless there is a clear reason to change them.
3. **Check hierarchy.** Make the primary action and important information obvious. Remove decorative elements that compete with the task.
4. **Check consistency.** Look for mismatched radii, spacing, typography, icon styles, button variants, and repeated components. Avoid nested cards and generic template styling without a product reason.
5. **Check all states.** Include hover/focus/pressed, disabled, loading, empty, error, success, and long-content states where relevant.
6. **Check responsive behavior.** Test narrow and wide layouts, overflow, touch targets, keyboard navigation, reduced motion, and text scaling.
7. **Check accessibility.** Verify semantic controls, labels, contrast, focus visibility, and status announcements.
8. **Validate in the actual UI.** Run the app and use available browser or screenshot tooling. Compare before/after at the same viewport. Do not claim visual verification if no rendered UI was inspected.
9. **Report focused changes.** Fix the highest-impact problems first; avoid a full redesign when targeted edits solve the issue.

## Guardrails

- Do not invent user research or claim a design is validated by users without evidence.
- Do not add gradients, animation, or extra cards just to make the screen look more elaborate.
- Preserve product functionality and existing design constraints.
- If using external design tools, follow their current official installation and license guidance.

## Completion checklist

- [ ] Primary task and visual hierarchy are clear.
- [ ] Existing design system is reused or changes are justified.
- [ ] Responsive and accessibility concerns are checked.
- [ ] Important interaction states are covered.
- [ ] Visual verification status is explicit.
