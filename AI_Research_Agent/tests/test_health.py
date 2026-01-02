from fastapi.testclient import TestClient

from ai_research_agent.app import create_app


def test_health_check() -> None:
    client = TestClient(create_app())

    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
