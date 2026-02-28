---
name: api-documentation
description: Use when documenting REST APIs, GraphQL endpoints, or SDK methods. Helps create clear, consistent endpoint documentation with request/response examples and error codes.
---

# API Documentation

## Overview

Create clear, developer-friendly API documentation that reduces support tickets and accelerates integration. This skill helps you document endpoints with consistent structure, practical examples, and comprehensive error handling.

## When to Use

- Documenting REST API endpoints
- Creating GraphQL schema documentation
- Writing SDK method references
- Building OpenAPI/Swagger specs
- Updating existing API docs

## Output Structure

```
ENDPOINT DOCUMENTATION:

## [Method] /path/to/endpoint

[One-line description of what this endpoint does]

### Authentication

[Auth requirements - API key, OAuth, etc.]

### Request

**Headers**
| Header | Required | Description |
|--------|----------|-------------|
| [name] | Yes/No   | [purpose]   |

**Path Parameters**
| Parameter | Type   | Description |
|-----------|--------|-------------|
| [name]    | [type] | [purpose]   |

**Query Parameters**
| Parameter | Type    | Default | Description |
|-----------|---------|---------|-------------|
| [name]    | [type]  | [value] | [purpose]   |

**Request Body**
```json
{
  "field": "value"
}
```

| Field | Type   | Required | Description |
|-------|--------|----------|-------------|
| [name]| [type] | Yes/No   | [purpose]   |

### Response

**Success Response (200 OK)**
```json
{
  "field": "value"
}
```

| Field | Type   | Description |
|-------|--------|-------------|
| [name]| [type] | [meaning]   |

### Errors

| Code | Message           | Description              |
|------|-------------------|--------------------------|
| 400  | Bad Request       | [when this occurs]       |
| 401  | Unauthorized      | [when this occurs]       |
| 404  | Not Found         | [when this occurs]       |

### Example

**Request**
```bash
curl -X [METHOD] \
  https://api.example.com/path \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"field": "value"}'
```

**Response**
```json
{
  "status": "success"
}
```

### Rate Limits

[Requests per minute/hour, throttling behavior]

### Notes

[Edge cases, deprecation warnings, related endpoints]
```

## Quick Reference

| Element | Best Practice |
|---------|--------------|
| Description | Start with verb: "Creates", "Returns", "Updates" |
| Parameters | Include type, required flag, default value |
| Examples | Show realistic data, not "foo" or "test" |
| Error codes | Explain when each error occurs |
| Request body | Show all fields, mark required |
| Response | Document every field returned |
| Auth | Be explicit about token format |

## Documentation Patterns

### CRUD Endpoint Set

Document related endpoints together:
- GET /resources - List all
- GET /resources/:id - Get one
- POST /resources - Create
- PUT /resources/:id - Update
- DELETE /resources/:id - Delete

### Paginated Endpoints

Always document:
- page/offset parameter
- limit/per_page parameter
- Total count in response
- Next/prev links or cursors

### Webhook Documentation

Include:
- Event types
- Payload structure
- Retry behavior
- Signature verification

## Common Mistakes

- **No examples**: Always show curl + response
- **Missing error codes**: Document all possible errors
- **Vague types**: "string" vs "email string (max 255 chars)"
- **No auth details**: Specify exactly where token goes
- **Outdated examples**: Test examples before publishing
- **Missing rate limits**: Developers need to know limits

## Examples

### Example 1: REST Endpoint Documentation

**Input**: Document a user creation endpoint for a SaaS API

**Output**:
```
## POST /v1/users

Creates a new user account and sends a welcome email.

### Authentication

Requires API key with `users:write` scope.

### Request

**Headers**
| Header | Required | Description |
|--------|----------|-------------|
| Authorization | Yes | Bearer token: `Bearer sk_live_xxx` |
| Content-Type | Yes | Must be `application/json` |
| Idempotency-Key | No | Unique key to prevent duplicate creates |

**Request Body**
```json
{
  "email": "user@example.com",
  "name": "Jane Smith",
  "role": "member",
  "team_id": "team_abc123",
  "send_invite": true
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | Valid email address (max 255 chars) |
| name | string | Yes | Full name (max 100 chars) |
| role | string | No | One of: `admin`, `member`, `viewer`. Default: `member` |
| team_id | string | No | Team to add user to. Uses default team if omitted |
| send_invite | boolean | No | Send welcome email. Default: `true` |

### Response

**Success Response (201 Created)**
```json
{
  "id": "usr_xyz789",
  "email": "user@example.com",
  "name": "Jane Smith",
  "role": "member",
  "team_id": "team_abc123",
  "status": "pending",
  "created_at": "2024-03-15T10:30:00Z",
  "invite_sent_at": "2024-03-15T10:30:01Z"
}
```

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique user identifier (prefix: `usr_`) |
| status | string | `pending` until invite accepted, then `active` |
| invite_sent_at | string | ISO 8601 timestamp, null if send_invite was false |

### Errors

| Code | Error | Description |
|------|-------|-------------|
| 400 | `email_invalid` | Email format is invalid |
| 400 | `name_required` | Name field is missing or empty |
| 409 | `email_exists` | User with this email already exists |
| 403 | `team_access_denied` | No permission to add users to this team |
| 429 | `rate_limited` | Exceeded 100 requests per minute |

### Example

**Request**
```bash
curl -X POST https://api.example.com/v1/users \
  -H "Authorization: Bearer sk_live_abc123" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: create-jane-20240315" \
  -d '{
    "email": "jane@company.com",
    "name": "Jane Smith",
    "role": "admin",
    "team_id": "team_engineering"
  }'
```

**Response**
```json
{
  "id": "usr_xyz789",
  "email": "jane@company.com",
  "name": "Jane Smith",
  "role": "admin",
  "team_id": "team_engineering",
  "status": "pending",
  "created_at": "2024-03-15T10:30:00Z",
  "invite_sent_at": "2024-03-15T10:30:01Z"
}
```

### Rate Limits

- 100 requests per minute per API key
- 429 response includes `Retry-After` header

### Notes

- Idempotency keys are valid for 24 hours
- Pending users automatically expire after 7 days if invite not accepted
- See [DELETE /v1/users/:id](#delete-users) to remove a user
```

### Example 2: List Endpoint with Pagination

**Input**: Document an endpoint that lists orders with filters and pagination

**Output**:
```
## GET /v1/orders

Returns a paginated list of orders with optional filtering.

### Authentication

Requires API key with `orders:read` scope.

### Request

**Query Parameters**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| page | integer | 1 | Page number (1-indexed) |
| per_page | integer | 20 | Results per page (max: 100) |
| status | string | all | Filter: `pending`, `paid`, `shipped`, `delivered`, `cancelled` |
| customer_id | string | - | Filter by customer ID |
| created_after | string | - | ISO 8601 date. Orders created after this time |
| created_before | string | - | ISO 8601 date. Orders created before this time |
| sort | string | created_at | Sort field: `created_at`, `total`, `updated_at` |
| order | string | desc | Sort order: `asc` or `desc` |

### Response

**Success Response (200 OK)**
```json
{
  "data": [
    {
      "id": "ord_abc123",
      "customer_id": "cus_xyz789",
      "status": "paid",
      "total": 9999,
      "currency": "usd",
      "items_count": 3,
      "created_at": "2024-03-15T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total_count": 150,
    "total_pages": 8,
    "has_next": true,
    "has_prev": false
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| data | array | Array of order objects |
| total | integer | Order total in cents |
| pagination.total_count | integer | Total orders matching filters |
| pagination.has_next | boolean | Whether more pages exist |

### Errors

| Code | Error | Description |
|------|-------|-------------|
| 400 | `invalid_date` | created_after/before is not valid ISO 8601 |
| 400 | `invalid_status` | Status value not recognized |
| 400 | `per_page_exceeded` | per_page cannot exceed 100 |

### Example

**Request**
```bash
curl "https://api.example.com/v1/orders?status=paid&per_page=50&created_after=2024-03-01" \
  -H "Authorization: Bearer sk_live_abc123"
```

**Response**
```json
{
  "data": [
    {
      "id": "ord_abc123",
      "customer_id": "cus_xyz789",
      "status": "paid",
      "total": 9999,
      "currency": "usd",
      "items_count": 3,
      "created_at": "2024-03-15T10:30:00Z"
    },
    {
      "id": "ord_def456",
      "customer_id": "cus_xyz789",
      "status": "paid",
      "total": 4500,
      "currency": "usd",
      "items_count": 1,
      "created_at": "2024-03-14T09:15:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 50,
    "total_count": 73,
    "total_pages": 2,
    "has_next": true,
    "has_prev": false
  }
}
```

### Notes

- Maximum date range is 90 days
- For large exports, use the [Export API](#exports) instead
- Results are cached for 60 seconds
```

### Example 3: Webhook Event Documentation

**Input**: Document a webhook event for payment completed

**Output**:
```
## Webhook: payment.completed

Triggered when a payment is successfully processed and funds are captured.

### Event Payload

```json
{
  "id": "evt_abc123",
  "type": "payment.completed",
  "created_at": "2024-03-15T10:30:00Z",
  "data": {
    "payment_id": "pay_xyz789",
    "order_id": "ord_def456",
    "customer_id": "cus_ghi789",
    "amount": 9999,
    "currency": "usd",
    "payment_method": "card",
    "card_last4": "4242",
    "card_brand": "visa"
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique event ID for idempotency |
| type | string | Always `payment.completed` for this event |
| created_at | string | ISO 8601 timestamp |
| data.amount | integer | Payment amount in cents |
| data.payment_method | string | `card`, `bank_transfer`, `wallet` |

### Signature Verification

All webhooks include a signature header for verification:

```
X-Webhook-Signature: sha256=abc123...
```

**Verification (Node.js)**
```javascript
const crypto = require('crypto');

function verifySignature(payload, signature, secret) {
  const expected = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  return `sha256=${expected}` === signature;
}
```

### Retry Behavior

| Attempt | Delay |
|---------|-------|
| 1 | Immediate |
| 2 | 1 minute |
| 3 | 5 minutes |
| 4 | 30 minutes |
| 5 | 2 hours |

Webhooks are considered failed after 5 attempts or if endpoint returns non-2xx status.

### Expected Response

Return `200 OK` with any body to acknowledge receipt.

### Related Events

- `payment.failed` - Payment was declined
- `payment.refunded` - Payment was refunded
- `payment.disputed` - Chargeback initiated
```

## Quality Checklist

- [ ] Method and path clearly stated
- [ ] One-line description starts with verb
- [ ] Authentication requirements explicit
- [ ] All parameters documented with types
- [ ] Request body shows realistic example
- [ ] Response includes all fields
- [ ] Error codes explain when they occur
- [ ] Working curl example provided
- [ ] Rate limits documented
- [ ] Related endpoints mentioned
