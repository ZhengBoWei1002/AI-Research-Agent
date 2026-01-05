"""State models owned by the supervisor agent."""

from typing import Literal

from pydantic import BaseModel, Field


class SupervisorDecision(BaseModel):
    """Decision payload produced by the supervisor."""

    normalized_query: str
    notes: list[str] = Field(default_factory=list)
    next_status: Literal["planning", "failed"] = "planning"
