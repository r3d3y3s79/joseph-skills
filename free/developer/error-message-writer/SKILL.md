---
name: error-message-writer
description: Use when writing user-facing error messages, validation feedback, or system alerts. Helps create clear, actionable error messages that guide users to resolution.
---

# Error Message Writer

## Overview

Write error messages that help users fix problems instead of frustrating them. This skill helps you create error messages that are clear, specific, actionable, and human-friendly while providing developers with the technical details they need.

## When to Use

- Writing validation error messages
- Creating API error responses
- Designing system alerts and notifications
- Improving existing cryptic error messages
- Building error handling for user interfaces

## Output Structure

```
ERROR MESSAGE DESIGN:

## Error Context
- **Situation**: [What triggers this error]
- **Audience**: [End user / Developer / Admin]
- **Severity**: [Info / Warning / Error / Critical]

## User-Facing Message

**Title**: [Short, clear headline]

**Body**: [What happened + Why + What to do next]

**Action**: [Primary button/link text]

---

## Technical Details (for developers/logs)

```json
{
  "code": "ERROR_CODE",
  "message": "Human-readable message",
  "details": {
    "field": "value",
    "constraint": "what was violated"
  },
  "help_url": "https://docs.example.com/errors/ERROR_CODE"
}
```

---

## Variations

### Short form (toast/inline)
[One-line version for constrained spaces]

### Detailed form (modal/page)
[Full explanation with steps to resolve]
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Tone | Helpful, not blaming |
| Length | As short as possible, as long as necessary |
| Action | Always tell user what to do next |
| Technical | Keep jargon in logs, not UI |
| Code | Use unique codes for debugging |
| Retry | Suggest retry only if it might help |
| Contact | Provide support path for unresolvable errors |

## Error Message Formula

### The Three Parts

1. **What happened**: State the problem clearly
2. **Why it happened**: Brief explanation (if helpful)
3. **What to do**: Specific next step

### Examples

Bad:
```
Error: Invalid input
```

Good:
```
Password must be at least 8 characters.
Your password has 6 characters. Add 2 more to continue.
```

## Error Categories

### Validation Errors
- Tell user exactly what's wrong
- Show where the error is
- Explain the requirement

### Authentication Errors
- Be vague about security details
- Don't confirm which part (user/password) is wrong
- Guide to recovery (forgot password)

### System Errors
- Apologize briefly
- Don't expose technical details
- Provide support contact
- Include reference ID for support

### Permission Errors
- Explain what permission is needed
- Tell who can grant access
- Don't reveal sensitive info

## Common Mistakes

- **Blaming the user**: "You entered invalid data"
- **Tech jargon**: "NullPointerException in UserService"
- **No action**: Error with no way forward
- **Too vague**: "Something went wrong"
- **Too technical**: "SQLITE_CONSTRAINT_UNIQUE"
- **Scary language**: "FATAL ERROR" for minor issues

## Examples

### Example 1: Form Validation Errors

**Input**: Write error messages for a signup form with email, password, and name fields

**Output**:

**Email Errors**:
```
## Email already registered

Looks like you already have an account with this email.

[Sign in instead] or [Reset your password]

---
Inline: "This email is already registered. Sign in or reset your password."
Code: EMAIL_ALREADY_EXISTS
```

```
## Invalid email format

Please enter a valid email address.
Example: name@example.com

---
Inline: "Enter a valid email address (e.g., name@example.com)"
Code: EMAIL_INVALID_FORMAT
```

**Password Errors**:
```
## Password requirements not met

Your password needs:
✓ At least 8 characters (you have 8)
✗ One uppercase letter
✗ One number

---
Inline: "Add an uppercase letter and a number"
Code: PASSWORD_REQUIREMENTS_NOT_MET
```

```
## Password too common

This password appears in data breaches and isn't secure.
Try adding numbers or symbols to make it unique.

[Generate strong password]

---
Inline: "This password isn't secure. Try something more unique."
Code: PASSWORD_COMPROMISED
```

**Name Errors**:
```
## Name is required

Please enter your name so we know what to call you.

---
Inline: "Enter your name"
Code: NAME_REQUIRED
```

**API Response Format**:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Please fix the errors below",
    "fields": {
      "email": {
        "code": "EMAIL_ALREADY_EXISTS",
        "message": "This email is already registered"
      },
      "password": {
        "code": "PASSWORD_REQUIREMENTS_NOT_MET",
        "message": "Password needs an uppercase letter and number",
        "requirements": {
          "minLength": { "required": 8, "actual": 8, "met": true },
          "uppercase": { "required": true, "met": false },
          "number": { "required": true, "met": false }
        }
      }
    }
  }
}
```

### Example 2: API Error Responses

**Input**: Write error messages for a REST API including authentication, rate limiting, and not found errors

**Output**:

**Authentication Errors**:
```
## 401 Unauthorized

{
  "error": {
    "code": "AUTHENTICATION_REQUIRED",
    "message": "Authentication required",
    "details": "Include a valid API key in the Authorization header",
    "help_url": "https://docs.api.com/authentication"
  }
}
```

```
## 401 Invalid API Key

{
  "error": {
    "code": "INVALID_API_KEY",
    "message": "Invalid API key",
    "details": "The API key provided is not valid or has been revoked",
    "help_url": "https://docs.api.com/api-keys"
  }
}
```

```
## 403 Insufficient Permissions

{
  "error": {
    "code": "INSUFFICIENT_PERMISSIONS",
    "message": "Your API key doesn't have permission for this action",
    "details": "Required scope: 'users:write'. Your key has: 'users:read'",
    "help_url": "https://docs.api.com/scopes"
  }
}
```

**Rate Limiting**:
```
## 429 Too Many Requests

{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests",
    "details": "You've exceeded 100 requests per minute",
    "retry_after": 32,
    "help_url": "https://docs.api.com/rate-limits"
  }
}

Headers:
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1710505800
Retry-After: 32
```

**Not Found**:
```
## 404 Resource Not Found

{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "User not found",
    "details": "No user exists with ID 'usr_xyz789'",
    "help_url": "https://docs.api.com/users#get-user"
  }
}
```

**Server Error**:
```
## 500 Internal Server Error

{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "Something went wrong on our end",
    "details": "Our team has been notified. Please try again in a few minutes.",
    "request_id": "req_abc123xyz",
    "support_url": "https://support.api.com"
  }
}

// Log (internal only):
{
  "request_id": "req_abc123xyz",
  "error": "NullPointerException",
  "stack": "...",
  "user_id": "usr_def456",
  "endpoint": "POST /users",
  "timestamp": "2024-03-15T10:30:00Z"
}
```

### Example 3: System/Application Errors

**Input**: Write error messages for a file upload feature including size limits, format errors, and network failures

**Output**:

**File Too Large**:
```
## User-Facing (Modal)

**File too large**

The file you selected is 25 MB, but the maximum size is 10 MB.

**How to fix:**
- Compress the file using a tool like TinyPNG (for images)
- Split the file into smaller parts
- Choose a different file

[Choose different file]  [Cancel]

---

## Inline (File Input)

"File exceeds 10 MB limit (yours: 25 MB)"

---

## API Response

{
  "error": {
    "code": "FILE_TOO_LARGE",
    "message": "File exceeds maximum size",
    "details": {
      "max_bytes": 10485760,
      "actual_bytes": 26214400,
      "max_display": "10 MB",
      "actual_display": "25 MB"
    }
  }
}
```

**Invalid File Type**:
```
## User-Facing (Modal)

**File type not supported**

We can't accept .exe files. Please upload one of these formats:
- Images: JPG, PNG, GIF, WebP
- Documents: PDF, DOC, DOCX

[Choose different file]

---

## Inline

"Only images and documents allowed (not .exe)"

---

## API Response

{
  "error": {
    "code": "INVALID_FILE_TYPE",
    "message": "File type not allowed",
    "details": {
      "received": "application/x-msdownload",
      "extension": ".exe",
      "allowed": ["image/jpeg", "image/png", "image/gif", "application/pdf"]
    }
  }
}
```

**Network Error**:
```
## User-Facing (Modal)

**Upload interrupted**

The upload couldn't complete due to a connection issue.
Your file hasn't been saved.

[Try again]  [Cancel]

---

## Toast Notification

"Upload failed. Check your connection and try again."

---

## Retry Logic Message (Progress UI)

"Connection lost. Retrying... (attempt 2 of 3)"
"Connection lost. Will retry when you're back online."
```

**Upload Processing Error**:
```
## User-Facing (Modal)

**Couldn't process file**

We received your file but couldn't process it.
This sometimes happens with corrupted files.

**Try this:**
- Re-save the file and upload again
- Try a different file
- Contact support if this keeps happening

Error reference: UPL-ERR-7829

[Try again]  [Contact support]

---

## API Response

{
  "error": {
    "code": "PROCESSING_FAILED",
    "message": "File could not be processed",
    "details": "The file appears to be corrupted or in an unsupported format variant",
    "reference": "UPL-ERR-7829",
    "support_url": "https://support.example.com?ref=UPL-ERR-7829"
  }
}
```

**Success with Warning**:
```
## User-Facing (Toast)

**File uploaded with warnings**

Your file was uploaded, but we noticed:
- Image quality was reduced to meet size limits
- EXIF data was removed for privacy

[View file]  [Dismiss]
```

## Quality Checklist

- [ ] Message explains what went wrong
- [ ] User knows what to do next
- [ ] No technical jargon in user-facing text
- [ ] Error codes provided for support/debugging
- [ ] Tone is helpful, not blaming
- [ ] Security-sensitive errors are appropriately vague
- [ ] Retry suggested only when it might help
- [ ] Contact/support path provided for unresolvable errors
- [ ] Short version available for space-constrained UI
- [ ] API response includes structured error details
