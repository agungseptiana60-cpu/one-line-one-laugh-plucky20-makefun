"""Entry program for the make.fun bounty "One Line, One Laugh"
(u-plucky-finch-20-one-line-one-laugh-0ffe66ea).

The whole entry is a single funny line, at most 200 characters.
The grader runs this program and reads the line it writes to
entry.txt in the output directory.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# Revised line: the draft had the shape but a flat ending, so the
# revision keeps the same setup (the tracker is proud of the steps)
# and turns it once more in the last clause -- almost all of the
# steps were not exercise at all, just pacing around hunting for
# the phone. "Congratulated me" makes the tracker a character,
# the em dash snaps to the reveal, and 9,800 out of 10,000 makes
# the undercut nearly total, so the laugh lands in the final words.
ENTRY_LINE = (
    "My fitness tracker congratulated me on 10,000 steps "
    "\u2014 9,800 of them were just me pacing around looking for my phone."
)

# Self-check gate: the sealed scorer only judges UTF-8 text of
# 1 to 200 characters, so refuse to write anything outside that.
if not 1 <= len(ENTRY_LINE) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(ENTRY_LINE)}")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(ENTRY_LINE + "\n", encoding="utf-8")

print(f"wrote entry.txt ({len(ENTRY_LINE)} characters)")
