---
description: What a workflow can reach at runtime — ctx, connectors, database, state, secrets and configs.
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
| **Schedule**  | Scheduler context and schedule metadata. |
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

{% hint style="info" %}
Auth headers are stripped before your code sees them. `Authorization` and `x-fastn-access-key` are not present in `ctx.headers`.
{% endhint %}

---

## fastn.connector

Calls actions on connected systems, by connector slug.

```javascript
const sale    = await fastn.connector.cin7core.getSale({ saleId });
const created = await fastn.connector.trackstar.createOrder({ ... });
```

The slug is the one on the connector's Overview tab. Available actions and their versions are pinned on the workflow's **Connectors** tab, and each connector there is marked *per customer* or workspace — which decides whose credential the call uses.

---

## fastn.db

Customer-scoped SQL. Each customer gets an isolated context, so a query cannot reach another customer's rows. Supports CREATE TABLE, SELECT, INSERT, UPDATE and DELETE with `$1`-style parameters.

```javascript
await fastn.db.query(
  `INSERT INTO sync_log (source_id) VALUES ($1)`,
  [record.id]
);

const rows = await fastn.db.query(
  `SELECT * FROM sync_log WHERE source_id = $1`,
  [record.id]
);
```

Which Postgres this reaches is set under [Settings → Database](../manage/database.md).

{% hint style="warning" %}
Always parameterise. String-interpolating a value from `ctx.input` into SQL is an injection waiting to happen.
{% endhint %}

---

## fastn.state

Durable key-value storage across runs.

| Scope             | Lifetime                                                       | Use for                                             |
| ----------------- | ---------------------------------------------------------------- | ----------------------------------------------------- |
| **ORG** (default) | Shared across all runs of this workflow in the organisation.   | Deduplication, synced-record IDs, caches.            |
| **INVOCATION**    | One run. Cleared when it finishes.                             | Temporary state inside a long run.                   |

An optional TTL expires entries automatically.

```javascript
const seen = await fastn.state.get(`deal:${dealId}`);
if (seen) {
  return { success: true, skipped: true, reason: "already_processed" };
}
await fastn.state.set(`deal:${dealId}`, { processedAt: new Date().toISOString() });
```

This is the standard idempotency guard. Pair it with a [deduplication key](../build/triggers.md) on the trigger and a retried delivery cannot double-write.

---

## fastn.secrets

Reads encrypted values from [Settings → Secrets](../manage/secrets.md).

```javascript
const token = await fastn.secrets.get("SHOPIFY_API_TOKEN");
```

Never logged, never in execution output, never in error messages.

## fastn.envConfig

Reads per-environment values from [Settings → Configs](../manage/secrets.md).

```javascript
const base = await fastn.envConfig.get("PARTNER_API_BASE");
```

---

## fastn.diff.compare

Produces a [sync report](../operate/sync-reports.md) — a record-by-record account of what a run created, updated, skipped or rejected. A workflow that calls it gets a report; one that does not, does not.

---

## Returning

Whatever you return becomes the workflow's output, and must match the output contract. On the **Instant** tier the caller receives it inline; on **Standard** and **Long** the caller gets a 202 and an execution id to poll.

## Errors

Throwing marks the execution **Failed** and, where a retry policy is enabled, triggers a retry. Code errors, data errors and out-of-memory never retry — only transient failures do.
