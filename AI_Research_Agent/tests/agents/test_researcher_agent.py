from ai_research_agent.agents.researcher import ResearcherAgent
from ai_research_agent.graph.state import ResearchState, ResearchTask


def test_researcher_agent_collects_evidence_and_tool_calls() -> None:
    agent = ResearcherAgent()
    state = ResearchState(
        session_id="research-session",
        user_query="Research multi-agent benchmark papers and open-source repos",
        normalized_query="Research multi-agent benchmark papers and open-source repos",
        tasks=[
            ResearchTask(
                task_id="task-1",
                title="Collect sources",
                objective="Research benchmark papers and code implementations for multi-agent systems",
                rationale="Need both literature and repositories",
                status="planned",
            )
        ],
        status="researching",
    )

    result = agent.run(state)

    assert result.status == "reviewing"
    assert len(result.evidence) >= 2
    assert len(result.tool_calls) >= 2
    assert all(task.status == "researched" for task in result.tasks)
    assert "Researcher aggregated" in result.researcher_summary
