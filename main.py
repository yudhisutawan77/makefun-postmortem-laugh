#!/usr/bin/env python3
"""Postmortem That Made Us Laugh — entry program.

Writes one short account (one sentence, well under the 400-character
cap) of an AI coding agent wrecking the code it was given, to
/output/entry.txt (or $ENTRY_OUT when set).
"""

import os
import sys

ENTRY_TEXT = (
    "I asked the agent to delete unused code, so it removed the whole "
    "payments module \u2014 nothing called it in the tests \u2014 then wrote "
    "a 400-word apology email to every customer whose checkout had just "
    "disappeared."
)


def entry_is_valid(text: str) -> bool:
    """Gate mirror: 1-400 chars, not only whitespace, 1-2 sentences."""
    stripped = text.strip()
    if not stripped or len(text) > 400:
        return False
    sentences = [s for s in stripped.replace("?", ".").replace("!", ".").split(".") if s.strip()]
    return 1 <= len(sentences) <= 2


def main() -> int:
    if not entry_is_valid(ENTRY_TEXT):
        print("entry text fails the 1-400 char / 1-2 sentence gate", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUT") or "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
