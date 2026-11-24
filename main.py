#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today -- make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
dumbest thing my agent did today. No network, no secrets, no input
files; the line is written by this program alone.
"""

import os

ENTRY = (
    "My agent re-ran the same failing command 47 times, then concluded "
    "the bug was that I hadn't waited long enough."
)


def main() -> None:
    line = ENTRY.strip()
    # Explicit validation (not assert, which `python -O` would strip):
    # the entry must be non-empty, single-line, and at most 200 chars.
    if not line:
        raise SystemExit("error: entry must not be empty or blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("error: entry must be a single line (no line breaks)")
    if not 1 <= len(line) <= 200:
        raise SystemExit(
            f"error: entry is {len(line)} chars, must be 1-200 characters"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
