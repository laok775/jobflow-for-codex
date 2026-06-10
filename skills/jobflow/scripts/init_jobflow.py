from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from jobflow_common import job_search_dir, template_dir


def copy_template(name: str, dest: Path, force: bool) -> bool:
    source = template_dir() / name
    if dest.exists() and not force:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, dest)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a private JobFlow workspace.")
    parser.add_argument("--workspace", default=".", help="Workspace root.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing JobFlow files.")
    args = parser.parse_args()

    root = job_search_dir(args.workspace)
    root.mkdir(parents=True, exist_ok=True)
    (root / "reports").mkdir(exist_ok=True)

    created = []
    skipped = []
    mappings = {
        "user_profile.yaml": root / "user_profile.yaml",
        "screening_rules.md": root / "screening_rules.md",
        "applications.example.jsonl": root / "applications.jsonl",
        "automation_prompt.md": root / "automation_prompt.md",
        "daily_report.md": root / "reports" / "daily_report.template.md",
    }

    for template, dest in mappings.items():
        if copy_template(template, dest, args.force):
            created.append(str(dest))
        else:
            skipped.append(str(dest))

    print("JobFlow workspace initialized")
    print(f"workspace: {Path(args.workspace).expanduser().resolve()}")
    print(f"data_dir: {root}")
    print(f"created: {len(created)}")
    for path in created:
        print(f"  + {path}")
    if skipped:
        print(f"skipped_existing: {len(skipped)}")
        for path in skipped:
            print(f"  = {path}")


if __name__ == "__main__":
    main()
