"""Arxiv tool implementation."""

from typing import List

from ai_research_agent.tools.base import BaseResearchTool, ToolInput, ToolMetadata, ToolResult


class ArxivTool(BaseResearchTool):
    """Return deterministic arXiv-style search results."""

    metadata = ToolMetadata(
        name="arxiv",
        category="academic",
        description="Search academic preprints for technical and research topics.",
    )

    def search(self, tool_input: ToolInput) -> List[ToolResult]:
        return [
            ToolResult(
                title=f"arXiv overview for {tool_input.query}",
                snippet=f"Academic preprint perspective related to {tool_input.query}.",
                url="https://arxiv.org/search/",
                source=self.metadata.name,
            )
        ][: tool_input.max_results]
