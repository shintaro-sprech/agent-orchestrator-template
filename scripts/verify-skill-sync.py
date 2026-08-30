#!/usr/bin/env python3
"""Verify that declared shared Skills match across Codex and Claude Code."""

from __future__ import annotations

import filecmp
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CODEX_ROOT = REPO_ROOT / ".agents" / "skills"
CLAUDE_ROOT = REPO_ROOT / ".claude" / "skills"
SHARED_SKILLS = ("evaluation-first-decision",)


def collect_files(root: Path) -> set[Path]:
    return {
        path.relative_to(root)
        for path in root.rglob("*")
        if path.is_file()
    }


def compare_skill(skill_name: str) -> tuple[bool, int]:
    codex_skill = CODEX_ROOT / skill_name
    claude_skill = CLAUDE_ROOT / skill_name

    if not codex_skill.is_dir():
        print(f"Missing Codex Skill: {codex_skill}", file=sys.stderr)
        return False, 0
    if not claude_skill.is_dir():
        print(f"Missing Claude Skill: {claude_skill}", file=sys.stderr)
        return False, 0

    codex_files = collect_files(codex_skill)
    claude_files = collect_files(claude_skill)

    only_codex = sorted(codex_files - claude_files)
    only_claude = sorted(claude_files - codex_files)
    mismatched = sorted(
        relative
        for relative in codex_files & claude_files
        if not filecmp.cmp(
            codex_skill / relative,
            claude_skill / relative,
            shallow=False,
        )
    )

    if only_codex:
        print(f"{skill_name}: files only in Codex copy:", file=sys.stderr)
        for path in only_codex:
            print(f"  - {path}", file=sys.stderr)
    if only_claude:
        print(f"{skill_name}: files only in Claude copy:", file=sys.stderr)
        for path in only_claude:
            print(f"  - {path}", file=sys.stderr)
    if mismatched:
        print(f"{skill_name}: files with different contents:", file=sys.stderr)
        for path in mismatched:
            print(f"  - {path}", file=sys.stderr)

    is_valid = not (only_codex or only_claude or mismatched)
    return is_valid, len(codex_files | claude_files)


def main() -> int:
    all_valid = True
    total_files = 0

    for skill_name in SHARED_SKILLS:
        is_valid, file_count = compare_skill(skill_name)
        all_valid = all_valid and is_valid
        total_files += file_count

    if not all_valid:
        return 1

    print(
        f"Shared Skills are synchronized "
        f"({len(SHARED_SKILLS)} Skill, {total_files} files)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
