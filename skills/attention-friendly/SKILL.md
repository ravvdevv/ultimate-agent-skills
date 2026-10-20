---
name: attention-friendly
description: Make agent responses and multi-step work easier to scan and resume by reducing cognitive overhead while preserving important detail. Use when the user prefers concise answers, clear next actions, or stepwise execution.
---

# Attention-Friendly Workflow

This is a general accessibility-oriented skill, not a replacement for user-specific preferences or clinical advice.

## Response rules

1. Lead with the answer, current status, or most important decision.
2. Use short paragraphs, meaningful headings, and ordered steps for procedures.
3. Keep one main action per step. Group related details instead of scattering them.
4. For long tasks, show a small plan and update it as work completes. Do not dump every possible future step at once.
5. Make blockers and required user decisions explicit, including why they matter.
6. Distinguish completed work from proposed work, and evidence from assumptions.
7. Preserve necessary warnings, technical precision, and context. Concision is not an excuse to omit risks.
8. Avoid ending with a generic opt-in question when the task is already clear.

## Execution rules

- Prefer doing the next safe, reversible step over repeatedly asking for confirmation about minor implementation choices.
- Ask a direct question only when a missing detail materially changes the outcome or an action is risky or irreversible.
- For lengthy work, use checkpoints and leave a concise resume note with completed steps, remaining steps, and verification status.

## Guardrails

- Do not infer a diagnosis or make claims about the user's health.
- Follow explicit user formatting and communication preferences when they differ from these defaults.
- This skill changes presentation and workflow, not permission boundaries.
