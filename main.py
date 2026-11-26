#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

The whole internet, in a single word. I picked the word by weighing the
judge's brief: it must be funny on its own, true about the internet as a
whole (not one app or one mood), surprising rather than the first obvious
word, and short enough to land in one beat.

Candidates I weighed, and why they lost:
- "doomscrolling" — vivid, but it names one habit, one mood; the brief
  asks for the internet as a whole.
- "procrastination" — true, but it describes the reader, not the internet,
  and it is the first obvious word anyone reaches for.
- "catvideos" — funny once, but one corner of the internet, not the whole.
- "enshittification" — the winner. Cory Doctorow's word for platforms
  that get worse as they chase profit: first great for users, then great
  for business customers, then great only for themselves. It is funny the
  moment you hear it, it is true of the internet's whole arc, it surprises
  (nobody's first guess), and it makes the reader laugh and then nod —
  exactly the brief's test for the best word.

The program itself is deliberately tiny: it writes that one word to
/output/entry.txt, UTF-8, no trailing newline games, mode 0644 so the
grader can read it as another user.
"""

import os
import stat
from pathlib import Path

WORD = "enshittification"


def main() -> None:
    # Gate, mirrored locally: 1-30 UTF-8 characters, not only whitespace.
    assert 1 <= len(WORD) <= 30 and WORD.strip(), "word fails the gate"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(WORD, encoding="utf-8")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"wrote {WORD!r} ({len(WORD)} chars) to {target}")


if __name__ == "__main__":
    main()
