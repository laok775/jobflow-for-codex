# Recruiter Message Rules

Review recruiter messages before new applications.

## Auto-Update to `not_suitable`

If the recruiter clearly says the candidate is not suitable, update the ledger status to `not_suitable`.

Common signals:

- not suitable
- not a match
- temporarily not considering
- experience does not fit
- resume does not fit
- position requirements do not match

Set `status_stage` when clear:

- `after_initial_chat`
- `after_resume`
- `after_interview`

## Auto-Send Resume

Only send a resume when all conditions are true:

- the recruiter clearly asks for a resume, attachment, portfolio, or more materials
- the user has configured an appropriate resume path
- the platform supports sending the configured resume or attachment in the current context
- no CAPTCHA or platform safety check blocks the action

After confirmed send success, update status to `resume_sent`.

## Notify User

Do not auto-reply. Notify the user with message content when the recruiter asks about:

- phone number
- WeChat
- interview time
- salary expectation or negotiation
- availability or start date
- relocation
- custom questions
- ambiguous requests
- anything requiring judgment

Use status `needs_user_action` when the message requires the user.

## Failed Message Handling

If a message is visible but the corresponding conversation cannot be opened:

- do not claim it was handled
- record `needs_review` or `needs_user_action`
- include recruiter, company, timestamp, and visible message content when available
