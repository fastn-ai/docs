---
description: Calling workflows and unified endpoints over HTTP.
---

# HTTP API

### Base URL

Production base URL: `https://api.fastn.dev`. Your workflow's **API** tab shows the URL for your workspace. Examples below use `YOUR_FASTN_HOST`.

From Node.js or TypeScript, the [SDK](sdk/README.md) (`@fastn-ai/sdk`) wraps the same API in typed methods. Every other endpoint, including installations, triggers and alerts, is in the [REST API reference](rest/README.md).

---

## Authentication

Every request carries an API key as a bearer token.

```
Authorization: Bearer fsk_live_<your-key>
```

Keys are created under [Embed → API keys and MCP](../manage/api-keys.md) and come in two modes.

| Header                   | Live key                    | Test key                              |
| ------------------------ | --------------------------- | ------------------------------------- |
| `Authorization`          | `Bearer fsk_live_…`         | `Bearer fsk_test_…`                   |
| `X-fastn-Test-Mode`      | Not needed                  | Must be `true`: **a test key is refused without it** |
| `x-fastn-env`            | Its pinned environment or `test` (see below) | Only `test`                  |

A test key without `X-fastn-Test-Mode: true` is rejected with `403`.

`x-fastn-env` picks which code runs:

* `test`: the workflow's latest published version.
* any other slug: the version deployed to that environment.

Which environments a key may name:

* **Test key:** only `test`. Any other slug is refused with `403` `ENV_NOT_PERMITTED`.
* **Live key pinned to an environment:** that environment or `test`; anything else is refused with `403` `ENV_NOT_PERMITTED`. Every new live key is pinned, to `live` when you do not pick an environment.
* **Live key made before keys were pinned:** any environment slug.

When `x-fastn-env` is omitted, a test key runs `test` and a live key runs `live` (a pinned live key runs its pinned environment).

{% hint style="danger" %}
A test key is not a sandbox. It reaches the same live connections as a live key and causes the same real writes.
{% endhint %}

---

## Execute a workflow

```
POST /api/v1/workflows/{workflowId}/execute
```

The workflow id is shown on the workflow's API tab, in the form `wf_b5880b29eb25`.

```bash
curl -X POST https://YOUR_FASTN_HOST/api/v1/workflows/WORKFLOW_ID/execute \
  -H "Authorization: Bearer fsk_test_<your-key>" \
  -H "X-fastn-Test-Mode: true" \
  -H "x-fastn-env: test" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "saleId": "S-1024",
      "isRetry": false,
      "syncMode": "incremental"
    }
  }'
```

### Request body

```json
{
  "input": {
    "key": "value"
  }
}
```

The `input` object is what arrives as `ctx.input`. Its shape comes from the workflow's input contract.

{% hint style="info" %}
Every workflow's **API** tab generates a ready-to-run curl filled in with that workflow's own host, id and contract fields. When the two differ, copy from there. It is generated from the deployment you are actually calling.
{% endhint %}

### Response: Instant tier

The workflow's return value comes back inline, synchronously, as a `200`. The run is cut off at 25 seconds (2 minutes for organizations with the "Increase Instant timeout" entitlement). The execution id is in the `X-Execution-Id` response header, because the body is the workflow's own return value. Its shape is the workflow's own **output contract**: read it on the Contract tab rather than from an example here, because it is different for every workflow.

### Response: Standard and Long tiers

`202 Accepted`, with the execution id in the body at `data.executionId`. The run continues in the background; the id is what identifies it afterwards in [Executions](../operate/executions.md), where each row expands to its input, output and per-step timings.

To get the outcome of a Standard or Long run, poll:

```
GET /api/v1/workflows/{workflowId}/executions/{executionId}
```

The workflow id is part of the path.

---

## Scoping a call to a customer

The same workflow serves all of your customers, and headers on the request are what say which one a call is for.

| Header                          | Carries                                                       |
| ------------------------------- | --------------------------------------------------------------- |
| `x-end-org-id`                  | The customer this call acts for.                               |
| `x-end-org-ref`                 | Your own reference for that customer.                          |
| `x-installation-id`             | Which installation of the integration the call belongs to.     |
| `x-fastn-connections`           | The connections the installation uses.                         |
| `x-fastn-installation-config`   | The configuration values that installation was set up with.    |

`x-fastn-connections` and `x-fastn-installation-config` are only read together with `x-installation-id`. On `/execute`, fastn reloads the named installation and overlays its stored connections and configuration on the headers, so callers name an installation; they cannot pick connections by sending them.

Inside the workflow these arrive on `ctx.headers`. See [Workflow runtime API](workflow-runtime.md). The workflow editor's autocomplete lists the exact shapes; check there before you hard-code one.

---

## Unified endpoints

Where a [unified API](../build/unified-apis/README.md) covers an entity, call it directly rather than a specific connector.

```http
GET  /api/v1/unified/crm/account?page_size=50
GET  /api/v1/unified/crm/account/{recordId}
POST /api/v1/unified/crm/account
POST /api/v1/unified/crm/note
```

fastn routes to whichever provider the customer authorized. Each endpoint on the Unified APIs page has a **Copy curl** button with the correct headers filled in.

---

## Webhook endpoints

A [webhook trigger](../build/triggers/README.md) gives you a public URL. Whether callers must authenticate is set on the trigger:

| Authentication setting            | Caller must send                      |
| --------------------------------- | --------------------------------------- |
| **API Key (x-api-key)**           | `x-api-key: <your-key>` (a fastn key, starting `fsk_`); `x-fastn-access-key: <your-key>` is still accepted |
| **None (public)**                 | Nothing                               |

---

## Embed tokens

Tokens that scope the widget to one customer. Mint them from your backend with your API key; never expose the API key to a browser.

### Mint a token

```
POST /api/v1/embed/token
```

| Header          | Value                    |
| --------------- | ------------------------ |
| `Authorization` | `Bearer <API key>`       |
| `x-org-id`      | The customer: fastn's id for it, or your own id for it |

`x-org-id` names the customer the token is for. Only an API key pinned to one customer leaves it out (a pinned key rejects the header) and sends `{"endOrgId": "…"}` in the body instead; a request with neither is refused with `400` `EMBED_TOKEN_REQUIRES_END_ORG_ID`.

```json
{
  "data": {
    "token": "emb_…",
    "endOrgId": "…",
    "userId": "…",
    "role": "end_user",
    "tierId": null,
    "expiresAt": "…",
    "expiresIn": 28800
  }
}
```

`expiresIn` is **28800 seconds: eight hours**. `endOrgId` is the customer the token is scoped to, and the returned role is always `end_user`.

### Refresh

```
POST /api/v1/embed/token/refresh
```

{% hint style="warning" %}
**Refresh is capped at seven days per session.** At the cap the widget posts `fastn:session-expired` to the parent window and stops: refreshing again does not extend it. Listen for that message and start a new session by minting a fresh token. A host app that assumes refresh is indefinite will strand long-lived sessions.
{% endhint %}

### Using the token

The iframe endpoint takes it on the query string:

```
https://YOUR_FASTN_HOST/api/v1/embed/iframe?token=emb_…
```

That URL carries a live credential. Treat it like one: build it server-side per session, and do not log or share it. Full setup in [Embedding the widget](../embed/embedding/README.md).

---

## Errors

| Response                  | Means                                                                          |
| ------------------------- | -------------------------------------------------------------------------------- |
| `WORKFLOW_NOT_PUBLISHED`  | The workflow has never had a snapshot published, so there is no version to run. **Every call returns this until you publish one**. It is the most common cause of "the API did nothing". Publish from the workflow editor. |
| `401` / `403`             | The key is wrong, revoked, expired, outside its IP allowlist, or lacks the permission for what you called. Check the key on [Embed → API keys and MCP](../manage/api-keys.md). |
| Test key rejected         | The key is a test key and `X-fastn-Test-Mode: true` was not sent.                |
| `ENV_NOT_PERMITTED` (`403`) | The key may not run the environment named in `x-fastn-env`. See [Authentication](#authentication). |

A workflow that runs and throws is a **Failed** execution rather than a transport error: look for it in [Executions](../operate/executions.md), not in the HTTP response.

---

## Rate limits

Two limits apply to API calls, both counted per minute:

| Limit | What it counts | Ceiling |
| ----- | -------------- | ------- |
| **Per organization** | Every call made with an API key or an embed session, across your whole account. Your customers' calls count toward your account. | 100 requests per minute on Launch, 500 on Scale, custom on Enterprise. |
| **Per caller** | Calls from one identity (one API key, one embed session, one signed-in person), held separately on each gateway instance. | A blunt cap on one caller hammering the API, separate from your plan. |

Two narrower limits can also apply: an API key can carry its own per-minute limit, and calls to `/execute` share one per-minute bucket per customer, so many embed sessions for one customer cannot run workflows without bound (code `EXECUTE_RATE_LIMITED`).

Going over any of these returns `429` with a `Retry-After` header. The organization limit answers with code `ORG_RATE_LIMITED`. Calls to the billing, plans, quota and usage endpoints never count toward the organization limit, so you can always see why you are limited. Your plan's limits are on [Settings → Billing](../manage/billing.md).
