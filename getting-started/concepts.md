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

### Connector versus connection

A **connector** is the definition: this API, these actions, these auth methods, this webhook config. A **connection** is an instance of it for one customer. One connector, many connections.

Connectors are either **managed by fastn** — maintained upstream, patched when the vendor changes something — or **custom**, created by you.

### Per-customer versus workspace connectors

Inside a workflow, each connector is wired one of two ways.

| Mode             | Credential used                          | Use for                                                 |
| ---------------- | ---------------------------------------- | --------------------------------------------------------- |
| **Per customer** | The connection belonging to the running customer | Anything touching customer data                    |
| **Workspace**    | A single connection owned by your org    | Your own systems — your Slack, your data warehouse       |

### Execution tiers

Every workflow declares how long it may run and how it answers the caller.

| Tier         | Behaviour                                | Returns       | Timeout range |
| ------------ | ---------------------------------------- | ------------- | ------------- |
| **Instant**  | Synchronous; the caller waits            | Result inline | 1s – 2min     |
| **Standard** | Asynchronous, queued and executed        | 202 Accepted  | 5s – 15min    |
| **Long**     | Asynchronous, for large volumes          | 202 Accepted  | 30s – 6hrs    |

Pick Instant only when something is waiting on the answer. Most syncs are Standard.

### Test and live

fastn separates *what the code is* from *where it runs*.

* **Versions** are immutable snapshots created by Publish (v1, v2, …).
* **Environments** are where versions are deployed. `test` and `live` are built in; you can add named ones such as `staging`.
* **API keys** carry a mode. An `fsk_test_` key must send `X-fastn-Test-Mode: true`; an `fsk_live_` key must not.

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

### The agent

fastn's agents are not autocomplete. They discover API specs, create connectors, wire auth, propose field mappings, generate test cases and write the workflow, and they show you a diff before anything runs. You review; they build.

### The MCP gateway

Everything you build can also be exposed to an AI client as tools, with the same customer scoping and permission model. See [MCP gateway](../build/mcp-gateway.md).
