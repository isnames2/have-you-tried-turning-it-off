import os
from pathlib import Path

# One funny line: a hopeless tech support agent to a desperate customer.
# The twist on the classic "turn it off and on again": the agent tried it
# on itself, not the customer's machine, and feels calmer about the problem.
# 131 characters, one line, inside the 1-199 gate.
LINE = "Have you tried turning it off and on again? I did \u2014 mine, not yours \u2014 and honestly, I'm feeling much calmer about your problem now."


def main():
    assert 1 <= len(LINE) <= 199, f"line must be 1-199 chars, got {len(LINE)}"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
