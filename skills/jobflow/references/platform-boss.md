# BOSS Direct Workflow

## Login Check

Treat BOSS Direct as logged in only when the page shows reliable account state such as:

- user name or profile entry
- resume entry
- message entry
- job detail page with user-specific contact controls

If login is missing, stop BOSS actions and ask the user to log in. Do not count the slot as executed.

## Job Contact Flow

1. Prefer opening the job detail page.
2. Read title, company, location, salary, and job description.
3. Apply screening rules before contacting.
4. Click the detail-page `immediate communication` control, usually displayed as `立即沟通`.
5. Confirm success state.
6. Append to ledger only after success.

## Success Signals

Accept either of these as success:

- sent-message confirmation, usually displayed as `已向BOSS发送消息`
- continue-chat state, usually displayed as `继续沟通`

Do not count a role when only the job detail page opened or the contact button was visible.

## Interaction Notes

- List-level contact buttons can point to a different job than the detail panel. Prefer detail pages.
- If Playwright role/text click stalls, read visible DOM and click the exact `立即沟通` node.
- If a page shows duplicate contact controls, scope to the job detail section.
- Do not use blind coordinates unless the exact element bounds were just inspected and no better control path exists.

## Screening Notes

Skip by default:

- low-salary outsourcing roles
- internships or junior roles
- unrelated operations, sales, QA, hardware-only, medical clinical, or compliance-heavy roles
- AML, KYC/KYB-heavy, transaction monitoring, financial crime, or deep risk compliance roles

SEO, AI productization, content growth, lifecycle growth, PLG, referral, activation, retention, and conversion optimization are strong positive signals when they match the user's profile.
