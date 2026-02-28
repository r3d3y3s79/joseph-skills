---
name: migration-guide
description: Use when creating migration or upgrade guides for software, APIs, or frameworks. Helps structure step-by-step migration paths with breaking changes, automated tooling, and rollback procedures.
---

# Migration Guide

## Overview

Create migration guides that help users upgrade safely and confidently. This skill helps you document breaking changes clearly, provide automated migration tools where possible, and include rollback procedures for when things go wrong.

## When to Use

- Major version upgrades
- API version migrations
- Framework or library updates
- Database schema changes
- Infrastructure migrations
- Deprecation sunsets

## Output Structure

```
MIGRATION GUIDE:

# Migrating from [Old] to [New]

## Overview

[What's changing and why. High-level summary.]

## Who Should Migrate

- [User type 1]
- [User type 2]

## Timeline

| Date | Action |
|------|--------|
| [Date] | New version available |
| [Date] | Old version deprecated |
| [Date] | Old version removed |

## Before You Start

### Prerequisites
- [Required version/access]
- [Backup procedure]

### Estimated Time
[Time range based on project complexity]

---

## Quick Migration (Automated)

```bash
[automated migration command if available]
```

---

## Step-by-Step Migration

### Step 1: [Action]

[Details]

### Step 2: [Action]

[Details]

---

## Breaking Changes

### [Change Name]

**Before:**
```
[old code/config]
```

**After:**
```
[new code/config]
```

**Why:** [Reason for change]

**Migration:** [Specific steps]

---

## Troubleshooting

### [Common issue]
[Solution]

---

## Rollback Procedure

[How to undo the migration if needed]

---

## Getting Help

[Support channels]
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Timeline | Clear dates for deprecation and removal |
| Prerequisites | What to backup, verify before starting |
| Automated tools | Provide scripts when possible |
| Breaking changes | Before/after with migration steps |
| Rollback | Always include escape hatch |
| Testing | How to verify migration success |

## Migration Types

### API Migration

Focus on:
- Endpoint changes
- Request/response format
- Authentication changes
- Rate limit changes

### Framework Migration

Focus on:
- Package updates
- Import changes
- API/syntax changes
- Configuration changes

### Database Migration

Focus on:
- Schema changes
- Data transformation
- Downtime requirements
- Backup/restore

### Infrastructure Migration

Focus on:
- Environment changes
- Configuration
- Deployment changes
- DNS/routing

## Common Mistakes

- **No timeline**: Users don't know urgency
- **Missing rollback**: What if it fails?
- **Vague changes**: "Updated API" helps no one
- **No automation**: Manual steps cause errors
- **Missing testing**: How to verify success?
- **Incomplete examples**: Show real before/after

## Examples

### Example 1: API Version Migration

**Input**: Create a migration guide from API v2 to v3 with authentication and response format changes

**Output**:
```markdown
# Migrating from API v2 to v3

## Overview

API v3 introduces a simplified authentication model, consistent response formatting, and improved error handling. This guide covers all breaking changes and provides automated migration tools.

## Who Should Migrate

- Anyone using API v2 endpoints (`api.example.com/v2/*`)
- Applications using OAuth token authentication
- Integrations parsing v2 response formats

## Timeline

| Date | Action |
|------|--------|
| March 1, 2024 | API v3 available |
| June 1, 2024 | v2 deprecated (no new features) |
| September 1, 2024 | v2 read-only mode |
| December 1, 2024 | v2 removed |

**Recommended**: Complete migration by August 2024 to allow testing before read-only mode.

## Before You Start

### Prerequisites
- [ ] Admin access to your API dashboard
- [ ] List of all v2 endpoints your application uses
- [ ] Ability to deploy code changes

### Backup
Export your current API configuration:
```bash
curl -H "Authorization: Bearer $API_KEY" \
  https://api.example.com/v2/account/export > backup.json
```

### Estimated Time
- Simple integration (1-5 endpoints): 1-2 hours
- Medium integration (5-20 endpoints): 4-8 hours
- Complex integration (20+ endpoints): 2-3 days

---

## Quick Migration (Automated)

We provide a migration tool that handles most changes automatically:

```bash
npx @example/api-migrate v2-to-v3 \
  --config ./api-config.json \
  --dry-run
```

Remove `--dry-run` to apply changes.

**What the tool does:**
- Updates endpoint URLs from `/v2/` to `/v3/`
- Converts OAuth tokens to API keys
- Transforms response parsing code
- Generates a migration report

---

## Step-by-Step Migration

### Step 1: Generate API Key

API v3 uses API keys instead of OAuth tokens.

1. Go to Dashboard > Settings > API Keys
2. Click "Generate New Key"
3. Select scopes matching your OAuth permissions
4. Copy the key (starts with `sk_live_` or `sk_test_`)

```bash
# Old (OAuth)
export API_TOKEN="oauth_xxxxx"

# New (API Key)
export API_KEY="sk_live_xxxxx"
```

### Step 2: Update Base URL

Change all API calls from v2 to v3:

```diff
- https://api.example.com/v2/users
+ https://api.example.com/v3/users
```

### Step 3: Update Authentication Header

```diff
- Authorization: Bearer oauth_xxxxx
+ Authorization: Bearer sk_live_xxxxx
```

### Step 4: Update Response Parsing

v3 wraps all responses in a `data` object:

```diff
- const users = response;
+ const users = response.data;
```

### Step 5: Update Error Handling

v3 uses consistent error format:

```javascript
// v3 error response
{
  "error": {
    "code": "NOT_FOUND",
    "message": "User not found",
    "details": { "user_id": "usr_123" }
  }
}
```

```javascript
// Update error handling
try {
  const response = await fetch(url);
  const data = await response.json();

  if (!response.ok) {
    // v3 error format
    throw new Error(data.error.message);
  }

  return data.data;
} catch (error) {
  console.error('API error:', error.message);
}
```

### Step 6: Verify Migration

Run the verification script:

```bash
npx @example/api-migrate verify \
  --config ./api-config.json
```

Expected output:
```
Checking authentication... OK
Checking endpoints... OK
Checking response parsing... OK
Migration verified successfully!
```

---

## Breaking Changes

### Authentication: OAuth to API Keys

**Before (v2):**
```bash
curl -H "Authorization: Bearer oauth_abc123" \
  https://api.example.com/v2/users
```

**After (v3):**
```bash
curl -H "Authorization: Bearer sk_live_xyz789" \
  https://api.example.com/v3/users
```

**Why:** API keys are simpler to manage, don't expire, and support fine-grained scopes.

**Migration:**
1. Generate API key in Dashboard
2. Map OAuth scopes to API key scopes:
   - `read:users` → `users:read`
   - `write:users` → `users:write`

---

### Response Format: Array to Object Wrapper

**Before (v2):**
```json
[
  { "id": "usr_1", "name": "Alice" },
  { "id": "usr_2", "name": "Bob" }
]
```

**After (v3):**
```json
{
  "data": [
    { "id": "usr_1", "name": "Alice" },
    { "id": "usr_2", "name": "Bob" }
  ],
  "pagination": {
    "has_more": false,
    "total": 2
  }
}
```

**Why:** Consistent structure allows pagination metadata on all list endpoints.

**Migration:**
```diff
- const users = await response.json();
+ const { data: users } = await response.json();
```

---

### Timestamps: Unix to ISO 8601

**Before (v2):**
```json
{ "created_at": 1709294400 }
```

**After (v3):**
```json
{ "created_at": "2024-03-01T12:00:00Z" }
```

**Why:** ISO 8601 is human-readable and timezone-aware.

**Migration:**
```javascript
// v2: Unix timestamp
const date = new Date(created_at * 1000);

// v3: ISO string (no change needed)
const date = new Date(created_at);
```

---

### Removed Endpoints

| v2 Endpoint | v3 Replacement |
|------------|----------------|
| `GET /v2/users/me/settings` | `GET /v3/users/me?include=settings` |
| `POST /v2/batch` | Individual requests (batch removed) |
| `GET /v2/legacy/*` | No replacement (sunset) |

---

## SDK Migration

### JavaScript SDK

```bash
npm uninstall @example/api-v2
npm install @example/api-v3
```

```diff
- import { Client } from '@example/api-v2';
- const client = new Client({ oauthToken: 'xxx' });
+ import { ApiClient } from '@example/api-v3';
+ const client = new ApiClient({ apiKey: 'sk_live_xxx' });
```

### Python SDK

```bash
pip uninstall example-api
pip install example-api>=3.0.0
```

```diff
- from example import Client
- client = Client(oauth_token='xxx')
+ from example import ApiClient
+ client = ApiClient(api_key='sk_live_xxx')
```

---

## Troubleshooting

### "Invalid API key" error

1. Verify key starts with `sk_live_` (production) or `sk_test_` (sandbox)
2. Check key has required scopes for the endpoint
3. Ensure key is not revoked in Dashboard

### "Unexpected response format"

You're probably hitting a v3 endpoint with v2 parsing logic. Look for `.data` wrapper:

```javascript
// Wrong
const users = response;

// Correct
const users = response.data;
```

### "Endpoint not found" (404)

1. Verify URL uses `/v3/` not `/v2/`
2. Check if endpoint was removed (see Removed Endpoints table)
3. Check spelling and case sensitivity

### Rate limiting errors

v3 has different rate limits. Check headers:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 0
Retry-After: 30
```

---

## Rollback Procedure

If you need to revert to v2:

1. **Restore backup configuration:**
   ```bash
   curl -X POST \
     -H "Authorization: Bearer $OLD_OAUTH_TOKEN" \
     -d @backup.json \
     https://api.example.com/v2/account/restore
   ```

2. **Revert code changes:**
   ```bash
   git revert HEAD  # Or revert to your pre-migration commit
   ```

3. **Redeploy previous version**

**Note:** v2 will be read-only after September 1, 2024. Plan final migration before then.

---

## Parallel Running

During migration, you can run v2 and v3 simultaneously:

```javascript
const API_VERSION = process.env.USE_V3 ? 'v3' : 'v2';
const BASE_URL = `https://api.example.com/${API_VERSION}`;

// Gradually roll out via feature flag
```

---

## Getting Help

- **Documentation:** https://docs.example.com/v3
- **Migration FAQ:** https://docs.example.com/v3/migration-faq
- **Support:** support@example.com
- **Status:** https://status.example.com
```

### Example 2: Framework Migration

**Input**: Create a migration guide for upgrading a React application from 17 to 18

**Output**:
```markdown
# Migrating React 17 to React 18

## Overview

React 18 introduces concurrent rendering, automatic batching, and new hooks. Most applications can upgrade with minimal changes. This guide covers breaking changes and new features.

## Who Should Migrate

- Applications running React 17.x
- Projects using Create React App, Next.js, or custom builds

## Timeline

| Version | Status |
|---------|--------|
| React 17 | Maintenance mode (security fixes only) |
| React 18 | Current stable |
| React 19 | In development |

**Recommendation:** Migrate now to access new features and ensure long-term support.

## Before You Start

### Prerequisites
- [ ] Node.js 14+ (Node 18+ recommended)
- [ ] Current codebase committed to git
- [ ] Test suite passing

### Compatibility Check

Run our compatibility checker:
```bash
npx react-upgrade-check
```

This identifies:
- Deprecated API usage
- Strict mode violations
- Potential concurrent rendering issues

### Estimated Time

- Small app (<50 components): 1-2 hours
- Medium app (50-200 components): 4-8 hours
- Large app (200+ components): 1-2 days

---

## Quick Migration

### Step 1: Update Dependencies

```bash
npm install react@18 react-dom@18

# Or with yarn
yarn add react@18 react-dom@18
```

### Step 2: Update Root Rendering

This is the only required change for most apps.

**Before (React 17):**
```jsx
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

**After (React 18):**
```jsx
import { createRoot } from 'react-dom/client';
import App from './App';

const root = createRoot(document.getElementById('root'));
root.render(<App />);
```

### Step 3: Run Tests

```bash
npm test
```

If tests pass, you're done with the basic migration!

---

## Breaking Changes

### ReactDOM.render Deprecated

**Status:** Warning in React 18, will be removed in React 19.

**Before:**
```jsx
import ReactDOM from 'react-dom';
ReactDOM.render(<App />, container);
```

**After:**
```jsx
import { createRoot } from 'react-dom/client';
createRoot(container).render(<App />);
```

**For hydration (SSR):**
```jsx
// Before
ReactDOM.hydrate(<App />, container);

// After
import { hydrateRoot } from 'react-dom/client';
hydrateRoot(container, <App />);
```

---

### Automatic Batching Changes

React 18 batches all state updates, including those in promises and timeouts.

**React 17 behavior:**
```jsx
setTimeout(() => {
  setCount(c => c + 1); // Re-render
  setFlag(f => !f);     // Re-render
  // Total: 2 re-renders
}, 1000);
```

**React 18 behavior:**
```jsx
setTimeout(() => {
  setCount(c => c + 1);
  setFlag(f => !f);
  // Total: 1 re-render (batched)
}, 1000);
```

**If you need synchronous updates (rare):**
```jsx
import { flushSync } from 'react-dom';

setTimeout(() => {
  flushSync(() => setCount(c => c + 1)); // Re-render now
  flushSync(() => setFlag(f => !f));     // Re-render now
}, 1000);
```

---

### Strict Mode Double Rendering

React 18 Strict Mode mounts components twice in development to catch issues.

**Symptoms:**
- `useEffect` runs twice
- `console.log` appears twice
- Network requests fire twice

**Solution:** Ensure effects handle cleanup properly:

```jsx
// Wrong: No cleanup
useEffect(() => {
  fetchData();
}, []);

// Correct: With cleanup
useEffect(() => {
  let cancelled = false;

  fetchData().then(data => {
    if (!cancelled) setData(data);
  });

  return () => { cancelled = true; };
}, []);
```

**This is intentional** and only happens in development. Production behavior is unchanged.

---

### Removed: ReactDOM.unmountComponentAtNode

**Before:**
```jsx
ReactDOM.unmountComponentAtNode(container);
```

**After:**
```jsx
root.unmount();
```

---

## TypeScript Updates

Update type definitions:
```bash
npm install @types/react@18 @types/react-dom@18
```

### Updated Types

```typescript
// Children prop no longer implicit
// Before
interface Props {
  title: string;
}

// After (if component accepts children)
import { PropsWithChildren } from 'react';
interface Props {
  title: string;
}
function Component({ title, children }: PropsWithChildren<Props>) {}

// Or explicitly
interface Props {
  title: string;
  children?: React.ReactNode;
}
```

---

## Third-Party Library Compatibility

Check your dependencies support React 18:

| Library | React 18 Support |
|---------|-----------------|
| react-router v6 | Yes |
| react-router v5 | Yes (upgrade to v6 recommended) |
| redux | Yes |
| react-query v4 | Yes |
| formik | Yes |
| styled-components | Yes (v5.3+) |

Run compatibility check:
```bash
npx npm-check-updates --filter "/react/" --peer
```

---

## New Features to Adopt

### useTransition Hook

Mark slow updates as non-urgent:

```jsx
import { useTransition } from 'react';

function SearchResults({ query }) {
  const [isPending, startTransition] = useTransition();
  const [results, setResults] = useState([]);

  function handleChange(e) {
    // Urgent: update input
    setQuery(e.target.value);

    // Non-urgent: update results
    startTransition(() => {
      setResults(filterResults(e.target.value));
    });
  }

  return (
    <>
      <input onChange={handleChange} />
      {isPending ? <Spinner /> : <ResultsList results={results} />}
    </>
  );
}
```

### useDeferredValue Hook

Defer updating expensive components:

```jsx
import { useDeferredValue } from 'react';

function App() {
  const [text, setText] = useState('');
  const deferredText = useDeferredValue(text);

  return (
    <>
      <input value={text} onChange={e => setText(e.target.value)} />
      <SlowList text={deferredText} />
    </>
  );
}
```

---

## Troubleshooting

### "ReactDOM.render is no longer supported"

Update to the new root API:
```jsx
import { createRoot } from 'react-dom/client';
const root = createRoot(container);
root.render(<App />);
```

### Tests failing with act() warnings

Update React Testing Library:
```bash
npm install @testing-library/react@latest
```

### "Cannot update a component while rendering"

This error is now enforced. Move state updates out of render:
```jsx
// Wrong
function Component() {
  const [count, setCount] = useState(0);
  setCount(1); // Error!
  return <div>{count}</div>;
}

// Correct
function Component() {
  const [count, setCount] = useState(0);
  useEffect(() => {
    setCount(1);
  }, []);
  return <div>{count}</div>;
}
```

---

## Rollback Procedure

If critical issues arise:

```bash
# Revert to React 17
npm install react@17 react-dom@17

# Revert code changes
git checkout HEAD~1 -- src/index.js

# Restore previous types
npm install @types/react@17 @types/react-dom@17
```

---

## Getting Help

- **Official Upgrade Guide:** https://react.dev/blog/2022/03/08/react-18-upgrade-guide
- **React Working Group:** https://github.com/reactwg/react-18/discussions
- **Stack Overflow:** Tag questions with `react-18`
```

### Example 3: Database Migration

**Input**: Create a migration guide for moving from MySQL to PostgreSQL

**Output**:
```markdown
# Migrating from MySQL to PostgreSQL

## Overview

This guide covers migrating your MySQL database to PostgreSQL, including schema conversion, data migration, and application code changes. PostgreSQL offers better JSON support, more SQL standards compliance, and stronger data integrity.

## Who Should Migrate

- Applications currently running MySQL 5.7 or 8.0
- Teams seeking improved JSON operations
- Projects requiring advanced data types (arrays, ranges)

## Timeline

| Phase | Duration |
|-------|----------|
| Assessment | 1-2 days |
| Schema migration | 1-3 days |
| Data migration | Hours to days (data dependent) |
| Application updates | 2-5 days |
| Testing | 3-5 days |
| Cutover | 1 day |

**Total:** 2-4 weeks for medium-sized databases

## Before You Start

### Prerequisites
- [ ] PostgreSQL 14+ installed
- [ ] MySQL backup completed
- [ ] Application code in version control
- [ ] Staging environment available

### Required Access
- MySQL: SELECT permissions on all tables
- PostgreSQL: CREATE DATABASE, CREATE TABLE permissions

### Backup MySQL Database

```bash
mysqldump -u root -p \
  --single-transaction \
  --routines \
  --triggers \
  --databases myapp > mysql_backup.sql
```

### Estimated Downtime

| Database Size | Estimated Downtime |
|---------------|-------------------|
| < 1 GB | < 1 hour |
| 1-10 GB | 1-4 hours |
| 10-100 GB | 4-12 hours |
| > 100 GB | Consider live migration |

---

## Quick Migration (Automated)

Use pgLoader for automated migration:

```bash
# Install pgLoader
apt install pgloader

# Create target database
createdb myapp_postgres

# Run migration
pgloader mysql://user:pass@localhost/myapp \
         postgresql://user:pass@localhost/myapp_postgres
```

pgLoader handles:
- Schema conversion
- Data type mapping
- Index recreation
- Foreign key constraints

**After pgLoader, proceed to "Verify Migration" section.**

---

## Step-by-Step Migration

### Step 1: Export MySQL Schema

```bash
mysqldump -u root -p \
  --no-data \
  --routines \
  myapp > schema.sql
```

### Step 2: Convert Schema

Common MySQL to PostgreSQL conversions:

| MySQL | PostgreSQL |
|-------|------------|
| `INT AUTO_INCREMENT` | `SERIAL` or `INT GENERATED ALWAYS AS IDENTITY` |
| `TINYINT(1)` | `BOOLEAN` |
| `DATETIME` | `TIMESTAMP` |
| `TEXT` | `TEXT` (same) |
| `DOUBLE` | `DOUBLE PRECISION` |
| `ENUM('a','b')` | Create TYPE or use CHECK constraint |
| `JSON` | `JSONB` (binary, faster) |

**Example conversions:**

```sql
-- MySQL
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  active TINYINT(1) DEFAULT 1,
  metadata JSON,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- PostgreSQL
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  active BOOLEAN DEFAULT TRUE,
  metadata JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Step 3: Create PostgreSQL Database

```bash
# Create database
createdb myapp

# Apply converted schema
psql myapp < schema_postgres.sql
```

### Step 4: Export Data from MySQL

```bash
# Export each table as CSV
mysql -u root -p myapp -e "SELECT * FROM users" \
  | sed 's/\t/,/g' > users.csv
```

Or use a migration script:

```python
import mysql.connector
import psycopg2
import csv

# Connect to both databases
mysql_conn = mysql.connector.connect(
    host='localhost', database='myapp',
    user='root', password='password'
)
pg_conn = psycopg2.connect(
    host='localhost', database='myapp',
    user='postgres', password='password'
)

# Migrate table
mysql_cur = mysql_conn.cursor()
pg_cur = pg_conn.cursor()

mysql_cur.execute("SELECT * FROM users")
rows = mysql_cur.fetchall()

for row in rows:
    pg_cur.execute(
        "INSERT INTO users (id, email, active, created_at) VALUES (%s, %s, %s, %s)",
        row
    )

pg_conn.commit()
```

### Step 5: Reset Sequences

After importing data, reset auto-increment sequences:

```sql
SELECT setval('users_id_seq', (SELECT MAX(id) FROM users));
SELECT setval('orders_id_seq', (SELECT MAX(id) FROM orders));
```

---

## Breaking Changes

### Query Syntax Differences

#### String Concatenation

```sql
-- MySQL
SELECT CONCAT(first_name, ' ', last_name) FROM users;

-- PostgreSQL (also works)
SELECT CONCAT(first_name, ' ', last_name) FROM users;
-- Or use ||
SELECT first_name || ' ' || last_name FROM users;
```

#### LIMIT/OFFSET

```sql
-- MySQL
SELECT * FROM users LIMIT 10, 20;  -- offset, limit

-- PostgreSQL
SELECT * FROM users LIMIT 20 OFFSET 10;  -- limit, offset
```

#### Case Sensitivity

```sql
-- MySQL (case-insensitive by default)
SELECT * FROM users WHERE email = 'USER@EXAMPLE.COM';

-- PostgreSQL (case-sensitive)
SELECT * FROM users WHERE LOWER(email) = LOWER('USER@EXAMPLE.COM');
-- Or use ILIKE
SELECT * FROM users WHERE email ILIKE 'USER@EXAMPLE.COM';
```

#### GROUP BY

PostgreSQL requires all non-aggregated columns in GROUP BY:

```sql
-- MySQL (allows this)
SELECT name, COUNT(*) FROM users GROUP BY country;

-- PostgreSQL (requires)
SELECT name, country, COUNT(*) FROM users GROUP BY name, country;
-- Or use aggregates
SELECT MAX(name), country, COUNT(*) FROM users GROUP BY country;
```

---

### Function Differences

| MySQL | PostgreSQL |
|-------|------------|
| `NOW()` | `NOW()` (same) |
| `CURDATE()` | `CURRENT_DATE` |
| `DATE_FORMAT(d, '%Y-%m')` | `TO_CHAR(d, 'YYYY-MM')` |
| `IFNULL(a, b)` | `COALESCE(a, b)` |
| `IF(cond, a, b)` | `CASE WHEN cond THEN a ELSE b END` |
| `RAND()` | `RANDOM()` |
| `AUTO_INCREMENT` | `SERIAL` |

---

### ORM/Driver Changes

#### Node.js

```bash
npm uninstall mysql2
npm install pg
```

```javascript
// Before (mysql2)
const mysql = require('mysql2/promise');
const conn = await mysql.createConnection({
  host: 'localhost',
  user: 'root',
  database: 'myapp'
});
const [rows] = await conn.execute('SELECT * FROM users WHERE id = ?', [1]);

// After (pg)
const { Pool } = require('pg');
const pool = new Pool({
  host: 'localhost',
  user: 'postgres',
  database: 'myapp'
});
const { rows } = await pool.query('SELECT * FROM users WHERE id = $1', [1]);
```

**Key difference:** PostgreSQL uses `$1, $2, $3` for parameters, not `?`.

#### Python

```bash
pip uninstall mysql-connector-python
pip install psycopg2-binary
```

```python
# Before (mysql)
import mysql.connector
conn = mysql.connector.connect(host='localhost', database='myapp')
cursor.execute("SELECT * FROM users WHERE id = %s", (1,))

# After (psycopg2)
import psycopg2
conn = psycopg2.connect(host='localhost', database='myapp')
cursor.execute("SELECT * FROM users WHERE id = %s", (1,))  # Same syntax!
```

---

## Verify Migration

### Row Count Comparison

```sql
-- MySQL
SELECT 'users' as tbl, COUNT(*) FROM users
UNION SELECT 'orders', COUNT(*) FROM orders;

-- PostgreSQL
SELECT 'users' as tbl, COUNT(*) FROM users
UNION SELECT 'orders', COUNT(*) FROM orders;
```

Compare counts match.

### Data Integrity Check

```sql
-- Check for NULL constraint violations
SELECT * FROM users WHERE email IS NULL;

-- Check foreign key integrity
SELECT o.* FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE u.id IS NULL;
```

### Application Smoke Test

1. Run application against PostgreSQL
2. Execute key user flows
3. Verify data displays correctly
4. Check write operations succeed

---

## Troubleshooting

### "Column does not exist"

PostgreSQL identifiers are case-sensitive when quoted:

```sql
-- This creates lowercase column
CREATE TABLE users ("Email" VARCHAR(255));

-- This fails
SELECT email FROM users;

-- This works
SELECT "Email" FROM users;
```

**Fix:** Use lowercase, unquoted identifiers.

### "Syntax error near LIMIT"

Update LIMIT syntax:
```sql
-- Wrong (MySQL style)
LIMIT 10, 20

-- Correct (PostgreSQL)
LIMIT 20 OFFSET 10
```

### "Type boolean cannot be compared"

```sql
-- Wrong
WHERE active = 1

-- Correct
WHERE active = TRUE
```

---

## Rollback Procedure

### During Migration (before cutover)

1. Stop migration process
2. Drop PostgreSQL database: `dropdb myapp`
3. Application continues using MySQL

### After Cutover

1. Stop application
2. Point application back to MySQL connection
3. Restore MySQL backup if needed
4. Restart application

```bash
# Update connection string
export DATABASE_URL="mysql://user:pass@localhost/myapp"

# Restart
systemctl restart myapp
```

---

## Post-Migration Optimization

### Add PostgreSQL-Specific Indexes

```sql
-- GIN index for JSONB
CREATE INDEX idx_users_metadata ON users USING GIN (metadata);

-- Partial index
CREATE INDEX idx_active_users ON users (email) WHERE active = TRUE;
```

### Analyze Tables

```sql
ANALYZE users;
ANALYZE orders;
```

---

## Getting Help

- **pgLoader docs:** https://pgloader.io
- **PostgreSQL wiki:** https://wiki.postgresql.org/wiki/Converting_from_other_Databases_to_PostgreSQL
- **Stack Overflow:** Tag with `mysql-to-postgresql`
```

## Quality Checklist

- [ ] Timeline includes deprecation and removal dates
- [ ] Prerequisites clearly stated
- [ ] Backup procedure documented
- [ ] Automated migration tool provided (if possible)
- [ ] All breaking changes have before/after examples
- [ ] Migration steps are numbered and testable
- [ ] Rollback procedure is complete
- [ ] Troubleshooting covers common issues
- [ ] Verification steps included
- [ ] Support channels listed
