"""Shared LangGraph state models."""

from typing import Literal

from pydantic import BaseModel, Field


WorkflowStatus = Literal["initialized", "planning", "completed", "failed"]
TaskStatus = Literal["pending", "planned"]


class ResearchTask(BaseModel):
    """Single task produced by the planning phase."""

    task_id: str
    title: str
    objective: str
    rationale: str
    status: TaskStatus = Field(default="pending")


class ResearchState(BaseModel):
    """Serializable state passed between graph nodes."""

    session_id: str = Field(default="uninitialized")
    user_query: str = Field(default="")
    normalized_query: str = Field(default="")
    supervisor_notes: list[str] = Field(default_factory=list)
    tasks: list[ResearchTask] = Field(default_factory=list)
    plan: list[str] = Field(default_factory=list)
    planning_summary: str = Field(default="")
    status: WorkflowStatus = Field(default="initialized")


def create_initial_state(user_query: str, session_id: str = "session-001") -> ResearchState:
    """Create a workflow state from the incoming user request."""

    return ResearchState(session_id=session_id, user_query=user_query)
