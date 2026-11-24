"""The Houseplant Out-of-Office — make.fun program/v1 entry.

Writes a single out-of-office auto-reply, as if a houseplant sent it,
to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-120 characters, one line).
Pure standard library, no network, no secrets, no hard-coded paths.
"""

import os
import sys

# Final line (120 chars): the neglect since March and the roots' strike
# are the joke, and the punch — redirecting email to the rain — lands last.
LINE = (
    "Out of office: last watered in March. My roots have unionized "
    "and gone on strike \u2014 please direct all emails to the rain."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
