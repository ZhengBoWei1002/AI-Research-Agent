# Architecture Overview

This project is designed as an industrial-grade multi-agent research assistant
built on LangGraph. The first iteration focuses on maintainable engineering
structure rather than business completeness.

## Design Goals

- Clear separation between API, orchestration, agents, and infrastructure
- Swappable OpenAI-compatible providers through a single LLM adapter
- Explicit state management with LangGraph state transitions
- Production-oriented configuration, logging, and deployment scaffolding
- Extensible storage strategy using SQLite for metadata and ChromaDB for retrieval

## Layered Architecture

```text
+------------------------------+
| FastAPI API Layer            |
| - REST endpoints             |
| - request/response schemas   |
+--------------+---------------+
               |
               v
+------------------------------+
| Application Orchestration    |
| - LangGraph workflow         |
| - state transitions          |
| - routing and retries        |
+--------------+---------------+
               |
               v
+------------------------------+
| Specialized Agents           |
| - Supervisor                 |
| - Planner                    |
| - Researcher                 |
| - Reviewer                   |
| - Writer                     |
| - MemoryManager              |
+--------------+---------------+
               |
               v
+------------------------------+
| Infrastructure Adapters      |
| - OpenAI-compatible LLM      |
| - SQLite checkpoint store    |
| - ChromaDB vector store      |
| - external tools (future)    |
+------------------------------+
```

## Core Boundaries

- `api`: FastAPI application and endpoint composition
- `core`: configuration, logging, and cross-cutting concerns
- `graph`: LangGraph state and workflow construction
- `agents`: role-specific decision units
- `infra`: adapters for LLM, storage, and retrieval backends
- `schemas`: Pydantic models for typed interfaces
