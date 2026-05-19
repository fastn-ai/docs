---
description: >-
  This page shows how Fastn's components connect to each other and where each
  piece fits in the architecture. Use it as a reference map when you're building
  integrations.
---

# Platform Overview

> **Diagram:** Architecture overview: SaaS App → Embedded Widget → Fastn Platform (Connectors, Workflows, Triggers, CDM, Event System, AI Agents) → Third-Party Apps. Show customer isolation boundary and MCP Gateway.

### Dashboard layout

The dashboard uses **top navigation** with five main sections:

#### Home

Your landing page after login. Contains:

**Setup Assistants** — A 5-step guided onboarding flow powered by AI agents:

| Step           | What happens                                                                           | Time                |
| -------------- | -------------------------------------------------------------------------------------- | ------------------- |
| 1. Research    | AI agent researches your company, industry, competitors, and integration opportunities | \~1 min (automatic) |
| 2. Connectors  | Set up your first connector with credentials                                           | \~5 min             |
| 3. Integration | Build the integration — plan + workflows                                               | \~10 min            |
| 4. Widget      | Configure the customer-facing widget                                                   | Coming soon         |
| 5. Done        | Setup complete — ready to use                                                          | —                   |

{% hint style="info" %}
**After your initial setup and overall onboarding is complete,** locked features that become available after your first customer connects: Pricing tiers, Real-time events, OAuth configuration, Custom domain, Workflow templates.
{% endhint %}

> **Screenshot:** Home page showing the full layout — Setup Assistants panel with AI output, the 5-step stepper at top, and the right sidebar checklist.

#### Integrations

Where you build everything. Four sub-tabs:

| Sub-tab         | What it does                                                                                                                                                                                                                                    |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Connectors**  | Create and manage connectors. Cards show name, description, creator, connection status. Buttons: **+ Create** (manual) and **Build with AI** (Connector Agent).                                                                                 |
| **Connections** | Manage active authenticated connections to third-party apps.                                                                                                                                                                                    |
| **Workflows**   | Create and manage workflows. Table shows name, status (active), version, updated date, and actions (Run, Delete). Buttons: **Create Workflow** (code editor) and **Build with AI** (Workflow Agent). Filter tabs: All, Instant, Standard, Long. |
| **Triggers**    | Create and manage triggers separately from workflows. Three tabs: Webhooks, Schedulers, App Events. Button: **Add Trigger**.                                                                                                                    |

> **Screenshot:** Integrations page showing the four sub-tabs (Connectors, Connections, Workflows, Triggers).

#### Widgets

Where you build the customer-facing integration hub. The **Widget Builder** has two panels:

1. **Builder:**

> **GIF:** Overview of widget builder on the left hand side

| Tab          | What it configures                                                                                                               |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| **Layout**   | Title, subtitle, and workflow templates (Use Templates with + Add)                                                               |
| **Style**    | Theme presets, color tokens, typography, border radii, shadows. Exportable as CSS variables or JSON tokens.                      |
| **Features** | Widget Filter, RBAC (both Coming Soon)                                                                                           |
| **Embed**    | Two methods: React SDK (`@fastn/react` with `<FastnHub>` component) or Headless SDK (`@fastn/headless` with `createFastnClient`) |

The builder also shows an **INTEGRATIONS** list where you add, edit, reorder, and delete widget integrations.

2. **Live Preview**

> **GIF:** Overview of preview on the right hand side

| Preview tab   | What it shows                                                                                                               |
| ------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Apps**      | Connected integrations with Configure/Disconnect buttons. AI assistant at bottom: "Can't find what you need? Build with AI" |
| **Workflows** | Active workflows with visualizer, plus Use Template cards that launch Integration Agent sessions                            |
| **Insights**  | KPI cards (Runs Today, Records Processed, Needs Attention), connector status, most-used workflow                            |

> **Screenshot:** Widget Builder showing the left panel with Layout tab and right panel with Live Preview (Apps tab).

#### Activity

Where you monitor everything. Four sub-tabs:

| Sub-tab        | What it shows                                                                                                                            | Filter tabs                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Events**     | Incoming and outgoing integration events. Auto-refresh toggle.                                                                           | All, Webhook, Scheduled, Manual          |
| **Traces**     | Connector execution traces and performance.                                                                                              | All, Success, Error, Pending             |
| **Alerts**     | Alert rules for monitoring connector and workflow performance. Conditions: error rate, latency (p99/p95/avg), throughput, failure count. | —                                        |
| **Executions** | Workflow execution history. Columns: Time, Workflow, Tier, Version, Status, Duration, Triggered By.                                      | All, Running, Completed, Failed, Timeout |

> **Screenshot:** Activity → Executions page showing the execution table with all columns populated.

#### Settings

Platform configuration. Left sidebar within Settings:

| Section              | What it does                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **People**           | Manage users, teams, and roles. Invite users, assign roles, filter by role/status/team.                                                                                   |
| **General**          | Organization name, timezone, domain & access control (email domain, auto-approve toggle).                                                                                 |
| **API Keys**         | Create and manage Test and Live API keys for programmatic access.                                                                                                         |
| **Secrets**          | Encrypted values your workflows can read at runtime.                                                                                                                      |
| **Environments**     | Deployment environments for workflows (dev, staging, production).                                                                                                         |
| **OAuth Apps**       | Fastn-managed OAuth apps — authenticate connectors without setting up your own OAuth app.                                                                                 |
| **Billing**          | Current plan (Free), usage stats, quota usage table with enforcement modes. Customize customer limits.                                                                    |
| **Customers**        | Create and manage customers (your end users). Each gets isolated credentials and data.                                                                                    |
| **Audit Log**        | Track all actions across your organization. Filter by user, action, type, date range. Columns: Timestamp, User, Action, Resource, Outcome.                                |
| **ADVANCED → Roles** | 6 system roles (Owner, Admin, Developer, Operator, Viewer, End User) + custom roles. Per-role permission matrix across Connectors, Connections, Workflows, Agents, Tools. |

> **Screenshot:** Settings page showing the left sidebar with all sections visible.

### How the pieces connect

Here's the flow of a typical integration, end to end:

#### 1. You set up (Home)

The Setup Assistants guide you through:

* AI researches your company and recommends connectors
* You create and authenticate a connector
* You build a workflow (via code or AI)
* You configure triggers to connect events to workflows

#### 2. Customer connects (Widget)

Your customer opens your product, sees the embedded widget, and connects their app (e.g., their Shopify store). Fastn handles the OAuth flow and stores their credentials isolated from all other customers.

#### 3. Event triggers (Triggers)

Something happens in the customer's connected app — a new order, an updated contact. The trigger receives the event and routes it to the matching workflow.

#### 4. Workflow executes (Workflows)

The workflow runs against the customer's data using their credentials. It fetches, transforms, and writes data between systems. The execution is logged under Activity → Executions.

#### 5. Monitoring (Activity)

You see every execution, event, trace, and alert under Activity. Filter by workflow, status, time range. Set up alert rules to catch errors automatically.

### Customer isolation

Every entity in Fastn is scoped to a customer:

```
Your Organization
├── Customer A (Acme Corp)
│   ├── Connections: Acme's Shopify token, Acme's Slack token
│   ├── Executions: Only Acme's workflow runs
│   └── Data: Only Acme's orders, contacts, invoices
├── Customer B (Widget Inc)
│   ├── Connections: Widget's Shopify token, Widget's HubSpot token
│   ├── Executions: Only Widget's workflow runs
│   └── Data: Only Widget's orders, contacts, invoices
```

Workflows are defined once by you but execute per-customer using each customer's own connections and data.

### API access

API requests require these headers:

| Header            | Purpose                                           |
| ----------------- | ------------------------------------------------- |
| `x-fastn-api-key` | Your API key (Settings → API Keys — Test or Live) |
| `Content-Type`    | `application/json`                                |

### Plan and quotas

The platform starts on the **Free** plan. Visible quota dimensions from Settings → Billing:

| Dimension            | Free plan default | Enforcement |
| -------------------- | ----------------- | ----------- |
| Events per day       | 500               | Hard Block  |
| Events per minute    | 10                | Hard Block  |
| API calls per day    | 1,000             | Hard Block  |
| API calls per minute | 20                | Hard Block  |

You can customize limits per customer with the **"Customize Customer Limits"** button on the Billing page.

> **Screenshot:** Settings → Billing showing the quota usage table with dimensions, defaults, usage bars, and enforcement modes.

### Security model

**Authentication** — Keycloak-based OIDC with JWT tokens. Social login via GitHub and Google.

**Authorization (RBAC)** — 6 system roles (Owner, Admin, Developer, Operator, Viewer, End User) with granular permissions across Connectors, Connections, Workflows, Agents, and Tools. Custom roles supported.

**Data isolation (RLS)** — Row-Level Security policies on PostgreSQL tables ensure customer data is isolated at the database level.

**Data residency** — Customers can be configured for US, EU, or APAC data residency.
