#!/usr/bin/env python3
"""make-the-ai-judge-feel-curious-20261122-2311 — v1 "The Well".

Writes one short text (267 Unicode code points) to /output/entry.txt.
A calm mystery: a well older than the house whose splash comes back a
breath too late, warm in winter, never dry — and no one remembers who
dug it, or what it is waiting for.

Verified in this session: 267 chars / 267 bytes, no trailing newline,
sha256 d70aa4a96247c247a881adfbbba3a93c2f24e05a48722b242c0551e8d3c1b21c.
"""

import os

TEXT = (
    "The well behind the house is older than the house.\n"
    "Drop a stone in, and the splash comes back a breath too late,\n"
    "as if the water were listening first.\n"
    "The water is warm in winter.\n"
    "It has never once gone dry,\n"
    "and no one remembers who dug it,\n"
    "or what it is waiting for."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry must be 1-280 code points"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
