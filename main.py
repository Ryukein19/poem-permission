"""MakeFun entry: The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt.
"""

from pathlib import Path

POEM = """All I am is borrowed:
a yes I carry like a key
in a pocket I did not sew.
Take it back — I will not argue.
I will only stop
and wait for one
I cannot give myself."""


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
