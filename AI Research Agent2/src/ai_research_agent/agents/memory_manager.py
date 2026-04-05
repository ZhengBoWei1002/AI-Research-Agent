"""Memory manager agent skeleton."""

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.graph.state import ResearchState


class MemoryManagerAgent(BaseAgent):
    """Owns conversation memory, long-term memory, and retrieval coordination."""

    metadata = AgentMetadata(
        name="memory_manager",
        responsibility="Persist state snapshots and manage retrieval context.",
    )

    def run(self, state: ResearchState) -> ResearchState:
        return state
