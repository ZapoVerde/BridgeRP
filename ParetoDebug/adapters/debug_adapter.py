# ParetoDebug/adapters/debug_adapter.py
# [AI], [ADAPTER]
# Role: Mediates access to [DEAD-END] or cross-layer systems
# @tags:
#   domain: UI
#   data_affinity: actor_data
#   scope_horizon: mvp
#   semantic_role: render_contract

from ParetoDebug.debug_core.debug_shared import Debugger

from ParetoDebug.debug_core.trace_utils import generate_trace_id as _generate_trace_id
from ParetoDebug.debug_core.trace_decorators import debug_trace

# Global fallback debugger (used if no specific context is supplied)
_global_debugger = Debugger("global/default")


def debug(action, data=None, state=None, ai_tags=None, print_console=False, trace_id=None):
    """Routes a debug call to the global fallback debugger.

    Use only when context is not meaningful. All important logs should use get_debugger().
    
    @tags: ["debug", "fallback", "UI", "runtime_behavior"]
    @status: "stable"
    """
    return _global_debugger(
        action=action,
        data=data,
        state=state,
        ai_tags=ai_tags,
        print_console=print_console,
        trace_id=trace_id
    )


def generate_trace_id() -> str:
    """Generates a unique trace ID for linking debug entries.

    All major flow calls (e.g. combat turns, AI decisions) should begin by calling this.
    
    @tags: ["debug", "trace", "UI", "mvp"]
    @status: "stable"
    """
    return _generate_trace_id()

def get_debugger(context: str):
    """Returns a context-bound debugger instance from ParetoDebug.

    Use this if you want fine-grained control over where logs go.
    """
    return Debugger(context)


__all__ = ["debug", "get_debugger", "generate_trace_id", "debug_trace"]

# Unified interface
__all__ = ["debug", "get_debugger", "generate_trace_id", "debug_trace"]
