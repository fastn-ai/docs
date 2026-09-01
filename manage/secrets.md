---
description: Encrypted values your workflows read at runtime.
---

# Secrets

**Settings → Secrets**

> Encrypted values your workflows read at runtime. Scope a secret to a customer or environment for per-tenant overrides.

A secret is written once and never shown again, so a key never has to live in your code:

```javascript
const apiToken = await fastn.secrets.get("SHOPIFY_API_TOKEN");
```

With no secrets yet, the page shows **No secrets yet** above the same instruction:

> A secret is written once and never shown again. Workflows read it with fastn.secrets.get.

### Creating one

**Create Secret** opens a form with five fields.

| Field             | Notes                                                                                                         |
| ----------------- | --------------------------------------------------------------------------------------------------------------- |
| **Name \***       | UPPER\_SNAKE\_CASE. This string is literally the argument to `fastn.secrets.get()`, so `SHOPIFY_API_TOKEN` here is `fastn.secrets.get("SHOPIFY_API_TOKEN")` in code. |
| **Type**          | **Text** (the default) or **JSON**. JSON is validated on save and comes back to your workflow already parsed — you do not `JSON.parse` it yourself. |
| **Value \***      | The value itself. Written once; the screen does not show it again afterwards.                                  |
| **Customer**      | Defaults to **All customers (org-wide)**. Pick a customer to hold a value that applies only to them.           |
| **Environment**   | Defaults to **All environments**. The other choices are **test** and **Live**.                                 |

To change a value, write a new one over the same name.

### Scoping

A secret can be org-wide, or scoped to a **customer**, an **environment**, or both — which is what gives you per-tenant overrides without branching in code. The same `fastn.secrets.get("PARTNER_TOKEN")` call is what runs for everybody.

{% hint style="info" %}
How fastn picks between a customer-scoped and an environment-scoped value when both could match is not documented here. If you rely on overlapping scopes, set one up and confirm which value a run actually reads before you build on it.
{% endhint %}

### What belongs here

Third-party API tokens, database credentials, signing keys, webhook signing secrets — anything you would not paste into a ticket.

What does **not** belong here: connector credentials. Those live on [connections](../build/connections.md) and are managed by fastn, including OAuth refresh.

{% hint style="warning" %}
Deleting a secret takes effect immediately. Any workflow calling `fastn.secrets.get` for that name starts failing on its next run.
{% endhint %}

For non-sensitive per-environment values, use [Configs](configs.md) instead.
