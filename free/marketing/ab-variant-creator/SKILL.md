---
name: ab-variant-creator
description: Use when creating A/B test variants for headlines, copy, emails, or landing pages. Helps generate meaningfully different test variants with clear hypotheses and expected outcomes.
---

# A/B Variant Creator

## Overview

Create A/B test variants that actually teach you something. This skill helps you design tests with meaningful differences, clear hypotheses, and statistically significant potential—not just random variations.

## When to Use

- Testing headline variations
- Comparing email subject lines
- Optimizing landing page copy
- Testing different value propositions
- Comparing CTA approaches
- Validating messaging angles

## Output Structure

```
TEST OBJECTIVE: [What you're trying to learn]

HYPOTHESIS: "If we [change], then [metric] will [improve/decrease] because [reason]."

---

CONTROL (A):
[Current or baseline version]

VARIANT B:
[First test variant]
- Change type: [Headline/CTA/Value prop/Tone/Length]
- Hypothesis: [Why this might win]

VARIANT C (optional):
[Second test variant]
- Change type: [Different element or approach]
- Hypothesis: [Why this might win]

---

TEST PARAMETERS:
- Primary metric: [CTR/Conversion rate/etc.]
- Secondary metrics: [Other things to watch]
- Minimum sample size: [Calculated estimate]
- Test duration: [Recommended timeframe]
- Confidence level: [95% standard]

EXPECTED OUTCOMES:
- If A wins: [What it tells you]
- If B wins: [What it tells you]
- If C wins: [What it tells you]
- If inconclusive: [Next steps]
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Variable count | Test ONE variable per test |
| Difference level | Meaningful, not minor tweaks |
| Sample size | 1,000+ per variant minimum |
| Duration | 1-2 full business cycles |
| Hypothesis | Write before testing |
| Winner action | Implement, then iterate |

## Test Types

### Headline Tests
- Benefit vs. feature focus
- Question vs. statement
- Short vs. long
- Specific vs. general

### CTA Tests
- Action words (Get vs. Start vs. Claim)
- First person vs. second person
- With urgency vs. without
- Length variations

### Value Proposition Tests
- Lead benefit vs. lead pain point
- Emotional vs. rational appeal
- Social proof presence vs. absence
- Risk reversal vs. no mention

### Format Tests
- Long copy vs. short copy
- Bullets vs. paragraphs
- Video vs. text
- Form length variations

## Common Mistakes

- **Too small changes**: "Get Started" vs "Get Started Now" won't teach much
- **Multiple variables**: Changing headline AND CTA AND image = no learnings
- **Stopping too early**: Wait for statistical significance
- **No hypothesis**: Random testing without learning goals
- **Ignoring segments**: Overall winner may lose in key segments
- **Testing opinions**: Test strategic questions, not personal preferences

## Examples

### Example 1: Landing Page Headline Test

**Input**: Create A/B test variants for a productivity app landing page. Current headline: "The Best Task Management App"

**Output**:
```
TEST OBJECTIVE: Determine if benefit-specific headlines outperform generic claims

HYPOTHESIS: "If we replace generic superlative ('Best') with specific outcome ('Finish work 2 hours earlier'), then signup rate will increase by 15-25% because specificity builds credibility and relevance."

---

CONTROL (A):
"The Best Task Management App"

VARIANT B:
"Finish Work 2 Hours Earlier Every Day"
- Change type: Generic claim → Specific outcome
- Hypothesis: Concrete benefit is more believable and desirable than subjective "best"

VARIANT C:
"Stop Forgetting Tasks. Start Finishing Projects."
- Change type: Generic claim → Pain point + outcome
- Hypothesis: Addressing the pain directly creates emotional connection and relevance

---

TEST PARAMETERS:
- Primary metric: Free trial signup rate
- Secondary metrics: Time on page, scroll depth, bounce rate
- Minimum sample size: 2,000 visitors per variant (6,000 total)
- Test duration: 2 weeks or until significance reached
- Confidence level: 95%

EXPECTED OUTCOMES:
- If A wins: Audience values brand positioning over specifics (rare, retest)
- If B wins: Specific outcomes resonate—test more specific claims
- If C wins: Pain-point messaging works—explore problem-aware copy
- If inconclusive: Test bigger differences (format, social proof)
```

### Example 2: Email Subject Line Test

**Input**: Create A/B test variants for a SaaS onboarding email. Current subject: "Welcome to TaskFlow"

**Output**:
```
TEST OBJECTIVE: Determine if action-oriented subjects increase open rates over welcome messages

HYPOTHESIS: "If we replace passive welcome with action prompt, then open rate will increase by 20-30% because it creates curiosity and implies immediate value."

---

CONTROL (A):
"Welcome to TaskFlow"

VARIANT B:
"Your first project is waiting (start here)"
- Change type: Welcome statement → Action prompt
- Hypothesis: Implying something is ready for them creates urgency and curiosity

VARIANT C:
"TaskFlow setup: 3 steps, 5 minutes"
- Change type: Welcome statement → Specific time/effort commitment
- Hypothesis: Showing low effort reduces procrastination on opening

---

TEST PARAMETERS:
- Primary metric: Email open rate
- Secondary metrics: Click rate, time to first project creation
- Minimum sample size: 500 recipients per variant (1,500 total)
- Test duration: 1 week (or 1,500 new signups)
- Confidence level: 95%

EXPECTED OUTCOMES:
- If A wins: Brand warmth matters more than action prompts in onboarding
- If B wins: Curiosity/implied value drives opens—test more teasers
- If C wins: Effort clarity reduces friction—be specific in future emails
- If inconclusive: Subjects aren't the bottleneck—test send timing or preview text
```

### Example 3: Pricing Page CTA Test

**Input**: Create A/B test variants for a pricing page CTA. Current CTA: "Start Free Trial"

**Output**:
```
TEST OBJECTIVE: Determine if addressing objections in CTA increases trial starts

HYPOTHESIS: "If we add 'No Credit Card' to the CTA, then conversion rate will increase by 10-20% because it removes the primary signup hesitation at point of action."

---

CONTROL (A):
"Start Free Trial"

VARIANT B:
"Start Free Trial—No Card Required"
- Change type: CTA only → CTA + objection removal
- Hypothesis: Addressing credit card concern at decision point reduces friction

VARIANT C:
"Try Free for 14 Days"
- Change type: Action focus → Time-specific framing
- Hypothesis: Specific trial length sets clear expectation and feels lower risk

---

TEST PARAMETERS:
- Primary metric: Trial signup rate
- Secondary metrics: Trial to paid conversion (watch for quality)
- Minimum sample size: 1,500 pricing page visitors per variant
- Test duration: 3 weeks or until significance
- Confidence level: 95%

EXPECTED OUTCOMES:
- If A wins: Simplicity wins—avoid cluttering CTAs
- If B wins: Objection handling in CTA works—test other objections
- If C wins: Time framing matters—test different durations (7, 14, 30)
- If inconclusive: CTA isn't bottleneck—test page layout, testimonials, pricing display
```

## Quality Checklist

- [ ] Clear hypothesis written before variants
- [ ] Only ONE variable changed per test
- [ ] Variants are meaningfully different (not minor tweaks)
- [ ] Sample size calculated and realistic
- [ ] Primary metric clearly defined
- [ ] Expected learnings documented for each outcome
- [ ] Test duration accounts for business cycles
- [ ] Secondary metrics identified
- [ ] Next steps planned for each outcome
- [ ] Inconclusive scenario has follow-up plan
