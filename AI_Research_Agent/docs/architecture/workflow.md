# LangGraph Workflow

## Graph Topology

```mermaid
flowchart TD
    A([START]) --> B[MemoryManager]
    B --> C[Supervisor]
    C --> D[Planner]
    D --> E[Researcher]
    E --> F[Reviewer]
    F --> G{Need Revision?}
    G -- Yes --> D
    G -- No --> H[Writer]
    H --> I([END])
```

## Implemented Workflow In Current Milestone

```mermaid
flowchart LR
    A([START]) --> B[Supervisor]
    B --> C[Planner]
    C --> D([END])
```

This is the workflow that is actually implemented in code for the current
iteration. It intentionally stops after task planning and does not execute any
research logic yet.

## Node Responsibilities

- `MemoryManager`: load prior context, checkpoints, and retrieval hints
- `Supervisor`: apply policy, determine next node, control retries and failure exits
- `Planner`: translate user intent into bounded subtasks and acceptance criteria
- `Researcher`: gather evidence from tools, web, memory, and vector retrieval
- `Reviewer`: score evidence quality and decide whether another research loop is needed
- `Writer`: synthesize reviewed evidence into a report or actionable answer

## Workflow Notes

- The first milestone keeps the graph linear in code for simplicity.
- The documented target workflow includes a review loop from `Reviewer` to `Planner`.
- Retry budgeting should eventually be controlled by `research_max_iterations`.
- Timeout and cancellation logic should be enforced by the `Supervisor`.
