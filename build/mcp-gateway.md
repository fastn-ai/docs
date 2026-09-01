---
description: Letting an AI client reach your connectors as tools.
---

# MCP gateway

**Home → Connect to Claude**, and the sparkle icon in the top bar

Everything you build in fastn — connectors, actions, workflows — can be exposed to an AI client over the Model Context Protocol. The client sees your connectors as tools it can call, with the same customer scoping and the same permission model as everything else.

<figure><img src="../.gitbook/assets/home.jpg" alt="The Connect to Claude button on the home screen"><figcaption>Connect to Claude sits under the build prompt on Home.</figcaption></figure>

### What the client gets

| Kind                | Contents                                                                                   |
| ------------------- | -------------------------------------------------------------------------------------------- |
| **Native tools**    | Platform operations — list connectors, run a workflow, inspect an execution.                |
| **Dynamic tools**   | The actions of every connector available to the calling identity, generated from the catalogue. |

Because tools are generated from what that identity may reach, two customers connected to the same gateway see different tool sets. A customer who has authorised HubSpot and Slack gets HubSpot and Slack tools; nothing else appears.

### Scoping

The gateway inherits the platform's access model rather than inventing a second one:

* **Customer scope** — a connection belongs to one customer, so a tool call runs against that customer's credential and cannot reach another's.
* **Role** — the API key's permissions cap what the gateway can do. A key carrying Viewer can read and cannot write.
* **Action scope** — the action checkboxes on a [connector](connectors.md) narrow the tool set further. This is what makes *read-only Jira for one customer, nothing beyond that* a configuration rather than a promise.

### Connecting

**Connect to Claude** on Home starts the connection for a Claude client. For any other MCP client, point it at the gateway endpoint for your deployment and authenticate with an API key from [Settings → API keys](../manage/api-keys.md).

```
Authorization: Bearer fsk_live_<your-key>
```

Test keys work too, with `X-fastn-Test-Mode: true` — and carry the same warning as everywhere else: a test key reaches the same live connections and causes the same real writes.

{% hint style="warning" %}
An MCP client acts with whatever the key it holds can do. Mint a key specifically for the client, give it the narrowest role that works, and name it after the client so the [audit log](../manage/audit-log.md) attributes its actions clearly.
{% endhint %}

### Watching it

Gateway activity lands in the same places as everything else. Executions triggered through MCP show `agent-service` in the **Triggered by** column of [Executions](../operate/executions.md), and every call appears in the [audit log](../manage/audit-log.md) attributed to the key that made it.

### The A2A option

The widget's Embed tab lists **A2A** — agent-to-agent — alongside Iframe and SDK, marked *soon*. That is the customer-facing counterpart: your customer's own agent reaching the integrations you offer. See [Embedding the widget](../embed/embedding.md).
