# Manifest

- Package: `harness-engineering`
- Public release: `0.1.0`
- Primary runtime: Claude Code
- Repository: `https://github.com/River-181/harness-engineering-skills`
- License: MIT

## Included

- Claude Code plugin manifest: `.claude-plugin/plugin.json`
- Lifecycle skills: `skills/*/SKILL.md`
- Shared references: `references/`
- Project templates: `templates/`
- Validation and scaffold scripts: `scripts/`
- Flagship example: `examples/jb-localguard-os`

## Release Contract

This pack is ready to publish when:

- `python3 scripts/validate_pack.py --strict` passes.
- `python3 scripts/validate_project.py examples/jb-localguard-os --strict` passes.
- README installation instructions match the local folder layout.
- No `.DS_Store`, placeholder organization URL, or release-blocking placeholder remains.
