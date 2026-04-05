"""Semantic Scholar tool implementation."""

from typing import List

from ai_research_agent.tools.base import BaseResearchTool, ToolInput, ToolMetadata, ToolResult


class SemanticScholarTool(BaseResearchTool):
    """Return deterministic Semantic Scholar style results."""

    metadata = ToolMetadata(
        name="semantic_scholar",
        category="academic",
        description="Search citation-aware academic literature and metadata.",
    )

    def search(self, tool_input: ToolInput) -> List[ToolResult]:
        return [
            ToolResult(
                title=f"Semantic Scholar analysis for {tool_input.query}",
                snippet=f"Citation-oriented literature summary for {tool_input.query}.",
                url="https://www.semanticscholar.org/",
                source=self.metadata.name,
            )
        ][: tool_input.max_results]
