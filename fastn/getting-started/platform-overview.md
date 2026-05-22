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

The Home page has two states depending on where you are in the setup process.

**During onboarding (Signing up as a new user):**

When you sign into Fastn as a new user, a Setup Assistant will activate prompting you to place in your company's website. The Setup Assistant will then guide you through a setup pipeline which consist of five steps:

1. **Use cases —** What your customers need to integrate.
2. **Connectors —** The integration building blocks your platform offers.
3. **Workflows —** The integration logic that connects with the connectors and triggers.
4. **Embed —** The customer-facing experiecing inside your product.
5. **Live —** Deployed on your platform and ready for your customer.

On the backend, AI agents research your company, recommend connectors, and help you build your first integrations. The right sidebar tracks your progress per setup pipeline.

{% hint style="info" %}
If you want to test your workflows before embedding and deploying, you can simply stop the onboarding and then head to the **Integrations** section to test your existing workflows or build new ones.
{% endhint %}

{% hint style="info" %}
You can reset onboarding anytime from **Settings → General → Reset Onboarding**. This wipes your onboarding state and reruns the full pipeline. However, it deletes your qualification wizard answers and every Setup Assistant thread.
{% endhint %}

> **Screenshot needed:** Home page during onboarding showing the Setup Assistants panel with the 5-step stepper.

**After onboarding (daily use):**

If you have already gone through the onboarding process, the Home page becomes your AI-powered command center which allows you to simply prompt in what you want to build and the agents on the backend will do the rest.

In the post-onboarding Home page, you can see:

* Recommended prompts and actions that you can execute.
* Your current active connectors.
* Your current events scheduled for today (if available or created).
* An activity card that redirects you to view integration events.
* A button to enable data sync.
* Credits counter (top-right) which shows usage credits remaining.

This is the primary way you interact with Fastn. Instead of navigating to different sections and manually configuring things, you describe what you need and the AI handles it.

> **Screenshot: Main home page post onboarding**

#### Integrations

Where you build everything and consists of four sub-tabs:

| Sub-tab         | What it does                                                                                                                                                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Connectors**  | Create and manage connectors. Cards show name, description, creator, connection status. Buttons: **+ Create** (manual) and **Build with AI** (Connector Agent).                                                                    |
| **Connections** | Manage active authenticated connections to third-party apps.                                                                                                                                                                       |
| **Workflows**   | Create and manage workflows. You can view the workflow name, status (active), version, updated date, and actions you can take. Additionally you can filter different types of workflows such as "Instant", "Standard", and "Long". |
| **Triggers**    | Create and manage triggers separately from workflow which consists of three categories i.e. Webhooks, Schedulers, App Events.                                                                                                      |

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

Before deployment of your widget, you can do a complete live preview of how your widget will look and work like for your customers. The Live Preview section consists of the following&#x20;

> **GIF:** Overview of preview on the right hand side

| Preview tab   | What it shows                                                                                                               |
| ------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Apps**      | Connected integrations with Configure/Disconnect buttons. AI assistant at bottom: "Can't find what you need? Build with AI" |
| **Workflows** | Active workflows with visualizer, plus Use Template cards that launch Integration Agent sessions                            |
| **Insights**  | KPI cards (Runs Today, Records Processed, Needs Attention), connector status, most-used workflow                            |

> **Screenshot:** Widget Builder showing the left panel with Layout tab and right panel with Live Preview (Apps tab).

#### Activity

Where you monitor everything which consists of four sub-tabs:

| Sub-tab        | What it shows                                                                                                                            | Filter tabs                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Events**     | Incoming and outgoing integration events. Auto-refresh toggle.                                                                           | All, Webhook, Scheduled, Manual          |
| **Traces**     | Connector execution traces and performance.                                                                                              | All, Success, Error, Pending             |
| **Alerts**     | Alert rules for monitoring connector and workflow performance. Conditions: error rate, latency (p99/p95/avg), throughput, failure count. | No filter tabs                           |
| **Executions** | Workflow execution history which are categorized by Time, Workflow, Tier, Version, Status, Duration, Triggered By.                       | All, Running, Completed, Failed, Timeout |

> **Screenshot:** Activity → Executions page showing the execution table with all columns populated.

#### Settings

Platform configuration. Left sidebar within Settings:

| Section              | What it does/contains                                                                                                                                                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **People**           | Manage users, teams, and roles. Invite users, assign roles, filter by role/status/team.                                                                                                                                                  |
| **General**          | Organization name, timezone, domain & access control (email domain, auto-approve toggle), Reset Onboarding.                                                                                                                              |
| **API Keys**         | Create and manage Test and Live API keys for programmatic access.                                                                                                                                                                        |
| **Secrets**          | Encrypted values your workflows can read at runtime.                                                                                                                                                                                     |
| **Environments**     | Deployment environments for workflows (dev, staging, production).                                                                                                                                                                        |
| **OAuth Apps**       | Fastn-managed OAuth apps that allows you authenticate connectors without setting up your own OAuth app.                                                                                                                                  |
| **Billing**          | Shows your current plan, usage stats, quota usage table with enforcement modes. This also includes customer tier setup and creation and an analysis of customer usage breakdown per execution, events, integrations, users, and storage. |
| **Customers**        | Create and manage customers (your end users). Each gets isolated credentials and data with a tier defined if created in the billing section.                                                                                             |
| **Audit Log**        | Track all actions across your organization. Filter by user, action, type, date range. Columns: Timestamp, User, Action, Resource, Outcome.                                                                                               |
| **ADVANCED → Roles** | 6 system roles (Owner, Admin, Developer, Operator, Viewer, End User) + custom roles. Per-role permission matrix across Connectors, Connections, Workflows, Agents, Tools.                                                                |

> **Screenshot:** Settings page showing the left sidebar with all sections visible.

### How the pieces connect

Here's the flow of a typical integration, end to end:

#### 1. You describe what you need (Home)

On the Home page, tell the AI what integration you want such as:

> "Sync HubSpot contacts to Cin7 customers, matching by email"

The AI agents will:

* Discover the HubSpot and Cin7 APIs
* Build connectors with auth, actions, and events
* Create a workflow that syncs the data
* Set up triggers to run it on schedule or on events
* Configure field mappings between the two systems
* Test everything

In the end, you get to review the result and either publish or make more changes if needed.

#### 2. Customer connects (Widget)

Your customer opens your product, sees the embedded widget, and connects their app (e.g., their Shopify store). Fastn handles the OAuth flow and stores their credentials isolated from all other customers.

#### 3. Event triggers (Triggers)

Something happens in the customer's connected app such as a new order, an updated contact. The trigger receives the event and routes it to the matching workflow.

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

For programmatic access, API requests require:

| Header                      | Purpose                                          |
| --------------------------- | ------------------------------------------------ |
| `x-fastn-access-key`        | Your API key (Settings → API Keys. Test or Live) |
| `x-fastn-account-id`        | Your account ID                                  |
| `x-fastn-account-tenant-id` | Customer ID for customer-scoped operations       |
| `Content-Type`              | `application/json`                               |

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
