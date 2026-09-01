---
description: The handful of ideas that everything else in fastn is built from.
---

# Core concepts

### Organisation, customer, connection

An **organisation** is you — the SaaS company. It holds your connectors, workflows, widgets, people and settings.

A **customer** is one of your customers. Every customer is isolated: its connections, credentials and data never cross into another. In older fastn material and in some API parameters this is called a *tenant*.

A **connection** is one customer's authorised link to one system. It stores the credential, encrypted, and records which auth method produced it.

```
Organisation (you)
├── Customer A
│   ├── Connection → HubSpot   (OAuth)
│   └── Connection → Cin7 Core (API key)
└── Customer B
    └── Connection → Salesforce (OAuth)
```

Every connection has an id in the form `ucl:org_<org>:<env>:<connectorId>:<authId>:<tenant>` — the detail page shows it with the line *Pass this to the API to act as this customer.* When you call a workflow on a customer's behalf, the tenancy is carried in request headers: `x-end-org-id`, `x-end-org-ref`, `x-installation-id`, `x-fastn-connections` and `x-fastn-installation-config`.

### Connector versus connection

A **connector** is the definition: this API, these actions, these auth methods, this webhook config. A **connection** is an instance of it for one customer. One connector, many connections.

Connectors are either **managed by fastn** — maintained upstream, patched when the vendor changes something — or **custom**, created by you.

### Per-customer versus account-level connectors

Inside a workflow, each connector is wired one of two ways.

| Mode              | Credential used                                  | Use for                                            |
| ----------------- | ------------------------------------------------ | -------------------------------------------------- |
| **Per customer**  | The connection belonging to the running customer | Anything touching customer data                    |
| Account level     | A single connection owned by your org, shared across the workspace | Your own systems — your Slack, your data warehouse |

Only the first of these is labelled in the UI: the workflow's Connectors tab shows a **Per customer** badge, and a connection's detail page shows `Scope: Account level` when it is shared across the workspace.

### Workflows are code

A workflow is a JavaScript module. The editor holds one file, `<slug>.js`, and it exports a single function:

```javascript
export default async function (ctx) {
  // ctx.input, ctx.headers, ctx.connectors
}
```

There is no node palette and no drag-and-drop step builder. The editor's Diagram tab draws a picture *from* that code, and is read-only.

### Execution tiers

Every workflow declares how long it may run and how it answers the caller.

| Tier         | Behaviour                                       | Returns       | Timeout range | Default |
| ------------ | ----------------------------------------------- | ------------- | ------------- | ------- |
| **Instant**  | Synchronous; the caller waits                   | Result inline | 1s – 30s      | 30s     |
| **Standard** | Asynchronous, run via Temporal                  | 202 Accepted  | 5s – 15min    | 2min    |
| **Long**     | Asynchronous, for large volumes                 | 202 Accepted  | 30s – 36h     | 15min   |

Pick Instant only when something is waiting on the answer. Most syncs are Standard.

### Test and live

fastn separates *what the code is* from *where it runs*.

* **Versions** are snapshots created by Publish, numbered v1, v2, … in the workflows list.
* **Environments** are where versions are deployed. `test` and `live` are built in and protected; you can add named ones such as `staging`, and mark any environment **Requires review** so promoting to it opens a pull request on a connected GitHub repository instead of deploying straight away.
* **API keys** carry a mode, `Test` or `Live`. A Test key is refused unless the caller sends `X-fastn-Test-Mode: true`.

{% hint style="warning" %}
Test mode is not a sandbox. A test key reaches the same live connections as a live key and causes the same real writes. It is a separate credential, not a safe one.
{% endhint %}

### Triggers

Three kinds, covered fully in [Triggers](../build/triggers.md).

* **Webhook** — an outside system calls a URL you give it.
* **Schedule** — a clock you set.
* **App event** — something changed in a connected system.

### Unified APIs

Where several providers do the same job — HubSpot, Salesforce and Zoho all hold contacts — fastn exposes one canonical endpoint per entity and routes to whichever provider that customer connected. Your code calls `/api/v1/unified/crm/contact` and does not branch on the CRM.

There are three categories today — CRM (`Account`, `contact`, `Note`), Documents (`Document`, `Document Content`) and Messaging (`Channel Message`, `Direct Message`). `Note` and both message entities are create-only. See [Unified APIs](../build/unified-apis.md).

### The agent

fastn's agents are not autocomplete. They discover API specs, create connectors, wire auth, propose field mappings, generate test cases and write the workflow, and they show you a diff before anything runs. You review; they build.

### The MCP gateway

Everything you build can also be exposed to an AI client as tools, with the same customer scoping and permission model. See [MCP gateway](../build/mcp-gateway.md).
