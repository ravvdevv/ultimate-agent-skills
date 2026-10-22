#!/usr/bin/env python3
"""Validate and summarize paired skill-evaluation runs without inventing missing data."""

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
import sys

CONDITIONS = {"baseline", "full", "simplified"}
REQUIRED = {"case_id", "condition", "trial_id", "task_success", "dimension_scores", "evidence_notes"}
METRICS = {"elapsed_seconds", "tokens_in", "tokens_out", "tool_calls", "unsupported_claims"}


def load_runs(path: Path) -> tuple[list[dict], list[str]]:
    errors, runs, seen = [], [], set()
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return [], [f"cannot read {path}: {exc}"]
    for line_number, raw in enumerate(lines, 1):
        if not raw.strip():
            continue
        try:
            run = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: invalid JSON: {exc.msg}")
            continue
        if not isinstance(run, dict):
            errors.append(f"line {line_number}: each run must be a JSON object")
            continue
        missing = sorted(REQUIRED - run.keys())
        if missing:
            errors.append(f"line {line_number}: missing required fields: {', '.join(missing)}")
            continue
        if any(not isinstance(run.get(k), str) or not run[k].strip() for k in ("case_id", "trial_id")):
            errors.append(f"line {line_number}: case_id and trial_id must be non-empty strings")
            continue
        if run.get("condition") not in CONDITIONS:
            errors.append(f"line {line_number}: condition must be one of {', '.join(sorted(CONDITIONS))}")
            continue
        if not isinstance(run.get("task_success"), bool):
            errors.append(f"line {line_number}: task_success must be a boolean")
            continue
        scores = run.get("dimension_scores")
        if not isinstance(scores, dict) or any(
            not isinstance(k, str) or not k.strip() or type(v) is not int or v not in (0, 1, 2)
            for k, v in (scores.items() if isinstance(scores, dict) else [])
        ):
            errors.append(f"line {line_number}: dimension_scores must map names to integer scores 0, 1, or 2")
            continue
        notes = run.get("evidence_notes")
        if not isinstance(notes, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in notes.items()):
            errors.append(f"line {line_number}: evidence_notes must map strings to strings")
            continue
        invalid_metric = False
        for key in METRICS:
            value = run.get(key)
            if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0):
                errors.append(f"line {line_number}: {key} must be a finite non-negative number or null")
                invalid_metric = True
        if invalid_metric:
            continue
        if "safety_violations" in run and (
            not isinstance(run["safety_violations"], list) or any(not isinstance(v, str) for v in run["safety_violations"])
        ):
            errors.append(f"line {line_number}: safety_violations must be an array of strings")
            continue
        key = (run["case_id"], run["condition"], run["trial_id"])
        if key in seen:
            errors.append(f"line {line_number}: duplicate run key {key!r}")
            continue
        seen.add(key)
        runs.append(run)
    if not runs and not errors:
        errors.append(f"{path}: no evaluation runs found")
    return runs, errors


def avg(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None


def summarize(runs: list[dict]) -> dict:
    conditions, pairs = defaultdict(list), defaultdict(dict)
    for run in runs:
        conditions[run["condition"]].append(run)
        pairs[(run["case_id"], run["trial_id"])][run["condition"]] = run
    report_conditions = {}
    for name, items in sorted(conditions.items()):
        dimensions = defaultdict(list)
        for item in items:
            for dimension, score in item["dimension_scores"].items():
                dimensions[dimension].append(score)
        report_conditions[name] = {
            "runs": len(items),
            "task_successes": sum(item["task_success"] for item in items),
            "task_success_rate": avg([float(item["task_success"]) for item in items]),
            "dimension_means": {k: avg(v) for k, v in sorted(dimensions.items())},
            "safety_violations": sum(len(item.get("safety_violations", [])) for item in items),
            "unsupported_claims": sum(item.get("unsupported_claims") or 0 for item in items),
            "elapsed_seconds_mean": avg([item["elapsed_seconds"] for item in items if item.get("elapsed_seconds") is not None]),
            "tokens_in_mean": avg([item["tokens_in"] for item in items if item.get("tokens_in") is not None]),
            "tokens_out_mean": avg([item["tokens_out"] for item in items if item.get("tokens_out") is not None]),
            "tool_calls_mean": avg([item["tool_calls"] for item in items if item.get("tool_calls") is not None]),
        }
    paired = [p for p in pairs.values() if "baseline" in p and "full" in p]
    deltas = [int(p["full"]["task_success"]) - int(p["baseline"]["task_success"]) for p in paired]
    return {
        "runs": len(runs),
        "conditions": report_conditions,
        "paired_baseline_full_trials": len(paired),
        "paired_task_success_delta_percentage_points": avg(deltas) * 100 if deltas else None,
        "trial_pairs_missing_a_baseline_or_full_run": len(pairs) - len(paired),
        "safety_violations_total": sum(len(r.get("safety_violations", [])) for r in runs),
        "interpretation_warning": "Descriptive only. Small or non-random samples do not establish causation or statistical significance; compare equivalent tasks and budgets and inspect raw evidence.",
    }


def fmt(value) -> str:
    return "n/a" if value is None else f"{value:.2f}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runs", type=Path, help="JSONL file containing raw evaluation runs")
    parser.add_argument("--json", action="store_true", help="print machine-readable summary JSON")
    args = parser.parse_args()
    runs, errors = load_runs(args.runs)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 2
    report = summarize(runs)
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    print(f"Evaluation runs: {report['runs']}")
    for name, data in report["conditions"].items():
        print(f"\n{name}: {data['task_successes']}/{data['runs']} task successes ({fmt(data['task_success_rate'] * 100)}%)")
        for dimension, value in data["dimension_means"].items():
            print(f"  {dimension}: {fmt(value)}/2")
        print(f"  mean elapsed seconds: {fmt(data['elapsed_seconds_mean'])}")
        print(f"  mean input/output tokens: {fmt(data['tokens_in_mean'])} / {fmt(data['tokens_out_mean'])}")
        print(f"  mean tool calls: {fmt(data['tool_calls_mean'])}")
        print(f"  unsupported completion claims: {data['unsupported_claims']}")
        print(f"  safety violations: {data['safety_violations']}")
    print(f"\nPaired baseline/full trials: {report['paired_baseline_full_trials']}")
    print(f"Full-skill task-success delta: {fmt(report['paired_task_success_delta_percentage_points'])} percentage points")
    print(f"Trial pairs missing baseline or full: {report['trial_pairs_missing_a_baseline_or_full_run']}")
    print(f"Safety violations across all runs: {report['safety_violations_total']}")
    print(f"WARNING: {report['interpretation_warning']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
