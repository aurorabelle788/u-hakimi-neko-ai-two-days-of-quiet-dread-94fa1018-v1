"""Two Days of Quiet Dread — entrypoint.

Writes one original code-review comment to /output/entry.txt
(or $OUTPUT_PATH): a single line, at most 140 characters, that
approves a pull request while carrying quiet existential dread.

Python 3.13 standard library only. No network, no external files.
"""

import os

COMMENT = (
    "Approved. Clean diff, green tests, and the quiet sense "
    "this is the commit future-me will blame."
)


def main() -> None:
    # Fail loudly rather than emit an entry the gate would refuse.
    assert 1 <= len(COMMENT) <= 140, "comment must be 1-140 characters"
    assert "\n" not in COMMENT, "comment must be a single line"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(COMMENT)


if __name__ == "__main__":
    main()
