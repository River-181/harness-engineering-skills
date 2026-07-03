# Install Harness Engineering Skills

## Local Plugin Run

From this repository root:

```bash
claude --plugin-dir .
```

Use:

```text
/harness-engineering:route
```

## Personal Install

```bash
./scripts/install.sh
```

This copies the plugin directory to:

```text
~/.claude/skills/harness-engineering/
```

Restart Claude Code or run:

```text
/reload-plugins
```

## Project-Scoped Install

From a target project:

```bash
claude --plugin-dir /path/to/harness-engineering-skills
```

This keeps the pack local to that Claude Code session.

## Validate Package Structure

```bash
python3 scripts/validate_pack.py --strict
```

## Scaffold A Project Harness

From a target repo root:

```bash
python3 /path/to/harness-engineering-skills/scripts/scaffold_project.py . --profile generic
```

For a financial AI competition-style project:

```bash
python3 /path/to/harness-engineering-skills/scripts/scaffold_project.py . --profile jb-finai
```
