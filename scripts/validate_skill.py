#!/usr/bin/env python3
"""
Skill Validator - Ensures skills meet quality standards (8.5+ score)

Usage:
    python validate_skill.py <path/to/SKILL.md>

Exit codes:
    0 - Skill passes validation (8.5+ score, no critical errors)
    1 - Skill fails validation

Quality scoring:
    - Starts at 10.0
    - Deductions for missing elements, banned patterns
    - Bonuses for comprehensive content
    - Minimum passing score: 8.5
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
    r"(?i)\bleverage\b",
    r"(?i)\bsynergy\b",
    r"(?i)game[- ]changer",
    r"(?i)revolutionary",
    r"(?i)seamlessly",
    r"(?i)unlock your potential",
    r"(?i)take it to the next level",
    r"(?i)empower your",
    r"(?i)transform your",
    r"(?i)elevate your"
]

def validate_frontmatter(content: str) -> tuple:
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

def validate_sections(content: str) -> tuple:
    """Validate required sections exist."""
    errors = []
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in content:
            errors.append(f"Missing required section: {section}")
    return len(errors) == 0, errors

def validate_examples(content: str) -> tuple:
    """Validate at least 3 examples exist."""
    errors = []
    example_count = len(re.findall(r"### Example \d+:", content))
    if example_count < 3:
        errors.append(f"Need 3+ examples, found {example_count}")
    return len(errors) == 0, errors

def validate_banned_patterns(content: str) -> tuple:
    """Check for banned generic patterns."""
    errors = []
    for pattern in BANNED_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            errors.append(f"Banned pattern found: '{matches[0]}'")
    return len(errors) == 0, errors

def validate_checklist(content: str) -> tuple:
    """Ensure quality checklist has items."""
    errors = []
    checklist_match = re.search(r"## Quality Checklist(.*?)##", content, re.DOTALL)
    if checklist_match:
        checklist_items = re.findall(r"- \[ \]", checklist_match.group(1))
        if len(checklist_items) < 3:
            errors.append(f"Quality Checklist needs 3+ items, found {len(checklist_items)}")
    return len(errors) == 0, errors

def validate_antipatterns(content: str) -> tuple:
    """Ensure anti-patterns section has items."""
    errors = []
    antipattern_match = re.search(r"## Anti-Patterns(.*?)(?:##|$)", content, re.DOTALL)
    if antipattern_match:
        items = re.findall(r"^- ", antipattern_match.group(1), re.MULTILINE)
        if len(items) < 3:
            errors.append(f"Anti-Patterns needs 3+ items, found {len(items)}")
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

    _, checklist_errors = validate_checklist(content)
    score -= len(checklist_errors) * 0.3

    _, antipattern_errors = validate_antipatterns(content)
    score -= len(antipattern_errors) * 0.3

    # Bonus for length (comprehensive skills)
    word_count = len(content.split())
    if word_count >= 800:
        score += 0.5
    if word_count >= 1200:
        score += 0.5

    # Bonus for detailed examples (look for code blocks, output structure)
    code_blocks = len(re.findall(r"```", content)) // 2
    if code_blocks >= 3:
        score += 0.3

    return max(0, min(10, score))

def validate_skill(path: Path) -> tuple:
    """Full validation of a skill file."""
    if not path.exists():
        return False, 0.0, [f"File not found: {path}"]

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

    _, e = validate_checklist(content)
    errors.extend(e)

    _, e = validate_antipatterns(content)
    errors.extend(e)

    score = calculate_score(content)
    passed = score >= 8.5 and len(errors) == 0

    return passed, score, errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_skill.py <path/to/SKILL.md>")
        print("\nValidates skill files against quality standards.")
        print("Exit code 0 = PASS (8.5+ score), 1 = FAIL")
        sys.exit(1)

    path = Path(sys.argv[1])
    passed, score, errors = validate_skill(path)

    print(f"File: {path}")
    print(f"Score: {score:.1f}/10")
    print(f"Status: {'PASS' if passed else 'FAIL'}")

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  - {e}")

    word_count = len(path.read_text().split()) if path.exists() else 0
    print(f"\nWord count: {word_count}")

    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()
