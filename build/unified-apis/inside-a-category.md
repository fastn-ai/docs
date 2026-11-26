---
description: "What you see when you open a category: its entities, providers, connection state and endpoints."
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

# Inside a category

**Build → Integrations → Unified APIs** → select a category · [Open in Fastn](https://app.fastn.dev/integrations?tab=unified)

When you select a category on the Unified APIs page, you see each of its entities: which apps (providers) serve it, which of them your organization has connected, and the endpoints you can call. For example, the **CRM** category shows an `Account` entity, the CRMs that serve it, and its List, Get, Search, Create, Update and Delete endpoints. For what a category, entity and provider are, see [Unified APIs](README.md#categories-entities-and-providers).

### The category view

The category view replaces the list of categories. It has:

* **All categories:** a back button to the list.
* **Breadcrumb:** **Unified APIs / \<Category>**.
* **Chips:** *N entities* and *N providers*.

Opening a category also sets `?surface=<slug>` in the URL, so a category view is linkable, survives a reload, and browser Back returns you to the category list.

### Each entity

Each entity has its own block with:

* **Connection state:** `<connected>/<total> connected`, meaning how many of the providers that serve the entity your organization has connected.
* **Providers:** one row per provider, with a **Connect** button, or **Connected** and a `⋯` menu. Viewers, who cannot connect accounts, see **Not connected** instead of a **Connect** button.
* **API:** the entity's endpoints, filtered by an **All providers** selector. Each row shows the HTTP method, the operation name and the path, with a **Copy curl** button.

The `⋯` menu on a connected provider offers:

* **Add another connection:** connect a second account for the same provider.
* **Use \<name> by default:** shown only when the provider has two or more connections, with one item per connection that is not the default.
* **Disconnect:** or **Disconnect \<name>**, one item per connection, when there are several.

### Endpoints

Every entity's endpoints follow the same shape. The operations are:

* **List:** many records, a page at a time.
* **Get:** one record, by its id.
* **Search:** the records that match filters you send in the body.
* **Create:** a new record.
* **Update:** changes to one record. Send only the fields to change.
* **Delete:** removes one record.

```http
GET    /v1/unified/crm/account?page_size=50     # List
GET    /v1/unified/crm/account/RECORD_ID        # Get
POST   /v1/unified/crm/account/search           # Search (filters go in the body)
POST   /v1/unified/crm/account                  # Create
PATCH  /v1/unified/crm/account/RECORD_ID        # Update (send only the fields to change)
DELETE /v1/unified/crm/account/RECORD_ID        # Delete
```

Not every entity supports every operation; some support only Create, for example. A row appears only for the operations at least one provider serves. When only some of the providers serve an operation, the row says **Only \<provider names>**, so it does not overstate coverage.

To send one of these requests, see [Set up and use a unified API](setup-and-usage.md).

### Filter by provider

Above the endpoint list, **All providers** shows the unified endpoints for every provider. Pick a single provider to see how that one behaves. This helps when one provider behaves differently and you need to design around it.
