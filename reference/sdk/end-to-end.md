---
description: "Build a partner integration with the SDK from start to finish: set up once, onboard a customer, make the calls your product needs, receive events, and handle retries and errors."
---

# Build an integration, end to end

This page walks through one complete integration in the order you build it. The example is a product that serves businesses which use a calendar and a CRM (a scheduling assistant, a sales tool, a support desk): it books meetings for a customer's calendar and keeps the customer's CRM up to date. Swap the apps and the fields for yours; the shape stays the same.

Words used here: a **customer** is one business you serve. An **account** is one app a customer connected (its Google Calendar, its HubSpot). Your one **API key** runs every call.

---

## 1. Before you start

### 1.1 Your constants

Keep every fixed value in one place.

| Value | Where it is used |
| ----- | ---------------- |
| Base URL `https://api.fastn.dev` | The client. It is the default. |
| API key `fsk_live_…` | Every call. Create it on [API keys](../../manage/api-keys.md). It is a password: secret store only. |
| Webhook secret `whsec_…` | Checking that an event really came from fastn (2.1). You get it once, when you register the webhook. |
| Package `@fastn-ai/sdk` 0.4.0 or newer, Node.js 20 or newer | `npm install @fastn-ai/sdk` |

### 1.2 Create the client

```typescript
// fastn.ts
import { FastnClient } from "@fastn-ai/sdk";

export const fastn = new FastnClient({ apiKey: process.env.FASTN_API_KEY! });

// one object per customer, named by YOUR id for that customer
export const forCustomer = (customerRef: string) => fastn.customer(customerRef);
```

Create one client when your app starts and reuse it: it caches the lookups it makes. `fastn.me()` tells you who the key is (`role`, `org.id`).

### 1.3 Names, dates and ids

* Record fields are `snake_case`, the catalogue's own names (`start_time`, `first_name`, `parent_id`). Options and setup arguments are `camelCase` (`idempotencyKey`, `connectionName`).
* Dates go in as ISO 8601 with a zone (`2026-11-03T15:00:00Z`) or as a JavaScript `Date`; they come back as ISO 8601 in the app's own zone.
* You choose the customer id (`customerRef`), any string unique per customer. fastn also has its own id for the customer; you never need it.
* Ids you receive and keep: `setupId` (a setup link), `connectionId` (one connected account), a record id (the meeting or contact inside the app), `requestId` (from an error, for support).

---

## 2. Set up once

### 2.1 Register your webhook and check signatures

```typescript
const hook = await fastn.webhooks.create({
  url: "https://api.example.com/fastn/events",
  eventTypes: [
    "connection.connected", "connection.revoked", "connection.expired",
    "setup_link.completed", "setup_link.expired",
    "connector.event", "unified.event",
  ],
  description: "Production",
});
// hook.id = esub_…   hook.secret = whsec_… (shown once: store it now)
```

Every event is a `POST` with a JSON body and three headers: `x-fastn-event-id`, `x-fastn-timestamp` and `x-fastn-signature`. Check the signature with the SDK before you trust the body; reply `200` first and do the work after:

```typescript
import express from "express";
import { parseEvent } from "@fastn-ai/sdk";

const app = express();
app.post("/fastn/events", express.raw({ type: "application/json" }), (req, res) => {
  let event;
  try {
    event = parseEvent(process.env.FASTN_EVENT_SECRET!, req.headers, req.body);
  } catch {
    return res.status(401).end();          // not from fastn, or older than 5 minutes
  }
  res.status(200).end();                   // reply quickly, then handle it
  handle(event);                           // event.type, event.tenantRef (your customerRef), event.data
});
```

A delivery that does not get a `2xx` is retried with growing gaps for 24 hours. The event id never changes across retries: ignore a second copy of an id you have handled. You can also register the endpoint in the dashboard: see [Events](events.md).

### 2.2 Register your return page

When a customer finishes a setup link, the browser is sent to a page of yours. Register that address once in the dashboard, under **Widget › Embed › Setup links › Pages to send people back to**. The first address is the default; a link can pick another registered one with `redirectUrl` (3.2). An address that is not on the list is refused with `400 SETUP_LINK_REDIRECT_NOT_ALLOWED`.

---

## 3. Onboard a customer

The order: create the customer, send them a setup link per app, receive `setup_link.completed` and `connection.connected`, then turn on the app changes you want to hear about. After that, the calls of section 4 work for that customer.

### 3.1 Create the customer

```typescript
const customer = forCustomer("acme_customer_42");
const made = await customer.register({ name: "Acme Dental" });
// made.existed === true when this customerRef was registered before (nothing is created twice)
```

### 3.2 Create a setup link

```typescript
const link = await customer.connect("googleCalendar", {
  redirectUrl: "https://app.example.com/connected",      // one of the registered addresses (2.2)
  metadata: { flowId: "flow_123" },                      // comes back on the link's events
});
// send link.url to the customer; link.setupId to check or cancel it later (customer.links.get / cancel)
```

One link per app: `connect("hubspot")` for their CRM. The link works once and expires after the lifetime set in the dashboard. The browser lands on your return page with `?status=completed&setupId=…` when it is done.

### 3.3 What you receive when the customer connects

| Event | When | What to keep |
| ----- | ---- | ------------ |
| `connection.connected` | The customer signed in to one app. | `event.tenantRef` (your customerRef), `event.app`, `event.connectionId` |
| `setup_link.completed` | The setup link is finished. | `event.setupLinkId`, `event.connections` (app → `connectionId`), `event.metadata` |
| `connection.expired` | The app rejected the stored login. | Send a new setup link for `event.app`. |
| `connection.revoked` | The account was removed. | Stop using that `connectionId`. |

You do not have to store `connectionId`: the typed methods find the customer's account by themselves. Keep it only when a customer has two accounts for the same app.

### 3.4 Turn on app changes

```typescript
await customer.watch("hubspot", ["contact.created", "contact.updated", "deal.stageChanged"]);
// each change arrives as a connector.event (the app's own body) and a unified.event (unified fields) on your webhook
```

`customer.watchableEvents("hubspot")` lists what the app offers; `customer.unwatch("hubspot")` turns it off. HubSpot has no stage-only event: `deal.stageChanged` maps to `deal.propertyChange`, so filter on `propertyName === "dealstage"` in the event.

### 3.5 The customer's accounts, and when a customer leaves

```typescript
const accounts = await customer.connections();        // accounts.data: one row per connected app (id, name, connector.slug, status)
await customer.renameAccount(accountId, "Front desk calendar");
await customer.disconnect(accountId);                  // only this customer's accounts: another customer's id is 404 CONNECTION_NOT_FOUND
await customer.remove();                               // the customer and everything connected; no undo
```

---

## 4. During a call

Every typed method takes the request options last: `idempotencyKey` (makes a write safe to retry), `correlationId` (your id for the request, to trace it later), `provider` and `connectionId` (when the customer has more than one app or account), `timeoutMs`, `retries`. See [Errors, retries and options](errors-and-options.md).

### 4.1 Check free time

```typescript
const free = await customer.calendar.freeSlots({
  start_time: "2026-11-03T08:00:00Z",
  end_time: "2026-11-03T18:00:00Z",
  timezone: "Europe/London",
  slot_minutes: 30,
});
// free.busy (from the calendar), free.free (the gaps), free.slots (the gaps cut into 30-minute pieces)
```

### 4.2 Book, find, reschedule, cancel

```typescript
const booked = await customer.calendar.book(
  { title: "Intro call", start_time: "2026-11-03T15:00:00Z", end_time: "2026-11-03T15:30:00Z", timezone: "Europe/London", attendee_email: "jane@example.com" },
  { idempotencyKey: "call_9f2_book", correlationId: "call_9f2" },
);
// booked.id (the meeting id in the calendar), booked.data.web_url

const found = await customer.calendar.find({ start_time: "2026-11-03T00:00:00Z", end_time: "2026-11-04T00:00:00Z", query: "jane@example.com" });
// found.records: one page; the search has no cursor, narrow the window or the query instead

await customer.calendar.reschedule(booked.id, { start_time: "2026-11-03T16:00:00Z", end_time: "2026-11-03T16:30:00Z" });
await customer.calendar.cancel(booked.id, { idempotencyKey: "call_9f2_cancel" });
```

### 4.3 Find the caller in the CRM, or add them

```typescript
const page = await customer.crm.contacts.find({ phone: "+15550100" });
const contact = page.records[0] ?? (await customer.crm.contacts.create(
  { first_name: "Jane", last_name: "Doe", phone: "+15550100", email: "jane@example.com" },
  { idempotencyKey: "contact_+15550100" },
));
```

A contact you have just added can take about ten seconds to show up in a phone search: search again before creating a second one.

### 4.4 Log the call, add a task, move a deal

```typescript
await customer.crm.notes.add({ body: "Booked an intro call for 3 Nov", parent_id: contact.id, parent_type: "contact" });
await customer.crm.tasks.add({ subject: "Call back", due_date: "2026-11-05T09:00:00Z", status: "open" });

const deal = await customer.crm.deals.create({ name: "Acme Dental: 12 chairs", amount: 48000, stage: "appointmentscheduled" });
await customer.crm.deals.moveStage(deal.id, "qualifiedtobuy");   // customer.crm.deals.stages() lists the stages the app knows
```

Every record answer is `{ id, provider, data, warnings? }`; `warnings` lists a field the app does not map and therefore dropped. The fields each entity takes are in the catalogue: `fastn.catalog.fields("crm", "contact")`. For an entity without a typed method, `customer.records({ category, entity })` takes any catalogue entity; for an app's own action, `customer.runAction(…)`. See [Calendar and CRM](calendar-and-crm.md) and [Unified records](unified-records.md).

---

## 5. Retries, tracing and limits

| Topic | What to do |
| ----- | ---------- |
| Retry keys | Pass `idempotencyKey` on every write. The same key with the same input returns the first answer instead of creating a second record; the same key with different input is `422`; a key whose first run is still going is `409 IDEMPOTENCY_IN_PROGRESS` (wait a moment, send the same call again). |
| Your call id | Pass `correlationId` on the calls of one conversation. `customer.callLog(correlationId)` then lists every app call fastn made for it. |
| What the SDK retries | Reads, and writes that carry an `idempotencyKey`, on `429`, `502`, `503`, `504` and network errors, twice by default. Everything else is thrown to you. |
| Rate limits | `429` carries `Retry-After`; the SDK waits for it. |
| Slow apps | Set `timeoutMs` per call when a provider is known to be slow; the default is 60 seconds. |

---

## 6. Errors you will meet

| Error | Means | Do |
| ----- | ----- | -- |
| `404 NO_CONNECTED_PROVIDER` | The customer has not connected an app for this entity. | Send a setup link (3.2). |
| `409 PROVIDER_AMBIGUOUS` | Two apps of the same kind are connected. | Pass `{ provider: "hubspot" }`. |
| `404 OPERATION_NOT_SUPPORTED` | The connected app cannot do this operation. | Check `customer.catalog.providers(category, entity)`. |
| `404 WIDGET_NOT_FOUND` | No widget on your account offers this app. | Add the app to your widget in the dashboard. |
| `400 UNIFIED_VALIDATION_FAILED` | A required field is missing or a field is unknown. | The message names the field. |
| `400 SETUP_LINK_REDIRECT_NOT_ALLOWED` | `redirectUrl` is not registered. | Register it in the dashboard first (2.2). |
| `404 CONNECTION_NOT_FOUND` | The account id is not one of this customer's. | Read `customer.connections()`. |
| `502 UNIFIED_PROVIDER_ERROR` | The app refused the request. | `e.body.providerStatus` and `e.body.providerError` say why. |

Every failure is a `FastnApiError` with `status`, `code`, `message` and `requestId` (quote it when you ask for help), or a `FastnNetworkError`. The full list is on [Errors, retries and options](errors-and-options.md).
