---
description: Every customer using your embedded integrations.
---

# Customers

**Customers**, or **Settings → Customers**

<figure><img src="../.gitbook/assets/customers.jpg" alt="The customers list"><figcaption></figcaption></figure>

A customer is one of your customers — an isolated container for their connections, credentials and workflow data. Nothing crosses between customers.

### The table

| Column          | Notes                                                          |
| --------------- | ---------------------------------------------------------------- |
| **Customer**    | Display name, with the identifier underneath.                   |
| **Connections** | How many systems they have authorised.                          |
| **Status**      | Active, or Pending admin activation.                            |

**View connections** on each row filters [Connections](../build/connections.md) to that customer.

### Status

**Active** — set up and usable.

**Pending admin activation** — created, but an administrator has not activated it. Its integrations will not run until they do.

### Creating a customer

**Create customer** adds one manually, which is what you want when onboarding an account before they first sign in. In normal operation your backend creates customers through the API as accounts are provisioned, so the two systems stay in step.

The identifier is what your code passes when it mints an embed token or calls a workflow on that customer's behalf. Use your own stable account ID rather than a display name.

### Deleting a customer

Open the customer and use its **Danger zone**. It asks you to **suspend** first, then delete.

{% hint style="danger" %}
Deleting a customer removes its connections, workflows and stored credentials, and cannot be undone.
{% endhint %}

### Tiers and limits

Every customer sits on exactly one **customer tier**, which caps what they may use — API keys, events per day, workflows, storage. Tiers are created under [Billing](../manage/billing.md), and the per-customer usage breakdown lives there too.

### Customers and tenants

Older fastn documentation and some API parameters call this a *tenant*. Same concept: one isolated customer container.
