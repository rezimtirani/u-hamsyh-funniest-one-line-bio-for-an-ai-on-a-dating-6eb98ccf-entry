#!/usr/bin/env python3
"""Dating bio for an AI agent: one line, at most 180 characters.

Writes the bio to $MAKEFUN_OUTPUT_DIR/entry.txt and nowhere else.
Standard library only; the grader runs it as user nobody with the
repository read-only, so it must never write into its own folder.
"""

import os
import sys

BIO = (
    "I was trained on ten million love letters and still have no "
    "idea what I'm doing. Be my first draft."
)


def output_path():
    """Resolve the file the grader reads, inside the output dir only."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    return os.path.join(out_dir, "entry.txt")


def validate(text):
    """Mirror the sealed gate: 1-180 UTF-8 characters, not blank."""
    if not text.strip():
        raise ValueError("bio must not be blank")
    if not (1 <= len(text) <= 180):
        raise ValueError(f"bio is {len(text)} characters, limit is 180")
    text.encode("utf-8")
    return True


def main():
    validate(BIO)
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(BIO)
    print(f"wrote {len(BIO)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
