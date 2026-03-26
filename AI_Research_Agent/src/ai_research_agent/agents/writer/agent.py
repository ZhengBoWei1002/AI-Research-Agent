"""Writer agent implementation."""

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.agents.writer.prompt import WRITER_SYSTEM_PROMPT
from ai_research_agent.core.logging import get_logger
from ai_research_agent.graph.state import ResearchState


class WriterAgent(BaseAgent):
    """Produce a concise report draft from approved evidence."""

    metadata = AgentMetadata(
        name="writer",
        responsibility="Generate a structured report draft from reviewed evidence.",
    )

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    def run(self, state: ResearchState) -> ResearchState:
        """Create the current milestone report draft."""

        state.transition_history.append("Writer")
        state.status = "writing"
        state.draft_report = (
            f"Report draft for '{state.normalized_query or state.user_query}' "
            f"with {len(state.evidence)} evidence items after "
            f"{state.reflection_count + 1} research passes."
        )
        state.reasoning_log.append(
            f"Writer generated draft_report using {len(state.evidence)} evidence items."
        )
        state.status = "completed"

        self.logger.info(
            "writer_completed",
            session_id=state.session_id,
            evidence_count=len(state.evidence),
            prompt=WRITER_SYSTEM_PROMPT,
        )
        return state
