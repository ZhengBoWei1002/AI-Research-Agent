from ai_research_agent.agents.planner import PlannerAgent
from ai_research_agent.graph.state import ResearchState


def test_planner_agent_creates_research_tasks() -> None:
    agent = PlannerAgent()
    state = ResearchState(
        session_id="planner-session",
        user_query="Compare leading agent orchestration frameworks",
        normalized_query="Compare leading agent orchestration frameworks",
        status="planning",
    )

    result = agent.run(state)

    assert result.status == "researching"
    assert len(result.tasks) == 3
    assert len(result.plan) == 3
    assert all(task.status == "planned" for task in result.tasks)
    assert "Planner created a deterministic three-step research backlog" in (
        result.planning_summary
    )
