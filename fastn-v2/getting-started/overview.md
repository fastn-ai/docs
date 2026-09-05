---
description: >-
  What fastn does, who each part is for, and the path from signup to a live
  sync.
---

# Overview

### The problem fastn solves

Every integration you ship yourself carries the same recurring cost: an OAuth app to register, tokens to refresh, per-customer credentials to store, an upstream API that changes without warning, and a support queue when a sync quietly stops. Multiply that by the number of systems your customers use.

fastn takes that whole layer. You keep the part your customers pay for.

### The five things you work with

**Connectors** are the systems your customers can authorise — a catalogue managed by fastn, plus any you create. A connector knows an API's actions, its auth methods, and its webhooks.

**Connections** are what you get when a specific customer authorises a specific connector. Credentials live encrypted on fastn's side, scoped to that customer.

**Workflows** are the code that runs. Each one is a JavaScript module — a file called `<slug>.js` that exports `export default async function(ctx)`. It reads from one system, transforms, and writes to another. The agent writes them; you review, test, publish and deploy.

**Triggers** decide when a workflow runs — an inbound webhook, a schedule, or an event from a connected system.

**Unified APIs** give you one canonical endpoint per business entity — contact, document, message — served by whichever provider each customer connected, so your code stops branching per vendor.

Around those five sit two surfaces: **Widgets**, the panel your customers see inside your product, and **Activity**, where you watch everything that happens.

### The shape of a build

1. Describe the integration to the **Agent**, or wire it by hand.
2. The agent picks or creates **Connectors** and handles authentication.
3. It drafts a **Workflow**, generates test cases, and shows you the diff.
4. You attach a **Trigger** so it runs on real events.
5. You publish a version and **deploy** it to an environment.
6. You add the integration to your **Widget** so customers can turn it on.
7. You watch it in **Activity** and set an **Alert** so failures are not silent.

### Two audiences, one platform

fastn is used by two different people at once, and the product is split accordingly.

| You are…                     | You work in…                                                          |
| ---------------------------- | --------------------------------------------------------------------- |
| The SaaS company using fastn | Build, Operate and Manage — the dashboard in these docs               |
| Your customer                | The embedded widget inside your product — they never sign in to fastn |

Inside the dashboard, what you can see and do depends on your role. The role vocabulary is **Platform Admin**, **Owner**, **Admin**, **Developer** and **Operator**, and it changes the Settings navigation as well as individual permissions — an Owner or Admin sees People, General, Billing, Roles and Audit log; a Developer does not, but does see Trash.

{% content-ref url="platform-tour.md" %}
[platform-tour.md](platform-tour.md)
{% endcontent-ref %}

{% content-ref url="../reference/faqs.md" %}
[faqs.md](../reference/faqs.md)
{% endcontent-ref %}
