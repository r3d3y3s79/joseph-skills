---
name: readme-creator
description: Use when creating README.md files for repositories, packages, or projects. Helps structure documentation with installation, usage, examples, and contribution guidelines.
---

# README Creator

## Overview

Create README files that help users understand, install, and use your project in minutes. This skill helps you write documentation that reduces friction for new users and contributors while showcasing your project's value.

## When to Use

- Starting a new open source project
- Publishing packages to npm/PyPI/etc.
- Documenting internal tools
- Improving existing sparse documentation
- Creating README templates for organizations

## Output Structure

```
README STRUCTURE:

# Project Name

[One-line description - what does this do?]

[Badges: build status, version, license, downloads]

## Features

- [Key feature 1]
- [Key feature 2]
- [Key feature 3]

## Quick Start

```bash
[installation command]
```

```language
[minimal working example]
```

## Installation

[Detailed installation instructions]

## Usage

[Core usage patterns with examples]

## API Reference

[Key methods/functions with signatures]

## Configuration

[Configuration options table or examples]

## Examples

[Real-world usage examples]

## Contributing

[How to contribute]

## License

[License type and link]
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Title | Clear, searchable project name |
| Description | One sentence, no jargon |
| Badges | Build status, version, license |
| Quick Start | Copy-paste to working state |
| Examples | Show, don't just tell |
| API | Signatures + descriptions |
| License | Always include |

## README Patterns

### Library/Package README

Focus on:
- Installation steps
- Import/require syntax
- Core API methods
- Common use cases

### CLI Tool README

Focus on:
- Installation (global)
- Basic commands
- Options/flags table
- Output examples

### Application README

Focus on:
- Prerequisites
- Setup instructions
- Configuration
- Deployment

### Internal Tool README

Focus on:
- What problem it solves
- Who should use it
- How to get access
- Support channels

## Common Mistakes

- **No quick start**: Users leave if they can't try it fast
- **Missing prerequisites**: Don't assume Node/Python/etc. is installed
- **Code without context**: Show what the code does, not just the code
- **Outdated examples**: Test examples before every release
- **Wall of text**: Use headers, lists, code blocks
- **No license**: People won't use unlicensed code

## Examples

### Example 1: NPM Package README

**Input**: Create a README for a TypeScript validation library called "valibot"

**Output**:
```markdown
# Valibot

The modular validation library for TypeScript with bundle size optimization.

[![npm version](https://badge.fury.io/js/valibot.svg)](https://www.npmjs.com/package/valibot)
[![bundle size](https://img.shields.io/bundlephobia/minzip/valibot)](https://bundlephobia.com/package/valibot)
[![TypeScript](https://img.shields.io/badge/TypeScript-Ready-blue.svg)](https://www.typescriptlang.org/)
[![license](https://img.shields.io/npm/l/valibot)](https://github.com/company/valibot/blob/main/LICENSE)

## Features

- **Tiny bundle**: Only import what you use (~1kb for common schemas)
- **Type-safe**: Full TypeScript inference, no manual type annotations
- **Composable**: Build complex schemas from simple pieces
- **Fast**: Optimized for runtime performance
- **Familiar**: API inspired by Zod with better tree-shaking

## Quick Start

```bash
npm install valibot
```

```typescript
import { object, string, email, minLength, parse } from 'valibot';

const UserSchema = object({
  name: string([minLength(2)]),
  email: string([email()]),
});

const user = parse(UserSchema, {
  name: 'Alice',
  email: 'alice@example.com',
});
// => { name: 'Alice', email: 'alice@example.com' }
```

## Installation

```bash
# npm
npm install valibot

# yarn
yarn add valibot

# pnpm
pnpm add valibot
```

**Requirements**: Node.js 16+ or modern browser

## Usage

### Basic Validation

```typescript
import { string, minLength, parse, safeParse } from 'valibot';

const Name = string([minLength(2)]);

// Throws on invalid input
const name = parse(Name, 'Al'); // => 'Al'

// Returns result object
const result = safeParse(Name, 'A');
if (result.success) {
  console.log(result.output);
} else {
  console.log(result.issues);
}
```

### Object Schemas

```typescript
import { object, string, number, optional, parse } from 'valibot';

const ProductSchema = object({
  id: string(),
  name: string(),
  price: number(),
  description: optional(string()),
});

type Product = Output<typeof ProductSchema>;
// { id: string; name: string; price: number; description?: string }
```

### Composing Schemas

```typescript
import { object, array, merge } from 'valibot';

const BaseEntity = object({
  id: string(),
  createdAt: date(),
});

const User = merge([
  BaseEntity,
  object({
    email: string([email()]),
    roles: array(string()),
  }),
]);
```

## API Reference

### Schema Types

| Function | Description | Example |
|----------|-------------|---------|
| `string()` | String values | `string([minLength(1)])` |
| `number()` | Number values | `number([min(0)])` |
| `boolean()` | Boolean values | `boolean()` |
| `object()` | Object shapes | `object({ name: string() })` |
| `array()` | Array of type | `array(string())` |
| `optional()` | Optional field | `optional(string())` |
| `nullable()` | Null allowed | `nullable(string())` |

### Validation Functions

| Function | Description |
|----------|-------------|
| `parse(schema, data)` | Validates and returns typed data. Throws on error. |
| `safeParse(schema, data)` | Returns `{ success, output?, issues? }` |
| `is(schema, data)` | Type guard, returns boolean |

### String Validators

| Validator | Description |
|-----------|-------------|
| `email()` | Valid email format |
| `url()` | Valid URL format |
| `minLength(n)` | Minimum length |
| `maxLength(n)` | Maximum length |
| `regex(pattern)` | Matches regex |

## Configuration

### Custom Error Messages

```typescript
const Name = string([
  minLength(2, 'Name must be at least 2 characters'),
  maxLength(50, 'Name cannot exceed 50 characters'),
]);
```

### Async Validation

```typescript
import { stringAsync, customAsync } from 'valibot';

const UniqueEmail = stringAsync([
  email(),
  customAsync(async (value) => {
    const exists = await checkEmailExists(value);
    return !exists;
  }, 'Email already registered'),
]);
```

## Examples

### Form Validation (React)

```typescript
import { useForm } from 'react-hook-form';
import { valibotResolver } from '@hookform/resolvers/valibot';

const SignupSchema = object({
  email: string([email()]),
  password: string([minLength(8)]),
});

function SignupForm() {
  const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: valibotResolver(SignupSchema),
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('email')} />
      {errors.email && <span>{errors.email.message}</span>}
      {/* ... */}
    </form>
  );
}
```

### API Request Validation

```typescript
import { object, string, parse } from 'valibot';

const CreateUserRequest = object({
  name: string([minLength(1)]),
  email: string([email()]),
});

app.post('/users', (req, res) => {
  try {
    const data = parse(CreateUserRequest, req.body);
    // data is fully typed
    await createUser(data);
    res.json({ success: true });
  } catch (error) {
    res.status(400).json({ error: error.issues });
  }
});
```

## Migration from Zod

| Zod | Valibot |
|-----|---------|
| `z.string()` | `string()` |
| `z.string().email()` | `string([email()])` |
| `z.object({...})` | `object({...})` |
| `schema.parse()` | `parse(schema, data)` |
| `schema.safeParse()` | `safeParse(schema, data)` |

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) first.

```bash
# Setup
git clone https://github.com/company/valibot
cd valibot
npm install

# Run tests
npm test

# Build
npm run build
```

## License

MIT License - see [LICENSE](./LICENSE) for details.
```

### Example 2: CLI Tool README

**Input**: Create a README for a CLI tool that converts markdown to various formats

**Output**:
```markdown
# mdx

Convert Markdown to HTML, PDF, DOCX, and more from the command line.

[![npm](https://img.shields.io/npm/v/mdx-cli)](https://www.npmjs.com/package/mdx-cli)
[![downloads](https://img.shields.io/npm/dm/mdx-cli)](https://www.npmjs.com/package/mdx-cli)

## Features

- **Multiple outputs**: HTML, PDF, DOCX, EPUB
- **Syntax highlighting**: 100+ languages supported
- **Custom templates**: Use your own HTML/CSS
- **Watch mode**: Auto-convert on file changes
- **Batch processing**: Convert entire directories

## Quick Start

```bash
npm install -g mdx-cli

# Convert to HTML
mdx README.md -o readme.html

# Convert to PDF
mdx README.md -o readme.pdf
```

## Installation

```bash
# npm (recommended)
npm install -g mdx-cli

# Homebrew (macOS)
brew install mdx

# Download binary
curl -fsSL https://get.mdx.dev | sh
```

**Requirements**: Node.js 18+ (for npm install)

## Usage

### Basic Conversion

```bash
# Markdown to HTML
mdx input.md -o output.html

# Markdown to PDF
mdx input.md -o output.pdf

# Markdown to DOCX
mdx input.md -o output.docx
```

### Output Format Options

```bash
# Specify format explicitly
mdx input.md --format pdf -o output.pdf

# Multiple outputs
mdx input.md -o output.html -o output.pdf
```

### Watch Mode

```bash
# Watch single file
mdx input.md -o output.html --watch

# Watch directory
mdx docs/ -o build/ --watch
```

### Batch Processing

```bash
# Convert all .md files in directory
mdx docs/*.md -o build/

# Recursive
mdx docs/**/*.md -o build/ --recursive
```

## Options

| Flag | Short | Description | Default |
|------|-------|-------------|---------|
| `--output` | `-o` | Output file or directory | stdout |
| `--format` | `-f` | Output format (html, pdf, docx, epub) | Inferred from -o |
| `--template` | `-t` | Custom HTML template file | Built-in |
| `--style` | `-s` | Custom CSS file | Built-in |
| `--watch` | `-w` | Watch for changes | false |
| `--recursive` | `-r` | Process subdirectories | false |
| `--toc` | | Include table of contents | false |
| `--highlight` | | Syntax highlighting theme | github |
| `--no-header` | | Omit header/metadata | false |
| `--verbose` | `-v` | Verbose output | false |
| `--help` | `-h` | Show help | |
| `--version` | | Show version | |

## Configuration

Create `mdx.config.json` in your project root:

```json
{
  "template": "./templates/custom.html",
  "style": "./styles/custom.css",
  "highlight": "dracula",
  "toc": true,
  "pdf": {
    "format": "A4",
    "margin": "2cm"
  }
}
```

### Custom Templates

```html
<!-- template.html -->
<!DOCTYPE html>
<html>
<head>
  <title>{{title}}</title>
  <style>{{styles}}</style>
</head>
<body>
  {{#if toc}}
  <nav>{{toc}}</nav>
  {{/if}}
  <main>{{content}}</main>
</body>
</html>
```

```bash
mdx input.md -t template.html -o output.html
```

## Examples

### Generate Documentation Site

```bash
# Convert docs folder with table of contents
mdx docs/*.md \
  -o site/ \
  --toc \
  --template docs-template.html \
  --style docs-style.css
```

### Create PDF Report

```bash
mdx report.md \
  -o report.pdf \
  --pdf-format letter \
  --pdf-margin 1in \
  --toc
```

### Watch and Preview

```bash
# Terminal 1: Watch for changes
mdx README.md -o preview.html --watch

# Terminal 2: Serve locally
npx serve .
```

## Troubleshooting

### PDF generation fails

Install system dependencies:

```bash
# macOS
brew install chromium

# Ubuntu
sudo apt install chromium-browser

# Or use puppeteer's bundled chromium
PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=false npm install -g mdx-cli
```

### Syntax highlighting not working

Specify language in code blocks:

````markdown
```javascript
const x = 1;
```
````

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development setup.

## License

MIT
```

### Example 3: Application/Project README

**Input**: Create a README for a self-hosted analytics dashboard

**Output**:
```markdown
# Insight

Self-hosted analytics dashboard for your web applications. Privacy-focused, lightweight, and easy to deploy.

![Dashboard Preview](./docs/images/dashboard-preview.png)

[![Docker](https://img.shields.io/docker/v/insight/insight)](https://hub.docker.com/r/insight/insight)
[![License](https://img.shields.io/github/license/company/insight)](./LICENSE)

## Features

- **Privacy-first**: No cookies, GDPR compliant out of the box
- **Lightweight**: <1KB tracking script, minimal performance impact
- **Self-hosted**: Your data stays on your servers
- **Real-time**: Live visitor count and event stream
- **Simple**: One-line integration, no configuration needed

## Quick Start

### Docker (Recommended)

```bash
docker run -d \
  -p 3000:3000 \
  -v insight-data:/data \
  -e SECRET_KEY=your-secret-key \
  insight/insight:latest
```

Open http://localhost:3000 and create your first site.

### Add Tracking Script

```html
<script defer src="https://your-insight-server.com/script.js"></script>
```

That's it! Pageviews are now being tracked.

## Installation

### Prerequisites

- Docker 20+ or Node.js 18+
- PostgreSQL 14+ (optional, SQLite default)
- 512MB RAM minimum

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  insight:
    image: insight/insight:latest
    ports:
      - '3000:3000'
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - DATABASE_URL=postgres://user:pass@db:5432/insight
    depends_on:
      - db

  db:
    image: postgres:14
    volumes:
      - postgres-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=insight

volumes:
  postgres-data:
```

```bash
docker-compose up -d
```

### Manual Installation

```bash
git clone https://github.com/company/insight
cd insight
npm install
cp .env.example .env
# Edit .env with your settings
npm run build
npm start
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Encryption key (required) | - |
| `DATABASE_URL` | Database connection string | `sqlite:./data/insight.db` |
| `PORT` | Server port | `3000` |
| `BASE_URL` | Public URL for script | Auto-detected |
| `DISABLE_SIGNUP` | Prevent new registrations | `false` |
| `RETENTION_DAYS` | Data retention period | `365` |

### Custom Domain

1. Point your domain to the server
2. Set `BASE_URL=https://analytics.yourdomain.com`
3. Configure SSL (nginx/Caddy recommended)

Example Caddy config:

```
analytics.yourdomain.com {
  reverse_proxy localhost:3000
}
```

## Usage

### Tracking Events

```javascript
// Track custom events
insight.track('signup', { plan: 'pro' });
insight.track('purchase', { amount: 99 });
```

### API Access

```bash
# Get pageviews for last 7 days
curl -H "Authorization: Bearer YOUR_API_KEY" \
  "https://your-server.com/api/stats/pageviews?period=7d"
```

See [API Documentation](./docs/API.md) for full reference.

### Embedding Dashboards

```html
<iframe
  src="https://your-server.com/embed/SITE_ID?theme=dark"
  width="100%"
  height="400"
  frameborder="0"
></iframe>
```

## Deployment

### Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/insight)

### DigitalOcean

[![Deploy to DigitalOcean](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/company/insight)

### Manual (VPS)

See [Deployment Guide](./docs/DEPLOYMENT.md) for detailed instructions.

## Screenshots

| Dashboard | Real-time | Events |
|-----------|-----------|--------|
| ![Dashboard](./docs/images/dashboard.png) | ![Realtime](./docs/images/realtime.png) | ![Events](./docs/images/events.png) |

## Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md).

```bash
# Development setup
git clone https://github.com/company/insight
cd insight
npm install
npm run dev
```

## Support

- [Documentation](https://insight.dev/docs)
- [GitHub Issues](https://github.com/company/insight/issues)
- [Discord Community](https://discord.gg/insight)

## License

AGPL-3.0 - see [LICENSE](./LICENSE)

Self-hosting is free. [Cloud-hosted version](https://insight.dev) available for those who prefer managed hosting.
```

## Quality Checklist

- [ ] Title is clear and searchable
- [ ] One-line description explains what project does
- [ ] Badges show status, version, license
- [ ] Quick start gets to working state fast
- [ ] Prerequisites clearly listed
- [ ] Installation covers all package managers
- [ ] Usage examples are copy-pasteable
- [ ] Configuration options documented
- [ ] API/CLI reference is complete
- [ ] Contributing section exists
- [ ] License is specified
- [ ] Screenshots included for visual projects
