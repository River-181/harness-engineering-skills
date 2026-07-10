# End-to-End Workflow Documentation Design

## Goal

Add a public entry document that explains how DDBM, Harness Engineering, SDD, evidence, demo, and pitch work as one iterative delivery system.

## Audience And Language

- Primary audience: GitHub visitors and teams applying the pack to product or competition work.
- Main language: English for public discoverability.
- Korean summary: placed near the top for River's domestic competition workflow.

## Document Shape

- Create one root-level `WORKFLOW.md` as the canonical workflow overview.
- Link it from `README.md` near the initial product description.
- Record the addition under an `Unreleased` section in `CHANGELOG.md`.
- Use a GitHub-rendered Mermaid flowchart plus a text fallback.

## Workflow Model

The primary path is:

```text
Intake -> DDBM -> Harness -> SDD -> Evidence -> Demo/Pitch -> Handoff
```

Feedback may originate in business-model review, product specification, development, evaluation, demo, or pitch. A finding must update its source-of-truth artifact, propagate to dependent artifacts, be recorded in `docs/11_change-log.md`, and then pass the affected gates again.

## Scope

The document explains responsibilities, inputs, outputs, stage gates, loop triggers, and traceability. It does not add new plugin commands, rename existing skills, or claim that the roadmap SDD implementation skill already exists.

## Acceptance Criteria

- A new visitor can identify what each layer contributes without reading every skill.
- The diagram shows forward delivery and backward feedback paths.
- Business, development, evidence, and pitch feedback each have an explicit destination.
- Existing validators pass unchanged.
- The unrelated untracked Korean competition skill file remains untouched and uncommitted.
