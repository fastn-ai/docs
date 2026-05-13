---
description: >-
  API endpoints, authentication, request formats, and error codes for Fastn
  Flows.
---

# API Reference

Fastn exposes a RESTful API with 60+ endpoints across 28 route modules. This reference covers authentication, flow execution, workflow management, the Canonical Data Model, the MCP gateway for AI tools, and the CLI.

### Base URL

```
https://live.fastn.ai/api/v1
```

### Authentication

Every API request requires these headers:

| Header                   | Required         | Description                                                                                                                                      |
| ------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `x-fastn-api-key`        | Yes              | Your API key. Generate in **Settings → API Keys** or the **\</> Integrate** panel in the flow builder.                                           |
| `Content-Type`           | Yes              | `application/json`                                                                                                                               |
| `x-fastn-space-id`       | Yes              | Your workspace ID. Found in the **\</> Integrate** panel.                                                                                        |
| `x-fastn-space-tenantid` | For multi-tenant | Scopes the request to a specific customer (tenant). Each tenant has isolated data, credentials, and logs. Leave empty for single-tenant testing. |
| `stage`                  | Optional         | `DRAFT` for testing against unpublished changes, or the live environment name for production.                                                    |
| `x-fastn-custom-auth`    | Optional         | `true` if your flow uses custom authentication.                                                                                                  |
| `authorization`          | Optional         | Bearer token or custom auth token.                                                                                                               |

**Minimal request:**

```bash
curl --request POST \
  --url https://live.fastn.ai/api/v1/YOUR_FLOW_NAME \
  --header "x-fastn-api-key: YOUR_KEY" \
  --header "Content-Type: application/json" \
  --header "x-fastn-space-id: YOUR_SPACE_ID" \
  --data '{"input": {}}'
```

**Multi-tenant request (on behalf of a specific customer):**

```bash
curl --request POST \
  --url https://live.fastn.ai/api/v1/sync_orders \
  --header "x-fastn-api-key: YOUR_KEY" \
  --header "Content-Type: application/json" \
  --header "x-fastn-space-id: YOUR_SPACE_ID" \
  --header "x-fastn-space-tenantid: tenant_customer_123" \
  --data '{"input": {"since": "2026-03-01"}}'
```

### Execute a flow

**Endpoint:**

```
POST /api/v1/{flow_name}
```

The `input` object must match the **Request Schema** defined in your flow's trigger step. Field names are case-sensitive.

```json
{
  "input": {
    "field_name": "value"
  }
}
```

The response body matches whatever you configured in your flow's **Success** response step.

### Webhook execution

For flows using the **Trigger on Http Webhook Event** trigger.

**Endpoint:**

```
POST /api/v1/clients/{space_id}/webhooks/{webhook_id}
```

The full URL is shown in the trigger step's right panel in the flow builder and in **Triggers → Webhooks** in the left sidebar.

**Security:** Webhook endpoints support HMAC signature verification using SHA-256 with a configurable secret per connector. The receiver also performs a timestamp freshness check (5-minute window) to prevent replay attacks, and Redis-based deduplication to prevent duplicate processing.

### Workflow management

All workflow endpoints follow the pattern `/api/v1/tenants/{tenant_id}/...`

#### Workflows

| Method | Endpoint                                        | Description                                                          |
| ------ | ----------------------------------------------- | -------------------------------------------------------------------- |
| `GET`  | `/api/v1/tenants/{tid}/workflows`               | List all flow definitions for the tenant                             |
| `GET`  | `/api/v1/tenants/{tid}/workflows/{wid}`         | Get a flow's full specification (steps, triggers, deployment status) |
| `POST` | `/api/v1/tenants/{tid}/workflows`               | Create a new flow definition                                         |
| `PUT`  | `/api/v1/tenants/{tid}/workflows/{wid}`         | Update a flow definition                                             |
| `POST` | `/api/v1/tenants/{tid}/workflows/{wid}/publish` | Deploy / publish a flow                                              |
| `POST` | `/api/v1/tenants/{tid}/workflows/{wid}/archive` | Deactivate a flow without deleting                                   |

#### Executions

| Method | Endpoint                                        | Description                                                           |
| ------ | ----------------------------------------------- | --------------------------------------------------------------------- |
| `GET`  | `/api/v1/tenants/{tid}/executions`              | List execution history                                                |
| `GET`  | `/api/v1/tenants/{tid}/executions/{eid}`        | Get full step-by-step execution trace (input/output per step, errors) |
| `POST` | `/api/v1/tenants/{tid}/executions/{eid}/cancel` | Cancel a running execution                                            |

**Execution statuses:**

| Status      | Meaning                         |
| ----------- | ------------------------------- |
| `pending`   | Triggered but not started       |
| `running`   | Currently executing             |
| `completed` | All steps succeeded             |
| `failed`    | One or more steps errored       |
| `cancelled` | Manually stopped                |
| `timed_out` | Exceeded maximum execution time |

#### Credentials

| Method | Endpoint                                  | Description                 |
| ------ | ----------------------------------------- | --------------------------- |
| `POST` | `/api/v1/tenants/{tid}/credentials`       | Store connector credentials |
| `GET`  | `/api/v1/tenants/{tid}/credentials`       | Retrieve stored credentials |
| `PUT`  | `/api/v1/tenants/{tid}/credentials/{cid}` | Rotate credentials          |

#### Environments and releases

| Method | Endpoint                             | Description                     |
| ------ | ------------------------------------ | ------------------------------- |
| `POST` | `/api/v1/tenants/{tid}/environments` | Create a deployment environment |
| `GET`  | `/api/v1/tenants/{tid}/environments` | List environments               |
| `POST` | `/api/v1/tenants/{tid}/releases`     | Create a new release version    |
| `GET`  | `/api/v1/tenants/{tid}/releases`     | List release versions           |

### Workflow engine

#### Step types

Flows are built from these step types, available both in the visual builder and the TypeScript DSL:

| Step type      | Description                                                       | Where to find in the builder                   |
| -------------- | ----------------------------------------------------------------- | ---------------------------------------------- |
| `action`       | Execute an operation — call a connector, transform data, run code | Connector, Data Mapper, Custom Code, AI Action |
| `wait`         | Pause execution for a duration or until a condition is met        | —                                              |
| `approval`     | Pause execution until a human approves                            | —                                              |
| `notification` | Send a notification (in-app, email, Slack, webhook)               | —                                              |
| `gate`         | Conditional branching based on data                               | Switch                                         |
| `loop`         | Iterate over a collection                                         | Loop                                           |

#### Trigger types

| Trigger   | Description                                                | Builder label                                   |
| --------- | ---------------------------------------------------------- | ----------------------------------------------- |
| `webhook` | Run when an HTTP request or external event arrives         | New API Request / Trigger on Http Webhook Event |
| `cron`    | Run on a schedule                                          | On Schedule                                     |
| `manual`  | Run when explicitly triggered by a user or API call        | On API Request                                  |
| `event`   | Run when an app event occurs (e.g., Shopify order created) | On App Event                                    |

#### Error strategies

Each step can be configured with an error strategy:

| Strategy   | Behavior                                          |
| ---------- | ------------------------------------------------- |
| `halt`     | Stop the entire flow if this step fails (default) |
| `continue` | Log the error and proceed to the next step        |

#### Execution runtime

* Steps execute in topological order (dependencies resolved automatically)
* Retry with configurable backoff strategy per step
* Context building with input/output data propagation between steps
* Distributed tracing via OpenTelemetry for debugging execution across steps

#### Deployment targets

Flows can be deployed to different infrastructure depending on your environment:

| Target            | Handler                   | Infrastructure                  |
| ----------------- | ------------------------- | ------------------------------- |
| AWS Lambda        | `createLambdaHandler()`   | Pulumi-managed Lambda functions |
| GCP Cloud Run     | `createCloudRunHandler()` | Docker-based Cloud Run services |
| Local development | Fastify server            | `tsx --watch` with hot reload   |

#### TypeScript DSL

Flows can also be defined in code using the `@fastn/workflow` package:

```typescript
import { workflow, step, defineConfig } from '@fastn/workflow';

const syncOrders = workflow('sync_orders', {
  trigger: { type: 'cron', schedule: '0 6 * * *' },
  steps: [
    step('fetch_orders', {
      type: 'action',
      handler: async (ctx) => {
        // fetch from Shopify
      },
      onError: 'continue'
    }),
    step('write_to_xero', {
      type: 'action',
      handler: async (ctx) => {
        // create invoice in Xero using ctx.steps.fetch_orders.output
      },
      onError: 'halt'
    })
  ]
});
```

### Canonical Data Model (CDM)

The CDM is Fastn's internal neutral schema. All connectors map their data to and from CDM entities, enabling cross-system normalization without custom point-to-point mappings.

#### CDM entities

| Entity              | Key fields                                                                        | Use case                                                    |
| ------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `CDMContact`        | id, email, firstName, lastName, company, phone, addresses, tags, customFields     | Unified customer/contact across CRM, e-commerce, accounting |
| `CDMProduct`        | id, name, sku, description, variants, pricingTiers, category, status, inventory   | Product catalog normalization across Shopify, Cin7, etc.    |
| `CDMOrder`          | id, contact, lineItems, totals, payments, status, shippingAddress, billingAddress | Order data from any e-commerce or ERP system                |
| `CDMInvoice`        | id, contact, lineItems, totals, status, dueDate, payments, currency               | Invoice normalization across Xero, QuickBooks, Stripe       |
| `CDMInventoryLevel` | productId, variantId, locationId, available, onHand, committed, reserved          | Real-time inventory across warehouses and channels          |
| `CDMFulfillment`    | id, orderId, status, trackingNumber, carrier, lineItems, shippedAt                | Shipping and fulfillment tracking across providers          |

#### Transformation engine

The transformation engine handles data conversion between connector-native formats and CDM entities:

**Field mapping:** JSONPath-based with dot notation and array index support.

**Built-in transforms:**

| Transform  | What it does                       |
| ---------- | ---------------------------------- |
| `UPPER`    | Convert text to uppercase          |
| `LOWER`    | Convert text to lowercase          |
| `TRIM`     | Remove leading/trailing whitespace |
| `ROUND`    | Round a number                     |
| `MULTIPLY` | Multiply a number                  |
| `ADD`      | Add to a number                    |
| `CONCAT`   | Combine strings                    |
| `COALESCE` | Return the first non-null value    |

**Type coercion:** Automatically handles date formats (Unix timestamps, ISO 8601, MM-DD-YYYY, DD-MM-YYYY), locale-aware numbers, booleans, currency (stored as string, not float), and enums.

### Connectors

#### List connectors

```
GET /api/v1/connectors
```

#### Discover connector capabilities

```
POST /api/v1/connectors/discover
```

Returns supported entities, actions, and events for a specific connector, plus field coverage scores showing CDM mapping completeness.

#### Built-in connectors

| Connector  | Category      | Key actions                                          |
| ---------- | ------------- | ---------------------------------------------------- |
| Shopify    | E-commerce    | Products, Orders, Inventory, Fulfillments, Customers |
| Stripe     | Payments      | Charges, Subscriptions, Customers, Invoices, Refunds |
| Xero       | Accounting    | Invoices, Contacts, Payments, Bank Transactions      |
| QuickBooks | Accounting    | Invoices, Customers, Items, Payments, Estimates      |
| Cin7 Core  | Inventory     | Products, Stock, Purchase Orders, Sales Orders       |
| Cin7 Omni  | Fulfillment   | Orders, Inventory, Shipping, Returns                 |
| GitHub     | Development   | Issues, PRs, Repos, Webhooks, Actions                |
| Slack      | Communication | Messages, Channels, Users, Reactions                 |
| Email      | Communication | Send, Templates, Attachments                         |
| HTTP       | Generic       | GET, POST, PUT, DELETE with configurable auth        |
| OpenAI     | AI/ML         | Chat completions, Embeddings, Image generation       |

**Auth types supported:** OAuth2, API Key, Basic Auth, Custom.

### Event pipeline

Events flow through a multi-stage pipeline ensuring reliability and at-least-once delivery:

```
Webhook/Poll → Outbox → Fan-out → Normalize → Route → Execute
```

| Stage            | What it does                                                                           |
| ---------------- | -------------------------------------------------------------------------------------- |
| **Webhook/Poll** | External events arrive via webhook receiver or synthetic polling                       |
| **Outbox**       | Events written to PostgreSQL outbox table (transactional guarantee — no events lost)   |
| **Fan-out**      | Outbox poller publishes to Redis Streams                                               |
| **Normalize**    | Creates a NormalizedEvent with SHA-256 idempotency key (prevents duplicate processing) |
| **Route**        | Flow Router matches events to registered triggers using condition evaluation           |
| **Execute**      | Matched flows dispatched for workflow execution                                        |

#### Event priority

| Priority     | Type           | Example                                 |
| ------------ | -------------- | --------------------------------------- |
| P1 (highest) | User-triggered | Customer clicks a button in your widget |
| P2           | Event-driven   | Shopify webhook with a new order        |
| P3           | Background     | Scheduled flow runs daily sync          |
| P4 (lowest)  | Polling        | Synthetic event detected a change       |

#### Dead Letter Queue

Failed events are captured in a Dead Letter Queue with full payload and error context. Failed events can be replayed manually or automatically once the root cause is fixed.

### MCP Gateway

The Model Context Protocol (MCP) gateway exposes Fastn as tools for AI assistants (Cursor, Copilot, Claude, custom agents).

```
POST /api/v1/mcp/tools
GET /api/v1/mcp/resources
```

#### Native tools

| Tool                           | Description                                     |
| ------------------------------ | ----------------------------------------------- |
| `fastn_list_integrations`      | List all active integrations for a tenant       |
| `fastn_get_integration_status` | Get detailed status of a specific integration   |
| `fastn_create_flow`            | Create a new automation flow from specification |
| `fastn_get_event_history`      | Retrieve recent events for a tenant             |
| `fastn_get_usage_summary`      | Get quota usage summary                         |
| `fastn_search_entities`        | Search CDM entities across integrations         |

#### Dynamic tools

Fastn also auto-generates MCP tools from connector capabilities. If a tenant has Shopify connected, the MCP gateway exposes Shopify-specific tools (list products, create order, etc.) automatically. Tool availability is per-tenant based on active integrations.

#### Example — AI tool creating a flow via MCP

```json
{
  "tool": "fastn_create_flow",
  "input": {
    "name": "order_to_invoice",
    "description": "When a Shopify order is created, create an invoice in Xero",
    "trigger": {
      "type": "event",
      "source": "shopify",
      "event": "order.created"
    },
    "steps": [
      {
        "name": "create_invoice",
        "type": "action",
        "connector": "xero",
        "action": "createInvoice",
        "mapping": {
          "Contact.EmailAddress": "{{trigger.customer.email}}",
          "LineItems": "{{trigger.line_items}}",
          "Total": "{{trigger.total_price}}"
        }
      }
    ]
  }
}
```

***

### AI agents

```
POST /api/v1/ai/chat
POST /api/v1/ai/generate
POST /api/v1/ai/run
```

Fastn includes 7 specialized AI agents powered by Anthropic Claude:

| Agent                     | Purpose                                                 | Key tools                                                                  |
| ------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------- |
| **SaaS Discovery**        | Research and profile SaaS companies for onboarding      | `web_search`, `fetch_url`, `save_company_profile`                          |
| **Business Intelligence** | Analyze tenant usage and recommend integrations         | `read_tenant_usage`, `list_connectors`, `recommend_integrations`           |
| **Onboarding**            | Guide users through integration setup                   | `check_permission`, `initiate_auth`, `discover_accounts`, `run_test_sync`  |
| **Workflow Builder**      | Help users create automation flows via natural language | `parse_intent`, `list_triggers`, `list_actions`, `build_flow`, `test_flow` |
| **Config Agent**          | Manage complex configuration scenarios                  | `read_tenant_config`, `detect_edge_cases`, `generate_documentation`        |
| **Operations**            | Monitor platform health and handle incidents            | `platform_metrics`, `connector_health`, `dlq_depth`, `create_incident`     |
| **Partner Check**         | Audit SaaS partner health and compliance                | `partner_metrics`, `integration_status`, `usage_patterns`                  |

#### Agent Builder

Create custom AI agents via natural language. The build lifecycle:

```
PLANNING → PLANNED → GENERATING → GENERATED → DEPLOYED
```

```
POST /api/v1/agent-builder/builds
GET /api/v1/agent-builder/builds/{build_id}
POST /api/v1/agent-builder/builds/{build_id}/generate
POST /api/v1/agent-builder/builds/{build_id}/test
POST /api/v1/agent-builder/builds/{build_id}/deploy
```

***

### Platform endpoints

#### Quota and usage

| Method | Endpoint                | Description                       |
| ------ | ----------------------- | --------------------------------- |
| `GET`  | `/api/v1/quota/usage`   | Current usage against plan limits |
| `GET`  | `/api/v1/quota/summary` | Usage summary                     |
| `GET`  | `/api/v1/quota/daily`   | Daily usage breakdown             |

**Plan limits:**

| Dimension              | Starter | Growth    | Enterprise |
| ---------------------- | ------- | --------- | ---------- |
| Events per day         | 1,000   | 50,000    | Unlimited  |
| Active integrations    | 5       | 50        | Unlimited  |
| Flows per tenant       | 10      | 100       | Unlimited  |
| API calls per minute   | 60      | 600       | 6,000      |
| Agent sessions per day | 10      | 100       | Unlimited  |
| LLM tokens per day     | 100,000 | 1,000,000 | 10,000,000 |
| Connectors per tenant  | 3       | 20        | Unlimited  |
| Storage (MB)           | 100     | 1,000     | 10,000     |

#### Configuration

Fastn uses a 5-level configuration hierarchy (highest priority first):

| Priority | Scope       | Description                |
| -------- | ----------- | -------------------------- |
| 1        | Flow        | Per-flow overrides         |
| 2        | Integration | Per-integration settings   |
| 3        | Tenant      | Customer-wide defaults     |
| 4        | SaaS        | Your organization defaults |
| 5        | Platform    | Global Fastn defaults      |

```
GET /api/v1/config
PUT /api/v1/config
```

#### Notifications

```
GET /api/v1/notifications
POST /api/v1/notifications
POST /api/v1/notifications/mark-read
```

Multi-channel notifications: in-app, email, Slack, webhook. Supports severity levels with automatic alert escalation for critical/error severity.

#### Billing

```
POST /api/v1/billing/subscribe
GET /api/v1/billing/portal
GET /api/v1/billing/usage
```

Stripe-based subscription management with plan tiers (Starter, Growth, Enterprise).

#### Audit log

All actions are recorded in an immutable audit trail queryable by tenant, actor, resource, and time range. Actor types: user, service\_account, agent, system.

#### Organizations

```
POST /api/v1/organizations
GET /api/v1/organizations
```

Manage teams, projects, and organizational structure.

#### API access

```
POST /api/v1/api-access
GET /api/v1/api-access
```

Manage API keys and OAuth clients.

***

### CLI

The `@fastn/cli` package provides command-line tools for managing flows:

| Command         | Description                                    |
| --------------- | ---------------------------------------------- |
| `fastn dev`     | Start local development server with hot reload |
| `fastn run`     | Execute a flow locally                         |
| `fastn deploy`  | Deploy a flow to Lambda or Cloud Run           |
| `fastn logs`    | View execution logs                            |
| `fastn destroy` | Remove a deployed flow                         |

### Error codes

| HTTP Status | Error Code                    | Meaning                                                                                                                       | Fix                                                                                                         |
| ----------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 400         | `DATASOURCE_CONNECTION_ERROR` | Connector failed to communicate with external service. Response includes `datasourceDebug` with the service's specific error. | Check `datasourceDebug.jsonObject` for the external error. Re-authenticate in **Connectors → Credentials**. |
| 401         | `UNAUTHORIZED`                | Missing or invalid API key.                                                                                                   | Generate a new key in **Settings → API Keys** or **\</> Integrate**.                                        |
| 403         | `FORBIDDEN`                   | No permission for this operation or tenant.                                                                                   | Verify `x-fastn-space-tenantid` and check role permissions.                                                 |
| 404         | `NOT_FOUND`                   | Flow does not exist or not accessible. Message: "The resource does not exist, or you do not have access."                     | Verify flow name (case-sensitive, underscores only). Confirm the flow is deployed (status: **Live**).       |
| 408         | `TIMED_OUT`                   | Execution exceeded maximum time.                                                                                              | Add pagination, reduce data volume, check for slow external APIs.                                           |
| 429         | `RATE_LIMITED`                | Too many requests. Limits per plan tier.                                                                                      | Reduce frequency or upgrade plan.                                                                           |
| 500         | `INTERNAL_ERROR`              | Unexpected error.                                                                                                             | Check execution logs for the failing step.                                                                  |

**Error response format (real example from the platform):**

```json
{
  "code": "DATASOURCE_CONNECTION_ERROR",
  "statusCode": 400,
  "isCustomAuthError": false,
  "step": "sendMessageApi",
  "datasourceDebug": {
    "name": "sendMessage",
    "jsonObject": {
      "ok": false,
      "error": "channel_not_found"
    }
  }
}
```

### Data mapping syntax

| Pattern                               | References                        | Example                           |
| ------------------------------------- | --------------------------------- | --------------------------------- |
| `{{input.fieldName}}`                 | Trigger's incoming request field  | `{{input.message}}`               |
| `{{trigger.fieldName}}`               | Same as input — trigger step data | `{{trigger.customer_email}}`      |
| `{{steps.stepName.output.fieldName}}` | Specific field from a named step  | `{{steps.sendMessage.output.ts}}` |
| `{{steps.stepName.output}}`           | Entire output object from a step  | `{{steps.fetchOrders.output}}`    |

### Sync engine

For integrations that keep data synchronized across systems:

#### ID mapping

Bidirectional ID mapping between source and target systems. For example, a Shopify order ID mapped to the corresponding Xero invoice ID. Redis-cached with PostgreSQL persistence.

#### Conflict resolution

When the same record is modified in both systems:

| Strategy          | Behavior                         | Use case                           |
| ----------------- | -------------------------------- | ---------------------------------- |
| `source_wins`     | Source value takes precedence    | Source is the authoritative system |
| `target_wins`     | Target value preserved           | Target is authoritative            |
| `last_write_wins` | Most recent timestamp wins       | Eventually consistent systems      |
| `merge`           | Field-level merge of both values | Complementary data sources         |
| `manual`          | Flag for human review            | High-value or ambiguous conflicts  |
