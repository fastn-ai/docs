---
description: "Receive signed events about connections, setup links and app changes, verify them with parseEvent, and manage deliveries."
---

# Events

fastn can tell your backend when something happens: a customer connected an app, a setup link was used, or a record changed in a customer's app. You register an https endpoint once (an **event subscription**). fastn then sends each event to it as a signed `POST`.

---

## Register your endpoint

For one customer only, create the subscription on the customer. The SDK fills in the customer for you:

```typescript
const sub = await customer.api.events.createEventSubscription({
  url: "https://hooks.example.com/fastn/events",
  eventTypes: ["connection.connected", "connection.revoked", "connection.expired", "setup_link.completed", "setup_link.expired"],
  description: "Production",
});

const subscriptionId = sub.data?.id;   // esub_…
const secret = sub.data?.secret;       // whsec_…: shown once, store it now
```

For every customer at once, call `fastn.events.createEventSubscription({ … })` with the same fields.

| Field | Required | Meaning |
| ----- | -------- | ------- |
| `url` | Yes | Your https endpoint. An `http` URL, or a private or internal address, is refused (`400 VALIDATION_ERROR`). |
| `eventTypes` | No | Which events to send (table below). Leave it out for every connection and setup link event. `connector.event` and `unified.event` are sent only when you list them. |
| `connectors` | No | `connector.event` only: just events from these apps (slug or connector id), for example `["hubspot"]`. |
| `providerEvents` | No | `connector.event` only: just these app event names, for example `["contact.creation"]`. |
| `entities` | No | `unified.event` only: just these entities, as `category/entity`, for example `["crm/contact"]`. |
| `endOrgId` | No | Only events about this customer, by your customer id. The customer form above fills it in for you. |
| `description` | No | Your label. |
| `enabled` | No | Default `true`. |

Answer: `{ data: { id, url, endOrgId, eventTypes, connectors, providerEvents, entities, enabled, description, createdBy, createdAt, updatedAt, secret } }`. The `secret` is returned **only here**: reading the subscription later never shows it.

---

## Event types

| `type` | Sent when | Fields on top of the common ones |
| ------ | --------- | -------------------------------- |
| `connection.connected` | A customer connected an account, or signed in to it again. | `app`, `connectionId`, `connectionName`, and when known `account`, `setupLinkId`, `metadata` |
| `connection.revoked` | An account was removed. | `app`, `connectionId` |
| `connection.expired` | The app rejected the stored login; the customer must sign in again. | `app`, `connectionId`, `reason` (for example `needs_reauth`) |
| `setup_link.completed` | The customer finished a setup link. | `setupLinkId`, `installationId`, `connections` (app slug → `connectionId`), `metadata` |
| `setup_link.expired` | A setup link expired unused. | `setupLinkId`, `metadata` |
| `connector.event` | A change in a customer's app, for example a new HubSpot contact. Needs an [app event trigger](#app-events). | `app`, `connector`, `connectionId`, `event` (the app's event name), `accountId`, `triggerId`, `payload` (the app's own body) |
| `unified.event` | The same app change, as a unified record. Needs an [app event trigger](#app-events). | `app`, `connector`, `connectionId`, `category`, `entity`, `action` (`created`, `updated` or `deleted`), `remoteId` (the record id in the app), `providerEvent`, `triggerId`, and `record` (the unified record `{ id, provider, data }`) or `recordError` (why it could not be read) |
| `endpoint.test` | You sent a test with `testEventSubscription`. | None |

Every event carries `id` (`evt_…`), `type`, `occurredAt`, `tenantRef` (your customer id: match on this) and `endOrgId` (fastn's own id for the customer; you can ignore it). `metadata` is the object you set on the setup link.

```json
{
  "id": "evt_3f9a0c2b7d4e4b8e9a1c5d6e7f8a9b0c",
  "type": "setup_link.completed",
  "occurredAt": "2026-10-26T00:01:03.486Z",
  "tenantRef": "acme_customer_42",
  "endOrgId": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
  "setupLinkId": "stp_1a2b3c4d5e6f",
  "installationId": "inst_…",
  "connections": { "hubspot": "ucl:…:default" },
  "metadata": { "flowId": "flow_123" }
}
```

---

## Receive and verify events

Each delivery carries these headers:

| Header | Meaning |
| ------ | ------- |
| `X-Fastn-Signature` | `sha256=` + HMAC-SHA256 of `<timestamp>.<raw body>`, keyed with your `whsec_…` secret. |
| `X-Fastn-Timestamp` | Unix seconds when the delivery was signed. |
| `X-Fastn-Event-Id` | The event id. It stays the same on every retry. |
| `X-Fastn-Redelivery` | `true` on a resend. |

`parseEvent` checks the signature, refuses deliveries older than five minutes, and returns the event. Give it the **raw** body exactly as received: a re-serialised object changes the bytes and fails the check.

```typescript
import express from "express";
import { parseEvent } from "@fastn-ai/sdk";

const app = express();
const seen = new Set<string>();

app.post("/fastn/events", express.raw({ type: "application/json" }), (req, res) => {
  let event;
  try {
    event = parseEvent(process.env.FASTN_EVENT_SECRET!, req.headers, req.body);
  } catch {
    res.status(401).end();           // wrong signature, altered body, or too old
    return;
  }

  if (event.id && seen.has(event.id)) {
    res.status(200).end();           // a retry of an event you already handled
    return;
  }
  if (event.id) seen.add(event.id);

  res.status(200).end();             // answer fast, then do the work

  switch (event.type) {
    case "connection.connected":
      console.log(event.tenantRef, "connected", event.app, event.connectionId);
      break;
    case "setup_link.completed":
      console.log(event.tenantRef, "finished setup", event.setupLinkId, event.metadata);
      break;
  }
});

app.listen(3000);
```

In production keep the seen ids in your database rather than in memory.

| Function | Input | Answer |
| -------- | ----- | ------ |
| `parseEvent(secret, headers, rawBody, opts?)` | `secret`: your `whsec_…`. `headers`: the request headers (Node, Fetch `Headers`, or a plain object). `rawBody`: string or `Buffer`. | The event object plus `headers` (`timestamp`, `signature`, `eventId`, `redelivery`). Throws when the signature does not match or the timestamp is too old. |
| `verifyEventSignature(secret, headers, rawBody, opts?)` | Same as above. | `true` or `false`, without parsing. |
| `readEventHeaders(headers)` | The request headers. | `{ timestamp, signature, eventId, redelivery }` |
| `signEventBody(secret, timestamp, rawBody)` | | The signature string fastn would send. Useful in your own tests. |

`opts.toleranceSeconds` changes the five-minute window (default 300; `0` turns the age check off).

Test your handler without fastn by signing a body yourself:

```typescript
import { parseEvent, signEventBody } from "@fastn-ai/sdk";

const body = JSON.stringify({ id: "evt_123", type: "endpoint.test", tenantRef: "acme_customer_42" });
const ts = Math.floor(Date.now() / 1000);
const headers = {
  "x-fastn-timestamp": String(ts),
  "x-fastn-signature": signEventBody("whsec_test", ts, body),
  "x-fastn-event-id": "evt_123",
};

const event = parseEvent("whsec_test", headers, body);   // { id: "evt_123", type: "endpoint.test", … }
```

---

## Deliveries and retries

fastn retries a delivery with growing gaps for 24 hours, until your endpoint answers `2xx`. After that the delivery is marked `dead`. The event id never changes, so drop repeats by id.

| Do this | SDK | Answer |
| ------- | --- | ------ |
| Send a test event | `fastn.events.testEventSubscription({ id: "esub_…" })` | `{ data: { eventId, status: "queued" } }`. Sends one `endpoint.test` event. |
| See deliveries | `fastn.events.listEventDeliveries({ id: "esub_…", status?, limit? })` | `{ data: [ { id, eventId, type, status, attempts, lastStatus, lastError, nextAttemptAt, createdAt, deliveredAt } ] }`. `status` is `pending`, `delivered` or `dead`. |
| Send one again | `fastn.events.replayEventDelivery({ id: "evd_…" })` | Sends the delivery again with the same event id, marked as a redelivery. Works for `dead` deliveries too. |
| Pause or change | `fastn.events.updateEventSubscription({ id, url?, eventTypes?, connectors?, providerEvents?, entities?, description?, enabled? })` | The updated subscription. With `enabled: false`, events queue and are sent when you enable it again. |
| Read | `fastn.events.getEventSubscription({ id })` / `fastn.events.listEventSubscriptions()` | The subscription(s), without the secret. |
| New secret | `fastn.events.rotateEventSubscriptionSecret({ id })` | A new secret, returned once. Deliveries after this are signed with it. |
| Remove | `fastn.events.deleteEventSubscription({ id })` | `{ data: { id, deleted: true } }`. Queued deliveries go with it. |

---

## App events

`connector.event` and `unified.event` come from changes inside a customer's app. fastn receives them only after you create an **app event trigger** for that customer's account.

First list the events an app offers:

```typescript
const conns = await customer.connections();
const hubspot = (conns.data ?? []).find((c: any) => c.connector?.slug === "hubspot");

const offered = await fastn.events.listConnectorEvents({ connectorId: String(hubspot?.connectorId) });
// offered.data.events = [ { id: "contact.creation", label: "Contact Created", description, payloadSchema }, … ]

// Then create the trigger for that account
await fastn.events.createAppEventTrigger({
  name: "Acme HubSpot contacts",
  connectorId: String(hubspot?.connectorId),
  connectorName: "HubSpot",
  events: [
    { id: "contact.creation", label: "Contact Created" },
    { id: "contact.propertyChange", label: "Contact Property Changed" },
  ],
  type: "WEBHOOK",
  accountId: "<the account id in the app, for example the HubSpot portal id>",
  endOrgId: "acme_customer_42",
  connectionId: String(hubspot?.id),
  status: "ACTIVE",
});
```

| Field | Required | Meaning |
| ----- | -------- | ------- |
| `name` | Yes | Your label. |
| `connectorId` | Yes | The app's id: `connectorId` of the connection. |
| `connectorName` | Yes | The app's name, for example `HubSpot`. |
| `events` | Yes | The app events to receive, each `{ id, label }`, from `listConnectorEvents`. |
| `endOrgId` | For a customer's account | Your customer id, `"acme_customer_42"` |
| `connectionId` | For a customer's account | The connection the events are for. |
| `accountId` | When the app needs it | The app's own account id, for example the HubSpot portal id or a Facebook Page id. |
| `type` | No | `WEBHOOK` or `POLLING`. |
| `status` | No | `ACTIVE` or `DISABLED`. |

List triggers with `fastn.events.listAppEventTriggers()` and remove one with `fastn.events.deleteAppEventTrigger({ id })`. See also [App event triggers](../../build/triggers/app-events.md) and, for the events fastn received, [Events](../../operate/events.md).
