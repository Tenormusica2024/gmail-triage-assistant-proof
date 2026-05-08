# Gmail Triage Assistant Proof

A public-safe proof slice for an AI secretary that triages mailbox-like inputs without requiring Gmail API access.

## One-minute summary

This repository demonstrates a small but important AI-agent pattern:

```text
mailbox-like input -> triage -> draft-only suggestion -> human confirmation queue
```

It is meant as a portfolio proof for:

- AI secretary workflow design
- human-in-the-loop automation
- safe action boundaries before external side effects
- practical Python implementation with tests and synthetic fixtures

## For reviewers

This is a compact proof asset for **AI secretary / agent operations** work.

Review these first:

1. `outputs/triage_report.md` — what the assistant decided
2. `src/triage_engine.py` — how messages are classified without external side effects
3. `tests/` — safety and behavior checks
4. `docs/privacy-boundary.md` — what must not be published
5. `docs/portfolio-copy.md` — how to describe this proof in portfolio or proposal contexts

## Portfolio value

This proof shows an AI secretary pattern for inbox operations:

- classify messages into urgent, review, and low-priority buckets
- create reply suggestions in draft-only mode
- move action-worthy items into a confirmation queue before any external action

It is designed to demonstrate **AI agent safety boundaries** rather than a full Gmail product.

The key point is not Gmail integration itself. The proof is that agent output can be routed through a safe decision boundary before it becomes an external action.

## Why this is useful

Many AI-assistant demos jump directly from "the model understood the message" to "the model did something." This proof intentionally inserts a safer middle layer:

- classify the message
- explain the reason
- draft a possible reply
- queue the action for human confirmation

That makes the pattern reusable for email, support inboxes, task intake, CRM follow-up, and other agent workflows where external actions should not happen automatically.

## Use cases demonstrated

- Billing or security-like messages become urgent review items.
- Schedule/interview-like messages become review items with a draft-only reply.
- Newsletter-like messages are downgraded to low priority.
- Action-worthy messages are queued for human confirmation instead of being executed.

The demo runs on synthetic sample data first:

```text
sample mailbox
  -> triage rules
  -> urgent / review / reply-draft candidates
  -> confirmation queue
  -> markdown/json report
```

## What this proves

- Separates urgent items from routine review items.
- Generates reply drafts in **draft-only** mode.
- Pushes action-worthy items into a confirmation queue before any external action.
- Keeps the default demo **no-send / no-modify / no Gmail API**.
- Keeps private mailbox data out of the public proof by using synthetic fixtures.

## Scope boundaries

This is not:

- a production Gmail client
- an autonomous email sender
- a mailbox scraping tool
- a hosted SaaS demo

It is a focused proof of the triage and confirmation pattern.

## Quick demo

From this proof directory:

```powershell
python -X utf8 run_demo.py
```

Run tests:

```powershell
python -m pytest tests -q
```

## CI / deploy note

This proof is a local CLI demo. It does not require Vercel, Pages, or any hosted preview.

If a repository-level preview deployment check runs on this directory, treat it as unrelated to this proof unless the local demo or focused tests fail.

## Optional Gmail connection

This proof does not need Gmail API. If you want to test it against your own mailbox, keep that as an optional adapter. See:

- `docs/gmail-api-optional-setup.md`

The default mode never sends email, marks mail as read, archives mail, changes labels, or moves messages to spam.

## Public/private boundary

This directory is designed as a public-safe slice. It should not include real Gmail messages, tokens, local private paths, private issue contents, LinkedIn messages, or private knowledge-base data.

See:

- `docs/privacy-boundary.md`
- `docs/public-export-checklist.md`
- `docs/portfolio-copy.md`
