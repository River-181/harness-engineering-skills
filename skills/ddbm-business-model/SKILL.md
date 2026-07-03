---
name: ddbm-business-model
description: Use before CPS, PRD, pitch, or competition submission when a product needs a sharp data-driven business model. Creates the 11-block DDBM canvas, data asset assumptions, risk linkage, cost/revenue model, and judge-facing business thesis.
argument-hint: "[product-or-competition-context]"
---
# DDBM Business Model

## Use when

- The product idea needs a data-driven business model before technical planning.
- A competition submission must explain value, data, barriers, costs, revenue, and impact.
- The team has a working concept but weak commercial logic.
- Financial, regulated, or customer-facing risks must connect to the business model.

## Do not use when

- The request is only technical implementation and business scope is already approved.
- There is no product/user/value proposition to model.
- The user asks for legal, tax, or accounting advice.

## Inputs to inspect

- Raw idea, pitch memo, competition brief, PRD, or meeting notes
- Existing `docs/00_source-log.md`, `docs/01_meeting-log.md`, and `docs/02_cps.md`
- Available data sources, API constraints, partner assumptions, and target users
- Risk/compliance artifacts if they already exist

## Files to create or update

- `docs/01_business-model.md`
- `harness.yaml.artifacts.business_model`
- `harness.yaml.open_questions`
- Optionally `docs/02_cps.md`, `docs/10_eval-plan.md`, and `rules/compliance-rules.md`

## Operating sequence

1. Identify the customer, job-to-be-done, and measurable business outcome.
2. Fill all 11 DDBM blocks: Mission, Key Partners, Key Activities, Key Data, Key Enablers, Key Barriers, Value Proposition, Benefits, Negative Impacts, Costs, Revenues.
3. Make `Key Data` concrete: source, ownership/permission, freshness, consent basis, quality risk, and fallback.
4. Turn `Negative Impacts` into risk rows with stable `Risk-ID` values that can be reused by risk/compliance artifacts.
5. Add unit economics assumptions where possible: acquisition cost, API/data cost, operating cost, revenue unit, and gross margin driver.
6. Write a one-paragraph judge-facing thesis that says why the data advantage is hard to copy.
7. Record unresolved assumptions in `harness.yaml.open_questions`.

## Quality gates

- All 11 blocks are present and specific to the product.
- `Key Data` names concrete data assets, not generic "AI data".
- Each high-impact negative impact has a `Risk-ID`.
- Costs and revenues contain units, not only categories.
- Value proposition names a user, problem, data advantage, and measurable benefit.

## Stop conditions

Stop before PRD or pitch if the value proposition is generic, the data source is unavailable, the consent basis is unclear, or the revenue model has no unit.

## Shared completion and integrity

End with the completion report in `../../references/common-completion-report.md` and follow `../../references/common-integrity-rules.md`.
