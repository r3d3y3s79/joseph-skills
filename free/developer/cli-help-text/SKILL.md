---
name: cli-help-text
description: Use when writing help text for command-line tools, including usage strings, option descriptions, and man pages. Helps create clear, consistent CLI documentation.
---

# CLI Help Text

## Overview

Write CLI help text that lets users accomplish tasks without consulting external documentation. This skill helps you create clear usage strings, descriptive option help, and well-organized command hierarchies that follow established conventions.

## When to Use

- Building new CLI tools
- Adding help text to commands
- Writing man pages
- Documenting subcommands and options
- Improving existing CLI documentation

## Output Structure

```
CLI HELP TEXT:

## Command Overview

```
USAGE: command [OPTIONS] <ARGS>

DESCRIPTION
  [One-line description of what this command does]

ARGUMENTS
  <arg>    Description of required argument

OPTIONS
  -h, --help       Show this help message
  -v, --version    Show version number

EXAMPLES
  $ command arg           Basic usage
  $ command -o value arg  With options

LEARN MORE
  Documentation: https://example.com/docs
  Report bugs:   https://example.com/issues
```

---

## Subcommand Structure

```
USAGE: tool <COMMAND> [OPTIONS]

COMMANDS
  init        Initialize a new project
  build       Build the project
  deploy      Deploy to production

Run 'tool <command> --help' for command-specific help.
```
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Usage | UPPERCASE for placeholders, lowercase for literals |
| Options | Short (-v) and long (--verbose) forms |
| Required args | Use <angle brackets> |
| Optional args | Use [square brackets] |
| Descriptions | Start with verb, no period |
| Examples | Show realistic usage, not trivial |
| Defaults | Always mention default values |

## Formatting Conventions

### Usage String Syntax

```
Required argument:     <file>
Optional argument:     [file]
Multiple values:       <file>...
Either/or:            <file|directory>
Optional with value:  [--output <file>]
Flag (no value):      [--verbose]
```

### Option Alignment

```
OPTIONS
  -h, --help              Show help message
  -o, --output <file>     Output file path (default: stdout)
  -v, --verbose           Enable verbose output
      --no-color          Disable colored output
```

### Subcommand Hierarchy

```
tool                      # Main command
├── init                  # Subcommand
├── config
│   ├── get <key>        # Nested subcommand
│   └── set <key> <val>
└── help <command>
```

## Common Mistakes

- **Missing examples**: Show don't tell
- **No defaults**: Users don't know what happens without flags
- **Jargon**: Use words users know
- **Too verbose**: Help should be scannable
- **No error guidance**: Tell users how to fix issues
- **Inconsistent format**: Pick a style and stick to it

## Examples

### Example 1: Single Command CLI

**Input**: Write help text for a file encryption CLI tool

**Output**:
```
USAGE
  encrypt [OPTIONS] <file>

DESCRIPTION
  Encrypt files using AES-256-GCM encryption.

ARGUMENTS
  <file>    Path to file to encrypt (use '-' for stdin)

OPTIONS
  -o, --output <path>     Output file path (default: <file>.enc)
  -k, --key <key>         Encryption key (or set ENCRYPT_KEY env var)
  -p, --password          Prompt for password instead of key
  -f, --force             Overwrite output file if it exists
  -d, --decrypt           Decrypt instead of encrypt
      --armor             Output base64-encoded text
  -q, --quiet             Suppress progress output
  -v, --verbose           Show detailed progress
  -h, --help              Show this help message
      --version           Show version number

ENVIRONMENT
  ENCRYPT_KEY    Default encryption key (if --key not provided)

EXAMPLES
  # Encrypt with prompted password
  $ encrypt -p secret.txt
  Enter password: ********
  Created secret.txt.enc

  # Encrypt with key to specific output
  $ encrypt -k "my-secret-key" -o backup.enc data.db

  # Decrypt a file
  $ encrypt -d -p secret.txt.enc

  # Encrypt from stdin, output base64
  $ cat data.json | encrypt -k "$KEY" --armor -

SECURITY NOTES
  - Never pass keys directly on command line in shared environments
  - Use -p (password prompt) or ENCRYPT_KEY environment variable
  - Generated files include authentication tag (tamper detection)

EXIT CODES
  0    Success
  1    Invalid arguments or options
  2    File not found
  3    Encryption/decryption failed
  4    Output file exists (use -f to overwrite)

LEARN MORE
  Full documentation: https://github.com/example/encrypt
  Report issues:      https://github.com/example/encrypt/issues
```

### Example 2: CLI with Subcommands

**Input**: Write help text for a project management CLI with init, build, and deploy commands

**Output**:

**Main Command**:
```
USAGE
  proj <COMMAND> [OPTIONS]

DESCRIPTION
  Project management CLI for building and deploying applications.

COMMANDS
  init        Create a new project
  build       Build project for production
  deploy      Deploy to cloud providers
  config      Manage project configuration
  help        Show help for a command

OPTIONS
  -C, --dir <path>    Run in specified directory (default: .)
  -q, --quiet         Minimal output
  -v, --verbose       Detailed output
      --no-color      Disable colored output
  -h, --help          Show this help message
      --version       Show version number

EXAMPLES
  $ proj init my-app          Create new project
  $ proj build                Build current project
  $ proj deploy --env prod    Deploy to production
  $ proj help deploy          Show deploy command help

CONFIGURATION
  Project settings are stored in proj.config.json
  Global settings: ~/.config/proj/config.json

LEARN MORE
  Documentation: https://proj.dev/docs
  Tutorials:     https://proj.dev/learn
```

**Init Subcommand**:
```
USAGE
  proj init [OPTIONS] <name>

DESCRIPTION
  Create a new project with standard directory structure and config.

ARGUMENTS
  <name>    Project name (creates directory with this name)

OPTIONS
  -t, --template <name>    Project template (default: basic)
                           Options: basic, web, api, library
      --git                Initialize git repository (default)
      --no-git             Skip git initialization
  -f, --force              Overwrite existing directory
  -y, --yes                Accept all defaults (no prompts)
  -h, --help               Show this help message

TEMPLATES
  basic      Minimal setup with config file only
  web        Web application with HTML/CSS/JS structure
  api        REST API with routes and middleware
  library    Publishable library with build config

EXAMPLES
  # Create new project (interactive)
  $ proj init my-app

  # Create API project, accept defaults
  $ proj init -t api -y my-api

  # Create in existing directory
  $ proj init -f .

FILES CREATED
  proj.config.json    Project configuration
  src/                Source code directory
  dist/               Build output (in .gitignore)
  README.md           Project documentation
```

**Build Subcommand**:
```
USAGE
  proj build [OPTIONS]

DESCRIPTION
  Build project for production deployment.

OPTIONS
  -o, --output <dir>      Output directory (default: dist/)
  -w, --watch             Watch for changes and rebuild
      --clean             Remove output directory before build
      --sourcemap         Generate source maps
      --minify            Minify output (default in production)
      --no-minify         Skip minification
      --analyze           Generate bundle analysis report
  -h, --help              Show this help message

EXAMPLES
  # Standard production build
  $ proj build

  # Development with watch mode
  $ proj build --watch --sourcemap --no-minify

  # Clean build with analysis
  $ proj build --clean --analyze

OUTPUT
  dist/
  ├── index.js        Main bundle
  ├── index.js.map    Source map (if --sourcemap)
  └── stats.html      Bundle analysis (if --analyze)
```

**Deploy Subcommand**:
```
USAGE
  proj deploy [OPTIONS] [target]

DESCRIPTION
  Deploy project to configured cloud provider.

ARGUMENTS
  [target]    Deployment target (default: from proj.config.json)

OPTIONS
  -e, --env <name>        Environment: dev, staging, prod (default: dev)
  -b, --build             Build before deploying (default)
      --no-build          Skip build step
      --dry-run           Show what would be deployed without deploying
  -y, --yes               Skip confirmation prompt
      --rollback          Rollback to previous deployment
  -h, --help              Show this help message

ENVIRONMENTS
  dev        Development environment (permissive, verbose logs)
  staging    Pre-production testing (production-like)
  prod       Production (requires confirmation)

EXAMPLES
  # Deploy to development
  $ proj deploy

  # Deploy to production (will prompt for confirmation)
  $ proj deploy --env prod

  # Preview deployment without making changes
  $ proj deploy --env staging --dry-run

  # Rollback last production deployment
  $ proj deploy --env prod --rollback

REQUIRED CONFIGURATION
  Set in proj.config.json or environment variables:

  AWS:     AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
  GCP:     GOOGLE_APPLICATION_CREDENTIALS
  Vercel:  VERCEL_TOKEN
```

### Example 3: Git-Style Command Help

**Input**: Write help text for a database migration CLI with git-style commands

**Output**:
```
USAGE
  migrate <command> [options]

DESCRIPTION
  Database migration tool. Track and apply schema changes safely.

COMMANDS

  Getting Started
    init              Initialize migrations in current project
    status            Show pending and applied migrations

  Creating Migrations
    new <name>        Create a new migration file
    generate          Auto-generate migration from model changes

  Running Migrations
    up                Apply all pending migrations
    down              Rollback the last migration
    to <version>      Migrate to a specific version
    redo              Rollback and re-apply last migration

  Utilities
    list              List all migrations with status
    validate          Check migrations for errors
    seed              Run database seeders
    reset             Rollback all and re-apply (DESTRUCTIVE)

OPTIONS
  -d, --database <url>    Database connection URL
                          (default: DATABASE_URL env var)
  -c, --config <file>     Config file (default: migrate.config.js)
      --dry-run           Show SQL without executing
  -f, --force             Skip safety confirmations
  -h, --help              Show help for command
      --version           Show version

EXAMPLES
  $ migrate init                    # Setup migrations
  $ migrate new add-users-table     # Create migration
  $ migrate up                      # Apply pending
  $ migrate down                    # Rollback one
  $ migrate status                  # Check state

QUICK START
  1. Initialize:  migrate init
  2. Create:      migrate new create-users
  3. Edit:        migrations/001_create-users.sql
  4. Apply:       migrate up

Run 'migrate <command> --help' for detailed command help.
```

**Detailed Command Help (migrate new)**:
```
USAGE
  migrate new [OPTIONS] <name>

DESCRIPTION
  Create a new migration file with timestamp prefix.

ARGUMENTS
  <name>    Migration name (use-kebab-case recommended)

OPTIONS
  -t, --template <type>    Migration template (default: sql)
                           Options: sql, js, ts
      --table <name>       Pre-fill with table creation boilerplate
      --alter <name>       Pre-fill with table alteration boilerplate
  -e, --editor             Open in $EDITOR after creation
  -h, --help               Show this help message

NAMING CONVENTIONS
  Good: add-users-table, create-orders-index, update-email-column
  Bad:  migration1, changes, fix (be descriptive!)

EXAMPLES
  # Create empty migration
  $ migrate new add-users-table
  Created: migrations/20240315103000_add-users-table.sql

  # Create with table template
  $ migrate new create-products --table products
  Created: migrations/20240315103100_create-products.sql
  # Pre-filled with CREATE TABLE boilerplate

  # Create and open in editor
  $ migrate new update-orders -e
  Created: migrations/20240315103200_update-orders.sql
  Opening in vim...

GENERATED FILE
  migrations/
  └── 20240315103000_add-users-table.sql

  -- migrate:up
  -- Write your UP migration here

  -- migrate:down
  -- Write your DOWN (rollback) migration here
```

## Quality Checklist

- [ ] Usage string shows correct syntax
- [ ] All options have descriptions
- [ ] Required vs optional clearly marked
- [ ] Default values documented
- [ ] Examples show realistic usage
- [ ] Subcommands listed with summaries
- [ ] Environment variables mentioned
- [ ] Exit codes documented for scripts
- [ ] Help for --help mentioned
- [ ] Learn more links included
