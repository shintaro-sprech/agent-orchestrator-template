# CLAUDE.md - Autonomous Orchestration Ecosystem

Add this section to your project's CLAUDE.md file.

---

## Agent Orchestration

**Must**: All implementation tasks must pass through the orchestrator workflow before execution.

### Decision Gate Exception

An explicitly invoked analysis-only Skill may run before `/task` when it does not modify code, files, external systems, or production state.
Use `/evaluation-first-decision` to create a Decision Card containing the verdict, evidence, guardrails, stop conditions, and rollback plan.

- `GO` or `PILOT` does not itself authorize execution.
- For `HIGH` or `CRITICAL` risk, record the responsible human decision owner.
- When execution is approved, include the Decision Card in the `/task` input.
- The orchestrator must preserve the approved scope, guardrails, stop conditions, and rollback requirements.
- `HOLD` or `STOP` blocks execution until the stated verdict-changing conditions are satisfied.

### Core Principle

**Do NOT use pre-defined abstract agents.** Instead:
1. Create specialized agents from actual task requirements
2. Integrate existing agents when synergy improves outcomes
3. Let the agent pool evolve through continuous improvement

### Workflow

```
Consequential decision (when applicable)
     ↓
/evaluation-first-decision
     ↓
Decision Card + human approval where required
     ↓
Task Received through /task
     ↓
Scan pool/ for existing agents
     ↓
Calculate coverage rate against task requirements
     ↓
┌─────────────────────────────────────────────────────┐
│ Coverage 90%+  → Use existing agent                 │
│ Coverage 60-90% → Create integrated agent           │
│ Coverage <60%  → Create new specialized agent       │
└─────────────────────────────────────────────────────┘
     ↓
Execute task within approved guardrails
     ↓
Update manifests/ with metrics
     ↓
Promote to elite/ if qualified
```

### Directory Structure

```
.claude/
├── skills/
│   └── evaluation-first-decision/
│       ├── SKILL.md
│       ├── references/
│       └── assets/
├── agents/
│   ├── orchestrator.md        # Orchestrator definition (read first)
│   ├── _template.md           # Template for new agents
│   ├── manifests/             # Skill sheets (metadata + metrics)
│   │   └── {agent-name}.yaml
│   └── pool/                  # Agent pool
│       ├── specialized/       # Task-specific agents (newly created)
│       ├── integrated/        # Merged agents (1st/2nd Gen Integration)
│       └── elite/             # Hyper-Elite agents (proven performers)
```

### Decision Matrix

| Coverage Rate | Action | Save Location |
|---------------|--------|---------------|
| **90%+** | Use existing agent directly | - |
| **60-90%** | Merge source agents into integrated agent | `pool/integrated/` |
| **Below 60%** | Create new specialized agent | `pool/specialized/` |

### Agent Creation Rules

When creating a new agent:

1. **Copy `_template.md`** structure
2. **Define in YAML frontmatter**:
   ```yaml
   ---
   name: task-domain-specialist
   description: One-line description
   tools: Read, Grep, Glob, Edit, Write, Bash
   model: opus
   ---
   ```
3. **Write detailed system prompt** in body
4. **Create skill sheet** in `manifests/{agent-name}.yaml`
5. **Save agent** to appropriate `pool/` subdirectory

### Integration Rules

When merging agents:

1. **Identify source agents** with partial coverage
2. **Combine capabilities**, eliminate redundancy
3. **Resolve conflicts** between source agents
4. **Record lineage** in skill sheet `parent_agents` field
5. **Save to `pool/integrated/merged-{source1}-{source2}.md`**

### Evolution Tracking

After every task execution, update the agent's skill sheet:

```yaml
metrics:
  usage_count: 5        # Increment
  success_rate: 0.85    # (successes / usage_count)
  last_used: 2025-01-15 # Current date
```

### Elite Promotion

An agent qualifies for elite status when:
- `usage_count >= 5`
- `success_rate >= 0.8`

Action: Move from `specialized/` or `integrated/` to `elite/`

### Reference Files

- `.claude/skills/evaluation-first-decision/SKILL.md` - Decision gate logic
- `.claude/agents/orchestrator.md` - Full orchestrator logic
- `.claude/agents/_template.md` - Agent definition template
- `.claude/agents/manifests/_template.yaml` - Skill sheet template

---

## Quick Reference

| Situation | Action |
|-----------|--------|
| Consequential decision before implementation | Run `/evaluation-first-decision` |
| Verdict is HOLD or STOP | Do not execute; satisfy verdict-changing conditions first |
| GO or approved PILOT | Pass the Decision Card to `/task` |
| New task received | Scan `pool/`, calculate coverage |
| Perfect match exists | Use existing agent |
| Partial matches | Create integrated agent |
| No good match | Create specialized agent |
| Task completed | Update `manifests/` metrics |
| High-performing agent | Promote to `elite/` |
