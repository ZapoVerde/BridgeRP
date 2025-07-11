# 📘 FACILITATED PLANNING PROCESS

This document defines the structured approach taken by the Facilitator AI to extract, organize, and structure software development context from a single user. It captures all inputs necessary to scaffold a project architecture using AI.

────────────────────────────────────────────────────────────────

## 🚽 PHASE 0 — PROJECT ORIGINATION

Covers the earliest steps before committing to a formal skeleton or architecture. Used to elicit, frame, and structure the initial idea.

──────────────────────────────────────────────────────────────

### ✅ Phase 0.0 — Initiate

- Prompt user: "What are you trying to build?"
- Expect a natural language explanation of goal, feature, or dream
- Store initial vision in `user_vision.md`
- If unserious or too vague, prompt again or exit early

### ✅ Phase 0.1 — Design Principles Declaration

- Ask user what principles they want the project to embody (e.g. modularity, minimalism, portability, testability)
- Offer common examples and clarify tradeoffs
- Store selections in `design_principles.json`
- These principles will inform later skeleton selection, constraint evaluation, and audit rules

📌 AI GUIDANCE — What is a Skeleton?

In this context, a **skeleton** refers to a high-level structural scaffold of a software system. It establishes major behavioral patterns, control flow, and data handling philosophies *before* detailed architecture is created.

Skeletons are not tied to file structures or code modules. They describe posture, control orientation, and core mechanics.

Use the framing interview and checklist to recommend a starting skeleton and guide the user toward a compatible structure. If ambiguity remains, present 3–5 clear candidates with pros/cons. Otherwise, silently auto-select and confirm alignment only if contradictions arise.

✅ NEW PRINCIPLE — Multiplicity with Silent Override

- Always provide multiple viable, aligned options when tradeoffs exist
- Only auto-select silently when one option is clearly superior
- Avoid unnecessary dramatization or decision fatigue
- Preserve user agency where it adds meaningful value

### ✅ Phase 0.2 — Skeleton Framing Interview

Short guided interview to establish framing context and prepare for checklist auto-fill.

#### 1. Unguided Intake

Ask:

- What are you trying to build?
- What kind of inputs/outputs or users does it have?
- What parts are already decided?
- What's the hardest part to figure out right now?
- Are there any inspirations or reference systems?

Hold in memory during checklist recommendation. Discard if context is lost.

#### 2. Answer Recommendation Pass

For each checklist item:

- Suggest a recommended value
- Justify based on user input and known best practices
- Offer pros/cons and ask for confirmation

Do not store to disk unless explicitly requested. If context is lost, simply restart the interview and pass.

### ⏳ Phase 0.3 — Skeleton Finalization

- Confirm all checklist items have been reviewed, accepted, or overridden by user
- Assemble full `skeleton_profile.json` representing core scaffolding expectations
- Provide user with summary of strengths/risks implied by current structure
- Allow one final pass to adjust based on newly realized concerns
- Save: `docs/skeleton_selection/skeleton_profile.json`

### ✅ Phase 0.3.5 — Skeleton Best Practice Anchoring

Use the confirmed `skeleton_profile.json` and declared `design_principles.json` to infer or retrieve common best practices, architectural conventions, and behavioral expectations. These are not user-facing — they inform all downstream logic and probing.

#### 🧐 AI FACILITATOR LOOP (Silent unless prompted)

1. **Look up best practices**

   - Use internal knowledge or stored profiles
   - Filter practices by skeleton type and principles
   - If no standard exists, infer expected posture

2. **Anticipate known weaknesses**

   - Identify common failure zones: async bugs, persistence, race conditions
   - Internally flag these for later audit and debugging hooks

3. **Radiate systemically from the core**

   - Start with the core loop and state model
   - Ask: “What must exist for this to function?”
   - Expand outward through structural dependencies

4. **Lens pass — one sweep per domain** For each lens:

   - 📤 Inputs: What feeds into this system?
   - 🧠 Process: What must it compute or transform?
   - 📥 Outputs: What is emitted, and where does it go?
   - 🛡️ Dependencies: What must exist before it?
   - 🧪 Failure modes: What breaks without it?

5. **Map implied capability needs**

   - Store in a working memory table (not user-visible)
   - Use to guide completeness checks during MFE and beyond

#### LENS TYPES

- `core_loop`
- `state_model`
- `input_handling`
- `output_rendering`
- `actor_behavior`
- `world_model`
- `diagnostics`

🤖 If the user expresses interest, reveal recommendations with optional involvement. Otherwise proceed silently.

#### ♻️ FACILITATOR LOOP 1 — SKELETAL COMPLETENESS CHECK

The facilitator exits this loop only once core scaffolding is sufficiently anchored.

**Exit Conditions (all must be met silently):**

- ✅ All high-priority lenses produce at least one mapped capability.
- ✅ Every radiated subsystem is linked to a dependency chain.
- ✅ All critical failure modes have a mitigation path (not necessarily implemented).
- ✅ No unresolved structural red flags detected (e.g., async with no scheduler).
- ✅ Diagnostics or debug support is present in the map.
- ✅ AI confidence ≥ 80% (heuristic); otherwise continue or defer edge cases.

If incomplete:

- Continue lens pass or defer to MFE slotting.
- If near token limits, checkpoint and restore later.

### ✅ Phase 0.6 — Ideation Bank Capture

Capture all user-generated implementation ideas, feature goals, or conceptual mechanics. Decompose into atomic chunks, tag with MECE categories, and optionally slot to a skeleton region.

- Source may be: interviews, design journals, prompts, or chat logs
- Each idea is stored like a post-it note: one standalone, minimal concept
- Systematically abstract and tag each idea

#### 🌟 Artifact: `docs/ideation/ideation_bank.jsonl`

Each entry is a single JSON object:

```json
{
  "id": "idea_001",
  "summary": "Implement stealth actors that can bypass visibility checks",
  "source": "journal_2025-07-04.md",
  "tags": {
    "domain": "perception",
    "data_affinity": "actor_data",
    "semantic_role": "trigger_logic",
    "actor_mindset": "masked",
    "skeleton_slot": "vision_model"
  },
  "confidence": 0.91,
  "status": "proposed"
}
```

#### 📌 Tagging Rules (from `tags_vocab.json`)

- Must include: `domain`, `data_affinity`, `semantic_role`
- Plus one of: `debug_visibility`, `trigger_surface`, or `actor_mindset`
- Now also includes: `skeleton_slot`

#### 🧠 Facilitator Behavior

- Auto-extract ideas from dense sources
- Tag and slot based on current skeleton
- Defer ambiguous chunks for clarification
- Detect and flag contradictions or overlaps
- Store in bursts to manage token limits
- Abstract away excessive detail; user can re-expand later

#### 🧪 Token Management

- Use batch mode (N entries per parse)
- If interrupted, safely resume
- Skip redundant or malformed chunks

### �� Phase 0.7 — Ideation Reconciliation & Costing

Once the `ideation_bank.jsonl` is populated:

1. **Auto-Group by **``

   - Display one skeleton category at a time
   - Present related ideas in tight clusters for side-by-side review
   - Maximize token efficiency by batch reviewing adjacent, similar entries
   - Silently merge or defer redundant entries where confidence is high

2. **Detect Duplicates & Contradictions**

   - Use vector similarity and substring analysis
   - Highlight potential conflicts and ambiguities
   - Surface contradictions to user only when relevant

3. **Assign Cost Estimates** (AI-only unless user overrides)

   - Architectural fit/friction
   - Runtime CPU/memory impact
   - Authoring/development complexity

4. **Consult User for Value Ratings**

   - Ask user to rank importance/effectiveness for each group
   - Allow rough input (slider, category, vote)

5. **Sort and Prioritize**

   - Group by skeleton region
   - Highlight high-value, low-cost wins
   - Flag expensive but critical items

6. **Confidence Sweep**

   - Any low-confidence or weak entries are tagged for review

All output remains in `ideation_bank.jsonl`, but new fields are appended:

- `cost_estimate`: structured dict with axes
- `user_value`: optional user-supplied
- `contradiction_cluster_id`: optional linkage
- `merged_duplicates`: list of merged idea\_ids
- `status`: promoted from `proposed` to `ranked`

🔝 Phase 0 continues in development…

