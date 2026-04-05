from ai_research_agent.agents.reviewer import ReviewerAgent
from ai_research_agent.graph.state import Evidence, ResearchState, ResearchTask


def test_reviewer_agent_requests_retry_when_evidence_is_insufficient() -> None:
    agent = ReviewerAgent()
    state = ResearchState(
        session_id="review-session",
        user_query="Review evidence quality",
        tasks=[
            ResearchTask(
                task_id="task-1",
                title="Collect",
                objective="Collect evidence",
                rationale="Need more evidence",
                status="researched",
            )
        ],
        evidence=[
            Evidence(
                evidence_id="ev-1",
                task_id="task-1",
                source="duckduckgo",
                title="One result",
                snippet="Insufficient single-source evidence",
                url="https://duckduckgo.com/",
            )
        ],
        status="reviewing",
        max_reflections=2,
    )

    result = agent.run(state)

    assert result.review_decision == "retry"
    assert result.status == "researching"
    assert result.reflection_count == 1
    assert len(result.reflection_history) == 1


def test_reviewer_agent_approves_when_evidence_is_sufficient() -> None:
    agent = ReviewerAgent()
    state = ResearchState(
        session_id="review-session-approve",
        user_query="Review evidence quality",
        tasks=[
            ResearchTask(
                task_id="task-1",
                title="Collect",
                objective="Collect evidence",
                rationale="Need coverage",
                status="researched",
            )
        ],
        evidence=[
            Evidence(
                evidence_id="ev-1",
                task_id="task-1",
                source="duckduckgo",
                title="Web result",
                snippet="web",
                url="https://duckduckgo.com/",
            ),
            Evidence(
                evidence_id="ev-2",
                task_id="task-1",
                source="arxiv",
                title="Paper result",
                snippet="paper",
                url="https://arxiv.org/search/",
            ),
            Evidence(
                evidence_id="ev-3",
                task_id="task-1",
                source="semantic_scholar",
                title="Citation result",
                snippet="citation",
                url="https://www.semanticscholar.org/",
            ),
            Evidence(
                evidence_id="ev-4",
                task_id="task-1",
                source="github_search",
                title="Code result",
                snippet="code",
                url="https://github.com/search",
            ),
        ],
        status="reviewing",
    )

    result = agent.run(state)

    assert result.review_decision == "approve"
    assert result.status == "writing"
