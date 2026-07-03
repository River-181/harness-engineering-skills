# Naming Rules

## Canonical Source

Use canonical domain terms from `docs/04_definitions.md`. Do not invent synonyms in code or UI.

## Forbidden Generic Names

- `Thing`
- `Item` unless it is a true domain term
- `Manager` unless it manages a real lifecycle
- `Utils` for domain logic
- `NewComponent`
- `ListPage` / `DetailPage` when a domain route name is clearer

## Pages and Routes

- Collection routes use plural nouns: `cases`, `customers`, `signals`.
- Detail routes use singular parameter names: `cases/[caseId]`.
- High-risk workflows include state or approval term in name: `PendingApprovalPanel`.

## AI/Agent Names

- Capabilities use verb-object names: `triageCase`, `collectEvidence`, `validateRecommendation`.
- Eval cases use scenario names: `missingEvidenceHighRisk`, `conflictingSourcesEscalate`.
