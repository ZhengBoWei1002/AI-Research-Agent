"""Base abstractions for all agents."""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ai_research_agent.graph.state import ResearchState


@dataclass(slots=True)
class AgentMetadata:
    """Common metadata describing an agent role."""

    name: str
    responsibility: str


class BaseAgent(ABC):
    """Base class for all specialized agents."""

    metadata: AgentMetadata

    @abstractmethod
    def run(self, state: ResearchState) -> ResearchState:
        """Process the current state and return the updated state."""
