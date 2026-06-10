<div align="center">

# JobFlow for Codex

A local Codex workflow for job screening, recruiter messages, application ledgers, and daily reports.

[简体中文](README.md) | [English](README.en.md)

[![Codex Workflow](https://img.shields.io/badge/Codex-Workflow-111827)](#)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB)](#prerequisites)
[![Windows Tested](https://img.shields.io/badge/Windows-tested-0078D4)](#compatibility)
[![License MIT](https://img.shields.io/badge/License-MIT-3DA639)](LICENSE)

</div>

---

JobFlow for Codex is a local job-search workflow for Codex. It organizes job discovery, screening, recruiter contact, message review, resume sending, progress tracking, and daily reports into reusable templates, scripts, and Codex skill instructions.

It is designed for users who want Codex to assist with repetitive job-search workflows on platforms such as BOSS Direct and Liepin. It is not a mass-application bot and does not bypass CAPTCHA, login, platform risk controls, or safety checks.

## What You Can Do With It

- Initialize a private local job-search workspace.
- Maintain an `applications.jsonl` application ledger.
- Store screening rules in `screening_rules.md`.
- Ask Codex to screen roles against your rules.
- Ask Codex to review recruiter messages and classify them.
- Generate daily job-search reports.
- Generate reviewable automation prompts for scheduled runs.

## When To Use It

- You are actively searching for jobs.
- You want a regular daily application and follow-up rhythm.
- You want a local record of contacted, resume-sent, rejected, and pending roles.
- You want Codex to handle repetitive workflow steps while keeping human judgment in the loop.

## Prerequisites

- Codex installed locally.
- Python 3.10 or newer.
- Logged-in browser sessions for supported job platforms if you want Codex to operate websites.
- Local resume file paths configured if you want resume sending support.
- Reviewed automation prompts if you want scheduled runs.

## Compatibility

This project has only been self-tested on Windows with local Codex workflows. Other operating systems, browser-control setups, or automation modes may work, but you should verify and adapt them yourself.

## Quick Start

Clone the repository:

```bash
git clone https://github.com/laok775/jobflow-for-codex.git
cd jobflow-for-codex
```

Initialize your private workspace:

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

Then edit:

- `user_profile.yaml`: target roles, cities, platforms, and resume paths.
- `screening_rules.md`: priorities, must-apply signals, and exclusions.

## Common Commands

Validate the ledger:

```bash
python skills/jobflow/scripts/validate_ledger.py --workspace /path/to/your/workspace
```

Generate a daily report:

```bash
python skills/jobflow/scripts/summarize_day.py --workspace /path/to/your/workspace --date 2026-01-01
```

Check daily targets:

```bash
python skills/jobflow/scripts/check_targets.py --workspace /path/to/your/workspace --date 2026-01-01 --boss 5 --liepin 5
```

Build an automation prompt:

```bash
python skills/jobflow/scripts/build_automation_prompt.py --workspace /path/to/your/workspace --output /path/to/your/workspace/data/job_search/automation_prompt.generated.md
```

## Where User Input Is Required

JobFlow is not fully unattended. User intervention is required when:

- You need to log in to job platforms.
- A CAPTCHA, risk control, or safety confirmation appears.
- A recruiter asks for WeChat, phone, salary details, availability, or interview time.
- A recruiter asks a question that requires personal judgment.
- You enable scheduled automation and need to review the generated prompt.
- A platform UI changes and Codex cannot confirm success state.

## Message Handling

Codex can help classify messages, but should not make judgment-heavy replies for you:

- Clearly unsuitable: set status to `not_suitable`.
- Resume requested: send the configured resume when possible and set status to `resume_sent`.
- Judgment required: set status to `needs_user_action`.
- Unclear or unconfirmed: set status to `needs_review`.

## Status Values

The ledger uses:

- `contacted`
- `resume_sent`
- `interviewed`
- `not_suitable`
- `needs_user_action`
- `needs_review`

## Where Data Is Stored

Your real data stays in your own workspace, for example:

```text
/path/to/your/workspace/data/job_search/
```

This repository contains only the plugin, templates, and scripts. It should not contain real resumes, account data, cookies, sessions, or real application records.

## Project Contents

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

Main parts:

- `SKILL.md`: workflow instructions for Codex.
- `references/`: platform notes, message rules, and screening guidance.
- `templates/`: user profile, screening rules, ledger, report, and automation prompt templates.
- `scripts/`: initialization, ledger validation, report generation, target checks, and prompt generation.

## Supported Platforms

- BOSS Direct
- Liepin

More platforms can be added later through new references and workflow rules.

## Limitations

- Does not bypass CAPTCHA or platform risk controls.
- Does not guarantee that a platform allows automation.
- Does not guarantee job-search outcomes.
- Platform UI changes may require workflow updates.
- Complex recruiter messages still require user judgment.

## Acknowledgements

- Thanks to OpenAI Codex for enabling local agent workflows.
- Thanks to the [Linux.do](https://linux.do/) community for discussion, feedback, and support.
- Thanks to job platforms such as BOSS Direct and Liepin for providing job-search and recruiter communication services.
- The README presentation style is inspired by open-source projects such as [CoCo Downloader](https://github.com/markcxx/coco-downloader).

## Disclaimer

1. This project is for personal job-search productivity, learning, and technical research only. It is not a platform bypass tool or bulk-application bot.
2. Users are responsible for following local laws, platform terms of service, and account safety rules.
3. This project does not bypass CAPTCHA, login, risk controls, safety confirmations, or platform restrictions.
4. This project does not guarantee screening accuracy, message classification accuracy, application outcomes, or interview opportunities.
5. Users should review automation prompts, screening rules, message handling results, and resume content before relying on them.
6. This project is not officially affiliated with, authorized by, or endorsed by BOSS Direct, Liepin, OpenAI, or other third-party platforms or companies.
7. If any project content affects your rights, please contact the maintainers through GitHub Issues.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
