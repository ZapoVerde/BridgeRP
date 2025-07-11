# sword_weirdos/ui_cli/main_menu.py

from typing import Optional
import json

from sword_weirdos.core.character_cards import (
    load_character,
    save_character,
    apply_status,
    update_stat,
)
from sword_weirdos.core.loot_engine import roll_loot
from sword_weirdos.core.summary_export import generate_summary
from ParetoDebug.adapters.debug_adapter import get_debugger, generate_trace_id

CHARACTER_PATH = "sword_weirdos/data/characters/karra.json"
LOOT_TABLE_PATH = "sword_weirdos/data/loot_table.json"

# @tags: ["system", "char_data", "runtime_behavior", "input"]
# @status: "stable"
def main_menu(trace_id: Optional[str] = None):
    """Launches the main tracker menu for character interaction."""
    trace_id = trace_id or generate_trace_id()
    dbg = get_debugger("ui_cli/main_menu")

    character = load_character(CHARACTER_PATH)
    try:
        with open(LOOT_TABLE_PATH, "r") as f:
            loot_table = json.load(f)
    except Exception as e:
        dbg(
            action="error_occurred",
            data={"exception": str(e)},
            state={"loot_table_path": LOOT_TABLE_PATH},
            ai_tags=["system", "char_data", "runtime_behavior", "init"],
            trace_id=trace_id
        )
        loot_table = {"items": []}

    dbg(
        action="enter_main_menu",
        state={"character_loaded": character.get("name", "Unknown")},
        ai_tags=["system", "char_data", "runtime_behavior", "init"],
        trace_id=trace_id
    )

    while True:
        print("\n=== TRACKER MENU ===")
        print("1. View summary")
        print("2. Update HP / Stress")
        print("3. Add status")
        print("4. Remove status")
        print("5. View inventory")
        print("6. Roll loot")
        print("7. Export summary")
        print("8. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            summary = generate_summary(character, trace_id=trace_id)
            print(summary)

        elif choice == "2":
            field = input("Field to update (hp/stress): ").strip().lower()
            delta = int(input("Change by (e.g. -2 or 5): "))
            update_stat(character, field, delta, trace_id=trace_id)

        elif choice == "3":
            status = input("Enter status to add: ").strip()
            apply_status(character, status, trace_id=trace_id)

        elif choice == "4":
            status = input("Enter status to remove: ").strip()
            if "status" in character and status in character["status"]:
                character["status"].remove(status)
                dbg(
                    action="remove_status",
                    state={"status_removed": status},
                    ai_tags=["system", "char_data", "runtime_behavior", "input"],
                    trace_id=trace_id
                )

        elif choice == "5":
            print("Inventory:", ", ".join(character.get("inventory", [])))

        elif choice == "6":
            item = roll_loot(loot_table, trace_id=trace_id)
            if item:
                character.setdefault("inventory", []).append(item["name"])
                print(f"You gained: {item['name']}")
                dbg(
                    action="add_loot_item",
                    state={"item_name": item["name"]},
                    ai_tags=["inventory", "item_data", "runtime_behavior", "input"],
                    trace_id=trace_id
                )

        elif choice == "7":
            print(generate_summary(character, trace_id=trace_id))

        elif choice == "8":
            save_character(CHARACTER_PATH, character)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
