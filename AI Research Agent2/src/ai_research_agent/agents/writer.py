"""Writer agent skeleton."""

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.graph.state import ResearchState


class WriterAgent(BaseAgent):
    """Produces the final report from validated evidence."""

    metadata = AgentMetadata(
        name="writer",
        responsibility="Generate the final response in the expected output format.",
    )

    def run(self, state: ResearchState) -> ResearchState:
        state.draft_report = "Report generation is intentionally deferred."
        state.status = "completed"
        return state
