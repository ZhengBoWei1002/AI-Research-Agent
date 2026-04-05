"""Tool registry and selection logic."""

from typing import Dict, List

from ai_research_agent.tools.arxiv import ArxivTool
from ai_research_agent.tools.base import BaseResearchTool, ToolInput, ToolResult
from ai_research_agent.tools.duckduckgo import DuckDuckGoTool
from ai_research_agent.tools.github_search import GitHubSearchTool
from ai_research_agent.tools.semantic_scholar import SemanticScholarTool


class ToolRegistry:
    """Registry for available and future research tools."""

    def __init__(self) -> None:
        self._tools: Dict[str, BaseResearchTool] = {
            "arxiv": ArxivTool(),
            "semantic_scholar": SemanticScholarTool(),
            "duckduckgo": DuckDuckGoTool(),
            "github_search": GitHubSearchTool(),
        }
        self._future_tool_slots: List[str] = ["browser", "pdf_reader", "mcp"]

    def list_tool_names(self) -> List[str]:
        """Return registered tool names."""

        return list(self._tools.keys())

    def get_future_tool_slots(self) -> List[str]:
        """Return reserved extension slots."""

        return self._future_tool_slots.copy()

    def select_tools(self, query: str) -> List[BaseResearchTool]:
        """Select the most relevant tools for a query."""

        normalized_query = query.lower()
        selected: List[BaseResearchTool] = [self._tools["duckduckgo"]]

        if any(keyword in normalized_query for keyword in ["paper", "research", "benchmark"]):
            selected.append(self._tools["arxiv"])
            selected.append(self._tools["semantic_scholar"])

        if any(keyword in normalized_query for keyword in ["github", "repo", "code", "implementation"]):
            selected.append(self._tools["github_search"])

        if len(selected) == 1:
            selected.append(self._tools["arxiv"])

        deduplicated: Dict[str, BaseResearchTool] = {tool.metadata.name: tool for tool in selected}
        return list(deduplicated.values())

    def execute_selected_tools(self, query: str, max_results: int = 2) -> Dict[str, List[ToolResult]]:
        """Execute selected tools and return results keyed by tool name."""

        selected_tools = self.select_tools(query)
        tool_input = ToolInput(query=query, max_results=max_results)
        return {
            tool.metadata.name: tool.search(tool_input)
            for tool in selected_tools
        }
