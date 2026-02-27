# Project Memory - Joseph Skills Pipeline

## Overview
- **Purpose**: Automated Claude Code skills creation and distribution pipeline
- **Free Tier**: 50+ skills on SkillsMP/SkillHub (auto-indexed from GitHub)
- **Premium Tier**: "Content Empire Pro" ($97) on Gumroad
- **Tech Stack**: Python, GitHub Actions, Playwright MCP, superpowers-chrome

## Key Paths
- Plan: `docs/plans/2026-02-28-automated-skills-pipeline.md`
- Free skills: `free/{category}/{skill-name}/SKILL.md`
- Premium skills: `premium/`
- Scripts: `scripts/`
- CI/CD: `.github/workflows/`

## Commands
- `python scripts/validate_skill.py <path>` - Validate skill quality (8.5+ required)
- `python scripts/generate_skill.py <category> <name>` - Generate skill from template
- `python scripts/package_premium.py` - Create premium ZIP for Gumroad
- `npx agent-skills-cli submit-repo <repo>` - Submit to SkillsMP

## Architecture
- GitHub as source of truth, auto-indexes to free marketplaces
- Quality gate: All skills must score 8.5+ before merge
- Browser automation (Playwright/Chrome MCP) for Gumroad submissions
- Template-based skill generation for consistency

## Quality Standards
- Minimum score: 8.5/10
- Required sections: When to Use, Output Structure, Quality Checklist, Anti-Patterns, Examples (3+)
- Banned patterns: "premium quality", "high-quality", "world-class", "cutting-edge", "leverage", "synergy"
- Word count target: 800-1500 words per skill

## Session Notes
- Last updated: 2026-02-28
- Initial pipeline design and plan created
- Browser automation discovered as solution for full Gumroad automation
- Free + Premium upsell strategy chosen over premium-only
