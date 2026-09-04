---
description: >-
  A single dense page for LLMs and coding agents: the model, the runtime surface,
  the endpoints, and the things that are easy to get wrong.
---

# fastn for AI agents

This page exists for AI agents and other machine readers. It is deliberately terse and factual: no narrative, no screenshots, every exact string spelled out. Human readers are better served by [Core concepts](../getting-started/concepts.md).

If you are an agent writing fastn workflows or calling the fastn API, read this page first, then confirm anything marked **Verify** against the live surfaces named at the bottom.

---

## The model in six lines

1. An **organisation** is you, the SaaS company. It holds everything below.
2. A **connector** defines an external system — its actions, auth methods and versions.
3. A **connection** is *one of your customers'* authorised link to one connector, holding the encrypted credential.
4. A **workflow** is JavaScript that runs on a trigger. It is code, not a drag-and-drop graph.
5. A **trigger** starts a workflow: webhook, schedule, or app event.
6. A **widget** is the integrations panel your customers see, embedded in your product.

fastn is multi-tenant throughout. One workflow serves every customer; headers on the request decide which customer a run acts for.

---

## Workflow anatomy

A workflow is an async function receiving a context object.

```javascript
export default async function (ctx) {
  const { recordId } = ctx.input;
  const record = await fastn.connector.hubspot.getContact({ recordId });
  return { ok: true, id: record.id };
}
```

* The file is `<slug>.js`. The export is default and async.
* The **Diagram** tab is generated *from* this code and is read-only. There is no visual editor to keep in sync.
* The editor autosaves. There is no Save button.
* Whatever you return must match the workflow's declared output contract.
* Throwing marks the execution **Failed**, and retries only where a retry policy is enabled.

{% hint style="warning" %}
**Do not generate TypeScript.** Workflows are JavaScript.
{% endhint %}

### `ctx`

| Property | Contains |
| -------- | -------- |
| `ctx.input` | The incoming payload. Webhook → request body. Schedule → the route's **Payload** JSON. App event → the connector's event payload. Manual/API → the `input` object from the request body. |
| `ctx.headers` | HTTP headers from the incoming request, including the multi-tenant headers below. |
| `ctx.connectors` | The connectors bound to this workflow — the same set listed on its **Connectors** tab. |

### Runtime surface

| Call | Purpose |
| ---- | ------- |
| `fastn.connector.<slug>.<action>(args)` | Call an action on a connected system. **Verify** — see the naming caveat below. |
| `fastn.unified.…` | Call a unified entity and let fastn route to whichever provider the customer connected. |
| `fastn.db.query(sql, params)` | SQL against your workspace's Postgres schema (`ws_<hash>`). **Verify** signature. |
| `fastn.state.get(key)` / `fastn.state.set(key, value)` | Durable key-value across runs. Scopes: `ORG`, `INVOCATION`. |
| `fastn.secrets.get("NAME")` | Read an encrypted secret. Name is UPPER_SNAKE_CASE, exactly as created. JSON-typed secrets return already parsed. |
| `fastn.envConfig.get("KEY")` | Read a per-environment config value. |
| `fastn.diff.compare(…)` | Produce a sync report. A workflow that does not call this produces no report. |

### Execution tiers

| Tier | Caller gets | Ceiling |
| ---- | ----------- | ------- |
| **Instant** | Return value inline, synchronously | 30 seconds |
| **Standard** | `202` + execution id | 15 minutes |
| **Long** | `202` + execution id | 36 hours |

Instant is the default. Anything calling two or three systems in sequence belongs on Standard.

---

## Multi-tenant headers

Sent on the request; readable at `ctx.headers`.

| Header | Carries |
| ------ | ------- |
| `x-end-org-id` | The customer the run acts for |
| `x-end-org-ref` | Your own reference for that customer |
| `x-installation-id` | Which installation of the integration this run belongs to |
| `x-fastn-connections` | The connections the run may use |
| `x-fastn-installation-config` | The configuration values that installation was set up with |

---

## HTTP API

Base URL is your deployment — production is `https://live.gcp.fastn.ai`. Each workflow's **API** tab shows the correct host for your workspace. Examples below use `YOUR_FASTN_HOST`.

### Auth

```
Authorization: Bearer fsk_live_<key>
```

| Header | Live key | Test key |
| ------ | -------- | -------- |
| `Authorization` | `Bearer fsk_live_…` | `Bearer fsk_test_…` |
| `X-fastn-Test-Mode` | Not needed | **Must be `true`** — a test key is refused without it |
| `x-fastn-env` | Environment slug | Environment slug |

`x-fastn-env: test` runs the latest published version; any other slug runs the version deployed to that environment.

{% hint style="danger" %}
A test key is **not** a sandbox. It reaches the same live connections as a live key and causes the same real writes. Never present test mode to a user as safe.
{% endhint %}

### Endpoints

```http
POST /api/v1/workflows/{workflowId}/execute

GET  /api/v1/unified/{category}/{entity}?page_size=50
GET  /api/v1/unified/{category}/{entity}/{recordId}
POST /api/v1/unified/{category}/{entity}

POST /api/v1/embed/token
POST /api/v1/embed/token/refresh
GET  /api/v1/embed/iframe?token=emb_…
```

Workflow ids look like `wf_b5880b29eb25`; execution ids like `exec_…`; embed tokens like `emb_…`.

Execute request body — the `input` object becomes `ctx.input`:

```json
{ "input": { "key": "value" } }
```

### Unified API categories

Five on the live platform: `CRM`, `Documents`, `Knowledge Base`, `Messaging`, `Project Management`.

CRM exposes ten entities across twelve providers: `Account`, `Contact`, `Engagement`, `Engagement Type`, `Lead`, `Note`, `Opportunity`, `Stage`, `Task`, `User`. Note and message entities are create-only.

### Errors

| Response | Means |
| -------- | ----- |
| `WORKFLOW_NOT_PUBLISHED` | No snapshot has ever been published. **Every call returns this until one is.** The single most common cause of "the API did nothing". |
| `401` / `403` | Key wrong, revoked, expired, outside its IP allowlist, or lacking the permission. |
| Test key rejected | `X-fastn-Test-Mode: true` was not sent with a test key. |

A workflow that runs and throws is a **Failed execution**, not a transport error. Look in Executions, not the HTTP response.

There is **no documented endpoint for polling an execution id**. For Standard and Long runs, have the workflow call back rather than assuming you can poll.

---

## Triggers

| Type | Starts a run when | Key settings |
| ---- | ----------------- | ------------ |
| **Webhook** | An HTTP request arrives at a public URL | Auth (`x-fastn-access-key` or public), routes, execution mode (Parallel/Sequential), deduplication key |
| **Schedule** | A time is reached | Cron/interval, plus a **Payload** JSON that becomes `ctx.input` |
| **App event** | Something changes in a connected system | Connector (**immutable after creation**), connection, event, routes |

An app event trigger cannot be created without an active connection for that connector.

---

## Two different MCP surfaces

Do not conflate these.

| | Docs MCP | Product MCP gateway |
| --- | --- | --- |
| **URL** | `<docs-site>/~gitbook/mcp` | `https://mcp.fastn.dev` |
| **Exposes** | This documentation, as searchable tools | Your connectors and actions, as callable tools |
| **Auth** | Public, as the docs site is | `Authorization: Bearer fsk_live_<key>` |
| **Use for** | Answering questions about fastn | Acting on real customer systems |

Claude Code, against the product gateway:

```
claude mcp add --transport http fastn https://mcp.fastn.dev
```

A gateway client acts with exactly what its key permits — customer scope, permission preset, and the actions selected on the connector. Mint a dedicated key per client and name it after the client; the name appears in the audit log beside everything the key does.

---

## Things agents get wrong

Read this section before generating code.

* **`fastn.connector` vs `fastn.connectors`.** The product is inconsistent. The workflow **Docs** tab documents the singular; the **Connectors** tab describes extracting bound connectors from `fastn.connectors.X.Y(…)` calls on save. Check the Docs tab in the target workspace, and confirm saving actually picks the calls up. **Verify.**
* **`fastn.state` `ORG` scope is not pinned down.** Whether `ORG` is org-wide across all workflows or partitioned per workflow is not settled. Namespace keys by workflow (`myworkflow:deal:123`) so it does not matter. **Verify.**
* **`fastn.db` isolates by workspace, not by customer.** Every customer's rows share one schema. Nothing scopes a query for you — add a customer column and a predicate on every query, or you will leak across tenants.
* **Always parameterise SQL.** Interpolating `ctx.input` into a query string is an injection.
* **Publishing is not optional.** Code that is saved but not published does not run over the API.
* **Instant's 30 seconds is a hard ceiling**, and finding out by timing out in production is expensive.
* **Embed refresh caps at seven days per session.** At the cap the widget posts `fastn:session-expired` to the parent window and stops. Listen for it and mint a fresh token.
* **Connector credentials are not secrets.** They live on connections and are managed by fastn, including OAuth refresh. `fastn.secrets` is for third-party tokens and keys you hold yourself.
* **Settings is role-scoped.** What a user can see under Settings depends on their role, so do not assume a screen exists for the current user.

---

## Authoritative surfaces

Generated from the deployment you are actually calling, and therefore more trustworthy than any document — this one included:

| Surface | Gives you |
| ------- | --------- |
| Workflow → **Docs** tab | Exact runtime call shapes and header value formats for your deployment |
| Workflow → **Contract** tab | The real input and output shapes |
| Workflow → **API** tab | A ready-to-run curl with your host, workflow id and contract fields |
| Workflow → **Connectors** tab | Which connectors and action versions are actually bound, and per-customer vs workspace scope |
| Connector detail page | The action list, and the **Select all** control that scopes them |

When this page and a generated tab disagree, the tab is right.

---

## Machine-readable formats

This documentation is published from GitBook, which serves it in agent-friendly formats without configuration:

| Path | Contains |
| ---- | -------- |
| `/llms.txt` | A curated index of the documentation |
| `/llms-full.txt` | The entire documentation as one markdown file |
| `<any page URL>.md` | That page as raw markdown |
| `/~gitbook/mcp` | The documentation as an MCP server |

Prefer `llms-full.txt` for a single bulk load, the MCP server for interactive lookup.
