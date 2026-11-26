---
description: The handful of ideas that everything else in Fastn is built from.
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

# Core concepts

These are the terms used across the dashboard and these docs. For one-line definitions, see the [Glossary](../reference/glossary.md).

### The building blocks

* **Connectors:** A connector is the definition of one external app's API, such as HubSpot, Jira or Stripe. It covers the app's actions, its auth methods (how users sign in to it) and its webhook events, and it holds no credentials. You can use one from Fastn's managed catalog, which Fastn keeps up to date when the vendor changes its API, or create your own. [Docs](../build/connectors/README.md) · [Open in Fastn](https://app.fastn.dev/integrations)
* **Connections:** A connection is one signed-in account on one connector. It is created when someone on your team or one of your customers authorizes access. Fastn stores the credential encrypted, scopes it to that owner and refreshes OAuth tokens, so nobody has to sign in again. One connector can have many connections. [Docs](../build/connections/README.md) · [Open in Fastn](https://app.fastn.dev/connections)
* **Workflows:** A workflow is the code that runs an integration. It is a JavaScript module that exports one function and calls connector actions, for example to read records from one app, transform them and write them to another. You publish numbered versions and deploy them to environments such as `test` and `live`. [Docs](../build/workflows/README.md) · [Open in Fastn](https://app.fastn.dev/integrations?tab=workflows)
* **Triggers:** A trigger starts a workflow on its own. It can be a webhook (an outside app calls a URL you give it), a schedule (a clock you set) or an app event (something changed in a connected app). A workflow without a trigger runs only when something calls it. [Docs](../build/triggers/README.md) · [Open in Fastn](https://app.fastn.dev/integrations?tab=triggers)
* **Unified APIs:** A unified API gives you one endpoint per business entity, such as a CRM contact. It sends each call to whichever provider that customer connected, such as HubSpot, Salesforce or Zoho, so your code doesn't branch per app. [Docs](../build/unified-apis/README.md) · [Open in Fastn](https://app.fastn.dev/integrations?tab=unified)
* **Widget:** The widget is the panel you embed in your product. Your customers use it to browse the integrations you offer, sign in to their own apps and turn integrations on. It carries your branding, and customers don't need a Fastn account. [Docs](../embed/widget-builder/README.md) · [Open in Fastn](https://app.fastn.dev/widgets)

### How a build fits together

<figure><img src="../.gitbook/assets/lifecycle/fastn-lifecycle.svg" alt="The Fastn integration lifecycle: who does what across Build, Publish, Embed, Customize, and Run and monitor"><figcaption><p>Who does what: your team, your customer, and Fastn</p></figcaption></figure>

1. Describe the integration to the Fastn agent or your AI tool, or write it in code.
2. The agent picks or creates the connectors and sets up authentication.
3. It drafts the workflow and its test cases, and shows you the diff.
4. You attach a trigger, publish a version, and deploy it to an environment.
5. You add the integration to your widget, and customers turn it on.
6. You watch runs in **Logs** and set an alert so failures are not silent.

What you can see in the dashboard depends on your role: **Owner**, **Admin**, **Developer**, **Operator**, or **Viewer**. People at your customers who use the widget have the **End User** role and never sign in to Fastn. See [Roles](../manage/roles.md).

### Organization, customer, connection

An **organization** is you, the company that builds the product. It holds your connectors, workflows, widgets, people, and settings.

A **customer** is one of your customers. Every customer is isolated: its connections, credentials, and data never cross into another. Some identifiers and older material say *tenant*.

Inside Fastn, each customer is its own small organization under yours. That is why the header that names a customer is called `x-org-id`: it never names your organization, which Fastn already knows from your API key or login.

API calls name a customer with `x-org-id` (or `orgId` in a query or body). The value can be either:

* your own id for the customer, which defaults to its slug if you did not set one, or
* Fastn's id for it.

Answers name the customer by your own id, as `orgId`.

A **connection** is one customer's authorized link to one app. It stores the credential, encrypted, and records which auth method produced it.

```
Organization (you)
├── Customer A
│   ├── Connection → HubSpot   (OAuth)
│   └── Connection → Cin7 Core (API key)
└── Customer B
    └── Connection → Salesforce (OAuth)
```

Every connection has an id in the form `ucl:<workspace>:<customer or default>:<connectorId>:<identity>[:<account>]`. The detail page shows it with the line *Pass this to the API to act as this customer.* In the customer segment you can use your own id for the customer, and answers to your API key show it that way. When you call a workflow on a customer's behalf, the customer is identified in request headers: `x-org-id`, `x-installation-id`, `x-fastn-connections`, and `x-fastn-installation-config`.

### Connector versus connection

A **connector** is the definition: this API, these actions, these auth methods, this webhook config. A **connection** is an instance of it for one customer. One connector, many connections.

Connectors are either **managed by Fastn**, maintained upstream and patched when the vendor changes something, or **custom**, created by you.

### Per-customer versus platform-wide connectors

Inside a workflow, each connector is wired one of two ways.

| Mode              | Credential used                                  | Use for                                            |
| ----------------- | ------------------------------------------------ | -------------------------------------------------- |
| **Per customer**  | The connection belonging to the running customer | Anything touching customer data                    |
| **Platform-wide** | A single connection owned by your org, shared across the workspace | Your own apps: your Slack, your data warehouse |

Both modes are labeled in the UI: the workflow's Connectors tab shows a **Per customer** or **Platform-wide** badge on each connector. On the connection side, a connection that belongs to your organization rather than to one customer shows `Scope: Account level` on its detail page.

### Workflows are code

A workflow is a JavaScript module. The editor holds one file, `<slug>.js`, and it exports a single function:

```javascript
export default async function (ctx) {
  // ctx.input, ctx.headers (connectors are called as fastn.connector.<slug>.<action>())
}
```

There is no node palette and no drag-and-drop step builder. The editor's Diagram tab is AI-generated documentation of that code: a read-only picture that regenerates when the code has changed.

### Execution tiers

Every workflow declares how long it may run and how it answers the caller.

| Tier         | Behavior                                        | Returns       | Timeout range | Default |
| ------------ | ----------------------------------------------- | ------------- | ------------- | ------- |
| **Instant**  | Synchronous; the caller waits                   | Result inline | 1s - 25s      | 25s     |
| **Standard** | Asynchronous, run via Temporal                  | 202 Accepted  | 5s - 15min    | 2min    |
| **Long**     | Asynchronous, for large volumes                 | 202 Accepted  | 30s - 36h     | 15min   |

Instant's 25-second ceiling rises to 2 minutes only for organizations where Fastn has turned on the longer Instant timeout. Long runs for up to 36 hours. Pick Instant only when something is waiting on the answer. Most syncs are Standard.

### Test and live

Fastn separates *what the code is* from *where it runs*.

* **Versions** are snapshots created by Publish, numbered v1, v2, … in the workflows list.
* **Environments** are where versions are deployed. `test` and `live` are built in and protected; you can add named ones such as `staging`, and mark any environment **Requires review** so promoting to it opens a pull request on a connected GitHub repository instead of deploying directly.
* **API keys** carry a mode, `Test` or `Live`. A Test key is refused unless the caller sends `X-fastn-Test-Mode: true`.

Test keys act on real data. See [API keys](../manage/api-keys.md).

### Triggers

Three kinds, covered fully in [Triggers](../build/triggers/README.md).

* **Webhook**: an outside app calls a URL you give it.
* **Schedule**: a clock you set.
* **App event**: something changed in a connected app.

### Unified APIs

Where several providers do the same job (HubSpot, Salesforce, and Zoho all hold contacts), Fastn exposes one canonical endpoint per entity and routes to whichever provider that customer connected. Your code calls `/api/v1/unified/crm/contact` and does not branch on the CRM.

The categories and entities available depend on the unified API catalog in your workspace, and the list grows over time; CRM contacts are a typical example. See [Unified APIs](../build/unified-apis/README.md) for how to browse what is available.

### The Fastn agent

The **Fastn agent** is Fastn's own agent for building integrations, on paid plans (Scale or Enterprise). Start it from **Integrations → Create integration → Build with fastn agent** or the prompt on **Home**. It finds API specs, creates connectors, sets up authentication, proposes field mappings, generates test cases, and writes the workflow. It shows you a diff before anything runs, and it uses AI credits.

On any plan, you can build the same way from your AI tool, such as Claude or Cursor, through the Fastn MCP server. That uses no AI credits.

### The Fastn MCP server and Fastn Connect

Fastn has two MCP addresses. The **Fastn MCP server** (`mcp.fastn.dev/fastn-workspace`) lets your AI tool build and manage integrations in your workspace. **Fastn Connect**, the MCP gateway, gives your AI agents each customer's connected apps as tools, with the same customer scoping and permission model. A customer's own AI client can use it too. See [Fastn MCP server](../build/mcp-gateway/README.md) and [Which MCP do I need?](architecture.md#which-mcp-do-i-need).
