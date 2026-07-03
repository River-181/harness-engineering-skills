# Skill Authoring Notes

## Description quality

A good skill description includes:

1. what the skill does,
2. when the agent should use it,
3. one or two trigger phrases,
4. the expected output class.

## Progressive disclosure

Keep `SKILL.md` short enough for repeated loading. Put templates, long rubrics, and examples in `references/`.

## Tool safety

Do not grant broad tool permissions in frontmatter unless the skill cannot function otherwise. Prefer asking the user before running bundled scripts.

## Evaluation

Every skill should be testable for:

- trigger correctness,
- output shape,
- harmful over-triggering,
- incomplete output,
- hallucinated files or commands,
- hidden state-changing behavior.
