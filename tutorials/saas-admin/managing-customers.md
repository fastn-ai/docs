---
description: >-
  Create customers under Operate → Customers, scope API calls per customer, and
  monitor customer-level activity.
---

# Managing Customers

**Prerequisites:** [Your First Integration](../../getting-started/quickstart.md).&#x20;

Each company using your product is a customer. Each customer gets an isolated environment with their own connections, data, and execution history.

### Creating customers

1. Go to **Operate → Customers**.
2. Click **Create customer**.
3. Enter the customer details (name, and any other required fields). Optionally, put your own ID for this customer (for example `customer_12345`) in **External ID**; if you leave it empty, it defaults to the slug.
4. Click **Create Customer** at the bottom of the form. Note fastn's **customer id** or the External ID - you'll use one of them for API calls and widget embedding.

> &#x20;**Screenshot:** Operate → Customers showing the Create customer button and the creation form.

> &#x20;**Screenshot:** Customer list showing created customers with their IDs.

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

### Customizing customer limits

By default, all customers share your plan's quota limits. To override limits for specific customers:

1. Go to **Settings → Billing**.
2. On the **Limits** card, click **Customize customer limits**.
3. Set per-customer overrides for any quota dimension.

Use this for:

* High-volume customers who need more events per day
* Trial customers with lower limits
* Enterprise customers with custom agreements

### Monitoring customer activity

#### Activity → Executions

1. Go to **Activity → Executions**.
2. Use the **"All workflows"** dropdown to filter.
3. Each execution row shows **Triggered by**, which tells you what started the execution: API key, Embed, Webhook, Schedule, Agent, Replay, Manual, or a person's name.

#### Activity → Events

1. Go to **Activity → Events**.
2. Filter by type: **All | Webhook | Scheduled | Manual**.
3. See incoming and outgoing events for your customers.

#### Audit Log

For a complete history of all actions:

1. Go to **Settings → Audit Log**.
2. Search by person, action or resource, and filter by person, action, resource type and date range.
3. Columns: Who, Action, Resource, Customer, Result, When.

### What you've learned

* How to create customers under Operate → Customers
* Customer isolation model i.e. each customer has separate connections, data, and executions
* How to customize quota limits per customer
* How to monitor customer activity through Executions, Events, and Audit Log
