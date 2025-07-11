# Project Goals: Adrift

## 🎯 Vision
Adrift is a modular, simulation-driven, tick-based RPG designed for extensibility and long-term AI co-development. It blends tactical ASCII gameplay with deep systemic interaction, allowing the player to explore, act, and evolve in a hostile world with minimal narrative scaffolding. The architecture is intentionally layered, decoupled, and deterministic to support replayability, modding, and AI-authored content.

## 🧱 Scope Boundaries
- Not multiplayer
- Not a full roguelike — death is not final by default
- No 3D rendering or complex physics
- ASCII-first rendering (sprite layer may evolve later)
- Single-world persistence — no procedural overworlds

## 🚦 Priorities
- MVP-first: early delivery of basic gameplay loop
- Modular evolution: systems like perception, combat, or mutation must evolve cleanly
- Full AI participation: assistant may build new systems as long as contract is followed
- Serialization and traceability are mandatory at all layers

## 🔁 Longevity Goals
- Game should be expandable without rewriting core systems
- Dead-end modules must be safely discardable via adapters
- Feature growth should follow roadmap and evolve cleanly
- Systems like skill trees, social AI, or factions can be layered on after MVP

## 🧠 AI Developer Role
- The assistant is the primary developer
- Must follow locked architecture (`game_architecture.txt`) and modularity rules
- No unauthorized changes to PERMANENT systems
- All code must be tagged and traceable
- Debugging hooks and test scaffolds must be included

## ✅ Success Criteria
- A player can: input commands, receive output, observe game state changes, and act
- Core loop runs deterministically by tick
- Combat, movement, messaging, and render all exist
- State can be saved and reloaded as JSON
- AI can extend gameplay via new actions, skills, or entity types without violating structure

