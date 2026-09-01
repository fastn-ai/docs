---
description: One canonical endpoint per business entity, served by whichever providers your customers connect.
---

# Unified APIs

**Integrations → Unified APIs**

<figure><img src="../.gitbook/assets/unified-apis.jpg" alt="Unified API categories"><figcaption></figcaption></figure>

Three of your customers use three different CRMs. Without a unified API, your code branches three ways for what is conceptually one operation: create a contact. With one, you call a single endpoint and fastn routes to whichever provider that customer authorised.

### Categories and entities

A **category** is a domain — CRM, Documents, Messaging. An **entity** is a business object inside it — Account, Contact, Note. Each entity is backed by one or more **providers**.

| Category      | Entities               | Providers                      |
| ------------- | ---------------------- | ------------------------------ |
| **CRM**       | Account, Contact, Note | HubSpot, Salesforce, Zoho CRM  |
| **Documents** | 2 entities             | Google Docs, Notion            |
| **Messaging** | 2 entities             | Slack, Microsoft Teams         |

The exact set depends on your workspace — the page header shows the category count, and each card its entity count.

### Inside a category

<figure><img src="../.gitbook/assets/unified-api-crm-detail.jpg" alt="The CRM unified surface, showing the Account entity"><figcaption></figcaption></figure>

Each entity gets its own block showing:

* **Connection state** — `0/1 connected`, `0/3 connected`. How many of the backing providers this customer has authorised.
* **Providers** — each with its own Connect button.
* **API** — the endpoints, filterable by provider, each with **Copy curl**.

Endpoints follow a consistent shape:

```http
GET  /api/v1/unified/crm/account?page_size=50
GET  /api/v1/unified/crm/account/RECORD_ID
POST /api/v1/unified/crm/account
```

```http
POST /api/v1/unified/crm/note
```

Not every entity supports every verb. Note, for example, is create-only, and the UI says so.

### Choosing between unified and direct

| Use a unified API when                                      | Use the connector directly when                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Several providers do the same job for different customers   | You need a field or action only one provider has            |
| You want one code path regardless of the customer's stack   | The operation has no meaningful equivalent elsewhere        |
| The fields you need are common across providers             | You are already deep in one vendor's model                  |

The two are not exclusive — a workflow can use a unified endpoint for the common path and a direct connector action for the vendor-specific part.

### The PROVIDER selector

Above the endpoint list, **All providers** shows the canonical surface; picking a single provider shows how that one behaves. Useful when a provider has a quirk you need to design around.
