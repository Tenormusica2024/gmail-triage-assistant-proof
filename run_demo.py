from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from triage_engine import build_report, load_json, render_markdown  # noqa: E402


def main() -> int:
    mailbox = ROOT / "samples" / "mailbox.json"
    rules = ROOT / "samples" / "personal_rules.json"
    output_dir = ROOT / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    report = build_report(load_json(mailbox), load_json(rules))
    report_md = output_dir / "triage_report.md"
    report_json = output_dir / "triage_report.json"

    report_md.write_text(render_markdown(report), encoding="utf-8")
    report_json.write_text(
        __import__("json").dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"wrote {report_md.relative_to(ROOT)}")
    print(f"wrote {report_json.relative_to(ROOT)}")
    print("safety: sample-first / draft-only / no-send / no-modify")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

