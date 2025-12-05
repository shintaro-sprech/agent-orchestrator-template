# Autonomous Orchestration Ecosystem

A self-evolving sub-agent management system for Claude Code. Instead of manually managing agents, let an orchestrator automatically compose, merge, and evolve agents based on task requirements.

> **Original concept by [@shintaro_sprech](https://x.com/shintaro_sprech)**

![Autonomous Orchestration Ecosystem](docs/images/orchestration-flow.jpg)

## Concept

Multiple implementations feed into **Initial Sub-agent Pools**, which flow through the **Orchestrator Engine**. The engine continuously evolves agents through:

- **Specialized Sub-agents** → 1st Gen Integration → 2nd Gen Integration
- **Hyper-Elite Integration** → Ultimate Elite Integration
- An **Infinite Evolution Cycle** that continuously improves agent capabilities

```
Implementation → Multiple Sub-agents → Orchestrator Engine → Evolution Cycle → Hyper-Elite Entity
```

## Key Features

- **Autonomous agent selection**: Orchestrator evaluates tasks against existing agents
- **Dynamic merging**: Combines agents when synergy improves outcomes
- **Automatic specialization**: Creates new focused agents when gaps exist
- **Infinite evolution**: Strong agents evolve through generations, weak ones fade
- **Lineage tracking**: Merged agents remember their parents, enabling evolution chains

## Directory Structure

```
your-project/
├── .claude/
│   ├── settings.json          # Hooks config (reminder on Task usage)
│   └── agents/
│       ├── selector.md        # Agent selection guide
│       ├── registry.yaml      # Built-in agent list
│       └── contexts/          # Project-specific contexts
│           ├── _template.yaml
│           └── {domain}.yaml
└── CLAUDE.md                  # Selection criteria as Must rules
```

## Quick Start

### 1. Copy files

```bash
cp -r .claude /path/to/your/project/
```

### 2. Add to CLAUDE.md

Add the content from `CLAUDE.md` to your project's CLAUDE.md:

```markdown
## Agent Selection

**Must**: Select appropriate `subagent_type` when using Task tool for complex tasks.

| Task Type | Agent to Use |
|-----------|--------------|
| Frontend | `frontend-dev` |
| Backend | `backend-dev` |
| Testing | `test-runner` |
...
```

### 3. Create project context (optional)

```bash
cp .claude/agents/contexts/_template.yaml .claude/agents/contexts/frontend.yaml
# Edit to add project-specific information
```

### 4. Start using

Use Claude Code as normal. Hooks will display a reminder when Task is used.

## Built-in Agent List

Available `subagent_type` for Claude Code's Task tool:

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

See `.claude/agents/registry.yaml` for details.

## Enforcement Mechanisms

### 1. Hooks (automatic)

`.claude/settings.json` displays a reminder when Task tool is used:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Task",
      "command": "echo '[Agent Selector] Please reference registry.yaml to select the optimal agent.'"
    }]
  }
}
```

### 2. CLAUDE.md Must Rules

By documenting in CLAUDE.md, Claude recognizes these as rules to prioritize.

### 3. Explicit Instructions

Most reliable method:
- "Please follow the selector approach"
- "Check registry.yaml and select the appropriate agent"

## Documentation

- [Concept Details](docs/concept.md) - Design philosophy
- [Quick Start](docs/quickstart.md) - Setup instructions
- [Advanced](docs/advanced.md) - Customization and operation

## License

MIT License

## Author

Original concept by [@shintaro_sprech](https://x.com/shintaro_sprech)
