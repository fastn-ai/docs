---
description: Programmatic access to your workspace.
---

# API keys

**Settings → API keys**

![The API keys list](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/settings-api-keys.jpg)

| Column        | Notes                                              |
| ------------- | -------------------------------------------------- |
| **Name**      | What you called it.                                |
| **Key**       | Prefix and last four characters, with a copy icon. |
| **Mode**      | Live or Test.                                      |
| **Scope**     | The permissions it carries.                        |
| **Last used** | Timestamp, or Never.                               |

**Search keys** narrows the list, and the filters are **All** / **Live** / **Test**.

**Rotate** issues a new secret for the same key. The **…** menu holds **Edit**, **Identity verification** and **Revoke** — there is no delete. Revoking is the way a key ends.

### Creating a key

![The create API key dialog](https://raw.githubusercontent.com/fastn-ai/docs/docs-v2/.gitbook/assets/create-api-key.jpg)

The dialog runs in three sections: **Identity**, **Access** and **Limits**.

#### Identity

**Name \*** — shown in the audit log beside everything this key does. Name it after the system that will hold it, not after a person.

**Mode** — **Test** or **Live**, defaulting to **Test**.

| Mode     | Behaviour                                                                            |
| -------- | ------------------------------------------------------------------------------------ |
| **Test** | Separately revocable, and refused unless the caller sends `X-fastn-Test-Mode: true`. |
| **Live** | Acts on real customer data. Treat it like a password.                                |

{% hint style="danger" %}
Neither mode is a sandbox. A Test key reaches the same live connections as a Live key and causes the same real writes — it is a separate credential, not a safe one.
{% endhint %}

#### Access

**Permissions \*** takes one of six presets — **Full access**, **Developer**, **Operator**, **Viewer** (the default), **End user** or **Custom**. These are key presets, not the people roles on [Roles](roles.md), even where the names match. Choose the narrowest that works: a key that only reads should stay on Viewer.

Whichever preset you pick, the **What it can touch** matrix below shows exactly what it grants, and **Custom** lets you set each box yourself. Ten resource groups:

| Resource        | Permissions                                                       |
| --------------- | ----------------------------------------------------------------- |
| **Connectors**  | create, read, update, delete, write                               |
| **Connections** | create, read, update, delete, share, decrypt                      |
| **Workflows**   | create, read, update, delete, execute, deploy\_test, deploy\_prod |
| **Users**       | create, read, update, invite, remove                              |
| **Settings**    | read, update, manage                                              |
| **Events**      | create, read, update, delete, replay                              |
| **Secrets**     | read, write, delete                                               |
| **Executions**  | create, read                                                      |
| **Widgets**     | create, read, update, delete                                      |
| **Unified API** | create, read, update, delete, execute                             |

{% hint style="warning" %}
`decrypt` on Connections and `read` on Secrets are the two boxes worth arguing about before you tick them. A key holding either can read credentials, and a key is easier to leak than a person.
{% endhint %}

**Customers it can reach** — **Every customer**, or **Only the ones I pick**. Narrowing it is not optional everywhere: the form notes that picking specific customers is _Required for keys used in an embed session._

**Verify caller identity (HMAC)** — turning it on requires callers to send a signed `x-identity-hmac` header, so a caller cannot change the `x-org-id` or `x-user-id` it claims to be. The signing secret is shown once at creation. If you lose it, reach it again through **Identity verification** on the key's **…** menu.

**Resource scope** _(optional)_ — narrows the key to particular resources rather than everything its permissions would otherwise cover.

#### Limits

| Field                                 | Notes                                                                                              |
| ------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Allowed IP addresses** _(optional)_ | An allowlist. Left blank, the key works from any address.                                          |
| **Rate limit** _(optional)_           | A ceiling per minute for this key.                                                                 |
| **Expires \***                        | **In 30 days**, **In 90 days** (the default), **In a year**, **Never**, or **On a specific date**. |

The dialog keeps a live summary sentence at the bottom describing what you have built, so you can read back the whole key before committing:

> This key can read on test data for every customer, from any address, and expires in 90 days.

### Using a key

```bash
curl -X POST https://YOUR_FASTN_HOST/api/v1/workflows/WORKFLOW_ID/execute \
  -H "Authorization: Bearer fsk_live_<your-key>" \
  -H "Content-Type: application/json" \
  -d '{ "input": { "key": "value" } }'
```

With a test key, add the two headers:

```bash
  -H "Authorization: Bearer fsk_test_<your-key>" \
  -H "X-fastn-Test-Mode: true" \
  -H "x-fastn-env: test"
```

Full detail in the [HTTP API reference](../reference/http-api.md).

### Practice worth keeping

* One key per consuming system, so revoking one does not take down four things.
* Rotate on a schedule, and when anyone with access leaves.
* Never in client-side code. Browser-facing widgets use short-lived embed tokens minted by your backend — see [Embedding the widget](../embed/embedding-the-widget.md).
* Check **Last used** before revoking. A key showing Never is either unused or misconfigured; either way, find out which.
* Set an expiry rather than **Never**, and turn on HMAC verification for any key a customer's browser session depends on.

{% hint style="info" %}
**API keys per customer** is one of the limits listed under [Billing](billing-and-limits.md). Check there if key creation starts refusing.
{% endhint %}
