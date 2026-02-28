---
name: sop-creator
description: Use when creating standard operating procedures, process documentation, or team workflows. Helps structure clear, actionable SOPs that anyone can follow without prior knowledge.
---

# SOP Creator

## Overview

Create standard operating procedures that people actually follow. This skill helps you document processes clearly enough that anyone can execute them correctly on the first try, without asking questions.

## When to Use

- Documenting repeatable business processes
- Creating onboarding procedures for new hires
- Standardizing team workflows
- Building operations manuals
- Delegating tasks to team members or contractors

## Output Structure

```
SOP HEADER:
Title: [Process Name]
Version: [X.X]
Last Updated: [Date]
Owner: [Role responsible for maintaining]
Applies to: [Roles/teams who use this]

---

PURPOSE:
[1-2 sentences: Why this process exists and what it achieves]

---

SCOPE:
- This SOP covers: [What's included]
- This SOP does NOT cover: [What's excluded, link to related SOPs]

---

PREREQUISITES:
- [ ] [Access/tool/knowledge required before starting]
- [ ] [Second prerequisite]
- [ ] [Third prerequisite]

---

DEFINITIONS:
| Term | Definition |
|------|------------|
| [Term 1] | [Plain language definition] |
| [Term 2] | [Plain language definition] |

---

PROCEDURE:

## Step 1: [Action Verb + Task]
**Time estimate**: [X minutes]
**Who**: [Role]

1. [Sub-step with specific details]
2. [Sub-step with specific details]
3. [Sub-step with specific details]

**Expected result**: [What should happen when done correctly]
**If something goes wrong**: [Troubleshooting guidance]

---

## Step 2: [Action Verb + Task]
[Repeat structure]

---

QUALITY CHECKLIST:
- [ ] [Verification step 1]
- [ ] [Verification step 2]
- [ ] [Verification step 3]

---

ESCALATION:
- Issue: [Common problem] → Contact: [Person/role]
- Issue: [Common problem] → Contact: [Person/role]

---

REVISION HISTORY:
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial creation | [Name] |
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Title | Action-oriented (How to X) |
| Steps | Start with verb, one action each |
| Screenshots | Include for any UI-based step |
| Time estimates | Add for each major step |
| Troubleshooting | Anticipate 2-3 common issues |
| Length | As short as possible, as long as necessary |
| Language | 8th grade reading level |
| Updates | Review quarterly minimum |

## SOP Types

### Sequential Process
- Linear steps A → B → C
- Clear start and end points
- Most common type

### Decision Tree Process
- Multiple paths based on conditions
- Use IF/THEN structures
- Flowchart recommended

### Checklist Process
- Order doesn't matter
- All items must be completed
- Good for quality checks

### Reference Process
- Not step-by-step
- Information lookup
- Policies, guidelines, standards

## Writing Principles

### One Action Per Step
**Bad**: "Log in to the system and navigate to the reports section and download the file"
**Good**:
1. Log in to [System]
2. Click "Reports" in the left sidebar
3. Click "Download" on the target report

### Specific Over General
**Bad**: "Send an email to the client"
**Good**: "Send email using the 'Order Confirmation' template in [Tool], including order number and estimated delivery date"

### Include the Why (Briefly)
"Enter the SKU in the Notes field (inventory team uses this for tracking)"

### Assume Zero Knowledge
Write for someone who has never done this before, but is reasonably intelligent.

## Common Mistakes

- **Too much assumed knowledge**: "Process the order" (how?)
- **Missing edge cases**: What if X doesn't exist? What if Y fails?
- **No screenshots**: Describing UI without visual reference
- **Outdated information**: Process changed, SOP didn't
- **Passive voice**: "The form should be completed" (by whom?)
- **Missing escalation**: No guidance when things break

## Examples

### Example 1: Customer Onboarding SOP

**Input**: Create an SOP for onboarding a new customer after they purchase our software

**Output**:
```
SOP: NEW CUSTOMER ONBOARDING

Version: 1.0
Last Updated: March 1, 2026
Owner: Customer Success Manager
Applies to: Customer Success Team

---

PURPOSE:
Ensure every new customer receives consistent onboarding within 24 hours of purchase, leading to successful product adoption and reduced churn.

---

SCOPE:
- This SOP covers: Post-purchase onboarding for standard plans ($50-500/month)
- This SOP does NOT cover: Enterprise onboarding (see SOP-015) or free trial users (see SOP-008)

---

PREREQUISITES:
- [ ] Access to HubSpot CRM
- [ ] Access to customer onboarding Notion workspace
- [ ] Calendly link for success team
- [ ] Welcome email template permissions

---

DEFINITIONS:
| Term | Definition |
|------|------------|
| Kickoff call | 30-minute initial setup and training call |
| Health score | Customer engagement metric in HubSpot (0-100) |
| TTV | Time to Value—days until customer uses core feature |

---

PROCEDURE:

## Step 1: Create Customer Record
**Time estimate**: 5 minutes
**Who**: Customer Success Rep

1. Log in to HubSpot CRM
2. Click "Contacts" → "Create Contact"
3. Enter customer details from Stripe:
   - Name
   - Email
   - Company name
   - Plan type
   - Purchase date
4. Set "Lifecycle Stage" to "Customer"
5. Set "Onboarding Status" to "Not Started"

**Expected result**: Customer appears in "New Customers" view
**If something goes wrong**: Check Stripe-HubSpot sync in Settings → Integrations

---

## Step 2: Send Welcome Email
**Time estimate**: 3 minutes
**Who**: Customer Success Rep

1. In HubSpot, open the customer contact
2. Click "Email" → "Templates"
3. Select "Welcome - Standard Plan"
4. Personalize:
   - Replace [FIRST_NAME] with customer's first name
   - Verify Calendly link is correct
   - Add any purchase-specific notes from Stripe
5. Click "Send"
6. In contact record, set "Welcome Email Sent" to "Yes"

**Expected result**: Customer receives welcome email within 2 minutes
**If something goes wrong**: Check spam folder guidance in template; resend after 4 hours if no delivery confirmation

---

## Step 3: Schedule Kickoff Call
**Time estimate**: 2 minutes
**Who**: Customer Success Rep

1. Monitor email for customer booking via Calendly
2. If no booking within 24 hours:
   - Send "Kickoff Reminder" email template
3. If no booking within 48 hours:
   - Escalate to CS Manager
4. Once booked:
   - Set "Kickoff Scheduled" to "Yes"
   - Add call date to "Kickoff Date" field

**Expected result**: Kickoff call scheduled within 48 hours of purchase
**If something goes wrong**: Call customer directly using phone number from Stripe

---

## Step 4: Prepare Kickoff Materials
**Time estimate**: 10 minutes
**Who**: Customer Success Rep
**When**: 1 hour before scheduled kickoff call

1. Open customer record in HubSpot
2. Review company website (understand their business)
3. Open Notion → "Onboarding" → Duplicate "Kickoff Template"
4. Rename to "[Company Name] Kickoff"
5. Pre-fill:
   - Company name and industry
   - Primary contact name
   - Plan features they have access to
   - 3 suggested first actions based on their industry
6. Share Notion page with customer's email (Editor access)

**Expected result**: Personalized kickoff document ready to screenshare
**If something goes wrong**: Use generic template if time is short; personalize during call

---

## Step 5: Conduct Kickoff Call
**Time estimate**: 30 minutes
**Who**: Customer Success Rep

1. Start Zoom meeting 2 minutes early
2. Agenda:
   - Introductions (2 min)
   - Understand their goals (5 min)
   - Platform walkthrough (15 min)
   - Set up their first [core action] together (5 min)
   - Q&A and next steps (3 min)
3. During call, complete one core action with them
4. Share Notion onboarding doc link in Zoom chat
5. Send calendar invite for 14-day check-in

**Expected result**: Customer completes first core action during call
**If something goes wrong**: If technical issues, reschedule within 24 hours and send screen recording as interim

---

## Step 6: Post-Call Documentation
**Time estimate**: 5 minutes
**Who**: Customer Success Rep

1. In HubSpot, update:
   - "Onboarding Status" → "In Progress"
   - "Kickoff Completed" → "Yes"
   - "First Value Action" → "Yes" (if completed during call)
2. Log call notes:
   - Customer goals
   - Questions asked
   - Action items for both sides
3. Set task reminder for 14-day check-in

**Expected result**: Complete record of onboarding status and next steps
**If something goes wrong**: Complete documentation within 2 hours of call

---

QUALITY CHECKLIST:
- [ ] Customer record created with all required fields
- [ ] Welcome email sent within 4 hours of purchase
- [ ] Kickoff call scheduled within 48 hours
- [ ] Customer completed first core action
- [ ] 14-day check-in scheduled
- [ ] All HubSpot fields updated

---

ESCALATION:
- Customer unresponsive after 48 hours → CS Manager
- Technical issues during setup → Engineering on-call
- Customer requests refund during onboarding → CS Manager + Finance

---

REVISION HISTORY:
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | March 1, 2026 | Initial creation | [Name] |
```

### Example 2: Content Publishing SOP

**Input**: Create an SOP for publishing blog posts on our company website

**Output**:
```
SOP: BLOG POST PUBLISHING

Version: 1.2
Last Updated: March 1, 2026
Owner: Content Manager
Applies to: Content Team, Guest Contributors

---

PURPOSE:
Ensure all blog posts are published consistently with proper formatting, SEO optimization, and quality standards before going live.

---

SCOPE:
- This SOP covers: Publishing approved blog drafts to WordPress
- This SOP does NOT cover: Content creation (see SOP-022), SEO keyword research (see SOP-023)

---

PREREQUISITES:
- [ ] WordPress admin access (Editor role or above)
- [ ] Approved blog draft in Google Docs (marked "Ready to Publish")
- [ ] Featured image (1200x630px minimum)
- [ ] Yoast SEO plugin access
- [ ] Canva access for image resizing (if needed)

---

DEFINITIONS:
| Term | Definition |
|------|------------|
| Slug | URL-friendly version of title (e.g., how-to-write-sops) |
| Alt text | Description of image for accessibility and SEO |
| Meta description | 150-160 character summary for search results |

---

PROCEDURE:

## Step 1: Import Content to WordPress
**Time estimate**: 5 minutes
**Who**: Content Editor

1. Log in to WordPress admin (yoursite.com/wp-admin)
2. Click "Posts" → "Add New"
3. Open the approved Google Doc
4. Copy title → Paste in WordPress title field
5. Copy body content → Paste in WordPress editor
6. If formatting breaks:
   - Use "Paste as plain text" (Ctrl+Shift+V)
   - Re-add headers, bold, links manually

**Expected result**: Draft post with all text content imported
**If something goes wrong**: If images don't paste, add them manually in Step 3

---

## Step 2: Format the Post
**Time estimate**: 10 minutes
**Who**: Content Editor

1. Check all headers are correct level:
   - H2 for main sections
   - H3 for subsections
   - Never skip levels (H2 → H4)
2. Add bullet points and numbered lists where appropriate
3. Bold key phrases (1-2 per section maximum)
4. Add internal links:
   - Minimum 2 links to related posts
   - Use descriptive anchor text (not "click here")
5. Add external links:
   - Open in new tab (check "Open in new tab" box)
   - Maximum 3-5 per post

**Expected result**: Properly formatted post matching style guide
**If something goes wrong**: Compare to recent published post for reference

---

## Step 3: Add Images
**Time estimate**: 5 minutes
**Who**: Content Editor

1. Upload featured image:
   - Click "Set featured image" in right sidebar
   - Upload image (1200x630px minimum)
   - Add alt text describing the image
2. Add in-post images:
   - Place images near relevant text
   - Each image must have alt text
   - Use "Large" size alignment
   - Center align unless text wraps

**Expected result**: Featured image set, all images have alt text
**If something goes wrong**: Resize images in Canva if too small

---

## Step 4: Configure SEO (Yoast)
**Time estimate**: 5 minutes
**Who**: Content Editor

1. Scroll to Yoast SEO section below post
2. Enter focus keyphrase (from Content Brief)
3. Edit slug:
   - Remove stop words (a, the, and, of)
   - Keep under 5 words
   - Example: "how-to-write-sops"
4. Write meta description:
   - 150-160 characters
   - Include focus keyphrase
   - End with action or benefit
5. Check Yoast indicators:
   - Green = good
   - Orange = acceptable
   - Red = must fix before publishing

**Expected result**: Yoast shows green "SEO" indicator (minimum orange)
**If something goes wrong**: Follow Yoast suggestions to improve score

---

## Step 5: Assign Categories and Tags
**Time estimate**: 2 minutes
**Who**: Content Editor

1. In right sidebar, select one Primary Category
2. Add 1-2 Secondary Categories (if applicable)
3. Add 3-5 Tags:
   - Use existing tags first (check autocomplete)
   - Create new tags only if necessary
4. Verify categories match content topic

**Expected result**: Post categorized for proper navigation and filtering
**If something goes wrong**: Ask Content Manager if unsure about categorization

---

## Step 6: Final Review and Publish
**Time estimate**: 5 minutes
**Who**: Content Editor

1. Click "Preview" → Open in new tab
2. Review checklist:
   - [ ] Title displays correctly
   - [ ] Featured image appears
   - [ ] Formatting looks correct on desktop
   - [ ] All links work
   - [ ] Images load properly
3. Check mobile preview (Chrome DevTools → Toggle device)
4. If publishing now: Click "Publish"
5. If scheduling: Set date/time → Click "Schedule"
6. Copy live URL and add to Content Calendar spreadsheet

**Expected result**: Post live or scheduled, URL logged in Content Calendar
**If something goes wrong**: If broken after publishing, set to Draft and troubleshoot

---

QUALITY CHECKLIST:
- [ ] Title under 60 characters
- [ ] H2 and H3 headers properly structured
- [ ] Minimum 2 internal links
- [ ] All images have alt text
- [ ] Featured image is 1200x630px minimum
- [ ] Meta description is 150-160 characters
- [ ] Yoast SEO indicator is green or orange
- [ ] Mobile preview looks correct
- [ ] URL logged in Content Calendar

---

ESCALATION:
- WordPress errors or crashes → IT Support (#wordpress-help Slack)
- SEO questions → SEO Manager
- Image rights concerns → Content Manager

---

REVISION HISTORY:
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Jan 15, 2026 | Initial creation | [Name] |
| 1.1 | Feb 1, 2026 | Added Yoast configuration details | [Name] |
| 1.2 | March 1, 2026 | Updated image size requirements | [Name] |
```

### Example 3: Invoice Processing SOP

**Input**: Create an SOP for processing vendor invoices for payment

**Output**:
```
SOP: VENDOR INVOICE PROCESSING

Version: 1.0
Last Updated: March 1, 2026
Owner: Accounts Payable Manager
Applies to: Finance Team, Accounts Payable

---

PURPOSE:
Ensure all vendor invoices are processed accurately and paid on time while maintaining proper documentation and approval workflows.

---

SCOPE:
- This SOP covers: Processing invoices under $10,000
- This SOP does NOT cover: Invoices over $10,000 (require CFO approval, see SOP-041), recurring subscription payments (see SOP-042)

---

PREREQUISITES:
- [ ] Access to QuickBooks Online (AP role)
- [ ] Access to Bill.com or payment platform
- [ ] Vendor on file in approved vendor list
- [ ] Invoice received (email or mail)

---

DEFINITIONS:
| Term | Definition |
|------|------------|
| 3-way match | Matching invoice to PO and receiving report |
| Net 30 | Payment due 30 days from invoice date |
| Coding | Assigning expense to correct GL account |

---

PROCEDURE:

## Step 1: Receive and Log Invoice
**Time estimate**: 2 minutes
**Who**: AP Clerk

1. Invoice received via:
   - Email: invoices@company.com
   - Mail: Scanned by admin and uploaded to SharePoint
2. Open Invoices Tracker spreadsheet
3. Log invoice:
   - Date received
   - Vendor name
   - Invoice number
   - Amount
   - Due date
4. Save invoice PDF to SharePoint: Finance → Invoices → [YYYY-MM] folder
5. Rename file: [Vendor]_[InvoiceNumber]_[Date].pdf

**Expected result**: Invoice logged and filed within 24 hours of receipt
**If something goes wrong**: If duplicate invoice number, contact vendor to confirm before processing

---

## Step 2: Verify Invoice Details
**Time estimate**: 5 minutes
**Who**: AP Clerk

1. Open invoice and verify:
   - [ ] Vendor name matches approved vendor list
   - [ ] Invoice number is unique (check for duplicates)
   - [ ] Invoice date is current (not over 90 days old)
   - [ ] Math is correct (line items = total)
   - [ ] Payment terms are stated
2. Perform 3-way match (for PO-based purchases):
   - Locate PO number on invoice
   - Find PO in QuickBooks
   - Compare: quantities, prices, totals
   - Check receiving report: items received?
3. If discrepancies found:
   - Flag invoice in tracker ("Discrepancy")
   - Email vendor with specific questions
   - Do not process until resolved

**Expected result**: Invoice verified or flagged for follow-up
**If something goes wrong**: Invoices without POs require department manager approval (Step 3 alternate)

---

## Step 3: Code and Route for Approval
**Time estimate**: 3 minutes
**Who**: AP Clerk

1. Determine expense coding:
   - Review invoice description
   - Assign GL account code (see GL Coding Reference)
   - Assign department (if applicable)
2. Route for approval based on amount:
   - Under $1,000: Department Manager
   - $1,000-$5,000: Department Director
   - $5,000-$10,000: VP
   - Over $10,000: CFO (escalate per SOP-041)
3. Enter into Bill.com:
   - Upload invoice PDF
   - Enter coding
   - Select approver
   - Click "Send for Approval"
4. Update tracker: Status = "Pending Approval"

**Expected result**: Invoice routed to correct approver
**If something goes wrong**: If approver is out, route to their backup (see Approval Backup List)

---

## Step 4: Process Approved Invoice
**Time estimate**: 3 minutes
**Who**: AP Clerk

1. Once approved in Bill.com (email notification):
   - Open approved invoice
   - Verify approval signature/timestamp
2. Schedule payment:
   - Calculate payment date (per vendor terms)
   - If early payment discount available: Flag for AP Manager decision
   - Schedule in Bill.com
3. Enter in QuickBooks:
   - Vendor → Enter Bill
   - Enter invoice details
   - Apply coding from Bill.com
   - Mark as "Scheduled for Payment"
4. Update tracker: Status = "Scheduled"

**Expected result**: Invoice scheduled for payment by due date
**If something goes wrong**: If payment date is past due, escalate to AP Manager immediately

---

## Step 5: Execute Payment
**Time estimate**: 2 minutes per payment
**Who**: AP Manager (Clerk cannot execute)

1. On payment run day (Tuesday/Thursday):
   - Review scheduled payments in Bill.com
   - Verify cash availability
   - Approve payment batch
2. Execute payments:
   - ACH: Process in Bill.com
   - Check: Print and mail
   - Wire: Process through bank portal
3. Update QuickBooks: Mark bills as "Paid"
4. Update tracker: Status = "Paid" + Payment Date + Payment Method

**Expected result**: Payment executed and recorded
**If something goes wrong**: If payment fails, contact bank/vendor within 24 hours

---

## Step 6: File and Reconcile
**Time estimate**: 1 minute per invoice
**Who**: AP Clerk

1. Move invoice in SharePoint to "Paid" folder
2. Attach payment confirmation to invoice record
3. Weekly reconciliation:
   - Compare tracker to QuickBooks AP aging
   - Investigate any discrepancies
   - Report unresolved items to AP Manager

**Expected result**: Complete audit trail from receipt to payment
**If something goes wrong**: Missing documentation must be obtained before month-end close

---

QUALITY CHECKLIST:
- [ ] Invoice logged within 24 hours of receipt
- [ ] 3-way match completed (PO-based invoices)
- [ ] Correct GL coding applied
- [ ] Approved by authorized approver
- [ ] Paid by due date (or within terms)
- [ ] Documentation complete in SharePoint
- [ ] QuickBooks and tracker reconciled

---

ESCALATION:
- Vendor disputes → AP Manager
- Missing PO → Department that ordered
- Approval delays (over 48 hours) → AP Manager to escalate
- Suspected duplicate payment → AP Manager + Controller

---

REVISION HISTORY:
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | March 1, 2026 | Initial creation | [Name] |
```

## Quality Checklist

- [ ] Purpose clearly states why process exists
- [ ] Scope defines what's included and excluded
- [ ] Prerequisites list everything needed before starting
- [ ] Steps start with action verbs
- [ ] Each step has one clear action
- [ ] Time estimates included for each step
- [ ] Expected results defined for each step
- [ ] Troubleshooting guidance for common issues
- [ ] Escalation paths clearly defined
- [ ] Quality checklist covers critical outputs
- [ ] Version history maintained
