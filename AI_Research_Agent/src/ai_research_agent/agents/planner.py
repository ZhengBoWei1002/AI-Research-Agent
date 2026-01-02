"""Planner agent skeleton."""

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.graph.state import ResearchState


class PlannerAgent(BaseAgent):
    """Transforms a user query into an executable research plan."""

    metadata = AgentMetadata(
        name="planner",
        responsibility="Decompose the task into research steps and success criteria.",
    )

    def run(self, state: ResearchState) -> ResearchState:
        state.plan = ["Clarify scope", "Collect evidence", "Synthesize findings"]
        state.status = "researching"
        return state
