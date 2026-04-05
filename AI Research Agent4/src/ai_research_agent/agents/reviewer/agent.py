"""Reviewer agent implementation."""

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.agents.reviewer.prompt import REVIEWER_SYSTEM_PROMPT
from ai_research_agent.agents.reviewer.state import ReviewerOutput
from ai_research_agent.core.logging import get_logger
from ai_research_agent.graph.state import ReflectionRecord, ResearchState


class ReviewerAgent(BaseAgent):
    """Review evidence sufficiency and decide whether reflection is needed."""

    metadata = AgentMetadata(
        name="reviewer",
        responsibility="Assess evidence quality and control retry decisions.",
    )

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    def run(self, state: ResearchState) -> ResearchState:
        """Evaluate evidence quality and decide the next workflow step."""

        state.transition_history.append("Reviewer")
        state.status = "reviewing"

        unique_sources = {item.source for item in state.evidence}
        evidence_threshold = len(state.tasks) * 3
        has_enough_evidence = len(state.evidence) >= evidence_threshold
        has_source_diversity = len(unique_sources) >= 4
        reached_retry_limit = state.reflection_count >= state.max_reflections

        if (has_enough_evidence and has_source_diversity) or reached_retry_limit:
            decision = ReviewerOutput(
                decision="approve",
                reason=(
                    "Evidence coverage is sufficient for report generation."
                    if has_enough_evidence and has_source_diversity
                    else "Retry limit reached; approving current evidence set."
                ),
            )
            state.status = "writing"
        else:
            decision = ReviewerOutput(
                decision="retry",
                reason=(
                    "Evidence coverage is insufficient; broaden academic and implementation retrieval."
                ),
            )
            state.reflection_count += 1
            state.status = "researching"

        state.review_decision = decision.decision
        state.review_reason = decision.reason
        state.latest_feedback = decision.reason
        state.review_notes.append(decision.reason)
        state.reflection_history.append(
            ReflectionRecord(
                iteration=state.reflection_count,
                decision=decision.decision,
                reason=decision.reason,
            )
        )
        state.reasoning_log.append(
            "Reviewer decision="
            f"{decision.decision}, evidence_count={len(state.evidence)}, "
            f"source_diversity={len(unique_sources)}, retry_count={state.reflection_count}."
        )

        self.logger.info(
            "reviewer_completed",
            session_id=state.session_id,
            decision=state.review_decision,
            retry_count=state.reflection_count,
            prompt=REVIEWER_SYSTEM_PROMPT,
        )
        return state
