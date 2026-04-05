"""GitHub Search tool implementation."""

from typing import List

from ai_research_agent.tools.base import BaseResearchTool, ToolInput, ToolMetadata, ToolResult


class GitHubSearchTool(BaseResearchTool):
    """Return deterministic GitHub search style results."""

    metadata = ToolMetadata(
        name="github_search",
        category="code",
        description="Search repositories and code references for implementation examples.",
    )

    def search(self, tool_input: ToolInput) -> List[ToolResult]:
        return [
            ToolResult(
                title=f"GitHub repositories for {tool_input.query}",
                snippet=f"Code-oriented search result related to {tool_input.query}.",
                url="https://github.com/search",
                source=self.metadata.name,
            )
        ][: tool_input.max_results]
