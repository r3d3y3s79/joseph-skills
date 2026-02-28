---
name: changelog-generator
description: Use when creating release changelogs, version history, or release notes. Helps structure changes by category with clear descriptions for users and developers.
---

# Changelog Generator

## Overview

Create changelogs that communicate release value clearly to users and developers. This skill helps you organize changes into meaningful categories, write user-focused descriptions, and maintain consistent changelog formatting.

## When to Use

- Preparing release notes for new versions
- Documenting breaking changes
- Creating user-facing update announcements
- Maintaining CHANGELOG.md files
- Writing migration notes for major versions

## Output Structure

```
CHANGELOG ENTRY:

## [Version] - YYYY-MM-DD

[One-line release summary - what's the headline?]

### Added
- [New feature or capability]
- [New feature or capability]

### Changed
- [Modification to existing functionality]
- [Modification to existing functionality]

### Deprecated
- [Feature that will be removed in future]

### Removed
- [Feature that was removed]

### Fixed
- [Bug that was fixed]
- [Bug that was fixed]

### Security
- [Security vulnerability addressed]

---

### Migration Guide (for breaking changes)

**Breaking Change: [Name]**

Before:
```code
[old usage]
```

After:
```code
[new usage]
```

Why: [Explanation of why this change was made]
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Version | Semantic versioning (MAJOR.MINOR.PATCH) |
| Date | ISO format: YYYY-MM-DD |
| Categories | Keep Changelog standard: Added, Changed, Fixed, etc. |
| Descriptions | User benefit, not technical implementation |
| Breaking changes | Clear migration path with examples |
| Links | Reference issues/PRs: (#123) |
| Order | Most impactful changes first within category |

## Changelog Categories

### Added
New features, capabilities, or options users didn't have before.

### Changed
Modifications to existing behavior. If it's a fix, use Fixed instead.

### Deprecated
Features that still work but will be removed. Include timeline and alternative.

### Removed
Features that were removed. Should have been deprecated first.

### Fixed
Bug fixes. Describe what was broken, not just "fixed bug."

### Security
Security patches. Be specific enough to inform but not exploit.

## Common Mistakes

- **Technical jargon**: "Refactored useEffect" vs "App loads 40% faster"
- **No user impact**: "Updated dependencies" - so what?
- **Vague fixes**: "Fixed bug" vs "Fixed crash when uploading large files"
- **Missing migration**: Breaking changes without upgrade path
- **Wrong category**: Don't put fixes under Changed
- **No context**: Link to issues/PRs for details

## Examples

### Example 1: Minor Release Changelog

**Input**: Write a changelog for v2.4.0 with new export feature, performance improvements, and bug fixes

**Output**:
```
## [2.4.0] - 2024-03-15

Dashboard export is here! Export any dashboard to PDF or CSV with one click.

### Added
- **Dashboard Export**: Export dashboards to PDF or CSV format
  - Includes all visible charts and tables
  - Customizable page layout for PDF
  - Scheduled exports coming in v2.5 (#892)
- Export history page to view and re-download past exports
- Keyboard shortcut `Cmd/Ctrl + E` to quick-export current view

### Changed
- Dashboard loading is now 40% faster through lazy-loading charts
- Chart tooltips show exact values instead of rounded numbers
- Date picker defaults to last 30 days instead of last 7 days

### Fixed
- Fixed crash when filtering by date range spanning multiple years (#1023)
- Fixed chart legend cutoff on mobile devices (#1019)
- Fixed incorrect totals in grouped bar charts when filters applied (#1015)
- Fixed timezone display showing UTC instead of user timezone (#998)

### Security
- Updated `pdf-lib` to address CVE-2024-1234 (moderate severity)

---

### Upgrade Notes

No breaking changes. Run `npm update @company/dashboard` to upgrade.

For the new export feature, users need the `export:read` permission. Add to roles:

```json
{
  "permissions": ["export:read", "export:write"]
}
```
```

### Example 2: Major Release with Breaking Changes

**Input**: Write a changelog for v3.0.0 with new API, removed legacy endpoints, and migration requirements

**Output**:
```
## [3.0.0] - 2024-03-15

Version 3.0 brings a completely redesigned API with better performance, stricter typing, and simplified authentication. This is a major release with breaking changes.

### Added
- **New REST API v3**: Complete redesign with consistent naming and responses
  - All endpoints now return standardized JSON structure
  - Cursor-based pagination for better performance
  - Expanded filtering and sorting options
- TypeScript SDK with full type coverage
- API Explorer in dashboard for testing endpoints
- Webhook event replay for debugging integrations
- Rate limit headers on all responses (`X-RateLimit-*`)

### Changed
- Authentication now uses API keys instead of OAuth tokens
- All timestamps are ISO 8601 format (previously Unix timestamps)
- Error responses include `error_code` for programmatic handling
- List endpoints return `data` array wrapper (previously flat array)
- IDs are now prefixed strings (`usr_abc123`) instead of integers

### Deprecated
- API v2 endpoints: Will be removed on 2024-09-15 (6 months)
- Legacy webhook format: Migrate to v3 format by 2024-06-15

### Removed
- API v1 endpoints (deprecated since 2023-01-01)
- `X-Legacy-Auth` header support
- XML response format
- `/users/me/settings` (use `/users/me` with `?include=settings`)

### Security
- API keys are now hashed at rest (regenerate existing keys)
- Added IP allowlist option for API keys

---

### Migration Guide

**1. Authentication Change**

Before (OAuth):
```bash
curl -H "Authorization: Bearer oauth_token_xxx" \
  https://api.example.com/v2/users
```

After (API Key):
```bash
curl -H "Authorization: Bearer sk_live_xxx" \
  https://api.example.com/v3/users
```

Generate API keys in Dashboard > Settings > API Keys.

**2. Response Format Change**

Before:
```json
[
  {"id": 1, "name": "Alice"},
  {"id": 2, "name": "Bob"}
]
```

After:
```json
{
  "data": [
    {"id": "usr_abc", "name": "Alice"},
    {"id": "usr_def", "name": "Bob"}
  ],
  "pagination": {"cursor": "xxx", "has_more": true}
}
```

**3. Timestamp Format**

Before: `1710505800` (Unix)
After: `2024-03-15T10:30:00Z` (ISO 8601)

Use your language's date parser. Example in JavaScript:
```javascript
const date = new Date(response.created_at);
```

**4. SDK Migration**

```bash
# Remove old SDK
npm uninstall @company/api-sdk

# Install new TypeScript SDK
npm install @company/sdk-v3
```

```typescript
// Old
import { Client } from '@company/api-sdk';
const client = new Client({ oauth: 'token' });

// New
import { ApiClient } from '@company/sdk-v3';
const client = new ApiClient({ apiKey: 'sk_live_xxx' });
```

### Timeline

| Date | Action |
|------|--------|
| 2024-03-15 | v3.0 released |
| 2024-06-15 | Legacy webhooks removed |
| 2024-09-15 | API v2 removed |

Questions? Contact support@example.com or visit our [migration guide](https://docs.example.com/v3-migration).
```

### Example 3: Security Patch Release

**Input**: Write a changelog for v2.3.5 security patch fixing an authentication bypass

**Output**:
```
## [2.3.5] - 2024-03-15

**Security Release**: This version patches a critical authentication vulnerability. Upgrade immediately.

### Security
- **Critical**: Fixed authentication bypass via malformed JWT tokens
  - Affected versions: 2.0.0 - 2.3.4
  - CVE: CVE-2024-5678
  - Severity: Critical (CVSS 9.8)
  - Thanks to @security-researcher for responsible disclosure

### Fixed
- Fixed JWT validation to reject tokens with invalid signatures
- Fixed token expiration check to use server time, not client time

---

### Impact Assessment

**Who is affected?**
All deployments running versions 2.0.0 through 2.3.4.

**What was the vulnerability?**
Attackers could forge authentication tokens by exploiting insufficient signature validation. This allowed unauthorized access to any user account.

**What should you do?**

1. **Upgrade immediately**:
   ```bash
   npm update @company/auth@2.3.5
   ```

2. **Rotate all API keys** in Dashboard > Settings > API Keys

3. **Review access logs** for the past 30 days for suspicious activity:
   ```bash
   grep "authentication" /var/log/app.log | grep -v "success"
   ```

4. **Force password reset** for users with sensitive roles (optional but recommended)

**Indicators of Compromise (IOC)**
- JWT tokens with `alg: none` in logs
- Multiple accounts accessed from single IP
- Access patterns inconsistent with user timezone

### Disclosure Timeline

- 2024-03-10: Vulnerability reported
- 2024-03-11: Confirmed and patch development began
- 2024-03-14: Patch tested
- 2024-03-15: Public release and disclosure

Contact security@example.com for questions.
```

## Quality Checklist

- [ ] Version number follows semantic versioning
- [ ] Date is in YYYY-MM-DD format
- [ ] Changes grouped by correct category
- [ ] Descriptions focus on user impact
- [ ] Breaking changes have migration guide
- [ ] Issues/PRs linked where relevant
- [ ] Security issues include CVE and severity
- [ ] Deprecated items include timeline
- [ ] Most important changes listed first
- [ ] No internal jargon - understandable to users
