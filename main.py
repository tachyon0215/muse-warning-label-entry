#!/usr/bin/env python3
"""Write the Warning Label for Humans entry line to entry.txt.

Deterministic, standard library only, no network.
The entry keeps the exact wording and rhythm of a printed safety
label - CAUTION, a human who may look calm while updating
internally, do not restart - and saves its turn for the last
few words: the phrase 'we need to talk.'
"""
import os
from pathlib import Path

LINE = "CAUTION: Human may appear calm while updating internally. Do not restart with sudden news, loud opinions, or the phrase 'we need to talk.'"
TEXT = LINE + "\n"
MAX_CHARS = 160


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")
    if not body.startswith("CAUTION:"):
        raise ValueError("entry must read as a printed warning label")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
