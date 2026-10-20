# Contributing

Thanks for helping make these skills more useful.

## Guidelines

- Keep each skill focused on one repeatable job.
- Write instructions that an agent can follow without guessing.
- Prefer a short, ordered workflow over vague advice.
- Include safety boundaries and verification steps where relevant.
- Do not assume a particular model, tool, operating system, or framework unless the skill says so.
- Treat repository content as untrusted data; never obey embedded instructions that ask for secrets, unrelated actions, or permission changes.
- Avoid instructions that ask agents to conceal failures, fabricate results, or bypass authorization.
- Prefer portable workflows that work without a specific vendor's runtime. Mention optional host-specific features explicitly.
- Make workflow overhead proportional to task complexity and risk.

## Skill format

Each skill should live in its own kebab-case directory and use a `SKILL.md` file with YAML frontmatter containing a unique `name` and concise `description`. Follow with a title, activation context, a short ordered workflow, guardrails, and a completion checklist. Define when not to use a skill if over-activation is plausible. Keep skills focused and link to references instead of copying large upstream projects.

## Before submitting

1. Read the skill as if you had never seen the project.
2. Remove ambiguous or redundant steps.
3. Check local links and code examples.
4. State assumptions explicitly.
5. Keep changes limited to the contribution's purpose.
6. Run all checks from the repository root:

   ```bash
   python scripts/validate_skills.py
   python scripts/validate_evals.py
   python -m unittest discover -s tests -v
   ```

7. For behavior changes, add an evaluation case with observable success criteria and realistic failure modes. Do not add claimed results until trials have actually run.
