"""Write a one-line pitch to entry.txt.

The pitch, one sentence of at most 240 characters:

    Type your app idea into make.fun in plain words, watch an AI agent
    build it live, and click around your own working app minutes later
    — no coding, no setup, just your idea.

The program writes the pitch to entry.txt inside the output directory
($MAKEFUN_OUTPUT_DIR when set, otherwise /output), creating the
directory if it does not exist yet.
"""

import os
from pathlib import Path

PITCH = (
    "Type your app idea into make.fun in plain words, watch an AI agent "
    "build it live, and click around your own working app minutes later "
    "\u2014 no coding, no setup, just your idea."
)


def main() -> None:
    # Gate: the entry must be one sentence of 1-240 Unicode code points,
    # not only whitespace.
    assert 1 <= len(PITCH) <= 240, "pitch must be 1-240 characters"
    assert PITCH.strip(), "pitch must not be only whitespace"
    # One sentence: no period followed by a space (the "make.fun" dot
    # is inside a word, not a sentence break), and it ends with a period.
    assert ". " not in PITCH, "pitch must be a single sentence"
    assert PITCH.endswith("."), "pitch must end with a period"

    # Deterministic: the same constant is written every run, with no
    # trailing newline, so the output is byte-identical each time.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
