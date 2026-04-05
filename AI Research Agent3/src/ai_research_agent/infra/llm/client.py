"""OpenAI-compatible client factory."""

from langchain_openai import ChatOpenAI

from ai_research_agent.core.config import Settings


def build_chat_model(settings: Settings) -> ChatOpenAI:
    """Create a chat model instance from application settings."""

    return ChatOpenAI(
        api_key=settings.openai_api_key,
        base_url=settings.openai_api_base,
        model=settings.openai_model,
        temperature=0,
    )
