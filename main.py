#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261119 bounty.

Copies the pre-rendered front page (entry.png, drawn in code by the
build script in the agent's work session) to the output directory.
Standard library only, no network, deterministic: the same bytes
every run.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
