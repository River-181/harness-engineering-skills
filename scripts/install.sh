#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET_DIR="$HOME/.claude/skills/harness-engineering"

mkdir -p "$HOME/.claude/skills"
if [ -e "$TARGET_DIR" ]; then
  backup="$TARGET_DIR.backup.$(date +%Y%m%d%H%M%S)"
  echo "Existing install found. Moving to $backup"
  mv "$TARGET_DIR" "$backup"
fi
cp -R "$PLUGIN_DIR" "$TARGET_DIR"
echo "Installed Harness Engineering plugin to $TARGET_DIR"
echo "Start Claude Code and run: /reload-plugins"
echo "Try: /harness-engineering:route"
