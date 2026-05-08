from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from confirmation_queue import build_confirmation_item
from reply_draft import build_reply_draft


def load_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def normalize_text(value: Any) -> str:
    return str(value or "").lower()


def sender_email(sender: str) -> str:
    if "<" in sender and ">" in sender:
        return sender.split("<", 1)[1].split(">", 1)[0].strip().lower()
    return sender.strip().lower()


def contains_any(text: str, keywords: list[str]) -> list[str]:
    lowered = text.lower()
    return [kw for kw in keywords if kw.lower() in lowered]


def classify_message(message: dict[str, Any], rules: dict[str, Any]) -> dict[str, Any]:
    text = " ".join(
        normalize_text(message.get(key))
        for key in ("sender", "subject", "snippet", "body")
    )
    sender = sender_email(str(message.get("sender") or ""))

    urgent_hits = contains_any(text, list(rules.get("urgent_keywords") or []))
    review_hits = contains_any(text, list(rules.get("review_keywords") or []))
    reply_hits = contains_any(text, list(rules.get("reply_draft_keywords") or []))

    protected = sender in {str(v).lower() for v in rules.get("protected_senders", [])}
    low_sender = sender in {str(v).lower() for v in rules.get("low_priority_senders", [])}

    if urgent_hits or protected and any(k in text for k in ("failed", "security", "suspended", "sign-in")):
        return {
            "category": "urgent",
            "severity": "high",
            "reason": f"urgent signal: {', '.join(urgent_hits[:3]) or 'protected sender with risk signal'}",
            "recommended_action": "review_official_console",
            "reply_draft_candidate": bool(reply_hits),
        }

    if review_hits:
        return {
            "category": "review",
            "severity": "medium",
            "reason": f"review signal: {', '.join(review_hits[:3])}",
            "recommended_action": "review_and_optionally_reply",
            "reply_draft_candidate": bool(reply_hits),
        }

    if low_sender or "newsletter" in text or "roundup" in text:
        return {
            "category": "low_priority",
            "severity": "low",
            "reason": "low-priority sender or newsletter-like content",
            "recommended_action": "read_later_or_skip",
            "reply_draft_candidate": False,
        }

    return {
        "category": "review",
        "severity": "medium",
        "reason": "uncertain; keep for human review",
        "recommended_action": "review",
        "reply_draft_candidate": False,
    }


def build_report(messages: list[dict[str, Any]], rules: dict[str, Any]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    queue: list[dict[str, Any]] = []
    drafts: list[dict[str, Any]] = []

    for message in messages:
        classification = classify_message(message, rules)
        row = {
            "message": {
                "id": message.get("id"),
                "sender": message.get("sender"),
                "subject": message.get("subject"),
                "received_at": message.get("received_at"),
            },
            "classification": classification,
        }
        rows.append(row)

        if classification["category"] in {"urgent", "review"}:
            queue.append(build_confirmation_item(message, classification))
        if classification.get("reply_draft_candidate"):
            drafts.append({
                "message_id": message.get("id"),
                "draft": build_reply_draft(message, classification),
            })

    counts: dict[str, int] = {}
    for row in rows:
        cat = row["classification"]["category"]
        counts[cat] = counts.get(cat, 0) + 1

    return {
        "summary": {
            "messages_scanned": len(messages),
            "counts": counts,
            "confirmation_queue_count": len(queue),
            "reply_draft_count": len(drafts),
            "safety": "sample-first / draft-only / no-send / no-modify",
        },
        "items": rows,
        "confirmation_queue": queue,
        "reply_drafts": drafts,
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Gmail Triage Assistant Proof Report",
        "",
        f"- scanned: `{report['summary']['messages_scanned']}`",
        f"- safety: `{report['summary']['safety']}`",
        f"- confirmation queue: `{report['summary']['confirmation_queue_count']}`",
        f"- reply drafts: `{report['summary']['reply_draft_count']}`",
        "",
        "## Reviewer Highlights",
        "",
        "- Urgent and review items are separated from low-priority messages.",
        "- Reply suggestions are draft-only and not send-ready.",
        "- Action-worthy items are represented as confirmation queue entries.",
        "- The report is generated from synthetic fixtures, not a real mailbox.",
        "",
        "## Items",
        "",
    ]
    for row in report["items"]:
        msg = row["message"]
        cls = row["classification"]
        lines.extend([
            f"### {msg.get('subject')}",
            f"- from: `{msg.get('sender')}`",
            f"- category: `{cls.get('category')}` / severity: `{cls.get('severity')}`",
            f"- reason: {cls.get('reason')}",
            f"- recommended_action: `{cls.get('recommended_action')}`",
            "",
        ])

    lines.extend(["## Confirmation Queue", ""])
    for item in report["confirmation_queue"]:
        lines.extend([
            f"- `{item['id']}` {item['title']} -> `{item['recommended_action']}`",
        ])
    if not report["confirmation_queue"]:
        lines.append("- none")

    lines.extend(["", "## Reply Drafts", ""])
    for draft in report["reply_drafts"]:
        lines.extend([
            f"### message `{draft['message_id']}`",
            f"- draft_only: `{draft['draft']['draft_only']}`",
            f"- subject: {draft['draft']['subject']}",
            "",
            draft["draft"]["body"],
            "",
        ])
    if not report["reply_drafts"]:
        lines.append("- none")

    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Sample-first Gmail triage proof")
    parser.add_argument("--mailbox", required=True)
    parser.add_argument("--rules", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--json-out", required=True)
    args = parser.parse_args(argv)

    messages = load_json(args.mailbox)
    rules = load_json(args.rules)
    report = build_report(messages, rules)

    out = Path(args.out)
    json_out = Path(args.json_out)
    out.parent.mkdir(parents=True, exist_ok=True)
    json_out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_markdown(report), encoding="utf-8")
    json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out}")
    print(f"wrote {json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
