---
type: workflow
subtype: decision
created: "{{DATE}}"
updated: "{{DATE}}"
status: in-progress
decision_name: "{{DECISION_NAME}}"
author: "{{NAME}}"
tags: [decision, framework, analysis]
pai_integration:
  track_history: true
  enable_voice: false
  agent_access: true
---

# Decision Framework: {{DECISION_NAME}}

**Decision Owner**: {{NAME}}
**Date**: {{DATE}}
**Deadline**: {{DECISION_DEADLINE}}
**Reversibility**: [Easily Reversible / Partially Reversible / Irreversible]

---

## Decision Context

<!-- PAI:SECTION:context -->
### The Decision
> [Clear, specific statement of what needs to be decided]

### Why This Decision Matters
- Impact scope: [Personal / Team / Organization / External]
- Time horizon: [Short-term / Medium-term / Long-term]
- Stakes: [Low / Medium / High / Critical]

### Trigger
What prompted this decision?
- [Trigger event or circumstance]

### Constraints
| Constraint | Type | Flexibility |
|------------|------|-------------|
| [Constraint 1] | [Time/Budget/Resource/Policy] | [Hard/Soft] |
| [Constraint 2] | [Time/Budget/Resource/Policy] | [Hard/Soft] |
<!-- PAI:END:context -->

---

## Current State

<!-- PAI:SECTION:current -->
### Status Quo
[Description of current situation if no decision is made]

### Problems with Status Quo
1. [Problem 1]
2. [Problem 2]
3. [Problem 3]

### What's Working
1. [What to preserve]
2. [What to preserve]
<!-- PAI:END:current -->

---

## Options Analysis

<!-- PAI:SECTION:options -->
### Option 1: {{OPTION_1_NAME}}

**Description**: [Detailed description]

**Pros**:
- [Pro 1]
- [Pro 2]
- [Pro 3]

**Cons**:
- [Con 1]
- [Con 2]
- [Con 3]

**Requirements**:
- [What's needed to implement]

**Risks**:
- [Risk 1]: [Mitigation]
- [Risk 2]: [Mitigation]

**Estimated Outcome**: [What success looks like]

---

### Option 2: {{OPTION_2_NAME}}

**Description**: [Detailed description]

**Pros**:
- [Pro 1]
- [Pro 2]
- [Pro 3]

**Cons**:
- [Con 1]
- [Con 2]
- [Con 3]

**Requirements**:
- [What's needed to implement]

**Risks**:
- [Risk 1]: [Mitigation]
- [Risk 2]: [Mitigation]

**Estimated Outcome**: [What success looks like]

---

### Option 3: {{OPTION_3_NAME}}

**Description**: [Detailed description]

**Pros**:
- [Pro 1]
- [Pro 2]

**Cons**:
- [Con 1]
- [Con 2]

**Requirements**:
- [What's needed to implement]

**Risks**:
- [Risk 1]: [Mitigation]

**Estimated Outcome**: [What success looks like]

---

### Option 4: Do Nothing / Defer

**Description**: Maintain status quo or delay decision

**Pros**:
- More time for information
- Preserves optionality
- [Other]

**Cons**:
- [Cost of delay]
- [Missed opportunity]
- [Other]

**When to Choose**: [Circumstances where this is right]
<!-- PAI:END:options -->

---

## Evaluation Criteria

<!-- PAI:SECTION:criteria -->
### Weighted Criteria Matrix

| Criterion | Weight | Option 1 | Option 2 | Option 3 | Option 4 |
|-----------|--------|----------|----------|----------|----------|
| [Criterion 1] | [1-5] | [1-10] | [1-10] | [1-10] | [1-10] |
| [Criterion 2] | [1-5] | [1-10] | [1-10] | [1-10] | [1-10] |
| [Criterion 3] | [1-5] | [1-10] | [1-10] | [1-10] | [1-10] |
| [Criterion 4] | [1-5] | [1-10] | [1-10] | [1-10] | [1-10] |
| [Criterion 5] | [1-5] | [1-10] | [1-10] | [1-10] | [1-10] |
| **Weighted Total** | | **[Sum]** | **[Sum]** | **[Sum]** | **[Sum]** |

### Criteria Definitions
- **[Criterion 1]**: [What this means, how to score]
- **[Criterion 2]**: [What this means, how to score]
- **[Criterion 3]**: [What this means, how to score]
- **[Criterion 4]**: [What this means, how to score]
- **[Criterion 5]**: [What this means, how to score]

### Must-Have Requirements
- [ ] [Non-negotiable requirement 1]
- [ ] [Non-negotiable requirement 2]

| Option | Meets Must-Haves? |
|--------|-------------------|
| Option 1 | [Yes/No] |
| Option 2 | [Yes/No] |
| Option 3 | [Yes/No] |
| Option 4 | [Yes/No] |
<!-- PAI:END:criteria -->

---

## Scenario Analysis

<!-- PAI:SECTION:scenarios -->
### Best Case Scenario
| Option | Best Case Outcome | Probability |
|--------|-------------------|-------------|
| Option 1 | [Outcome] | [%] |
| Option 2 | [Outcome] | [%] |
| Option 3 | [Outcome] | [%] |

### Worst Case Scenario
| Option | Worst Case Outcome | Probability | Survivable? |
|--------|-------------------|-------------|-------------|
| Option 1 | [Outcome] | [%] | [Yes/No] |
| Option 2 | [Outcome] | [%] | [Yes/No] |
| Option 3 | [Outcome] | [%] | [Yes/No] |

### Most Likely Scenario
| Option | Most Likely Outcome | Probability |
|--------|---------------------|-------------|
| Option 1 | [Outcome] | [%] |
| Option 2 | [Outcome] | [%] |
| Option 3 | [Outcome] | [%] |

### Regret Minimization
"In 10 years, which decision would I regret NOT making?"
- [Reflection]
<!-- PAI:END:scenarios -->

---

## Additional Perspectives

<!-- PAI:SECTION:perspectives -->
### Stakeholder Views
| Stakeholder | Likely Preference | Rationale |
|-------------|-------------------|-----------|
| [Stakeholder 1] | [Option X] | [Why] |
| [Stakeholder 2] | [Option Y] | [Why] |

### Expert/Advisor Input
| Source | Recommendation | Key Insight |
|--------|----------------|-------------|
| [Expert 1] | [Recommendation] | [Insight] |
| [Expert 2] | [Recommendation] | [Insight] |

### Opposing Views to Consider
- Against Option 1: [Steel-man argument]
- Against Option 2: [Steel-man argument]
- Against Option 3: [Steel-man argument]
<!-- PAI:END:perspectives -->

---

## Cognitive Biases Check

<!-- PAI:SECTION:biases -->
### Bias Audit
| Bias | Risk | Mitigation |
|------|------|------------|
| Confirmation bias | [Risk level] | [How to counter] |
| Sunk cost fallacy | [Risk level] | [How to counter] |
| Availability bias | [Risk level] | [How to counter] |
| Anchoring | [Risk level] | [How to counter] |
| Status quo bias | [Risk level] | [How to counter] |
| Overconfidence | [Risk level] | [How to counter] |

### Pre-Mortem
"If this decision fails, what went wrong?"
- [Potential failure mode 1]
- [Potential failure mode 2]
- [Potential failure mode 3]

### What Would Change My Mind?
- [Evidence/event that would shift my thinking]
- [Information I would need to see]
<!-- PAI:END:biases -->

---

## Decision

<!-- PAI:SECTION:decision -->
### Recommendation
**Selected Option**: [Option Name]

**Confidence Level**: [High / Medium / Low]

### Rationale
1. [Primary reason]
2. [Secondary reason]
3. [Supporting reason]

### Key Tradeoffs Accepted
- Accepting [tradeoff] in exchange for [benefit]
- Accepting [tradeoff] in exchange for [benefit]

### Conditions for Reconsidering
If any of these occur, revisit this decision:
- [ ] [Trigger condition 1]
- [ ] [Trigger condition 2]
<!-- PAI:END:decision -->

---

## Implementation Plan

<!-- PAI:SECTION:implementation -->
### Immediate Actions (Next 48 hours)
- [ ] [Action 1]
- [ ] [Action 2]
- [ ] [Action 3]

### Short-term Actions (Next 2 weeks)
- [ ] [Action 1]
- [ ] [Action 2]

### Communication Plan
| Audience | Message | Channel | Timing |
|----------|---------|---------|--------|
| [Who] | [What to communicate] | [How] | [When] |

### Success Metrics
| Metric | Target | Measurement Method | Check Date |
|--------|--------|-------------------|------------|
| [Metric 1] | [Target] | [How measured] | [Date] |
| [Metric 2] | [Target] | [How measured] | [Date] |

### Review Schedule
- [ ] 30-day check-in: [Date]
- [ ] 90-day review: [Date]
- [ ] [Longer-term review]: [Date]
<!-- PAI:END:implementation -->

---

## Post-Decision Log

<!-- PAI:SECTION:postdecision -->
### Decision Made
- **Date**: {{DECISION_DATE}}
- **Final Choice**: [Option chosen]
- **Deciding Factor**: [What ultimately tipped the decision]

### Outcome Tracking
| Date | Observation | Aligned with Expectation? |
|------|-------------|---------------------------|
| | | |
| | | |

### Lessons Learned
[To be filled after outcome is known]

### Would I Decide Differently?
[Retrospective reflection]
<!-- PAI:END:postdecision -->

---

## PAI Integration

> **Agent Commands**:
> - "Analyze options for [decision]" - Structured analysis
> - "Check for biases in my reasoning" - Bias audit
> - "Generate decision summary" - Executive summary
> - "Compare this to past decisions" - Pattern matching

> **Voice Commands**:
> - "Read decision recommendation" - Audio summary
> - "What's my decision deadline?" - Quick reminder

---

*Decision ID: {{DECISION_ID}} | Framework v1.0*
