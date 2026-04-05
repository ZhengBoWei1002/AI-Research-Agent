from ai_research_agent.agents.supervisor import SupervisorAgent
from ai_research_agent.graph.state import create_initial_state


def test_supervisor_agent_normalizes_query_and_routes_to_planning() -> None:
    agent = SupervisorAgent()
    state = create_initial_state("  Analyze   AI agent system design  ", session_id="test-session")

    result = agent.run(state)

    assert result.session_id == "test-session"
    assert result.normalized_query == "Analyze AI agent system design"
    assert result.status == "planning"
    assert result.supervisor_notes == [
        "Supervisor accepted the incoming task.",
        "Workflow routed to Planner.",
    ]
