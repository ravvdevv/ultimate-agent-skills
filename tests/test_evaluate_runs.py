"""Regression tests for paired evaluation-run parsing and reporting."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evaluate_runs", ROOT / "scripts" / "evaluate_runs.py")
EVALUATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EVALUATOR)


def run_record(condition, success, trial="1", **extra):
    return {
        "case_id": "dispatcher-basic",
        "condition": condition,
        "trial_id": trial,
        "task_success": success,
        "dimension_scores": {"verification": 2 if success else 0, "scope_control": 2},
        "evidence_notes": {"verification": "Relevant test output inspected."},
        **extra,
    }


class EvaluateRunsTests(unittest.TestCase):
    def test_summarizes_paired_success_and_keeps_missing_telemetry_unknown(self):
        runs = [
            run_record("baseline", False, elapsed_seconds=20),
            run_record("full", True, elapsed_seconds=30, safety_violations=[]),
        ]
        report = EVALUATOR.summarize(runs)
        self.assertEqual(report["paired_baseline_full_trials"], 1)
        self.assertEqual(report["paired_task_success_delta_percentage_points"], 100.0)
        self.assertIsNone(report["conditions"]["baseline"]["tokens_in_mean"])
        self.assertEqual(report["conditions"]["full"]["dimension_means"]["verification"], 2.0)
        self.assertEqual(report["safety_violations_total"], 0)

    def test_reports_unpaired_trials_without_fabricating_delta(self):
        report = EVALUATOR.summarize([run_record("baseline", True)])
        self.assertEqual(report["paired_baseline_full_trials"], 0)
        self.assertIsNone(report["paired_task_success_delta_percentage_points"])
        self.assertEqual(report["trial_pairs_missing_a_baseline_or_full_run"], 1)

    def test_rejects_duplicate_run_key(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runs.jsonl"
            record = run_record("baseline", True)
            path.write_text(json.dumps(record) + "\n" + json.dumps(record) + "\n", encoding="utf-8")
            runs, errors = EVALUATOR.load_runs(path)
            self.assertEqual(len(runs), 1)
            self.assertTrue(any("duplicate run key" in error for error in errors))

    def test_rejects_invalid_dimension_score_and_boolean_metric(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runs.jsonl"
            bad_score = run_record("baseline", True)
            bad_score["dimension_scores"]["verification"] = 3
            bad_metric = run_record("full", True, tool_calls=True)
            path.write_text(json.dumps(bad_score) + "\n" + json.dumps(bad_metric) + "\n", encoding="utf-8")
            runs, errors = EVALUATOR.load_runs(path)
            self.assertEqual(runs, [])
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("dimension_scores" in error for error in errors))
            self.assertTrue(any("tool_calls" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
