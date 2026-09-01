---
description: Encrypted values your workflows read at runtime.
---

# Secrets

**Settings → Secrets**

> Encrypted values your workflows read at runtime. Scope a secret to a customer or environment for per-tenant overrides.

A secret is written once and never shown again. Workflows read it with `fastn.secrets.get`, so a key never has to live in your code.

```javascript
const apiToken = await fastn.secrets.get("SHOPIFY_API_TOKEN");
```

The empty state says it plainly: *A secret is written once and never shown again. Workflows read it with `fastn.secrets.get`, so a key never has to live in your code.*

### Creating one

**New secret** — or **Create your first secret** on the empty state — takes a name and a value. The name is what your code passes to `fastn.secrets.get`; the value is encrypted on save and is not retrievable afterwards, from the UI or the API.

To change a value, write a new one over the same name.

### Scoping

A secret can be global to the organisation, or scoped to a **customer** or an **environment**.

Scoping gives you per-tenant overrides without branching in code: the same `fastn.secrets.get("PARTNER_TOKEN")` call resolves to whichever value applies to whoever is running. Resolution goes from most to least specific — customer, then environment, then organisation.

### Guarantees

Secrets are never logged, never included in execution output, and never exposed in error messages. The [audit log](audit-log.md) records `secret.create`, `secret.update` and `secret.delete` — who and when, never the value.

### What belongs here

Third-party API tokens, database credentials, signing keys, webhook signing secrets — anything you would not paste into a ticket.

What does **not** belong here: connector credentials. Those live on [connections](../build/connections.md) and are managed by fastn, including OAuth refresh.

{% hint style="warning" %}
Deleting a secret takes effect immediately. Any workflow calling `fastn.secrets.get` for that name starts failing on its next run.
{% endhint %}

For non-sensitive per-environment values, use [Configs](configs.md) instead.
