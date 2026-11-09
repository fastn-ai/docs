---
description: >-
  What a workflow can reach at runtime: ctx, customer headers, connectors,
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

The headers also carry customer context. See [Customer headers](#customer-headers) below.

## Customer and run fields on ctx

The simplest way to know which of your customers a run is acting for is to read it straight off `ctx`:

| Field             | Holds                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------- |
| `ctx.endOrgId`    | fastn's id for the customer the run acts for, or `null` when the run is not for a customer. |
| `ctx.externalRef` | Your own id for that customer, when the caller named the customer by it; otherwise `null`. |
| `ctx.env`         | The environment the run executes in, for example `test` or `live`.                   |
| `ctx.attempt`     | The attempt number, starting at `1`.                                                  |
| `ctx.isRetry`     | `true` when this run is a retry (`ctx.attempt` is greater than `1`).                  |

```javascript
const customerId = ctx.endOrgId;
if (ctx.isRetry) {
  // pick up from a checkpoint instead of starting over
}
```

## Connectors are not on ctx

`ctx` carries only `input`, `headers`, `env`, `endOrgId`, `externalRef`, `attempt` and `isRetry`. There is no `ctx.connectors`: call connectors through the `fastn` global, as shown in [Calling a connector](#calling-a-connector). What a run can reach is what the workflow's **Connectors** tab lists, so that tab is the authoritative view.

---

## Customer headers

One workflow serves all of your customers, and these four headers on the incoming request are how a call says which customer it is for and what it may use. Getting them right is the difference between a workflow that serves one customer and one that serves all of them.

| Header                          | Carries                                                                 |
| ------------------------------- | ------------------------------------------------------------------------- |
| `x-org-id`                      | The customer the run acts for: your own id for it, or fastn's id for it. |
| `x-installation-id`             | Which installation of the integration this run belongs to.               |
| `x-fastn-connections`           | The connections the installation uses.                                   |
| `x-fastn-installation-config`   | The configuration values that installation was set up with.              |

`x-fastn-connections` and `x-fastn-installation-config` are only read together with `x-installation-id`. On a direct call to `/execute`, fastn reloads the named installation and overlays its stored connections and configuration on whatever the headers say, so a caller names an installation; it cannot pick connections by sending them.

Their exact shapes are listed in the workflow editor's autocomplete, which is generated from the runtime: check there before wiring them into a caller.

---

## Calling a connector

Calls actions on connected apps, by connector slug.

```javascript
const sale    = await fastn.connector.cin7core.getSale({ saleId });
const created = await fastn.connector.trackstar.createOrder({ ... });
```

{% hint style="warning" %}
**Use `fastn.connector.<slug>.<action>()`, singular.** The plural `fastn.connectors.<slug>.<action>()` fails at run time. Saving the workflow extracts bound connectors from both spellings, so seeing your calls picked up on the **Connectors** tab does not prove the spelling is right.
{% endhint %}

The slug is the one on the connector's Overview tab. Available actions and their versions are pinned on the workflow's **Connectors** tab, and each connector there is marked *per customer* or workspace, which decides whose credential the call uses.

---

## fastn.unified

Calls a [unified API](../build/unified-apis/README.md) (one canonical entity, served by whichever provider the running customer has connected), rather than naming a specific connector.

This is the runtime counterpart to the `GET|POST /api/v1/unified/{category}/{entity}` endpoints on the Unified APIs page. Use it wherever you would otherwise write a branch per CRM: the routing to hubspot, salesforce or zohoCrm is the platform's problem rather than your code's. The workflow editor's autocomplete shows the exact call shape.

---

## fastn.db

SQL against your workspace's Postgres schema.

Which schema a query runs in depends on how your organization's database is set up (see [Database](../manage/database.md)). Do not rely on the database to keep one customer's rows apart from another's: if a table holds data for several customers, add a customer column (for example `ctx.endOrgId`) and filter on it in every query.

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
The signature is `query(sql, params)` with `$1`-style placeholders; the workflow editor's autocomplete shows the full shape.
{% endhint %}

{% hint style="warning" %}
Always parameterize. String-interpolating a value from `ctx.input` into SQL is an injection waiting to happen.
{% endhint %}

---

## fastn.state

Durable key-value storage across runs, in one of two scopes.

| Scope          | Lifetime                                                        | Use for                                    |
| -------------- | ----------------------------------------------------------------- | -------------------------------------------- |
| **ORG** (the default) | Outlives a single run. Org-wide: one key space shared by every workflow in the workspace and every customer's runs. | Deduplication, synced-record IDs, caches. |
| **INVOCATION** | Bounded to one execution.                                        | Temporary state inside a long run.          |

{% hint style="warning" %}
**`ORG` keys are shared across workflows and customers.** A key like `deal:123` collides between two workflows that both process deals, and between two customers whose deals share an id. Namespace every key by workflow and, where the data belongs to one customer, by customer (for example with `ctx.endOrgId`).
{% endhint %}

```javascript
const key  = `myworkflow:${ctx.endOrgId}:deal:${dealId}`;
const seen = await fastn.state.get(key);
if (seen) {
  return { success: true, skipped: true, reason: "already_processed" };
}
await fastn.state.set(key, { processedAt: new Date().toISOString() });
```

That is the standard idempotency guard. Pair it with a [deduplication key](../build/triggers/README.md) on the trigger and a retried delivery is much less likely to double-write: verify the guard actually holds under a replay in your own workspace before treating it as a guarantee.

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
const base = await fastn.envConfig.get("UPSTREAM_API_BASE");
```

---

## fastn.diff.compare

Produces a [sync report](../operate/sync-reports.md): a record-by-record account of what a run changed. A workflow that calls it gets a report; one that does not, does not.

---

## Returning

Whatever you return becomes the workflow's output, and must match the output contract. The tier decides who waits for it:

| Tier         | The caller gets                                                        | Ceiling  |
| ------------ | ------------------------------------------------------------------------ | -------- |
| **Instant**  | The return value inline, synchronously.                                 | 25 seconds (2 minutes with the per-organization "Increase Instant timeout" entitlement) |
| **Standard** | `202` and an execution id.                                              | 15 minutes |
| **Long**     | `202` and an execution id.                                              | Up to 36 hours |

**Instant's ceiling is 25 seconds** unless your organization holds the "Increase Instant timeout" entitlement, which raises it to 2 minutes. It is short on purpose. It is the tier for something a caller is blocked on. Anything that reaches out to two or three apps in sequence belongs on Standard, and finding out by timing out in production is the expensive way to learn it.

## Errors

Throwing marks the execution **Failed**. A `throw` from your code is recorded as a user code error and never retries, whatever the retry policy says. Where the workflow's retry policy allows more than one attempt, only transient failures retry: for example a connector call that escapes your code still failing with a 429 or 5xx after the connector's own retries, or a transient database error. Out of memory, a result that is too large, and a cancelled run never retry.
