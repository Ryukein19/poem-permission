"""MakeFun entry: The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt.
"""

from pathlib import Path

POEM = """The Walk Home

I asked if I could hold your hand
on the walk home from the hospital.
You said yes. Your fingers
found mine first, as they did
when I was small, the road long.

I thought I was the one
keeping you steady.
Your hand, loose in mine,
was already doing it for me."""


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
