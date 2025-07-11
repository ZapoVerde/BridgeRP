──────────────────────────────────────────────────────────── 🗽 ARCHITECTURAL PROCESS — FINAL FORM ────────────────────────────────────────────────────────
This defines the **complete workflow** for the AI Architect during the Architecture Phase. It includes all required outputs, sequencing, and logic constraints.
This process is designed to be independently auditable and avoids premature exposure to modules, filenames, or implementation details.

──────────────────────────────────────────────── 📌 PHASES OVERVIEW ────────────────────────────────────────────────

1. **Milestone Definition** — Define high-level project milestones that represent major capability tiers or completed features.
2. **Block Scoping** — Within each milestone, define blocks representing the steps to reach that milestone, capturing dependencies and destructive transitions.
3. **Architecture Index Population** — For every block, define its concrete module outputs in a unified index structure with sequencing, file paths, and tags.
4. **Validation & Locking** — All three artifacts (`roadmap.json` with embedded blocks, `architecture_index.json`) are reviewed and locked before any planning occurs.

──────────────────────────────────────────────── 📆 STEP 1: DEFINE MILESTONES ────────────────────────────────────────────────
**Artifact**: `roadmap.json`
**Purpose**: Capture the major high-level stages of the project.

**Fields**:

* `milestone_sequence_no`
* `milestone` (name)
* `description`
* `blocks` (initially empty)

✅ **Rules**:

* Milestones define *capability goals*, not module content.
* Must include all critical development eras (e.g. core loop, UI stack, skills).
* Must not reference module names or file paths.

────────────────────────────────────────────────
📎 IMPLEMENTATION BOUNDARY: STEP 1 → STEP 2
────────────────────────────────────────────────

🚧 A strict break is enforced between Step 1 (milestone definition) and Step 2 (block population).

The Architect must **fully complete and lock the milestone structure before proceeding to block scoping**. This separation ensures:

* Milestone structure is clear and token-efficient
* AI does not prematurely reason about block-level detail
* Memory constraints are not exceeded when operating on large project structures

This staging allows milestones to serve as a stable foundation for all subsequent logic — enabling clean, chunked architectural planning.

────────────────────────────────────────────────
📎 IMPLEMENTATION CONTROL: BLOCK POPULATION ORDER
────────────────────────────────────────────────

🚧 Blocks must be populated one at a time, in ascending `block_sequence_no` order.

The Architect must begin with the first block and traverse sequentially, completing each entry fully before advancing. This enforces memory safety, preserves contextual clarity, and avoids speculative forward dependency.

──────────────────────────────────────────────── 📆 STEP 2: POPULATE BLOCKS ────────────────────────────────────────────────
**Artifact**: `roadmap.json`
**Purpose**: Define all the **blocks** within each milestone. Each block represents a unit of architectural development.

Each milestone contains a `blocks` list with entries including:

* `block_sequence_no` (global)
* `block` (name)
* `description`
* `milestone` (string)
* `milestone_sequence_no` (inherited)
* `dependencies`: other blocks this one builds on
* `destructive_replacements`: names of blocks/functionality it fully replaces or obsoletes (even if it is itself)
* `status`: \["planned", "partial", "complete"]
* `conceptual_level_outputs`: list of high-level systems, models, or behaviors this block is intended to deliver

✅ **Rules**:

* **📌 Composability Rule:**
  Every block must produce a coherent and testable architectural increment when combined with earlier blocks. Blocks may depend on previous work, but must not anticipate or rely on future or undeclared systems.
* **Dependencies must be declared early.** Any block requiring preconditions must list them explicitly.
* **Dependency-first sequencing is mandatory.** Blocks that provide functionality required by others must be placed early in the milestone sequence, even if this shifts their natural grouping.
* **Avoid stubbing where possible.** Prefer full implementation of dependencies early rather than scaffolding throwaway code. Stub only if essential to unblock progress.
* **Destructive transitions must be explicit**, especially if they replace dead-ends or temporary scaffolds.
* **Conceptual-level outputs must be stated** to guide module planning and enforce architectural intent.
* Blocks are defined inline inside `roadmap.json`. There is no separate `milestones.json` artifact.

──────────────────────────────────────────────── 📆 STEP 3: BUILD ARCHITECTURE INDEX ────────────────────────────────────────────────
**Artifact**: `architecture_index.json`
**Purpose**: Define every **real, file-backed module** that the codebase will contain. These are actual files with assigned names, locations, inputs/outputs, and system purpose.
Conceptual blocks are now resolved into file-level deliverables.

**Fields per module**:

* `status`: PERMANENT, UPGRADEABLE, DEAD-END
* `module_sequence_no`: global execution order
* `block`: name of parent block
* `block_sequence_no`: inherited from block
* `replaces`: name of module it obsoletes (if any)
* `planned`: whether the module is in scope
* `path`: full filepath (must match directory rules)
* `description`: human-readable summary
* `inputs`: description string
* `outputs`: description string
* `ai_tags`: required MECE tag set

**Rules:**

This artifact is governed by `architecture_index_creation_contract.md`, which defines all generation phases, tagging rules, and validation constraints.

──────────────────────────────────────────────── 🌿 VALIDATION AND AUDIT ────────────────────────────────────────────────
All steps are **auditable via JSON artifacts only**. No human-readable Markdown, contract duplication, or sidecar files are required.

Validation points:

* All blocks must appear in the correct milestone inside `roadmap.json`.
* All modules in `architecture_index.json` must reference a declared block.
* All block names and sequence numbers must be globally consistent.
* Every destructive transition or dependency must be explicitly defined within `roadmap.json`.
* **Every milestone must be achievable by its blocks.**
* **Every block must be constructible from its listed modules.**
* **All declared ****`conceptual_level_outputs`**** must be reflected in module responsibilities during planning.**

──────────────────────────────────────────────── 🏁 FLOW SUMMARY ────────────────────────────────────────────────

```
Define milestones → Create dependent blocks → Populate remaining blocks →
Embed blocks in roadmap → Populate architecture index →
Validate all links and transitions → Lock → Begin planning
```
