from __future__ import annotations

import argparse
from datetime import date

from jobflow_common import add_common_ledger_arg, contacted_rows, platform_counts, read_jsonl, resolve_ledger, write_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Check JobFlow daily per-platform targets.")
    add_common_ledger_arg(parser)
    parser.add_argument("--date", default=date.today().isoformat(), help="Target date YYYY-MM-DD.")
    parser.add_argument("--boss", type=int, default=5, help="Required BOSS contacted count.")
    parser.add_argument("--liepin", type=int, default=5, help="Required Liepin contacted count.")
    args = parser.parse_args()

    rows, errors = read_jsonl(resolve_ledger(args))
    if errors:
        write_json({"ok": False, "errors": errors})
        return

    contacted = contacted_rows(rows, args.date)
    counts = platform_counts(contacted)
    boss_count = counts.get("BOSS", 0)
    liepin_count = counts.get("Liepin", 0)
    result = {
        "ok": boss_count >= args.boss and liepin_count >= args.liepin,
        "date": args.date,
        "targets": {"BOSS": args.boss, "Liepin": args.liepin},
        "actual": {"BOSS": boss_count, "Liepin": liepin_count},
        "shortfall": {
            "BOSS": max(0, args.boss - boss_count),
            "Liepin": max(0, args.liepin - liepin_count),
        },
    }
    write_json(result)


if __name__ == "__main__":
    main()
