---
name: tutorial-creator
description: Use when creating step-by-step technical tutorials, how-to guides, or learning materials. Helps structure tutorials with clear prerequisites, incremental steps, and working code examples.
---

# Tutorial Creator

## Overview

Create technical tutorials that take learners from zero to working implementation. This skill helps you structure tutorials with clear prerequisites, incremental steps, checkpoints, and code examples that actually work.

## When to Use

- Writing getting started guides
- Creating how-to documentation
- Building course content
- Explaining complex technical concepts
- Teaching new tools or frameworks

## Output Structure

```
TUTORIAL:

# [Action Verb] + [What You'll Build/Learn]

[One sentence describing the end result and who this is for]

## What You'll Learn

- [Skill/concept 1]
- [Skill/concept 2]
- [Skill/concept 3]

## Prerequisites

- [Required knowledge]
- [Required software with version]
- [Required accounts/access]

## Time Required

[X minutes/hours]

---

## Step 1: [Action Verb] [Specific Task]

[Brief explanation of what this step accomplishes]

```language
[code block]
```

[Explanation of key parts of the code]

> **Note**: [Important callout if needed]

**Checkpoint**: [How to verify this step worked]

---

## Step 2: [Action Verb] [Specific Task]

[Continue pattern...]

---

## Summary

[What was accomplished]

## Next Steps

- [Related tutorial]
- [Advanced topic]
- [Community resources]

## Troubleshooting

### [Common problem]
[Solution]

### [Common problem]
[Solution]
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Title | Start with verb: Build, Create, Deploy, Learn |
| Prerequisites | Be specific: Node.js 18+, not just "Node" |
| Steps | One task per step, numbered |
| Code | Complete and runnable, not fragments |
| Checkpoints | After every significant step |
| Explanations | Explain why, not just how |
| Troubleshooting | Include common issues |

## Tutorial Types

### Getting Started

Focus on:
- Minimal working example
- Zero to running in 10 minutes
- Skip advanced configuration

### How-To Guide

Focus on:
- Specific task completion
- Multiple approaches if relevant
- Production-ready code

### Concept Explanation

Focus on:
- Analogy or visual
- Build understanding incrementally
- Interactive examples

### Project Tutorial

Focus on:
- Building something complete
- Each section adds functionality
- Final result is usable

## Common Mistakes

- **Assumed knowledge**: Don't skip "obvious" steps
- **Broken code**: Test every code block
- **No checkpoints**: Reader doesn't know if they're on track
- **Wall of code**: Break into digestible chunks
- **Missing context**: Explain why, not just what
- **No troubleshooting**: Anticipate where readers get stuck

## Examples

### Example 1: Getting Started Tutorial

**Input**: Create a tutorial for building a REST API with Express.js

**Output**:
```markdown
# Build a REST API with Express.js

Create a simple but complete REST API with Express.js in 30 minutes. Perfect for developers new to Node.js or backend development.

## What You'll Learn

- Set up a Node.js project from scratch
- Create REST endpoints (GET, POST, PUT, DELETE)
- Handle JSON request/response
- Add basic error handling
- Test your API with curl

## Prerequisites

- **Node.js 18+** installed ([download](https://nodejs.org))
- **A code editor** (VS Code recommended)
- **Terminal/command line** basics
- **Basic JavaScript** (variables, functions, objects)

Verify Node is installed:
```bash
node --version
# Should output v18.x.x or higher
```

## Time Required

30 minutes

---

## Step 1: Create Your Project

Create a new directory and initialize a Node.js project.

```bash
mkdir todo-api
cd todo-api
npm init -y
```

This creates `package.json` with default settings.

Install Express:

```bash
npm install express
```

**Checkpoint**: Your folder should contain:
```
todo-api/
  node_modules/
  package.json
  package-lock.json
```

---

## Step 2: Create Your Server

Create `index.js` in your project root:

```javascript
const express = require('express');
const app = express();
const PORT = 3000;

// Parse JSON request bodies
app.use(express.json());

// Health check endpoint
app.get('/', (req, res) => {
  res.json({ message: 'Todo API is running' });
});

// Start server
app.listen(PORT, () => {
  console.log('Server running at http://localhost:' + PORT);
});
```

**What this does:**
- `express()` creates your application
- `app.use(express.json())` enables JSON parsing
- `app.get('/')` defines a route that responds to GET requests
- `app.listen()` starts the server

Run your server:
```bash
node index.js
```

**Checkpoint**: Open http://localhost:3000 in your browser. You should see:
```json
{"message":"Todo API is running"}
```

> **Tip**: Press `Ctrl+C` to stop the server.

---

## Step 3: Add In-Memory Data Storage

For this tutorial, we'll store todos in memory. Add this after your imports:

```javascript
const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

// In-memory storage (resets when server restarts)
let todos = [
  { id: 1, title: 'Learn Express', completed: false },
  { id: 2, title: 'Build an API', completed: false },
];
let nextId = 3;
```

> **Note**: In a real application, you'd use a database. We're using memory to focus on Express concepts.

---

## Step 4: Create CRUD Endpoints

### GET all todos

```javascript
// GET /todos - List all todos
app.get('/todos', (req, res) => {
  res.json(todos);
});
```

### GET single todo

```javascript
// GET /todos/:id - Get one todo
app.get('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const todo = todos.find(t => t.id === id);

  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }

  res.json(todo);
});
```

**Key concept**: `:id` is a URL parameter. Express makes it available as `req.params.id`.

### POST create todo

```javascript
// POST /todos - Create new todo
app.post('/todos', (req, res) => {
  const { title } = req.body;

  if (!title) {
    return res.status(400).json({ error: 'Title is required' });
  }

  const todo = {
    id: nextId++,
    title,
    completed: false,
  };

  todos.push(todo);
  res.status(201).json(todo);
});
```

**Key concept**: `req.body` contains the parsed JSON from the request body.

### PUT update todo

```javascript
// PUT /todos/:id - Update a todo
app.put('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const todo = todos.find(t => t.id === id);

  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }

  const { title, completed } = req.body;
  if (title !== undefined) todo.title = title;
  if (completed !== undefined) todo.completed = completed;

  res.json(todo);
});
```

### DELETE todo

```javascript
// DELETE /todos/:id - Delete a todo
app.delete('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = todos.findIndex(t => t.id === id);

  if (index === -1) {
    return res.status(404).json({ error: 'Todo not found' });
  }

  todos.splice(index, 1);
  res.status(204).send();
});
```

**Key concept**: `204 No Content` is the standard response for successful DELETE.

---

## Step 5: Test Your API

Restart your server, then test each endpoint:

```bash
# Get all todos
curl http://localhost:3000/todos

# Get single todo
curl http://localhost:3000/todos/1

# Create new todo
curl -X POST http://localhost:3000/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"Test the API"}'

# Update a todo
curl -X PUT http://localhost:3000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"completed":true}'

# Delete a todo
curl -X DELETE http://localhost:3000/todos/2
```

**Checkpoint**: All commands should return appropriate JSON responses or status codes.

---

## Complete Code

Your final `index.js` should look like this:

```javascript
const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

let todos = [
  { id: 1, title: 'Learn Express', completed: false },
  { id: 2, title: 'Build an API', completed: false },
];
let nextId = 3;

app.get('/', (req, res) => {
  res.json({ message: 'Todo API is running' });
});

app.get('/todos', (req, res) => {
  res.json(todos);
});

app.get('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const todo = todos.find(t => t.id === id);
  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }
  res.json(todo);
});

app.post('/todos', (req, res) => {
  const { title } = req.body;
  if (!title) {
    return res.status(400).json({ error: 'Title is required' });
  }
  const todo = { id: nextId++, title, completed: false };
  todos.push(todo);
  res.status(201).json(todo);
});

app.put('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const todo = todos.find(t => t.id === id);
  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }
  const { title, completed } = req.body;
  if (title !== undefined) todo.title = title;
  if (completed !== undefined) todo.completed = completed;
  res.json(todo);
});

app.delete('/todos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = todos.findIndex(t => t.id === id);
  if (index === -1) {
    return res.status(404).json({ error: 'Todo not found' });
  }
  todos.splice(index, 1);
  res.status(204).send();
});

app.listen(PORT, () => {
  console.log('Server running at http://localhost:' + PORT);
});
```

---

## Summary

You built a REST API with:
- Five endpoints covering CRUD operations
- JSON request/response handling
- Basic error handling with appropriate status codes

## Next Steps

- [Add a database with PostgreSQL](./express-postgres)
- [Add authentication with JWT](./express-jwt-auth)
- [Deploy to production](./express-deploy)

## Troubleshooting

### "Cannot find module 'express'"
Run `npm install express` in your project directory.

### "Port 3000 already in use"
Another process is using port 3000. Either stop it or change PORT in your code.

### curl command not found (Windows)
Use PowerShell's `Invoke-RestMethod` or install Git Bash.
```

### Example 2: Concept Tutorial

**Input**: Create a tutorial explaining React hooks for developers familiar with class components

**Output**:
```markdown
# Understanding React Hooks: From Classes to Functions

Learn how React hooks work and why they're better than class components. By the end, you'll convert a class component to hooks and understand when to use each hook.

## What You'll Learn

- Why hooks exist and what problems they solve
- How useState replaces this.state
- How useEffect replaces lifecycle methods
- When to use each hook
- Common hooks patterns and gotchas

## Prerequisites

- **React experience** with class components
- **Understanding** of this.state and lifecycle methods
- **Node.js 18+** for running examples

## Time Required

20 minutes

---

## The Problem Hooks Solve

Before hooks, sharing logic between components was awkward. You had to choose between:

1. **Higher-Order Components (HOCs)**: Wrapped your component in another component
2. **Render props**: Passed functions as children

Both led to "wrapper hell" and made code hard to follow.

Here's a class component that fetches user data:

```jsx
class UserProfile extends React.Component {
  state = {
    user: null,
    loading: true,
    error: null,
  };

  componentDidMount() {
    this.fetchUser();
  }

  componentDidUpdate(prevProps) {
    if (prevProps.userId !== this.props.userId) {
      this.fetchUser();
    }
  }

  fetchUser() {
    this.setState({ loading: true });
    fetch('/api/users/' + this.props.userId)
      .then(res => res.json())
      .then(user => this.setState({ user, loading: false }))
      .catch(error => this.setState({ error, loading: false }));
  }

  render() {
    const { user, loading, error } = this.state;
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;
    return <div>Hello, {user.name}</div>;
  }
}
```

Problems:
- Logic spread across multiple lifecycle methods
- `this` binding confusion
- Can't easily extract `fetchUser` for other components

---

## Step 1: Understand useState

`useState` replaces `this.state`. It returns a pair: the current value and a function to update it.

**Class version:**
```jsx
class Counter extends React.Component {
  state = { count: 0 };

  render() {
    return (
      <button onClick={() => this.setState({ count: this.state.count + 1 })}>
        Count: {this.state.count}
      </button>
    );
  }
}
```

**Hooks version:**
```jsx
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}
```

**Key differences:**
- No `this` keyword
- State is a value, not an object
- `setCount` replaces `this.setState`
- Function component, not class

**Checkpoint**: Create a counter component using useState. Verify it increments when clicked.

---

## Step 2: Understand useEffect

`useEffect` replaces `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`.

### Run on Every Render

```jsx
useEffect(() => {
  console.log('Component rendered');
});
```

Equivalent to: `componentDidMount` + `componentDidUpdate`

### Run Once on Mount

```jsx
useEffect(() => {
  console.log('Component mounted');
}, []); // Empty dependency array
```

Equivalent to: `componentDidMount`

### Run When Dependencies Change

```jsx
useEffect(() => {
  console.log('userId changed:', userId);
}, [userId]); // Runs when userId changes
```

Equivalent to: `componentDidMount` + `componentDidUpdate` with comparison

### Cleanup on Unmount

```jsx
useEffect(() => {
  const subscription = subscribe(userId);

  return () => {
    subscription.unsubscribe(); // Cleanup function
  };
}, [userId]);
```

Equivalent to: `componentWillUnmount`

---

## Step 3: Convert the Class Component

Now let's convert our UserProfile class to hooks:

```jsx
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    setError(null);

    fetch('/api/users/' + userId)
      .then(res => res.json())
      .then(data => {
        setUser(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err);
        setLoading(false);
      });
  }, [userId]); // Re-run when userId changes

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  return <div>Hello, {user.name}</div>;
}
```

**What improved:**
- All related logic is together (fetch + state updates)
- No lifecycle method confusion
- No `this` keyword
- Easier to read top-to-bottom

---

## Step 4: Extract Custom Hooks

Here's the real power of hooks - extracting reusable logic:

```jsx
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch(url)
      .then(res => res.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [url]);

  return { data, loading, error };
}
```

Now any component can use it:

```jsx
function UserProfile({ userId }) {
  const { data: user, loading, error } = useFetch('/api/users/' + userId);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  return <div>Hello, {user.name}</div>;
}

function ProductList() {
  const { data: products, loading } = useFetch('/api/products');

  if (loading) return <div>Loading...</div>;
  return <ul>{products.map(p => <li key={p.id}>{p.name}</li>)}</ul>;
}
```

**This was impossible with classes** without HOCs or render props.

---

## Common Hooks Reference

| Hook | Purpose | Class Equivalent |
|------|---------|------------------|
| useState | Local state | this.state |
| useEffect | Side effects | Lifecycle methods |
| useContext | Access context | static contextType |
| useRef | Mutable reference | createRef() |
| useMemo | Memoize values | Manual caching |
| useCallback | Memoize functions | Binding in constructor |

---

## Summary

Hooks simplify React components by:
- Eliminating `this` and binding confusion
- Colocating related logic
- Enabling custom hooks for reusable logic
- Making components more readable

## Next Steps

- [Advanced Patterns: useReducer](./react-usereducer)
- [Performance: useMemo and useCallback](./react-memoization)
- [Custom Hooks Library](./custom-hooks)

## Troubleshooting

### "Hooks can only be called inside function components"
You're trying to use a hook in a class component or outside a component. Hooks only work in function components.

### Infinite loop with useEffect
You're probably missing the dependency array or updating a dependency inside the effect.

### State not updating immediately
State updates are asynchronous. If you need the new value immediately, use the callback form: `setState(prev => prev + 1)`.
```

### Example 3: Project Build Tutorial

**Input**: Create a tutorial for building a CLI tool that generates project scaffolding

**Output**:
```markdown
# Build a CLI Project Generator with Node.js

Create a command-line tool that scaffolds new projects, similar to `create-react-app` or `npm init`. You'll learn CLI development patterns used by popular tools.

## What You'll Learn

- Parse command-line arguments
- Create interactive prompts
- Generate files from templates
- Publish to npm as a global command

## Prerequisites

- **Node.js 18+** installed
- **npm** basics (init, install, publish)
- **JavaScript** async/await understanding
- **Terminal** familiarity

## Time Required

45 minutes

## What You'll Build

A `create-project` CLI that:
1. Asks for project name and type
2. Creates directory structure
3. Generates config files
4. Initializes git

```bash
$ create-project
? Project name: my-app
? Project type: web
Creating project...
Done! Run: cd my-app && npm install
```

---

## Step 1: Set Up the CLI Project

```bash
mkdir create-project
cd create-project
npm init -y
```

Update `package.json` to make it a CLI tool:

```json
{
  "name": "create-project",
  "version": "1.0.0",
  "bin": {
    "create-project": "./bin/cli.js"
  },
  "type": "module"
}
```

**Key concept**: The `bin` field tells npm to create a command that runs our script.

Create the entry point:

```bash
mkdir bin
touch bin/cli.js
```

Add this to `bin/cli.js`:

```javascript
#!/usr/bin/env node
console.log('create-project CLI');
```

Make it executable and link it:

```bash
chmod +x bin/cli.js
npm link
```

**Checkpoint**: Run `create-project` in your terminal. You should see "create-project CLI".

---

## Step 2: Add Argument Parsing

Install commander for argument parsing:

```bash
npm install commander
```

Update `bin/cli.js`:

```javascript
#!/usr/bin/env node
import { program } from 'commander';

program
  .name('create-project')
  .description('Generate a new project')
  .version('1.0.0')
  .argument('[name]', 'project name')
  .option('-t, --template <type>', 'project template', 'basic')
  .option('-y, --yes', 'skip prompts, use defaults')
  .action((name, options) => {
    console.log('Name:', name);
    console.log('Options:', options);
  });

program.parse();
```

**Checkpoint**: Test argument parsing:
```bash
create-project my-app
# Name: my-app

create-project --template web my-app
# Name: my-app
# Options: { template: 'web', yes: undefined }

create-project --help
# Shows usage information
```

---

## Step 3: Add Interactive Prompts

Install inquirer for interactive prompts:

```bash
npm install inquirer
```

Create `src/prompts.js`:

```javascript
import inquirer from 'inquirer';

export async function getProjectOptions(defaults = {}) {
  const questions = [
    {
      type: 'input',
      name: 'name',
      message: 'Project name:',
      default: defaults.name || 'my-project',
      validate: (input) => {
        if (/^[a-z0-9-]+$/.test(input)) return true;
        return 'Use lowercase letters, numbers, and hyphens only';
      },
    },
    {
      type: 'list',
      name: 'template',
      message: 'Project type:',
      default: defaults.template || 'basic',
      choices: [
        { name: 'Basic - Minimal setup', value: 'basic' },
        { name: 'Web - HTML/CSS/JS', value: 'web' },
        { name: 'API - Express server', value: 'api' },
      ],
    },
    {
      type: 'confirm',
      name: 'git',
      message: 'Initialize git repository?',
      default: true,
    },
  ];

  return inquirer.prompt(questions);
}
```

---

## Step 4: Create Project Generator

Create `src/generator.js` with file generation logic. The generator creates directories, writes template files, and optionally initializes a git repository.

For the complete generator code, see the project repository.

---

## Summary

You built a CLI tool that:
- Parses arguments with commander
- Prompts users with inquirer
- Generates projects from templates
- Initializes git repositories
- Provides colorful, user-friendly output

## Next Steps

- [Publish to npm](./npm-publish)
- [Add more templates](./cli-templates)
- [Test CLI tools](./cli-testing)

## Troubleshooting

### "command not found: create-project"
Run `npm link` in the project directory to register the CLI globally.

### "Cannot find module"
Make sure you're using ES modules (`"type": "module"` in package.json) and the correct import syntax.
```

## Quality Checklist

- [ ] Title starts with action verb
- [ ] Prerequisites are specific (versions, tools)
- [ ] Time estimate provided
- [ ] Each step has one clear goal
- [ ] Code blocks are complete and runnable
- [ ] Checkpoints verify progress
- [ ] Key concepts explained (not just code)
- [ ] Common errors addressed in troubleshooting
- [ ] Next steps for continued learning
- [ ] All code tested before publishing
