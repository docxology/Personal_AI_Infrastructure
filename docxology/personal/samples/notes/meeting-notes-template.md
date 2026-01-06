---
type: note
subtype: meeting
created: "{{DATE}}"
meeting_date: "{{MEETING_DATE}}"
meeting_type: "{{MEETING_TYPE}}"
author: "{{NAME}}"
tags: [meeting, notes, {{MEETING_TAG}}]
pai_integration:
  track_history: true
  enable_voice: true
  agent_access: true
---

# Meeting Notes: {{MEETING_TITLE}}

**Date**: {{MEETING_DATE}}
**Time**: {{START_TIME}} - {{END_TIME}} ({{DURATION}})
**Location**: [In-person location / Video call link / Phone]
**Type**: [1:1 / Team / Project / Client / External / Workshop]

---

## Attendees

<!-- PAI:SECTION:attendees -->
| Name | Role | Organization | Present |
|------|------|--------------|---------|
| {{NAME}} | [Your role] | [Org] | [x] |
| [Name 2] | [Role] | [Org] | [ ] |
| [Name 3] | [Role] | [Org] | [ ] |

**Facilitator**: [Name]
**Note Taker**: {{NAME}}
<!-- PAI:END:attendees -->

---

## Agenda

<!-- PAI:SECTION:agenda -->
| # | Topic | Owner | Time | Status |
|---|-------|-------|------|--------|
| 1 | [Topic 1] | [Who] | [X min] | [x] Covered |
| 2 | [Topic 2] | [Who] | [X min] | [ ] Skipped |
| 3 | [Topic 3] | [Who] | [X min] | [ ] Deferred |

**Pre-read Materials**:
- [Document 1]
- [Document 2]
<!-- PAI:END:agenda -->

---

## Discussion Notes

<!-- PAI:SECTION:discussion -->
### Topic 1: [Topic Name]

**Context**: [Brief background]

**Key Points Discussed**:
- [Point 1]
- [Point 2]
- [Point 3]

**Decisions Made**:
- [Decision 1]
- [Decision 2]

**Open Questions**:
- [Question 1]
- [Question 2]

---

### Topic 2: [Topic Name]

**Context**: [Brief background]

**Key Points Discussed**:
- [Point 1]
- [Point 2]

**Decisions Made**:
- [Decision 1]

**Open Questions**:
- [Question 1]

---

### Topic 3: [Topic Name]

**Key Points**:
- [Point 1]
- [Point 2]

**Outcome**: [Summary of discussion outcome]
<!-- PAI:END:discussion -->

---

## Decisions Log

<!-- PAI:SECTION:decisions -->
| # | Decision | Made By | Rationale | Impact |
|---|----------|---------|-----------|--------|
| D1 | [Decision] | [Who decided] | [Why] | [Who/what affected] |
| D2 | [Decision] | [Who decided] | [Why] | [Who/what affected] |

### Decisions Deferred
| Topic | Reason | Target Date |
|-------|--------|-------------|
| [Topic] | [Why deferred] | [When to decide] |
<!-- PAI:END:decisions -->

---

## Action Items

<!-- PAI:SECTION:actions -->
| # | Action | Owner | Due Date | Priority | Status |
|---|--------|-------|----------|----------|--------|
| A1 | [Action description] | [Name] | [Date] | [H/M/L] | [ ] |
| A2 | [Action description] | [Name] | [Date] | [H/M/L] | [ ] |
| A3 | [Action description] | [Name] | [Date] | [H/M/L] | [ ] |
| A4 | [Action description] | [Name] | [Date] | [H/M/L] | [ ] |

### My Action Items
- [ ] [A1]: [Description] - Due: [Date]
- [ ] [A2]: [Description] - Due: [Date]

### Waiting On
| Item | From | Expected By |
|------|------|-------------|
| [Item] | [Person] | [Date] |
<!-- PAI:END:actions -->

---

## Key Quotes & Insights

<!-- PAI:SECTION:quotes -->
> "[Important quote from the meeting]" - [Speaker]

> "[Another significant statement]" - [Speaker]

**Aha Moments**:
- [Insight 1]
- [Insight 2]
<!-- PAI:END:quotes -->

---

## Follow-up Items

<!-- PAI:SECTION:followup -->
### Next Meeting
- **Date**: [Next meeting date]
- **Time**: [Time]
- **Agenda Items**: [What to cover]

### Topics for Future Discussion
- [Topic 1]
- [Topic 2]

### Information to Gather
- [ ] [Information needed before next meeting]
- [ ] [Research to do]
<!-- PAI:END:followup -->

---

## Personal Reflection

<!-- PAI:SECTION:reflection -->
### My Takeaways
- [Personal insight 1]
- [Personal insight 2]

### Concerns/Risks Noted
- [Concern 1]
- [Concern 2]

### Relationship Notes
[Observations about dynamics, tone, alignment]

### Follow-up Conversations Needed
| With | About | Priority |
|------|-------|----------|
| [Person] | [Topic] | [H/M/L] |
<!-- PAI:END:reflection -->

---

## Attachments & References

<!-- PAI:SECTION:attachments -->
### Documents Shared
| Document | Link/Location | Notes |
|----------|---------------|-------|
| [Doc name] | [Link] | [Context] |

### Related Materials
- [Link to related project]
- [Link to previous meeting notes]
- [Reference document]
<!-- PAI:END:attachments -->

---

## Meeting Effectiveness

<!-- PAI:SECTION:effectiveness -->
### Quick Assessment
- Meeting started/ended on time: [Yes/No]
- Agenda covered: [All/Most/Some/Little]
- Clear outcomes: [Yes/Partial/No]
- Right attendees: [Yes/No]

### Improvement Notes
[What could make future meetings better]
<!-- PAI:END:effectiveness -->

---

## Summary

<!-- PAI:SECTION:summary -->
### TL;DR
[2-3 sentence summary of the entire meeting]

### Key Outcomes
1. [Outcome 1]
2. [Outcome 2]
3. [Outcome 3]

### Critical Next Steps
1. [Most important follow-up]
2. [Second most important]
<!-- PAI:END:summary -->

---

## PAI Integration

> **Agent Commands**:
> - "Summarize this meeting" - Generate executive summary
> - "Extract action items" - Pull out all actions
> - "Send meeting summary to [person]" - Share notes
> - "Compare to previous [project] meeting" - Track progress

> **Voice Commands**:
> - "Read meeting summary" - Audio overview
> - "What are my action items?" - Personal tasks

> **Auto-save**: This meeting will be saved to `~/.claude/history/sessions/meetings/`

---

*Meeting ID: {{MEETING_ID}} | Notes v1.0*
