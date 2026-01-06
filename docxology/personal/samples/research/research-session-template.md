---
type: research
subtype: session
created: "{{DATE}}"
updated: "{{DATE}}"
status: active
domain: "{{DOMAIN}}"
author: "{{NAME}}"
tags: [research, session, {{DOMAIN_TAG}}]
pai_integration:
  track_history: true
  enable_voice: false
  agent_access: true
  auto_summarize: true
---

# Research Session: {{TOPIC}}

**Domain**: {{DOMAIN}}
**Date**: {{DATE}}
**Duration**: {{START_TIME}} - {{END_TIME}}
**Session Type**: [Exploratory / Deep Dive / Literature Review / Synthesis]

---

## Session Objectives

<!-- PAI:SECTION:objectives -->
### Primary Question
> [The main question driving this research session]

### Secondary Questions
1. [Supporting question 1]
2. [Supporting question 2]
3. [Supporting question 3]

### Success Criteria
- [ ] [What would make this session successful]
- [ ] [Specific deliverable or insight]
<!-- PAI:END:objectives -->

---

## Background Context

<!-- PAI:SECTION:context -->
### Prior Knowledge
[What you already know about this topic]

### Related Work
| Source | Key Points | Relevance |
|--------|------------|-----------|
| [Source 1] | [Key points] | [How it relates] |
| [Source 2] | [Key points] | [How it relates] |

### Open Questions from Previous Sessions
- [Question 1]
- [Question 2]
<!-- PAI:END:context -->

---

## Sources Consulted

<!-- PAI:SECTION:sources -->
### Papers & Articles
| Title | Authors | Year | Key Contribution | Notes |
|-------|---------|------|------------------|-------|
| | | | | |
| | | | | |

### Books
| Title | Author | Chapters | Key Ideas |
|-------|--------|----------|-----------|
| | | | |

### Web Resources
| URL | Type | Credibility | Key Points |
|-----|------|-------------|------------|
| | [Blog/Docs/Video] | [High/Med/Low] | |

### Conversations & Discussions
| With | Date | Key Insights |
|------|------|--------------|
| | | |
<!-- PAI:END:sources -->

---

## Key Findings

<!-- PAI:SECTION:findings -->
### Major Discoveries
1. **[Finding 1]**
   - Evidence: [Supporting evidence]
   - Implications: [What this means]
   - Confidence: [High/Medium/Low]

2. **[Finding 2]**
   - Evidence: [Supporting evidence]
   - Implications: [What this means]
   - Confidence: [High/Medium/Low]

### Surprising Insights
- [Unexpected finding 1]
- [Unexpected finding 2]

### Contradictions Found
| Claim A | Claim B | Resolution/Note |
|---------|---------|-----------------|
| | | |
<!-- PAI:END:findings -->

---

## Concepts & Definitions

<!-- PAI:SECTION:concepts -->
### New Terms Encountered
| Term | Definition | Source | Context |
|------|------------|--------|---------|
| | | | |
| | | | |

### Concept Map
```
[Main Concept]
    ├── [Sub-concept 1]
    │   ├── [Detail]
    │   └── [Detail]
    ├── [Sub-concept 2]
    │   └── [Detail]
    └── [Sub-concept 3]
        ├── [Detail]
        └── [Detail]
```

### Relationships Identified
- [Concept A] → [relates to] → [Concept B]
- [Concept C] → [causes] → [Concept D]
<!-- PAI:END:concepts -->

---

## Hypotheses & Theories

<!-- PAI:SECTION:hypotheses -->
### Working Hypotheses
| Hypothesis | Supporting Evidence | Counter Evidence | Status |
|------------|---------------------|------------------|--------|
| [H1] | [Evidence for] | [Evidence against] | [Active/Rejected/Confirmed] |
| [H2] | [Evidence for] | [Evidence against] | [Active/Rejected/Confirmed] |

### Theoretical Framework
[Description of theoretical lens being used]

### Predictions
If [hypothesis] is correct, then we should observe:
1. [Prediction 1]
2. [Prediction 2]
<!-- PAI:END:hypotheses -->

---

## Methodology Notes

<!-- PAI:SECTION:methodology -->
### Approach Used
- [Method 1]: [Description]
- [Method 2]: [Description]

### Search Strategy
- **Keywords**: [search terms used]
- **Databases**: [sources searched]
- **Filters**: [date range, type, etc.]

### Analysis Method
[How you analyzed the information]

### Limitations
- [Limitation 1]
- [Limitation 2]
<!-- PAI:END:methodology -->

---

## Synthesis & Integration

<!-- PAI:SECTION:synthesis -->
### How This Connects
| Existing Knowledge | New Finding | Integration |
|--------------------|-------------|-------------|
| [What you knew] | [What you learned] | [How they connect] |

### Updated Mental Model
[Description of how your understanding has evolved]

### Implications for Other Work
- [Project/Area 1]: [Implication]
- [Project/Area 2]: [Implication]
<!-- PAI:END:synthesis -->

---

## Questions Generated

<!-- PAI:SECTION:questions -->
### Answered Questions
- [x] [Question] → [Answer]

### New Questions
- [ ] [Question requiring more research]
- [ ] [Question for expert consultation]
- [ ] [Question for experimentation]

### Questions for Collaborators
| Question | Best Person to Ask | Status |
|----------|-------------------|--------|
| | | [ ] Asked |
<!-- PAI:END:questions -->

---

## Action Items

<!-- PAI:SECTION:actions -->
### Immediate Follow-ups
- [ ] [Action 1] - Due: [Date]
- [ ] [Action 2] - Due: [Date]

### Future Research
- [ ] [Topic to explore later]
- [ ] [Paper to read]

### To Share/Discuss
- [ ] Share [finding] with [person]
- [ ] Discuss [topic] in [meeting/forum]
<!-- PAI:END:actions -->

---

## Session Reflection

<!-- PAI:SECTION:reflection -->
### What Worked
- [Effective approach 1]
- [Effective approach 2]

### What Didn't Work
- [Ineffective approach]

### For Next Session
- [Improvement idea]
- [Different approach to try]

### Time Efficiency
- Productive time: [X] minutes
- Distracted time: [X] minutes
- Most productive phase: [Beginning/Middle/End]
<!-- PAI:END:reflection -->

---

## Raw Notes

<!-- PAI:SECTION:raw -->
[Unstructured notes, quotes, screenshots, stream of consciousness]
<!-- PAI:END:raw -->

---

## Session Summary

<!-- PAI:SECTION:summary -->
### One-Sentence Summary
[Capture the essence of what you learned]

### Key Takeaways
1. [Takeaway 1]
2. [Takeaway 2]
3. [Takeaway 3]

### Confidence Level
Overall confidence in findings: [High/Medium/Low]

### Next Session Focus
[What to explore next time]
<!-- PAI:END:summary -->

---

## PAI Integration

> **Agent Commands**:
> - "Summarize this research session" - Generate executive summary
> - "Find related papers on [topic]" - Expand literature search
> - "Compare findings with [previous session]" - Cross-reference
> - "Generate citation list" - Format references

> **History Integration**:
> This session will be saved to: `~/.claude/history/research/{{DATE}}-{{TOPIC_SLUG}}.md`

---

*Session ID: {{SESSION_ID}} | Template v1.0*
