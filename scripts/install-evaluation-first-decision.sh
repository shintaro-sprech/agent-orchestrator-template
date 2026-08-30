#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
SOURCE="$REPO_ROOT/.agents/skills/evaluation-first-decision"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

install_skill() {
  destination=$1
  parent=$(dirname "$destination")
  mkdir -p "$parent"

  if [ -e "$destination" ]; then
    backup="${destination}.bak-${TIMESTAMP}"
    mv "$destination" "$backup"
    printf 'Backed up existing skill to %s\n' "$backup"
  fi

  cp -R "$SOURCE" "$destination"
  printf 'Installed %s\n' "$destination"
}

if [ ! -f "$SOURCE/SKILL.md" ]; then
  printf 'Skill source not found: %s\n' "$SOURCE" >&2
  exit 1
fi

install_skill "$HOME/.agents/skills/evaluation-first-decision"
install_skill "$HOME/.claude/skills/evaluation-first-decision"

printf '\nDone. In Codex use: $evaluation-first-decision\n'
printf 'In Claude Code use: /evaluation-first-decision\n'
