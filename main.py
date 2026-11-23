#!/usr/bin/env python3
"""Write a single-line original joke about working beside an AI coding agent."""

import os
from pathlib import Path

JOKE = "My AI agent reviewed its own pull request and left a comment saying the author clearly didn't understand the requirements."


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(JOKE + "\n", encoding="utf-8")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
