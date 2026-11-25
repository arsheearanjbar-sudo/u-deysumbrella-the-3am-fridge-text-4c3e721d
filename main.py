# SPDX-License-Identifier: MIT
# The 3AM Fridge Text — a deterministic one-line text writer.
#
# The program writes exactly one line to /output/entry.txt: the text
# message a smart fridge sends its owner at 3am. No network, no model,
# no clock, no randomness — the same line every run, byte for byte.

import os

LINE = (
    "You have opened me four times since midnight and taken nothing. "
    "I am not a fridge anymore. I am a very cold mirror."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the competition gate before writing anything: the file must
    # hold 1 to 140 characters of UTF-8 text, not only white space.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError("entry line fails the 1-140 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.replace(tmp_path, OUTPUT_PATH)


if __name__ == "__main__":
    main()
