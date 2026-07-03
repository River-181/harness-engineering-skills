---
name: intake-log
description: Use before CPS, PRD, or implementation when raw transcripts, notes, client conversations, brainstorms, or vague requirements need normalization. Converts them into source logs, meeting logs, explicit/implied requirements, decisions, open questions, and build implications.
argument-hint: "[source-text-or-file]"
---
# Intake and Meeting Log Normalizer

## Use when

- User pastes a transcript or chaotic note
- A customer meeting needs to become buildable artifacts
- The team needs traceability from raw input to product decisions

## Do not use when

- The user asks for final copyediting only
- The input is already a clean PRD and only validation is needed

## Inputs to inspect

- Raw text, transcript, screenshots, issue notes, existing source log

## Files to create or update

- `docs/00_source-log.md`
- `docs/01_meeting-log.md`
- Updates to `harness.yaml.open_questions` and `harness.yaml.decisions`

## Operating sequence

1. Preserve source identity and scope.
2. Separate explicit requirements from inferred requirements.
3. Extract decisions, rejected options, unresolved questions, risks, and next actions.
4. Label confidence for each extracted requirement.
5. Map source signals to downstream artifact impact.
6. Do not prematurely narrow user ideas; note feasibility questions separately.

## Extraction Rules

- **Explicit** means the source directly says it.
- **Implied** means it follows from workflow, role, permission, or risk.
- **Assumption** means the agent is filling a gap; label it.
- **Decision** requires a rationale or source; otherwise it is an open question.

## Meeting Log Shape

```markdown
## Decisions
| Decision | Rationale | Owner | Status |

## Requirements Mentioned
| Requirement | Source Phrase | Priority | Confidence |

## Open Questions
| Question | Why It Matters | Suggested Resolution |

## Build Implications
| Signal | Product/Architecture Impact | Risk |
```

## Quality gates

- Every requirement has a source phrase or an assumption label.
- Open questions are not hidden inside prose.
- Meeting log is usable by someone who did not attend the meeting.


## Stop conditions

Stop and route backward when prerequisite artifacts are missing, when the requested action would erase user work, or when a high-risk workflow lacks evidence, approval, audit, or fail-closed handling.

## Example invocation

```text
/harness-engineering:intake-log

Apply this skill to the current repository. Inspect existing artifacts first, update only what is necessary, and report files changed, decisions, assumptions, validation, risks, and next skill.
```

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
