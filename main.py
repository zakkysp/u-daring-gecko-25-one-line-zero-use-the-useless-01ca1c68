#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes one original one-liner (at most 200 characters) describing a
hilariously useless superpower to /output/entry.txt, or to
$OUTPUT_DIR/entry.txt when OUTPUT_DIR is set.

Stdlib only. Deterministic, no network, no randomness: every run
produces byte-identical output.
"""

import os

LINE = "I can read minds, but only my own, and only the thoughts I already had."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
