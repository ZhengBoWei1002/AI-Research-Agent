from ai_research_agent.agents.writer import WriterAgent
from ai_research_agent.graph.state import Evidence, ResearchState


def test_writer_agent_generates_draft_report() -> None:
    agent = WriterAgent()
    state = ResearchState(
        session_id="writer-session",
        user_query="Summarize evidence",
        normalized_query="Summarize evidence",
        evidence=[
            Evidence(
                evidence_id="ev-1",
                task_id="task-1",
                source="duckduckgo",
                title="Result",
                snippet="Snippet",
                url="https://duckduckgo.com/",
            )
        ],
        status="writing",
    )

    result = agent.run(state)

    assert result.status == "completed"
    assert "Report draft" in result.draft_report
    assert "Writer" in result.transition_history
