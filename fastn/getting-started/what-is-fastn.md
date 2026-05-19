---
description: >-
  Embedded integration platform that lets SaaS companies offer native
  integrations without building connector infrastructure.
---

# What is Fastn

Fastn is an embedded integration platform that lets SaaS companies offer native integrations to their customers without building or maintaining connector infrastructure.

You embed Fastn into your product. Your customers connect their apps (Slack, HubSpot, Shopify, Xero, and others) through a branded widget inside your UI. Fastn handles authentication, data normalization, workflow execution, and monitoring behind the scenes.

### Who is Fastn for

Fastn is built for two audiences:

**SaaS companies (you)** — You have a product and your customers need integrations with third-party apps. You don't want to build and maintain connector infrastructure yourself. With Fastn, you configure connectors, build automation workflows, and embed a branded integration hub into your product. You manage everything from the Fastn dashboard at `live.fastn.ai`.

**Your customers** — The people who use your SaaS product. They interact with Fastn through the embedded widget inside your app — connecting their own accounts (their Slack workspace, their HubSpot instance, their Shopify store), activating integrations, and viewing sync status. They never see the Fastn dashboard or know that Fastn exists behind the scenes.

### What Fastn replaces

Without Fastn, SaaS companies typically face one of these situations:

* Building integrations in-house: a team maintains OAuth flows, API versioning, error handling, and data mapping for every third-party app per customer.
* Using an integration marketplace like Zapier or Make: works for simple triggers, but doesn't give you a native, branded experience inside your product.
* Hiring a systems integrator: expensive, slow, and creates a dependency on external consultants for every new connector.

Fastn replaces all of these with a single platform. You embed once, configure connectors and workflows, and every customer gets isolated, working integrations with no additional engineering effort from your side. Built-in AI agents handle connector building, workflow creation, testing, and operations so your team spends less time on integration support.

### Core product areas

Fastn has four core product areas visible in the dashboard:

#### Connectors

Pre-built or AI-generated integrations with third-party apps. Fastn provides connectors for apps like Shopify, Stripe, Xero, QuickBooks, Slack, HubSpot, GitHub, and others — or you can build your own using the **Connector Agent** or the **+ Create** button.

Each connector defines:

* **Authentication** — OAuth 2.0, API Key, Bearer Token, Basic Auth, Custom, or No Auth
* **Actions** — things you can do (create a contact, fetch orders, send a message)
* **Events** — webhook events you can subscribe to (new order created, contact updated)

Once a connector exists, you or your customers create **Connections** — authenticated instances that store credentials per user.

You manage connectors under **Integrations → Connectors** and connections under **Integrations → Connections**.

> **Screenshot:** Integrations → Connectors page showing connector cards with + Create and Build with AI buttons.

#### Workflows

The automation backbone. Workflows define what happens when data needs to move between systems. You write them in JavaScript/TypeScript using a code editor — each workflow is an `async function(ctx)` that receives input and headers, processes data, and returns a result.

Example: When a new order lands in Shopify, fetch the customer details, normalize the data, create an invoice in Xero, and send a confirmation to Slack.

Workflows support three execution tiers:

* **Instant** — synchronous, returns result inline, max 60 seconds
* **Standard** — default async execution
* **Long** — extended execution for large data volumes

You manage workflows under **Integrations → Workflows**.

> **Screenshot:** Integrations → Workflows page showing the workflow table with status, version, tier columns.

> **Screenshot:** Workflow code editor showing the default `export default async function(ctx)` template with the Configuration panel on the left and Test panel on the right.

#### Triggers

Triggers connect external events to your workflows. They're managed as a separate section — you create a trigger, then route it to one or more workflows.

Three trigger types:

* **Webhook** — receives HTTP POST events from external services. Supports routes with JSON filters to direct different payloads to different workflows.
* **Scheduler** — runs workflows on a schedule (every 5 minutes, daily, weekly, monthly, or custom cron).
* **App Event** — subscribes to events from your connectors (e.g., "Sale Created" from Cin7, "Contact Updated" from HubSpot).

You manage triggers under **Integrations → Triggers**.

> **Screenshot:** Integrations → Triggers page showing the three tabs (Webhooks, Schedulers, App Events) and the Add Trigger button.

#### Widgets

The customer-facing piece. The **Widget Builder** (under **Widgets** in the top nav) lets you create an embeddable integration hub that lives inside your product. Your customers use it to connect their apps, view workflows, configure field mappings, and monitor sync status — all without leaving your app.

The Widget Builder has four configuration tabs:

* **Layout** — title, subtitle, and workflow templates
* **Style** — theme presets, colors, typography, borders, shadows
* **Features** — widget filter and RBAC (coming soon)
* **Embed** — two integration methods: React SDK (`@fastn/react`) or Headless SDK (`@fastn/headless`)

The live preview shows three tabs your customers will see:

* **Apps** — connected integrations with Configure/Disconnect buttons and an AI assistant ("Build with AI")
* **Workflows** — active workflows and workflow templates
* **Insights** — KPIs (runs today, records processed, needs attention), connector status, most-used workflow

> &#x20;**Screenshot:** Widget Builder showing the left panel (Layout tab) and right panel (Live Preview with Apps tab showing connected integrations).

### AI agents across the platform

Fastn uses AI agents powered by Anthropic Claude to reduce manual work throughout the platform. These aren't a separate product they're built in and accessible via **"Build with AI"** buttons on the Connectors, Workflows, and Widgets pages, and through the **Setup Assistants** on the Home page.

15 specialized agents are available, organized by function:

**Onboarding & Intelligence**

| Agent                  | What it does                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| **SaaS Onboarding**    | Guides SaaS companies through the 5-step setup stepper (Research → Connectors → Integration → Widget → Done) |
| **Tenant Onboarding**  | Helps customers connect tools, map fields, configure syncs via the widget                                    |
| **Intelligence Brief** | Multi-agent graph that researches companies and produces integration strategy briefs                         |
| **Planner Agent**      | Analyzes integration requirements, asks clarifying questions, produces build plans                           |

**Building & Configuration**

| Agent                              | What it does                                                                  |
| ---------------------------------- | ----------------------------------------------------------------------------- |
| **Connector Builder**              | Creates connectors with auth setup, API actions, and webhook events           |
| **Connector Agent (Orchestrator)** | Orchestrator-managed connector builder with handback support                  |
| **Workflow Builder**               | Builds workflows from a plan, validates against test cases                    |
| **Workflow Agent (Orchestrator)**  | Orchestrator-managed workflow builder with handback support                   |
| **Event Builder**                  | Creates webhook events and configures subscribe/unsubscribe lifecycle         |
| **Configuration Agent**            | Probes live APIs to gather sample data, defines filter conditions and targets |

**API & Spec Management**

| Agent                     | What it does                                                             |
| ------------------------- | ------------------------------------------------------------------------ |
| **Spec Import Builder**   | Finds and imports machine-readable API specs (OpenAPI, Swagger, Postman) |
| **Manual Action Builder** | Creates API actions one-by-one from docs when no spec exists             |

**Testing & Quality**

| Agent               | What it does                                                         |
| ------------------- | -------------------------------------------------------------------- |
| **Test Case Agent** | Generates executable integration test cases for workflows            |
| **Action Tester**   | Executes actions against real test connections and reports pass/fail |
| **Action Fixer**    | Fixes broken actions using real API docs, applies schema patches     |

> **GIF needed:** The SaaS Onboarding agent in action on the Home page — the Setup Assistants panel researching a company and producing recommendations.

### How data flows through Fastn

> **Diagram needed:** Visual flow: Event source (webhook/schedule/API) → Trigger → Workflow execution → CDM Normalization → Target System. Show customer isolation boundary.

1. **Event arrives** — A webhook fires from Shopify, a scheduler triggers, or an app event is received.
2. **Trigger routes** — The trigger matches the event to one or more workflows via routes and filters.
3. **Workflow executes** — Fastn runs your workflow code: fetch data, transform it, write to a target system.
4. **Data normalizes** — The Canonical Data Model (CDM) translates between different systems' data formats.
5. **Customer isolation** — Every piece of data is scoped to a specific customer. Your customers never see each other's data, credentials, or execution history.
6. **Monitoring** — Every execution is logged under **Activity → Executions** with workflow name, tier, version, status, duration, and what triggered it.

### What you need to get started

* A SaaS product where your customers need third-party integrations
* A Fastn account (sign up at [fastn.ai](https://fastn.ai/))
* Basic familiarity with JavaScript/TypeScript (for writing workflows via code)
* Frontend capability to embed the widget (when available)

No infrastructure setup required. Fastn runs as a managed service.

{% hint style="info" %}
If you do not have any coding experience, you can simply build a workflow or an integration through our "Build with AI" feature.
{% endhint %}
