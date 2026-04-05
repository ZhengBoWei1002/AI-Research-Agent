"""Planner agent implementation."""

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.agents.planner.prompt import PLANNER_SYSTEM_PROMPT
from ai_research_agent.agents.planner.state import PlannerOutput
from ai_research_agent.core.logging import get_logger
from ai_research_agent.graph.state import ResearchState, ResearchTask


class PlannerAgent(BaseAgent):
    """Decompose the normalized task into executable research tasks."""

    metadata = AgentMetadata(
        name="planner",
        responsibility="Break the task into a bounded set of research tasks.",
    )

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)

    def run(self, state: ResearchState) -> ResearchState:
        """Create research tasks for downstream execution."""

        topic = state.normalized_query or state.user_query
        output = PlannerOutput(
            tasks=[
                ResearchTask(
                    task_id="task-1",
                    title="Clarify Objective",
                    objective=f"Define the scope and expected outcome for: {topic}",
                    rationale="A clear objective prevents downstream ambiguity.",
                    status="planned",
                ),
                ResearchTask(
                    task_id="task-2",
                    title="Break Down Questions",
                    objective=f"Identify the key sub-questions that make up: {topic}",
                    rationale="Research should follow a structured question set.",
                    status="planned",
                ),
                ResearchTask(
                    task_id="task-3",
                    title="Prepare Research Backlog",
                    objective=f"Sequence the future research steps for: {topic}",
                    rationale="A prioritized backlog enables controlled execution.",
                    status="planned",
                ),
            ],
            planning_summary=(
                "Planner created a deterministic three-step research backlog "
                "for the downstream Researcher."
            ),
        )

        state.tasks = output.tasks
        state.plan = [task.objective for task in output.tasks]
        state.planning_summary = output.planning_summary
        state.status = "researching"
        state.reasoning_log.append(
            f"Planner created {len(state.tasks)} tasks and moved workflow to researching."
        )
        state.transition_history.append("Planner")

        self.logger.info(
            "planner_completed",
            session_id=state.session_id,
            task_count=len(state.tasks),
            prompt=PLANNER_SYSTEM_PROMPT,
        )
        return state
