"""High-level LangGraph workflow skeleton."""

from typing import Dict, Union

from langgraph.graph import END, START, StateGraph

from ai_research_agent.agents.planner import PlannerAgent
from ai_research_agent.agents.researcher import ResearcherAgent
from ai_research_agent.agents.reviewer import ReviewerAgent
from ai_research_agent.agents.supervisor import SupervisorAgent
from ai_research_agent.agents.writer import WriterAgent
from ai_research_agent.core.config import get_settings
from ai_research_agent.graph.state import ResearchState, create_initial_state


def _run_supervisor_node(
    state: Union[ResearchState, Dict[str, object]],
) -> Dict[str, object]:
    """Adapt LangGraph state payloads to the Supervisor agent interface."""

    supervisor = SupervisorAgent()
    research_state = ResearchState.model_validate(state)
    return supervisor.run(research_state).model_dump()


def _run_planner_node(
    state: Union[ResearchState, Dict[str, object]],
) -> Dict[str, object]:
    """Adapt LangGraph state payloads to the Planner agent interface."""

    planner = PlannerAgent()
    research_state = ResearchState.model_validate(state)
    return planner.run(research_state).model_dump()


def _run_researcher_node(
    state: Union[ResearchState, Dict[str, object]],
) -> Dict[str, object]:
    """Adapt LangGraph state payloads to the Researcher agent interface."""

    researcher = ResearcherAgent()
    research_state = ResearchState.model_validate(state)
    return researcher.run(research_state).model_dump()


def _run_reviewer_node(
    state: Union[ResearchState, Dict[str, object]],
) -> Dict[str, object]:
    """Adapt LangGraph state payloads to the Reviewer agent interface."""

    reviewer = ReviewerAgent()
    research_state = ResearchState.model_validate(state)
    return reviewer.run(research_state).model_dump()


def _run_writer_node(
    state: Union[ResearchState, Dict[str, object]],
) -> Dict[str, object]:
    """Adapt LangGraph state payloads to the Writer agent interface."""

    writer = WriterAgent()
    research_state = ResearchState.model_validate(state)
    return writer.run(research_state).model_dump()


def _route_after_review(state: Union[ResearchState, Dict[str, object]]) -> str:
    """Route workflow after review."""

    research_state = ResearchState.model_validate(state)
    if research_state.review_decision == "retry":
        return "researcher"
    return "writer"


def build_research_graph() -> StateGraph:
    """Build the implemented workflow for the current milestone."""

    graph = StateGraph(ResearchState)
    graph.add_node("supervisor", _run_supervisor_node)
    graph.add_node("planner", _run_planner_node)
    graph.add_node("researcher", _run_researcher_node)
    graph.add_node("reviewer", _run_reviewer_node)
    graph.add_node("writer", _run_writer_node)

    graph.add_edge(START, "supervisor")
    graph.add_edge("supervisor", "planner")
    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "reviewer")
    graph.add_conditional_edges(
        "reviewer",
        _route_after_review,
        {
            "researcher": "researcher",
            "writer": "writer",
        },
    )
    graph.add_edge("writer", END)

    return graph


def run_research_workflow(
    user_query: str,
    session_id: str = "session-001",
) -> ResearchState:
    """Run the current workflow from a raw user query."""

    settings = get_settings()
    compiled_graph = build_research_graph().compile()
    result = compiled_graph.invoke(
        create_initial_state(
            user_query,
            session_id,
            max_reflections=settings.research_max_iterations,
        ).model_dump()
    )
    return ResearchState.model_validate(result)
