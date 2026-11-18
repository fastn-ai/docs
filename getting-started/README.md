---
description: What fastn does, its four building blocks and the connections they run on, and the steps of a typical build.
---

# Overview

<figure><img src="../.gitbook/assets/lifecycle/fastn-lifecycle.svg" alt="The fastn integration lifecycle: who does what across Build, Publish, Embed, Customize, and Run and monitor"><figcaption><p>The full lifecycle: your team, your customer and fastn</p></figcaption></figure>

### The problem fastn solves

Every integration you ship yourself carries the same recurring cost: an OAuth app to register, tokens to refresh, per-customer credentials to store, an upstream API that changes without warning, and a support queue when a sync quietly stops. Multiply that by the number of systems your customers use.

fastn takes that whole layer. You keep the part your customers pay for.

### The building blocks

Every integration you build is made of four building blocks: connectors, workflows, triggers and unified APIs. Connections are the fifth thing you work with: one is created each time someone signs in to a connector, usually a customer in your widget.

**Connectors** are the systems your customers can authorize. There is a catalog managed by fastn, plus any you create. A connector knows an API's actions, its auth methods, and its webhooks.

**Connections** are what you get when a specific customer authorizes a specific connector. Credentials live encrypted on fastn's side, scoped to that customer.

**Workflows** are the code that runs. Each one is a JavaScript module: a file called `<slug>.js` whose default export is `async function(ctx)`. It reads from one system, transforms, and writes to another. Build with AI writes them; you review, test, publish and deploy.

**Triggers** decide when a workflow runs: an inbound webhook, a schedule, or an event from a connected system.

**Unified APIs** give you one canonical endpoint per business entity (contact, document, message), served by whichever provider each customer connected, so your code stops branching per vendor.

Around them sit two surfaces: the **Widget**, the panel your customers see inside your product, and the **Operate** group (**Health**, **Customers**, **Connections** and **Activity**), where you watch everything that happens.

### The shape of a build

1. Describe the integration to **Build with AI** (or your AI tool), or wire it by hand.
2. fastn's agent picks or creates **Connectors** and handles authentication.
3. It drafts a **Workflow**, generates test cases, and shows you the diff.
4. You publish a version and **deploy** it to an environment.
5. You attach a **Trigger** so the deployed version runs on real events.
6. You add the integration to your **Widget** so customers can turn it on.
7. You watch it in **Operate → Health** and **Operate → Activity**, and turn on an alert in **Operate → Health → Alerts** so failures are not silent.

### Two audiences, one platform

fastn is used by two different people at once, and the product is split accordingly.

| You are…                     | You work in…                                                            |
| ---------------------------- | ------------------------------------------------------------------------ |
| The SaaS company using fastn | The dashboard in these docs: Home, the Build, Embed and Operate groups, and Settings |
| Your customer                | The embedded widget inside your product. They never sign in to fastn    |

Inside the dashboard, what you can see and do depends on your role. The dashboard roles are **Owner**, **Admin**, **Developer**, **Operator** and **Viewer** (**End User** is the role for people at your customers using the widget), and the role changes the Settings navigation as well as individual permissions. An Owner or Admin sees People, General, Billing, Roles and Audit log. A Developer does not, but does see Trash.

{% content-ref url="platform-tour.md" %}
[Platform tour](platform-tour.md)
{% endcontent-ref %}

{% content-ref url="../reference/faqs.md" %}
[FAQs](../reference/faqs.md)
{% endcontent-ref %}
