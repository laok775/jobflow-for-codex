from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any


CANONICAL_STATUSES = {
    "contacted",
    "resume_sent",
    "interviewed",
    "not_suitable",
    "needs_user_action",
    "needs_review",
}

REQUIRED_FIELDS = [
    "platform",
    "job_title",
    "company",
    "recruiter",
    "location",
    "salary",
    "job_url",
    "status",
    "status_stage",
    "last_action_at",
    "last_reviewed_at",
    "next_follow_up_at",
    "source_slot",
    "notes",
]


def job_search_dir(workspace: str | Path) -> Path:
    return Path(workspace).expanduser().resolve() / "data" / "job_search"


def skill_dir() -> Path:
    return Path(__file__).resolve().parents[1]


def template_dir() -> Path:
    return skill_dir() / "templates"


def read_jsonl(path: str | Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    ledger = Path(path).expanduser().resolve()
    rows: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    if not ledger.exists():
        return rows, [{"line": 0, "error": f"file not found: {ledger}"}]

    text = ledger.read_text(encoding="utf-8-sig")
    for index, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append({"line": index, "error": exc.msg})
            continue
        if not isinstance(value, dict):
            errors.append({"line": index, "error": "line is not a JSON object"})
            continue
        rows.append(value)
    return rows, errors


def write_json(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def iso_day(value: Any) -> str:
    text = str(value or "")
    return text[:10] if len(text) >= 10 else text


def parse_day(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def today_rows(rows: list[dict[str, Any]], day: str) -> list[dict[str, Any]]:
    return [
        row
        for row in rows
        if iso_day(row.get("last_action_at")) == day
        or iso_day(row.get("last_reviewed_at")) == day
    ]


def contacted_rows(rows: list[dict[str, Any]], day: str) -> list[dict[str, Any]]:
    return [
        row
        for row in rows
        if iso_day(row.get("last_action_at")) == day and row.get("status") == "contacted"
    ]


def due_rows(rows: list[dict[str, Any]], day: str) -> list[dict[str, Any]]:
    target = parse_day(day)
    due: list[dict[str, Any]] = []
    for row in rows:
        value = str(row.get("next_follow_up_at") or "").strip()
        if not value:
            continue
        try:
            if parse_day(value[:10]) <= target:
                due.append(row)
        except ValueError:
            continue
    return due


def platform_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    return dict(Counter(str(row.get("platform") or "unknown") for row in rows))


def add_common_ledger_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--ledger",
        default=None,
        help="Path to applications.jsonl. Defaults to <workspace>/data/job_search/applications.jsonl.",
    )
    parser.add_argument(
        "--workspace",
        default=".",
        help="Workspace root used when --ledger is omitted.",
    )


def resolve_ledger(args: argparse.Namespace) -> Path:
    if args.ledger:
        return Path(args.ledger).expanduser().resolve()
    return job_search_dir(args.workspace) / "applications.jsonl"
