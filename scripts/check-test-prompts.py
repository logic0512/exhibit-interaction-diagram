#!/usr/bin/env python3
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEST_FILE = ROOT / "test-prompts.json"

REQUIRED_TOP_LEVEL = {"schema_version", "purpose", "usage", "cases"}
REQUIRED_CASE_FIELDS = {
    "id",
    "title",
    "mode",
    "user_prompt",
    "space_assumption",
    "must_read",
    "required_visual_assets",
    "pass_criteria",
    "known_failure_to_prevent",
}
ALLOWED_MODES = {"direct_image", "idea_expansion_then_image", "idea_expansion_only"}


def fail(message: str) -> None:
    print(f"FAIL {message}")
    sys.exit(1)


def warn(message: str) -> None:
    print(f"WARN {message}")


def main() -> None:
    if not TEST_FILE.exists():
        fail("test-prompts.json is missing")

    try:
        data = json.loads(TEST_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"test-prompts.json is invalid JSON: {exc}")

    missing = REQUIRED_TOP_LEVEL - set(data)
    if missing:
        fail(f"top-level fields missing: {', '.join(sorted(missing))}")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("cases must be a non-empty list")

    seen_ids = set()
    errors = []

    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(f"case #{index} is not an object")
            continue

        case_id = case.get("id", f"case #{index}")
        missing_case_fields = REQUIRED_CASE_FIELDS - set(case)
        if missing_case_fields:
            errors.append(f"{case_id}: missing fields: {', '.join(sorted(missing_case_fields))}")

        if case_id in seen_ids:
            errors.append(f"{case_id}: duplicate id")
        seen_ids.add(case_id)

        if case.get("mode") not in ALLOWED_MODES:
            errors.append(f"{case_id}: unsupported mode {case.get('mode')!r}")

        if not isinstance(case.get("must_read"), list) or not case.get("must_read"):
            errors.append(f"{case_id}: must_read must be a non-empty list")
        else:
            for rel_path in case["must_read"]:
                if not (ROOT / rel_path).exists():
                    errors.append(f"{case_id}: must_read path does not exist: {rel_path}")

        if not isinstance(case.get("required_visual_assets"), list):
            errors.append(f"{case_id}: required_visual_assets must be a list")
        else:
            for rel_path in case["required_visual_assets"]:
                if not (ROOT / rel_path).exists():
                    errors.append(f"{case_id}: visual asset does not exist: {rel_path}")

        criteria = case.get("pass_criteria")
        if not isinstance(criteria, list) or len(criteria) < 3:
            errors.append(f"{case_id}: pass_criteria must contain at least 3 checks")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        sys.exit(1)

    if len(cases) < 6:
        warn("fewer than 6 regression cases; consider adding more coverage")

    print(f"PASS {len(cases)} regression cases validated")


if __name__ == "__main__":
    main()
