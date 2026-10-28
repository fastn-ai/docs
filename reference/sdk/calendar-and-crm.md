---
description: "Typed calendar and CRM methods on a customer: book and find meetings, free slots, contacts, notes, tasks and deals, with the app picked from what the customer connected."
---

# Calendar and CRM

`customer.calendar` and `customer.crm` are the [unified API](unified-records.md) with the fields named. Each method takes a TypeScript interface with the catalogue's own field names (`start_time`, `first_name`, …) and answers a record `{ id, provider, data, warnings? }` or a page `{ records, nextCursor, hasMore }`. You never name the app: the SDK reads which app the customer connected for that entity and uses it.

```typescript
const customer = fastn.customer("acme_customer_42");

const booked = await customer.calendar.book(
  { title: "Intro call", start_time: "2026-11-03T15:00:00Z", end_time: "2026-11-03T15:30:00Z", timezone: "Europe/London", attendee_email: "jane@example.com" },
  { idempotencyKey: "booking_123", correlationId: "req_abc" },
);
console.log(booked.id, booked.provider, booked.data.web_url);

const { records } = await customer.crm.contacts.find({ email: "jane@example.com" });
const contact = records[0] ?? (await customer.crm.contacts.create({ first_name: "Jane", last_name: "Doe", email: "jane@example.com" }));
await customer.crm.notes.add({ body: "Booked an intro call", parent_id: contact.id, parent_type: "contact" });
```

Every method takes the [request options](errors-and-options.md#request-options) last: `provider`, `connectionId`, `idempotencyKey`, `correlationId`, `timeoutMs`, `retries`.

---

## Which app answers

| Situation | What happens |
| --------- | ------------ |
| The customer connected one app for the entity | It is used. The choice is kept for 60 seconds per client, then read again, so a new connection is picked up without a restart. |
| None | `404 NO_CONNECTED_PROVIDER`. Send a [setup link](connecting-apps.md#connect-by-app). |
| Several, for example two CRMs | `409 PROVIDER_AMBIGUOUS`. Pass `{ provider: "hubspot" }` on the call. |
| The connected app cannot do this operation | `404 OPERATION_NOT_SUPPORTED`. Check `customer.catalog.providers(category, entity)`. |
| Two accounts for the same app | Pass `{ connectionId }` (from `customer.connections()`). |

`Date` values are sent as ISO strings. `warnings` on an answer lists a field the app does not map and therefore dropped.

---

## Calendar

| Method | Underneath | Input |
| ------ | ---------- | ----- |
| `calendar.freeSlots(window)` | scheduling/availability | `start_time`, `end_time` (required), `timezone`, `slot_minutes`. Answers `{ busy, free, slots }`: `busy` from the calendar, `free` the gaps, `slots` the gaps cut into `slot_minutes` pieces (left out without `slot_minutes`). |
| `calendar.book(meeting)` | scheduling/meeting create | `title`, `start_time`, `end_time` (required), `timezone`, `description`, `attendee_email`, `attendee_name`, `location`. |
| `calendar.get(id)` | get | The meeting id. |
| `calendar.find(filters, page?)` | search | `start_time`, `end_time` (required), `query` (matches the title, description and attendee email). `page_size` only: a search answers one page. |
| `calendar.list(page?)` | list | `page_size`, `cursor`. |
| `calendar.reschedule(id, times)` | update | `start_time`, `end_time`. |
| `calendar.cancel(id)` | delete | The meeting id. Answers `{ id, provider, deleted: true }`. |

```typescript
const slots = await customer.calendar.freeSlots({
  start_time: "2026-11-03T08:00:00Z",
  end_time: "2026-11-03T18:00:00Z",
  timezone: "Europe/London",
  slot_minutes: 30,
});
// slots.busy, slots.free, slots.slots: [{ start_time, end_time }, …]

await customer.calendar.reschedule(booked.id, { start_time: "2026-11-03T16:00:00Z", end_time: "2026-11-03T16:30:00Z" });
await customer.calendar.cancel(booked.id, { idempotencyKey: "cancel_123" });
```

`freeIntervals(start, end, busy)` and `slotsOf(free, minutes)` are exported too: the arithmetic behind `freeSlots`, for busy times you already have.

---

## CRM

| Group | Underneath | Methods |
| ----- | ---------- | ------- |
| `crm.contacts` | crm/contact | `create`, `get`, `find({ email, phone, first_name, last_name })`, `list`, `update`, `delete` |
| `crm.notes` | crm/note | `add({ body, parent_id, parent_type, title?, created_at? })`, `update`, `delete`. `created_at` defaults to now. |
| `crm.tasks` | crm/task | `add({ subject, due_date, status, … })`, `get`, `list`, `update`, `delete` |
| `crm.deals` | crm/opportunity and crm/stage | `create({ name, amount, stage, … })`, `get`, `list`, `update`, `moveStage(id, stage)`, `delete`, `stages()` |

```typescript
const deal = await customer.crm.deals.create({ name: "Acme Dental: 12 chairs", amount: 48000, stage: "appointmentscheduled" });
const stages = await customer.crm.deals.stages();           // the pipeline stages the app knows
await customer.crm.deals.moveStage(deal.id, "qualifiedtobuy");

await customer.crm.tasks.add({ subject: "Call back", due_date: "2026-11-05T09:00:00Z", status: "open" });
```

`find` is the app's own search and answers one page: narrow the filters or raise `page_size` to see more. Passing a `cursor` to `find` is refused with a `TypeError`; `list({ page_size, cursor })` pages.

---

## The catalogue

Which categories and entities exist, the fields each takes, and which apps a customer connected:

```typescript
const categories = await fastn.catalog.categories();                   // [{ slug: "crm", entities: [{ slug: "contact", operations, createFields }] }]
const fields = await fastn.catalog.fields("crm", "contact");           // [{ field: "email", type: "string", required: false }, …]
const providers = await customer.catalog.providers("crm", "contact");  // [{ connectorSlug: "hubspot", connected: true, operations: […] }]
```

| Method | Answer |
| ------ | ------ |
| `fastn.catalog.categories()` | Every category with its entities. Cached for the life of the client; `fastn.catalog.refresh()` reads it again. |
| `fastn.catalog.category(slug)`, `fastn.catalog.entity(category, entity)` | One category, one entity. |
| `fastn.catalog.fields(category, entity)` | The create fields, each `{ field, label, type, required }`. |
| `fastn.catalog.providers(category, entity)` | The apps mapped to the entity. |
| `customer.catalog.providers(category, entity)` | The same list with `connected` for this customer. |

What the typed methods do not cover is one call away: `customer.records({ category, entity })` takes any entity in the catalogue (see [Unified records](unified-records.md)), and `customer.runAction(…)` runs an app's own action (see [Direct app actions](app-actions.md)).
