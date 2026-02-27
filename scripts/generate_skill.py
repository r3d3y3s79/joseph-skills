#!/usr/bin/env python3
"""
Skill Generator - Creates SKILL.md files from templates

Usage:
    python generate_skill.py <category> <skill-name> [config.json]

Examples:
    python generate_skill.py content-creation youtube-script-pro config.json
    python generate_skill.py ecommerce shopify-product-writer
"""
import os
import sys
import json
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

def validate_category(category: str) -> bool:
    """Validate category exists."""
    valid_categories = ["content-creation", "ecommerce", "business", "developer", "marketing"]
    return category in valid_categories

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_skill.py <category> <skill-name> [config.json]")
        print("Categories: content-creation, ecommerce, business, developer, marketing")
        sys.exit(1)

    category = sys.argv[1]
    name = sys.argv[2]
    config_file = sys.argv[3] if len(sys.argv) > 3 else None

    if not validate_category(category):
        print(f"Error: Invalid category '{category}'")
        print("Valid categories: content-creation, ecommerce, business, developer, marketing")
        sys.exit(1)

    if config_file:
        config = json.loads(Path(config_file).read_text())
    else:
        config = {}

    content = generate_skill(category, name, config)
    save_skill(category, name, content)

if __name__ == "__main__":
    main()
