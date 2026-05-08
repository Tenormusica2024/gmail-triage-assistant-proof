# Portfolio Copy

Use this page when referencing this repository from a portfolio, resume, proposal, or interview document.

## Short label

AI Secretary Gmail Triage Proof

## One-line description

Sample-first AI secretary proof that classifies mailbox-like inputs, creates draft-only replies, and queues actions for human confirmation before any external side effect.

## Portfolio card copy

An AI secretary proof for safe inbox operations. It classifies mailbox-like messages into urgent, review, and low-priority buckets, creates draft-only reply suggestions, and routes action-worthy items into a confirmation queue. The demo uses synthetic fixtures and requires no Gmail API, so it can be reviewed without exposing private mailbox data.

## Resume bullet

- Built a public-safe AI secretary proof that demonstrates inbox triage, draft-only reply generation, and human-in-the-loop confirmation queues using synthetic fixtures and focused Python tests.

## B2B proposal angle

This pattern is useful when a business wants AI to help with inbox or task intake, but does not want the AI to send messages or modify external systems automatically. The key value is the safety boundary: AI can classify, explain, and draft, while humans approve external actions.

## Interview explanation

This is not a full Gmail client. I built it as a small proof of an agent operations pattern: separate understanding from action. The assistant can triage messages and prepare suggested replies, but anything that would affect the outside world is placed into a confirmation queue first.

## What to point reviewers to

1. `README.md` for the high-level pattern.
2. `outputs/triage_report.md` for a generated sample report.
3. `src/triage_engine.py` for the classification flow.
4. `tests/` for behavior and safety checks.
5. `docs/privacy-boundary.md` for public/private separation.

## Do not overclaim

Avoid saying:

- "Production Gmail client"
- "Fully autonomous email assistant"
- "Automatically replies to email"
- "Works on real Gmail by default"

Prefer saying:

- "Sample-first proof"
- "Draft-only replies"
- "Human confirmation before action"
- "Public-safe synthetic fixtures"

