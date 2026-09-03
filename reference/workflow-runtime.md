---
description: >-
  What a workflow can reach at runtime — ctx, multi-tenant headers, connectors,
  unified APIs, database, state, secrets and configs.
---

# Workflow runtime API

Every workflow is an async function that receives a context object, does its work, and returns a result.

```javascript
export default async function (ctx) {
  // ...
  return { ok: true };
}
```

---

## ctx.input

The incoming payload. What it contains depends on what started the run.

| Trigger       | `ctx.input` holds                       |
| ------------- | ----------------------------------------- |
| **Webhook**   | The HTTP request body.                   |
| **Schedule**  | Whatever JSON you put in the route's **Payload** field. A schedule has no payload of its own, so this is how a scheduled run gets parameters. |
| **App event** | The event payload from the connector.    |
| **Manual / API** | The `input` object from the request body. |

The shape is declared on the workflow's **Contract** tab, which is also what fills the Test tab and the API examples.

```javascript
const { saleId, syncMode, connection_id } = ctx.input;
```

## ctx.headers

HTTP headers from the incoming request, for webhook-triggered workflows.

```javascript
const contentType = ctx.headers['content-type'];
```

`ctx.headers` is also how a run knows which of your customers it is acting for — see [Multi-tenant headers](#multi-tenant-headers) below.

## ctx.connectors

The connectors bound to this workflow, available on the context object alongside `ctx.input` and `ctx.headers`. What is bound is what the workflow's **Connectors** tab lists, so that tab is the authoritative view of what a run can reach.

---

## Multi-tenant headers

fastn is multi-tenant, and these five headers on the incoming request are how a call says which customer it is for and what it may use. Getting them right is the difference between a workflow that serves one customer and one that serves all of them.

| Header                          | Carries                                                                 |
| ------------------------------- | ------------------------------------------------------------------------- |
| `x-end-org-id`                  | The customer the run acts for.                                           |
| `x-end-org-ref`                 | Your own reference for that customer.                                    |
| `x-installation-id`             | Which installation of the integration this run belongs to.               |
| `x-fastn-connections`           | The connections the run may use.                                         |
| `x-fastn-installation-config`   | The configuration values that installation was set up with.              |

They are documented on every workflow's **Docs** tab, generated from the runtime you are actually calling — read exact shapes and value formats there before wiring them into a caller.

---

## Calling a connector

Calls actions on connected systems, by connector slug.

```javascript
const sale    = await fastn.connector.cin7core.getSale({ saleId });
const created = await fastn.connector.trackstar.createOrder({ ... });
```

{% hint style="warning" %}
**The product is inconsistent about the name here.** A workflow's **Docs** tab documents `fastn.connector` (singular), while the **Connectors** tab describes auto-extracting bound connectors from `fastn.connectors.X.Y(…)` calls (plural) when you save. Check your own workspace's Docs tab and confirm that saving picks up your calls on the Connectors tab — if the extraction misses them, you are on the wrong spelling.
{% endhint %}

The slug is the one on the connector's Overview tab. Available actions and their versions are pinned on the workflow's **Connectors** tab, and each connector there is marked *per customer* or workspace — which decides whose credential the call uses.

---

## fastn.unified

Calls a [unified API](../build/unified-apis/README.md) — one canonical entity, served by whichever provider the running customer has connected — rather than naming a specific connector.

This is the runtime counterpart to the `GET|POST /api/v1/unified/{category}/{entity}` endpoints on the Unified APIs page. Use it wherever you would otherwise write a branch per CRM: the routing to hubspot, salesforce or zohoCrm is the platform's problem rather than your code's. The exact call shape is on the workflow's **Docs** tab.

---

## fastn.db

SQL against your workspace's Postgres schema.

**The isolation unit is the workspace, not the customer.** Each workspace gets its own schema — named `ws_<hash>` — isolated from every other workspace. Rows written for one of *your* customers and rows written for another sit in that same schema together. Nothing scopes a query to a customer for you: if you need that separation, put a customer column on the table and a predicate on every query.

```javascript
await fastn.db.query(
  `INSERT INTO sync_log (customer_id, source_id) VALUES ($1, $2)`,
  [customerId, record.id]
);

const rows = await fastn.db.query(
  `SELECT * FROM sync_log WHERE customer_id = $1 AND source_id = $2`,
  [customerId, record.id]
);
```

Which Postgres this reaches is set under [Settings → Database](../manage/database.md).

{% hint style="info" %}
The exact signature above — `query(sql, params)` with `$1`-style placeholders — should be confirmed against your workflow's **Docs** tab, which is generated from the runtime you are calling.
{% endhint %}

{% hint style="warning" %}
Always parameterise. String-interpolating a value from `ctx.input` into SQL is an injection waiting to happen.
{% endhint %}

---

## fastn.state

Durable key-value storage across runs, in one of two scopes.

| Scope          | Lifetime                                                        | Use for                                    |
| -------------- | ----------------------------------------------------------------- | -------------------------------------------- |
| **ORG**        | Outlives a single run.                                           | Deduplication, synced-record IDs, caches.   |
| **INVOCATION** | Bounded to one run.                                              | Temporary state inside a long run.          |

{% hint style="warning" %}
**Confirm what `ORG` actually spans before you rely on it.** The two scope names are what the runtime documents; whether `ORG` means org-wide across every workflow, or is partitioned per workflow, is not settled here — and the difference matters. Org-wide, a key like `deal:123` collides between two workflows that both process deals. Check your workspace's **Docs** tab, or namespace your keys by workflow so it does not matter either way.
{% endhint %}

```javascript
const key  = `myworkflow:deal:${dealId}`;
const seen = await fastn.state.get(key);
if (seen) {
  return { success: true, skipped: true, reason: "already_processed" };
}
await fastn.state.set(key, { processedAt: new Date().toISOString() });
```

That is the standard idempotency guard. Pair it with a [deduplication key](../build/triggers/README.md) on the trigger and a retried delivery is much less likely to double-write — verify the guard actually holds under a replay in your own workspace before treating it as a guarantee.

---

## fastn.secrets

Reads encrypted values from [Settings → Secrets](../manage/secrets.md).

```javascript
const token = await fastn.secrets.get("SHOPIFY_API_TOKEN");
```

The string you pass is the secret's **Name** exactly, in UPPER\_SNAKE\_CASE. A secret of type JSON comes back already parsed.

## fastn.envConfig

Reads per-environment values from [Settings → Configs](../manage/configs.md).

```javascript
const base = await fastn.envConfig.get("PARTNER_API_BASE");
```

---

## fastn.diff.compare

Produces a [sync report](../operate/sync-reports.md) — a record-by-record account of what a run changed. A workflow that calls it gets a report; one that does not, does not.

---

## Returning

Whatever you return becomes the workflow's output, and must match the output contract. The tier decides who waits for it:

| Tier         | The caller gets                                                        | Ceiling  |
| ------------ | ------------------------------------------------------------------------ | -------- |
| **Instant**  | The return value inline, synchronously.                                 | 30 seconds |
| **Standard** | `202` and an execution id.                                              | 15 minutes |
| **Long**     | `202` and an execution id.                                              | 36 hours |

**Instant's ceiling is 30 seconds.** It is short on purpose — it is the tier for something a caller is blocked on. Anything that reaches out to two or three systems in sequence belongs on Standard, and finding out by timing out in production is the expensive way to learn it.

## Errors

Throwing marks the execution **Failed** and, where a retry policy is enabled, triggers a retry. Code errors, data errors and out-of-memory never retry — only transient failures do.
