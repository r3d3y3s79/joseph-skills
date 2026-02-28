---
name: cross-sell-suggester
description: Use when writing cross-sell and upsell copy for e-commerce. Helps create persuasive add-on suggestions, "frequently bought together" sections, and upgrade prompts.
---

# Cross-Sell Suggester

## Overview

Write persuasive cross-sell and upsell copy that increases average order value. This skill helps you suggest complementary products and upgrades in ways that feel helpful, not pushy.

## When to Use

- Writing "Frequently Bought Together" sections
- Creating cart page add-on suggestions
- Developing post-purchase cross-sell emails
- Writing product page "You May Also Like" copy
- Suggesting upgrades or premium alternatives

## Output Structure

```
CROSS-SELL/UPSELL TYPE: [Cart Add-on/Product Page/Post-Purchase/Upgrade]

PRIMARY PRODUCT: [What customer is buying/bought]

---

SECTION HEADER:
[Headline for the cross-sell section]

---

CROSS-SELL SUGGESTIONS (3-4 products):

SUGGESTION 1:
- Product: [Name]
- Price: $XX
- Connection: [Why it complements primary product]
- Copy: [1-2 sentence persuasive description]
- Urgency: [Optional time/stock element]

SUGGESTION 2:
- Product: [Name]
- Price: $XX
- Connection: [Why it complements primary product]
- Copy: [1-2 sentence persuasive description]
- Urgency: [Optional time/stock element]

SUGGESTION 3:
- Product: [Name]
- Price: $XX
- Connection: [Why it complements primary product]
- Copy: [1-2 sentence persuasive description]
- Urgency: [Optional time/stock element]

---

ADD-ON COPY OPTIONS:

Quick add prompt: [Button/link text]
Bundle suggestion: [Discount for adding items]
Social proof: [Stats or reviews supporting the add-on]

---

UPSELL ALTERNATIVE (if applicable):
- Product: [Premium version]
- Price difference: +$XX
- Why upgrade: [Key benefit of premium option]
- Upgrade CTA: [Button text]
```

## Quick Reference

| Cross-Sell Type | Best Placement | Conversion Tip |
|-----------------|----------------|----------------|
| Complementary | Product page | "Goes great with..." |
| Essential add-on | Cart page | "Don't forget..." |
| Upgrade | Product page | "Most popular choice" |
| Post-purchase | Order confirmation email | "Complete your setup" |
| Replenishment | Post-purchase email (timed) | "Time to restock?" |

| Element | Best Practice |
|---------|--------------|
| Header | Benefit-focused, not sales-y |
| Suggestions | 3-4 items max |
| Connection | Explain WHY they go together |
| Pricing | Show clearly, small add-on feel |
| CTA | "Add" or "Quick add" (low friction) |

## Cross-Sell Strategies

### Complementary Products
Products that enhance the primary purchase:
- Camera + memory card
- Dress + matching accessories
- Skincare + applicator tools

### Essential Add-ons
Products customers often need but forget:
- Batteries for electronics
- Care products for furniture
- Protective cases for devices

### Upgrade Path
Premium versions of what they're buying:
- Standard → Pro version
- Small → Large size
- Basic → Bundle package

### Complete the Look/Set
Products that form a cohesive collection:
- Matching furniture pieces
- Coordinating outfit items
- Full skincare routine

### Replenishment
Products that need regular replacement:
- Filters for machines
- Refills for dispensers
- Consumables

## Copy Frameworks

### The "Goes Great With" Approach
"Customers who bought [X] also loved [Y] because [reason]."

### The "Complete Your Order" Approach
"Don't forget [essential item]—you'll need it for [reason]."

### The "Smart Bundle" Approach
"Add [product] and save [%] when you buy them together."

### The "Popular Pairing" Approach
"Our most popular pairing: [X] + [Y]. Rated 4.8/5 by customers who bought both."

## Common Mistakes

- **Too many suggestions**: 3-4 max, or none stand out
- **Irrelevant products**: Random suggestions kill trust
- **No connection explained**: Tell them WHY it pairs well
- **Pushy language**: "You NEED this" feels aggressive
- **Hidden prices**: Surprises in cart = abandoned carts
- **Generic "You may also like"**: Be specific about the pairing

## Examples

### Example 1: Product Page Cross-Sell (Electronics)

**Input**: Write cross-sell copy for a customer viewing a digital camera ($599)

**Output**:
```
CROSS-SELL/UPSELL TYPE: Product Page Cross-Sell

PRIMARY PRODUCT: Digital Camera ($599)

---

SECTION HEADER:
Complete Your Camera Setup

---

CROSS-SELL SUGGESTIONS:

SUGGESTION 1:
- Product: 128GB High-Speed SD Card
- Price: $34.99
- Connection: Essential storage for photos and videos
- Copy: Most cameras ship without storage. This card holds 10,000+ photos and records 4K video without stuttering. Rated 4.9/5 by our photography customers.
- Urgency: None needed (essential item)

SUGGESTION 2:
- Product: Camera Carrying Case (Water-Resistant)
- Price: $49.99
- Connection: Protection during transport
- Copy: Custom-fit padding protects your new camera from bumps and weather. Includes accessory pockets for cards, batteries, and cables. Fits this exact model.
- Urgency: None needed

SUGGESTION 3:
- Product: Extra Camera Battery (2-Pack)
- Price: $59.99
- Connection: Extended shooting time
- Copy: One battery gets you about 300 shots. Most photographers burn through that in a single session. This 2-pack triples your shooting time—essential for travel and events.
- Urgency: "Low stock—only 8 left"

SUGGESTION 4:
- Product: Basic Photography Online Course
- Price: $29.99
- Connection: Learn to use your new camera
- Copy: Get more from your camera with 2 hours of beginner-friendly video lessons. Covers settings, composition, and editing basics. Lifetime access included.
- Urgency: None needed

---

ADD-ON COPY OPTIONS:

Quick add prompt: "+ Add to Cart"
Bundle suggestion: "Add all 4 items and save $25 (15% off accessories)"
Social proof: "87% of customers who bought this camera also purchased a memory card"

---

UPSELL ALTERNATIVE:
- Product: Camera Pro Bundle (Camera + 2 Lenses + Bag)
- Price difference: +$299 ($898 total, saves $150)
- Why upgrade: Most popular choice for serious photographers. Includes wide-angle and portrait lenses that sell separately for $449.
- Upgrade CTA: "Upgrade to Pro Bundle — Save $150"
```

### Example 2: Cart Page Add-On (Skincare)

**Input**: Write cart page cross-sell copy for a customer who has a vitamin C serum ($38) in their cart

**Output**:
```
CROSS-SELL/UPSELL TYPE: Cart Add-On

PRIMARY PRODUCT: Vitamin C Brightening Serum ($38) in cart

---

SECTION HEADER:
Frequently Bought Together

---

CROSS-SELL SUGGESTIONS:

SUGGESTION 1:
- Product: SPF 50 Daily Sunscreen
- Price: $24
- Connection: Protects vitamin C results
- Copy: Vitamin C makes skin more sensitive to sun. Protect your glow with our lightweight SPF 50—won't pill under makeup, won't leave white cast. Essential pairing.
- Urgency: None needed (essential item)

SUGGESTION 2:
- Product: Gentle Foaming Cleanser
- Price: $22
- Connection: Prep step before serum
- Copy: Clean skin absorbs serum better. This pH-balanced cleanser removes impurities without stripping—the perfect first step in your vitamin C routine.
- Urgency: None needed

SUGGESTION 3:
- Product: Hyaluronic Acid Hydrating Serum
- Price: $32
- Connection: Layer for enhanced results
- Copy: The power couple of skincare: Vitamin C for brightening, hyaluronic acid for hydration. Layer them together for your best skin ever.
- Urgency: "Selling fast—34 sold today"

---

ADD-ON COPY OPTIONS:

Quick add prompt: "Quick Add — $XX"
Bundle suggestion: "Buy all 3 together and save 15%. Your total: $XX (was $XX)"
Social proof: "These 3 products are our most-purchased routine. 4.8/5 average rating from 2,000+ reviews."

---

UPSELL ALTERNATIVE:
- Product: Complete Brightening Kit (Cleanser + Serum + Sunscreen + Bag)
- Price difference: +$12 vs buying separately ($84 → $72)
- Why upgrade: Everything you need for a complete brightening routine, packaged together. Includes a free travel bag ($15 value).
- Upgrade CTA: "Get the Complete Kit — Save $27"
```

### Example 3: Post-Purchase Email Cross-Sell

**Input**: Write a post-purchase cross-sell email for someone who just bought a yoga mat ($45)

**Output**:
```
CROSS-SELL/UPSELL TYPE: Post-Purchase Email

PRIMARY PRODUCT: Yoga Mat ($45) - just purchased

---

EMAIL SUBJECT LINES:
1. Your yoga mat is on its way. Here's what pairs with it.
2. One more thing to complete your practice
3. What 500+ yogis add to their mat order

EMAIL PREVIEW TEXT:
These three add-ons make your practice even better.

---

EMAIL BODY:

Hi [First Name],

Your new yoga mat is on its way! Order #[number] ships within 24 hours.

While you wait, here are three things other customers add to their mat orders:

---

SUGGESTION 1:
**Yoga Block Set (2 Blocks)**
$24

Blocks make poses accessible—whether you're a beginner needing support or an advanced practitioner going deeper. These high-density foam blocks won't compress or slip.

[ADD TO NEXT ORDER →]

---

SUGGESTION 2:
**Cotton Yoga Strap**
$16

Can't quite reach your toes yet? A strap bridges the gap. Also great for shoulder openers and deeper stretches. 8 feet long with a metal D-ring buckle.

[ADD TO NEXT ORDER →]

---

SUGGESTION 3:
**Microfiber Mat Towel**
$28

For hot yoga or sweaty flows, this towel grips your mat and absorbs moisture. Prevents slipping when things get intense. Machine washable.

[ADD TO NEXT ORDER →]

---

BUNDLE OPTION:

**Yoga Essentials Kit**
Mat + Blocks + Strap + Towel
$99 (save $14)

Add all three items to your mat order and save. We'll ship everything together.

[GET THE COMPLETE KIT →]

---

CLOSING:

No pressure—these are just the items our yoga community loves most. Your mat is great on its own.

Questions about your order? Just reply to this email.

Namaste,
[Brand Name]

P.S. Use code PRACTICE10 for 10% off your next order. Valid for 7 days.

---

CROSS-SELL METRICS TO TRACK:
- Click-through rate by product
- Add-to-cart rate from email
- Revenue per email sent
```

## Quality Checklist

- [ ] Section header is benefit-focused, not "Buy More"
- [ ] 3-4 suggestions maximum (not overwhelming)
- [ ] Each suggestion has clear connection to primary product
- [ ] Copy explains WHY items go together
- [ ] Prices are visible and clear
- [ ] Quick add option has low friction
- [ ] Bundle discount offered (if applicable)
- [ ] Social proof supports suggestions (reviews, purchase stats)
- [ ] Upsell alternative presented as "upgrade" not "more expensive"
- [ ] Tone is helpful, not pushy
- [ ] Suggestions are genuinely relevant (not random products)
