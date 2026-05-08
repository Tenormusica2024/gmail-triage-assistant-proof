# Optional Gmail API Setup

The demo works without Gmail API. Use this only if you want to build a private adapter for your own mailbox.

## Minimal setup outline

1. Create or select a Google Cloud project.
2. Enable the Gmail API.
3. Configure an OAuth consent screen for personal/testing use.
4. Create an OAuth client of type `Desktop app`.
5. Download the client file as `credentials.json`.
6. Store tokens outside the public proof directory.

Recommended local-only locations:

```text
.local/gmail/credentials.json
.local/gmail/token.json
```

Add `.local/` to `.gitignore` before creating real credentials.

## Recommended scopes

Start read-only when possible:

```text
https://www.googleapis.com/auth/gmail.readonly
```

Only use broader scopes such as `gmail.modify` in a private adapter after you intentionally add label/filter/spam operations.

## Public proof rule

Do not make Gmail API required for the public demo. Keep the public proof runnable with `samples/mailbox.json`.
