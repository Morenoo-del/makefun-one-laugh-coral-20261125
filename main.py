#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line to /output/entry.txt.
"""

LINE = (
    "My password manager changed my password to something even I don't know "
    "\u2014 now we're both locked out, and it's never been happier."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters, a single non-blank line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
