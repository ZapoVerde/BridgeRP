# sword_weirdos/core/character_cards.py

import json
import traceback
from typing import Optional
from ParetoDebug.adapters.debug_adapter import get_debugger, generate_trace_id

# @tags: ["system", "char_data", "runtime_behavior", "init"]
# @status: "stable"
def load_character(file_path: str) -> dict:
    """Loads character data from a JSON file."""
    trace_id = generate_trace_id()
    dbg = get_debugger("core/character_cards")

    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            dbg(
                action="load_character",
                state={"path": file_path},
                ai_tags=["system", "char_data", "runtime_behavior", "init"],
                trace_id=trace_id
            )
            return data
    except FileNotFoundError as e:
        dbg(
            action="error_occurred",
            data={"exception": str(e)},
            state={"traceback": traceback.format_exc()},
            ai_tags=["system", "char_data", "runtime_behavior", "init"],
            trace_id=trace_id
        )
        return {}
    except json.JSONDecodeError as e:
        dbg(
            action="error_occurred",
            data={"exception": str(e)},
            state={"traceback": traceback.format_exc()},
            ai_tags=["system", "char_data", "runtime_behavior", "init"],
            trace_id=trace_id
        )
        return {}

# @tags: ["system", "char_data", "runtime_behavior", "input"]
# @status: "stable"
def save_character(file_path: str, data: dict):
    """Saves character data to a JSON file."""
    trace_id = generate_trace_id()
    dbg = get_debugger("core/character_cards")

    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)
            dbg(
                action="save_character",
                state={"path": file_path},
                ai_tags=["system", "char_data", "runtime_behavior", "input"],
                trace_id=trace_id
            )
    except Exception as e:
        dbg(
            action="error_occurred",
            data={"exception": str(e)},
            state={"traceback": traceback.format_exc()},
            ai_tags=["system", "char_data", "runtime_behavior", "input"],
            trace_id=trace_id
        )

# @tags: ["system", "status_data", "runtime_behavior", "input"]
# @status: "stable"
def apply_status(character: dict, status: str, trace_id: Optional[str] = None):
    """Adds a status to the character if not already present."""
    trace_id = trace_id or generate_trace_id()
    dbg = get_debugger("core/character_cards")

    if "status" not in character:
        character["status"] = []

    if status not in character["status"]:
        character["status"].append(status)
        dbg(
            action="apply_status",
            state={"status_added": status, "current_status": character["status"]},
            ai_tags=["system", "status_data", "runtime_behavior", "input"],
            trace_id=trace_id
        )

# @tags: ["system", "char_data", "runtime_behavior", "input"]
# @status: "stable"
def update_stat(character: dict, field: str, delta: int, trace_id:Optional[str] = None):
    """Modifies a stat by a delta value."""
    trace_id = trace_id or generate_trace_id()
    dbg = get_debugger("core/character_cards")

    if "stats" not in character or field not in character["stats"]:
        dbg(
            action="stat_missing",
            state={"field": field, "has_stats": "stats" in character},
            ai_tags=["system", "char_data", "runtime_behavior", "input"],
            trace_id=trace_id
        )
        return

    original = character["stats"][field]
    character["stats"][field] += delta
    dbg(
        action="update_stat",
        state={
            "field": field,
            "old_value": original,
            "delta": delta,
            "new_value": character["stats"][field]
        },
        ai_tags=["system", "char_data", "runtime_behavior", "input"],
        trace_id=trace_id
    )
