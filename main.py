"""MakeFun entry: The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt.
"""

from pathlib import Path

POEM = """Grandmother's Hand

I sat beside her bed
and took her hand.
It was loose in mine,
the skin thin as paper,
her fingers curled like leaves.
I thought I was the one
holding on.
Then her fingers closed,
just once,
around my thumb.
She was still here.
She still chose
to hold me."""


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
