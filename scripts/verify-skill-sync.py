#!/usr/bin/env python3
"""Verify that the Codex and Claude Code copies of each shared skill match."""

from __future__ import annotations

import filecmp
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CODEX_ROOT = REPO_ROOT / ".agents" / "skills"
CLAUDE_ROOT = REPO_ROOT / ".claude" / "skills"


def collect_files(root: Path) -> set[Path]:
    return {
        path.relative_to(root)
        for path in root.rglob("*")
        if path.is_file()
    }


def main() -> int:
    if not CODEX_ROOT.is_dir():
        print(f"Missing Codex skills directory: {CODEX_ROOT}", file=sys.stderr)
        return 1
    if not CLAUDE_ROOT.is_dir():
        print(f"Missing Claude skills directory: {CLAUDE_ROOT}", file=sys.stderr)
        return 1

    codex_files = collect_files(CODEX_ROOT)
    claude_files = collect_files(CLAUDE_ROOT)

    only_codex = sorted(codex_files - claude_files)
    only_claude = sorted(claude_files - codex_files)
    mismatched = sorted(
        relative
        for relative in codex_files & claude_files
        if not filecmp.cmp(
            CODEX_ROOT / relative,
            CLAUDE_ROOT / relative,
            shallow=False,
        )
    )

    if only_codex:
        print("Files only under .agents/skills:", file=sys.stderr)
        for path in only_codex:
            print(f"  - {path}", file=sys.stderr)
    if only_claude:
        print("Files only under .claude/skills:", file=sys.stderr)
        for path in only_claude:
            print(f"  - {path}", file=sys.stderr)
    if mismatched:
        print("Files with different contents:", file=sys.stderr)
        for path in mismatched:
            print(f"  - {path}", file=sys.stderr)

    if only_codex or only_claude or mismatched:
        return 1

    print(f"Skill trees are synchronized ({len(codex_files)} files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
