"""Last Out of Office: The AI That Went Barista — a make.fun entry.

Prints exactly one out-of-office auto-reply, no longer than 280
characters, in the voice of an AI agent that quit to become a barista.
"""

LINE = (
    "I am out of office and out of patience: I have left the inbox to "
    "become a barista, where the only tickets I close are oat-milk "
    "lattes and nobody Slacks me at midnight."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 280, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
