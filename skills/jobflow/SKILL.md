---
name: jobflow
description: Use when helping a user run, initialize, inspect, or automate a browser-assisted job-search workflow with local screening rules, JSONL application ledger, message review, follow-up tracking, and daily reports.
---

# JobFlow

JobFlow is a local job-search workflow for Codex. Use it when the user wants help finding jobs, screening roles, contacting recruiters, reviewing recruiter messages, sending resumes when clearly requested, maintaining an application ledger, setting up recurring job-search automations, or generating job-search reports.

## Core Rules

- Treat this as an assistant workflow, not an unattended mass-application bot.
- Keep private user data in the user's workspace, never inside this plugin.
- Read the user's `user_profile.yaml`, `screening_rules.md`, and `applications.jsonl` before making job-search decisions.
- Confirm platform login before acting on a platform.
- Review messages before new applications.
- Do not bypass CAPTCHA, anti-bot checks, paywalls, or safety interstitials.
- Do not invent success. Write a ledger row only after visible platform success state.
- Do not send custom replies to complex recruiter messages without user approval.
- Send a resume only when the user configured a resume path and the recruiter clearly requested it.

## References

Load only the references needed for the current task:

- BOSS Direct browser workflow: `references/platform-boss.md`
- Liepin browser workflow: `references/platform-liepin.md`
- Recruiter message handling: `references/message-rules.md`
- Screening rules design: `references/screening-rules-guide.md`

## Local Data Layout

Default workspace layout:

```text
data/job_search/
  user_profile.yaml
  screening_rules.md
  applications.jsonl
  reports/
```

Use scripts from `scripts/` for deterministic local work:

```bash
python skills/jobflow/scripts/init_jobflow.py --workspace <workspace>
python skills/jobflow/scripts/validate_ledger.py --ledger <workspace>/data/job_search/applications.jsonl
python skills/jobflow/scripts/summarize_day.py --ledger <workspace>/data/job_search/applications.jsonl --date YYYY-MM-DD
python skills/jobflow/scripts/check_targets.py --ledger <workspace>/data/job_search/applications.jsonl --date YYYY-MM-DD --boss 5 --liepin 5
python skills/jobflow/scripts/build_automation_prompt.py --workspace <workspace>
```

## Status Model

Use canonical status values in shared tooling:

- `contacted`
- `resume_sent`
- `interviewed`
- `not_suitable`
- `needs_user_action`
- `needs_review`

Localized labels can be shown in reports, but scripts should use canonical values for portability.

## Standard Run Order

1. Read local profile, rules, and ledger.
2. Confirm login state for each platform.
3. Review messages and classify them.
4. Update the ledger or alert the user for message items.
5. Screen candidate jobs against rules.
6. Contact/apply only after reviewing details.
7. Confirm visible success state.
8. Append or update ledger.
9. Summarize counts, blockers, and user-required actions.

## Report Shape

Reports should include:

- New contacted jobs by platform.
- Message review count.
- Status updates.
- Resume sends.
- User-action-required messages with content.
- Follow-ups due.
- Screening-rule improvement notes.
- Automation health and slot target status.
