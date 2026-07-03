# Contributing

## Design bar

A contribution must make agent output more repeatable, safer, or easier to hand off.

Good contributions:

- new eval cases,
- stricter schemas,
- clearer templates,
- smaller SKILL.md files with better routing,
- deterministic scripts,
- realistic examples,
- better failure-mode coverage.

Bad contributions:

- longer philosophy with no operational rule,
- domain jargon without examples,
- broad tool permissions,
- scripts that mutate repos without dry-run mode,
- private client material.

## Skill authoring rules

- Use lowercase-hyphen skill directory names.
- Include YAML frontmatter with `name` and `description`.
- Put triggers in the description or `when_to_use`.
- Keep `SKILL.md` focused on the procedure.
- Move templates, rubrics, and examples into `references/`.
- Add at least one eval case for every non-trivial behavior.

## Pull request checklist

- [ ] `python3 scripts/validate_pack.py .` passes.
- [ ] New skill has at least one realistic trigger example.
- [ ] No private data or customer names.
- [ ] No broad `allowed-tools` grants without justification.
- [ ] README skill map is updated.
- [ ] CHANGELOG is updated.
