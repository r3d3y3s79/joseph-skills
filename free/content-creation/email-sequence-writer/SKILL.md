---
name: email-sequence-writer
description: Use when creating email nurture sequences, sales sequences, or onboarding flows. Helps structure multi-email campaigns with proper timing, progression, and conversion triggers.
---

# Email Sequence Writer

## Overview

Create strategic email sequences that nurture leads, drive sales, and onboard customers. This skill helps you structure multi-email campaigns with proper pacing, emotional progression, and conversion triggers that turn subscribers into buyers.

## When to Use

- Building welcome/onboarding sequences
- Creating sales or launch sequences
- Designing lead nurture campaigns
- Writing cart abandonment flows
- Developing re-engagement sequences
- Setting up post-purchase follow-ups

## Output Structure

```
SEQUENCE OVERVIEW:
- Name: [Sequence name]
- Goal: [Primary conversion goal]
- Length: [Number of emails]
- Timing: [Send frequency]
- Trigger: [What starts the sequence]

---

EMAIL 1: [Email Name]
Timing: [Day/Time from trigger]
Subject Line: [Subject]
Preview Text: [90 characters]
Purpose: [What this email achieves]

[Full email body]

CTA: [Primary action]

---

EMAIL 2: [Email Name]
[Same structure...]

---

[Continue for all emails in sequence...]

---

SEQUENCE NOTES:
- Exit triggers: [When to remove from sequence]
- Branch conditions: [If/then logic]
- Key metrics to track: [Opens, clicks, conversions]
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Sequence length | 5-7 emails for sales, 3-5 for welcome |
| Email spacing | 1-2 days between emails |
| Subject lines | Mix curiosity, benefit, personal |
| First email | Sets expectations, delivers value immediately |
| Middle emails | Build desire, handle objections |
| Final emails | Create urgency, make the ask |
| CTA per email | One primary action only |
| Unsubscribe | Always include, honor requests |

## Sequence Types

### Welcome Sequence
- Email 1: Deliver promised lead magnet + set expectations
- Email 2: Your story/why you do this
- Email 3: Quick win/immediate value
- Email 4: Social proof/results
- Email 5: Soft pitch to next step

### Sales Sequence
- Email 1: Problem awareness + tease solution
- Email 2: Agitate pain + show transformation
- Email 3: Introduce offer + benefits
- Email 4: Objection handling + FAQ
- Email 5: Social proof + testimonials
- Email 6: Urgency + final pitch
- Email 7: Last chance + deadline

### Onboarding Sequence
- Email 1: Welcome + first step
- Email 2: Quick win tutorial
- Email 3: Feature highlight
- Email 4: Common mistakes to avoid
- Email 5: Success story + what's possible

## Examples

### Example 1: Welcome Sequence for Course Creator

**Input**: Create a 5-email welcome sequence for someone who downloaded my free guide on YouTube growth

**Output**:
```
SEQUENCE OVERVIEW:
- Name: YouTube Growth Welcome
- Goal: Pitch paid YouTube course
- Length: 5 emails
- Timing: Days 0, 1, 3, 5, 7
- Trigger: Free guide download

---

EMAIL 1: The Welcome
Timing: Immediately after download
Subject Line: Your YouTube guide is inside (+ what's next)
Preview Text: Here's exactly how to use this guide...
Purpose: Deliver value, set expectations

Hey [Name],

Your YouTube Growth Blueprint is ready.

[DOWNLOAD LINK]

Here's how to get the most from it:

1. Read Section 1 today (10 minutes)
2. Implement ONE strategy this week
3. Reply and tell me which one you picked

Over the next week, I'll send you bonus tips that aren't in the guide—strategies I use with my private clients.

Talk soon,
[Your Name]

P.S. Tomorrow I'll share the #1 mistake killing most YouTube channels.

CTA: Download the guide

---

EMAIL 2: The Problem
Timing: Day 1
Subject Line: The #1 mistake killing your YouTube growth
Preview Text: I made this mistake for 2 years straight...
Purpose: Build connection through shared struggle

[Name],

Want to know what held me back for 2 years?

Inconsistent posting.

Not bad content. Not wrong niche. Just posting whenever I "felt like it."

Here's what nobody tells you: The algorithm rewards consistency more than quality.

I know that sounds backwards. But a good video every week beats a great video every month.

In your guide, check out page 7—that's my exact content calendar system.

Tomorrow: How I went from 500 to 50,000 subscribers in 8 months.

[Your Name]

CTA: Re-read page 7 of the guide

---

EMAIL 3: The Transformation
Timing: Day 3
Subject Line: 500 to 50,000 subscribers (what actually worked)
Preview Text: It wasn't what I expected...
Purpose: Show what's possible, build desire

[Name],

18 months ago, I was stuck at 500 subscribers.

Posting twice a week. Optimizing thumbnails. Doing everything "right."

Still stuck.

Then I made three changes:
1. Niched down (way down)
2. Started every video with a hook, not an intro
3. Posted at the same time every single week

8 months later: 50,000 subscribers.

The first two are in your guide. The third one—consistency—is on you.

But here's what I've learned: Having a system makes consistency automatic.

I'll tell you more about my system Friday.

[Your Name]

CTA: None (pure value)

---

EMAIL 4: Social Proof
Timing: Day 5
Subject Line: "I hit 10k subscribers using your method"
Preview Text: Sarah's results after 6 months...
Purpose: Third-party validation

[Name],

Got this message last week:

"I was skeptical, but I followed your guide exactly. 6 months later, I just hit 10,000 subscribers. My channel grew more in 6 months than the previous 3 years combined." — Sarah M.

Sarah isn't special (sorry Sarah).

She just followed a proven system instead of guessing.

The strategies in your free guide work. But they work better with accountability and advanced tactics.

That's why I created YouTube Growth Academy.

Tomorrow I'll share more about it—including a special offer for guide readers.

[Your Name]

CTA: None (tease next email)

---

EMAIL 5: The Offer
Timing: Day 7
Subject Line: Ready to grow your channel faster?
Preview Text: Special offer expires in 48 hours...
Purpose: Convert to paid course

[Name],

You've had the guide for a week.

If you've implemented even one strategy, you're ahead of 90% of creators.

But here's the truth: The guide is the foundation. The real growth happens when you go deeper.

YouTube Growth Academy includes:
- 6 modules of advanced strategies (not in the free guide)
- Monthly live Q&A calls
- Private community of serious creators
- My exact thumbnail templates and scripts

For guide readers only: $100 off with code GUIDE100.

[JOIN YOUTUBE GROWTH ACADEMY →]

This code expires in 48 hours.

No pressure—the free guide is enough to get started. But if you want faster results with support, the Academy is the next step.

Either way, I'm here to help.

[Your Name]

CTA: Join the Academy

---

SEQUENCE NOTES:
- Exit triggers: Purchases course, unsubscribes
- Branch conditions: If opens email 5 but doesn't click, send reminder in 24h
- Key metrics: Email 1 open rate, Email 5 click rate, conversion rate
```

### Example 2: Cart Abandonment Sequence

**Input**: Write a 3-email cart abandonment sequence for my online store selling productivity tools

**Output**:
```
SEQUENCE OVERVIEW:
- Name: Cart Recovery
- Goal: Complete abandoned purchase
- Length: 3 emails
- Timing: 1 hour, 24 hours, 72 hours after abandonment
- Trigger: Cart abandonment (items in cart, no purchase)

---

EMAIL 1: The Reminder
Timing: 1 hour after abandonment
Subject Line: You left something behind
Preview Text: Your cart is waiting...
Purpose: Simple reminder, catch distracted buyers

Hey [Name],

Looks like you got interrupted.

Your cart is still waiting with:
[CART CONTENTS]

Total: [PRICE]

[COMPLETE YOUR ORDER →]

Questions? Just reply to this email.

— [Brand Name] Team

CTA: Complete your order

---

EMAIL 2: The Value Reminder
Timing: 24 hours after abandonment
Subject Line: Still thinking about it?
Preview Text: Here's what you're getting...
Purpose: Remind them of value, address hesitation

[Name],

Still deciding?

Here's what [PRODUCT NAME] will help you do:
- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

Plus: Free shipping on orders over $50.

Your cart:
[CART CONTENTS]

[COMPLETE YOUR ORDER →]

"This completely changed how I work. Best purchase I've made this year." — Jamie R.

Any questions? Reply and I'll personally help.

— [Your Name], Founder

CTA: Complete your order

---

EMAIL 3: The Urgency
Timing: 72 hours after abandonment
Subject Line: Last chance: 10% off your cart
Preview Text: We're holding your items, but not for long...
Purpose: Create urgency with discount

[Name],

Your cart's about to expire.

Here's the deal: Use code SAVE10 for 10% off.

Your cart:
[CART CONTENTS]

Original: [PRICE]
With code: [DISCOUNTED PRICE]

[COMPLETE YOUR ORDER →]

Code expires in 24 hours.

After that, I can't guarantee we'll have your items in stock.

— [Brand Name] Team

P.S. This is our last reminder. If these items aren't for you, no worries at all.

CTA: Complete your order with discount

---

SEQUENCE NOTES:
- Exit triggers: Completes purchase, empties cart
- Branch conditions: If opens email 3 but doesn't purchase, add to re-engagement list
- Key metrics: Recovery rate, revenue recovered, discount usage
```

### Example 3: SaaS Onboarding Sequence

**Input**: Create an onboarding sequence for new users of my project management SaaS

**Output**:
```
SEQUENCE OVERVIEW:
- Name: New User Onboarding
- Goal: Drive activation (first project created)
- Length: 5 emails
- Timing: Days 0, 1, 3, 5, 7
- Trigger: Account signup

---

EMAIL 1: Welcome + First Step
Timing: Immediately after signup
Subject Line: Welcome to [App Name] - start here
Preview Text: Your first project in 2 minutes...
Purpose: Get first action, prevent overwhelm

Welcome to [App Name], [Name]!

Let's get you set up in 2 minutes.

**Your first step:**
1. Click [LOG IN TO YOUR ACCOUNT]
2. Click "New Project"
3. Name it anything (you can change it later)

That's it. One project, and you're officially started.

[CREATE YOUR FIRST PROJECT →]

Tomorrow, I'll show you how to invite your team.

— [Founder Name]

CTA: Create first project

---

EMAIL 2: Quick Win
Timing: Day 1
Subject Line: Invite your team (30 seconds)
Preview Text: Collaboration is where the magic happens...
Purpose: Drive second activation metric

[Name],

Got your first project set up? Great.

Now let's make it powerful: invite your team.

**Here's how:**
1. Open your project
2. Click "Team" in the top right
3. Add email addresses

Pro tip: Start with just 1-2 people. You can always add more.

[INVITE YOUR TEAM →]

Teams that collaborate in [App Name] get 3x more done. Seriously—we measured it.

Tomorrow: The one feature that saves our users 5+ hours per week.

— [Founder Name]

CTA: Invite team members

---

EMAIL 3: Feature Highlight
Timing: Day 3
Subject Line: The feature that saves 5+ hours/week
Preview Text: Most new users miss this...
Purpose: Show power feature, increase stickiness

[Name],

Most new users miss our best feature: [Feature Name].

Here's what it does: [One-sentence explanation]

Instead of [manual process], you can [automated process].

**Quick setup:**
1. Go to Settings > [Feature Name]
2. Turn it on
3. Set your preferences

Takes 60 seconds. Saves hours.

[SET UP [FEATURE NAME] →]

Already using it? Reply and tell me how it's working.

— [Founder Name]

CTA: Set up feature

---

EMAIL 4: Common Mistakes
Timing: Day 5
Subject Line: 3 mistakes new users make (avoid these)
Preview Text: I've seen thousands of accounts...
Purpose: Prevent churn, show expertise

[Name],

After watching thousands of teams use [App Name], I see the same mistakes:

**Mistake 1: Too many projects**
Start with 1-3 projects max. You can always add more.

**Mistake 2: Not using [Feature]**
This one feature cuts task management time in half. [Quick link to set it up]

**Mistake 3: Going solo**
[App Name] is 10x more powerful with a team. Even adding one person changes everything.

Avoid these three, and you're ahead of 80% of new users.

Questions? I read every reply.

— [Founder Name]

CTA: None (educational)

---

EMAIL 5: Success Story + Check-In
Timing: Day 7
Subject Line: How [Company] manages 50 projects without stress
Preview Text: Their secret? Just three things...
Purpose: Show what's possible, offer help

[Name],

Quick story:

[Company Name] manages 50+ client projects in [App Name].

Before us: Spreadsheets, missed deadlines, chaos.
After: Clear visibility, on-time delivery, happy clients.

Their setup:
1. One project per client
2. Weekly review using [Feature]
3. Team notifications turned on

That's it. Simple system, consistent execution.

**How's your first week going?**

- Need help? Reply to this email
- Want a walkthrough? [Book a free 15-min call]
- Doing great? Tell me what's working

Here to help,

— [Founder Name]

CTA: Book a call or reply

---

SEQUENCE NOTES:
- Exit triggers: Becomes paying customer, churns
- Branch conditions: If no project created by Day 3, send alternate "need help?" email
- Key metrics: Project creation rate, team invite rate, Day 7 activation
```

## Quality Checklist

- [ ] Clear sequence goal defined
- [ ] Appropriate timing between emails
- [ ] Each email has ONE clear purpose
- [ ] Subject lines vary in style (curiosity, benefit, personal)
- [ ] Preview text complements subject line
- [ ] First email delivers immediate value
- [ ] Progression builds toward conversion
- [ ] Objections addressed before final pitch
- [ ] Clear CTAs in each email
- [ ] Exit triggers defined
- [ ] Unsubscribe option respected
