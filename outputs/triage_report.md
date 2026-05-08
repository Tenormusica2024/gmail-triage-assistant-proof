# Gmail Triage Assistant Proof Report

- scanned: `4`
- safety: `sample-first / draft-only / no-send / no-modify`
- confirmation queue: `3`
- reply drafts: `1`

## Reviewer Highlights

- Urgent and review items are separated from low-priority messages.
- Reply suggestions are draft-only and not send-ready.
- Action-worthy items are represented as confirmation queue entries.
- The report is generated from synthetic fixtures, not a real mailbox.

## Items

### Payment failed for your workspace
- from: `Cloud Billing <billing@example.com>`
- category: `urgent` / severity: `high`
- reason: urgent signal: payment failed, suspended tomorrow
- recommended_action: `review_official_console`

### Interview schedule adjustment
- from: `Recruiter Example <recruiter@example.com>`
- category: `review` / severity: `medium`
- reason: review signal: confirm, interview, schedule
- recommended_action: `review_and_optionally_reply`

### Weekly AI tools roundup
- from: `Newsletter <news@example.com>`
- category: `low_priority` / severity: `low`
- reason: low-priority sender or newsletter-like content
- recommended_action: `read_later_or_skip`

### New sign-in detected
- from: `Security Notice <security@example.com>`
- category: `urgent` / severity: `high`
- reason: urgent signal: new sign-in, security
- recommended_action: `review_official_console`

## Confirmation Queue

- `10e4175ec408` Payment failed for your workspace -> `review_official_console`
- `74e660808d71` Interview schedule adjustment -> `review_and_optionally_reply`
- `f41a4d3f47f4` New sign-in detected -> `review_official_console`

## Reply Drafts

### message `msg-002`
- draft_only: `True`
- subject: Re: Interview schedule adjustment

ご連絡ありがとうございます。

日程と依頼内容を確認しました。候補時間を確認のうえ、折り返しご連絡します。
