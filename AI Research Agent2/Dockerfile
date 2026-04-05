FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml README.md ./
COPY src ./src
COPY configs ./configs

RUN uv pip install --system .

EXPOSE 8000

CMD ["uvicorn", "ai_research_agent.app:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
