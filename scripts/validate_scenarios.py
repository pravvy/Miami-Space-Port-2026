#!/usr/bin/env python3
"""Small standard-library validator for repository scenario JSON files."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCENARIO_DIR = ROOT / "scenarios"
REQUIRED = {"schema_version", "scenario_id", "name", "description", "classification", "seed", "initial_state", "events", "expected_outcomes"}
VALID_LIFECYCLES = {"INIT", "NOMINAL", "DEGRADED", "RECOVERY"}
errors = []
files = sorted(SCENARIO_DIR.glob("*.json"))
if not files:
    errors.append("No scenario JSON files found.")
for path in files:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        continue
    missing = REQUIRED - data.keys()
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing keys: {sorted(missing)}")
        continue
    if not isinstance(data["seed"], int):
        errors.append(f"{path.relative_to(ROOT)}: seed must be an integer")
    if not isinstance(data["initial_state"], dict):
        errors.append(f"{path.relative_to(ROOT)}: initial_state must be an object")
    if not isinstance(data["events"], list) or not data["events"]:
        errors.append(f"{path.relative_to(ROOT)}: events must be a non-empty array")
    else:
        last_time = -1
        for index, event in enumerate(data["events"]):
            if not isinstance(event, dict) or not {"at_seconds", "type", "target", "value"} <= event.keys():
                errors.append(f"{path.relative_to(ROOT)}: event {index} has invalid shape")
                continue
            at = event["at_seconds"]
            if not isinstance(at, (int, float)) or at < last_time:
                errors.append(f"{path.relative_to(ROOT)}: event times must be numeric and non-decreasing")
            else:
                last_time = at
            if event["type"] == "LIFECYCLE_TRANSITION" and event["value"] not in VALID_LIFECYCLES:
                errors.append(f"{path.relative_to(ROOT)}: invalid lifecycle state {event['value']}")
    if not isinstance(data["expected_outcomes"], list) or not data["expected_outcomes"]:
        errors.append(f"{path.relative_to(ROOT)}: expected_outcomes must be a non-empty array")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Validated {len(files)} scenario file(s).")
