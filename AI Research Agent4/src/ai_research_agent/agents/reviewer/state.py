"""State models owned by the reviewer agent."""

from pydantic import BaseModel

from ai_research_agent.graph.state import ReviewDecision


class ReviewerOutput(BaseModel):
    """Structured reviewer output written back to shared state."""

    decision: ReviewDecision
    reason: str
