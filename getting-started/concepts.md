---
description: The handful of ideas that everything else in fastn is built from.
---

# Core concepts

### Organization, customer, connection

An **organization** is you, the SaaS company. It holds your connectors, workflows, widgets, people and settings.

A **customer** is one of your customers. Every customer is isolated: its connections, credentials and data never cross into another. Some identifiers and older material say *tenant*. API calls name a customer with `x-org-id` (or `orgId` in a query or body): your own id for it, which defaults to the customer's slug if you did not set one, or fastn's id for it. Answers name the customer by your own id, as `orgId`.

A **connection** is one customer's authorized link to one app. It stores the credential, encrypted, and records which auth method produced it.

```
Organization (you)
├── Customer A
│   ├── Connection → HubSpot   (OAuth)
│   └── Connection → Cin7 Core (API key)
└── Customer B
    └── Connection → Salesforce (OAuth)
```

Every connection has an id in the form `ucl:<workspace>:<customer or default>:<connectorId>:<identity>[:<account>]`. The detail page shows it with the line *Pass this to the API to act as this customer.* In the customer segment you can use your own id for the customer, and answers to your API key show it that way. When you call a workflow on a customer's behalf, the customer is identified in request headers: `x-org-id`, `x-installation-id`, `x-fastn-connections` and `x-fastn-installation-config`.

### Connector versus connection

A **connector** is the definition: this API, these actions, these auth methods, this webhook config. A **connection** is an instance of it for one customer. One connector, many connections.

Connectors are either **managed by fastn**, maintained upstream and patched when the vendor changes something, or **custom**, created by you.

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

Instant's 25-second ceiling rises to 2 minutes only for organizations where fastn has turned on the longer Instant timeout. Long runs for up to 36 hours. Pick Instant only when something is waiting on the answer. Most syncs are Standard.

### Test and live

fastn separates *what the code is* from *where it runs*.

* **Versions** are snapshots created by Publish, numbered v1, v2, … in the workflows list.
* **Environments** are where versions are deployed. `test` and `live` are built in and protected; you can add named ones such as `staging`, and mark any environment **Requires review** so promoting to it opens a pull request on a connected GitHub repository instead of deploying straight away.
* **API keys** carry a mode, `Test` or `Live`. A Test key is refused unless the caller sends `X-fastn-Test-Mode: true`.

{% hint style="warning" %}
Test mode is not a sandbox. A test key reaches the same live connections as a live key and causes the same real writes. It is a separate credential, not a safe one.
{% endhint %}

### Triggers

Three kinds, covered fully in [Triggers](../build/triggers/README.md).

* **Webhook**: an outside app calls a URL you give it.
* **Schedule**: a clock you set.
* **App event**: something changed in a connected app.

### Unified APIs

Where several providers do the same job (HubSpot, Salesforce and Zoho all hold contacts), fastn exposes one canonical endpoint per entity and routes to whichever provider that customer connected. Your code calls `/api/v1/unified/crm/contact` and does not branch on the CRM.

The categories and entities available depend on the unified API catalog in your workspace, and the list grows over time; CRM contacts are a typical example. See [Unified APIs](../build/unified-apis/README.md) for how to browse what is available.

### Build with AI

fastn's builder, **Build with AI**, is not autocomplete. It discovers API specs, creates connectors, wires auth, proposes field mappings, generates test cases and writes the workflow, and it shows you a diff before anything runs. You review; it builds.

### The MCP gateway

Everything you build can also be exposed to an AI client as tools, with the same customer scoping and permission model. See [MCP gateway](../build/mcp-gateway/README.md).
