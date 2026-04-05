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
TaskStatus = Literal["pending", "planned", "researched"]
ReviewDecision = Literal["retry", "approve"]


class ResearchTask(BaseModel):
    """Single task produced by the planning phase."""

    task_id: str
    title: str
    objective: str
    rationale: str
    status: TaskStatus = Field(default="pending")


class ToolCallRecord(BaseModel):
    """Trace record for a tool invocation."""

    tool_name: str
    query: str
    success: bool
    result_count: int = Field(default=0)


class Evidence(BaseModel):
    """Evidence item aggregated by the researcher."""

    evidence_id: str
    task_id: str
    source: str
    title: str
    snippet: str
    url: str


class ReflectionRecord(BaseModel):
    """Trace entry for a reviewer reflection cycle."""

    iteration: int
    decision: ReviewDecision
    reason: str


class ResearchState(BaseModel):
    """Serializable state passed between graph nodes."""

    session_id: str = Field(default="uninitialized")
    user_query: str = Field(default="")
    normalized_query: str = Field(default="")
    supervisor_notes: list[str] = Field(default_factory=list)
    tasks: list[ResearchTask] = Field(default_factory=list)
    plan: list[str] = Field(default_factory=list)
    planning_summary: str = Field(default="")
    evidence: list[Evidence] = Field(default_factory=list)
    tool_calls: list[ToolCallRecord] = Field(default_factory=list)
    researcher_summary: str = Field(default="")
    review_decision: ReviewDecision = Field(default="retry")
    review_reason: str = Field(default="")
    review_notes: list[str] = Field(default_factory=list)
    reflection_count: int = Field(default=0)
    max_reflections: int = Field(default=2)
    reflection_history: list[ReflectionRecord] = Field(default_factory=list)
    reasoning_log: list[str] = Field(default_factory=list)
    transition_history: list[str] = Field(default_factory=list)
    latest_feedback: str = Field(default="")
    draft_report: str = Field(default="")
    status: WorkflowStatus = Field(default="initialized")


def create_initial_state(
    user_query: str,
    session_id: str = "session-001",
    max_reflections: int = 2,
) -> ResearchState:
    """Create a workflow state from the incoming user request."""

    return ResearchState(
        session_id=session_id,
        user_query=user_query,
        max_reflections=max_reflections,
        transition_history=["START"],
    )
