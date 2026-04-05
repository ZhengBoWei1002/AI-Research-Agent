"""DuckDuckGo tool implementation."""

from typing import List

from ai_research_agent.tools.base import BaseResearchTool, ToolInput, ToolMetadata, ToolResult


class DuckDuckGoTool(BaseResearchTool):
    """Return deterministic web search style results."""

    metadata = ToolMetadata(
        name="duckduckgo",
        category="web",
        description="Search general web results for broad coverage and discovery.",
    )

    def search(self, tool_input: ToolInput) -> List[ToolResult]:
        return [
            ToolResult(
                title=f"DuckDuckGo web results for {tool_input.query}",
                snippet=f"General web discovery result related to {tool_input.query}.",
                url="https://duckduckgo.com/",
                source=self.metadata.name,
            )
        ][: tool_input.max_results]
