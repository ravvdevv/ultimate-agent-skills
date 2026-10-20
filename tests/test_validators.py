"""Regression tests for repository validators; standard library only."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SKILLS_VALIDATOR = load_module("validate_skills", REPO_ROOT / "scripts" / "validate_skills.py")
EVALS_VALIDATOR = load_module("validate_evals", REPO_ROOT / "scripts" / "validate_evals.py")


def valid_skill(name: str = "example-skill") -> str:
    return f"""---
name: {name}
description: A sufficiently descriptive skill for validator tests.
---

# Example

## Workflow

1. Inspect the input.

## Guardrails

- Keep the scope limited.

## Completion checklist

- [ ] Verify the result.
"""


def valid_case(skill: str = "example-skill") -> dict:
    return {
        "id": "case-one",
        "skill": skill,
        "task": "Perform a small, well-scoped task.",
        "expected_behavior": ["Inspect the relevant input."],
        "failure_modes": ["Claims an unperformed check."],
        "dimensions": ["correctness", "verification"],
    }


class ValidatorRegressionTests(unittest.TestCase):
    def run_skill_validator(self, root: Path) -> tuple[int, str]:
        SKILLS_VALIDATOR.ROOT = root
        SKILLS_VALIDATOR.SKILLS_DIR = root / "skills"
        SKILLS_VALIDATOR.ERRORS = []
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            result = SKILLS_VALIDATOR.main()
        return result, output.getvalue()

    def run_eval_validator(self, root: Path) -> tuple[int, str]:
        EVALS_VALIDATOR.ROOT = root
        EVALS_VALIDATOR.CASES_FILE = root / "evals" / "cases.jsonl"
        EVALS_VALIDATOR.errors = []
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            result = EVALS_VALIDATOR.main()
        return result, output.getvalue()

    def test_skill_validator_accepts_valid_skill(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill_dir = root / "skills" / "example-skill"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(valid_skill(), encoding="utf-8")
            (root / "README.md").write_text("[Skill](skills/example-skill/SKILL.md)\n", encoding="utf-8")
            result, output = self.run_skill_validator(root)
            self.assertEqual(result, 0, output)

    def test_skill_validator_rejects_duplicate_metadata_and_broken_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill_dir = root / "skills" / "example-skill"
            skill_dir.mkdir(parents=True)
            malformed = valid_skill().replace(
                "description: A sufficiently descriptive skill for validator tests.",
                "description: A sufficiently descriptive skill for validator tests.\nname: duplicate-name",
            )
            (skill_dir / "SKILL.md").write_text(malformed, encoding="utf-8")
            (root / "README.md").write_text("[Missing](does-not-exist.md)\n", encoding="utf-8")
            result, output = self.run_skill_validator(root)
            self.assertEqual(result, 1)
            self.assertIn("duplicate frontmatter field", output)
            self.assertIn("broken local link", output)

    def test_skill_validator_rejects_directory_without_skill_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "skills" / "empty-skill").mkdir(parents=True)
            result, output = self.run_skill_validator(root)
            self.assertEqual(result, 1)
            self.assertIn("missing SKILL.md", output)

    def test_eval_validator_accepts_valid_case(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "skills" / "example-skill").mkdir(parents=True)
            (root / "skills" / "example-skill" / "SKILL.md").write_text(valid_skill(), encoding="utf-8")
            (root / "evals").mkdir()
            (root / "evals" / "cases.jsonl").write_text(json.dumps(valid_case()) + "\n", encoding="utf-8")
            result, output = self.run_eval_validator(root)
            self.assertEqual(result, 0, output)

    def test_eval_validator_rejects_path_traversal_skill_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "skills").mkdir()
            (root / "evals").mkdir()
            case = valid_case("../outside")
            (root / "evals" / "cases.jsonl").write_text(json.dumps(case) + "\n", encoding="utf-8")
            result, output = self.run_eval_validator(root)
            self.assertEqual(result, 1)
            self.assertIn("kebab-case directory name", output)

    def test_eval_validator_rejects_duplicate_dimensions_and_unknown_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "skills" / "example-skill").mkdir(parents=True)
            (root / "skills" / "example-skill" / "SKILL.md").write_text(valid_skill(), encoding="utf-8")
            (root / "evals").mkdir()
            case = valid_case()
            case["dimensions"] = ["correctness", "correctness"]
            case["unexpected"] = True
            (root / "evals" / "cases.jsonl").write_text(json.dumps(case) + "\n", encoding="utf-8")
            result, output = self.run_eval_validator(root)
            self.assertEqual(result, 1)
            self.assertIn("unknown field", output)
            self.assertIn("must not contain duplicates", output)


if __name__ == "__main__":
    unittest.main()
