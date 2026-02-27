---
name: shopify-product-writer
description: Create Shopify product descriptions that convert browsers to buyers. Generates benefit-driven copy, SEO-optimized titles, meta descriptions, and variant descriptions with proper formatting for Shopify's editor.
---

# Shopify Product Writer

Write product descriptions that sell. This skill creates conversion-focused copy that highlights benefits over features, addresses buyer objections, and formats correctly for Shopify's product editor.

## When to Use

Use this skill when:
- Writing new product descriptions for Shopify stores
- Rewriting existing descriptions to improve conversion
- Creating variant descriptions (sizes, colors, materials)
- Generating product collection descriptions
- Writing SEO metadata for product pages

## Output Structure

### SEO Elements
- Product title (under 70 characters, keyword + benefit)
- Meta description (under 155 characters, includes USP and soft CTA)
- URL handle suggestion (lowercase, hyphens, keyword-rich)

### Main Description
Structured in Shopify-compatible HTML:
- Opening hook (1-2 sentences addressing pain point or desire)
- Benefit bullets (3-5 items, feature → benefit format)
- Social proof placement (review quotes, usage stats, certifications)
- Specifications section (formatted as clean list)
- Care/usage instructions (if applicable)
- Trust signals (warranty, shipping, returns)

### Variant Descriptions
For products with multiple variants:
- Size guide with measurements
- Color descriptions with real-world comparisons
- Material breakdowns with touch/feel language

### Additional Fields
- Product tags (for filtering and search)
- Collection suggestions
- Cross-sell product pairings

## Quality Checklist

Before finalizing output, verify:
- [ ] Title includes primary keyword and benefit/differentiator
- [ ] Meta description has keyword, USP, and call-to-action
- [ ] Opening line addresses buyer need (not product name)
- [ ] Benefits outnumber features 2:1 minimum
- [ ] Sensory language used (how it looks, feels, works)
- [ ] Objections addressed (sizing, quality, durability)
- [ ] Trust signals present (warranty, reviews, certifications)
- [ ] Formatting works in Shopify (proper HTML/markdown)
- [ ] No generic adjectives without proof (no "amazing", "perfect")
- [ ] Specifications include all decision-making details

## Anti-Patterns (AVOID)

- Feature dumping: Listing specs without explaining why they matter to the buyer
- Generic openers: "Introducing our new..." or "This product is..." wastes prime real estate
- Unsubstantiated claims: "Best quality" without proof damages credibility
- Missing measurements: Forcing customers to guess sizes causes returns
- Wall of text: No formatting, no bullets, no scanning equals no sales
- Keyword stuffing: "Leather wallet men leather wallet genuine leather" reads as spam
- Ignoring objections: Not addressing common concerns (durability, fit, quality) loses hesitant buyers
- Weak CTAs: No urgency or reason to buy now means "I'll think about it" forever
- Copy-paste templates: Obviously templated descriptions make products feel cheap
- Mobile unfriendly: Long paragraphs that require endless scrolling on phone screens

## Examples

### Example 1: Physical Product (Apparel)

**Input:** Write a product description for a merino wool travel jacket, $189, targets frequent flyers, machine washable, packs small, temperature regulating

**Output:**

```
PRODUCT TITLE
-----------------------------------------
Merino Wool Travel Jacket | Packable, Machine Washable

META DESCRIPTION
-----------------------------------------
Merino wool travel jacket that packs into its own pocket. Machine washable. Regulates temperature from airport to altitude. Free shipping over $150.

URL HANDLE: merino-wool-travel-jacket

---

MAIN DESCRIPTION
-----------------------------------------

<p><strong>Twelve flights. Zero wrinkles. One wash at the hotel sink.</strong></p>

<p>This jacket goes from your carry-on to the conference room without ironing. Merino wool naturally regulates temperature (no more sweating through security or freezing on the plane), and it packs down to the size of a paperback.</p>

<h3>Why Frequent Flyers Love This Jacket</h3>

<ul>
  <li><strong>Packs into its own pocket</strong> – Fits in your personal item without eating valuable space</li>
  <li><strong>Machine washable merino</strong> – No dry cleaning. Wash cold, hang dry, wear the same day</li>
  <li><strong>Temperature regulating</strong> – Comfortable from 55°F to 75°F, perfect for unpredictable planes and airports</li>
  <li><strong>Wrinkle-resistant</strong> – Unpack and wear immediately, even after a 14-hour flight</li>
  <li><strong>Hidden security pocket</strong> – Interior zip pocket fits passport and phone</li>
</ul>

<h3>What Customers Say</h3>

<blockquote>"I've taken this jacket through 8 countries and 23 flights. Still looks new." — David R., verified buyer</blockquote>

<h3>Specifications</h3>

<ul>
  <li><strong>Material:</strong> 100% Australian merino wool, 18.5 micron (softer than cashmere)</li>
  <li><strong>Weight:</strong> 14 oz (lighter than most fleece jackets)</li>
  <li><strong>Packed size:</strong> 8" x 6" x 3" (fits in jacket pocket)</li>
  <li><strong>Pockets:</strong> 2 exterior zip, 1 interior security, 1 interior open</li>
  <li><strong>Care:</strong> Machine wash cold, gentle cycle. Hang dry.</li>
  <li><strong>Origin:</strong> Designed in New Zealand. Manufactured in Portugal.</li>
</ul>

<h3>Sizing</h3>

<p>Fit is tailored but not slim. Order your usual size. If between sizes, size up for layering.</p>

<table>
  <tr>
    <th>Size</th>
    <th>Chest</th>
    <th>Shoulder</th>
    <th>Length</th>
  </tr>
  <tr>
    <td>S</td>
    <td>38-40"</td>
    <td>17"</td>
    <td>26"</td>
  </tr>
  <tr>
    <td>M</td>
    <td>40-42"</td>
    <td>18"</td>
    <td>27"</td>
  </tr>
  <tr>
    <td>L</td>
    <td>42-44"</td>
    <td>19"</td>
    <td>28"</td>
  </tr>
  <tr>
    <td>XL</td>
    <td>44-46"</td>
    <td>20"</td>
    <td>29"</td>
  </tr>
</table>

<h3>Our Guarantee</h3>

<p>✓ Free shipping on orders over $150<br>
✓ Free returns within 30 days (unworn, tags attached)<br>
✓ 2-year warranty against defects</p>

---

PRODUCT TAGS
-----------------------------------------
travel, merino wool, packable jacket, machine washable, men's jacket, temperature regulating, travel jacket

COLLECTION SUGGESTIONS
-----------------------------------------
Travel Essentials, New Arrivals, Men's Outerwear

CROSS-SELL PRODUCTS
-----------------------------------------
- Merino T-Shirt (complete the travel capsule)
- Packing Cubes (pair with packable jacket)
- Travel Dopp Kit (same travel collection)
```

### Example 2: Digital Product (Software/SaaS)

**Input:** Write a product description for a Shopify app that automates inventory sync across multiple sales channels, $29/month, targets multi-channel sellers

**Output:**

```
PRODUCT TITLE
-----------------------------------------
Multi-Channel Inventory Sync | Real-Time Stock Updates

META DESCRIPTION
-----------------------------------------
Sync inventory across Shopify, Amazon, Etsy, and eBay in real-time. Stop overselling. Automatic updates when you sell anywhere. 14-day free trial.

URL HANDLE: multi-channel-inventory-sync

---

MAIN DESCRIPTION (App Store Format)
-----------------------------------------

<p><strong>Sold the same item twice? Never again.</strong></p>

<p>Every time you sell on Amazon, your Shopify inventory updates automatically. Sell on Etsy? Updated. eBay? Updated. Your inventory stays accurate across every sales channel without spreadsheets, manual entry, or that sinking feeling when you realize you've oversold.</p>

<h3>What This App Does</h3>

<ul>
  <li><strong>Real-time sync</strong> – Inventory updates within 60 seconds of any sale, anywhere</li>
  <li><strong>Multi-warehouse support</strong> – Different inventory counts for different locations, synced separately</li>
  <li><strong>Low stock alerts</strong> – Get notified before you run out, by channel or overall</li>
  <li><strong>Sync rules</strong> – Reserve inventory for specific channels or set minimum thresholds</li>
  <li><strong>Bulk import/export</strong> – Update thousands of SKUs via CSV</li>
</ul>

<h3>Channels We Support</h3>

<p>Shopify (obviously) + Amazon (US, UK, CA, DE, AU) + eBay + Etsy + Walmart + WooCommerce + BigCommerce + Google Shopping</p>

<h3>How It Works</h3>

<ol>
  <li>Connect your channels (takes 2 minutes per channel)</li>
  <li>Map your SKUs (auto-matching for products with same SKU)</li>
  <li>Set your sync preferences (real-time or scheduled)</li>
  <li>That's it. Inventory syncs automatically from now on.</li>
</ol>

<h3>What Customers Say</h3>

<blockquote>"I was updating inventory manually every morning. This app gave me that hour back, every single day." — Jennifer M., 4,000 SKUs across 3 channels</blockquote>

<blockquote>"The one time I oversold before this app cost me a 1-star review and $50 in shipping to fix. This app pays for itself." — Marcus K., jewelry seller</blockquote>

<h3>Pricing</h3>

<ul>
  <li><strong>Starter:</strong> $29/month (3 channels, 500 SKUs)</li>
  <li><strong>Growth:</strong> $79/month (5 channels, 5,000 SKUs)</li>
  <li><strong>Enterprise:</strong> $199/month (unlimited channels, unlimited SKUs)</li>
</ul>

<p>All plans include a 14-day free trial. No credit card required to start.</p>

<h3>Setup & Support</h3>

<p>✓ 5-minute setup (seriously, we timed it)<br>
✓ Live chat support, 9am-6pm EST<br>
✓ Free migration from other inventory apps<br>
✓ Video tutorials for every feature</p>

---

PRODUCT TAGS
-----------------------------------------
inventory management, multi-channel selling, stock sync, Amazon integration, Etsy integration, eBay integration, inventory automation

---

LISTING NOTES
-----------------------------------------
This format works for Shopify App Store submissions. Adjust header levels if using as regular product page.
```

### Example 3: Handmade/Artisan Product

**Input:** Write a product description for a handmade ceramic mug, $45, made in New Zealand, holds 12oz, dishwasher safe, small batch production

**Output:**

```
PRODUCT TITLE
-----------------------------------------
Handmade Ceramic Mug | New Zealand Stoneware, 12oz

META DESCRIPTION
-----------------------------------------
Handmade ceramic mug by New Zealand potter. 12oz capacity. Dishwasher safe. Each piece is unique. Free NZ shipping.

URL HANDLE: handmade-ceramic-mug-nz

---

MAIN DESCRIPTION
-----------------------------------------

<p><strong>This isn't a mug. It's your morning ritual, made tangible.</strong></p>

<p>Hand-thrown on a potter's wheel in our Wellington studio, each mug takes shape under hands that have crafted over 3,000 pieces. The clay comes from local deposits. The glaze is our own formula, developed over eight years of experimentation.</p>

<p>No two mugs are identical. Slight variations in glaze pattern, handle placement, and rim shape mean yours is genuinely one of a kind.</p>

<h3>Details That Matter</h3>

<ul>
  <li><strong>Capacity:</strong> 12oz (350ml) – enough for a proper coffee, not a dainty sip</li>
  <li><strong>Handle:</strong> Sized for two fingers, comfortable grip even when full</li>
  <li><strong>Base:</strong> Weighted bottom prevents tipping, unglazed for stability</li>
  <li><strong>Dishwasher safe:</strong> Yes, but hand washing extends the glaze life</li>
  <li><strong>Microwave safe:</strong> Yes (as long as there's liquid inside)</li>
</ul>

<h3>The Making Process</h3>

<p>Each mug takes 3 weeks from clay to your hands:</p>

<ol>
  <li><strong>Throwing:</strong> Shaped on the wheel in our Wellington studio</li>
  <li><strong>Drying:</strong> 7 days of slow drying to prevent cracks</li>
  <li><strong>First firing:</strong> 1000°C bisque fire hardens the clay</li>
  <li><strong>Glazing:</strong> Hand-dipped in our signature glaze</li>
  <li><strong>Final firing:</strong> 1280°C vitrification creates the finished piece</li>
</ol>

<h3>Specifications</h3>

<ul>
  <li><strong>Material:</strong> High-fire stoneware clay</li>
  <li><strong>Dimensions:</strong> 4" tall, 3.5" diameter</li>
  <li><strong>Weight:</strong> 380g (substantial but not heavy)</li>
  <li><strong>Origin:</strong> Handmade in Wellington, New Zealand</li>
</ul>

<h3>Glaze Options</h3>

<p><strong>Cloud White:</strong> Soft, matte white with subtle grey undertones. Shows coffee stains if not washed promptly.<br>
<strong>Ocean Blue:</strong> Deep blue with crystalline variations. Each one patterns differently.<br>
<strong>Forest Black:</strong> Glossy black with brown breaking at edges. Hides wear well.</p>

<h3>Care Instructions</h3>

<p>Dishwasher safe, but hand washing keeps the glaze pristine longer. Avoid thermal shock (don't pour boiling water into a cold mug straight from the fridge). Store upright to protect the rim.</p>

<h3>Shipping & Packaging</h3>

<p>✓ Free shipping within New Zealand<br>
✓ International shipping: $25 (tracked)<br>
✓ Packaged in recycled cardboard with custom foam insert<br>
✓ Ships within 5-7 days (made to order)</p>

<h3>Our Promise</h3>

<p>If your mug arrives damaged, we'll replace it. If you don't love it within 14 days, return it for a full refund. We've been making pottery for 12 years – your satisfaction is how we stay in business.</p>

---

PRODUCT TAGS
-----------------------------------------
handmade, ceramic, mug, New Zealand made, stoneware, artisan, pottery, coffee mug, tea mug, gift

COLLECTION SUGGESTIONS
-----------------------------------------
Mugs & Cups, New Zealand Made, Gifts Under $50

CROSS-SELL PRODUCTS
-----------------------------------------
- Matching ceramic bowl (breakfast set)
- Pour over coffee dripper (coffee lover bundle)
- Gift box with NZ coffee beans (ready-to-gift)
```
