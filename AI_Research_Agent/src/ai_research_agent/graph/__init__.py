"""LangGraph workflow definitions."""

from typing import Any

__all__ = ["build_research_graph", "run_research_workflow"]


def __getattr__(name: str) -> Any:
    """Lazily expose workflow helpers without eager import side effects."""

    if name == "build_research_graph":
        from ai_research_agent.graph.workflow import build_research_graph

        return build_research_graph
    if name == "run_research_workflow":
        from ai_research_agent.graph.workflow import run_research_workflow

        return run_research_workflow
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
