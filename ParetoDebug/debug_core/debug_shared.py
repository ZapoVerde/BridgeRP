# ParetoDebug/debug_core/debug_shared.py
# [AI]
# @tags:
#   domain: UI
#   data_affinity: actor_data
#   scope_horizon: mvp
#   semantic_role: connector

from ParetoDebug.debug_core.debugger import Debugger

def get_debugger(context: str) -> Debugger:
    """Returns a context-bound Debugger instance."""
    return Debugger(context)
