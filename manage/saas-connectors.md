---
description: Connecting your own product, through its API or webhooks, and the scopes your customers connect under.
---

# Connect your product

**Build → Connect your product**

> Connect your product through its API or webhooks, so each customer's connection to it can be scoped. Integrations can't go live until your product is connected.

Every other connector in fastn represents someone else's system: Shopify, HubSpot, Jira. This page is for the opposite case: **your own product**, through its API or webhooks, registered so that each of your customers has a connection to your product, scoped the way your product is organised.

An integration usually has two ends. One end is the app your customer uses, picked from **Integrations**. The other end is your product, connected here. Workflows read and write both through the same kind of connection. You can explore and build before this is done, but no integration goes live until your product is connected.

Admin only.

With nothing registered the page reads:

> Your product is not connected yet. Pick the connector for your product, through its API or webhooks, and define connection scopes (e.g. inventory, product) that your customers' connections to it are created under.

### Connecting it

**Connect your product** opens the **Connect your product** panel, which takes two things.

| Field | Notes |
| ----- | ----- |
| **Connector \*** | A picker over the whole connector catalogue (*Select your product's connector…*). Its helper text is the important part: *"The connector for your own product, through its API or webhooks: the one your customers' connections are made against."* This is not the system you are integrating **with**; it is the one representing **you**. If your product is not in the catalogue yet, create its connector first from **Integrations → Connectors → Create connector**. |
| **Connection scopes** | A free-text field with an **Add** button beside it, seeded with the example `inventory`. Add as many as you need. |

The panel closes with **Cancel** and **Add connector**.

### What a scope is for

The helper text under the scopes field states the rule directly:

> Each customer holds at most one connection per scope (e.g. inventory, product). A widget tags your product's connector with a scope, and installation pins the customer's matching connection.

Three consequences worth being deliberate about:

* **One connection per customer per scope.** A scope is the uniqueness key. A customer cannot hold two `inventory` connections to your product, so a scope is how you stop a customer from accidentally wiring the same thing twice.
* **Widgets tag against a scope.** The [widget](../embed/widget-builder/README.md) names the scope it wants, which is what lets one widget resolve to the right connection for whichever customer is looking at it.
* **Installation pins the match.** When a customer installs an integration, the connection matching that scope is the one bound, so the scopes you choose here decide how granular each customer's setup can be.

Pick scopes that name a *capability boundary* in your own product (`inventory`, `product`, `billing`), rather than one scope per customer. Customers are already one axis; scopes are the second axis crossing it.

{% hint style="info" %}
This page sits under **Build**, beside Integrations rather than inside it. Integrations is the catalogue of other companies' apps; this is the one connector that is yours. It moved here from Settings (where it was called SaaS Connectors) and from the Integrations page (where it was briefly called Your API), and both old links redirect.
{% endhint %}

{% hint style="warning" %}
How a scope behaves once connections exist against it (whether it can be renamed or removed with live customer connections attached) is not documented here. Register a scope you intend to keep, and confirm the behaviour in your own workspace before restructuring one that is in use.
{% endhint %}
