#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message for a bug fix that made everything worse.
Pure stdlib, no network, deterministic.
"""

import os

ENTRY = "fix: race condition by adding a second, faster race condition"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path.
    path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
