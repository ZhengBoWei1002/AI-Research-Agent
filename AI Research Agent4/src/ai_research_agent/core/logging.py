"""Logging bootstrap utilities."""

import logging
import logging.config
from pathlib import Path
from typing import Any, Optional

import structlog
import yaml


DEFAULT_LOGGING_CONFIG = Path("configs/logging.yaml")


def configure_logging(config_path: Optional[Path] = None) -> None:
    """Configure stdlib logging and structlog."""

    resolved_path = config_path or DEFAULT_LOGGING_CONFIG

    if resolved_path.exists():
        with resolved_path.open("r", encoding="utf-8") as file:
            config: dict[str, Any] = yaml.safe_load(file)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """Return a structlog logger instance."""

    return structlog.get_logger(name)
