"""Researcher agent skeleton."""

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.graph.state import ResearchState


class ResearcherAgent(BaseAgent):
    """Collects information and stores evidence in the shared state."""

    metadata = AgentMetadata(
        name="researcher",
        responsibility="Retrieve evidence from tools, memory, and knowledge stores.",
    )

    def run(self, state: ResearchState) -> ResearchState:
        state.evidence.append("Evidence collection is intentionally not implemented yet.")
        state.status = "reviewing"
        return state
