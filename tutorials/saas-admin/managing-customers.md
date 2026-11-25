---
description: >-
  Create customers under Operate → Customers, scope API calls per customer, and
  monitor customer-level activity.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Manage customers

Each company using your product is a customer. Each customer gets an isolated space with their own connections, data, and execution history. Create customers, choose how to identify them, set their limits, and watch their activity.

### Before you start

* The [Quickstart: your first integration](../../getting-started/quickstart.md).

### Create customers

1. Go to **Operate → Customers**.
2. Click **Create customer**.
3. Enter a **Customer Name**. **Slug** is generated from the name, and **Admin Email** (invite an admin at the customer) and **Tier** (the tier the customer is billed under) are optional. Optionally, put your own ID for this customer (for example `customer_12345`) in **External ID**; if you leave it empty, it defaults to the slug.
4. Click **Create Customer** at the bottom of the form.

**You should see:** the new customer in the **Customers** list. Note fastn's **customer id** or the External ID: API calls and widget embedding use one of them.

#### Which identifier to use

API calls and widget configuration identify a customer. Use fastn's customer id, or the External ID shown on the customer (your own id if you set one when creating the customer; otherwise it defaults to the slug). An identifier that matches neither returns 404 "Tenant not found".

{% hint style="info" %}
Pick one convention early. Changing identifiers later means updating every API call.
{% endhint %}

### Customer isolation

Every entity is scoped to a customer:

```
Your Organization
├── Customer A (Acme Corp)
│   ├── Connections: Acme's Shopify token, Acme's Slack token
│   ├── Executions: Only Acme's workflow runs
│   └── Data: Only Acme's orders, contacts, invoices
├── Customer B (Globex)
│   ├── Connections: Globex's HubSpot token
│   ├── Executions: Only Globex's workflow runs
│   └── Data: Only Globex's contacts
```

Workflows are defined once by you but execute per-customer using each customer's own connections and data.

### Customize customer limits

By default, all customers share your plan's quota limits. To override limits for specific customers:

1. Go to **Settings → Billing**.
2. On the **Limits** card, click **Customize customer limits**.
3. Pick a customer, then set overrides for any quota dimension. Overrides win over the plan default.

Use this for:

* High-volume customers who need more events per day
* Trial customers with lower limits
* Enterprise customers with custom agreements

### Monitor customer activity

#### Logs → Executions

1. Go to **Operate → Logs → Executions**.
2. Use the **All workflows** dropdown to filter.

Each execution row shows **Triggered by**, which tells you what started the execution: API key, Embed, Webhook, Schedule, Agent, Replay, Manual, or a person's name.

#### Logs → Events

1. Go to **Operate → Logs → Events**.
2. Filter by type: **All**, **Webhook**, **Scheduled**, or **Manual**.

**You should see:** incoming and outgoing events for your customers.

#### Audit log

For a complete history of all actions:

1. Go to **Settings → Audit log**.
2. Search by person, action, or resource, and filter by person, action, resource type, and date range.

The columns are **Who**, **Action**, **Resource**, **Customer**, **Result**, and **When**.

### What you've learned

* How to create customers under Operate → Customers
* The customer isolation model: each customer has separate connections, data, and executions
* How to customize quota limits per customer
* How to monitor customer activity through Executions, Events, and Audit log

### Next steps

* Use the customer's id in a token request: [Find your org identifier](../developer/finding-your-org-identifier.md).
* Run a workflow for one customer: [Run an integration for one customer](../../how-to/run-for-a-customer.md).
