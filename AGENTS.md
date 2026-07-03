# Repository Agent Instructions

This repository is the source for the Harness Engineering Claude Code plugin.

Before changing the pack:

- Keep this repo Claude Code first. Codex compatibility can be added later, but should not distort the Claude plugin shape.
- Do not edit generated consumer project artifacts unless the task explicitly targets `examples/` or `templates/`.
- Keep every skill focused on one lifecycle job and prefer shared references over repeated boilerplate.
- Run the relevant validators before finishing:

```bash
python3 scripts/validate_pack.py --strict
python3 scripts/validate_project.py examples/jb-localguard-os --strict
```

For consumer projects, use `templates/project-CLAUDE.md` as the copied project contract.
