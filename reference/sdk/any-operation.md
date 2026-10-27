---
description: "Every other fastn API operation from the SDK: by area, by name with call(), for one customer, and with paginate()."
---

# Any other operation

The pages before this one cover the common partner flow. The SDK also has a method for every other partner operation of the fastn API.

### By area

Operations are grouped in areas on the client, and each method has the same name as the operation:

```typescript
await fastn.orgs.getTenant({ id: "acme_customer_42" });
await fastn.connections.listConnections({ endOrgId: "acme_customer_42" });
await fastn.events.listEventSubscriptions();
await fastn.embed.listWidgets();
```

Some areas: `orgs`, `embed`, `connections`, `connectors`, `unified`, `events`, `workflows`. Your editor lists every area and method, with typed inputs. `fastn.api` holds the same areas (`fastn.api.orgs` is `fastn.orgs`).

Inputs are one object. Path, query, body and header fields all go in it by name; the SDK puts each where the API expects it.

Wherever an input names a customer (`id` on the customer routes, `endOrgId` elsewhere), pass your own customer id, as above.

### By name: call()

```typescript
const orgs = await fastn.call("listOrgs", { type: "end_org" });
```

`fastn.call(operationId, input, options)` runs any operation by its name. Use it when the name comes from data, for example a list of operations.

### For one customer: customer.api

`customer.api.<area>.<operation>()` runs an operation for one customer. Each call carries your customer id, and on routes that take the customer in the body, the SDK fills that field too.

```typescript
await customer.api.events.createEventSubscription({ url: "https://hooks.example.com/fastn/events" });
```

{% hint style="warning" %}
Not every route reads the customer from the request. Prefer the customer methods on the earlier pages where they exist (`customer.connections()`, `customer.records(...)`, `customer.setupLink(...)`), and check the answer of any other `customer.api` call. For example `customer.api.connections.listConnections()` lists your own org's connections, not the customer's: use `customer.connections()` for that.
{% endhint %}

### Page through lists: paginate()

```typescript
import { paginate } from "@fastn-ai/sdk";

for await (const event of paginate((input) => fastn.events.listEvents(input), {}, { pageSize: 100 })) {
  console.log(event.id, event.type);
}
```

`paginate(fn, input, options)` calls a list operation page after page and yields one row at a time. It stops on a short page, when there is no next cursor, or when the list ignores paging.

| Option | Default | Meaning |
| ------ | ------- | ------- |
| `pageSize` | 100 | Rows per request. |
| `limitKey` | `limit` | The input name for the page size. |
| `offsetKey` | `offset` | The input name for the offset. Set it to `null` for cursor-only lists. |
| `cursorKey` | `cursor` | The input name for the cursor. |
| `rows` | `data`, `data.items`, `items` or `records` | A function that picks the rows out of an answer. |
| `nextCursor` | `nextCursor`, `data.nextCursor` or `cursor` | A function that picks the next cursor out of an answer. |
| `maxPages` | 1000 | A safety cap on pages. |

For unified records, page with `cursor` and `hasMore` as shown in [Unified records](unified-records.md#list-and-page-through-records).

See [HTTP API](../api.md) for the same API over plain HTTP.
