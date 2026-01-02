"""High-level LangGraph workflow skeleton."""

from langgraph.graph import END, START, StateGraph

from ai_research_agent.agents.memory_manager import MemoryManagerAgent
from ai_research_agent.agents.planner import PlannerAgent
from ai_research_agent.agents.researcher import ResearcherAgent
from ai_research_agent.agents.reviewer import ReviewerAgent
from ai_research_agent.agents.supervisor import SupervisorAgent
from ai_research_agent.agents.writer import WriterAgent
from ai_research_agent.graph.state import ResearchState


def build_research_graph() -> StateGraph:
    """Build the first-pass workflow graph for the research agent."""

    graph = StateGraph(ResearchState)

    supervisor = SupervisorAgent()
    memory_manager = MemoryManagerAgent()
    planner = PlannerAgent()
    researcher = ResearcherAgent()
    reviewer = ReviewerAgent()
    writer = WriterAgent()

    graph.add_node("supervisor", supervisor.run)
    graph.add_node("memory_manager", memory_manager.run)
    graph.add_node("planner", planner.run)
    graph.add_node("researcher", researcher.run)
    graph.add_node("reviewer", reviewer.run)
    graph.add_node("writer", writer.run)

    graph.add_edge(START, "memory_manager")
    graph.add_edge("memory_manager", "supervisor")
    graph.add_edge("supervisor", "planner")
    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "reviewer")
    graph.add_edge("reviewer", "writer")
    graph.add_edge("writer", END)

    return graph
