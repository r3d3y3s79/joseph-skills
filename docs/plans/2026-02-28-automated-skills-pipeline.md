# Automated Skills Pipeline Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a fully automated pipeline that creates Claude Code skills, validates quality, publishes to free marketplaces (SkillsMP/SkillHub), and creates premium Gumroad listings - all with zero manual intervention.

**Architecture:** GitHub repo as source of truth → GitHub Actions for CI/CD → Browser automation (Playwright/Chrome MCP) for web submissions → Quality gates ensure 8.5+ scores before publishing.

**Tech Stack:** Python, GitHub Actions, Playwright MCP, superpowers-chrome, SkillsMP CLI, Gumroad API

---

## Phase 1: Repository Setup

### Task 1: Initialize GitHub Repository Structure

**Files:**
- Create: `/home/r3d3y3s77/projects/joseph-skills/README.md`
- Create: `/home/r3d3y3s77/projects/joseph-skills/free/README.md`
- Create: `/home/r3d3y3s77/projects/joseph-skills/premium/README.md`
- Create: `/home/r3d3y3s77/projects/joseph-skills/.gitignore`

**Step 1: Create directory structure**

```bash
mkdir -p /home/r3d3y3s77/projects/joseph-skills/{free,premium,scripts,templates,.github/workflows}
mkdir -p /home/r3d3y3s77/projects/joseph-skills/free/{content-creation,ecommerce,business,developer,marketing}
mkdir -p /home/r3d3y3s77/projects/joseph-skills/premium/{workflows,notion,videos}
```

**Step 2: Create main README**

```markdown
# Joseph's Claude Code Skills

Production-ready Claude Code skills for content creators, marketers, and developers.

## Free Skills (50+)
Available on [SkillsMP](https://skillsmp.com) and [SkillHub](https://skillhub.club)

## Premium: Content Empire Pro ($97)
Available on [Gumroad](https://storemanjoe3.gumroad.com)

## Categories
- Content Creation (12 skills)
- E-commerce (10 skills)
- Business (8 skills)
- Developer (10 skills)
- Marketing (10 skills)

## Installation
\`\`\`bash
# Install via SkillsMP CLI
skills install joseph-skills/youtube-script-pro
\`\`\`
```

**Step 3: Create .gitignore**

```
*.pyc
__pycache__/
.env
*.log
node_modules/
dist/
*.zip
```

**Step 4: Initialize git and commit**

```bash
cd /home/r3d3y3s77/projects/joseph-skills
git init
git add .
git commit -m "Initial repository structure"
```

---

### Task 2: Create Skill Template System

**Files:**
- Create: `/home/r3d3y3s77/projects/joseph-skills/templates/skill_template.md`
- Create: `/home/r3d3y3s77/projects/joseph-skills/scripts/generate_skill.py`

**Step 1: Create skill template**

```markdown
---
name: {{SKILL_NAME}}
description: {{DESCRIPTION}}
---

# {{SKILL_TITLE}}

{{INTRO_PARAGRAPH}}

## When to Use

Use this skill when:
- {{USE_CASE_1}}
- {{USE_CASE_2}}
- {{USE_CASE_3}}

## Output Structure

### {{OUTPUT_SECTION_1}}
{{OUTPUT_DETAILS_1}}

### {{OUTPUT_SECTION_2}}
{{OUTPUT_DETAILS_2}}

## Quality Checklist

Before finalizing output, verify:
- [ ] {{CHECK_1}}
- [ ] {{CHECK_2}}
- [ ] {{CHECK_3}}
- [ ] {{CHECK_4}}

## Anti-Patterns (AVOID)

- {{ANTIPATTERN_1}}
- {{ANTIPATTERN_2}}
- {{ANTIPATTERN_3}}

## Examples

### Example 1: {{EXAMPLE_1_TITLE}}

**Input:** {{EXAMPLE_1_INPUT}}

**Output:**
{{EXAMPLE_1_OUTPUT}}

### Example 2: {{EXAMPLE_2_TITLE}}

**Input:** {{EXAMPLE_2_INPUT}}

**Output:**
{{EXAMPLE_2_OUTPUT}}

### Example 3: {{EXAMPLE_3_TITLE}}

**Input:** {{EXAMPLE_3_INPUT}}

**Output:**
{{EXAMPLE_3_OUTPUT}}
```

**Step 2: Create skill generator script**

```python
#!/usr/bin/env python3
"""
Skill Generator - Creates high-quality SKILL.md files from templates
"""
import os
import sys
import json
import re
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / "templates" / "skill_template.md"
FREE_PATH = Path(__file__).parent.parent / "free"

def generate_skill(category: str, name: str, config: dict) -> str:
    """Generate a skill from template and config."""
    template = TEMPLATE_PATH.read_text()

    # Replace all template variables
    for key, value in config.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))

    return template

def save_skill(category: str, name: str, content: str):
    """Save skill to appropriate directory."""
    skill_dir = FREE_PATH / category / name
    skill_dir.mkdir(parents=True, exist_ok=True)

    skill_path = skill_dir / "SKILL.md"
    skill_path.write_text(content)
    print(f"Created: {skill_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_skill.py <category> <skill-name> [config.json]")
        sys.exit(1)

    category = sys.argv[1]
    name = sys.argv[2]
    config_file = sys.argv[3] if len(sys.argv) > 3 else None

    if config_file:
        config = json.loads(Path(config_file).read_text())
    else:
        config = {}

    content = generate_skill(category, name, config)
    save_skill(category, name, content)
```

**Step 3: Commit**

```bash
git add templates/ scripts/
git commit -m "feat: add skill template system"
```

---

### Task 3: Create Quality Validation Script

**Files:**
- Create: `/home/r3d3y3s77/projects/joseph-skills/scripts/validate_skill.py`

**Step 1: Create validation script**

```python
#!/usr/bin/env python3
"""
Skill Validator - Ensures skills meet quality standards (8.5+ score)
"""
import sys
import re
from pathlib import Path

REQUIRED_SECTIONS = [
    "When to Use",
    "Output Structure",
    "Quality Checklist",
    "Anti-Patterns",
    "Examples"
]

BANNED_PATTERNS = [
    r"(?i)premium quality",
    r"(?i)high[- ]quality",
    r"(?i)best in class",
    r"(?i)world[- ]class",
    r"(?i)cutting[- ]edge",
    r"(?i)leverage",
    r"(?i)synergy"
]

def validate_frontmatter(content: str) -> tuple[bool, list]:
    """Validate YAML frontmatter."""
    errors = []
    if not content.startswith("---"):
        errors.append("Missing YAML frontmatter")
        return False, errors

    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append("Invalid YAML frontmatter format")
        return False, errors

    frontmatter = parts[1]
    if "name:" not in frontmatter:
        errors.append("Missing 'name' in frontmatter")
    if "description:" not in frontmatter:
        errors.append("Missing 'description' in frontmatter")

    return len(errors) == 0, errors

def validate_sections(content: str) -> tuple[bool, list]:
    """Validate required sections exist."""
    errors = []
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in content:
            errors.append(f"Missing required section: {section}")
    return len(errors) == 0, errors

def validate_examples(content: str) -> tuple[bool, list]:
    """Validate at least 3 examples exist."""
    errors = []
    example_count = len(re.findall(r"### Example \d+:", content))
    if example_count < 3:
        errors.append(f"Need 3+ examples, found {example_count}")
    return len(errors) == 0, errors

def validate_banned_patterns(content: str) -> tuple[bool, list]:
    """Check for banned generic patterns."""
    errors = []
    for pattern in BANNED_PATTERNS:
        if re.search(pattern, content):
            errors.append(f"Banned pattern found: {pattern}")
    return len(errors) == 0, errors

def calculate_score(content: str) -> float:
    """Calculate quality score (0-10)."""
    score = 10.0

    # Deductions
    _, frontmatter_errors = validate_frontmatter(content)
    score -= len(frontmatter_errors) * 1.0

    _, section_errors = validate_sections(content)
    score -= len(section_errors) * 0.5

    _, example_errors = validate_examples(content)
    score -= len(example_errors) * 1.0

    _, banned_errors = validate_banned_patterns(content)
    score -= len(banned_errors) * 0.5

    # Bonus for length (comprehensive skills)
    word_count = len(content.split())
    if word_count > 800:
        score += 0.5
    if word_count > 1200:
        score += 0.5

    return max(0, min(10, score))

def validate_skill(path: Path) -> tuple[bool, float, list]:
    """Full validation of a skill file."""
    content = path.read_text()
    errors = []

    _, e = validate_frontmatter(content)
    errors.extend(e)

    _, e = validate_sections(content)
    errors.extend(e)

    _, e = validate_examples(content)
    errors.extend(e)

    _, e = validate_banned_patterns(content)
    errors.extend(e)

    score = calculate_score(content)
    passed = score >= 8.5 and len(errors) == 0

    return passed, score, errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_skill.py <path/to/SKILL.md>")
        sys.exit(1)

    path = Path(sys.argv[1])
    passed, score, errors = validate_skill(path)

    print(f"Score: {score:.1f}/10")
    print(f"Status: {'PASS' if passed else 'FAIL'}")

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  - {e}")

    sys.exit(0 if passed else 1)
```

**Step 2: Test validation script**

```bash
python scripts/validate_skill.py free/content-creation/youtube-script-pro/SKILL.md
```

**Step 3: Commit**

```bash
git add scripts/validate_skill.py
git commit -m "feat: add skill quality validation (8.5+ threshold)"
```

---

## Phase 2: Browser Automation Setup

### Task 4: Create Gumroad Automation Script

**Files:**
- Create: `/home/r3d3y3s77/projects/joseph-skills/scripts/gumroad_automation.py`

**Step 1: Create Gumroad automation script**

```python
#!/usr/bin/env python3
"""
Gumroad Automation - Creates/updates products via browser automation
Requires: superpowers-chrome MCP or Playwright MCP
"""
import json
import subprocess
import time
from pathlib import Path

class GumroadAutomation:
    """Automate Gumroad product management via browser."""

    def __init__(self):
        self.base_url = "https://app.gumroad.com"

    def _run_browser_action(self, action: dict) -> dict:
        """Execute browser action via MCP."""
        # This will be called via Claude Code's MCP tools
        # For standalone use, implement CDP connection
        return action

    def navigate(self, url: str):
        """Navigate to URL."""
        return {"action": "navigate", "payload": url}

    def wait_for(self, selector: str, timeout: int = 10000):
        """Wait for element."""
        return {"action": "await_element", "selector": selector, "timeout": timeout}

    def type_text(self, selector: str, text: str):
        """Type into field."""
        return {"action": "type", "selector": selector, "payload": text}

    def click(self, selector: str):
        """Click element."""
        return {"action": "click", "selector": selector}

    def create_product_actions(self, name: str, description: str, price: int) -> list:
        """Generate actions to create a Gumroad product."""
        return [
            self.navigate(f"{self.base_url}/products/new"),
            self.wait_for("input[name='name']"),
            self.type_text("input[name='name']", name),
            self.type_text("textarea[name='description']", description),
            self.type_text("input[name='price']", str(price)),
            self.click("button[type='submit']"),
            self.wait_for(".product-created", timeout=15000)
        ]

    def generate_workflow(self, product_config: dict) -> str:
        """Generate Claude Code workflow for product creation."""
        actions = self.create_product_actions(
            product_config["name"],
            product_config["description"],
            product_config["price"]
        )

        workflow = "# Gumroad Product Creation Workflow\n\n"
        workflow += "Execute these browser actions in sequence:\n\n"

        for i, action in enumerate(actions, 1):
            workflow += f"## Step {i}\n```json\n{json.dumps(action, indent=2)}\n```\n\n"

        return workflow

if __name__ == "__main__":
    auto = GumroadAutomation()

    config = {
        "name": "Content Empire Pro",
        "description": "50+ premium Claude Code skills for content creators",
        "price": 97
    }

    workflow = auto.generate_workflow(config)
    print(workflow)
```

**Step 2: Create skill for Gumroad automation**

```bash
mkdir -p /home/r3d3y3s77/.claude/skills/gumroad-product-creator
```

**Step 3: Commit**

```bash
git add scripts/gumroad_automation.py
git commit -m "feat: add Gumroad browser automation script"
```

---

### Task 5: Create SkillsMP Submission Automation

**Files:**
- Create: `/home/r3d3y3s77/projects/joseph-skills/scripts/submit_to_marketplaces.py`

**Step 1: Create marketplace submission script**

```python
#!/usr/bin/env python3
"""
Marketplace Submission - Auto-submit skills to SkillsMP and SkillHub
"""
import subprocess
import os
from pathlib import Path

REPO_NAME = "josephmarr/joseph-skills"  # Update with actual GitHub username

def submit_to_skillsmp():
    """Submit repo to SkillsMP via CLI."""
    try:
        result = subprocess.run(
            ["npx", "agent-skills-cli", "submit-repo", REPO_NAME],
            capture_output=True,
            text=True,
            timeout=120
        )
        print(f"SkillsMP submission: {result.stdout}")
        return result.returncode == 0
    except Exception as e:
        print(f"SkillsMP submission failed: {e}")
        return False

def submit_to_skillhub():
    """SkillHub auto-indexes from GitHub - just ensure repo is public."""
    print("SkillHub: Auto-indexes from GitHub (no action needed)")
    return True

def main():
    """Submit to all marketplaces."""
    print("Submitting to marketplaces...")

    skillsmp_ok = submit_to_skillsmp()
    skillhub_ok = submit_to_skillhub()

    print(f"\nResults:")
    print(f"  SkillsMP: {'OK' if skillsmp_ok else 'FAILED'}")
    print(f"  SkillHub: {'OK' if skillhub_ok else 'FAILED'}")

    return skillsmp_ok and skillhub_ok

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
```

**Step 2: Commit**

```bash
git add scripts/submit_to_marketplaces.py
git commit -m "feat: add marketplace submission automation"
```

---

## Phase 3: GitHub Actions CI/CD

### Task 6: Create Validation Workflow

**Files:**
- Create: `/home/r3d3y3s77/projects/joseph-skills/.github/workflows/validate.yml`

**Step 1: Create validation workflow**

```yaml
name: Validate Skills

on:
  pull_request:
    paths:
      - 'free/**/*.md'
      - 'premium/**/*.md'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Find changed skills
        id: changed
        run: |
          FILES=$(git diff --name-only ${{ github.event.pull_request.base.sha }} -- '*.md' | grep SKILL.md || true)
          echo "files=$FILES" >> $GITHUB_OUTPUT

      - name: Validate skills
        run: |
          for file in ${{ steps.changed.outputs.files }}; do
            echo "Validating: $file"
            python scripts/validate_skill.py "$file"
          done

      - name: Quality gate
        run: |
          echo "All skills passed quality gate (8.5+ score)"
```

**Step 2: Commit**

```bash
git add .github/workflows/validate.yml
git commit -m "ci: add skill validation workflow"
```

---

### Task 7: Create Auto-Publish Workflow

**Files:**
- Create: `/home/r3d3y3s77/projects/joseph-skills/.github/workflows/publish.yml`

**Step 1: Create publish workflow**

```yaml
name: Publish Skills

on:
  push:
    branches: [main]
    paths:
      - 'free/**/*.md'

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install agent-skills-cli
        run: npm install -g agent-skills-cli

      - name: Submit to SkillsMP
        env:
          SKILLSMP_API_KEY: ${{ secrets.SKILLSMP_API_KEY }}
        run: |
          skills submit-repo ${{ github.repository }}

      - name: Notify success
        run: echo "Skills published to SkillsMP successfully"
```

**Step 2: Commit**

```bash
git add .github/workflows/publish.yml
git commit -m "ci: add auto-publish workflow for marketplaces"
```

---

## Phase 4: Create First Batch of Skills (10 High-Quality)

### Task 8: Create YouTube Script Pro Skill

**Files:**
- Create: `/home/r3d3y3s77/projects/joseph-skills/free/content-creation/youtube-script-pro/SKILL.md`

**Step 1: Create the skill**

(Full skill content - approximately 1500 words with 3 detailed examples, quality checklist, anti-patterns)

**Step 2: Validate**

```bash
python scripts/validate_skill.py free/content-creation/youtube-script-pro/SKILL.md
```

Expected: Score 9.0+, PASS

**Step 3: Commit**

```bash
git add free/content-creation/youtube-script-pro/
git commit -m "feat: add youtube-script-pro skill"
```

---

### Task 9: Create Blog SEO Writer Skill

(Similar structure to Task 8)

---

### Task 10: Create Shopify Product Writer Skill

(Similar structure to Task 8)

---

## Phase 5: Premium System Setup

### Task 11: Create Premium Packaging Script

**Files:**
- Create: `/home/r3d3y3s77/projects/joseph-skills/scripts/package_premium.py`

**Step 1: Create packaging script**

```python
#!/usr/bin/env python3
"""
Premium Packager - Creates distributable ZIP for Gumroad
"""
import zipfile
import os
from pathlib import Path
from datetime import datetime

PREMIUM_PATH = Path(__file__).parent.parent / "premium"
OUTPUT_PATH = Path(__file__).parent.parent / "dist"

def package_premium():
    """Create premium ZIP package."""
    OUTPUT_PATH.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d")
    zip_name = f"content-empire-pro-{timestamp}.zip"
    zip_path = OUTPUT_PATH / zip_name

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add premium skills
        for skill_path in PREMIUM_PATH.rglob("SKILL.md"):
            arcname = str(skill_path.relative_to(PREMIUM_PATH.parent))
            zf.write(skill_path, arcname)

        # Add README
        readme = PREMIUM_PATH / "README.md"
        if readme.exists():
            zf.write(readme, "premium/README.md")

        # Add installation guide
        install = PREMIUM_PATH / "INSTALL.md"
        if install.exists():
            zf.write(install, "premium/INSTALL.md")

    print(f"Created: {zip_path}")
    print(f"Size: {zip_path.stat().st_size / 1024:.1f} KB")
    return zip_path

if __name__ == "__main__":
    package_premium()
```

**Step 2: Commit**

```bash
git add scripts/package_premium.py
git commit -m "feat: add premium packaging script"
```

---

## Phase 6: Claude Code Integration Skill

### Task 12: Create Skill Creation Skill

**Files:**
- Create: `/home/r3d3y3s77/.claude/skills/skill-creator/SKILL.md`

**Step 1: Create the meta-skill**

This skill enables one-command skill creation with automatic publishing.

```markdown
---
name: skill-creator
description: Use when creating new Claude Code skills. Automatically generates, validates, and publishes skills to marketplaces.
---

# Skill Creator

Create production-ready Claude Code skills with one command.

## Workflow

1. Generate skill from template
2. Validate quality (8.5+ required)
3. Push to GitHub
4. Auto-publish to SkillsMP/SkillHub

## Usage

"Create a skill for writing LinkedIn posts"

## Output

- SKILL.md file in joseph-skills repo
- Automatic PR creation
- Quality validation
- Marketplace submission on merge
```

**Step 2: Commit to skills repo**

```bash
git add /home/r3d3y3s77/.claude/skills/skill-creator/
git commit -m "feat: add skill-creator meta-skill"
```

---

## Summary

**Total Tasks:** 12
**Estimated Time:** 4-6 hours
**End Result:** Fully automated pipeline where:

1. You say "Create a skill for X"
2. Claude generates high-quality skill
3. Pushes to GitHub
4. CI validates quality
5. Auto-publishes to SkillsMP/SkillHub
6. Premium skills auto-package for Gumroad

**Zero manual steps after initial setup.**
