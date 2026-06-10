from __future__ import annotations

import argparse
from pathlib import Path

from jobflow_common import job_search_dir, template_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a JobFlow automation prompt for review.")
    parser.add_argument("--workspace", default=".", help="Workspace root.")
    parser.add_argument("--output", default="", help="Optional output file.")
    args = parser.parse_args()

    root = job_search_dir(args.workspace)
    template = (template_dir() / "automation_prompt.md").read_text(encoding="utf-8")
    prompt = template.replace("<workspace>", str(Path(args.workspace).expanduser().resolve()))
    prompt += "\n\nWorkspace files:\n"
    prompt += f"- Profile: {root / 'user_profile.yaml'}\n"
    prompt += f"- Screening rules: {root / 'screening_rules.md'}\n"
    prompt += f"- Ledger: {root / 'applications.jsonl'}\n"

    if args.output:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(prompt, encoding="utf-8")
        print(f"Wrote automation prompt: {output}")
    else:
        print(prompt)


if __name__ == "__main__":
    main()
