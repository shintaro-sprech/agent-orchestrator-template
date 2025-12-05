# Quick Start Guide

Get the Autonomous Orchestration Ecosystem running in your project.

## Prerequisites

- Claude Code installed
- A project where you want to use orchestrated agents

## Step 1: Copy Files

```bash
# Copy the .claude directory to your project
cp -r .claude /path/to/your/project/

# Windows (PowerShell)
Copy-Item -Recurse .claude C:\path\to\your\project\
```

Your project should now have:
```
your-project/
├── .claude/
│   ├── settings.json
│   └── agents/
│       ├── orchestrator.md
│       ├── _template.md
│       ├── manifests/
│       │   └── _template.yaml
│       └── pool/
│           ├── specialized/
│           ├── integrated/
│           └── elite/
```

## Step 2: Update CLAUDE.md

Add orchestration rules to your `CLAUDE.md`:

```markdown
## Agent Orchestration

**Must**: All tasks must pass through the orchestrator workflow before execution.

### Core Principle

**Do NOT use pre-defined abstract agents.** Instead:
1. Create specialized agents from actual task requirements
2. Integrate existing agents when synergy improves outcomes
3. Let the agent pool evolve through continuous improvement

### Workflow

1. Scan `pool/` for existing agents
2. Calculate coverage against task requirements
3. Decide: Use existing / Integrate / Create new
4. Execute task
5. Update metrics in `manifests/`
6. Promote high-performers to `elite/`
```

## Step 3: Start Using

That's it! Now when you give Claude Code a task:

### First Task (Empty Pool)

```
You: "Create a REST API endpoint for user authentication"

Claude (via orchestrator):
- Scanned pool/: 0 agents found
- Coverage: 0% → Creating new specialized agent
- Created: pool/specialized/auth-api-specialist.md
- Created: manifests/auth-api-specialist.yaml
- Executing task with new agent...
[task completion]
```

### Subsequent Task (Partial Match)

```
You: "Add rate limiting to the auth API"

Claude (via orchestrator):
- Scanned pool/: auth-api-specialist found
- Coverage: 65% → Need to integrate with rate-limiting capability
- Created: pool/integrated/merged-auth-ratelimit.md
- Created: manifests/merged-auth-ratelimit.yaml
- Executing task with integrated agent...
[task completion]
```

### High-Coverage Task

```
You: "Fix the JWT expiration bug in auth"

Claude (via orchestrator):
- Scanned pool/: auth-api-specialist found
- Coverage: 95% → Using existing agent
- Executing task with auth-api-specialist...
- Updated metrics: usage_count=3, success_rate=1.0
[task completion]
```

## Watching Evolution

Check the agent pool as it grows:

```bash
ls .claude/agents/pool/specialized/
# auth-api-specialist.md
# db-query-optimizer.md

ls .claude/agents/pool/integrated/
# merged-auth-ratelimit.md
# merged-api-db.md

ls .claude/agents/pool/elite/
# (empty initially, populated as agents are promoted)
```

Check skill sheets:

```bash
cat .claude/agents/manifests/auth-api-specialist.yaml
```

```yaml
name: auth-api-specialist
tier: specialized
metrics:
  usage_count: 5
  success_rate: 0.8
  last_used: 2025-01-15
```

## Elite Promotion

When an agent meets the criteria:
- `usage_count >= 5`
- `success_rate >= 0.8`

The orchestrator will:
1. Move the agent to `pool/elite/`
2. Update the skill sheet `tier: elite`

## Tips for Best Results

1. **Be specific in tasks**: Clear requirements help the orchestrator create focused agents

2. **Let it evolve**: Don't manually create agents—let the orchestrator build them from real tasks

3. **Check the manifests**: See which agents are performing well, which need work

4. **Trust integration**: When the orchestrator wants to merge agents, let it—integration often produces better results than using separate agents

## Next Steps

- Read [Concept](concept.md) for deeper understanding
- See [Advanced](advanced.md) for optimization strategies
