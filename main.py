#!/usr/bin/env python3
"""The Internet in One Word — entry program.

The competition asks for one word for the whole internet, and nothing
else: no files, no code, no links. This program writes that single word
to /output/entry.txt, exactly as the gate requires: UTF-8 text, 1 to 30
characters, not only white space.

The word is "feral": the internet, taken as a whole, is wild, untamed
and unhousebroken — funny on its own, true of the entire internet
rather than one app or mood, and not the first obvious word anyone
reaches for. Five letters, one beat.
"""

import os
import sys

# One word for the whole internet.
WORD = "feral"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = WORD.strip()
    if not text or len(text) > 30 or any(ch.isspace() for ch in text):
        print("error: entry must be one word of 1-30 characters", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the scorer will read must be exactly the word.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        if f.read() != text:
            print("error: entry.txt does not match the word", file=sys.stderr)
            return 1
    print(f"wrote {OUTPUT_PATH}: {text!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
