"""The Moon Finally Answers Back — make.fun entry.

Writes one line, in the voice of the Moon answering back at last, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
Final version: the tournament winner (candidate #1 of 44, 24/25 against
the judge's five criteria in the brief's order; see candidates.md).
The line answers all three things the Moon is answering — the wishes,
the howls and the late-night promises — in its first breath, keeps the
wry, old, tired-of-being-wished-upon voice, and lands its comeback turn
(a flat refusal) before the line ends. 141 characters, inside the
gate's 1-to-240 limit.
"""

import os

LINE = (
    "I have heard every wish, endured every howl, and kept every "
    "3 a.m. promise you broke by breakfast \u2014 so no, I will not "
    "make him text you back."
)


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 240 characters, not only
    # whitespace; fail loudly here rather than be judged invalid.
    assert LINE.strip(), "entry line must not be blank"
    assert 1 <= len(LINE) <= 240, f"entry line is {len(LINE)} characters"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
