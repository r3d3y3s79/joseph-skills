#!/usr/bin/env python3
"""
Marketplace Submission - Auto-submit skills to SkillsMP and SkillHub

Usage:
    python submit_to_marketplaces.py              # Submit all skills
    python submit_to_marketplaces.py --validate   # Validate first, then submit
    python submit_to_marketplaces.py --dry-run    # Show what would be submitted

Marketplaces:
    - SkillsMP: Uses agent-skills-cli to submit repo
    - SkillHub: Auto-indexes from GitHub (no action needed)

Requirements:
    - npm/npx installed
    - agent-skills-cli installed or available via npx
    - GitHub repo must be public
    - SKILLSMP_API_KEY env variable (optional, for authenticated submissions)
"""
import subprocess
import os
import sys
from pathlib import Path

# Update with actual GitHub username/repo
REPO_NAME = os.environ.get("GITHUB_REPO", "josephmarr/joseph-skills")
FREE_PATH = Path(__file__).parent.parent / "free"

def find_skills() -> list:
    """Find all SKILL.md files in free directory."""
    skills = []
    for skill_file in FREE_PATH.rglob("SKILL.md"):
        relative_path = skill_file.relative_to(FREE_PATH.parent)
        category = skill_file.parent.parent.name
        name = skill_file.parent.name
        skills.append({
            "path": str(skill_file),
            "relative": str(relative_path),
            "category": category,
            "name": name
        })
    return skills

def validate_skill(path: str) -> tuple:
    """Validate a skill file."""
    validate_script = Path(__file__).parent / "validate_skill.py"
    try:
        result = subprocess.run(
            [sys.executable, str(validate_script), path],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode == 0, result.stdout
    except Exception as e:
        return False, str(e)

def submit_to_skillsmp() -> bool:
    """Submit repo to SkillsMP via CLI."""
    print(f"Submitting to SkillsMP: {REPO_NAME}")
    try:
        result = subprocess.run(
            ["npx", "agent-skills-cli", "submit-repo", REPO_NAME],
            capture_output=True,
            text=True,
            timeout=120
        )
        if result.returncode == 0:
            print(f"  Success: {result.stdout.strip()}")
            return True
        else:
            print(f"  Failed: {result.stderr.strip()}")
            return False
    except FileNotFoundError:
        print("  Error: npx not found. Install Node.js to use SkillsMP CLI.")
        return False
    except subprocess.TimeoutExpired:
        print("  Error: Submission timed out after 120 seconds.")
        return False
    except Exception as e:
        print(f"  Error: {e}")
        return False

def submit_to_skillhub() -> bool:
    """SkillHub auto-indexes from GitHub - just ensure repo is public."""
    print("SkillHub: Auto-indexes from public GitHub repos")
    print("  No manual submission required")
    print(f"  Ensure {REPO_NAME} is public on GitHub")
    return True

def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    validate_first = "--validate" in args

    print("=" * 60)
    print("Marketplace Submission Tool")
    print("=" * 60)

    # Find all skills
    skills = find_skills()
    print(f"\nFound {len(skills)} skills:")
    for skill in skills:
        print(f"  - {skill['category']}/{skill['name']}")

    # Validate if requested
    if validate_first:
        print("\n--- Validation ---")
        failed = []
        for skill in skills:
            passed, output = validate_skill(skill["path"])
            status = "PASS" if passed else "FAIL"
            print(f"  [{status}] {skill['name']}")
            if not passed:
                failed.append(skill["name"])

        if failed:
            print(f"\n{len(failed)} skills failed validation:")
            for name in failed:
                print(f"  - {name}")
            print("\nFix validation errors before submitting.")
            sys.exit(1)
        else:
            print("\nAll skills passed validation!")

    # Dry run mode
    if dry_run:
        print("\n--- Dry Run (no submissions) ---")
        print(f"Would submit repo: {REPO_NAME}")
        print("Marketplaces: SkillsMP, SkillHub")
        sys.exit(0)

    # Submit
    print("\n--- Submitting ---")
    skillsmp_ok = submit_to_skillsmp()
    skillhub_ok = submit_to_skillhub()

    # Results
    print("\n--- Results ---")
    print(f"  SkillsMP: {'OK' if skillsmp_ok else 'FAILED'}")
    print(f"  SkillHub: {'OK' if skillhub_ok else 'FAILED'}")

    if not (skillsmp_ok and skillhub_ok):
        print("\nSome submissions failed. Check errors above.")
        sys.exit(1)

    print("\nSubmission complete!")
    sys.exit(0)


if __name__ == "__main__":
    main()
