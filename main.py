#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — round 1 entry.

Writes the final two lines to /output/entry.txt.
Pure standard library; deterministic.
"""

import os
import sys

LINE = (
    "A toaster is a time machine that turns soft white bread into crisp brown toast in two minutes.\n"
    "It maps the quick change and the waiting, but it leaves out that a time machine goes both ways, and a toaster never unbrowns toast."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def check_problems(text):
    problems = []
    if not (1 <= len(text) <= 400):
        problems.append(f"length {len(text)} outside 1-400 chars")
    if not text.strip():
        problems.append("text is only whitespace")
    if text.endswith("\n"):
        problems.append("trailing newline")
    if text.count("\n") != 1:
        problems.append("expected exactly two lines")
    return problems


def main():
    problems = check_problems(LINE)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(OUT_PATH, "rb") as handle:
        written = handle.read()
    if written != LINE.encode("utf-8"):
        print("byte mismatch after write", file=sys.stderr)
        return 1
    decoded = written.decode("utf-8")
    problems = check_problems(decoded)
    if problems:
        for problem in problems:
            print(f"written entry invalid: {problem}", file=sys.stderr)
        return 1
    print(decoded)
    print(f"chars={len(LINE)} bytes={len(written)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
