"""State models owned by the researcher agent."""

from pydantic import BaseModel, Field

from ai_research_agent.graph.state import Evidence, ToolCallRecord


class ResearcherOutput(BaseModel):
    """Structured researcher output written back to shared state."""

    evidence: list[Evidence] = Field(default_factory=list)
    tool_calls: list[ToolCallRecord] = Field(default_factory=list)
    researcher_summary: str
