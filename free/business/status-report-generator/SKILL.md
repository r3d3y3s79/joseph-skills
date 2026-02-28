---
name: status-report-generator
description: Use when creating project status reports, weekly updates, or progress summaries for stakeholders. Helps structure clear, actionable reports that communicate status, blockers, and next steps without wasting readers' time.
---

# Status Report Generator

## Overview

Create status reports that people actually read and act on. This skill helps you structure updates that clearly communicate progress, surface blockers early, and keep stakeholders informed without burying them in details.

## When to Use

- Sending weekly project updates
- Reporting to executives or leadership
- Updating clients on project progress
- Summarizing sprint or iteration status
- Preparing board or investor updates
- Creating team standup summaries

## Output Structure

```
STATUS REPORT

Project: [Project Name]
Reporting Period: [Date Range]
Report Date: [Date]
Author: [Name/Role]
Distribution: [Who receives this]

---

OVERALL STATUS: [GREEN/YELLOW/RED]
[One sentence explaining the rating]

---

EXECUTIVE SUMMARY:
[2-3 sentences: What happened, what's the headline, what action is needed?]

---

KEY METRICS:
| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| [Metric 1] | [X] | [Y] | [Up/Down/Flat] |
| [Metric 2] | [X] | [Y] | [Up/Down/Flat] |

---

ACCOMPLISHMENTS (This Period):
- [x] [Completed item with impact/outcome]
- [x] [Completed item with impact/outcome]
- [x] [Completed item with impact/outcome]

---

IN PROGRESS:
| Task | Owner | % Complete | Due Date | Status |
|------|-------|------------|----------|--------|
| [Task 1] | [Name] | [X%] | [Date] | On Track |
| [Task 2] | [Name] | [X%] | [Date] | At Risk |

---

BLOCKERS & RISKS:
| Issue | Impact | Owner | Mitigation | Escalation Needed? |
|-------|--------|-------|------------|-------------------|
| [Blocker 1] | [H/M/L] | [Name] | [Action] | [Yes/No] |

---

UPCOMING (Next Period):
- [ ] [Planned item with owner and date]
- [ ] [Planned item with owner and date]
- [ ] [Planned item with owner and date]

---

DECISIONS NEEDED:
1. [Decision required + deadline + from whom]

---

APPENDIX (Optional):
- Detailed metrics
- Meeting notes
- Supporting documents
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Length | 1 page for weekly, 2-3 for monthly |
| Status colors | Green/Yellow/Red only (no orange) |
| Accomplishments | Start with verb, include outcome |
| Blockers | Include mitigation, not just complaint |
| Metrics | 3-5 key metrics, not 20 |
| Frequency | Consistent timing (same day each week) |
| Audience | Write for the most senior reader |

## Status Report Types

### Weekly Team Update
- Quick summary
- Accomplishments this week
- Focus for next week
- Blockers
- Audience: Team and direct manager

### Executive Status Report
- Start with overall status
- Business metrics focus
- Decisions needed
- Skip tactical details
- Audience: Leadership team

### Client Project Update
- Professional tone
- Progress against milestones
- Next deliverables
- Any client actions needed
- Audience: Client stakeholders

### Sprint/Iteration Report
- Sprint goals vs. actual
- Velocity/story points
- Burndown or key metrics
- Retrospective highlights
- Audience: Product and engineering

### Board/Investor Update
- Financial and growth metrics
- Key wins and challenges
- Strategic initiatives progress
- Ask/decisions if applicable
- Audience: Board members, investors

## Traffic Light Status Definitions

### GREEN (On Track)
- Project on schedule and budget
- No significant risks
- Metrics meeting or exceeding targets
- No decisions needed urgently

### YELLOW (At Risk)
- Schedule slipping or budget concerns
- Risks identified that need attention
- Metrics below target but recoverable
- Decisions needed within 2 weeks

### RED (Critical)
- Schedule or budget significantly impacted
- Major risks or blockers unresolved
- Metrics significantly below target
- Urgent decisions or escalation needed

## Writing Principles

### Lead with Status
Put the overall status first. Let readers know immediately if they need to worry.

### Accomplishments Show Outcomes
**Weak**: "Worked on website redesign"
**Strong**: "Launched website redesign—page load time improved 40%"

### Blockers Include Solutions
**Weak**: "Waiting on legal review"
**Strong**: "Waiting on legal review—escalated to General Counsel, expecting response by Friday"

### Be Specific About Time
**Vague**: "Project is behind schedule"
**Specific**: "Project is 2 weeks behind schedule; revised launch date is April 30"

### One Report, Multiple Audiences
Write so executives can scan the top section and skip details, while team members can dive deep into appendix if needed.

## Common Mistakes

- **Status lies**: Showing green when it's clearly yellow
- **No executive summary**: Forcing readers to hunt for the point
- **Blockers without mitigation**: Problems without proposed solutions
- **Too many metrics**: Tracking 20 things when 5 matter
- **Missing decisions**: Burying the ask instead of making it explicit
- **Inconsistent format**: Different structure each week
- **No outcomes**: Listing activities instead of results

## Examples

### Example 1: Weekly Project Status Report

**Input**: Write a weekly status report for a website redesign project that's slightly behind schedule

**Output**:
```
STATUS REPORT

Project: Corporate Website Redesign
Reporting Period: February 24 - March 1, 2026
Report Date: March 1, 2026
Author: Sarah Chen, Project Manager
Distribution: Steering Committee, Marketing Leadership

---

OVERALL STATUS: YELLOW
Design phase completed 1 week late; implementing recovery plan to meet original launch date.

---

EXECUTIVE SUMMARY:
Design phase closed this week with client approval on all page templates. The 1-week delay was due to additional stakeholder feedback rounds. We've added weekend development capacity to recover the schedule—launch date of April 15 remains achievable but has no buffer.

---

KEY METRICS:
| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| Schedule | On time | 1 week behind | Recovering |
| Budget | $150K | $142K spent | On track |
| Scope | 25 pages | 25 pages | On track |
| Client NPS | 8+ | 9 | Up |

---

ACCOMPLISHMENTS (This Week):
- [x] Completed final design approval for all 25 page templates
- [x] Began development sprint 1—homepage and navigation components complete
- [x] Migrated content for 8/25 pages to staging environment
- [x] Secured additional dev resources (2 contractors) for March

---

IN PROGRESS:
| Task | Owner | % Complete | Due Date | Status |
|------|-------|------------|----------|--------|
| Development Sprint 1 | Dev Lead | 40% | March 8 | On Track |
| Content Migration | Content Team | 32% | March 22 | On Track |
| SEO Implementation | SEO Specialist | 15% | March 29 | On Track |
| QA Test Plan | QA Lead | 75% | March 4 | On Track |

---

BLOCKERS & RISKS:
| Issue | Impact | Owner | Mitigation | Escalation Needed? |
|-------|--------|-------|------------|-------------------|
| 1-week schedule slip | Medium | PM | Added 2 weekend dev days; reduced buffer to zero | No |
| Photography not delivered | High | Marketing | Placeholder images ready; final assets due March 10 | Yes—need Marketing VP to follow up with vendor |
| Legal review of new privacy page | Medium | Legal | Meeting scheduled March 3; built buffer into plan | No |

---

UPCOMING (Next Week):
- [ ] Complete Development Sprint 1 (Dev Lead, March 8)
- [ ] Finalize QA test plan and begin testing (QA Lead, March 5)
- [ ] Client review of staging site—first 8 pages (PM, March 7)
- [ ] Receive final photography assets (Marketing, March 10)

---

DECISIONS NEEDED:
1. **Photography contingency**: If vendor misses March 10 deadline, do we launch with stock photos or delay 1 week? Decision needed by March 8 from Marketing VP.

---

APPENDIX:
- Sprint 1 detailed task list: [Link]
- Content migration tracker: [Link]
- Budget detail: [Link]
```

### Example 2: Executive Monthly Update

**Input**: Write a monthly executive status report for an enterprise software implementation program

**Output**:
```
STATUS REPORT

Project: Enterprise ERP Implementation Program
Reporting Period: February 2026
Report Date: March 3, 2026
Author: Program Director
Distribution: Executive Steering Committee

---

OVERALL STATUS: GREEN
All workstreams on track. Phase 2 (Finance Module) go-live successful February 15. On schedule for Phase 3 kickoff.

---

EXECUTIVE SUMMARY:
February marked a major milestone with the successful go-live of the Finance Module. 850 users transitioned with 98% adoption in week one and zero critical incidents. We're now 2 of 4 phases complete, $2.1M of $5.2M budget spent (40%), and on track for full program completion by September 2026.

---

PROGRAM DASHBOARD:

| Phase | Status | Go-Live | Progress |
|-------|--------|---------|----------|
| Phase 1: HR/Payroll | Complete | Nov 2025 | 100% |
| Phase 2: Finance | Complete | Feb 2026 | 100% |
| Phase 3: Supply Chain | In Progress | May 2026 | 25% |
| Phase 4: Manufacturing | Not Started | Sep 2026 | 0% |

**Overall Progress: 56% complete**

---

KEY METRICS:
| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| Schedule | On time | On time | Stable |
| Budget | $5.2M | $2.1M spent (40%) | On track |
| User Adoption (Phase 2) | 90% by Day 30 | 98% by Day 15 | Ahead |
| Critical Defects (Phase 2) | <5 | 0 | Better than target |
| Training Completion | 95% | 97% | On track |
| Business Sponsor Satisfaction | 8/10 | 8.5/10 | Stable |

---

ACCOMPLISHMENTS (February):
- [x] Finance Module go-live completed on schedule (Feb 15)—first AP run processed $4.2M without errors
- [x] Achieved 98% user adoption vs. 90% target by week two
- [x] Closed 147 Phase 2 testing defects before go-live (zero P1/P2 open)
- [x] Supply Chain design workshops completed with all regional stakeholders
- [x] Vendor contract amendment signed for Phase 3 resources

---

UPCOMING (March):
- [ ] Phase 3 Supply Chain development sprint 1 begins (March 4)
- [ ] Phase 2 30-day stability review and handoff to support (March 15)
- [ ] Phase 4 Manufacturing requirements gathering kickoff (March 18)
- [ ] Quarterly Steering Committee presentation (March 25)

---

RISKS & ISSUES:
| Item | Type | Impact | Status | Owner | Action |
|------|------|--------|--------|-------|--------|
| Supply Chain data quality | Risk | High | Mitigating | Data Lead | Data cleansing project added; on track |
| Key resource leaving | Issue | Medium | Resolved | HR | Replacement hired, starts March 10 |
| Vendor support response times | Risk | Low | Monitoring | PM | Escalation path documented |

---

BUDGET SUMMARY:
| Category | Budget | Spent | Remaining | Forecast |
|----------|--------|-------|-----------|----------|
| Software & Licenses | $1.8M | $1.8M | $0 | On budget |
| Implementation Partner | $2.4M | $1.6M | $0.8M | On budget |
| Internal Labor | $0.6M | $0.4M | $0.2M | On budget |
| Contingency | $0.4M | $0.1M | $0.3M | Under budget |
| **Total** | **$5.2M** | **$2.1M** | **$3.1M** | **On budget** |

---

PHASE 2 OUTCOMES:
- 850 finance users transitioned from legacy system
- Month-end close reduced from 12 days to 6 days
- Real-time financial reporting now available (previously 2-week lag)
- $145K annual savings from retired legacy licenses

---

DECISIONS NEEDED:
None at this time. Next decision point: Phase 3 go/no-go (April Steering Committee).

---

NEXT REPORT: April 2, 2026
```

### Example 3: Client Project Update

**Input**: Write a bi-weekly client status report for a marketing campaign project

**Output**:
```
STATUS REPORT

Project: Q2 Product Launch Campaign
Client: Apex Technologies
Reporting Period: February 17 - March 1, 2026
Report Date: March 2, 2026
Prepared by: Jordan Miller, Account Director
For: Marketing Director, VP of Marketing

---

OVERALL STATUS: GREEN
Campaign development on track for March 15 soft launch. Creative approved, media plan finalized.

---

EXECUTIVE SUMMARY:
Your Q2 Product Launch Campaign is progressing on schedule. This period we finalized creative concepts (your team approved the "Innovation Unleashed" direction), locked the media plan across digital and trade channels, and began production on video assets. We're on track for soft launch March 15 and full launch April 1.

---

KEY MILESTONES:
| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Creative concept approval | Feb 21 | Complete |
| Media plan finalization | Feb 28 | Complete |
| Video production complete | March 10 | In Progress (on track) |
| Landing pages live | March 12 | In Progress (on track) |
| Soft launch (email + social) | March 15 | On Track |
| Full launch (paid media) | April 1 | On Track |

---

ACCOMPLISHMENTS (Past 2 Weeks):
- [x] **Creative approved**: "Innovation Unleashed" campaign concept approved by your leadership team
- [x] **Media plan locked**: $85K budget allocated across LinkedIn ($40K), Google ($25K), trade publications ($15K), and email ($5K)
- [x] **Video production started**: On-location shoot completed Feb 27; post-production underway
- [x] **Messaging finalized**: Core messaging matrix and taglines approved
- [x] **Landing page wireframes approved**: Development begins March 3

---

IN PROGRESS:
| Deliverable | Status | Due | Notes |
|-------------|--------|-----|-------|
| 60-second hero video | Editing | March 10 | First cut ready March 5 for your review |
| 3 x 15-second social videos | Editing | March 10 | Same timeline as hero video |
| Landing page development | Starting | March 12 | Development begins March 3 |
| Email sequences (3 emails) | Drafting | March 10 | First drafts for review March 6 |
| LinkedIn ad creative (6 variants) | Design | March 8 | Static and animated versions |

---

ITEMS REQUIRING YOUR ACTION:
| Item | Action Needed | From | Deadline |
|------|---------------|------|----------|
| Video first cut review | Approve or provide feedback | Marketing Director | March 6 |
| Email sequence copy review | Approve or provide revisions | Product Marketing | March 8 |
| Customer quote approvals | Get sign-off from 2 featured customers | PR Team | March 10 |

---

BUDGET SUMMARY:
| Category | Budget | Committed | Spent | Remaining |
|----------|--------|-----------|-------|-----------|
| Creative & Production | $45,000 | $42,000 | $28,000 | $3,000 |
| Media Spend | $85,000 | $85,000 | $0 | $85,000 |
| Agency Fees | $25,000 | $25,000 | $12,500 | $12,500 |
| **Total** | **$155,000** | **$152,000** | **$40,500** | **$100,500** |

*Note: Media spend will be invoiced monthly starting April 1*

---

RISKS & MITIGATION:
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Customer quote approvals delayed | Medium | Low | Have backup customer quotes ready; can launch without if needed |
| Video revisions push timeline | Low | Medium | Built 2-day buffer into schedule; prioritize quick review turnaround |

---

UPCOMING (Next 2 Weeks):
- [ ] Video first cut delivery for review (March 5)
- [ ] Email copy delivery for review (March 6)
- [ ] Landing page development complete (March 12)
- [ ] All assets finalized (March 13)
- [ ] Soft launch: Email blast + organic social (March 15)

---

NEXT CHECK-IN:
- Status call: Thursday, March 6 at 2 PM EST
- Next written report: March 16, 2026

Questions? Contact Jordan Miller: jordan@agency.com | (555) 123-4567
```

## Report Templates by Frequency

### Daily Standup (3 items)
```
Yesterday: [What was completed]
Today: [What's planned]
Blockers: [What's in the way]
```

### Weekly Report (1 page)
```
Status: [Green/Yellow/Red]
Summary: [2-3 sentences]
Accomplishments: [3-5 items]
Next week: [3-5 items]
Blockers: [If any]
```

### Monthly Report (2-3 pages)
```
Executive summary
Key metrics dashboard
Accomplishments with outcomes
Risks and issues
Budget summary
Upcoming milestones
Decisions needed
```

### Quarterly Business Review (5-10 pages)
```
Executive summary
Quarterly highlights
Goals vs. actuals
Financial summary
Lessons learned
Next quarter plan
Strategic recommendations
```

## Quality Checklist

- [ ] Overall status (Green/Yellow/Red) appears first
- [ ] Executive summary captures the headline in 2-3 sentences
- [ ] Accomplishments show outcomes, not just activities
- [ ] Key metrics include target vs. actual
- [ ] Blockers include mitigation actions
- [ ] Decisions needed have clear deadlines
- [ ] Consistent format with previous reports
- [ ] Appropriate length for audience (shorter for executives)
- [ ] All dates and owners specified
- [ ] Honest assessment (status matches reality)
