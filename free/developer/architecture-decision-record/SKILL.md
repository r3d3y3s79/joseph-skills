---
name: architecture-decision-record
description: Use when documenting architectural decisions, technology choices, or significant design decisions. Helps create structured ADRs with context, alternatives, and consequences.
---

# Architecture Decision Record

## Overview

Create Architecture Decision Records (ADRs) that capture the "why" behind technical decisions. This skill helps you document context, alternatives considered, and consequences so future developers understand the reasoning when revisiting decisions.

## When to Use

- Choosing between technologies or frameworks
- Making significant architectural changes
- Establishing coding standards or patterns
- Deciding on infrastructure approaches
- Documenting trade-offs for future reference

## Output Structure

```
ADR DOCUMENT:

# ADR-[NUMBER]: [Title]

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-XXX
**Deciders:** [Names/roles involved]

## Context

[What is the situation that requires a decision? Include technical and business context.]

## Decision Drivers

- [Driver 1: requirement or constraint]
- [Driver 2: requirement or constraint]
- [Driver 3: requirement or constraint]

## Considered Options

1. [Option 1]
2. [Option 2]
3. [Option 3]

## Decision Outcome

**Chosen option:** "[Option X]" because [justification].

### Consequences

**Good:**
- [Positive outcome]
- [Positive outcome]

**Bad:**
- [Negative outcome/trade-off]
- [Negative outcome/trade-off]

**Neutral:**
- [Side effect]

## Pros and Cons of Options

### [Option 1]

[Description]

- Good: [advantage]
- Good: [advantage]
- Bad: [disadvantage]
- Bad: [disadvantage]

### [Option 2]

[Description]

- Good: [advantage]
- Bad: [disadvantage]

### [Option 3]

[Description]

- Good: [advantage]
- Bad: [disadvantage]

## Links

- [Related ADRs]
- [Documentation]
- [External resources]
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Title | Start with verb or noun, be specific |
| Status | Proposed → Accepted → (Deprecated/Superseded) |
| Context | Business AND technical background |
| Options | At least 2-3 real alternatives |
| Decision | Clear statement with justification |
| Consequences | Include negatives, not just positives |
| Links | Reference related decisions |

## ADR Patterns

### Technology Selection

Focus on:
- Evaluation criteria
- Team expertise
- Long-term support
- Integration requirements

### Architecture Change

Focus on:
- Current problems
- Proposed solution
- Migration path
- Risk assessment

### Process/Standard

Focus on:
- Current inconsistencies
- Proposed standard
- Enforcement mechanism
- Exceptions

## Common Mistakes

- **Missing context**: Future readers don't know why decision was needed
- **No alternatives**: Looks like rubber-stamping, not evaluation
- **Only positives**: Every decision has trade-offs
- **Too vague**: "Better performance" - how much? measured how?
- **No status tracking**: Decisions become outdated
- **Missing deciders**: Accountability unclear

## Examples

### Example 1: Database Selection ADR

**Input**: Write an ADR for choosing PostgreSQL over MongoDB for a new e-commerce application

**Output**:
```markdown
# ADR-001: Use PostgreSQL as Primary Database

**Date:** 2024-03-15
**Status:** Accepted
**Deciders:** Engineering Team, CTO, Lead Architect

## Context

We are building a new e-commerce platform that needs to handle:
- Product catalog with complex attributes
- Order processing with transactions
- Inventory management with consistency requirements
- Reporting and analytics queries
- Expected scale: 100K products, 10K orders/day initially

We need to choose a primary database that will serve as the source of truth for all transactional data. The team has experience with both SQL (PostgreSQL, MySQL) and NoSQL (MongoDB) databases.

## Decision Drivers

- **Data consistency**: Orders and inventory require ACID transactions
- **Query flexibility**: Complex reporting needs (joins, aggregations)
- **Schema evolution**: Product attributes change frequently
- **Team expertise**: 3 engineers familiar with PostgreSQL, 2 with MongoDB
- **Operational cost**: Managed database services preferred
- **Performance**: Sub-100ms response for product queries

## Considered Options

1. PostgreSQL
2. MongoDB
3. MySQL
4. CockroachDB (distributed PostgreSQL)

## Decision Outcome

**Chosen option:** "PostgreSQL" because it provides strong ACID compliance for our transactional requirements, excellent JSON support for flexible product attributes, and the team has existing expertise.

### Consequences

**Good:**
- Strong transaction support for order processing
- JSONB columns handle variable product attributes without schema changes
- Excellent tooling (pgAdmin, monitoring, backups)
- Rich ecosystem of extensions (PostGIS for future geo features)
- AWS RDS and Google Cloud SQL offer managed options

**Bad:**
- Vertical scaling limits (may need read replicas at scale)
- More complex sharding if we outgrow single-node (unlikely in 2-3 years)
- Less natural fit for document-heavy features (product reviews)

**Neutral:**
- Team will need to learn PostgreSQL-specific JSON operators
- Will use separate search engine (Elasticsearch) for product search

## Pros and Cons of Options

### PostgreSQL

PostgreSQL is an open-source relational database with strong SQL compliance and excellent extensibility.

- Good: ACID transactions guarantee order consistency
- Good: JSONB provides document flexibility within relational model
- Good: Mature, battle-tested (Instagram, Spotify scale)
- Good: 3 team members have production PostgreSQL experience
- Good: Rich indexing options (B-tree, GIN for JSON, full-text)
- Bad: Single-node scaling limit (~10TB practical)
- Bad: Complex sharding solutions (Citus) add operational overhead

### MongoDB

MongoDB is a document database designed for flexible schemas and horizontal scaling.

- Good: Natural fit for product catalog's variable attributes
- Good: Built-in horizontal sharding
- Good: Flexible schema evolution
- Bad: Transactions only recently added (4.0+), less mature
- Bad: Weaker consistency guarantees in distributed mode
- Bad: Less powerful aggregation for financial reporting
- Bad: Team has less production experience (2 members, smaller projects)

### MySQL

MySQL is a widely-used open-source relational database.

- Good: Team familiarity
- Good: Simple, reliable for basic use cases
- Bad: JSON support less powerful than PostgreSQL
- Bad: Fewer advanced features (no partial indexes, weaker JSON indexing)
- Bad: Licensing concerns with Oracle ownership

### CockroachDB

CockroachDB is a distributed SQL database with PostgreSQL compatibility.

- Good: Horizontal scaling built-in
- Good: PostgreSQL wire protocol (familiar tooling)
- Good: Strong consistency across regions
- Bad: Higher operational complexity
- Bad: Higher cost at our current scale
- Bad: Less mature ecosystem
- Bad: Overkill for initial scale (< 1M rows)

## Validation

We will revisit this decision if:
- Order volume exceeds 100K/day (need read replicas)
- Product catalog exceeds 10M items (need search optimization)
- Multi-region deployment required (consider CockroachDB)

## Links

- [ADR-002: Elasticsearch for Product Search](./ADR-002.md)
- [PostgreSQL JSONB Documentation](https://www.postgresql.org/docs/current/datatype-json.html)
- [E-commerce Data Model Reference](../docs/data-model.md)
```

### Example 2: Architecture Pattern ADR

**Input**: Write an ADR for adopting a microservices architecture versus staying with a monolith

**Output**:
```markdown
# ADR-007: Adopt Modular Monolith Before Microservices

**Date:** 2024-03-15
**Status:** Accepted
**Deciders:** Engineering Team, VP Engineering, CTO

## Context

Our monolithic application has grown to 500K lines of code with 15 developers. We're experiencing:
- Slow CI/CD (45-minute builds)
- Difficulty isolating failures
- Team stepping on each other's code
- Long deployment windows (weekly)

Leadership has proposed moving to microservices. Before committing, we evaluated the options and our current capabilities.

## Decision Drivers

- **Deployment frequency**: Need to deploy multiple times per day
- **Team autonomy**: 4 teams want to work independently
- **Fault isolation**: Single bugs shouldn't take down entire system
- **Operational readiness**: Current DevOps capabilities and tooling
- **Timeline**: Need improvements within 6 months

## Considered Options

1. Full microservices extraction (8-12 services)
2. Modular monolith with clear boundaries
3. Hybrid: Extract 2-3 critical services, keep monolith
4. Status quo with better practices

## Decision Outcome

**Chosen option:** "Modular monolith with clear boundaries" as an intermediate step, because it delivers most benefits without the operational complexity of distributed systems. We will extract services only when modularity proves insufficient.

### Consequences

**Good:**
- Single deployment unit reduces operational complexity
- Clear module boundaries enable independent team work
- Can still deploy together, reducing integration risk
- Proves our domain boundaries before committing to service extraction
- 3-month implementation vs 12+ months for microservices

**Bad:**
- Still requires coordinated deployments (mitigated by feature flags)
- Database remains shared (can create module-specific schemas)
- Doesn't solve all scaling concerns (acceptable at current scale)

**Neutral:**
- May need to revisit in 12-18 months as we grow
- Teams need to learn and enforce module boundaries

## Pros and Cons of Options

### Full Microservices Extraction

Extract 8-12 bounded contexts into independent services with separate deployments.

- Good: Independent deployment per service
- Good: Technology flexibility per service
- Good: Clear team ownership
- Good: Fault isolation (one service down doesn't affect others)
- Bad: Requires Kubernetes or similar orchestration (we have none)
- Bad: Need service mesh, distributed tracing, API gateway
- Bad: 12+ month implementation timeline
- Bad: Team lacks distributed systems experience
- Bad: Network latency between services
- Bad: Distributed transaction complexity (saga pattern needed)

### Modular Monolith

Restructure codebase into well-defined modules with enforced boundaries while keeping single deployable.

```
monolith/
├── modules/
│   ├── orders/
│   │   ├── api/           # Public interfaces
│   │   ├── internal/      # Implementation
│   │   └── events/        # Event contracts
│   ├── inventory/
│   ├── users/
│   └── payments/
└── shared/
    └── kernel/            # Shared types, utilities
```

- Good: Achievable in 3 months
- Good: No new infrastructure required
- Good: Teams work on separate modules
- Good: Single database transaction when needed
- Good: Proves bounded contexts before extraction
- Bad: Still single deployment (mitigated by feature flags)
- Bad: Risk of boundary violations without enforcement
- Bad: Shared database can create coupling

### Hybrid Approach

Extract highest-traffic services (Orders API, Payment processing) while keeping rest as monolith.

- Good: Reduces risk vs full extraction
- Good: Addresses specific pain points
- Bad: Maintains two paradigms (monolith + services)
- Bad: Integration complexity at boundaries
- Bad: Unclear which approach to use for new features

### Status Quo with Better Practices

Improve CI/CD, add feature flags, better testing without architectural changes.

- Good: Lowest effort
- Good: No learning curve
- Bad: Doesn't address team coupling
- Bad: Doesn't address fault isolation
- Bad: Technical debt continues accumulating

## Implementation Plan

### Phase 1: Define Modules (Month 1)
- Identify bounded contexts using event storming
- Define public APIs for each module
- Create module folder structure

### Phase 2: Enforce Boundaries (Month 2)
- Add ArchUnit tests to prevent cross-module imports
- Each module exposes only its public API
- Implement module-level dependency injection

### Phase 3: Decouple Data (Month 3)
- Create module-specific database schemas
- Migrate shared tables to owning modules
- Use events for cross-module data needs

### Extraction Triggers

We will extract a module to a service when:
- Module needs independent scaling (10x traffic increase)
- Module needs different technology stack
- Team needs fully independent deployment

## Links

- [Event Storming Results](../docs/event-storming-2024-02.md)
- [Module Boundaries RFC](../rfcs/RFC-012-module-boundaries.md)
- [ADR-008: Inter-Module Communication](./ADR-008.md)
- ["Monolith First" - Martin Fowler](https://martinfowler.com/bliki/MonolithFirst.html)
```

### Example 3: Standard/Process ADR

**Input**: Write an ADR for adopting a specific code review process

**Output**:
```markdown
# ADR-015: Adopt Two-Reviewer Code Review Policy

**Date:** 2024-03-15
**Status:** Accepted
**Deciders:** Engineering Team (consensus), Engineering Manager

## Context

Our current code review process is inconsistent:
- Some PRs merged with no review
- Some PRs require 3+ reviewers, causing delays
- No clear criteria for what needs review
- Junior engineers sometimes review senior code without context
- Average PR wait time: 2.5 days

We've had 3 production incidents in the past quarter traced to code that bypassed review.

## Decision Drivers

- **Quality**: Reduce bugs reaching production
- **Velocity**: Don't slow down small, safe changes
- **Knowledge sharing**: Spread context across team
- **Mentorship**: Seniors review junior code, juniors learn from senior code
- **Accountability**: Clear standards everyone follows

## Considered Options

1. Two-reviewer minimum for all PRs
2. Tiered reviews (size/risk-based reviewer count)
3. Single reviewer with post-merge review
4. Optional review (author decides)

## Decision Outcome

**Chosen option:** "Tiered reviews (size/risk-based reviewer count)" because it balances quality with velocity, requiring more review for higher-risk changes while allowing fast iteration on small fixes.

### Review Tiers

| Tier | Criteria | Reviewers | Auto-merge |
|------|----------|-----------|------------|
| **Trivial** | Typo fixes, comment updates, config tweaks < 10 lines | 0 (self-merge) | Yes |
| **Standard** | Feature work, bug fixes, refactoring | 1 | No |
| **Critical** | Security, payments, auth, database migrations, public APIs | 2 (including senior) | No |

### Consequences

**Good:**
- Small fixes ship immediately (unblocking deploys)
- Knowledge spreads through reviews
- Critical code gets appropriate attention
- Clear expectations reduce friction

**Bad:**
- Requires discipline to correctly categorize PRs
- Potential for gaming the system (marking critical as standard)
- Need tooling to enforce tiers

**Neutral:**
- Will adjust thresholds based on incident data

## Pros and Cons of Options

### Two-Reviewer Minimum for All PRs

Every PR requires two approvals before merge.

- Good: Maximum oversight
- Good: Simple rule, easy to enforce
- Bad: Trivial changes blocked waiting for 2 reviewers
- Bad: Reviewer fatigue on small changes
- Bad: Doesn't scale with team size

### Tiered Reviews (Chosen)

Different requirements based on risk/size of change.

- Good: Matches effort to risk
- Good: Trivial changes unblocked
- Good: Critical changes get appropriate scrutiny
- Bad: Categorization requires judgment
- Bad: Edge cases may be miscategorized

### Single Reviewer with Post-Merge Review

One review before merge, second reviewer does post-merge review.

- Good: Faster initial merge
- Good: Second perspective eventually provided
- Bad: Bugs may be deployed before caught
- Bad: Post-merge reviews often skipped (low urgency)
- Bad: Difficult to enforce

### Optional Review (Author Decides)

Authors choose whether to request review.

- Good: Maximum velocity
- Good: Trusts engineer judgment
- Bad: Inconsistent quality
- Bad: No learning opportunities
- Bad: No accountability
- Bad: Led to our current incident rate

## Enforcement

### Tooling
- GitHub branch protection rules enforce approval counts
- CODEOWNERS file routes critical paths to senior reviewers
- PR template includes risk tier selection
- CI check validates tier selection matches change scope

### CODEOWNERS Example
```
# Critical paths require senior review
/src/auth/           @senior-engineers
/src/payments/       @senior-engineers @security-team
/db/migrations/      @senior-engineers @dba-team
/.github/workflows/  @platform-team
```

### Review Checklist

Reviewers must verify:
- [ ] Tests cover new functionality
- [ ] No security vulnerabilities introduced
- [ ] Error handling is appropriate
- [ ] Code is readable and maintainable
- [ ] Documentation updated if needed

### Escalation

If tier is disputed:
1. Author and reviewer discuss
2. If unresolved, escalate to tech lead
3. Default to higher tier when uncertain

## Metrics

We will track:
- PR time-to-merge by tier
- Incidents traced to inadequate review
- Reviewer load distribution

Review policy quarterly based on data.

## Links

- [PR Template with Tier Selection](../.github/PULL_REQUEST_TEMPLATE.md)
- [CODEOWNERS File](../.github/CODEOWNERS)
- [Incident Post-mortem: Auth Bypass (trigger for this ADR)](../incidents/2024-02-auth-bypass.md)
- [Google's Code Review Guidelines](https://google.github.io/eng-practices/review/)
```

## Quality Checklist

- [ ] Title clearly describes the decision
- [ ] Date and status are documented
- [ ] Deciders are named (accountability)
- [ ] Context explains why decision was needed
- [ ] At least 2-3 alternatives were considered
- [ ] Each option has pros AND cons
- [ ] Decision outcome states choice with justification
- [ ] Consequences include negative trade-offs
- [ ] Links connect to related decisions/docs
- [ ] Status is tracked (Proposed/Accepted/Deprecated)
