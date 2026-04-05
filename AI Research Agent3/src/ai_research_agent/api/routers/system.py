"""System endpoints."""

from fastapi import APIRouter

from ai_research_agent.core.config import get_settings
from ai_research_agent.schemas.system import HealthResponse

router = APIRouter(tags=["system"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Simple health endpoint for local verification."""

    settings = get_settings()
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        environment=settings.app_env,
    )
