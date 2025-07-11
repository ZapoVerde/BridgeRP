# sword_weirdos/ui_cli/character_menu.py

from typing import Optional
from ParetoDebug.adapters.debug_adapter import get_debugger, generate_trace_id


def edit_stat(character: dict, field: str, value: int, trace_id: Optional[str] = None):
    """Directly sets a stat to a specific value.
    @tags: ["system", "char_data", "runtime_behavior", "input"]
    @status: "stable"
    """
    trace_id = trace_id or generate_trace_id()
    dbg = get_debugger("ui_cli/character_menu")

    if "stats" not in character or field not in character["stats"]:
        dbg(
            action="stat_missing",
            state={"field": field, "has_stats": "stats" in character},
            ai_tags=["system", "char_data", "runtime_behavior", "input"],
            trace_id=trace_id
        )
        return

    old = character["stats"][field]
    character["stats"][field] = value

    dbg(
        action="set_stat",
        state={"field": field, "old_value": old, "new_value": value},
        ai_tags=["system", "char_data", "runtime_behavior", "input"],
        trace_id=trace_id
    )


def add_inventory_item(character: dict, item: str, trace_id: Optional[str] = None):
    """Adds an item to the character's inventory.
    @tags: ["inventory", "item_data", "runtime_behavior", "input"]
    @status: "stable"
    """
    trace_id = trace_id or generate_trace_id()
    dbg = get_debugger("ui_cli/character_menu")

    character.setdefault("inventory", []).append(item)
    dbg(
        action="add_item",
        state={"item_added": item, "inventory_size": len(character["inventory"])},
        ai_tags=["inventory", "item_data", "runtime_behavior", "input"],
        trace_id=trace_id
    )


def remove_inventory_item(character: dict, item: str, trace_id: Optional[str] = None):
    """Removes an item from the character's inventory.
    @tags: ["inventory", "item_data", "runtime_behavior", "input"]
    @status: "stable"
    """
    trace_id = trace_id or generate_trace_id()
    dbg = get_debugger("ui_cli/character_menu")

    if "inventory" in character and item in character["inventory"]:
        character["inventory"].remove(item)
        dbg(
            action="remove_item",
            state={"item_removed": item, "inventory_size": len(character["inventory"])},
            ai_tags=["inventory", "item_data", "runtime_behavior", "input"],
            trace_id=trace_id
        )


def add_trait(character: dict, trait: str, trace_id: Optional[str] = None):
    """Adds a trait if not already present.
    @tags: ["system", "char_data", "runtime_behavior", "input"]
    @status: "stable"
    """
    trace_id = trace_id or generate_trace_id()
    dbg = get_debugger("ui_cli/character_menu")

    character.setdefault("traits", [])
    if trait not in character["traits"]:
        character["traits"].append(trait)
        dbg(
            action="add_trait",
            state={"trait_added": trait, "traits_count": len(character["traits"])},
            ai_tags=["system", "char_data", "runtime_behavior", "input"],
            trace_id=trace_id
        )


def remove_trait(character: dict, trait: str, trace_id: Optional[str] = None):
    """Removes a trait if present.
    @tags: ["system", "char_data", "runtime_behavior", "input"]
    @status: "stable"
    """
    trace_id = trace_id or generate_trace_id()
    dbg = get_debugger("ui_cli/character_menu")

    if "traits" in character and trait in character["traits"]:
        character["traits"].remove(trait)
        dbg(
            action="remove_trait",
            state={"trait_removed": trait, "traits_count": len(character["traits"])},
            ai_tags=["system", "char_data", "runtime_behavior", "input"],
            trace_id=trace_id
        )
