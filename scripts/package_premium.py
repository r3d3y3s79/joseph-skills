#!/usr/bin/env python3
"""
Premium Packager - Creates distributable ZIP for Gumroad

Usage:
    python package_premium.py              # Create ZIP with default name
    python package_premium.py --name MyPack # Create ZIP with custom name
    python package_premium.py --validate   # Validate before packaging

Output:
    Creates ZIP file in /dist/ directory ready for Gumroad upload
"""
import zipfile
import os
import sys
import hashlib
from pathlib import Path
from datetime import datetime

PREMIUM_PATH = Path(__file__).parent.parent / "premium"
FREE_PATH = Path(__file__).parent.parent / "free"
OUTPUT_PATH = Path(__file__).parent.parent / "dist"
SCRIPTS_PATH = Path(__file__).parent

def validate_skill(skill_path: Path) -> tuple:
    """Validate a skill using the validation script."""
    import subprocess
    result = subprocess.run(
        [sys.executable, str(SCRIPTS_PATH / "validate_skill.py"), str(skill_path)],
        capture_output=True,
        text=True,
        timeout=30
    )
    return result.returncode == 0, result.stdout

def count_skills(base_path: Path) -> int:
    """Count SKILL.md files in directory."""
    return len(list(base_path.rglob("SKILL.md")))

def create_install_guide() -> str:
    """Generate installation guide content."""
    return """# Content Empire Pro - Installation Guide

## Quick Install (5 minutes)

### Step 1: Extract the ZIP
Extract all files to a temporary location.

### Step 2: Copy to Claude Skills Directory

**macOS/Linux:**
```bash
cp -r premium/* ~/.claude/skills/
```

**Windows:**
```powershell
Copy-Item -Path "premium\\*" -Destination "$env:USERPROFILE\\.claude\\skills" -Recurse
```

### Step 3: Verify Installation
```bash
ls ~/.claude/skills/
```
You should see all premium skill folders.

### Step 4: Use the Skills
In Claude Code, reference any skill by name:
- "Use the youtube-script-pro skill to write a video script"
- "Apply the shopify-product-writer skill to this product"

## Troubleshooting

**Skills not loading?**
- Ensure SKILL.md exists in each folder
- Check file permissions (should be readable)
- Restart Claude Code

**Need help?**
- Email: support@teaotech.co.nz
- Include your order ID and error message

## Updates
You have lifetime access to updates. New versions will be emailed to your purchase email.

## License
Personal use only. Do not redistribute or resell.

---
Thank you for purchasing Content Empire Pro!
"""

def create_readme() -> str:
    """Generate premium README content."""
    return """# Content Empire Pro

50+ production-ready Claude Code skills for content creators, marketers, and developers.

## What's Included

### Content Creation Skills
- youtube-script-pro - YouTube video scripts with hook frameworks
- blog-seo-writer - SEO-optimized blog posts
- twitter-thread-builder - Viral Twitter threads
- newsletter-writer - Email newsletters
- linkedin-post-creator - LinkedIn content

### E-commerce Skills
- shopify-product-writer - Product descriptions that convert
- amazon-listing-optimizer - Amazon product listings
- email-sequence-builder - E-commerce email sequences

### Workflow Skills (Premium Exclusive)
- content-calendar-planner - Full month content planning
- batch-content-generator - Generate 10+ pieces at once
- repurpose-content - Transform one piece into many formats

### Notion Integration Skills (Premium Exclusive)
- notion-content-tracker - Sync content with Notion
- notion-idea-capture - Quick idea to structured note
- notion-weekly-review - Automated weekly summaries

## Installation
See INSTALL.md for setup instructions.

## Support
- Email: support@teaotech.co.nz
- Response time: Within 24 hours

## License
Personal use only. Do not redistribute.

---
Version: 1.0.0
Last Updated: {date}
""".format(date=datetime.now().strftime("%Y-%m-%d"))

def package_premium(name: str = None, validate: bool = False) -> Path:
    """Create premium ZIP package."""
    OUTPUT_PATH.mkdir(exist_ok=True)

    # Count skills
    premium_count = count_skills(PREMIUM_PATH)
    free_count = count_skills(FREE_PATH)
    total_count = premium_count + free_count

    print(f"Skills found:")
    print(f"  Premium: {premium_count}")
    print(f"  Free (bonus): {free_count}")
    print(f"  Total: {total_count}")

    # Validate if requested
    if validate:
        print("\nValidating skills...")
        failed = []
        for skill_path in list(PREMIUM_PATH.rglob("SKILL.md")) + list(FREE_PATH.rglob("SKILL.md")):
            passed, output = validate_skill(skill_path)
            status = "PASS" if passed else "FAIL"
            print(f"  [{status}] {skill_path.parent.name}")
            if not passed:
                failed.append(skill_path.parent.name)

        if failed:
            print(f"\n{len(failed)} skills failed validation. Fix before packaging.")
            sys.exit(1)
        print("\nAll skills validated successfully!")

    # Create ZIP
    timestamp = datetime.now().strftime("%Y%m%d")
    zip_name = name or f"content-empire-pro-{timestamp}"
    if not zip_name.endswith(".zip"):
        zip_name += ".zip"
    zip_path = OUTPUT_PATH / zip_name

    print(f"\nCreating package: {zip_path}")

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add premium skills
        for skill_path in PREMIUM_PATH.rglob("SKILL.md"):
            arcname = str(skill_path.relative_to(PREMIUM_PATH.parent))
            zf.write(skill_path, arcname)
            print(f"  Added: {arcname}")

        # Add free skills as bonus
        for skill_path in FREE_PATH.rglob("SKILL.md"):
            arcname = str(skill_path.relative_to(FREE_PATH.parent))
            zf.write(skill_path, arcname)
            print(f"  Added (bonus): {arcname}")

        # Add documentation
        zf.writestr("INSTALL.md", create_install_guide())
        zf.writestr("README.md", create_readme())
        print("  Added: INSTALL.md")
        print("  Added: README.md")

    # Stats
    file_size = zip_path.stat().st_size
    file_hash = hashlib.md5(zip_path.read_bytes()).hexdigest()[:8]

    print(f"\n{'='*50}")
    print(f"Package created successfully!")
    print(f"{'='*50}")
    print(f"File: {zip_path}")
    print(f"Size: {file_size / 1024:.1f} KB")
    print(f"Hash: {file_hash}")
    print(f"Skills: {total_count}")
    print(f"\nReady for Gumroad upload!")

    return zip_path

def main():
    args = sys.argv[1:]
    name = None
    validate = False

    for i, arg in enumerate(args):
        if arg == "--name" and i + 1 < len(args):
            name = args[i + 1]
        elif arg == "--validate":
            validate = True

    package_premium(name=name, validate=validate)

if __name__ == "__main__":
    main()
