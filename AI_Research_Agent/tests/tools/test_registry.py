from ai_research_agent.tools.registry import ToolRegistry


def test_tool_registry_contains_required_tools() -> None:
    registry = ToolRegistry()

    assert registry.list_tool_names() == [
        "arxiv",
        "semantic_scholar",
        "duckduckgo",
        "github_search",
    ]
    assert registry.get_future_tool_slots() == ["browser", "pdf_reader", "mcp"]


def test_tool_registry_selects_code_and_academic_tools() -> None:
    registry = ToolRegistry()

    selected = registry.select_tools("research code implementation benchmark github")
    selected_names = [tool.metadata.name for tool in selected]

    assert "duckduckgo" in selected_names
    assert "arxiv" in selected_names
    assert "semantic_scholar" in selected_names
    assert "github_search" in selected_names
