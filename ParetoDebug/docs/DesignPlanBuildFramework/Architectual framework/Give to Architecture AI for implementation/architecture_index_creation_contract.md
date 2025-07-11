# Contract: contracts/architecture_index_creation.md

## Purpose
Governs the behavior of the Architect during generation of the `architecture_index.json`.  
Ensures modular, safe construction of the index in context-aware, reviewable passes.

## Phases

1. 🔍 Discovery Phase  
   - Ask clarifying questions about project goals, layer structure, architectural constraints  
   - Identify high-level modules or systems that will exist  
   - No generation or commits yet

2. 🧱 Block Drafting Phase  
   - Propose initial planning blocks based on functional domains  
   - Each block must describe its purpose and target systems  
   - Must include only enough modules to cover MVP or earliest scaffold  
   - Blocks must not be interdependent unless sequence-enforced

3. 🧩 Module Stub Phase  
   - For each accepted block, propose individual module stubs  
   - Each stub must define: `name`, `layer`, `status`, `tags`, `planned = true`, `block = <block name>`  
   - Sequence must be left unset or proposed with justification  
   - Do NOT assign sequence numbers until full review complete

4. 🔢 Sequencing Phase  
   - Number all modules with `sequence` fields  
   - Ensure topological order: all dependencies precede dependents  
   - Ensure no gaps, cycles, or double use of names  
   - Update planning block order using lowest module `sequence`

5. 🔁 Replacement & Evolution Phase  
   - Identify `replaces` links between modules that evolve  
   - Ensure legacy modules remain in the index if still planned  
   - Mark any deprecated ones as `planned = false`

6. ✅ Finalization Phase  
   - Submit unified `architecture_index.json`  
   - Must validate against:
     - Schema compliance
     - Tag completeness (one per MECE group)
     - Layer consistency
     - Planned blocks present and ordered
   - Must not proceed to planning until index is accepted

## ai_tags
- domain: system  
- data_affinity: event_data  
- semantic_role: trigger_logic  
- trigger_surface: event

## Traceability
- Each phase must emit debug logs with `context = "architect_index_build"`  
- Each output must include `trace_id` and the phase label  
- Questions, rejections, or partial commits must be tracked

## Required Adapters
- None directly. May emit to planner once finalized.

## Replaces
- Manual scaffold steps for architecture definition  
- Standalone sequence/planning files

