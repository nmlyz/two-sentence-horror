"""Two-Sentence Horror: one short horror story in exactly two sentences.

Writes the story to /output/entry.txt: a fisherman pulls a wedding ring
from the water, engraved with the narrator's initials and a date that has
not happened yet. Pure standard library, fully deterministic.
"""
import os

ENTRY = (
    "The fisherman pulled a wedding ring up on his line, engraved with "
    "my initials and a date. "
    "The date is next Tuesday, and I have never been married."
)


def main():
    # Gate: 1-400 characters, exactly two sentences.
    sentences = [s for s in ENTRY.split(". ") if s.strip()]
    assert 1 <= len(ENTRY) <= 400
    assert len(sentences) == 2, f"expected 2 sentences, got {len(sentences)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
