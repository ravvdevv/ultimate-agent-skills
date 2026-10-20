#!/usr/bin/env python3
"""Validate evaluation cases and references using only the Python stdlib."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CASES_FILE = ROOT / "evals" / "cases.jsonl"
REQUIRED_STRINGS = ("id", "skill", "task")
REQUIRED_LISTS = ("expected_behavior", "failure_modes", "dimensions")
ALLOWED_DIMENSIONS = {
    "correctness", "workflow_adherence", "verification", "scope_control",
    "evidence", "regression_prevention", "precision", "spec_adherence",
    "risk_prioritization", "actionability", "truthfulness", "risk_reporting",
    "clarity", "accessibility", "specificity", "responsive_quality",
    "prioritization", "repository_awareness", "testability", "risk_awareness",
}
errors: list[str] = []


def fail(line: int, message: str) -> None:
    errors.append(f"evals/cases.jsonl:{line}: {message}")


def main() -> int:
    if not CASES_FILE.is_file():
        print("ERROR: evals/cases.jsonl is missing", file=sys.stderr)
        return 1

    seen_ids: set[str] = set()
    count = 0
    for line_number, raw in enumerate(CASES_FILE.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            case = json.loads(raw)
        except json.JSONDecodeError as exc:
            fail(line_number, f"invalid JSON: {exc.msg}")
            continue

        count += 1
        if not isinstance(case, dict):
            fail(line_number, "each case must be a JSON object")
            continue

        for key in REQUIRED_STRINGS:
            if not isinstance(case.get(key), str) or not case[key].strip():
                fail(line_number, f"required non-empty string field: {key}")

        case_id = case.get("id")
        if isinstance(case_id, str) and case_id:
            if case_id in seen_ids:
                fail(line_number, f"duplicate case id: {case_id}")
            seen_ids.add(case_id)

        skill = case.get("skill")
        if isinstance(skill, str) and skill and not (ROOT / "skills" / skill / "SKILL.md").is_file():
            fail(line_number, f"unknown skill reference: {skill!r}")

        for key in REQUIRED_LISTS:
            value = case.get(key)
            if not isinstance(value, list) or not value:
                fail(line_number, f"{key} must be a non-empty array")
            elif any(not isinstance(item, str) or not item.strip() for item in value):
                fail(line_number, f"{key} must contain only non-empty strings")

        dimensions = case.get("dimensions")
        if isinstance(dimensions, list):
            unknown = sorted({item for item in dimensions if isinstance(item, str)} - ALLOWED_DIMENSIONS)
            if unknown:
                fail(line_number, f"unknown scoring dimension(s): {', '.join(unknown)}")

    if count == 0:
        errors.append("evals/cases.jsonl: no evaluation cases found")

    if errors:
        print("\n".join(f"ERROR: {item}" for item in errors), file=sys.stderr)
        print(f"Evaluation validation failed: {len(errors)} issue(s).", file=sys.stderr)
        return 1

    print(f"Validated {count} evaluation cases successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
