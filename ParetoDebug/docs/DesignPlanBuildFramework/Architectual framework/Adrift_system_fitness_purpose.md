# System Fitness Purpose: Adrift

## Purpose

This document defines the minimum functional capabilities that the Adrift architecture must support. These statements represent the **operational contract** — the behaviors the software must deliver to be considered fit for purpose.

This file is referenced during all Design Fitness audits.

---

## Minimum Functional Expectations

The system must:

1. Accept and interpret player input

   - Translate user actions into structured in-game effects via the Interface layer

2. Advance simulation by deterministic ticks

   - A tick loop must process time-based updates with no floating-point or real-time dependency

3. Modify and persist game state

   - All changes must occur via `world_state`
   - The game state must be serializable to and from JSON

4. Support basic interactivity

   - The player must be able to move, perceive, act, and receive feedback
   - Actors must respond to game events (e.g., combat, detection)

5. Represent spatial structure internally

   - The game world must expose coordinate-based spatial access
   - All entities must have locatable positions within a shared model
   - Spatial structure must support adjacency and pathfinding

6. Maintain actor-specific state tracking

   - Each actor must track its own stats, memory, and visibility
   - Per-actor data must be persistable within `world_state`

7. Support turn-phase modeling

   - Core simulation must support phased logic (e.g., perception → action → cleanup)
   - Each tick must respect actor initiative and latency ordering

   - The player must be able to move, perceive, act, and receive feedback
   - Actors must respond to game events (e.g., combat, detection)

---

## Interface Evolution Requirements

The architecture must support a staged output evolution:

1. **Text output only**

   - Initial interface accepts text commands and prints feedback.
   - Enables rapid prototyping and early logic testing.

2. **ASCII tactical interface**

   - Replaces text-only output with a tile-based ASCII renderer.
   - Actors, items, and zones must be visually representable using fixed-width glyphs.
   - Rendering must reflect spatial relationships and visibility rules.

3. **2D graphical interface**

   - Final implementation must support RimWorld-style top-down graphics.
   - System must support frame-based rendering, layered tilemaps, and viewport logic.

At all stages, the rendering interface must be swappable without changes to simulation logic.

---

## Required System Components

To fulfill this contract, the architecture must include:

- A tick controller and dispatcher
- A command interpreter or input adapter
- A world state container (`world_state`) used globally
- A JSON save/load mechanism

All components must be represented in the planned architecture before planning begins.

---

## Audit Alignment

This document is referenced by:

- `auditor_behavior_profile.md` (Design Fitness phase)
- `architecture_audit_protocol.md` (fitness checklist)

---

## Version

Canonical: `docs/system_fitness_purpose.md`\
Last updated: 2025-07-05

