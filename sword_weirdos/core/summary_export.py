# sword_weirdos/core/summary_export.py

from typing import Optional
from ParetoDebug.adapters.debug_adapter import get_debugger, generate_trace_id

# @tags: ["system", "char_data", "render_contract", "input"]
# @status: "stable"
def generate_summary(character: dict, trace_id: Optional[str] = None) -> str:
    """Generates a formatted character status summary block for display."""
    trace_id = trace_id or generate_trace_id()
    dbg = get_debugger("core/summary_export")

    name = character.get("name", "Unnamed")
    char_class = character.get("class", "Unknown Class")
    stats = character.get("stats", {})
    combat = stats.get("combat", 0)
    grit = stats.get("grit", 0)
    move = stats.get("move", 0)
    hp = stats.get("hp", 0)
    max_hp = stats.get("max_hp", 0)
    stress = stats.get("stress", 0)

    status = character.get("status", [])
    inventory = character.get("inventory", [])
    traits = character.get("traits", [])

    block = [
        "=== CHARACTER STATUS ===",
        f"Name: {name}",
        f"Class: {char_class}",
        f"Combat: +{combat} | Grit: +{grit} | Move: +{move}",
        f"HP: {hp}/{max_hp} | Stress: {stress}",
        f"Status: {', '.join(status) if status else 'None'}",
        f"Inventory: {', '.join(inventory) if inventory else 'Empty'}",
        f"Traits: {', '.join(traits) if traits else 'None'}"
    ]

    result = "\n".join(block)

    dbg(
        action="generate_summary",
        state={"character": name, "has_traits": bool(traits), "inventory_count": len(inventory)},
        ai_tags=["system", "char_data", "render_contract", "input"],
        trace_id=trace_id
    )

    return result
