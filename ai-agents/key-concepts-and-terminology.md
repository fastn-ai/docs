---
description: Core concepts to understand crucial areas around Fastn
hidden: true
---

# Key Concepts & Terminology

This page defines the core terms used throughout Fastn's platform and documentation. If you encounter an unfamiliar term while reading other pages, come back here.

### Customers (alternatively called "Tenants")

Each customer gets an isolated environment with their own credentials, integrations, data, and execution history in the form of a tenant. In Fastn, the platform calls them **Customers** (found under **Settings → Customers**).

Customer isolation is enforced at the database level using Row-Level Security (RLS). A customer's data is invisible to other customers.

> **Diagram needed:** Your organization at the top, two or three customers below, each with their own credentials, data, and executions in separate boxes.

### Connectors

A pre-built or custom integration with a third-party app. You manage connectors under **Integrations → Connectors**.

Each connector defines:

* **Authentication method** — Consists of 6 types: No Auth, Basic Auth, Bearer Token, API Key, OAuth 2.0, or Custom
* **Actions** — operations you can perform (create a contact, fetch orders, send a message)
* **Events** — webhook events you can subscribe to (new order created, contact updated)

#### Creating connectors

There are two ways to create a connector, either method can work:

* **+ Create** — manually fill in Name, Slug, Description, Domain, Visibility, Icon URL, and Auth Methods
* **Build with AI** — describe what you need and the Connector Agent discovers the API, builds actions, sets up events, and tests everything

> **Screenshot needed:** Create Connector dialog showing Name, Slug, Description, Domain, Visibility, Icon URL, Auth Methods fields.

#### Connections

A connection is an authenticated instance of a connector. When you (or your customer) authorize an app through OAuth or provide an API key, that creates a connection. This is managed under **Integrations → Connections**.

One connector (e.g., HubSpot) can have multiple connections i.e. your test connection plus each customer's connection.

### Workflows

An automated process written in JavaScript/TypeScript. Each workflow is a code file (`workflow.js`) that exports a default async function receiving a context object (`ctx`).

```javascript
export default async function(ctx) {
  const { input, headers } = ctx;
  // Your workflow logic here
  return { result: "done", input };
}
```

You manage workflows under **Integrations → Workflows**.

#### Workflow configuration

When creating a workflow, you configure:

| Setting               | What it does                                                  |
| --------------------- | ------------------------------------------------------------- |
| **Name**              | Workflow identifier                                           |
| **Description**       | What the workflow does                                        |
| **Execution Tier**    | Instant (sync, max 60s), Standard (async), or Long (extended) |
| **Execution Timeout** | Max time before timeout. Range: 1s–2min for Instant tier.     |
| **Retry Policy**      | Toggle on/off. Configures automatic retry on failure.         |

> **Screenshot needed:** Workflow editor showing the Configuration panel (left), code editor (center), and Test panel (right).

#### Workflow status

| Status       | What it means                                  |
| ------------ | ---------------------------------------------- |
| **active**   | Workflow is deployed and can be triggered      |
| **inactive** | Workflow exists but is not processing triggers |

#### Execution

A single run of a workflow. Every execution is logged under **Activity → Executions** with these columns:

| Column           | What it shows                                               |
| ---------------- | ----------------------------------------------------------- |
| **Time**         | When it ran (relative: "17h ago", "1d ago")                 |
| **Workflow**     | Which workflow executed                                     |
| **Tier**         | Execution tier badge (INSTANT, STANDARD, LONG)              |
| **Version**      | Workflow version (v1, v2, etc.)                             |
| **Status**       | Result: Running, Completed, Failed, Timeout                 |
| **Duration**     | How long it took (79ms, 2.1s)                               |
| **Triggered By** | What started it (agent-service, webhook, scheduler, manual) |

> **Screenshot needed:** Activity → Executions page showing the execution table with all columns.

### Triggers

Triggers are what start workflows. They're managed as a **separate section** under **Integrations → Triggers** not inside the workflow editor. You create a trigger, then route it to one or more workflows.

Three trigger types:

| Type          | What it does                                                                                                                       |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Webhook**   | Receives events from external services via HTTP POST. Supports routes with JSON filters to direct payloads to different workflows. |
| **Scheduler** | Triggers workflows on a schedule. Presets: Interval, Daily, Weekly, Monthly, Custom.                                               |
| **App Event** | Subscribes to events from connectors (HubSpot, GitHub, Stripe). Select a connector, connection, and event to listen for.           |

The Triggers page has three tabs: **Webhooks | Schedulers | App Events**

> **Screenshot needed:** Integrations → Triggers page showing the three tabs and the Add Trigger type selection panel.

#### Webhook routes

A single webhook trigger can route to multiple workflows. Each route has:

* A target workflow (selected from dropdown)
* Optional JSON filters that control which payloads trigger which route
* Optional headers (key-value pairs)

> **Screenshot needed:** Webhook trigger configuration showing Routes with workflow dropdown and filter fields.

### Canonical Data Model (CDM)

Fastn's universal data format which consists of six standard entities i.e. Contact, Product, Order, Invoice, InventoryLevel, Fulfillment — with consistent field names and types.

When data moves between connectors, Fastn maps it through the CDM. A "customer" in Shopify becomes a `CDMContact`. That same `CDMContact` can map to a "contact" in HubSpot or a "client" in Xero.

### Authentication methods

Six auth methods are available when creating connectors:

| Method           | When to use                                                              |
| ---------------- | ------------------------------------------------------------------------ |
| **No Auth**      | Public APIs that don't require authentication                            |
| **Basic Auth**   | Username/password pair                                                   |
| **Bearer Token** | Token-based auth sent in Authorization header                            |
| **API Key**      | Key sent in a custom header (e.g., `X-API-Key`)                          |
| **OAuth 2.0**    | User authorizes via the app's login screen. Fastn manages token refresh. |
| **Custom**       | App-specific auth that doesn't fit standard patterns                     |

> **Screenshot needed:** Auth Methods dropdown in the Create Connector dialog showing all 6 options.

### Platform navigation

The Fastn dashboard uses **top navigation** with four main sections:

| Section          | Sub-tabs                                                                                                      | What it does                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Home**         | —                                                                                                             | Setup Assistants (AI-guided onboarding), setup checklist |
| **Integrations** | Connectors, Connections, Workflows, Triggers                                                                  | Build and manage everything                              |
| **Activity**     | Events, Traces, Alerts, Executions                                                                            | Monitor and debug                                        |
| **Settings**     | People, General, API Keys, Secrets, Environments, OAuth Apps, Billing, Customers, Audit Log, ADVANCED → Roles | Configure the platform                                   |

#### Home

The first thing you see after login. Shows the **Setup Assistants** — a 5-step guided onboarding powered by AI agents:

1. Research your SaaS (\~1 min, automatic)
2. Set up your connector (\~5 min)
3. Build the integration (\~10 min)
4. Configure widget (coming soon)
5. Setup complete

The right sidebar shows **YOUR SETUP** progress and **AFTER YOUR FIRST CUSTOMER CONNECTS** with locked advanced features (Pricing tiers, Real-time events, OAuth configuration, Custom domain, Workflow templates).

> **📷Screenshot needed:** Home page showing the Setup Assistants panel with the research output and the right sidebar checklist.

### Roles

Six system roles control access. Found under **Settings → ADVANCED → Roles**:

| Role          | Permissions | Description                                   |
| ------------- | ----------- | --------------------------------------------- |
| **Owner**     | 39          | Full access within organization and customers |
| **Admin**     | 39          | Full access within organization and customers |
| **Developer** | 34          | Build connectors, workflows, agents           |
| **Operator**  | 18          | Operational access                            |
| **Viewer**    | 7           | Read-only access                              |
| **End User**  | 9           | Customer-facing widget access                 |

Permission categories: Connectors, Connections, Workflows, Agents, Tools. Each has granular actions: create, read, update, delete, execute, deploy test, deploy prod, share.

You can also **create custom roles** by clicking "Create Custom Role" or duplicating a system role with "Duplicate as Custom."

> **Screenshot needed:** Settings → ADVANCED → Roles page showing the 6 system roles with permission counts.

### API Keys

Two types of API keys, managed under **Settings → API Keys**:

| Type     | Purpose                     |
| -------- | --------------------------- |
| **Test** | For development and testing |
| **Live** | For production use          |

Create keys with **"+ Create API Key"**. Keys authenticate API requests via the `x-fastn-api-key` header.

### Secrets

Encrypted values your workflows can read at runtime. Managed under **Settings → Secrets**. Use these for sensitive credentials like third-party API tokens or database connection strings.

### Environments

Deployment environments for workflows. Managed under **Settings → Environments**. Separate your development, staging, and production configurations.

### Alerts

Metric-based alert rules configured under **Activity → Alerts**. Each alert has:

* **Name** — e.g., "High Error Rate"
* **Condition** — one of: error rate, latency p99, latency p95, latency avg, throughput, failure count
* **Threshold** — the value that triggers the alert (e.g., 5 for 5% error rate)

***

**Next:** [Platform Overview →](https://claude.ai/chat/platform-overview.md)
