---
description: Find, create and update contacts in whichever CRM a customer connected, with one piece of code.
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

# Read and write a customer's CRM records

Your product needs to read or write contacts in each customer's CRM. One customer uses HubSpot, another Salesforce. With the [unified API](../build/unified-apis/README.md), a contact has the same fields in every CRM, so your code does not change per app.

### Before you start

* An API key that can act for more than one customer. See [Authentication](../tutorials/developer/authentication-and-api-keys.md).
* A customer that has connected a CRM, in the widget or with a [connection you created for them](../embed/embedding/integration-flow.md#create-a-connection-for-a-customer).
* Node.js 20 or newer, for the SDK.

### 1. Install the SDK and create a client

```bash
npm install @fastn-ai/sdk
```

```typescript
import { FastnClient } from "@fastn-ai/sdk";

const fastn = new FastnClient({ apiKey: process.env.FASTN_API_KEY! });

// One object per customer, named by YOUR id for that customer
const customer = fastn.customer("acme_customer_42");
```

### 2. Find or create a contact

```typescript
const { records } = await customer.crm.contacts.find({ email: "jane@example.com" });

const contact = records[0]
  ?? (await customer.crm.contacts.create({ first_name: "Jane", last_name: "Doe", email: "jane@example.com" }));
```

The SDK uses whichever CRM the customer connected. If they connected more than one CRM, calls on a single record need `provider`, for example `{ provider: "hubspot" }`, passed as the last argument.

**You should see:** a contact with an `id`, and a new contact in the customer's CRM if none matched.

### 3. Add a note to it

```typescript
await customer.crm.notes.add({ body: "Signed up for the annual plan", parent_id: contact.id, parent_type: "contact" });
```

### 4. List contacts, page by page

```typescript
let cursor: string | undefined;
do {
  const page = await customer.crm.contacts.list({ page_size: 100, cursor });
  for (const r of page.records ?? []) console.log(r.id, r.data);
  cursor = page.hasMore ? (page.nextCursor ?? undefined) : undefined;
} while (cursor);
```

### Without the SDK

Every SDK call maps to a unified endpoint. The dashboard copies a ready request for each one: open **Integrations → Unified APIs**, pick the category, and click **Copy curl** on the row you need. Name the customer with `x-org-id`:

```bash
curl -X POST 'https://api.fastn.dev/api/v1/unified/crm/contact' \
  -H 'Authorization: Bearer fsk_live_<your-key>' \
  -H 'x-org-id: acme_customer_42' \
  -H 'Content-Type: application/json' \
  -d '{"first_name": "Jane", "last_name": "Doe", "email": "jane@example.com"}'
```

Start from the copied request: the fields each entity accepts come from your live catalog.

### Related

* [crm-contacts-node](https://github.com/fastn-ai/docs/tree/main/examples/crm-contacts-node): this guide as a runnable project

* [Unified records](../reference/sdk/unified-records.md): every entity, `records()` and the live catalog
* [Calendar and CRM](../reference/sdk/calendar-and-crm.md): every typed method, including deals and tasks
* [Errors, retries and options](../reference/sdk/errors-and-options.md)
