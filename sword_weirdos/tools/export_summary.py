# sword_weirdos/tools/export_summary.py

"""
Export character summary and copy to system clipboard for SillyTavern.

@tags: ["system", "actor_data", "render_contract", "input"]
@status: "mvp"
"""

import platform
import subprocess
from typing import Optional

from sword_weirdos.core.character_cards import load_character
from sword_weirdos.core.summary_export import generate_summary
from ParetoDebug.adapters.debug_adapter import get_debugger, generate_trace_id

CHARACTER_PATH = "data/karra.json"

def copy_to_clipboard(text: str, trace_id: Optional[str] = None) -> None:
    """
    Copy the given text to the system clipboard using OS-native utilities.

    @tags: ["system", "actor_data", "runtime_behavior", "input"]
    """
    dbg = get_debugger("tools/export_summary")
    system = platform.system()

    try:
        if system == "Windows":
            subprocess.run("clip", text=True, input=text, check=True)
        elif system == "Darwin":
            subprocess.run("pbcopy", text=True, input=text, check=True)
        else:  # Assume Linux
            subprocess.run("xclip -selection clipboard", shell=True, input=text.encode(), check=True)

        dbg(
            action="copy_summary",
            state={"os": system},
            trace_id=trace_id,
            ai_tags=["system", "actor_data", "mvp", "runtime_behavior"]
        )
    except Exception as e:
        dbg(
            action="error_occurred",
            data={"exception": str(e)},
            state={"os": system},
            trace_id=trace_id,
            ai_tags=["system", "actor_data", "mvp", "runtime_behavior"]
        )
        print("[Clipboard] Failed to copy. See debug logs.")

def export_summary_to_clipboard():
    """
    Load a character, generate summary, and copy to clipboard.

    @tags: ["system", "actor_data", "render_contract", "input"]
    """
    trace_id = generate_trace_id()
    dbg = get_debugger("tools/export_summary")

    try:
        character = load_character(CHARACTER_PATH)
        summary = generate_summary(character, trace_id)
        copy_to_clipboard(summary, trace_id)

        dbg(
            action="export_clipboard_summary",
            data={"length": len(summary)},
            trace_id=trace_id,
            ai_tags=["system", "actor_data", "mvp", "runtime_behavior"]
        )
        print("✅ Summary copied to clipboard. Paste into SillyTavern.")
    except Exception as e:
        dbg(
            action="error_occurred",
            data={"exception": str(e)},
            state={"step": "export_summary"},
            trace_id=trace_id,
            ai_tags=["system", "actor_data", "mvp", "runtime_behavior"]
        )
        print("[Clipboard] Export failed.")

if __name__ == "__main__":
    export_summary_to_clipboard()
