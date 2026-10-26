---
description: "Call the fastn platform from your backend with the fastn SDK: install, set up the client, and learn the ids."
---

# SDK

The fastn SDK is the fastn platform API as a library for your backend. The first version is for Node.js and TypeScript: `@fastn-ai/sdk`. You call normal typed methods, you get plain objects back, and failures come back as typed errors. The SDK also handles customer ids, retries and event signatures for you.

Use it from your **backend**. It needs your fastn API key, which must never reach a browser.

{% hint style="info" %}
This is not the widget SDK. `@fastn-ai/sdk` runs on your server and calls the fastn API. The browser package that shows the connect widget inside your app is `@fastn-ai/embed`: see [Embedding the widget: SDK](../../embed/embedding/sdk.md).
{% endhint %}

---

## Install

```bash
npm install @fastn-ai/sdk
```

| Item     | Value                                                                       |
| -------- | --------------------------------------------------------------------------- |
| Runtime  | Node.js 20 or newer. The SDK uses the built-in `fetch`.                     |
| Modules  | ESM and CommonJS. TypeScript types are included.                            |
| API key  | Create one on [Settings → API keys](../../manage/api-keys.md). Keep it in your secret store. |

---

## Create the client

Create one client when your app starts, and reuse it. It caches the lookups it makes, such as each customer's fastn id.

```typescript
import { FastnClient } from "@fastn-ai/sdk";

const fastn = new FastnClient({ apiKey: process.env.FASTN_API_KEY! });

// One object per customer, named by YOUR id for that customer
const customer = fastn.customer("acme_customer_42");
```

| Option      | Required | Meaning |
| ----------- | -------- | ------- |
| `apiKey`    | Yes      | Your fastn API key. The SDK sends it on every call. |
| `baseUrl`   | No       | The API address. Default `https://api.fastn.dev`. |
| `timeoutMs` | No       | Time limit per request, in milliseconds. Default 60000. |
| `retries`   | No       | How many times a safe call is retried (see [Errors, retries and options](errors-and-options.md)). Default 2. |
| `defaults`  | No       | [Request options](errors-and-options.md#request-options) applied to every call, for example `{ customer: { ref: "acme_customer_42" } }` to tie a whole client to one customer. |
| `onRequest` | No       | A function called after every HTTP attempt, for your logs. It gets the operation, method, URL, status, duration, attempt number and request id. It never gets the API key. |
| `tools`     | No       | Only for the optional [workspace tools](workspace-tools.md) route. |
| `fetch`, `userAgent` | No | Your own `fetch` implementation, and a custom user agent. |

### Check the key

```typescript
const me = await fastn.me();
console.log(me.role, me.org?.id);
```

`fastn.me()` answers who the key is: `actor` (`api_key`), `role`, `org` (`id`, `name`, `type`, `externalRef`), `parentOrg`, `environment`, `permissions` and `apiKey` (`mode`, `environment`). The answer is cached for the life of the client.

---

## Your customers and their ids

fastn is multi-tenant. You are the **partner**; each business you serve is a **customer** (fastn also calls it a tenant or end org). Each customer gets its own connections, records and events. See [Understanding tenancy](../../tutorials/developer/understanding-tenancy.md) for the model.

You name each customer with **your own id**, for example the id it has in your database. fastn also gives the same customer its own internal id. The SDK lets you use only yours: `fastn.customer("acme_customer_42")`. It looks up fastn's id when a call needs it, and caches it.

{% hint style="warning" %}
To act for your customers, the API key must be allowed to act for customers (a multi-tenant partner key).
{% endhint %}

### Every id you will see

| Id | Example | What it is | Who makes it |
| -- | ------- | ---------- | ------------ |
| Your customer id | `acme_customer_42` | Your own id for a customer. The API also calls it `orgId`, `externalRef`, `endOrgRef` and `tenantRef`: all the same value. | You |
| fastn customer id | `7c9e6679-…` (a UUID) | fastn's own id for the same customer. Called `id` in customer answers and `endOrgId` elsewhere. Get it with `await customer.id()`. | fastn |
| `widgetId` | `wgt_…` | A widget: which apps a setup link or the embedded widget offers. | You, in the dashboard |
| `setupId` | `stp_…` | One setup link. | fastn |
| `installationId` | `inst_…` | The finished setup made from a setup link or the widget. | fastn |
| `connectionId` | `ucl:…:default` | One connected account, for example one Google Calendar of one customer. | fastn, when the customer connects |
| `connectorId` | a UUID | One app (connector) in the catalogue. | fastn |
| Connector slug | `hubspot`, `googleCalendar` | The app's short name. Used as `provider` and `connector` in calls. | fastn |
| Action slug | `getContact` | One action of an app. | fastn |
| Record id | `51234567890` | A record (contact, meeting, deal) in the app itself. | The app |
| Subscription id | `esub_…` | One event subscription (your webhook). | fastn |
| Delivery id | `evd_…` | One delivery of one event to your webhook. | fastn |
| Event id | `evt_…` | One event. It stays the same across retries. | fastn |
| Webhook secret | `whsec_…` | Signs the events fastn sends you. Shown once. | fastn |
| `idempotencyKey` | `booking_123` | Your key that makes a write safe to retry. | You |
| `correlationId` | `req_abc` | Your id for a request, to trace what fastn did for it. | You |
| `requestId` | from the error | fastn's id of one failed request. Quote it when you ask for help. | fastn |

---

## What you get back

Answers are returned exactly as the REST API sends them.

| Kind of call | Answer |
| ------------ | ------ |
| Customers, links, connections, events | `{ data: { … } }` for one item, `{ data: [ … ] }` for a list. Some lists add `pagination` or `meta`. |
| One unified record (create, get, update) | `{ id, provider, data: { …fields } }`. `id` is the record's id in the app. |
| A list of unified records (list, search) | `{ records: [ { id, provider, data } ], nextCursor, hasMore, provider }` |
| A failure | A thrown `FastnApiError` or `FastnNetworkError`. See [Errors, retries and options](errors-and-options.md). |

Fields of unified records and their list options use `snake_case` (`start_time`, `page_size`). Everything else uses `camelCase` (`widgetId`, `connectionId`, `idempotencyKey`).

---

## The pages in this section

| Page | Covers |
| ---- | ------ |
| [Customers](customers.md) | Register, find, read, list, change and remove customers. |
| [Connecting apps](connecting-apps.md) | Widgets, setup links, redirect addresses, embed tokens, and the connections a customer made. |
| [Unified records](unified-records.md) | One set of methods for every app: create, get, list, search, update and delete records, and how to find the fields. |
| [Direct app actions](app-actions.md) | Run an app's own action when the unified API does not cover what you need. |
| [Events](events.md) | Receive signed events about connections, setup links and app changes. |
| [Errors, retries and options](errors-and-options.md) | Retry keys, tracing, time limits, and the errors to handle. |
| [Workspace tools](workspace-tools.md) | The optional route: run your workspace's MCP tools by name. |
| [Any other operation](any-operation.md) | Every other API operation, by name. |

The SDK has one method for every partner operation of the fastn API, under an area such as `fastn.orgs`, `fastn.embed`, `fastn.connections`, `fastn.unified`, `fastn.events` or `fastn.connectors`. Each method has the same name as the operation. For the plain HTTP calls, see [HTTP API](../api.md).
