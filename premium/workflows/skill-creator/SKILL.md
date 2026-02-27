---
name: skill-creator
description: Create production-ready Claude Code skills with automatic quality validation. Use when building new skills that need proper structure, examples, and publishing readiness.
---

# Skill Creator

Build Claude Code skills that meet marketplace quality standards. This skill guides you through creating skills with proper structure, comprehensive examples, and validation-ready content.

## When to Use

Use this skill when:
- Creating new Claude Code skills from scratch
- Converting existing workflows into reusable skills
- Building skills for SkillsMP/SkillHub publication
- Packaging skills for premium distribution
- Refactoring existing skills to pass quality validation

## Output Structure

### YAML Frontmatter
Every skill starts with:
```yaml
---
name: skill-name (lowercase, hyphens)
description: One sentence describing when to use this skill and what it produces
---
```

### Skill Sections (Required)
1. **Title** - H1 with skill name in readable format
2. **Introduction** - 2-3 sentences explaining the skill's purpose
3. **When to Use** - 5+ bullet points of specific use cases
4. **Output Structure** - Detailed breakdown of what the skill generates
5. **Quality Checklist** - 8+ verification items as checkboxes
6. **Anti-Patterns** - 5+ things to avoid with explanations
7. **Examples** - 3+ complete input/output examples

### Validation Requirements
To pass quality validation (8.5+ score):
- All required sections present
- At least 3 detailed examples
- At least 3 quality checklist items
- At least 3 anti-patterns
- 800+ words total
- No banned patterns (generic AI phrases)

## Quality Checklist

Before finalizing a new skill, verify:
- [ ] Name is lowercase with hyphens (e.g., youtube-script-pro)
- [ ] Description is one clear sentence under 200 characters
- [ ] Introduction explains purpose without fluff
- [ ] When to Use has 5+ specific scenarios
- [ ] Output Structure describes exact deliverables
- [ ] Quality Checklist has actionable verification items
- [ ] Anti-Patterns explain WHY to avoid each pattern
- [ ] Examples show complete input AND output
- [ ] Examples cover different use cases (not variations of same thing)
- [ ] No generic phrases: "best practices", "optimize", "enhance"
- [ ] Word count is 800-1500 words
- [ ] Formatting is consistent throughout

## Anti-Patterns (AVOID)

- Vague descriptions: "Helps you write better content" - says nothing specific about what or how
- Single-purpose examples: Three examples that are basically the same scenario with different words
- Empty checklist items: "Check for quality" - what does quality mean here?
- Anti-patterns without context: "Don't use passive voice" - why? what's the consequence?
- Feature lists instead of benefits: "Supports markdown" - so what? what does that enable?
- Missing output structure: User has no idea what format to expect
- Generic skill names: "content-helper" or "writing-assistant" - not discoverable
- Overpromising descriptions: "The only skill you'll ever need" - damages credibility
- Thin examples: Input/output pairs that are one line each - not useful for complex tasks

## Examples

### Example 1: Creating a Content Skill

**Input:** Create a skill for writing Twitter threads from blog posts

**Output:**

```markdown
---
name: blog-to-thread
description: Convert blog posts into viral Twitter threads. Extracts key points, creates hooks, and formats for Twitter's character limits.
---

# Blog to Thread

Transform blog posts into Twitter threads that drive engagement. This skill extracts the most shareable insights from long-form content and structures them for Twitter's format.

## When to Use

Use this skill when:
- Converting blog posts into Twitter content
- Repurposing newsletter content for social
- Creating thread versions of articles
- Building a Twitter presence from existing content
- Breaking down complex topics into thread format

## Output Structure

### Thread Structure
- Hook tweet (< 280 characters, curiosity-driven)
- Context tweet (why this matters)
- 5-10 insight tweets (one key point each)
- Conclusion tweet with CTA
- Alt text for any images suggested

### Per-Tweet Format
- Character count shown
- Emoji placement if appropriate
- Thread numbering (1/12 format)
- Reply chain structure

## Quality Checklist

Before finalizing output, verify:
- [ ] Hook creates curiosity (not clickbait)
- [ ] Each tweet can stand alone (context included)
- [ ] All tweets under 280 characters
- [ ] Thread flows logically
- [ ] Original blog attribution included
- [ ] CTA is clear and specific
- [ ] No orphan tweets (all connect to narrative)
- [ ] Thread length appropriate for content depth

## Anti-Patterns (AVOID)

- Thread padding: Adding tweets just to make it longer - reduces engagement
- Missing hook: Starting with context instead of curiosity - no one clicks to expand
- Dense tweets: Cramming 280 characters of info - exhausting to read
- No structure: Disconnected thoughts with no narrative - loses readers
- Vague CTAs: "Let me know what you think" - no action direction

## Examples

[3 complete examples would follow with actual blog post input and thread output]
```

### Example 2: Creating a Developer Skill

**Input:** Create a skill for writing Git commit messages

**Output:**

```markdown
---
name: commit-message-writer
description: Generate clear, conventional Git commit messages from code diffs or change descriptions. Follows Angular/Conventional Commits format.
---

# Commit Message Writer

Write commit messages that explain what changed and why. This skill follows the Conventional Commits specification while keeping messages readable for future developers.

## When to Use

Use this skill when:
- Committing code changes
- Writing messages for merged PRs
- Documenting breaking changes
- Creating release notes from commits
- Standardizing team commit style

## Output Structure

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- feat: New feature
- fix: Bug fix
- docs: Documentation only
- style: Formatting (no code change)
- refactor: Code change (no feature/fix)
- test: Adding/updating tests
- chore: Maintenance tasks

## Quality Checklist

Before finalizing output, verify:
- [ ] Type matches the change
- [ ] Scope identifies affected area
- [ ] Subject is imperative mood ("add" not "added")
- [ ] Subject under 50 characters
- [ ] Body explains WHY (not just what)
- [ ] Breaking changes noted in footer
- [ ] Related issues referenced

## Anti-Patterns (AVOID)

- "Fix bug" - which bug? what was the symptom?
- "Update code" - all commits update code, be specific
- Past tense subjects - use imperative: "add" not "added"
- Giant commits - if you need 5 paragraphs, commit should be smaller
- No context - future developers need to understand the why

## Examples

[3 complete examples with actual diffs and commit messages]
```

### Example 3: Creating an E-commerce Skill

**Input:** Create a skill for writing product FAQ sections

**Output:**

```markdown
---
name: product-faq-generator
description: Generate FAQ sections for e-commerce product pages. Creates common questions with conversion-focused answers that address buyer objections.
---

# Product FAQ Generator

Build FAQ sections that answer real customer questions before they have to ask. This skill anticipates objections, provides detailed answers, and uses structured data for SEO benefits.

## When to Use

Use this skill when:
- Creating new product pages
- Reducing customer support tickets
- Improving SEO with FAQ schema
- Addressing common objections preemptively
- Building trust with detailed product information

## Output Structure

### FAQ Section
- 5-10 question/answer pairs
- Questions in customer voice
- Answers that sell while informing
- Schema markup suggestions

### Per Question Format
- Question: Written as customer would ask it
- Answer: 2-4 sentences, benefit-focused
- Related link: Internal link opportunity

## Quality Checklist

Before finalizing output, verify:
- [ ] Questions sound like real customer language
- [ ] Answers address the underlying concern (not just surface question)
- [ ] At least one question about shipping/returns
- [ ] At least one question about sizing/compatibility
- [ ] Answers don't repeat product description verbatim
- [ ] Schema markup provided for rich results
- [ ] Questions ordered by buyer journey stage

## Anti-Patterns (AVOID)

- Corporate voice: "Our product leverages..." - customers don't talk like this
- Avoiding negatives: "Can I return this?" answered without return policy
- FAQ as ad: Every answer is a sales pitch - damages trust
- Obvious questions: "Is this product good?" - waste of space
- Long answers: 500 words per question - use product description instead

## Examples

[3 complete examples with product context and FAQ output]
```

---

## Creating Your First Skill

1. **Start with the use case** - What specific task will this skill accomplish?
2. **Write the description** - One sentence that appears in skill discovery
3. **List when to use** - At least 5 specific scenarios
4. **Define the output** - What exactly does the skill generate?
5. **Build the checklist** - What must be verified before delivery?
6. **Document anti-patterns** - What mistakes does this skill prevent?
7. **Create examples** - At least 3, covering different scenarios
8. **Validate** - Run through validate_skill.py, score must be 8.5+

## Publishing Workflow

1. Create skill in `free/[category]/[skill-name]/SKILL.md`
2. Validate: `python scripts/validate_skill.py path/to/SKILL.md`
3. Commit and push - CI validates automatically
4. On merge to main, auto-publishes to SkillsMP
5. For premium skills, use `scripts/package_premium.py` for Gumroad
