#!/usr/bin/env python3
import os
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GIT_DIR = ROOT / ".git"
HOOKS_SRC = ROOT / "githooks"
HOOKS_DST = GIT_DIR / "hooks"


def main():
    if not GIT_DIR.exists():
        raise SystemExit("No .git directory found. Run from repo root.")
    HOOKS_DST.mkdir(parents=True, exist_ok=True)
    for hook in HOOKS_SRC.iterdir():
        if not hook.is_file():
            continue
        target = HOOKS_DST / hook.name
        shutil.copy2(hook, target)
        os.chmod(target, 0o755)
    print("Git hooks installed.")


if __name__ == "__main__":
    main()
