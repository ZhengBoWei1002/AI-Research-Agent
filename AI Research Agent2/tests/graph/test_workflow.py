from ai_research_agent.graph.workflow import build_research_graph, run_research_workflow


def test_build_research_graph_contains_supervisor_and_planner_path() -> None:
    graph = build_research_graph()

    assert graph is not None


def test_run_research_workflow_returns_planned_tasks() -> None:
    result = run_research_workflow(
        user_query="Create a research plan for enterprise AI agents",
        session_id="workflow-session",
    )

    assert result.session_id == "workflow-session"
    assert result.status == "completed"
    assert result.normalized_query == "Create a research plan for enterprise AI agents"
    assert len(result.tasks) == 3
    assert result.tasks[0].title == "Clarify Objective"
