# JobFlow for Codex

JobFlow for Codex is a local, browser-assisted job-search workflow plugin for Codex. It helps a user initialize private job-search files, maintain a JSONL application ledger, apply screening rules, generate daily reports, and build reviewed automation prompts.

It is an assistant workflow, not an unattended mass-application bot. It does not bypass CAPTCHA, anti-bot controls, paywalls, or platform safety checks.

## What It Includes

- A Codex skill: `jobflow`
- Platform notes for BOSS Direct and Liepin
- Recruiter message handling rules
- Screening rule guidance
- Templates for private user setup
- Python scripts for local ledger validation, reports, target checks, and automation prompt generation

## What It Does Not Include

- Personal resumes
- Platform accounts, cookies, sessions, or credentials
- Real application ledgers
- Any guaranteed platform integration
- Any CAPTCHA or anti-bot bypass

## Repository Layout

```text
.codex-plugin/
  plugin.json
skills/
  jobflow/
    SKILL.md
    references/
    scripts/
    templates/
```

## Quick Start

Clone the repository and initialize a private workspace:

```bash
python skills/jobflow/scripts/init_jobflow.py --workspace /path/to/your/workspace
```

This creates:

```text
/path/to/your/workspace/data/job_search/
  user_profile.yaml
  screening_rules.md
  applications.jsonl
  automation_prompt.md
  reports/
```

Edit `user_profile.yaml` and `screening_rules.md` with your own job-search preferences and resume paths.

## Validate the Ledger

```bash
python skills/jobflow/scripts/validate_ledger.py --workspace /path/to/your/workspace
```

## Generate a Daily Report

```bash
python skills/jobflow/scripts/summarize_day.py --workspace /path/to/your/workspace --date 2026-01-01
```

## Check Daily Targets

```bash
python skills/jobflow/scripts/check_targets.py --workspace /path/to/your/workspace --date 2026-01-01 --boss 5 --liepin 5
```

## Build an Automation Prompt

```bash
python skills/jobflow/scripts/build_automation_prompt.py --workspace /path/to/your/workspace --output /path/to/your/workspace/data/job_search/automation_prompt.generated.md
```

Review the generated prompt before enabling any recurring automation.

## Canonical Status Values

Scripts use portable canonical values:

- `contacted`
- `resume_sent`
- `interviewed`
- `not_suitable`
- `needs_user_action`
- `needs_review`

Localized display labels can be added by downstream users, but shared tooling should rely on the canonical values.

## Privacy Rules

Before pushing this repository to GitHub:

- Do not commit real resumes.
- Do not commit account credentials, cookies, browser sessions, or tokens.
- Do not commit a real `applications.jsonl`.
- Do not commit a real `user_profile.yaml`.
- Keep private runtime data in your own workspace, not in the plugin repository.

The included `.gitignore` blocks the most common private files, but you should still inspect `git status` and run a secret scan before publishing.

## Supported Platforms in MVP

- BOSS Direct
- Liepin

Other platforms can be added later through new platform reference files and updated workflow instructions.

## License

Add a license before public distribution.
