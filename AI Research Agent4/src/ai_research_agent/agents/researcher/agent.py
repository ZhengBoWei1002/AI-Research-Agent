"""Researcher agent implementation."""

from typing import List, Optional

from ai_research_agent.agents.base import AgentMetadata, BaseAgent
from ai_research_agent.agents.researcher.prompt import RESEARCHER_SYSTEM_PROMPT
from ai_research_agent.agents.researcher.state import ResearcherOutput
from ai_research_agent.core.logging import get_logger
from ai_research_agent.graph.state import Evidence, ResearchState, ToolCallRecord
from ai_research_agent.tools.base import ToolResult
from ai_research_agent.tools.registry import ToolRegistry


class ResearcherAgent(BaseAgent):
    """Select tools, collect preliminary evidence, and summarize findings."""

    metadata = AgentMetadata(
        name="researcher",
        responsibility="Select tools and aggregate normalized evidence.",
    )

    def __init__(self, tool_registry: Optional[ToolRegistry] = None) -> None:
        self.logger = get_logger(self.__class__.__name__)
        self.tool_registry = tool_registry or ToolRegistry()

    def run(self, state: ResearchState) -> ResearchState:
        """Execute research tool selection and evidence aggregation."""

        state.transition_history.append("Researcher")
        state.status = "researching"

        all_evidence: List[Evidence] = []
        all_tool_calls: List[ToolCallRecord] = []
        reflection_mode = state.reflection_count > 0
        max_results = 2 if reflection_mode else 1
        existing_evidence = list(state.evidence)
        existing_tool_calls = list(state.tool_calls)

        for task in state.tasks:
            tool_query = self._build_tool_query(task.objective, state.latest_feedback, reflection_mode)
            tool_results = self.tool_registry.execute_selected_tools(tool_query, max_results=max_results)
            for tool_name, results in tool_results.items():
                all_tool_calls.append(
                    ToolCallRecord(
                        tool_name=tool_name,
                        query=tool_query,
                        success=True,
                        result_count=len(results),
                    )
                )
                all_evidence.extend(
                    self._to_evidence(task.task_id, tool_name, results, state.reflection_count)
                )
            task.status = "researched"

        output = ResearcherOutput(
            evidence=existing_evidence + all_evidence,
            tool_calls=existing_tool_calls + all_tool_calls,
            researcher_summary=(
                f"Researcher aggregated {len(all_evidence)} evidence items "
                f"from {len(all_tool_calls)} tool calls in iteration {state.reflection_count + 1}."
            ),
        )

        state.evidence = output.evidence
        state.tool_calls = output.tool_calls
        state.researcher_summary = output.researcher_summary
        state.reasoning_log.append(
            "Researcher collected evidence with "
            f"reflection_count={state.reflection_count} and feedback={state.latest_feedback!r}."
        )
        state.status = "reviewing"

        self.logger.info(
            "researcher_completed",
            session_id=state.session_id,
            evidence_count=len(state.evidence),
            tool_call_count=len(state.tool_calls),
            prompt=RESEARCHER_SYSTEM_PROMPT,
        )
        return state

    def _to_evidence(
        self,
        task_id: str,
        tool_name: str,
        results: List[ToolResult],
        reflection_count: int,
    ) -> List[Evidence]:
        """Convert tool results into normalized evidence records."""

        evidence_items: List[Evidence] = []
        for index, result in enumerate(results, start=1):
            evidence_items.append(
                Evidence(
                    evidence_id=f"{task_id}-{tool_name}-r{reflection_count + 1}-{index}",
                    task_id=task_id,
                    source=result.source,
                    title=result.title,
                    snippet=result.snippet,
                    url=result.url,
                )
            )
        return evidence_items

    def _build_tool_query(self, objective: str, feedback: str, reflection_mode: bool) -> str:
        """Build the query sent to the tool framework."""

        if not reflection_mode:
            return objective
        return (
            f"{objective} broader research benchmark implementation examples "
            f"{feedback}".strip()
        )
