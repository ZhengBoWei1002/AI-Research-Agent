"""Supervisor agent implementation."""

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.agents.supervisor.prompt import SUPERVISOR_SYSTEM_PROMPT
from ai_research_agent.agents.supervisor.state import SupervisorDecision
from ai_research_agent.core.logging import get_logger
from ai_research_agent.graph.state import ResearchState


class SupervisorAgent(BaseAgent):
    """Normalize the user task and prepare workflow execution."""

    metadata = AgentMetadata(
        name="supervisor",
        responsibility="Validate user intent and hand off the workflow to planning.",
    )

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    def run(self, state: ResearchState) -> ResearchState:
        """Accept the incoming task and transition the state to planning."""

        normalized_query = " ".join(state.user_query.split())
        notes = [
            "Supervisor accepted the incoming task.",
            "Workflow routed to Planner.",
        ]

        decision = SupervisorDecision(
            normalized_query=normalized_query,
            notes=notes,
            next_status="planning" if normalized_query else "failed",
        )

        state.normalized_query = decision.normalized_query
        state.supervisor_notes = decision.notes
        state.status = decision.next_status
        state.reasoning_log.append(
            f"Supervisor normalized query and routed workflow with status={state.status}."
        )
        state.transition_history.append("Supervisor")

        self.logger.info(
            "supervisor_completed",
            session_id=state.session_id,
            status=state.status,
            prompt=SUPERVISOR_SYSTEM_PROMPT,
        )
        return state
