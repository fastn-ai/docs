---
description: Calling workflows and unified endpoints over HTTP.
---

# HTTP API

### Base URL

Production base URL: `https://api.fastn.dev`. Your workflow's **API** tab shows the URL for your workspace. Examples below use `YOUR_FASTN_HOST`.

From Node.js or TypeScript, the [SDK](sdk/README.md) (`@fastn-ai/sdk`) wraps the same API in typed methods. Every other endpoint, including installations, triggers and alerts, is in the [REST API reference](rest/README.md).

---

## Authentication

Every request carries an API key, as a bearer token or in `X-API-Key`:

```
Authorization: Bearer fsk_live_<your-key>
```

```
X-API-Key: fsk_live_<your-key>
```

These two are the only headers this API reads a key from. A webhook trigger URL takes them too, and also `x-fastn-access-key` (see [Webhook endpoints](#webhook-endpoints)). No endpoint reads `x-fastn-api-key`: a call that sends the key there is answered `401`.

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
| `x-org-id`                      | The customer this call acts for: your own id for it, or fastn's id for it. |
| `x-installation-id`             | Which installation of the integration the call belongs to.     |
| `x-fastn-connections`           | The connections the installation uses.                         |
| `x-fastn-installation-config`   | The configuration values that installation was set up with.    |

**Naming the customer:** `x-org-id` is the one header that names a customer. Send your own id for the customer (the `orgId` you gave it when you created it) or fastn's id for it. It must be one of your customers, or the call returns `404 IDENTITY_ORG_NOT_FOUND`. A partner backend can sign it: send `x-user-id` too, with `x-identity-hmac`. A key set to Enforce must send them on every call (`401 IDENTITY_HEADERS_REQUIRED`). On a key pinned to one customer, `x-org-id` naming any other customer is refused with `400 IDENTITY_HEADERS_CONFLICT`, and so is a request whose `x-org-id` and `?orgId=` name two different customers. On a key limited to some customers, a customer outside that list is refused with `403 API_KEY_SCOPE_MISMATCH`, and a key that covers several customers must name one in `x-org-id` (`400 API_KEY_SCOPE_AMBIGUOUS`). Leave `x-org-id` out to act as your own organization, although a key set to Enforce still needs a signed `x-user-id`.

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
| **API Key (x-api-key)**           | `x-api-key: <your-key>` (a fastn key, starting `fsk_`) or `Authorization: Bearer <your-key>`; `x-fastn-access-key: <your-key>` is still accepted |
| **None (public)**                 | Nothing                               |

`X-API-Key` and `Authorization: Bearer` count only when the value starts `fsk_`, the prefix every fastn key has, so a sender's own `x-api-key` or bearer token is not mistaken for one. A connector's webhook URL (with **Require API key** on) takes `x-api-key` or `x-fastn-access-key` only, not `Authorization`.

---

## Embed tokens

Tokens that scope the widget to one customer. Mint them from your backend with your API key; never expose the API key to a browser.

### Mint a token

```
POST /api/v1/embed/token
```

| Header            | Value                    |
| ----------------- | ------------------------ |
| `Authorization`   | `Bearer <API key>` (or `X-API-Key: <API key>`) |
| `x-org-id`        | The customer: fastn's id for it, or your own id for it |
| `x-user-id`       | Optional. Your id for the user |
| `x-identity-hmac` | Hex HMAC-SHA256 of `<x-org-id>\n<x-user-id>`, signed with the key's identity secret. Required when the key's **Verify caller identity** is set to Enforce |

`x-org-id` names the customer the token is for, and with these headers the body can be empty. A key set to Enforce must send the signed headers: a request without them is `401 IDENTITY_HEADERS_REQUIRED`, even when the body names the customer. A key without identity verification can send `{"orgId": "…"}` in the body instead, with the same value; if you send both, they must name the same customer (`400 IDENTITY_ORG_MISMATCH`). A request that names no customer is refused with `400` `EMBED_TOKEN_REQUIRES_END_ORG_ID`. A key limited to a single customer names it with `orgId` in the body, set to fastn's id for it: with such a key your own id for the customer is `404 Tenant not found`.

```json
{
  "data": {
    "token": "emb_…",
    "userId": "…",
    "role": "end_user",
    "tierId": null,
    "expiresAt": "…",
    "expiresIn": 28800,
    "orgId": "acme_customer_42"
  }
}
```

The token is `data.token`. `expiresIn` is **28800 seconds: eight hours**. `orgId` is the customer the token is scoped to, under your own id for it, and the returned role is always `end_user`.

Every body field and error: [Generate embed tokens](../tutorials/developer/generating-embed-tokens.md).

### Refresh

```
POST /api/v1/embed/token/refresh
```

The body is `{"token": "emb_…"}`, and no API key is sent: the token is the credential. The answer carries `data.token`, `data.role`, `data.expiresAt` and `data.expiresIn`, with no `userId` or `tierId`. `expiresIn` is the seconds the new token has left, below 28800 near the seven-day cap.

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
