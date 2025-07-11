# sword_weirdos/core/loot_engine.py

import random
from copy import deepcopy
from ParetoDebug.adapters.debug_adapter import get_debugger, generate_trace_id
from typing import Optional

# @tags: ["inventory", "item_data", "runtime_behavior", "input"]
# @status: "stable"
def roll_loot(loot_table: dict, trace_id:  Optional[str] = None) -> dict:
    """Selects a random item from the provided loot table."""
    trace_id = trace_id or generate_trace_id()
    dbg = get_debugger("core/loot_engine")

    if not loot_table or "items" not in loot_table or not loot_table["items"]:
        dbg(
            action="loot_table_invalid",
            state={"has_items": "items" in loot_table, "count": len(loot_table.get("items", []))},
            ai_tags=["inventory", "item_data", "runtime_behavior", "input"],
            trace_id=trace_id
        )
        return {}

    item = deepcopy(random.choice(loot_table["items"]))
    dbg(
        action="select_loot",
        data={"item": item},
        ai_tags=["inventory", "item_data", "runtime_behavior", "input"],
        trace_id=trace_id
    )
    return item
