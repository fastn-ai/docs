---
description: >-
  Create customers under Settings → Customers, scope API calls per customer, and
  monitor customer-level activity.
---

# Managing Customers

**Prerequisites:** [Your First Integration](../../getting-started/your-first-integration.md).&#x20;

In Fastn, your end users are called **Customers** (alternatively called "Tenants"). Each customer gets an isolated environment with their own connections, data, and execution history.

### Creating customers

1. Go to **Settings → Customers**.
2. Click **"Create Customer"**.
3. Enter the customer details (name, and any other required fields).
4. Click create. Note the **customer ID** — you'll use this for API calls and widget embedding.

> &#x20;**Screenshot:** Settings → Customers showing the Create Customer button and the creation form.

> &#x20;**Screenshot:** Customer list showing created customers with their IDs.

#### Naming conventions

Customer IDs are used in API headers and widget configuration. Pick a convention early:

* Internal customer ID: `customer_12345`
* Slug: `acme-corp`
* Auto-generated UUID

{% hint style="info" %}
Changing IDs later means updating every API call.
{% endhint %}

### Customer isolation

Every entity is scoped to a customer:

```
Your Organization
├── Customer A (Acme Corp)
│   ├── Connections: Acme's Shopify token, Acme's Slack token
│   ├── Executions: Only Acme's workflow runs
│   └── Data: Only Acme's orders, contacts, invoices
├── Customer B (Widget Inc)
│   ├── Connections: Widget's HubSpot token
│   ├── Executions: Only Widget's workflow runs
│   └── Data: Only Widget's contacts
```

Workflows are defined once by you but execute per-customer using each customer's own connections and data.

### Customizing customer limits

By default, all customers share your plan's quota limits. To override limits for specific customers:

1. Go to **Settings → Billing**.
2. Click **"Customize Customer Limits"**.
3. Set per-customer overrides for any quota dimension.

Use this for:

* High-volume customers who need more events per day
* Trial customers with lower limits
* Enterprise customers with custom agreements

> **Screenshot:** Customize Customer Limits interface showing per-customer quota overrides.

### Monitoring customer activity

#### Activity → Executions

1. Go to **Activity → Executions**.
2. Use the **"All workflows"** dropdown to filter.
3. Each execution row shows **Triggered By** which tells you what started the execution (agent-service, webhook, scheduler, manual).

> **Screenshot:** Activity → Executions filtered to show a specific customer's workflow runs.

#### Activity → Events

1. Go to **Activity → Events**.
2. Filter by type: **All | Webhook | Scheduled | Manual**.
3. See incoming and outgoing events for your customers.

#### Audit Log

For a complete history of all actions:

1. Go to **Settings → Audit Log**.
2. Filter by user, action type, resource, and date range.
3. Columns: Timestamp, User, Action, Resource, Outcome.

### What you've learned

* How to create customers under Settings → Customers
* Customer isolation model i.e. each customer has separate connections, data, and executions
* How to customize quota limits per customer
* How to monitor customer activity through Executions, Events, and Audit Log
