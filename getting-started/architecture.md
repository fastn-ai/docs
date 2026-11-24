---
description: How the parts of fastn fit together, who uses each one, and how a request moves from your product to a customer's app.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Architecture

fastn sits between your product and the apps your customers use. Your team builds integrations once; each customer connects their own accounts; fastn runs the integrations for each customer with that customer's sign-in.

<figure><img src="../.gitbook/assets/diagrams/architecture.svg" alt="fastn architecture. Your team builds in the fastn dashboard or from an AI tool through the fastn MCP server. Your backend holds the API key and uses the API and SDK to get embed tokens and start runs. Your customer uses the widget inside your product to connect apps, which stores a connection per customer. Integrations hold connectors, workflows and triggers, and the workflow runtime runs them once per customer with that customer's connections. The maintainer agent watches apps and proposes fixes, fastn Connect gives your AI agents each customer's apps as tools, and Health and Logs record every run and event."><figcaption>Purple is your side, green is your customer's side, and gray is fastn.</figcaption></figure>

## The parts

| Part | What it does | Who uses it |
| --- | --- | --- |
| [fastn dashboard](platform-tour.md) | Build integrations, set up the widget, watch every run. At `app.fastn.dev`. | Your team |
| [fastn MCP server](../build/mcp-gateway/README.md) | Lets an AI tool such as Claude or Cursor build and manage integrations in your workspace. At `mcp.fastn.dev/fastn-workspace`. | Your team, from an AI tool |
| [Integrations](../build/integrations.md) | Connectors (one per app), workflows (the code that runs) and triggers (what starts a run). | Built by your team |
| [API and SDK](../reference/api.md) | Your backend mints embed tokens, runs workflows, and reads or writes customer data through unified APIs. Authenticated with an API key that never leaves your server. | Your backend |
| [Widget](../embed/README.md) | The panel inside your product where a customer connects apps and adjusts each integration. Opened with a short-lived embed token. | Your customers |
| [Connections](../build/connections/README.md) | One signed-in account per customer per app. Each customer's connections are isolated from every other customer's. | Created by your customers, or by you for them |
| Workflow runtime | Runs a workflow for one customer at a time, with that customer's connections and configuration. | fastn |
| [fastn Connect](../reference/ai-agents.md) | The MCP gateway: gives your AI agents one customer's connected apps as tools, with policies and audit logs. | Your AI agents |
| [Maintainer agent](../build/connector-updates.md) | Watches the apps you connect to, detects API changes, and proposes fixes for your team to accept. | fastn, reviewed by your team |
| [Health](../operate/health.md) and [Logs](../operate/README.md) | What needs attention now, and every event and run as it happened. | Your team |

## How a request flows

### A customer connects an app

1. Your backend asks fastn for an embed token for one customer, using your API key.
2. Your product opens the widget with that token.
3. The customer signs in to an app in the widget. fastn stores the result as a connection for that customer.

See [Authentication](../tutorials/developer/authentication-and-api-keys.md) for the full flow, including identity verification.

### An integration runs

1. A trigger fires: an event from an app, a schedule, a webhook from your product, or an API call from your backend.
2. The workflow runtime starts one run for the customer the trigger names.
3. The workflow calls the customer's apps through their connections, and the run is recorded in **Operate → Logs**.

See [Run an integration for a customer](../how-to/run-for-a-customer.md).

### An AI agent acts for a customer

1. Your agent connects to fastn Connect at your organization's address, `https://mcp.fastn.dev/<your-org>`, and acts for one customer. A customer's own AI client, such as Claude, connects with a one-time [customer MCP URL](../embed/embedding/customer-mcp-url.md) instead.
2. It sees that customer's connected apps as tools, filtered by your policies.
3. Each call runs with the customer's connection and is logged.

### An app changes its API

1. The maintainer agent detects the change and proposes a patch to the connector.
2. The proposal waits in **Operate → Health → Pending updates**. Nothing changes until your team accepts it.
3. Once accepted, the fix applies to every customer that uses the connector.

## Which MCP do I need?

fastn has two MCP addresses for two different jobs:

| You want to | Use | Address |
| --- | --- | --- |
| Build and manage integrations from Claude, Cursor or another AI tool | **fastn MCP server** | `https://mcp.fastn.dev/fastn-workspace` |
| Let your AI agent, or a customer's AI client, use a customer's connected apps | **fastn Connect** (the MCP gateway) | `https://mcp.fastn.dev/<your-org>`, or a one-time [customer MCP URL](../embed/embedding/customer-mcp-url.md) |

## Isolation

* Each customer is identified by `x-org-id` (or `orgId`). A run, a connection and a token always belong to exactly one customer.
* Connections and their credentials are never shared across customers.
* A customer can customize an integration for their own account without changing it for anyone else.
