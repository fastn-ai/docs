---
description: "Register, find, read, list, change and remove your customers with the SDK."
---

# Customers

Each business you serve is a customer org under your account. You address it with your own id for it:

```typescript
const customer = fastn.customer("acme_customer_42");
```

You do not have to register a customer before you create a [setup link](connecting-apps.md#setup-links) for it: the link creates the customer on first use. Register first when you want to set its name yourself.

| Do this | SDK | Input | Answer |
| ------- | --- | ----- | ------ |
| Create | `customer.register({ name })` | `name` (required): display name. Optional: `slug` (made from the name when left out), `plan`, `tier`, `limits`, `domain`. | The customer. Calling it again for the same id returns the existing customer instead of a second one. |
| Look up | `customer.find()` | None | The customer row, or `undefined` when fastn does not know this id. |
| Read | `customer.get()` | None | `{ data: customer }` |
| List all | `fastn.orgs.listOrgs({ parent_id })` | Optional: `parent_id` (your own org id, from `fastn.me()`), `type` (`end_org` for customers), `include_usage: "true"` (adds usage numbers per customer). | `{ data: [customer, …] }` |
| Change | `customer.update({ name?, status? })` | `name`: a new display name. `status`: `active` or `suspended`. | The updated customer. |
| Remove | `customer.remove()` | None | Nothing. See the warning below. |
| Trace a request | `customer.callLog(correlationId)` | The `correlationId` you sent on a call. | One entry per app call fastn made for that request. |

```typescript
const customer = fastn.customer("acme_customer_42");

await customer.register({ name: "Acme Dental" });

const row = await customer.find();          // undefined when unknown

const { data } = await customer.get();
console.log(data.name, data.status);
```

### A customer

```json
{
  "data": {
    "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
    "name": "Acme Dental",
    "slug": "acme-dental",
    "orgId": "acme_customer_42",
    "externalRef": "acme_customer_42",
    "parentId": "your-org-id",
    "type": "end_org",
    "status": "active",
    "plan": "free",
    "adminEmail": null,
    "adminUserId": null,
    "createdAt": "2026-10-17T14:23:25.667Z",
    "updatedAt": "2026-10-23T12:10:19.545Z"
  }
}
```

| Field | Meaning |
| ----- | ------- |
| `id` | fastn's own id for the customer; you can ignore it. Match the customer by your own id, in the next row. |
| `orgId`, `externalRef` | Your id for the customer (the same value). Use it to match the customer. |
| `parentId` | Your own org: the account the customer belongs to. |
| `type` | `end_org` for a customer. |
| `status` | `active` or `suspended`. |

Rows from `customer.find()` and `listOrgs` carry two more fields, `connectionsCount` and `tierId`. With `include_usage: "true"`, `listOrgs` rows also carry `executions`, `events`, `storage_gb`, `overage`, `credits`, `integrations` and `users`.

### List your customers

```typescript
const me = await fastn.me();
const list = await fastn.orgs.listOrgs({ parent_id: String(me.org?.id), type: "end_org" });

for (const c of list.data ?? []) console.log(c.externalRef, c.name);
```

`customer.find()` and every other `customer` method only look at customers under your own org, so they never return another account's customer.

### Change a customer, trace a request

```typescript
await customer.update({ name: "Acme Dental Group" });
await customer.update({ status: "suspended" });

const calls = await customer.callLog("req_abc");       // what fastn did for correlationId req_abc
```

### Remove a customer

```typescript
await fastn.customer("acme_customer_42").remove();
```

{% hint style="danger" %}
`remove()` suspends the customer and then deletes it. Its connections and data go with it, and there is no undo. If the delete fails, the SDK checks the customer again: when it is already gone, that counts as removed; otherwise the customer is set back to `active` and the error says so.
{% endhint %}

See also [Customers](../../operate/customers.md) for the same customers in the dashboard.
