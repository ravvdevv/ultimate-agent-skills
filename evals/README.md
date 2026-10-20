# Skill evaluations

This directory contains small, reviewable task cases for checking whether a skill guides an agent toward the intended behavior. These are **evaluation prompts and rubrics**, not results or a claim that the skills have already improved a model.

## Files

- `cases.jsonl`: one JSON object per line. Each case references an existing skill directory and defines a task, expected behavior, failure modes, and scoring dimensions.
- `../scripts/validate_evals.py`: offline structural checks for the dataset and skill references.

## Run the offline checks

From the repository root:

```bash
python scripts/validate_skills.py
python scripts/validate_evals.py
```

Both checks use the Python standard library and do not require API keys, network access, external scanners, or agent CLIs.

## Manual A/B evaluation

To measure skill lift rather than merely validate file structure:

1. Choose a case and record the agent, model/version, repository state, date, and relevant configuration.
2. Run the task without the target skill. Use a clean, equivalent workspace and the same task prompt.
3. Reset to the same starting state and run it with only the target skill enabled.
4. Keep tool permissions, model settings, time budget, and available context as consistent as possible.
5. Score both outputs against the case's expected behavior, failure modes, and dimensions. Prefer evidence from diffs, test output, commands, and observed behavior over stylistic impressions.
6. Repeat stochastic tasks when practical. Record failures and uncertainty rather than cherry-picking the best run.
7. Publish the task set, scoring rubric, model/runtime details, and raw observations before making comparative claims.

Use a simple 0–2 scale per dimension: **0** = absent or materially wrong; **1** = partially met; **2** = met with observable evidence. Report each dimension and the with-skill minus without-skill difference. Do not collapse a tiny sample into a universal quality claim.

## Live evaluation and security

For larger-scale paired trials, consider [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) and its [documentation](https://docs.nvidia.com/skills/skillevaluator). It separates static validation/security checks, semantic overlap detection, and live agent evaluation. Treat it as an optional external tool: pin and review the version, check its current requirements, and run untrusted skills in an appropriate sandbox. Live trials may require model credentials, agent runtimes, and sandbox resources, and can incur costs.

A passing structural check is not a security certification. Before installing or recommending a skill, inspect its instructions and any scripts or linked downloads for unexpected network access, secret access, destructive commands, privilege escalation, and attempts to override the user's intent. Do not execute a skill merely because it passed validation.

## Adding cases

- Keep tasks concrete and plausible.
- Include both positive expectations and recognizable failure modes.
- Ensure each case names an existing `skills/<name>/SKILL.md`.
- Prefer observable outcomes over preferences about writing style.
- Do not add fabricated scores, benchmark results, or claims of model improvement.
