"""Shared LangGraph state models."""

from typing import Literal

from pydantic import BaseModel, Field


WorkflowStatus = Literal[
    "initialized",
    "planning",
    "researching",
    "reviewing",
    "writing",
    "completed",
    "failed",
]


class ResearchState(BaseModel):
    """Serializable state passed between graph nodes."""

    session_id: str = Field(default="uninitialized")
    user_query: str = Field(default="")
    plan: list[str] = Field(default_factory=list)
    evidence: list[str] = Field(default_factory=list)
    review_notes: list[str] = Field(default_factory=list)
    draft_report: str = Field(default="")
    status: WorkflowStatus = Field(default="initialized")
