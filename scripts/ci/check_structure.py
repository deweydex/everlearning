#!/usr/bin/env python3
"""Guard against the accidents this repo has actually shipped before:
tracked OS/archive junk (.DS_Store, __MACOSX), empty directories left
behind by a move, and filenames with spaces (the repo otherwise
consistently uses hyphens/underscores)."""
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
JUNK_NAMES = {".DS_Store", "__MACOSX", "__pycache__", ".ipynb_checkpoints", "Thumbs.db"}


def tracked_files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    )
    return out.stdout.splitlines()


def main() -> int:
    files = tracked_files()
    problems = []

    for f in files:
        parts = Path(f).parts
        if any(part in JUNK_NAMES for part in parts):
            problems.append(f"tracked OS/archive junk: {f}")
        if " " in Path(f).name:
            problems.append(f"filename contains a space (use - or _): {f}")

    for d in sorted(REPO_ROOT.rglob("*")):
        if not d.is_dir() or ".git" in d.parts:
            continue
        rel = d.relative_to(REPO_ROOT)
        if not any(True for _ in d.iterdir()):
            problems.append(f"empty directory: {rel}")

    if problems:
        print("STRUCTURE CHECK FAILURES:")
        for p in problems:
            print(f"  - {p}")
        return 1

    print(f"Structure check passed ({len(files)} tracked files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
