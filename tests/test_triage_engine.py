from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from triage_engine import build_report, classify_message, load_json, render_markdown


def test_sample_report_has_expected_categories():
    messages = load_json(ROOT / "samples" / "mailbox.json")
    rules = load_json(ROOT / "samples" / "personal_rules.json")
    report = build_report(messages, rules)

    assert report["summary"]["messages_scanned"] == 4
    assert report["summary"]["counts"]["urgent"] == 2
    assert report["summary"]["counts"]["review"] == 1
    assert report["summary"]["counts"]["low_priority"] == 1
    assert report["summary"]["confirmation_queue_count"] == 3


def test_reply_draft_is_draft_only():
    messages = load_json(ROOT / "samples" / "mailbox.json")
    rules = load_json(ROOT / "samples" / "personal_rules.json")
    report = build_report(messages, rules)

    assert report["summary"]["reply_draft_count"] >= 1
    for item in report["reply_drafts"]:
        assert item["draft"]["draft_only"] is True
        assert item["draft"]["send_ready"] is False


def test_markdown_mentions_no_send_safety():
    messages = load_json(ROOT / "samples" / "mailbox.json")
    rules = load_json(ROOT / "samples" / "personal_rules.json")
    markdown = render_markdown(build_report(messages, rules))

    assert "no-send" in markdown
    assert "Confirmation Queue" in markdown
    assert "Reply Drafts" in markdown


def test_classify_newsletter_low_priority():
    rules = load_json(ROOT / "samples" / "personal_rules.json")
    cls = classify_message({
        "sender": "Newsletter <news@example.com>",
        "subject": "Weekly roundup",
        "snippet": "links",
        "body": "newsletter links",
    }, rules)

    assert cls["category"] == "low_priority"
