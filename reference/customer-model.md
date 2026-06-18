---
description: >-
  The customer hierarchy, isolation model, customer management, and data
  residency.
---

# Customer model

A **customer** is an end user organization of your SaaS product, the businesses that use the integrations you offer through Fastn. Each customer's connections, data, and sync history are isolated from every other customer's.

### Where customers live

Customers are managed under **Settings → Customers** ("Manage customers under your account").

When a customer connects an app through the embedded widget, they are associated with a customer record. You can also create customer records directly.

### What a customer record contains

Opening a customer record shows:

| Field              | Description                                               | Example                       |
| ------------------ | --------------------------------------------------------- | ----------------------------- |
| **Name**           | The customer's display name                               | John-Acme                     |
| **Slug**           | A URL-safe identifier                                     | acme-customer                 |
| **Status**         | The customer's activation state                           | Pending Admin Activation      |
| **Customer Admin** | The admin user for this customer, and their invite status | john@acme.ai (Invite Pending) |
| **Created**        | The date the record was created                           | 2026-06-09                    |

The list view also shows a **Plan** column (e.g., Free).

A customer record also has a **Connected Accounts** section (the apps this customer has authenticated) and a **Danger Zone** (destructive actions).

### The customer identifier

Integration flows — generating embed tokens and configuring the MCP Gateway — require the customer's internal identifier.

* The **slug** (e.g., `katana-customer`) is shown in the UI but does **not** work as the identifier in API calls (it returns 404).
* The internal **UUID** is what the token and gateway calls require, but it is **not currently displayed in the Customers UI**.

See [Finding Your Org Identifier](https://claude.ai/fastn/tutorials/developer/finding-your-org-identifier) for how to obtain the UUID.

> **VERIFY:** Confirm the relationship between the customer identifier used in the embed token (`endOrgId`), the MCP Gateway (`customer_id`), and the customer record — and the recommended way to retrieve the UUID.

### Customer status

Customers move through activation states. One observed value is **Pending Admin Activation**, shown when a customer record exists but its admin has not yet accepted their invitation.

> **VERIFY:** Confirm the full set of customer status values and what each means.

### Per-customer quotas

You can set quota overrides per customer from **Settings → Billing → Customize Customer Limits** — useful when specific customers need higher limits than your plan default, or when you want to cap an individual customer to protect shared capacity.

### Related

* [Managing Customers](https://claude.ai/fastn/tutorials/saas-admin/managing-customers) — the tutorial for working with customers
* [Tenancy](https://claude.ai/fastn/tutorials/developer/tenancy) — how connections are scoped within a customer
* [Finding Your Org Identifier](https://claude.ai/fastn/tutorials/developer/finding-your-org-identifier) — obtaining the customer UUID
