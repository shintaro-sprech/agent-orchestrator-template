# Agent Selector

A guide for selecting the optimal built-in agent for each task.

## Important Prerequisites

**This file provides "guidance" and is NOT an automatically executed mechanism.**

- Actual task execution uses Claude Code's Task tool (built-in agents)
- This document provides criteria for "which agent to choose"
- Reliable application requires combining CLAUDE.md Must rules and Hooks

## Built-in Agent List

Available `subagent_type` for the Task tool:

| Agent | Purpose | Model |
|-------|---------|-------|
| `frontend-dev` | React/Vite frontend development | opus |
| `backend-dev` | FastAPI backend development | opus |
| `test-runner` | Test execution/creation | - |
| `code-refactorer` | Code structure/readability improvement | - |
| `security-auditor` | Security audit | opus |
| `doc-writer` | Documentation creation | - |
| `lib-researcher` | Library research | opus |
| `Explore` | Codebase exploration (fast) | - |
| `Plan` | Implementation planning design | - |
| `general-purpose` | General multi-step tasks | - |

See `registry.yaml` for details.

## Selection Flow

### Step 1: Task Analysis

When receiving a task, identify:

1. **Primary domain**: frontend / backend / test / doc / security / research
2. **Complexity**: Simple (single operation) / Moderate (multiple steps) / Complex (design required)
3. **Constraints**: Special requirements or considerations

### Step 2: Agent Selection

```
Single domain → Specialized agent (frontend-dev, backend-dev, etc.)
Multi-domain  → Primary domain agent, or split execution
Research only → Explore
Design needed → Plan
Unknown       → general-purpose
```

### Step 3: Context Check

If there's a corresponding `contexts/{domain}.yaml` for the selected agent, reference it to check project-specific constraints.

### Step 4: Execution

Call the selected agent using the Task tool.

## Differences from the Old Orchestrator

### Deprecated Concepts

| Old Concept | Reason |
|-------------|--------|
| Automatic merging | Built-in agents cannot be merged |
| New agent generation | Custom agents are not recognized by Task |
| Coverage rate calculation | No practical enforcement |
| Automatic skill sheet scanning | No automation mechanism |

### Retained Concepts

| Concept | Changed Format |
|---------|----------------|
| Agent selection guidance | selector.md (this file) |
| Capability/constraint definition | contexts/*.yaml (project-specific info) |
| Selection criteria | registry.yaml (built-in agent list) |

## Handling Compound Tasks

### Method A: Split Execution (Recommended)

```
Task: "Create API and call it from frontend"

1. backend-dev for API implementation
2. frontend-dev for frontend implementation
3. test-runner for tests
```

### Method B: General-Purpose Agent

```
Task: "Complex task difficult to split"

→ Process all at once with general-purpose
```

## Ensuring Reliable Application

To reliably apply these guidelines:

1. **CLAUDE.md Must rules**: "Reference selector.md when using Task tool"
2. **Hooks configuration**: Display reminder before Task execution
3. **Explicit instructions**: "Please follow the selector approach"

See `../settings.json` and `../../CLAUDE.md` for details.

## Recording Evolution

Instead of the old orchestrator's "evolution tracking," we recommend:

- **Frequently used patterns**: Document in CLAUDE.md
- **Project-specific insights**: Add to contexts/*.yaml
- **Effective combinations**: Add to registry.yaml examples

Explicit recording by humans ensures reliable knowledge accumulation.
