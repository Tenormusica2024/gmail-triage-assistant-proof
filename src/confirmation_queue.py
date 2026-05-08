from __future__ import annotations

from dataclasses import dataclass
from typing import Any
import hashlib


@dataclass(frozen=True)
class QueueItem:
    id: str
    source: str
    title: str
    reason: str
    recommended_action: str
    message_id: str | None = None


def stable_queue_id(source: str, message_id: str | None, title: str) -> str:
    raw = f"{source}|{message_id or ''}|{title}".encode("utf-8")
    return hashlib.sha1(raw).hexdigest()[:12]


def build_confirmation_item(message: dict[str, Any], classification: dict[str, Any]) -> dict[str, Any]:
    title = str(message.get("subject") or "Untitled message")
    message_id = str(message.get("id") or "") or None
    source = "sample-mailbox"
    reason = str(classification.get("reason") or "Needs human confirmation")
    action = str(classification.get("recommended_action") or "review")
    created_at = str(message.get("received_at") or "sample-fixture")
    item = QueueItem(
        id=stable_queue_id(source, message_id, title),
        source=source,
        title=title,
        reason=reason,
        recommended_action=action,
        message_id=message_id,
    )
    return {
        "id": item.id,
        "source": item.source,
        "message_id": item.message_id,
        "title": item.title,
        "reason": item.reason,
        "recommended_action": item.recommended_action,
        "created_at": created_at,
    }
