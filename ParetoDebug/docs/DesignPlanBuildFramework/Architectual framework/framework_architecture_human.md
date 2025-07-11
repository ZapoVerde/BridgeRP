📘 HUMAN OVERVIEW — ARCHITECTURE FRAMEWORK

Project: Modular AI-Cooperative Game Engine\
Audience: Human developers, architects, and technical reviewers\
Purpose: To explain, in clear terms, how the project’s architecture is structured, what rules it enforces, and how it supports AI-assisted development

────────────────────────────────────────────── 🏠 WHAT IS THIS FOR? ──────────────────────────────────────────────

This framework governs the **structure and sequencing** of your entire project. It is not code. It is the blueprint that ensures:

- Every file has a valid place and purpose
- Layers don’t bleed into each other
- AI tools follow the same rules you do
- All logic is modular, traceable, and replaceable
- Growth happens in stable, testable increments

No implementation can begin until this architecture is locked.

---

────────────────────────────────────────────── 📦 WHAT IT CONTROLS ──────────────────────────────────────────────

✔ File layout\
✔ Layer boundaries\
✔ Allowed module behavior\
✔ Status labels for modules\
✔ Build order and replacements\
✔ AI safety rules\
✔ Debug tag structure\
✔ Contracts and planning artifacts

This is your **source of truth** for what gets built, when, and how.

---

────────────────────────────────────────────── 📀 LAYER MODEL ──────────────────────────────────────────────

Each source file lives in one of these layers:

| Layer         | What It’s For                                   |
| ------------- | ----------------------------------------------- |
| `core/`       | Pure logic, stateless helpers, frozen constants |
| `systems/`    | Tick-based simulation logic and gameplay        |
| `interface/`  | Rendering, I/O, debug visuals                   |
| `adapters/`   | Safe bridges across boundaries                  |
| `config/`     | Global constants, no computation                |
| `assets/`     | Data: items, actors, skills, etc. (JSON/TXT)    |
| `tests/`      | Unit/integration tests, world\_state isolation  |
| `documents/`  | Design and planning documents                   |
| `savefiles/`  | Versioned JSON states with metadata             |
| `debug_logs/` | JSONL-formatted runtime traces per context      |

**Rules**:

- No logic in adapters, assets, interface, or config
- No side effects in `core/`
- Only adapters may cross layers
- Tests must not mutate shared state

---

────────────────────────────────────────────── 🔄 MODULE EVOLUTION & STATUS ──────────────────────────────────────────────

Each module declares its current state:

- `[DEAD-END]` – temporary scaffold, must be replaced
- `[UPGRADEABLE]` – evolving but valid
- `[PERMANENT]` – final, reviewed, and stable

Modules **replace** earlier ones via an explicit chain:

```
render_text → render_ascii → render_sprite
```

Every module is tied to a **planning block** which belongs to a **milestone**. These are tracked in `architecture_index.json` and `roadmap.json` respectively.

---

────────────────────────────────────────────── 🗓 ARCHITECTURE PROCESS (PHASES) ──────────────────────────────────────────────

All architecture follows a **strictly sequenced** six-step flow:

1. **Milestone Definition**
   - Declare major project goals (e.g. Combat, Rendering)
2. **Block Scoping**
   - Define the building steps to reach each milestone
3. **Module Indexing**
   - List actual files, their purpose, and sequence
4. **Sequencing**
   - Number modules, enforce build order
5. **Replacement Mapping**
   - Link temporary scaffolds to permanent successors
6. **Finalization**
   - Lock the architecture. No changes allowed afterward.

Each phase builds only on completed earlier ones. No forward guessing, stubbing, or parallel design is permitted.

---

────────────────────────────────────────────── 🏷️ TAG SYSTEM ──────────────────────────────────────────────

Every module and debug log includes a MECE-compliant tag set:

- One `domain` (e.g. combat, UI, mutation)
- One `data_affinity` (e.g. actor\_data, skill\_data)
- One `semantic_role` (e.g. runtime\_behavior, trigger\_logic)
- One from ONLY ONE of:
  - `debug_visibility` (e.g. always, on\_failure)
  - `trigger_surface` (e.g. tick, input)
  - `actor_mindset` (e.g. scripted, deliberative)

These tags are validated using `tags_vocab.json` and applied in both:

- `@tags`: in module headers
- `ai_tags`: in runtime debug logs

---

────────────────────────────────────────────── 🤖 AI BEHAVIOR IN ARCHITECTURE ──────────────────────────────────────────────

AI tools are allowed to generate architectural output only under **STRUCTURE mode**, with these boundaries:

✅ Can:

- Output `roadmap.json` and `architecture_index.json`
- Use existing contract files and tag vocabularies
- Propose build sequences and replacement chains

❌ Cannot:

- Generate code or filenames before block resolution
- Reference undeclared modules, layers, or paths
- Skip adapters, tags, or trace IDs
- Speculate, stub, or assume

If a tag, contract, or adapter is missing, AI must **halt** — not workaround.

---

────────────────────────────────────────────── 📘 REQUIRED DOCUMENTS & ARTIFACTS ──────────────────────────────────────────────

To operate correctly, this architecture layer requires:

1. `framework_architecture.md` — this file
2. `tags_vocab.json` — all valid tags
3. `roadmap.json` — milestones and blocks
4. `architecture_index.json` — modules, paths, sequence
5. `contracts/*.md` — what each module does and requires

No other documents may declare build order, file paths, or logic ownership.

---

🟢 Once these files are complete and locked, planning may begin. All implementation must follow the sequencing, status, and contracts declared here.

