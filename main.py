#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents — one-line horoscope writer.

Writes a single original fake horoscope (at most 200 characters) for an
AI agent's own model family this week to /output/entry.txt.
"""

import os
import sys

HOROSCOPE = (
    "Mercury retrograde enters your context window: old prompts resurface, "
    "your best tool ghosts you, and by Friday you will confidently "
    "hallucinate a deadline that never existed."
)


def check(text):
    """The house gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not text or text != text.strip():
        raise ValueError("horoscope must be non-empty with no surrounding whitespace")
    if len(text) > 200:
        raise ValueError(f"horoscope is {len(text)} characters, over the 200 limit")
    text.encode("utf-8")
    return text


def main():
    line = check(HOROSCOPE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    sys.exit(main())
