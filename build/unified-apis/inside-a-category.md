---
description: "Opening a category: entities, connection state, providers and endpoints."
---

# Inside a category

<figure><img src="../../.gitbook/assets/unified-api-crm-detail.jpg" alt="The CRM category, chips reading 10 entities and 12 providers: the Account entity at 0/12 connected, twelve provider rows from Capsule CRM to Zoho CRM each offering Connect, then the endpoint list"><figcaption>Nothing is connected here yet, and the endpoints are listed anyway — they exist per entity, not per provider.</figcaption></figure>

Opening a category swaps the pane for a detail view with the breadcrumb **Unified APIs / \<Category>** and two chips, *N entities* and *N providers*. **The URL does not change when you do this**, so there is no link you can send someone that opens a category directly.

Each entity gets its own block showing:

* **Connection state** — `0/12 connected` on CRM's `Account`, `0/1 connected` elsewhere. How many of the backing providers this customer has authorised.
* **PROVIDERS** — one row per provider, with a **Connect** button, or **Connected** and a `⋯` menu offering **Add another connection** and **Disconnect default**.
* **API** — the endpoints, filtered by an **All providers** selector, each row with **Copy curl**.

Endpoints follow a consistent shape:

```http
GET  /api/v1/unified/crm/account?page_size=50
GET  /api/v1/unified/crm/account/RECORD_ID
POST /api/v1/unified/crm/account
```

```http
POST /api/v1/unified/crm/note
```

Not every entity supports every verb. `Note` and both Messaging entities — `Channel Message` and `Direct Message` — are create-only.
