# Quickstart

## Run As A Local Claude Code Plugin

```bash
cd harness-engineering-skills
claude --plugin-dir .
```

## First Commands In A Real Project

```text
/harness-engineering:init-project
Scaffold this repo with the generic profile. Do not overwrite existing docs.

/harness-engineering:route
Inspect the project and choose the next harness skill.

/harness-engineering:ddbm-business-model
Create the 11-block business model before PRD or pitch.

/harness-engineering:cps-framing
Create or update CPS from the current README, issues, and notes.

/harness-engineering:validate-harness
Validate readiness before build, demo, or handoff.
```

## Financial Competition Fast Path

```text
/harness-engineering:init-project
Use profile jb-finai.

/harness-engineering:ddbm-business-model
Make the data, cost, revenue, and negative-impact logic judge-ready.

/harness-engineering:jb-finai-adapter
Align this MVP to financial AI Agent judging criteria.
```

## Verify The Included Example

```bash
python3 scripts/validate_project.py examples/jb-localguard-os --strict
```
