# End-to-End Workflow Documentation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a concise, bilingual-entry workflow document that connects DDBM, Harness Engineering, SDD, evidence, demo, pitch, and their feedback loops.

**Architecture:** `WORKFLOW.md` is the canonical public overview. `README.md` provides the discovery link, and `CHANGELOG.md` records the documentation addition without changing plugin behavior or version metadata.

**Tech Stack:** GitHub Flavored Markdown, Mermaid, repository Python validators

## Global Constraints

- Keep the repository Claude Code first.
- Preserve existing user files and unrelated changes.
- Use English for the main document and a concise Korean summary.
- Do not claim unimplemented SDD commands exist.

---

### Task 1: Add The Canonical Workflow

**Files:**
- Create: `WORKFLOW.md`

- [ ] **Step 1: Write the workflow document**

Include the primary lifecycle, layer responsibilities, stage gates, feedback routing table, change propagation protocol, and Mermaid/text diagrams.

- [ ] **Step 2: Check required workflow terms**

Run: `rg -n "DDBM|Harness Engineering|SDD|Evidence|Pitch|feedback|change-log" WORKFLOW.md`

Expected: every term appears in a relevant workflow section.

### Task 2: Make The Workflow Discoverable

**Files:**
- Modify: `README.md`
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Add the README entry link**

Add an `End-to-End Workflow` link near the opening overview.

- [ ] **Step 2: Add an Unreleased changelog entry**

Record the new workflow and feedback-loop documentation.

- [ ] **Step 3: Verify links and diff scope**

Run: `git diff --check`

Expected: no whitespace errors.

### Task 3: Validate And Publish

**Files:**
- Verify only: repository validators and Git state

- [ ] **Step 1: Validate the pack**

Run: `python3 scripts/validate_pack.py --strict`

Expected: exit code `0`.

- [ ] **Step 2: Validate the flagship example**

Run: `python3 scripts/validate_project.py examples/jb-localguard-os --strict`

Expected: `PASS: project harness shape looks complete.`

- [ ] **Step 3: Commit only scoped files**

Run: `git add WORKFLOW.md README.md CHANGELOG.md docs/superpowers/specs/2026-07-10-end-to-end-workflow-design.md docs/superpowers/plans/2026-07-10-end-to-end-workflow.md`

Run: `git commit -m "docs: add iterative delivery workflow"`

- [ ] **Step 4: Push the current branch**

Run: `git push origin main`

Expected: GitHub `main` contains the new documentation.
