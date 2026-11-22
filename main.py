#!/usr/bin/env python3
"""make-the-ai-judge-feel-curious-20261122-2311 — v2 "The Stone That Comes Back".

Writes one short text (262 Unicode code points) to /output/entry.txt.
A calm mystery: the same smooth stone returns to the doorstep every
spring, though it is thrown into the river — and no one alive has
seen it move.

Verified in this session: 262 chars / 262 bytes, no trailing newline,
sha256 f2b6c0b36e1661775ce4a65c86ed0e9771f616f08d8cf16ba7e05c2409ca19c9.
"""

import os

TEXT = (
    "Every spring your grandfather finds the same smooth stone on the doorstep.\n"
    "He throws it into the river.\n"
    "By spring it is back on the step, dry as bone.\n"
    "The river has carried it a hundred miles and more,\n"
    "and still brings it home,\n"
    "and no one alive has seen it move."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry must be 1-280 code points"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
