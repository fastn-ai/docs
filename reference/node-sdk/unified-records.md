---
description: "One set of methods for every app: create, get, list, search, update and delete unified records, and find the fields each entity takes."
---

# Unified records

The [unified API](../../build/unified-apis/README.md) gives every app of one kind the same record shape. A contact has the same fields whether it lives in HubSpot or Salesforce; a meeting has the same fields in Google Calendar or Outlook.

The SDK has no app-specific methods. Every app goes through one call:

```typescript
const contacts = customer.records({ category: "crm", entity: "contact", provider: "hubspot" });
const meetings = customer.records({ category: "scheduling", entity: "meeting", provider: "googleCalendar" });
```

Then `create`, `get`, `list`, `search`, `update` or `delete` on it. To use another app, change only `provider`; the code stays the same.

| `records()` field | Required | Meaning |
| ----------------- | -------- | ------- |
| `category` | Yes | The kind of app, for example `crm` or `scheduling`. |
| `entity` | Yes | The kind of record, for example `contact`, `note`, `task`, `opportunity`, `engagement`, `meeting` or `availability`. |
| `provider` | No | The app's slug, for example `hubspot`. Leave it out to use whichever app of that kind the customer connected. When the customer has more than one, single-record calls need it. |
| `connectionId` | No | One account, when the customer has more than one for the same app. See [below](#pick-one-account-connectionid). |

---

## Find categories, entities and fields

The catalogue is live. Read it rather than hard-coding it:

```typescript
const catalog = await fastn.unified.listUnifiedCategories();

for (const category of catalog.data ?? []) {
  for (const entity of category.entities ?? []) {
    console.log(category.slug, entity.slug, entity.operations, entity.connectorSlugs);
  }
}
```

| Field | Meaning |
| ----- | ------- |
| `data[].slug` | The category, for `records({ category })`. |
| `data[].entities[].slug` | The entity, for `records({ entity })`. |
| `entities[].operations` | What the entity supports overall: `create`, `get`, `list`, `search`, `update`, `delete`. A single app can support fewer (see below). |
| `entities[].connectorSlugs` | The apps mapped for this entity: the values `provider` can take. |
| `entities[].createFields` | The fields you can send: `{ field, label, type, required }`. `required: true` means a create is refused without it. |

For example, the `crm` / `note` entity lists these `createFields`:

| `field` | `type` | `required` | `label` |
| ------- | ------ | ---------- | ------- |
| `body` | string | true | Body |
| `parent_id` | string | true | Parent record ID |
| `parent_type` | string | false | Parent record type (contact, deal, company, account, lead, opportunity) |
| `created_at` | string | false | Created at (ISO 8601; used as the note timestamp for HubSpot) |
| `title` | string | false | Title |

Times are ISO 8601 strings with `Z` or an offset, for example `2026-11-03T15:00:00Z`.

### Which apps a customer can use

```typescript
const providers = await contacts.providers();

for (const p of providers.data ?? []) {
  console.log(p.connectorSlug, p.connected, p.operations);
}
```

Each row of `providers().data`:

| Field | Meaning |
| ----- | ------- |
| `connectorSlug`, `connectorName` | The app. |
| `operations` | What **this app** supports for this entity, for example `["get", "list", "create"]`. An operation not in the list fails with `UNIFIED_UNSUPPORTED_OPERATION`. |
| `connected` | `true` when the customer can use an active connection for this app. |
| `connectionCount` | How many such connections there are. |
| `healthy`, `verifyStatus` | The connection's health check result, when one has run. |

Use `connected: false` rows to show "Connect" buttons, and send a [setup link](connecting-apps.md#setup-links).

---

## Create

```typescript
const created = await contacts.create(
  { first_name: "Jane", last_name: "Doe", email: "jane@example.com" },
  { idempotencyKey: "signup_9f2_contact" },
);

console.log(created.id, created.provider, created.data);
```

Answer:

```json
{
  "id": "51234567890",
  "provider": "hubspot",
  "data": {
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane@example.com",
    "created_at": "2026-10-25T23:58:19.258Z"
  }
}
```

`id` is the record's id in the app. Keep it to read, change or delete the record later.

* Pass an `idempotencyKey` on writes. Sending the same key again returns the first answer (the same `id`) instead of creating a second record. See [Errors, retries and options](errors-and-options.md#safe-retries-idempotencykey).
* A field the catalogue does not know is refused: `400 UNIFIED_VALIDATION_FAILED` with `Unknown field "…"`. A missing required field gives `Field "…" is required`.
* A field the entity knows but this app does not map is skipped, and the answer says so in `warnings`, for example `["Field \"contact_id\" is not mapped for provider \"hubspot\" and was not sent"]`.

A meeting looks the same:

```typescript
const booked = await meetings.create(
  {
    title: "Intro call",
    start_time: "2026-11-03T15:00:00Z",
    end_time: "2026-11-03T15:30:00Z",
    timezone: "Europe/London",
    description: "First call",
  },
  { idempotencyKey: "booking_123", correlationId: "req_abc" },
);

console.log(booked.id, booked.data?.web_url);
```

The answer also carries fields the app sets, such as `status`, `web_url`, `organizer_email`, `created_at` and `updated_at`.

Some entities use `create` for a question rather than a new record. For example `scheduling` / `availability` returns busy times:

```typescript
const availability = customer.records({ category: "scheduling", entity: "availability", provider: "googleCalendar" });

const free = await availability.create({
  start_time: "2026-11-03T08:00:00Z",
  end_time: "2026-11-03T18:00:00Z",
  timezone: "Europe/London",
});
// free.data.busy = [ { start: "2026-11-03T15:00:00Z", end: "2026-11-03T15:30:00Z" } ]
```

---

## Get, update and delete

```typescript
const one = await contacts.get("51234567890");

const changed = await contacts.update(
  "51234567890",
  { last_name: "Doe-Smith" },
  { idempotencyKey: "signup_9f2_rename" },
);

const removed = await contacts.delete("51234567890", { idempotencyKey: "signup_9f2_delete" });
// removed = { id: "51234567890", provider: "hubspot", deleted: true }
```

| Method | Input | Answer |
| ------ | ----- | ------ |
| `get(id)` | `id` (required): the record id. | `{ id, provider, data }` |
| `update(id, fields)` | `id` (required). `fields`: only the fields that change. | `{ id, provider, data }` |
| `delete(id)` | `id` (required). | `{ id, provider, deleted: true }` |

What delete means is up to the app. Some archive the record (HubSpot), so a later `get` fails. Some mark it cancelled (a Google Calendar meeting), so a later `get` still works and shows `status: "cancelled"`.

---

## List and page through records

```typescript
const page = await contacts.list({ page_size: 50 });

for (const r of page.records ?? []) console.log(r.id, r.data);

if (page.hasMore && page.nextCursor) {
  const next = await contacts.list({ page_size: 50, cursor: page.nextCursor });
}
```

| Input | Required | Meaning |
| ----- | -------- | ------- |
| `page_size` | No | Records per page, from 1 to 200. |
| `cursor` | No | The `nextCursor` from the previous page. |
| `include_remote_data` | No | `true` adds `remoteData` to each record: the app's own raw record beside the unified one. |

Answer: `{ records: [ { id, provider, data } ], nextCursor, hasMore, provider }`. Keep calling with the new `nextCursor` while `hasMore` is `true`.

To read every page in one loop:

```typescript
let cursor: string | undefined;
do {
  const page = await contacts.list({ page_size: 100, cursor });
  for (const r of page.records ?? []) console.log(r.id);
  cursor = page.hasMore ? (page.nextCursor ?? undefined) : undefined;
} while (cursor);
```

---

## Search

```typescript
const found = await contacts.search({ email: "jane@example.com" });

const inWindow = await meetings.search({
  start_time: "2026-11-03T00:00:00Z",
  end_time: "2026-11-03T23:59:00Z",
  query: "Intro call",
});
```

`search` takes the fields to match as one object. Which fields an app can search by depends on its mapping, for example `email` or `phone` for a CRM contact, and a time window plus `query` text for a meeting.

Answer: `{ records: [ … ], hasMore, provider }` (plus `nextCursor` when there are more). No match gives `{ records: [], hasMore: false }`.

---

## Pick one account: connectionId

When a customer has two accounts for the same app (for example two calendars), pass the one to use:

```typescript
const secondCalendar = customer.records({
  category: "scheduling",
  entity: "meeting",
  provider: "googleCalendar",
  connectionId,
});
```

Get `connectionId` from `customer.connections()` or the `connection.connected` event (see [Connecting apps](connecting-apps.md#connections)). A wrong or removed id is an error (`404 UNIFIED_CONNECTION_NOT_FOUND`), never a silent fallback to another account.

---

## Errors from unified calls

| Status and code | Means |
| --------------- | ----- |
| `400 UNIFIED_VALIDATION_FAILED` | A field is unknown, has the wrong type, or a required field is missing. The message names the field. |
| `404 UNIFIED_UNSUPPORTED_ENTITY` | The category or entity does not exist. |
| `404 UNIFIED_UNSUPPORTED_OPERATION` | This app does not support the operation for this entity (check `providers()`). Use a [direct app action](app-actions.md) instead. |
| `404 UNIFIED_NO_CONNECTED_PROVIDER` | The customer has no active connection for any app mapped to this entity (or for the `provider` you named). Send a setup link. |
| `404 UNIFIED_CONNECTION_NOT_FOUND` | The `connectionId` is wrong, removed or not active. |
| `409 UNIFIED_MULTIPLE_PROVIDERS` | Several apps are connected and the call needs one: pass `provider`. |
| `502 UNIFIED_PROVIDER_ERROR` | The app refused the request, for example a record id that does not exist (or was archived). When `details` is present, it carries what the app said. |

The full list of error fields is on [Errors, retries and options](errors-and-options.md#errors).
