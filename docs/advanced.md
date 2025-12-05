# Advanced Guide

Effective operation and customization methods for the Autonomous Orchestration Ecosystem.

## Utilizing Project Contexts

### Defining Multiple Domains

For large projects, create multiple context files:

```
.claude/agents/contexts/
├── _template.yaml
├── frontend.yaml
├── backend.yaml
├── database.yaml
└── infrastructure.yaml
```

### Linking Between Contexts

Explicitly define related contexts:

```yaml
# frontend.yaml
domain: frontend
applies_to: frontend-dev

related_contexts:
  - context: backend
    relationship: "API call destination, check endpoint definitions"
  - context: database
    relationship: "Required for understanding data structure"
```

### Progressive Detailing

Start minimal, add details as needed:

```yaml
# Initial (minimal)
domain: frontend
applies_to: frontend-dev
project_specifics:
  stack:
    - React 19

# After operation (detailed)
domain: frontend
applies_to: frontend-dev
project_specifics:
  stack:
    - React 19
    - Vite 7
    - TypeScript strict
    - TanStack Query
    - Zustand
  patterns:
    - Component naming: PascalCase
    - File naming: camelCase.tsx
    - Data fetching: use useQuery
  constraints:
    - Class components prohibited
    - any type prohibited
  examples:
    - task: "Add a new page"
      approach: "Place in src/pages/, routing in App.tsx"
```

## Customizing registry.yaml

### Project-Specific Agent Definitions

Add project-specific usage notes alongside built-in agents:

```yaml
# Append to registry.yaml
project_specific_usage:
  frontend-dev:
    additional_context: contexts/frontend.yaml
    typical_tasks:
      - "Create React components"
      - "Fix UI bugs"
      - "Responsive design"

  backend-dev:
    additional_context: contexts/backend.yaml
    typical_tasks:
      - "Add REST API endpoints"
      - "Implement auth logic"
```

### Recording Selection Patterns

Record frequently used patterns for reuse:

```yaml
# Append to registry.yaml
common_patterns:
  - name: "New feature (full-stack)"
    steps:
      - agent: Plan
        purpose: "Design, impact assessment"
      - agent: backend-dev
        purpose: "API implementation"
      - agent: frontend-dev
        purpose: "UI implementation"
      - agent: test-runner
        purpose: "Test creation"

  - name: "Bug fix"
    steps:
      - agent: Explore
        purpose: "Investigate cause"
      - agent: "{relevant-domain}"
        purpose: "Fix"
      - agent: test-runner
        purpose: "Regression test"
```

## Extending Hooks

### More Detailed Reminders

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Task",
        "command": "echo '[Agent Selector] Checklist:\\n1. Select agent from registry.yaml\\n2. Check project constraints in contexts/\\n3. Consider splitting compound tasks'"
      }
    ]
  }
}
```

### Additional Checks on Specific Agent Usage

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Task",
        "command": "echo '[Agent Selector] Task completed. Consider running test-runner if testing is needed.'"
      }
    ]
  }
}
```

## Team Operations

### New Member Onboarding

1. Read the "Agent Selection" section in CLAUDE.md
2. Review agent list in registry.yaml
3. Understand project-specific constraints via contexts/*.yaml

### Context Update Rules

```markdown
## Context Update Rules

1. When discovering new patterns, add to contexts/*.yaml
2. When constraints change, update constraints
3. Record major changes in CLAUDE.md changelog
4. For deprecated information, comment out with # instead of deleting
```

### Review Checklist

Checkpoints during PR review:

- [ ] Was the appropriate agent used?
- [ ] Are there any context constraint violations?
- [ ] If new patterns exist, are they added to contexts?

## Limitations and Countermeasures

### When Agent Selection is Ignored

**Countermeasure**: Explicit instructions

```
"Please follow the selector.md procedure.
First check registry.yaml, then check contexts/,
then select the appropriate agent."
```

### When Context is Too Long

**Countermeasure**: Split and prioritize

```yaml
# Only most important constraints in constraints
constraints:
  - UTF-8 required
  - Direct App.tsx editing prohibited

# Details in notes (reference is optional)
notes: |
  For detailed patterns and sample code,
  see docs/coding-guidelines.md
```

### Complex Task Judgment

**Countermeasure**: Use Plan agent first

```
"This task seems complex, so first use the Plan agent
to create an implementation plan. Then follow the plan
to use appropriate agents sequentially."
```

## Metrics and Improvement

### Manual Retrospective

Periodically check the following:

1. **Frequently used agents**: Update typical_tasks in registry.yaml
2. **Unused agents**: Consider if truly unnecessary
3. **Recurring patterns**: Add to common_patterns
4. **Constraint violations**: Emphasize or detail constraints

### Context Maturity

```
Level 1: Basic stack only
Level 2: Added patterns and constraints
Level 3: Added examples and related_contexts
Level 4: Entire team participates in updates
```

## Summary

Key points for effective operation:

1. **Start small**: Begin with minimal configuration, gradually detail
2. **Be explicit**: Specify agents directly when certainty is needed
3. **Continuously update**: Accumulate new insights in contexts
4. **Share with team**: Use CLAUDE.md and contexts as documentation
