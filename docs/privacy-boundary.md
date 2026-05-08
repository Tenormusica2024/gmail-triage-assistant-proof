# Privacy Boundary

This proof slice is sample-first and public-safe by default.

## Safe to publish

- Synthetic mailbox fixtures under `samples/`
- Generic personal rules
- Deterministic triage logic
- Draft-only reply examples
- Confirmation queue examples
- Markdown/JSON reports generated from synthetic data

## Do not publish

- `gmail_token.json`
- `credentials.json`
- Real Gmail message IDs or thread IDs
- Real senders, subjects, or message bodies
- LinkedIn DM contents
- Private issue or support-ticket contents
- Local scheduler state
- Private knowledge-base outputs
- Local absolute paths that reveal private environment details

## Default safety model

The default demo is:

- no Gmail API
- no external send
- no label mutation
- no archive/delete/spam operation
- no automatic reply

Actions are represented as queue items so a user can review them before doing anything externally.
