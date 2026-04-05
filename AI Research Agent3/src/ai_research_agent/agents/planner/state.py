"""State models owned by the planner agent."""

from pydantic import BaseModel, Field

from ai_research_agent.graph.state import ResearchTask


class PlannerOutput(BaseModel):
    """Structured planner output written back to the workflow state."""

    tasks: list[ResearchTask] = Field(default_factory=list)
    planning_summary: str
