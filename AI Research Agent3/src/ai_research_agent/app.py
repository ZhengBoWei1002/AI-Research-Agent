"""FastAPI application factory."""

from fastapi import FastAPI

from ai_research_agent.api.routers.system import router as system_router
from ai_research_agent.core.config import get_settings
from ai_research_agent.core.logging import configure_logging, get_logger


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()
    configure_logging()

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        debug=settings.app_debug,
        docs_url="/docs",
        redoc_url="/redoc",
    )
    app.include_router(system_router, prefix="/api/v1")

    logger = get_logger(__name__)
    logger.info("application_initialized", environment=settings.app_env)

    return app
