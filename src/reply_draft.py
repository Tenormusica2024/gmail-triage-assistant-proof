from __future__ import annotations

from typing import Any


def build_reply_draft(message: dict[str, Any], classification: dict[str, Any]) -> dict[str, Any]:
    """Build a deterministic draft-only reply. This never sends email."""
    subject = str(message.get("subject") or "")
    sender = str(message.get("sender") or "the sender")
    category = classification.get("category")

    if category == "urgent":
        body = (
            "ご連絡ありがとうございます。内容を確認しました。\n\n"
            "安全のため、本文中のリンクからではなく公式画面から状況を確認します。\n"
            "必要な対応が終わり次第、改めて連絡します。"
        )
    else:
        body = (
            "ご連絡ありがとうございます。\n\n"
            "日程と依頼内容を確認しました。候補時間を確認のうえ、折り返しご連絡します。"
        )

    return {
        "draft_only": True,
        "send_ready": False,
        "to_hint": sender,
        "subject": f"Re: {subject}" if subject and not subject.lower().startswith("re:") else subject,
        "body": body,
        "safety_note": "This is a draft-only suggestion. Review before sending.",
    }
