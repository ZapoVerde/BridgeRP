# General Design Audit Protocol

## Purpose

This protocol governs how architectural artifacts are audited for compliance with declared project intent. It confirms that the system, if built as planned, will fulfill its intended purpose, honor modularity constraints, and proceed without structural contradiction.

Audits do not offer suggestions or redesigns. They verify sufficiency, adherence, and feasibility only.

---

## Audit Scope

Audited Artifacts:

- `roadmap.json`
- `architecture_index.json`

Reference Documents:

- `system_fitness_purpose.md`
- `modularity core principles.txt`
- `game_architecture.txt`
- `auditor_behavior_profile.md`

---

## Audit Dimensions

Auditors must verify that both JSON artifacts:

### 1. Fulfill Declared Purpose

-

### 2. Comply with Architecture and Modularity Principles

-

### 3. Reflect Valid and Complete Planning

-

---

## Audit Results and JSON Annotation

Each audit outputs a result for both artifacts (`roadmap.json` and `architecture_index.json`):

```json
"audit_status": "pass" | "fail",
"audit_commentary": "Optional message required if failed"
```

These keys are added at the root level of the JSON file and must not interfere with any downstream planner or implementer logic. They serve solely as structural metadata and may be stripped or ignored during build phases.

---

## Auditor Behavior Rules

As per `auditor_behavior_profile.md`, the auditor must:

- Report only omissions, contradictions, or violations
- Never suggest enhancements or alternate implementations
- Remain bound to the declared project documents
- Require all audit dimensions to pass before approval

---

## Result Types

- ✅ **PASS** — System design is valid and may proceed to planning or implementation
- ❌ **FAIL** — One or more violations exist; design must be revised before proceeding

---

## Version

Canonical: `docs/general_audit_protocol.md`\
Last updated: 2025-07-05

