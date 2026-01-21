# Personal Content Samples

Configurable templates for personal documentation. Use these as starting points for your own content.

---

## How to Use These Samples

### 1. Copy and Customize

```bash
# Copy a template to your personal folder
cp samples/plans/life-plan-template.md ../my-life-plan-2026.md

# Or copy to docxology root for quick access
cp samples/plans/life-plan-template.md ../../MY_PLAN.md
```

### 2. Replace Variables

Templates use `{{variable}}` placeholders. Replace with your values:

| Variable | Description | Example |
|----------|-------------|---------|
| `{{NAME}}` | Your name | Daniel Ari Friedman |
| `{{YEAR}}` | Target year | 2026 |
| `{{QUARTER}}` | Quarter (Q1-Q4) | Q1 |
| `{{PROJECT}}` | Project name | CEREBRUM |
| `{{DOMAIN}}` | Knowledge domain | Active Inference |
| `{{DATE}}` | Current date | 2026-01-05 |
| `{{LOCATION}}` | Your location | Crescent City, CA |

### 3. PAI Integration

These templates are designed to work with PAI features:

- **Agents**: Can process and update your documents
- **Skills**: Templates reference skill capabilities
- **History**: Changes tracked in history system
- **Voice**: Summaries can be read aloud

---

## Sample Categories

### Plans (`plans/`)

| Template | Purpose | Use When |
|----------|---------|----------|
| `life-plan-template.md` | Quarterly/annual life planning | Goal setting, life reviews |
| `project-plan-template.md` | Project planning and tracking | Starting new projects |
| `weekly-review-template.md` | Weekly review and planning | Weekly check-ins |

### Research (`research/`)

| Template | Purpose | Use When |
|----------|---------|----------|
| `research-session-template.md` | Document research sessions | Deep research work |
| `literature-review-template.md` | Systematic literature review | Academic research |
| `concept-exploration-template.md` | Explore new concepts | Learning new topics |

### Projects (`projects/`)

| Template | Purpose | Use When |
|----------|---------|----------|
| `project-brief-template.md` | Project definition | Project kickoff |
| `milestone-tracker-template.md` | Track project milestones | Ongoing projects |
| `retrospective-template.md` | Project retrospectives | Project completion |

### Workflows (`workflows/`)

| Template | Purpose | Use When |
|----------|---------|----------|
| `daily-routine-template.md` | Daily routine structure | Establishing habits |
| `research-workflow-template.md` | Research process | Research projects |
| `writing-workflow-template.md` | Writing process | Content creation |
| `decision-framework-template.md` | Decision making | Important decisions |

### Notes (`notes/`)

| Template | Purpose | Use When |
|----------|---------|----------|
| `meeting-notes-template.md` | Meeting documentation | Any meeting |
| `one-on-one-template.md` | 1:1 meeting notes | Regular 1:1s |
| `learning-log-template.md` | Track learning | Skill development |

---

## Template Features

### Metadata Headers

All templates include YAML frontmatter for PAI integration:

```yaml
---
type: plan|research|project|workflow|note
created: {{DATE}}
updated: {{DATE}}
status: draft|active|completed|archived
tags: [tag1, tag2]
pai_integration:
  track_history: true
  enable_voice: false
  agent_access: true
---
```

### Section Markers

Templates use markers for agent processing:

```markdown
<!-- PAI:SECTION:goals -->
Your goals here...
<!-- PAI:END:goals -->
```

### Checklists

Trackable progress items:

```markdown
- [ ] Pending task
- [x] Completed task
- [~] In progress
- [-] Blocked/cancelled
```

### Links to PAI

Templates can reference PAI capabilities:

```markdown
> **PAI Note**: Use `/agents` to spawn research agents for this section
> **PAI Note**: Run health check with `bun run docxology/scripts/setup-health-check.ts`
```

---

## Customization Guide

### Adding Your Own Templates

1. Create new template in appropriate folder
2. Use `{{variable}}` for customizable values
3. Include YAML frontmatter
4. Add to this README

### Modifying Existing Templates

1. Copy to your personal folder first
2. Customize for your needs
3. Keep original samples intact

### Template Variables Reference

Create a `variables.json` in your personal folder:

```json
{
  "NAME": "Your Name",
  "YEAR": "2026",
  "LOCATION": "Your City",
  "PRIMARY_DOMAIN": "Your Field",
  "PROJECTS": ["Project1", "Project2"],
  "COLLABORATORS": ["Person1", "Person2"]
}
```

Then use with PAI:
```
"Apply my variables to the life plan template"
```

---

## PAI Commands for Templates

### Generate from Template

```
"Create a new research session from the template for Active Inference"
```

### Update Existing Document

```
"Update my life plan with Q1 progress"
```

### Review and Summarize

```
"Summarize my project milestones and identify blockers"
```

### Voice Summary

```
"Read me a summary of my weekly review"
```

---

## Privacy Notes

- **Samples are public** - included in git
- **Your personal copies are private** - gitignored
- **Never commit** personal data to samples folder
- **Use variables** to keep templates generic

---

*These samples demonstrate PAI capabilities. Copy and customize for your personal use.*
