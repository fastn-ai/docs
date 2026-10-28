---
description: "Let a customer connect their apps with a setup link or the embedded widget, then read the connections they made."
---

# Connecting apps

Before fastn can read or write a customer's data in an app, the customer has to connect that app (sign in to it). There are two ways:

| Way | What the customer sees | SDK |
| --- | ---------------------- | --- |
| **Setup link** | A hosted fastn page you send them a link to. | `customer.connect("hubspot")`, or `customer.setupLink(...)` with a widget id |
| **Embedded widget** | The fastn widget inside your own app. | `customer.embedToken(...)`, then the widget package in the browser |

Either way, the result is a **connection**: one connected account, with its own `connectionId`.

---

## Widgets

A widget decides which app (or apps) a setup link or the embedded widget offers. You build widgets in the dashboard: see [Widgets](../../embed/README.md). From the SDK you only read them, to get their ids.

```typescript
const widgets = await fastn.embed.listWidgets();
for (const w of (widgets.data ?? []) as any[]) {
  console.log(w.id, w.name, (w.connectorRefs ?? []).map((c: any) => c.slug));
}
```

| Do this | SDK | Answer |
| ------- | --- | ------ |
| List your widgets | `fastn.embed.listWidgets()` | `{ data: [ { id, name, slug, connectorRefs, unifiedRefs, enabled, status, … } ] }`. `connectorRefs[].slug` is the app, for example `hubspot`. |
| Read one | `fastn.embed.getWidget({ id: "wgt_…" })` | `{ data: widget }` |

---

## Connect by app

The short way to a setup link names the app and nothing else. The SDK finds your widget for that app, creates the link for the customer and answers the address to send:

```typescript
const link = await customer.connect("googleCalendar", {
  expiresInMinutes: 60 * 24,
  redirectUrl: "https://app.example.com/connected",
  metadata: { flowId: "flow_123" },
});

console.log(link.url);     // send this to the customer
```

| Field | Required | Meaning |
| ----- | -------- | ------- |
| app (first argument) | Yes | The app's slug, for example `googleCalendar` or `hubspot`. |
| `widgetId` | No | Which widget, when more than one of your widgets offers the app (`409 WIDGET_AMBIGUOUS` otherwise). No widget offers it: `404 WIDGET_NOT_FOUND`. |
| `connectionName`, `label`, `expiresInMinutes`, `redirectUrl`, `metadata`, `allowAdditionalConnection` | No | As on `setupLink` below. `connectionName` defaults to the widget's name. |

Answer: `{ setupId, url, status, expiresAt, widgetId }`. Read or cancel the link later with `customer.links.get(setupId)` and `customer.links.cancel(setupId)`. The widget list is reused for 60 seconds, so a widget you create after start-up is found without a restart.

---

## Setup links

A setup link is a one-time link to a hosted fastn page. The customer opens it, signs in to the app, and the connection is stored on that customer. `connect(app)` above makes one by app name; `setupLink` takes the widget id yourself:

```typescript
const link = await customer.setupLink({
  widgetId: "wgt_your_widget_id",
  connectionName: "Front desk calendar",
  label: "Acme Dental",
  expiresInMinutes: 60 * 24,
  redirectUrl: "https://app.example.com/connected",
  metadata: { flowId: "flow_123" },
  allowAdditionalConnection: false,
});

console.log(link.data?.setupUrl);   // send this link to the customer
```

### Input

| Field | Required | Meaning |
| ----- | -------- | ------- |
| `widgetId` | Yes | Which widget, and so which app, the link connects. |
| `connectionName` | Yes | The name of the new connection, for example `Front desk calendar`. It is shown to the customer and comes back on the connection. |
| `label` | No | A label for the link, for example the customer's name. |
| `expiresInMinutes` | No | How long the link works, in minutes. Your org config carries a default link lifetime (`setupLinkDefaultTtlMinutes`, below). |
| `redirectUrl` | No | Where the browser goes when setup ends. It must be on your list of registered redirect addresses (below), or the call is refused. |
| `metadata` | No | Your own data, any JSON object. fastn does not use it. It comes back to you on the link and on the link's events, so you can tell which of your flows the new connection is for. |
| `allowAdditionalConnection` | No | `true` lets the customer add another account for the same app (for example a second calendar). |

The SDK fills in the customer for you. If the customer does not exist yet, the link creates it.

### Answer

```json
{
  "data": {
    "setupId": "stp_1a2b3c4d5e6f",
    "setupUrl": "https://app.fastn.dev/setup/stp_1a2b3c4d5e6f#t=…",
    "status": "pending",
    "expiresAt": "2026-10-27T00:29:58.968Z",
    "endOrgId": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
    "metadata": { "flowId": "flow_123" },
    "redirectUrl": "https://app.example.com/connected",
    "allowAdditionalConnection": false,
    "connectionName": "Front desk calendar"
  }
}
```

| Field | Meaning |
| ----- | ------- |
| `setupUrl` | The link to send to the customer. It carries a live credential: do not log it or share it beyond the customer. |
| `setupId` | The link's id, to check or cancel it. |
| `status` | `pending` (new), `complete` (used) or `revoked` (cancelled). |
| `expiresAt` | When the link stops working. |
| `endOrgId` | fastn's own id for the customer; you can ignore it. The link belongs to the customer you created it for. |

### Check or cancel a link

| Do this | SDK | Answer |
| ------- | --- | ------ |
| Read a link | `fastn.embed.getSetupLink({ id: "stp_…" })` | `{ data: { setupId, status, widgetId, endOrgId, label, connectionName, installationId, expiresAt, redirectUrl, allowAdditionalConnection, metadata, widget } }`. `installationId` is set once the link is complete. |
| Cancel a link | `fastn.embed.cancelSetupLink({ id: "stp_…" })` | `{ data: { setupId, status: "revoked" } }` |

```typescript
const setupId = link.data?.setupId ?? "";

const status = await fastn.embed.getSetupLink({ id: setupId });
console.log(status.data?.status);    // "pending"

await fastn.embed.cancelSetupLink({ id: setupId });
```

To hear when a link is used or expires, subscribe to the `setup_link.completed` and `setup_link.expired` [events](events.md).

### Redirect addresses

`redirectUrl` must be registered on your org first. Read the list from your org config:

```typescript
const me = await fastn.me();
const config = await fastn.orgs.getOrgConfig({ id: String(me.org?.id) });

console.log(config.data?.setupLinkRedirectUrls);       // ["https://app.example.com/connected"]
console.log(config.data?.setupLinkDefaultTtlMinutes);  // the default link lifetime
```

To change it, send the **full** list with `fastn.orgs.updateOrgConfig({ id, setupLinkRedirectUrls: [ … ] })`. Saving the list replaces it, so include every address you still use.

A setup link with an address that is not on the list is refused with `400` and the code `SETUP_LINK_REDIRECT_NOT_ALLOWED`.

---

## Embedded widget: embed tokens

To show the fastn widget inside your own app instead of sending a link, your backend creates a short-lived token for the customer and hands it to the page.

```typescript
const t = await customer.embedToken({
  userId: "user_42",
  userEmail: "owner@example.com",
  userName: "Sam Owner",
});

// give t.data.token to the widget in the browser
```

| Field | Required | Meaning |
| ----- | -------- | ------- |
| `userId` | No | Your own id for the person using the widget. Leave it out and fastn makes one. |
| `userEmail`, `userName` | No | The person's email and name. |
| `metadata` | No | Your own data. |

Answer:

```json
{
  "data": {
    "token": "…",
    "endOrgId": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
    "userId": "user_42",
    "role": "end_user",
    "tierId": null,
    "expiresAt": "2026-10-26T08:00:01.122Z",
    "expiresIn": 28800
  }
}
```

`endOrgId` is fastn's own id for the customer; you can ignore it. The token is for the customer you created it for.

`expiresIn` is in seconds: the token lasts eight hours. Treat the token as a credential. How the browser side uses it is in [Embedding the widget](../../embed/embedding/README.md) and [Token API](../../embed/embedding/token-api.md).

---

## Connections

When the customer connects an app, fastn stores a connection on that customer. You receive its id on the `connection.connected` [event](events.md), and you can list connections at any time.

```typescript
const list = await customer.connections();

for (const c of list.data ?? []) {
  console.log(c.id, c.name, c.connector?.slug, c.status);
}

const hubspot = (list.data ?? []).find((c: any) => c.connector?.slug === "hubspot");
const connectionId = hubspot?.id;
```

### A connection

```json
{
  "data": [
    {
      "id": "ucl:your-org:7c9e6679-…:3fa85f64-…:default",
      "name": "Front desk CRM",
      "connectorId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "connector": { "name": "HubSpot", "slug": "hubspot", "domain": "hubspot.com", "protocol": "REST" },
      "authType": "OAUTH",
      "authMethod": { "type": "OAUTH", "title": "OAUTH" },
      "status": "ACTIVE",
      "isDefault": true,
      "orgId": "your-org-id",
      "endOrgId": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "endOrgName": "Acme Dental",
      "tokenExpiresAt": "2026-10-26T00:21:06.000Z",
      "createdAt": "2026-10-18T06:26:08.000Z",
      "updatedAt": "2026-10-18T06:26:08.000Z"
    }
  ],
  "pagination": { "total": 1, "limit": 1, "offset": 0 }
}
```

| Field | Meaning |
| ----- | ------- |
| `id` | The `connectionId`. Pass it to [unified records](unified-records.md#pick-one-account-connectionid) when a customer has more than one account for the same app. |
| `name` | The connection's name, for example the `connectionName` from the setup link. |
| `connector.slug` | The app, for example `hubspot`. Use it as `provider` in unified calls and as `connector` in [direct actions](app-actions.md). |
| `connectorId` | The app's id in the catalogue. |
| `status` | For example `ACTIVE` or `EXPIRED`. An expired connection needs the customer to sign in again. |
| `isDefault` | The account used when you do not pick one. |
| `endOrgId` | fastn's own id for the customer the connection belongs to; you can ignore it. |

### Other connection calls

| Do this | SDK | Input |
| ------- | --- | ----- |
| List a customer's connections | `customer.connections()` | Optional: `includePartnerPool: "true"` adds your own org's shared connections that the customer can also use. |
| Read one | `fastn.connections.getConnection({ id })` | `id` (required): the `connectionId`. Answer: `{ data: connection }`. Credentials are not returned. |
| Rename | `customer.renameAccount(connectionId, name)` | The connection must belong to this customer (`404 CONNECTION_NOT_FOUND` otherwise), so one key serving every customer can never touch another customer's account by mistake. |
| Disconnect | `customer.disconnect(connectionId)` | Same check. The account is removed; stop using its `connectionId`. |

{% hint style="info" %}
A unified call for a customer can also use connections in **your own** org's shared pool. So `providers()` (see [Unified records](unified-records.md#which-apps-a-customer-can-use)) can show an app as connected even when `customer.connections()` does not list it. Use `customer.connections({ includePartnerPool: "true" })` to see both.
{% endhint %}

See also [Connections](../../build/connections/README.md) for connection statuses in the dashboard.
