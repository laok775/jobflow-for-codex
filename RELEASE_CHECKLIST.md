# GitHub Release Checklist

Use this checklist before pushing JobFlow for Codex to a public repository.

## Privacy

- [ ] `git status --short` contains no resume files.
- [ ] `git status --short` contains no real `applications.jsonl`.
- [ ] `git status --short` contains no real `user_profile.yaml`.
- [ ] No account names, phone numbers, WeChat IDs, emails, cookies, sessions, tokens, or credentials are present.
- [ ] No local absolute paths to private files are present.
- [ ] No real recruiter messages or application records are present.

## Suggested Scans

Run from the repository root:

```bash
rg -n "password|token|secret|cookie|session|credential|authorization|bearer|api[_-]?key|resume|简历|C:/Users|C:\\\\Users|/Users/|applications\\.jsonl|user_profile\\.yaml" .
```

Review every match manually. Some matches are expected in documentation and templates, but no private values should appear.

## Validation

```bash
python /path/to/validate_plugin.py .
python -m py_compile skills/jobflow/scripts/*.py
python skills/jobflow/scripts/init_jobflow.py --workspace /tmp/jobflow-test
python skills/jobflow/scripts/validate_ledger.py --workspace /tmp/jobflow-test
python skills/jobflow/scripts/summarize_day.py --workspace /tmp/jobflow-test --date 2026-01-01
python skills/jobflow/scripts/check_targets.py --workspace /tmp/jobflow-test --date 2026-01-01 --boss 1 --liepin 1
python skills/jobflow/scripts/build_automation_prompt.py --workspace /tmp/jobflow-test
```

## Distribution Notes

- Keep the plugin repository generic.
- Keep private runtime data outside the repository.
- Tell users to review automation prompts before enabling recurring tasks.
- Tell users this workflow does not bypass platform safety checks.
