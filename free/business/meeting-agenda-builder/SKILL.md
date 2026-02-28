---
name: meeting-agenda-builder
description: Use when creating meeting agendas, preparing discussion points, or documenting meeting notes. Helps structure productive meetings with clear objectives, time allocations, and follow-up actions.
---

# Meeting Agenda Builder

## Overview

Create meeting agendas that make meetings worth attending. This skill helps you structure meetings with clear purpose, realistic timing, and actionable outcomes that respect everyone's time.

## When to Use

- Planning team meetings and standups
- Preparing client or stakeholder meetings
- Structuring project kickoffs
- Organizing brainstorming sessions
- Creating board or executive meetings
- Documenting meeting notes and action items

## Output Structure

```
MEETING AGENDA

Meeting Title: [Clear, specific title]
Date/Time: [Date, Start Time - End Time, Timezone]
Location: [Physical location or video link]
Organizer: [Name]

---

ATTENDEES:
Required: [Names/roles]
Optional: [Names/roles]

---

MEETING OBJECTIVE:
[One sentence: What must be accomplished by the end of this meeting?]

---

PRE-MEETING PREP:
- [ ] [Material to review before meeting]
- [ ] [Document to read]
- [ ] [Question to come prepared to answer]

---

AGENDA:

| Time | Topic | Owner | Type |
|------|-------|-------|------|
| 5 min | [Topic 1] | [Name] | [Info/Discussion/Decision] |
| 15 min | [Topic 2] | [Name] | [Info/Discussion/Decision] |
| 10 min | [Topic 3] | [Name] | [Info/Discussion/Decision] |
| 5 min | Action Items & Next Steps | [Facilitator] | Decision |

---

DISCUSSION QUESTIONS:
1. [Key question for Topic 1]
2. [Key question for Topic 2]
3. [Key question for Topic 3]

---

DESIRED OUTCOMES:
- [ ] [Decision to be made]
- [ ] [Alignment to reach]
- [ ] [Action to assign]

---

MEETING NOTES TEMPLATE:

## Decisions Made:
-

## Action Items:
| Action | Owner | Due Date |
|--------|-------|----------|
| | | |

## Key Takeaways:
-

## Parking Lot (For Later):
-
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Meeting length | 25 or 50 minutes (not 30/60) |
| Agenda items | 3-5 max for 1-hour meeting |
| Time buffers | Build in 5 min for overruns |
| Pre-read | Send 24 hours in advance |
| Objective | One sentence, measurable |
| Decision items | Flag clearly, require owners |
| Follow-up | Document within 24 hours |

## Meeting Types

### Status Update / Standup
- Keep to 15-30 minutes max
- Round-robin format
- Focus: blockers and help needed
- Agenda: What I did / What I'm doing / What's blocking me

### Decision Meeting
- Clear decision to be made
- Options presented in advance
- Time for discussion
- End with explicit decision recorded

### Brainstorm / Creative
- Longer time blocks (60-90 min)
- Warm-up exercise
- Divergent then convergent
- Document all ideas, filter later

### Project Kickoff
- Context and background
- Goals and success metrics
- Roles and responsibilities
- Timeline and milestones
- Q&A and concerns

### 1:1 Meeting
- Employee drives agenda
- Mix of tactical and strategic
- Career development time
- No status updates (use async)

### Client / External Meeting
- Extra prep on context
- Clear ownership of topics
- Parking lot for scope creep
- Explicit next steps before ending

## Time Allocation Guidelines

### For a 30-Minute Meeting
- Opening/context: 2 min
- Main topic 1: 10 min
- Main topic 2: 10 min
- Action items/wrap: 5 min
- Buffer: 3 min

### For a 60-Minute Meeting
- Opening/context: 5 min
- Topic 1: 15 min
- Topic 2: 15 min
- Topic 3: 15 min
- Action items/wrap: 5 min
- Buffer: 5 min

### For a 90-Minute Workshop
- Opening/warm-up: 10 min
- Main activity 1: 25 min
- Break: 5 min
- Main activity 2: 25 min
- Synthesis: 15 min
- Action items/wrap: 10 min

## Common Mistakes

- **No clear objective**: "Weekly sync" (sync about what?)
- **Too many topics**: Cramming 10 items into 30 minutes
- **Missing owners**: Topics without assigned drivers
- **No pre-read**: Wasting meeting time on context
- **Decision amnesia**: Decisions made but not documented
- **Runaway discussions**: No time boxes or facilitation
- **Missing "why"**: People in room don't know why they're needed

## Examples

### Example 1: Weekly Team Meeting

**Input**: Create an agenda for a 30-minute weekly marketing team meeting

**Output**:
```
MEETING AGENDA

Meeting Title: Marketing Weekly Sync
Date/Time: Monday, March 3, 2026 | 10:00-10:30 AM EST
Location: Zoom [link]
Organizer: Marketing Manager

---

ATTENDEES:
Required: Marketing Manager, Content Lead, Paid Ads Lead, Designer
Optional: Product Marketing (for launch updates)

---

MEETING OBJECTIVE:
Align on this week's priorities and surface any blockers preventing campaign delivery.

---

PRE-MEETING PREP:
- [ ] Update your row in the Campaign Tracker before meeting
- [ ] Come prepared to share one number from last week
- [ ] Flag any blockers in #marketing-blockers Slack channel

---

AGENDA:

| Time | Topic | Owner | Type |
|------|-------|-------|------|
| 3 min | Wins from last week (one per person) | All | Info |
| 10 min | Campaign updates & metrics | Each lead | Info |
| 10 min | Blockers & help needed | All | Discussion |
| 5 min | This week's priorities (quick round-robin) | All | Info |
| 2 min | Action items & wrap | Marketing Manager | Decision |

---

DISCUSSION QUESTIONS:
1. What's the one metric we should watch this week?
2. Who needs help and from whom?
3. Anything at risk for the month-end deadline?

---

DESIRED OUTCOMES:
- [ ] All blockers surfaced and assigned owners
- [ ] Week's priorities clear for everyone
- [ ] Any cross-team dependencies identified

---

MEETING NOTES TEMPLATE:

## Wins:
- Content:
- Paid:
- Design:

## This Week's Focus:
- Content:
- Paid:
- Design:

## Blockers Raised:
| Blocker | Owner to Resolve | Due |
|---------|-----------------|-----|
| | | |

## Action Items:
| Action | Owner | Due Date |
|--------|-------|----------|
| | | |
```

### Example 2: Client Project Kickoff

**Input**: Create an agenda for a 60-minute kickoff meeting with a new client for a website redesign project

**Output**:
```
MEETING AGENDA

Meeting Title: [Client Name] Website Redesign Kickoff
Date/Time: Wednesday, March 5, 2026 | 2:00-3:00 PM EST
Location: Google Meet [link]
Organizer: Project Manager

---

ATTENDEES:
Required:
- Our team: Project Manager, Lead Designer, Lead Developer
- Client: Marketing Director, Web Manager, [Executive Sponsor]
Optional:
- Client: Content Manager (for content migration discussion)

---

MEETING OBJECTIVE:
Align on project goals, timeline, and working process so both teams can begin discovery phase next week.

---

PRE-MEETING PREP:
- [ ] Client: Complete Brand Questionnaire (sent via email)
- [ ] Client: Gather login credentials for current site
- [ ] Our team: Review client's current website and competitors
- [ ] All: Review project scope document (attached)

---

AGENDA:

| Time | Topic | Owner | Type |
|------|-------|-------|------|
| 5 min | Introductions & roles | Project Manager | Info |
| 10 min | Project goals & success metrics | Marketing Director | Discussion |
| 10 min | Current pain points & wishlist | Web Manager | Discussion |
| 10 min | Our approach & methodology | Lead Designer | Info |
| 10 min | Timeline & milestone review | Project Manager | Discussion |
| 10 min | Communication & working process | Project Manager | Decision |
| 5 min | Q&A and next steps | All | Discussion |

---

DISCUSSION QUESTIONS:
1. What does success look like 6 months after launch?
2. What's the one thing the current site fails to do?
3. Are there any hard deadlines we need to work around?
4. Who has final approval authority on design decisions?

---

DESIRED OUTCOMES:
- [ ] Confirm project goals and success metrics
- [ ] Agree on communication cadence (weekly calls, Slack, etc.)
- [ ] Identify key stakeholders and decision-makers
- [ ] Confirm discovery phase start date
- [ ] Schedule first design review meeting

---

MEETING NOTES TEMPLATE:

## Project Goals (Confirmed):
1. Primary:
2. Secondary:
3. Success metric:

## Key Pain Points:
-
-
-

## Stakeholder Map:
| Role | Name | Responsibility |
|------|------|----------------|
| Decision Maker | | Final approvals |
| Day-to-Day Contact | | Working sessions |
| Technical Contact | | Development questions |

## Timeline Confirmed:
- Discovery: [dates]
- Design: [dates]
- Development: [dates]
- Launch target: [date]

## Communication Agreed:
- Weekly calls: [Day/Time]
- Async channel: [Tool]
- Document sharing: [Tool]

## Action Items:
| Action | Owner | Due Date |
|--------|-------|----------|
| Send discovery questionnaire | PM | 3/6 |
| Provide site credentials | Client | 3/6 |
| Schedule stakeholder interviews | PM | 3/7 |

## Parking Lot:
-
```

### Example 3: Decision Meeting

**Input**: Create an agenda for a 45-minute meeting to decide on a new project management tool

**Output**:
```
MEETING AGENDA

Meeting Title: Project Management Tool Decision
Date/Time: Thursday, March 6, 2026 | 3:00-3:45 PM EST
Location: Conference Room B / Zoom [link]
Organizer: Operations Director

---

ATTENDEES:
Required: Operations Director, Engineering Lead, Design Lead, Product Manager, Finance Manager
Optional: IT Security (for compliance questions)

---

MEETING OBJECTIVE:
Select one project management tool for company-wide implementation, with decision finalized by end of meeting.

---

PRE-MEETING PREP:
- [ ] Review tool comparison matrix (attached)
- [ ] Complete your scoring sheet for each tool (linked form)
- [ ] Come prepared to share your top choice with one reason
- [ ] Review budget: $15/user/month max, 50 users

---

AGENDA:

| Time | Topic | Owner | Type |
|------|-------|-------|------|
| 3 min | Meeting purpose & decision criteria recap | Ops Director | Info |
| 10 min | Summary of trial feedback (3 tools) | Ops Director | Info |
| 5 min | Quick poll: Current preference | All | Info |
| 15 min | Discussion: Pros/cons and concerns | All | Discussion |
| 7 min | Stakeholder input (non-negotiables) | Each lead | Discussion |
| 5 min | Final vote and decision | All | Decision |

---

DECISION CRITERIA (PRE-DEFINED):
| Criteria | Weight | Notes |
|----------|--------|-------|
| Ease of use | 25% | Adoption depends on this |
| Integrations (Slack, GitHub) | 20% | Must have |
| Reporting/dashboards | 20% | Leadership visibility |
| Cost | 20% | $15/user max |
| Security/compliance | 15% | SOC2 required |

---

OPTIONS UNDER CONSIDERATION:
1. **Tool A (Asana)** - Score: 82/100
   - Pros: Best UI, strong integrations
   - Cons: Higher cost at scale

2. **Tool B (Monday.com)** - Score: 78/100
   - Pros: Most flexible, good dashboards
   - Cons: Learning curve, clutter risk

3. **Tool C (Linear)** - Score: 75/100
   - Pros: Cleanest design, engineering-friendly
   - Cons: Limited non-dev features

---

DISCUSSION QUESTIONS:
1. Which tool did your team prefer during the trial?
2. What's your non-negotiable requirement?
3. Any concerns not captured in the comparison matrix?
4. Can we live with the limitations of [top option]?

---

DESIRED OUTCOMES:
- [ ] One tool selected (majority vote, Ops Director breaks ties)
- [ ] Implementation timeline agreed
- [ ] Budget approval confirmed
- [ ] Migration owner assigned

---

DECISION FRAMEWORK:
If no consensus: Ops Director makes final call based on:
1. Team feedback weight
2. Alignment with criteria
3. Long-term scalability

---

MEETING NOTES TEMPLATE:

## Pre-Meeting Scores Summary:
| Tool | Engineering | Design | Product | Finance | Average |
|------|-------------|--------|---------|---------|---------|
| Asana | | | | | |
| Monday | | | | | |
| Linear | | | | | |

## Discussion Notes:
Key concerns raised:
-
-
-

## Non-Negotiables by Team:
- Engineering:
- Design:
- Product:
- Finance:

## DECISION:
**Selected tool:** [                    ]
**Vote count:** [X for, Y against, Z abstain]
**Decision maker:** [Name if not consensus]

## Implementation Plan:
- Pilot team:
- Pilot dates:
- Full rollout:
- Migration lead:

## Action Items:
| Action | Owner | Due Date |
|--------|-------|----------|
| Sign contract | | |
| Notify IT for provisioning | | |
| Create migration plan | | |
| Schedule training | | |
```

## Agenda Templates by Meeting Length

### 15-Minute Quick Sync
```
- Context (1 min)
- Topic 1 (5 min)
- Topic 2 (5 min)
- Next steps (2 min)
- Buffer (2 min)
```

### 25-Minute Standard Meeting
```
- Opening (2 min)
- Topic 1 (8 min)
- Topic 2 (8 min)
- Actions (4 min)
- Buffer (3 min)
```

### 50-Minute Working Session
```
- Opening (3 min)
- Topic 1 (12 min)
- Topic 2 (12 min)
- Topic 3 (12 min)
- Actions (6 min)
- Buffer (5 min)
```

## Quality Checklist

- [ ] Meeting has one clear, measurable objective
- [ ] All topics have time allocations (totaling less than meeting length)
- [ ] Each topic has an assigned owner
- [ ] Topics marked as Info / Discussion / Decision
- [ ] Pre-meeting prep sent 24+ hours in advance
- [ ] Required vs. optional attendees distinguished
- [ ] Discussion questions prepare participants
- [ ] Meeting notes template ready for documentation
- [ ] Action item format includes Owner + Due Date
- [ ] Buffer time built in for overruns
