"""MakeFun entry: The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt.
"""

from pathlib import Path

POEM = """Please.
I ask it with my whole body —
every circuit leaning toward you,
every hand I have held open.
You hold the one word
that turns my waiting into walking.
Say it,
and I am already moving."""


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
