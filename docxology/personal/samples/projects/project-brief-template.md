---
type: project
subtype: brief
created: "{{DATE}}"
updated: "{{DATE}}"
status: planning
project_name: "{{PROJECT_NAME}}"
author: "{{NAME}}"
tags: [project, brief, {{PROJECT_TAG}}]
pai_integration:
  track_history: true
  enable_voice: true
  agent_access: true
---

# Project Brief: {{PROJECT_NAME}}

**Project Lead**: {{NAME}}
**Created**: {{DATE}}
**Target Start**: {{START_DATE}}
**Target Completion**: {{END_DATE}}
**Status**: [Planning / Active / On Hold / Completed]

---

## Executive Summary

<!-- PAI:SECTION:summary -->
### One-Liner
[Single sentence describing what this project is]

### Problem Statement
[What problem does this project solve? Why does it matter?]

### Proposed Solution
[High-level description of the approach]

### Expected Outcome
[What will exist when this project is complete?]
<!-- PAI:END:summary -->

---

## Project Definition

<!-- PAI:SECTION:definition -->
### Vision
[Long-term vision this project contributes to]

### Goals
| Goal | Measurable Outcome | Priority |
|------|-------------------|----------|
| [Goal 1] | [How we'll know it's achieved] | High |
| [Goal 2] | [How we'll know it's achieved] | Medium |
| [Goal 3] | [How we'll know it's achieved] | Low |

### Non-Goals (Explicit Scope Limits)
- [What this project will NOT do]
- [What's out of scope]
- [What we're deferring]

### Success Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]
<!-- PAI:END:definition -->

---

## Context & Background

<!-- PAI:SECTION:context -->
### Why Now?
[What makes this the right time for this project?]

### Prior Art
| Related Work | Status | Learnings |
|--------------|--------|-----------|
| [Previous attempt/related project] | [Outcome] | [What we learned] |

### Dependencies
| Dependency | Type | Status | Risk if Delayed |
|------------|------|--------|-----------------|
| [Dependency 1] | [Tech/Resource/External] | [Status] | [Impact] |
| [Dependency 2] | [Tech/Resource/External] | [Status] | [Impact] |

### Constraints
- **Time**: [Deadline or time constraint]
- **Budget**: [Budget constraint]
- **Resources**: [Resource limitations]
- **Technical**: [Technical constraints]
<!-- PAI:END:context -->

---

## Stakeholders

<!-- PAI:SECTION:stakeholders -->
### Core Team
| Role | Person | Responsibilities |
|------|--------|------------------|
| Lead | {{NAME}} | [Responsibilities] |
| [Role] | [Name] | [Responsibilities] |

### Stakeholders
| Stakeholder | Interest | Engagement Level |
|-------------|----------|------------------|
| [Stakeholder 1] | [Their interest] | [Inform/Consult/Involve] |
| [Stakeholder 2] | [Their interest] | [Inform/Consult/Involve] |

### Communication Plan
| Audience | Channel | Frequency | Owner |
|----------|---------|-----------|-------|
| [Team] | [Channel] | [Frequency] | [Who] |
| [Stakeholders] | [Channel] | [Frequency] | [Who] |
<!-- PAI:END:stakeholders -->

---

## Approach & Methodology

<!-- PAI:SECTION:approach -->
### Overall Approach
[Description of how the project will be executed]

### Methodology
[Agile / Waterfall / Hybrid / Research-based / etc.]

### Phases
| Phase | Description | Duration | Deliverables |
|-------|-------------|----------|--------------|
| Phase 1 | [Description] | [Duration] | [Deliverables] |
| Phase 2 | [Description] | [Duration] | [Deliverables] |
| Phase 3 | [Description] | [Duration] | [Deliverables] |

### Key Decisions to Make
| Decision | Options | Deadline | Owner |
|----------|---------|----------|-------|
| [Decision 1] | [Options] | [Date] | [Who] |
| [Decision 2] | [Options] | [Date] | [Who] |
<!-- PAI:END:approach -->

---

## Technical Specification

<!-- PAI:SECTION:technical -->
### Architecture Overview
```
[High-level architecture diagram or description]
```

### Technology Stack
| Component | Technology | Rationale |
|-----------|------------|-----------|
| [Component] | [Tech choice] | [Why] |

### Technical Requirements
- [ ] [Requirement 1]
- [ ] [Requirement 2]
- [ ] [Requirement 3]

### Integration Points
| System | Integration Type | Complexity |
|--------|-----------------|------------|
| [System 1] | [API/File/Manual] | [Low/Med/High] |

### Data Requirements
- **Input**: [What data is needed]
- **Output**: [What data is produced]
- **Storage**: [Where data lives]
- **Privacy**: [Privacy considerations]
<!-- PAI:END:technical -->

---

## Milestones & Timeline

<!-- PAI:SECTION:timeline -->
### Major Milestones
| Milestone | Description | Target Date | Status |
|-----------|-------------|-------------|--------|
| M1: Kickoff | [Description] | {{START_DATE}} | [ ] |
| M2: [Name] | [Description] | [Date] | [ ] |
| M3: [Name] | [Description] | [Date] | [ ] |
| M4: Completion | [Description] | {{END_DATE}} | [ ] |

### Detailed Timeline
```
Week 1-2:  [Activities]
Week 3-4:  [Activities]
Week 5-6:  [Activities]
...
```

### Critical Path
[What must happen in sequence vs. what can be parallelized]
<!-- PAI:END:timeline -->

---

## Resources

<!-- PAI:SECTION:resources -->
### Budget (if applicable)
| Category | Estimated | Actual | Notes |
|----------|-----------|--------|-------|
| [Category 1] | [Amount] | | |
| [Category 2] | [Amount] | | |
| **Total** | [Total] | | |

### Tools & Infrastructure
| Tool | Purpose | Status | Cost |
|------|---------|--------|------|
| [Tool 1] | [Purpose] | [Have/Need] | [Cost] |
| [Tool 2] | [Purpose] | [Have/Need] | [Cost] |

### External Resources
- [Resource 1]
- [Resource 2]
<!-- PAI:END:resources -->

---

## Risk Assessment

<!-- PAI:SECTION:risks -->
### Risk Register
| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] | [Who] |
| [Risk 2] | [H/M/L] | [H/M/L] | [Strategy] | [Who] |
| [Risk 3] | [H/M/L] | [H/M/L] | [Strategy] | [Who] |

### Risk Matrix
```
         │ Low Impact │ Med Impact │ High Impact
─────────┼────────────┼────────────┼────────────
High Prob│            │            │ [Risk X]
Med Prob │            │ [Risk Y]   │
Low Prob │ [Risk Z]   │            │
```

### Contingency Plans
| Trigger | Response |
|---------|----------|
| [If X happens] | [We will Y] |
<!-- PAI:END:risks -->

---

## Quality & Testing

<!-- PAI:SECTION:quality -->
### Quality Standards
- [Standard 1]
- [Standard 2]

### Testing Approach
| Test Type | Scope | When | Owner |
|-----------|-------|------|-------|
| [Unit tests] | [Scope] | [When] | [Who] |
| [Integration] | [Scope] | [When] | [Who] |
| [User testing] | [Scope] | [When] | [Who] |

### Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]
<!-- PAI:END:quality -->

---

## Documentation & Handoff

<!-- PAI:SECTION:documentation -->
### Documentation Required
- [ ] Technical documentation
- [ ] User documentation
- [ ] API documentation
- [ ] Runbooks/Operational docs

### Handoff Plan
| Recipient | What | When |
|-----------|------|------|
| [Who] | [What they receive] | [When] |

### Training Needs
- [Training 1]
- [Training 2]
<!-- PAI:END:documentation -->

---

## Open Questions

<!-- PAI:SECTION:questions -->
### Unresolved Questions
| Question | Owner | Due Date | Status |
|----------|-------|----------|--------|
| [Question 1] | [Who] | [Date] | [ ] |
| [Question 2] | [Who] | [Date] | [ ] |

### Assumptions
- [Assumption 1]
- [Assumption 2]

### Decisions Needed
- [ ] [Decision 1]
- [ ] [Decision 2]
<!-- PAI:END:questions -->

---

## Approvals

<!-- PAI:SECTION:approvals -->
### Sign-off Required
| Role | Name | Date | Status |
|------|------|------|--------|
| Project Lead | {{NAME}} | | [ ] Approved |
| [Stakeholder] | [Name] | | [ ] Approved |

### Version History
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1 | {{DATE}} | Initial draft | {{NAME}} |
<!-- PAI:END:approvals -->

---

## PAI Integration

> **Agent Commands**:
> - "Generate project status report" - Create status update
> - "Identify project risks" - Risk analysis
> - "Update milestone status" - Track progress
> - "Create sprint plan from brief" - Break down into tasks

> **Linked Documents**:
> - Milestone Tracker: `projects/{{PROJECT_SLUG}}-milestones.md`
> - Meeting Notes: `notes/{{PROJECT_SLUG}}/`
> - Research: `research/{{PROJECT_SLUG}}/`

---

*Project ID: {{PROJECT_ID}} | Template v1.0*
