"""Agent definitions for the LangGraph workflow."""

from typing import Any

__all__ = ["PlannerAgent", "SupervisorAgent"]


def __getattr__(name: str) -> Any:
    """Lazily expose top-level agent classes without import-time cycles."""

    if name == "PlannerAgent":
        from ai_research_agent.agents.planner import PlannerAgent

        return PlannerAgent
    if name == "SupervisorAgent":
        from ai_research_agent.agents.supervisor import SupervisorAgent

        return SupervisorAgent
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
