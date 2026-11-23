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
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert line.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
