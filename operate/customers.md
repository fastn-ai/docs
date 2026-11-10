---
description: Every customer using your embedded integrations.
---

# Customers

**Operate → Customers** · `/customers`

A top-level item in the sidebar's **Operate** group, beside Health, Connections and Activity. It used to live under Settings at `/settings/customers`, and that old address redirects here.

<figure><img src="../.gitbook/assets/customers.jpg" alt="The Customers table with a single row: testing, identifier testing underneath, 1 connection, status Active, ending in View connections, with an All tiers filter and a 1 customer count above"><figcaption>The second line under each name is the customer's slug.</figcaption></figure>

A customer is one company using your product: a container for their connections, credentials and workflow data.

### The table

| Column          | Notes                                                          |
| --------------- | ---------------------------------------------------------------- |
| **Customer**    | Display name, with the customer's slug underneath.              |
| **Connections** | How many systems they have authorized.                          |
| **Status**      | Active, Pending admin activation, Suspended, Pending review or Blocked. |

A count sits above the table, and **Search customers** narrows it. **View connections** on each row opens that customer's panel on this page: their settings, connections and installations.

### Status

**Active**: set up and usable.

**Pending admin activation**: the customer admin you invited has not accepted the invitation yet.

**Suspended**: the customer has been suspended, and their users lose access.

**Pending review** and **Blocked**: the customer is held for review, or blocked.

### Creating a customer

**Create customer** adds one manually, which is what you want when onboarding an account before they first sign in.

You can put your own ID for the customer in **External ID** when you create it. When you mint an [embed token](../embed/embedding/README.md) or send `x-org-id`, identify the customer this way: use fastn's customer id, or the External ID shown on the customer (your own id if you set one when creating the customer; otherwise it defaults to the slug). The token response names the customer by its External ID, as `orgId`.

### Customers in connection IDs

A connection's ID names the customer it belongs to:

```
ucl:<workspace>:<customer or default>:<connectorId>:<identity>[:<account>]
```

`default` in the customer segment means the connection belongs to your own organization rather than to a customer. Some API fields and older screens still say "tenant"; it means the same thing as customer.

### Where customers show up elsewhere

| Surface                            | What it does                                        |
| ---------------------------------- | ----------------------------------------------------- |
| ⌘K search, **Your customers** group | Picking one opens **Customers**.                    |
| [Connections](../build/connections/README.md) | A **Customer** column in the **Customers** view. |
| Widget builder preview             | The **View as** selector (default **View as admin**) renders the widget as a customer. |
| [Embed tab](../embed/embedding/README.md) | The **USER** selector scopes the generated snippet.  |
