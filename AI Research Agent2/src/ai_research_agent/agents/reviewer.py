"""Reviewer agent skeleton."""

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.graph.state import ResearchState


class ReviewerAgent(BaseAgent):
    """Validates the plan and evidence quality before report generation."""

    metadata = AgentMetadata(
        name="reviewer",
        responsibility="Check evidence quality, detect gaps, and request retries.",
    )

    def run(self, state: ResearchState) -> ResearchState:
        state.review_notes.append("Review logic is not implemented in the first iteration.")
        state.status = "writing"
        return state
