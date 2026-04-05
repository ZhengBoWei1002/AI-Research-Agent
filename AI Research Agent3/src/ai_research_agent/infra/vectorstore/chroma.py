"""ChromaDB vector store placeholders."""

from pathlib import Path


class ChromaKnowledgeStore:
    """Placeholder adapter for embeddings and semantic retrieval."""

    def __init__(self, persist_directory: Path) -> None:
        self.persist_directory = persist_directory
