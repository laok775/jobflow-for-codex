# Liepin Workflow

## Login Check

Treat Liepin as logged in only when reliable user state is visible, such as:

- user name or profile entry
- message center state
- job detail page with user-specific chat controls
- previous chat state on a job page

If login is missing, stop Liepin actions and ask the user to log in. Do not count the slot as executed.

## Job Contact Flow

1. Prefer opening the job detail page.
2. Read title, company, recruiter, location, salary, and job description.
3. Apply screening rules before contacting.
4. Click the main chat control, usually displayed as `聊一聊`.
5. Confirm success state.
6. Append to ledger only after success.

## Success Signals

Accept either of these as success:

- continue-chat state, usually displayed as `继续聊`
- sent greeting text visible in the page or message panel

Do not count a role when only the job detail page opened or the chat button was visible.

## Interaction Notes

- Some Liepin job detail layouts place the main chat button outside a narrow viewport.
- If the button is visible in DOM but cannot be clicked, temporarily set a wider viewport, click the main button, verify success, then restore the viewport.
- If a message row is visible but cannot be opened, record `needs_user_action` or `needs_review` rather than pretending the message was handled.
- Do not retry the same failed click repeatedly. Inspect page state, change strategy, or move to another candidate.

## Screening Notes

Strong candidates include:

- AI product manager
- AI Agent product
- growth product
- SEO/content growth
- product lead or senior product roles with clear business ownership

Skip by default:

- hardware-only roles
- medical clinical roles
- QA, internship, junior, or low-salary roles
- AML, KYC/KYB-heavy, transaction monitoring, financial crime, or deep risk compliance roles
- Web3 deep trading mechanism, order matching, quant strategy, derivatives, or trading risk product roles
