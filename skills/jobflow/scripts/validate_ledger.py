from __future__ import annotations

import argparse
from collections import Counter

from jobflow_common import (
    CANONICAL_STATUSES,
    REQUIRED_FIELDS,
    add_common_ledger_arg,
    read_jsonl,
    resolve_ledger,
    write_json,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a JobFlow applications JSONL ledger.")
    add_common_ledger_arg(parser)
    args = parser.parse_args()

    ledger = resolve_ledger(args)
    rows, parse_errors = read_jsonl(ledger)
    validation_errors = []
    seen_urls: Counter[str] = Counter()

    for index, row in enumerate(rows, start=1):
        missing = [field for field in REQUIRED_FIELDS if field not in row]
        if missing:
            validation_errors.append({"line": index, "error": "missing_fields", "fields": missing})
        status = row.get("status")
        if status not in CANONICAL_STATUSES:
            validation_errors.append({"line": index, "error": "unsupported_status", "status": status})
        url = str(row.get("job_url") or "").strip()
        if url:
            seen_urls[url] += 1

    duplicates = [{"job_url": url, "count": count} for url, count in seen_urls.items() if count > 1]
    result = {
        "ledger": str(ledger),
        "ok": not parse_errors and not validation_errors,
        "rows": len(rows),
        "parse_errors": parse_errors,
        "validation_errors": validation_errors,
        "duplicate_urls": duplicates,
    }
    write_json(result)


if __name__ == "__main__":
    main()
