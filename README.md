# BridgeRP

**BridgeRP** is a modular Roleplay Bridge Engine that links structured character state to visual output. It enables dynamic, persistent avatars across LLM-based storytelling tools like SillyTavern, JanitorAI, and more.

> Think of it as an offline visual memory engine for your characters — layering pose, outfit, expression, and state to produce fast, consistent renders.

---

## 🔧 Features

* 🧠 **Persistent character state** (memory, traits, conditions, etc.)
* 🖼️ **Layered image composition** (pose + outfit + expression + overlays)
* ⚡ **Fast local rendering** — no GPU or web calls required
* 🔌 **Adapter-friendly** — can integrate with any LLM or frontend
* 🛠️ **Extensible design** — portable JSON state, modular folders

---

## 📂 Project Structure

```
BridgeRP/
├── core/           # Render and stack engine
├── state/          # Memory and condition tracking
├── adapters/       # Interfaces for SillyTavern, CLI, etc.
├── assets/         # PNG layers organized by character
├── outputs/        # Final rendered frames
└── README.md
```

---

## 🛠️ Getting Started

> Run standalone or attach to an existing RP setup.

1. Place your character layers in `assets/`
2. Create a `character_state.json` file describing pose, outfit, etc.
3. Run the renderer (coming soon)
4. View the output frame in `outputs/`

---

## 🔗 Integrations

* SillyTavern (via watched JSON files or custom button)
* Local bots (e.g. OpenRouter, JanitorAI)
* TTRPG tools, VNs, Discord bots

---

## 📄 License

MIT License © 2025 [ZapoVerde](https://github.com/ZapoVerde)

---

## ⚠️ Status

BridgeRP is in early development. Core rendering and state management are coming next. Stay tuned!
