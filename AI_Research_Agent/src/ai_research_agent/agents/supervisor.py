"""Supervisor agent skeleton."""

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.graph.state import ResearchState


class SupervisorAgent(BaseAgent):
    """Coordinates graph routing and termination conditions."""

    metadata = AgentMetadata(
        name="supervisor",
        responsibility="Route state transitions and enforce execution policy.",
    )

    def run(self, state: ResearchState) -> ResearchState:
        state.status = "planning"
        return state
