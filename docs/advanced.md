# Advanced Guide

Strategies for optimizing your agent ecosystem.

## Evolution Strategies

### Encouraging Strong Integrations

When you notice certain agent combinations working well together, update their skill sheets:

```yaml
# auth-specialist.yaml
synergy_hints:
  - agent: db-specialist
    reason: "Excellent for auth with persistent sessions"
  - agent: cache-specialist
    reason: "Essential for token caching"
```

These hints guide the orchestrator toward proven combinations.

### Permanent Integrations

If an integrated agent is selected repeatedly with high success:

1. Review the integrated agent's definition
2. Refine its capabilities based on observed usage
3. Consider promoting to elite early if performance is exceptional

### Controlled Specialization

Prevent over-generalization by setting clear constraints:

```yaml
# db-specialist.yaml
constraints:
  - No application logic
  - No API design
  - Query optimization only, not business rules
```

Clear boundaries prevent "god agents" that try to do everything poorly.

## Pool Maintenance

### Identifying Dead Agents

Agents that haven't been used may be:
- Obsolete (superseded by integrations)
- Too specialized (narrow use case)
- Poorly defined (low coverage scores)

Check `manifests/` for:
```yaml
metrics:
  usage_count: 0
  last_used: null  # Never used
```

Consider:
- Merging into a broader agent
- Refining capabilities for better matching
- Removing if truly obsolete

### Preventing Fragmentation

Too many tiny agents creates overhead. Watch for:
- Agents with only 1-2 capabilities
- High overlap between agents
- Frequent "create new" decisions for similar domains

Solution: Lower the integration threshold or add synergy hints.

### Gap Analysis

Track "create new" events. Patterns reveal:
- Domains you work in frequently
- Missing coverage in your ecosystem
- Opportunities for strategic agent creation

## Advanced Skill Sheet Patterns

### Versioned Evolution

Track agent evolution through versions:

```yaml
name: api-specialist
version: "2.0"
changelog:
  - version: "2.0"
    date: 2025-01-15
    changes: "Added GraphQL support via integration"
  - version: "1.0"
    date: 2025-01-01
    changes: "Initial REST focus"
```

### Conditional Capabilities

Some capabilities only apply in context:

```yaml
capabilities:
  - REST API design
  - GraphQL (when project uses Apollo)
  - gRPC (when project uses Protocol Buffers)
```

### Multi-Generation Lineage

For deeply integrated agents:

```yaml
name: hyper-fullstack-v3
tier: elite
parent_agents: [merged-frontend-backend-v2, devops-specialist]
lineage:
  generation_1:
    - frontend-specialist
    - backend-specialist
  generation_2:
    - merged-frontend-backend
  generation_3:
    - merged-frontend-backend-v2 (added caching)
  generation_4:
    - hyper-fullstack-v3 (current)
```

## Customizing the Orchestrator

### Adjusting Thresholds

Default decision matrix:
- 90%+ → Use existing
- 60-90% → Integrate
- <60% → Create new

Modify in `orchestrator.md` based on your preferences:

**Conservative (prefer existing)**:
```
85%+ → Use existing
50-85% → Integrate
<50% → Create new
```

**Aggressive (prefer specialization)**:
```
95%+ → Use existing
70-95% → Integrate
<70% → Create new
```

### Adding Decision Factors

Beyond coverage, consider:

```markdown
### Additional Factors

- **Task criticality**: High-stakes tasks prefer elite agents
- **Time constraints**: Urgent tasks use existing when possible
- **Learning mode**: Experimental tasks encourage new agents
```

## Team Operations

### Shared Agent Pool

For team projects, the `pool/` directory should be version controlled:

```
.claude/agents/pool/        # Committed to git
.claude/agents/manifests/   # Committed to git
```

This allows:
- Team members to benefit from each other's agent evolutions
- Review of new/integrated agents via PR
- Tracking of ecosystem growth over time

### Agent Review Process

When a new agent is created or integrated:

1. Check the agent definition for quality
2. Verify capabilities match actual task requirements
3. Ensure constraints are appropriate
4. Review synergy_hints for accuracy

### Metrics Dashboard

Periodically review:

```bash
# Find most-used agents
grep -r "usage_count" .claude/agents/manifests/ | sort -t: -k2 -n -r

# Find highest success rates
grep -r "success_rate" .claude/agents/manifests/ | sort -t: -k2 -n -r

# Find promotion candidates
grep -r "promotion_candidate: true" .claude/agents/manifests/
```

## Future Possibilities

### Automated Pruning

Script to identify and archive unused agents:

```bash
# Find agents unused for 30+ days
find .claude/agents/pool -name "*.md" -mtime +30
```

### Cross-Project Pollination

Export successful elite agents for use in other projects:

```bash
cp .claude/agents/pool/elite/proven-agent.md ~/.claude/shared-agents/
```

### Ecosystem Analytics

Track over time:
- Total agents created
- Integration success rate
- Elite promotion rate
- Most effective lineages

## Summary

Effective orchestration requires:

1. **Trust the process**: Let the orchestrator manage agent creation/integration
2. **Maintain quality**: Review new agents, update skill sheets
3. **Watch for patterns**: Repeated integrations suggest permanent mergers
4. **Prune regularly**: Remove or refine underperforming agents
5. **Share knowledge**: Version control the pool for team benefit
