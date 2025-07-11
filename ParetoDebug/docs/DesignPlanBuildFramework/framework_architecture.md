## NOT needed for AI Architect

────────────────────────────────────────────── 📘 FRAMEWORK ARCHITECTURE DEFINITION ──────────────────────────────────────────────

Project: AI-Cooperative Modular Game Framework
Layer: ARCHITECTURE
Audience: Machine (AI Coder + Planner)
Status: LOCKED

────────────────────────────────────────────── 🏛️ PURPOSE ──────────────────────────────────────────────

The Architecture Layer defines the static structure, build order, and modular partitioning of the entire software project. It enforces:

* Layer separation and data flow
* Directory and file contracts
* Adapter boundaries
* Tag vocabulary schema
* Modular build units
* Sequencing and replaceability

This is the first formal output after ideation. It must be fully locked before planning or implementation.

────────────────────────────────────────────── 🧱 STRUCTURAL LAYER MODEL ──────────────────────────────────────────────

LAYER:         PURPOSE:
──────────────────────────────────────────────
CORE           Stateless logic, pure functions, frozen data only
SYSTEMS        Tick-based gameplay logic, AI, actions, XP, perception
INTERFACE      Input, output, renderers, debug surfaces
ADAPTERS       Mandatory isolation for all cross-layer access or volatility
ASSETS         JSON or txt-based game definitions (items, actors, techniques)
CONFIG         Constants and global settings only
TESTS          Validation layer
DOCUMENTS      Planning, design, and governance artifacts
SAVEFILES      Versioned simulation state (JSON)
DEBUG\_LOGS     Structured JSONL trace logs per context

────────────────────────────────────────────── 📂 DIRECTORY & FILE POLICY ──────────────────────────────────────────────

Each directory has a strict contract:

Directory       | File Types     | Rules
────────────────|----------------|------------------------------------------------------
/core/          | .py            | Stateless only. Frozen constants. No side effects. Must use \[PERMANENT] or \[UPGRADEABLE] only. Shared values → /config/, Large registries → /definitions/
/systems/       | .py            | Tick-safe logic only. Access world\_state directly. May emit events or use adapters. Must avoid side effects. Imports limited to declared contracts.
/interface/     | .py/.txt/.json | UI routing only. No logic. No world\_state access. `.txt` layouts must follow internal schemas.
/adapters/      | .py            | Routing only. No logic. Must include # \[ADAPTER] tag. May call \[DEAD-END] or volatile systems.
/assets/        | .json/.txt     | Templates, tags, and gameplay data. Must be tag-compatible.
/config/        | .py/.json      | Global constants only. No computation. No runtime logic.
/tests/         | .py            | Unit and integration only. Test world\_state in isolation.
/debug\_logs/    | .jsonl         | One file per context. Structured trace output only.
/documents/     | .md/.txt       | Planning artifacts. Not executed.
/savefiles/     | .save.json     | Versioned JSON. Must include metadata block.

📁 FILE LOCATION POLICY

* All *primary logic files* (declared in `architecture_index.json`) live in their assigned directory (e.g. `/core/render_ascii.py`).
* All *non-primary files* (contracts, docblocks, sequence metadata, debug logs, config constants, etc.) live in the **project root** or `/documents/`, `/config/`, `/debug_logs/`, `/tests/`, `/assets/`, or `/savefiles/` unless explicitly declared otherwise.
* This supports modular resolution and simplifies dependency-free loading by downstream AI agents.

────────────────────────────────────────────── 🧩 MODULE STATUS ENFORCEMENT ──────────────────────────────────────────────

Every module must be tagged:

* \[PERMANENT]  — Stable, long-term, tested logic
* \[UPGRADEABLE] — Will evolve into final form
* \[DEAD-END]   — Placeholder, must be isolated, replaceable

────────────────────────────────────────────── 🏷️ TAG SYSTEM (MECE) ──────────────────────────────────────────────

Tags are required for all:

* Static file docstrings (@tags)
* Runtime debug logs (ai\_tags)

Each tag set must include exactly one from each group:

* domain: combat, time, perception, etc.
* data\_affinity: actor\_data, item\_data, etc.
* semantic\_role: runtime\_behavior, system\_definition, etc.
* debug\_visibility | trigger\_surface | actor\_mindset: (pick one group only)

Source of truth: `tags_vocab.json`

────────────────────────────────────────────── 🧠 AI COLLABORATION MODEL ──────────────────────────────────────────────

AI generation is constrained to:

1. Load `framework_architecture.txt` (this file)
2. Load `architecture_index.json` for all module metadata and planning blocks
3. Obey contract links and declared sequence within that index

AI must never:

* Invent or access undeclared systems
* Assume availability of modules outside declared index
* Skip declared tags, trace\_id, or adapter usage

────────────────────────────────────────────── 📘 REQUIRED ARTIFACTS ──────────────────────────────────────────────

1. `framework_architecture.txt` — this file
2. `tags_vocab.json` — MECE tag groups
3. `architecture_index.json` — full metadata, block, and sequencing info
4. `contracts/*.md` — one contract file per module (not populated here)

────────────────────────────────────────────── 📐 EXAMPLE CONTRACT TEMPLATE FORMAT ──────────────────────────────────────────────

```
# Contract: contracts/render_ascii.md

## Purpose
Describe what this module must do.

## Inputs
(world_state, events, etc.)

## Outputs
(debug log, event payloads, mutations, etc.)

## ai_tags
- domain:
- data_affinity:
- semantic_role:
- [debug_visibility | trigger_surface | actor_mindset]:

## Traceability
Must emit trace_id and structured debug events.

## Required Adapters
Names and paths of any required adapters.

## Replaces
Name of previous module it evolves from (optional)
```

────────────────────────────────────────────── 📦 SEQUENCING AND REPLACEMENT ──────────────────────────────────────────────

Each module in `architecture_index.json` must define:

* `status`: PERMANENT, UPGRADEABLE, or DEAD-END
* `sequence`: numeric build order
* `replaces`: optional predecessor
* `block`: name of planning block
* `planned`: boolean for current scope

🔁 Iterative growth is modeled by chaining:

```json
"render_text": {
  "status": "DEAD-END",
  "sequence": 1,
  "block": "Rendering Foundation"
},
"render_ascii": {
  "status": "UPGRADEABLE",
  "replaces": "render_text",
  "sequence": 5,
  "block": "Rendering Upgrade"
},
"render_sprite": {
  "status": "PERMANENT",
  "replaces": "render_ascii",
  "sequence": 12,
  "block": "Rendering Final"
}
```

🧮 Planning blocks are automatically ordered by the **lowest sequence number** of any module they contain. This removes the need for `planning_blocks.json`.

────────────────────────────────────────────── ✅ END OF ARCHITECTURE LAYER ──────────────────────────────────────────────

Planning may now begin, using only the modules, contracts, blocks, and sequences defined in `architecture_index.json`.
