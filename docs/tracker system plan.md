📌 FINALIZED MVP STRUCTURE — Sword Weirdos RPG Tracker (Phase 1–2)

SwordWeirdosTracker/
│
├── run.py                          # Entry point for CLI engine
│
├── core/                           # Pure logic modules (no I/O or CLI)
│   ├── character\_cards.py          # Load/save/edit persistent character JSONs
│   ├── party\_manager.py            # Assemble party from available characters
│   ├── encounter\_tracker.py        # Enemy HP/status, turn order, actions
│   ├── loot\_engine.py              # Loot rolls + item generation
│   ├── summary\_export.py           # Formats AI-friendly summary text
│   ├── registries.py               # Loot tables, status effects, traits
│   └── hooks.py                    # (future) dispatchers for phase hooks
│
├── data/                           # Persistent world and game data
│   ├── characters/                 # One JSON file per character
│   │   ├── karra.json
│   │   ├── jorran.json
│   │   └── ...
│   ├── loot\_table.json            # Structured drop tables
│   ├── town\_npcs.json             # Town interactions and shops
│   ├── party.json                 # Active party (IDs only)
│   ├── enemies.json               # Active encounter snapshot
│   └── settings.json              # Global constants (e.g. max party size)
│
├── ui\_cli/                         # CLI menu routing
│   ├── main\_menu.py               # Entry interface for user
│   ├── character\_menu.py          # View/edit character data
│   ├── party\_menu.py              # Assemble, view, update party
│   ├── encounter\_menu.py          # Run encounters, track turns
│   └── loot\_menu.py               # Roll loot, assign to inventory
│
├── ui\_web/                         # (future) HTML/JS GUI
│   ├── index.html
│   ├── app.js
│   └── styles.css
│
├── assets/                         # Visual render assets (portraits, overlays)
│   ├── portraits/
│   ├── backgrounds/
│   └── overlays/
│
└── docs/                           # Design and governance
├── architecture\_manifest.md   # Core modularity rules and tags
├── phase\_plan.md              # Roadmap and module goals
└── world\_notes.md             # Lore, names, factions, tags

📊 FUNCTIONAL BLOCK DIAGRAM — Tracker System (Phase 1–2)

┌────────────────────────────────────────────┐
│        SillyTavern / ChatGPT              │
│     (AI narrator with no memory burden)   │
└──────────────┬────────────────────────────┘
│  (reads GPT summary block)
▼
┌──────────────────────────────┐
│     summary\_export.py        │◄──────┐
└────────┬─────────────┬───────┘       │
│             │               │
┌──────────▼───────┐ ┌────▼────────────┐ │
│ character\_cards  │ │ party\_manager   │ │
│ (persistent JSON)│ │ (expedition prep)│ │
└──────────┬───────┘ └─────────┬────────┘ │
│                   │          │
┌───────▼─────────┐ ┌───────▼─────────┐ │
│ encounter\_tracker│ │ loot\_engine     │ │
│ (enemies, turns) │ │ (rolls/items)   │ │
└────────▲────────┘ └─────────────────┘ │
│                              │
┌──────────┴─────────────┐                │
│      CLI Interface     │ ───────────────┘
└────────────────────────┘

✅ MVP SPEC (Minimum Viable Product — Phase 1 Full)

🎯 Purpose:
A single-character offline tracker to accompany AI-narrated RPG gameplay.
Keeps stats, inventory, and combat state externally, outputs clean GPT summaries.

🔹 Features:

* Load a single character from `data/characters/`
* Track HP, stress, traits, status effects
* View/edit inventory
* Roll loot from `loot_table.json`
* Add/remove simple effects (e.g., "wounded", "suppressed")
* Export a clean GPT paste summary (for SillyTavern use)

🛠 Module Summary:

* `character_cards.py`: Flat dict, JSON-based stat storage
* `loot_engine.py`: Random d6 rolls, item dicts
* `summary_export.py`: Pretty text summary
* `main_menu.py` and `character_menu.py`: CLI interaction only

🧠 MVP Rules:

* No persistent party yet — just one character
* No combat mechanics — just state tracking
* No world state — JSON is ground truth

✅ Output should look like:

```
=== CHARACTER STATUS ===
Name: Karra
Class: Bone Witch
Combat: +2 | Grit: +1 | Move: +1
HP: 6/10 | Stress: 1
Status: Wounded, Suppressed
Inventory: Bone Wand, Healing Salve, 7 Coins
Traits: Vengeful, Loyal
```
