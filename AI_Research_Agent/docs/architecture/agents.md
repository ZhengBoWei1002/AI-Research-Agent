# Agent Responsibilities

## Supervisor

- Owns top-level orchestration policy
- Controls node routing, retry budget, timeout, and failure handling
- Enforces guardrails such as output contracts and execution boundaries

## Planner

- Parses the user objective into a structured research plan
- Defines subtasks, dependencies, and completion criteria
- Produces the plan that downstream agents execute

## Researcher

- Executes evidence collection tasks
- Calls retrieval tools, knowledge sources, and external APIs
- Stores structured findings back into shared graph state

## Reviewer

- Evaluates evidence completeness, relevance, and consistency
- Detects weak citations, contradictory evidence, or missing coverage
- Decides whether to continue research or move to final writing

## Writer

- Converts validated evidence into the final answer format
- Adapts tone, structure, and output schema to the request type
- Produces executive summaries and long-form reports in future iterations

## MemoryManager

- Manages short-term state, checkpoints, and long-term memory hooks
- Coordinates SQLite persistence and ChromaDB retrieval context
- Supports resumable sessions and context hydration
