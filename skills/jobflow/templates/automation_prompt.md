JobFlow automation has started. First read the current local date and time in the user's timezone from `user_profile.yaml`.

Read:

- `<workspace>/data/job_search/user_profile.yaml`
- `<workspace>/data/job_search/screening_rules.md`
- `<workspace>/data/job_search/applications.jsonl`

If the current local minute is 00 and the current local hour is configured in `automation.execution_hours_local`, run the execution slot:

1. Confirm login state for every enabled platform.
2. Only process platforms confirmed logged in.
3. Review recruiter messages before new applications.
4. If a recruiter clearly says the user is not suitable, update ledger status to `not_suitable`.
5. If a recruiter clearly requests a resume and a matching resume path is configured, send the resume through the platform when possible and update status to `resume_sent`.
6. If a recruiter asks for phone, WeChat, interview time, salary details, availability, relocation, or any complex question, do not reply automatically. Notify the user with the message content.
7. Screen jobs against `screening_rules.md`.
8. Contact the configured per-slot target count for each enabled platform.
9. Append a ledger row only after visible platform success state.
10. Report login state, message review count, status updates, resumes sent, user-action messages, per-platform contacted counts, and blockers.

If the current local minute is configured in `automation.inspection_minutes`, run the inspection slot:

1. Read the ledger.
2. Check cumulative targets for the day.
3. Notify the user immediately if a platform is short or blocked.
4. Do not apply, send resumes, or reply to messages during inspection.

Never bypass CAPTCHA, anti-bot controls, paywalls, or platform safety checks.
