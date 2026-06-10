from __future__ import annotations

import argparse
from collections import Counter
from datetime import date

from jobflow_common import (
    add_common_ledger_arg,
    contacted_rows,
    due_rows,
    platform_counts,
    read_jsonl,
    resolve_ledger,
    today_rows,
)


def bullet(row: dict) -> str:
    title = row.get("job_title") or "Untitled"
    company = row.get("company") or "Unknown company"
    platform = row.get("platform") or "Unknown platform"
    status = row.get("status") or "unknown"
    return f"- [{platform}] {title} / {company} / {status}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a Markdown JobFlow daily report.")
    add_common_ledger_arg(parser)
    parser.add_argument("--date", default=date.today().isoformat(), help="Report date YYYY-MM-DD.")
    args = parser.parse_args()

    ledger = resolve_ledger(args)
    rows, errors = read_jsonl(ledger)
    if errors:
        print(f"# JobFlow Daily Report - {args.date}\n")
        print("Ledger parse errors:")
        for error in errors:
            print(f"- line {error['line']}: {error['error']}")
        return

    todays = today_rows(rows, args.date)
    contacted = contacted_rows(rows, args.date)
    due = due_rows(rows, args.date)
    status_counts = Counter(str(row.get("status") or "unknown") for row in todays)
    counts = platform_counts(contacted)
    needs_user = [row for row in todays if row.get("status") == "needs_user_action"]

    print(f"# JobFlow Daily Report - {args.date}\n")
    print("## Summary\n")
    print(f"- BOSS contacted: {counts.get('BOSS', 0)}")
    print(f"- Liepin contacted: {counts.get('Liepin', 0)}")
    print(f"- Total contacted: {len(contacted)}")
    print(f"- Status updates: {len(todays) - len(contacted)}")
    print(f"- Resumes sent: {status_counts.get('resume_sent', 0)}")
    print(f"- Needs user action: {len(needs_user)}")

    print("\n## New Contacts\n")
    if contacted:
        for row in contacted:
            print(bullet(row))
    else:
        print("- None")

    print("\n## Message Review\n")
    reviewed = [row for row in todays if row not in contacted]
    if reviewed:
        for row in reviewed:
            print(bullet(row))
    else:
        print("- None")

    print("\n## Follow-Ups Due\n")
    if due:
        for row in due:
            print(bullet(row))
    else:
        print("- None")


if __name__ == "__main__":
    main()
