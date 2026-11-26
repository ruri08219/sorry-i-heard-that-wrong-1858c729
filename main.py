#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — the apology a smart speaker gives its owner
after mishearing them.

Writes one funny line to /output/entry.txt (gate: UTF-8, 1-140 characters).
Standard library only.

The joke: the owner said "book a flight" and the speaker heard "book a
fight" — one phoneme apart, so the mishearing is plausible, and the speaker
doubles down by treating its owner like a boxer with a weigh-in on Friday.
"""

import os

LINE = "Sorry — I heard 'book a flight' as 'book a fight.' Weigh-in is Friday, champ."

# Gate from the competition rules: entry.txt must be 1-140 UTF-8 characters.
MAX_CHARS = 140


def main():
    line = LINE.strip()
    # One line only: no embedded newline, no control characters.
    assert "\n" not in line and all(ord(c) >= 32 for c in line), (
        "entry must be a single line"
    )
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-140 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
