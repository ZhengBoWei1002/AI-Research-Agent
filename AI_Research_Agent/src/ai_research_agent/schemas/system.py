"""Shared system-level schemas."""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    service: str
    environment: str
