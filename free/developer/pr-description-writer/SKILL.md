---
name: pr-description-writer
description: Use when creating pull request descriptions for code changes. Helps write clear, reviewable PR descriptions with context, changes summary, testing notes, and screenshots.
---

# PR Description Writer

## Overview

Create pull request descriptions that make code review faster and more effective. This skill helps you communicate the what, why, and how of your changes so reviewers can provide meaningful feedback quickly.

## When to Use

- Opening new pull requests
- Updating PR descriptions after changes
- Creating PR templates for teams
- Documenting complex refactors
- Explaining breaking changes

## Output Structure

```
PR DESCRIPTION:

## Title
[type]: [brief description] (max 72 chars)

---

## Summary

[2-3 sentences explaining WHAT changed and WHY]

## Changes

### [Category 1]
- [Specific change]
- [Specific change]

### [Category 2]
- [Specific change]
- [Specific change]

## Type of Change

- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Refactor (no functional changes)
- [ ] Documentation update
- [ ] Performance improvement

## How to Test

1. [Step-by-step testing instructions]
2. [Include specific inputs/expected outputs]
3. [Edge cases to verify]

## Screenshots / Recordings

[If UI changes, include before/after screenshots]

## Related Issues

- Closes #[issue_number]
- Related to #[issue_number]

## Checklist

- [ ] Tests pass locally
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated (if needed)
- [ ] No console errors or warnings

## Notes for Reviewers

[Specific areas to focus on, questions for reviewers, deployment notes]
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Title | Use conventional commits: feat:, fix:, refactor: |
| Summary | Answer "what" and "why" in 2-3 sentences |
| Changes | Group by feature/area, use bullet points |
| Testing | Step-by-step, not "run tests" |
| Screenshots | Before/after for any UI changes |
| Issues | Use "Closes #X" to auto-close |
| Notes | Guide reviewers to tricky areas |

## PR Types

### Bug Fix PR

Focus on:
- What was broken
- Root cause
- How this fixes it
- How to verify the fix

### Feature PR

Focus on:
- What capability this adds
- User-facing changes
- API changes (if any)
- Migration/rollout plan

### Refactor PR

Focus on:
- Why refactoring was needed
- What improved (readability, performance, etc.)
- Proof that behavior unchanged
- Before/after comparisons

### Breaking Change PR

Focus on:
- What breaks
- Migration path
- Deprecation timeline
- Affected users/systems

## Common Mistakes

- **No "why"**: "Fixed bug" vs "Fixed race condition that caused duplicate orders"
- **Too vague**: "Updated code" tells reviewers nothing
- **No test steps**: "Test it" is not helpful
- **Missing context**: Reviewers shouldn't need to guess intent
- **Giant PRs**: If you need 20 bullet points, split the PR
- **No screenshots**: UI changes without visuals slow reviews

## Examples

### Example 1: Bug Fix PR

**Input**: Write a PR description for fixing a race condition in order processing

**Output**:
```
## fix: prevent duplicate orders from race condition in checkout

---

## Summary

Fixes a race condition where rapid double-clicks on the checkout button could create duplicate orders. Added idempotency key validation and optimistic locking to prevent concurrent order creation.

## Changes

### Order Service
- Added idempotency key check before order creation
- Implemented optimistic locking on cart checkout
- Added database unique constraint on idempotency_key

### Checkout Controller
- Generate idempotency key client-side on page load
- Disable submit button immediately on click
- Return existing order if idempotency key matches

### Tests
- Added integration test for concurrent checkout attempts
- Added unit tests for idempotency validation

## Type of Change

- [x] Bug fix (non-breaking change fixing an issue)

## How to Test

1. Checkout flow (happy path):
   - Add item to cart, proceed to checkout
   - Complete payment
   - Verify single order created

2. Double-click prevention:
   - Open browser devtools Network tab
   - Enable "Slow 3G" throttling
   - Click checkout button rapidly 5+ times
   - Verify only ONE order created in database

3. Concurrent request test:
   ```bash
   # Run included test
   npm run test:integration -- --grep "concurrent checkout"
   ```

## Related Issues

- Closes #1234
- Related to #1180 (initial report from customer)

## Checklist

- [x] Tests pass locally
- [x] Code follows project style guidelines
- [x] Self-review completed
- [x] Database migration tested locally
- [x] No console errors or warnings

## Notes for Reviewers

- Please review the locking strategy in `OrderService.createOrder()` (line 45-67)
- I chose optimistic locking over pessimistic because our checkout volume doesn't warrant the performance hit
- Migration is backward-compatible; idempotency_key column allows NULL for existing orders
```

### Example 2: Feature PR

**Input**: Write a PR description for adding dark mode support

**Output**:
```
## feat: add dark mode with system preference detection

---

## Summary

Adds dark mode support across the entire application. Users can toggle between light/dark/system in settings. System preference detection enables automatic switching based on OS settings.

## Changes

### Theme System
- Created ThemeProvider context with light/dark/system modes
- Added CSS custom properties for all color tokens
- Implemented prefers-color-scheme media query detection

### Components Updated
- Header: updated for theme-aware styling
- Sidebar: added dark variants
- Cards: adjusted shadows and borders
- Forms: updated input/button colors
- Modal: backdrop and content colors

### Settings Page
- Added theme selector with preview
- Persists preference to localStorage
- Shows current system preference

### CSS Architecture
- Moved from hardcoded colors to CSS variables
- Created `_themes.scss` with light/dark palettes
- Added smooth transition on theme switch

## Type of Change

- [x] New feature (non-breaking change adding functionality)

## How to Test

1. Theme toggle:
   - Go to Settings > Appearance
   - Select "Dark" - verify all pages are dark
   - Select "Light" - verify all pages are light
   - Select "System" - should match OS setting

2. System preference:
   - Set theme to "System"
   - Change OS to dark mode
   - App should switch without refresh

3. Persistence:
   - Set theme to "Dark"
   - Refresh page
   - Theme should remain dark

4. Component check (spot check these pages):
   - Dashboard
   - Profile settings
   - Order history
   - Checkout flow

## Screenshots

### Light Mode
[screenshot of dashboard in light mode]

### Dark Mode
[screenshot of dashboard in dark mode]

### Theme Selector
[screenshot of settings page with theme options]

## Related Issues

- Closes #892
- Closes #901 (accessibility contrast request)

## Checklist

- [x] Tests pass locally
- [x] Tested in Chrome, Firefox, Safari
- [x] Tested on mobile viewport
- [x] All components verified
- [x] No FOUC (flash of unstyled content)

## Notes for Reviewers

- CSS variable naming follows the pattern: `--color-{semantic}-{variant}`
- I left some commented code in `_themes.scss` for potential future "dim" mode
- The transition duration (200ms) can be adjusted in `ThemeProvider.tsx` line 34
- Please check the contrast ratios in dark mode meet WCAG AA
```

### Example 3: Refactor PR

**Input**: Write a PR description for refactoring authentication to use hooks

**Output**:
```
## refactor: migrate auth logic from HOCs to custom hooks

---

## Summary

Refactors authentication from Higher-Order Components (HOCs) to custom hooks for better composability, testing, and TypeScript support. No functional changes - all existing behavior preserved.

## Changes

### New Hooks
- `useAuth()` - returns current user, login/logout functions
- `useRequireAuth()` - redirects if not authenticated
- `usePermissions()` - checks user permissions

### Removed (deprecated)
- `withAuth` HOC - replaced by `useAuth`
- `withRequireAuth` HOC - replaced by `useRequireAuth`
- `AuthContext.Consumer` pattern - use hooks instead

### Migration
- Updated 23 components to use hooks
- Removed HOC wrappers
- Added deprecation warnings to old exports

### Tests
- Added comprehensive hook tests
- Migrated existing HOC tests to hook equivalents
- Added integration tests for auth flows

## Type of Change

- [x] Refactor (no functional changes)

## How to Test

1. All existing auth flows should work identically:
   - Login with valid credentials
   - Login with invalid credentials (error shown)
   - Logout clears session
   - Protected routes redirect to login

2. Run test suite:
   ```bash
   npm run test -- --coverage src/hooks/auth
   ```

3. Verify no runtime warnings in console about deprecated APIs

## Before/After

### Before (HOC pattern)
```jsx
export default withAuth(withRequireAuth(ProfilePage));
```

### After (hooks pattern)
```jsx
function ProfilePage() {
  const { user } = useRequireAuth();
  // ...
}
```

## Related Issues

- Closes #567
- Part of #500 (hooks migration epic)

## Checklist

- [x] Tests pass locally (coverage: 94%)
- [x] All 23 components migrated
- [x] TypeScript types updated
- [x] No console warnings
- [x] Bundle size reduced by 2.3kb

## Notes for Reviewers

- Focus on `useRequireAuth` hook (src/hooks/useRequireAuth.ts) - this has the redirect logic
- I kept the old HOCs exported with deprecation warnings for any external consumers
- The `usePermissions` hook is new but follows the same pattern we discussed in #500
- Let me know if you want me to split this into smaller PRs by component area

## Migration Guide

For teams using our auth HOCs externally:

```jsx
// Old
import { withAuth } from '@company/auth';
export default withAuth(MyComponent);

// New
import { useAuth } from '@company/auth';
function MyComponent() {
  const { user, isLoading } = useAuth();
}
```
```

## Quality Checklist

- [ ] Title follows conventional commit format
- [ ] Summary explains what AND why
- [ ] Changes grouped logically
- [ ] Type of change marked
- [ ] Testing steps are specific and reproducible
- [ ] Screenshots included for UI changes
- [ ] Related issues linked with proper keywords
- [ ] Notes guide reviewers to important areas
- [ ] Breaking changes clearly documented
- [ ] PR is focused (one concern per PR)
