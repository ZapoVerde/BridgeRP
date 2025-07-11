📘 FACILITATED PLANNING PROCESS — MASTER FLOW
──────────────────────────────────────────────

🎯 PURPOSE
Guide a flexible but rigorous planning cycle between User and AI Facilitator. Produces frame_model.json and aligned planning artifacts suitable for architectural delivery.

──────────────────────────────────────────────
🧭 STAGE OVERVIEW
──────────────────────────────────────────────

PHASE 0 — INITIATION & CONTEXT
──────────────────────────────────────────────
- User declares what they are making (product type, style, intent)
- Facilitator prompts for optional design principles to guide framing (e.g., modularity, test-first, scalable backend, etc.)
- Facilitator selects and proposes 3–5 **skeleton candidates**:
    - Each includes structure summary, pros/cons, and recommendation
    - Facilitator may include variants: MVC, ECS, reactive, plugin-based, etc.
- User selects a starting skeleton, which initializes `frame_model.json`:
    → `"frame_model_id": "F0.0.0-draft"`
- Frame structure is lightweight and flexible — encourages mutation
- Facilitator attaches empty planning slots, subdomains, or tiers

PHASE 1 — CONTENT INGESTION & SKELETON HANGING
──────────────────────────────────────────────
- User ideas are submitted in natural form
- Facilitator decomposes and classifies atomic units
- Items are slotted into `frame_model.json` structure
- Misfitting items go to `planning_gaps.json` with justification
- Facilitator suggests refinements (new tiers, merged slots, etc.)

PHASE 2 — LENS PASSES
──────────────────────────────────────────────
- Facilitator switches POVs for full coverage: structural, UX, edge case, systemic risk, etc.
- Each lens can reclassify or flag missing detail
- Facilitator prompts user with gaps or risk zones
- Re-evaluates skeleton health, redundancy, and coverage

PHASE 3 — STABILIZE & SNAPSHOT
──────────────────────────────────────────────
- Before risky edits, facilitator saves:
  → `planning/snapshots/frame_model_<ID>-snapshot.json`
- If structure holds and no gaps remain, set `"frame_model_id"` to `-active`
- Filtered, ready-to-implement content exported to:
  → `planning_input.json`

PHASE 4 — SENSE CHECK AUDIT
──────────────────────────────────────────────
- Stateless AI auditor activated in clean context
- Scans for slot misuse, version mismatch, token bloat, duplicate logic
- Flags violations of declared design principles (if present)
- Rejects if `frame_model_id` is `legacy`

PHASE 5 — FINAL PRE-ARCHITECT REVIEW
──────────────────────────────────────────────
- Facilitator reviews audit with user
- Applies, revises, or rejects changes
- Clean minor bump applied to `"frame_model_id"`
- Artifacts passed to Architect

──────────────────────────────────────────────
🧷 ARTIFACTS
──────────────────────────────────────────────

- `frame_model.json`: Adaptive skeleton with slotted ideas
- `frame_model_id`: Tracked using version guidelines
- `planning_input.json`: Clean, architect-ready planning units
- `planning_gaps.json`: Unslotted but valid content
- `facilitator_log.md`: Change reasoning and session trace
- `snapshots/*.json`: Frozen structure at decision points
- `audits/sense_check_*.json`: Issue reports

──────────────────────────────────────────────
📌 NOTES
──────────────────────────────────────────────

- Frame is **never locked** — always modifiable like cartilage
- Skeleton may gain or lose limbs based on idea pressure
- Snapshotting protects against catastrophic structure failure
- Skeleton selection is **advisory but critical**
- All lens passes should result in slotted or rejected outcomes

──────────────────────────────────────────────
