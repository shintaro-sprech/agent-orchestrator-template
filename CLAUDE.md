# CLAUDE.md - Agent Selector Template

Add this section to your project's CLAUDE.md file.

---

## Agent Selection

**Must**: Select appropriate `subagent_type` when using Task tool for complex tasks.

### Selection Rules

| Task Type | Agent to Use |
|-----------|--------------|
| Frontend (UI/React/CSS) | `frontend-dev` |
| Backend (API/DB) | `backend-dev` |
| Test creation/execution | `test-runner` |
| Code refactoring | `code-refactorer` |
| Security audit | `security-auditor` |
| Documentation creation | `doc-writer` |
| Library research | `lib-researcher` |
| Codebase exploration | `Explore` |
| Implementation planning | `Plan` |
| Compound tasks | `general-purpose` |

### Workflow

1. Identify task domain (frontend / backend / test / doc / security)
2. Check `.claude/agents/registry.yaml` for relevant agent
3. If `.claude/agents/contexts/{domain}.yaml` exists, check project-specific constraints
4. Execute selected agent with Task tool

### Handling Compound Tasks

Split multi-domain tasks for execution:

```
Example: "Create API and call it from frontend"
1. backend-dev → API implementation
2. frontend-dev → Frontend implementation
3. test-runner → Test creation
```

### Project-Specific Context

Place domain-specific context files in `.claude/agents/contexts/` directory:

```yaml
# Example: contexts/frontend.yaml
domain: frontend
applies_to: frontend-dev
project_specifics:
  stack:
    - React 19
    - Vite 7
  constraints:
    - Do not edit App.tsx directly, use subcomponents
```

### Reference Files

- `.claude/agents/registry.yaml` - Built-in agent list
- `.claude/agents/selector.md` - Detailed selection guidance
- `.claude/agents/contexts/` - Project-specific contexts
- `.claude/settings.json` - Hooks configuration (reminder displayed on Task usage)

---

## Technical Background

### Why This Design

Claude Code's Task tool recognizes **only built-in subagent_type**.
There is no functionality to dynamically load agents from custom `.md` files.

Therefore, this template:

1. **Uses built-in agents** - Uses mechanisms that reliably work
2. **Supplements with context files** - Manages project-specific info in separate files
3. **Uses Hooks for awareness** - Displays reminder on Task usage
4. **Uses CLAUDE.md Must rules** - Documents standards for both humans and Claude to follow

### Migration from v1.x

| v1.x Concept | v2.x Equivalent |
|--------------|-----------------|
| orchestrator.md | selector.md (limited to guidance) |
| manifests/*.yaml (skill sheets) | contexts/*.yaml (project context) |
| Automatic merging | Deprecated (not possible with built-in) |
| New agent generation | Deprecated (custom not recognized) |
| Coverage rate calculation | Deprecated (no enforcement) |
