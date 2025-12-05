# Quick Start Guide

Steps to introduce the Autonomous Orchestration Ecosystem to your project.

## Prerequisites

- Claude Code installed
- Project directory exists

## Step 1: Copy Files

```bash
# Copy entire .claude directory to project
cp -r .claude /path/to/your/project/

# Windows (PowerShell)
Copy-Item -Recurse .claude C:\path\to\your\project\
```

Structure after copying:
```
your-project/
├── .claude/
│   ├── settings.json
│   └── agents/
│       ├── selector.md
│       ├── registry.yaml
│       └── contexts/
│           └── _template.yaml
└── ... (existing files)
```

## Step 2: Add to CLAUDE.md

Add the following to your project's `CLAUDE.md`:

```markdown
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

### Reference Files

- `.claude/agents/registry.yaml` - Built-in agent list
- `.claude/agents/selector.md` - Detailed selection guidance
- `.claude/agents/contexts/` - Project-specific contexts
```

## Step 3: Create Project Context (Recommended)

Copy and edit the template:

```bash
cp .claude/agents/contexts/_template.yaml .claude/agents/contexts/frontend.yaml
```

Example (frontend.yaml):

```yaml
domain: frontend
applies_to: frontend-dev

project_specifics:
  stack:
    - React 19
    - Vite 7
    - TypeScript strict

  patterns:
    - Components placed in src/components/
    - Custom hooks placed in src/hooks/
    - Styles use CSS Modules

  constraints:
    - Do not edit App.tsx directly, use subcomponents
    - UTF-8 without BOM required

  critical_files:
    - path: src/App.tsx
      note: "Over 1,800 lines, direct editing prohibited"
    - path: vite.config.ts
      note: "Only location for proxy settings"
```

## Step 4: Start Using

Setup complete.

### Normal Usage

Request tasks from Claude Code as usual:

```
"Please add an API endpoint for user authentication"
```

Hooks will display a reminder when Task is used, prompting appropriate agent selection.

### Explicit Instructions

For more certainty:

```
"Please follow selector.md and choose the appropriate agent"
```

Or:

```
"Use the backend-dev agent to implement the authentication API"
```

## Verification

### Checking if Hooks Work

When Task tool is used, the following message should appear:

```
[Agent Selector] Using Task tool. Please reference registry.yaml and selector.md to select the optimal agent.
```

If not displayed, verify `.claude/settings.json` is correctly placed.

### Checking if Contexts are Referenced

Ask Claude to confirm the content:

```
"Please show me the contents of .claude/agents/contexts/frontend.yaml"
```

## Troubleshooting

### Hooks Not Working

1. Verify `.claude/settings.json` is in project root's `.claude/`
2. Check JSON syntax is correct
3. Restart Claude Code

### Agent Not Selected

1. Verify selection rules are documented in CLAUDE.md
2. Give explicit instruction "Please follow selector.md"
3. Specify agent directly: "Use frontend-dev to..."

### Context Being Ignored

1. Verify contexts/*.yaml path is correct
2. Check YAML syntax is correct
3. Give explicit reference instruction: "Check contexts/frontend.yaml before proceeding"

## Next Steps

- [Concept Details](concept.md) - Understand the design philosophy
- [Advanced](advanced.md) - Customization and operation techniques
