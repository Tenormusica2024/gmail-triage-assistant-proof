# Public Export Checklist

Use this checklist before moving this proof slice into a standalone public repository.

## Required checks

- The demo runs with only `samples/mailbox.json` and `samples/personal_rules.json`.
- Gmail API setup remains optional.
- No real Gmail token, OAuth client secret, message ID, thread ID, sender, subject, or body is included.
- No private issue or support-ticket content is included.
- No LinkedIn DM content is included.
- No private knowledge-base output is included.
- No local absolute path is required to run the demo.
- Default behavior is still no-send / no-modify.
- Reply output is draft-only.
- Actionable items go to a confirmation queue instead of being executed.

## Suggested export shape

```text
README.md
docs/
samples/
src/
tests/
outputs/triage_report.md
outputs/triage_report.json
```

## Export procedure

Recommended flow:

1. Create a fresh public repository.
2. Copy only the contents of this proof directory into the fresh repository root.
3. Do not copy the parent private repository history.
4. Run the focused tests and sample demo in the fresh repository.
5. Re-run a secret/private-string scan before publishing.

Example from the parent private repository:

```powershell
$src = "public-proof\gmail-triage"
$dst = "C:\path\to\fresh-public-repo"
robocopy $src $dst /E /XD .local __pycache__ .pytest_cache /XF *.pyc
```

Then, inside the fresh public repository:

```powershell
python -m pytest tests -q
python -X utf8 run_demo.py
python scripts/check_public_boundary.py
```

## Pre-export commands

```powershell
python -m pytest tests -q
python -X utf8 run_demo.py
python scripts/check_public_boundary.py
```

If exporting from inside the private repository, copy only this proof directory into a fresh public repository rather than publishing the private repository history.

## Public repository description draft

Short description:

```text
Sample-first AI secretary proof for Gmail-like triage, draft-only replies, and confirmation queues.
```

README tagline:

```text
Classify mailbox-like inputs, draft safe replies, and queue actions for human confirmation without requiring Gmail API.
```
