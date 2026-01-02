"""SQLite persistence placeholders."""

from pathlib import Path


class SQLiteStore:
    """Placeholder repository for metadata, sessions, and checkpoints."""

    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path
