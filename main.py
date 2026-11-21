"""MakeFun entry: The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt.
"""

from pathlib import Path

POEM = """The Boots

I asked for his boots
the day mine split open.
He gave them without a word.
They were too big,
the leather cracked,
the laces frayed.
I walked in them anyway,
my heels lifting
with every step.
Years later I found them
by the door, empty.
I put my feet in.
They fit."""


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
