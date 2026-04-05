"""Base abstractions for the tool framework."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from pydantic import BaseModel, Field


class ToolResult(BaseModel):
    """Single normalized search result returned by a tool."""

    title: str
    snippet: str
    url: str
    source: str


class ToolInput(BaseModel):
    """Input payload for tool execution."""

    query: str
    max_results: int = Field(default=3, ge=1, le=10)


@dataclass
class ToolMetadata:
    """Metadata describing a research tool."""

    name: str
    category: str
    description: str


class BaseResearchTool(ABC):
    """Abstract base class for all research tools."""

    metadata: ToolMetadata

    @abstractmethod
    def search(self, tool_input: ToolInput) -> List[ToolResult]:
        """Execute a search and return normalized results."""
