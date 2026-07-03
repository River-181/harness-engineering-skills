---
name: jb-finai-adapter
description: Use for JB금융그룹 Fin:AI 본선/예선 work or similar financial AI Agent competitions. Aligns a financial AI Agent MVP, proposal, feature specification, demo flow, change log, and risk controls to judging criteria.
argument-hint: "[project-or-submission]"
---
# JB Fin:AI Adapter

## Use when

- Preparing JB Fin:AI documents
- Need map MVP to five judging categories
- Need ensure AI Agent 판단/행동/검증-개선
- Need feature change history

## Do not use when

- Non-financial project with no competition context, unless user asks for adapter pattern

## Inputs to inspect

- All harness docs
- Official judging criteria from user/project
- MVP/demo state

## Files to create or update

- Judging alignment section in PRD/handoff
- Updates to `docs/08_feature-spec.md`, `docs/09_flow.md`, `docs/10_eval-plan.md`, `docs/11_change-log.md`
- Optional `docs/jb-finai-scorecard.md`

## Operating sequence

1. Map project to five 20-point criteria.
2. Verify required proposal sections.
3. Verify feature specification sections.
4. Verify AI Agent common requirements: judgment/action/verification-improvement.
5. Check demo can run locally on own hardware.
6. Check change history for post-prelim changes.
7. Check risks: privacy/security/copyright/hallucination/explainability/responsibility.
8. Produce a scorecard and prioritized fixes.

## JB Fin:AI Scorecard

```markdown
| Criterion | Evidence in MVP/docs | Gap | Fix | Priority |
|---|---|---|---|---|
| 1. 주제적합성 및 문제정의 | | | | |
| 2. 금융업무·사업 연계성 및 고객가치 | | | | |
| 3. AI Agent 설계 및 기술적 구현 가능성 | | | | |
| 4. MVP 완성도 및 검증 가능성 | | | | |
| 5. 혁신성·확장성 및 운영 리스크 관리 | | | | |
```

## Required Agent Proof

For each core feature, show:

- 판단: what state/risk/priority is derived,
- 행동: what next action is selected,
- 검증/개선: what check/retry/stop condition exists.

## Quality gates

- Every judging criterion has concrete evidence.
- Required deliverable sections are present.
- Feature changes after baseline are recorded.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:jb-finai-adapter

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
