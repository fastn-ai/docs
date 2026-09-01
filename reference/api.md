---
description: Calling workflows and unified endpoints over HTTP.
---

# HTTP API

<figure><img src="../.gitbook/assets/workflow-api-tab.jpg" alt="A workflow's API tab"><figcaption>Every workflow's API tab shows its own endpoint and a copyable curl.</figcaption></figure>

### Base URL

The base URL is the deployment you are on — for example `https://dev.gcp.fastn.ai` on the development platform. Your workflow's **API** tab always shows the correct one for your workspace; the examples below use `YOUR_FASTN_HOST`.

---

## Authentication

Every request carries an API key as a bearer token.

```
Authorization: Bearer fsk_live_<your-key>
```

Keys are created under [Settings → API keys](../manage/api-keys.md) and come in two modes.

| Header                   | Live key                    | Test key                              |
| ------------------------ | --------------------------- | ------------------------------------- |
| `Authorization`          | `Bearer fsk_live_…`         | `Bearer fsk_test_…`                   |
| `X-fastn-Test-Mode`      | Must be **absent**          | Must be `true`                        |
| `x-fastn-env`            | Any environment slug        | May only ever be `test`               |

`x-fastn-env` picks which code runs:

* `test` — the workflow's latest published version.
* any other slug — the version deployed to that environment.

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
Every workflow's **API** tab generates a ready-to-run curl filled in with that workflow's own host, id and contract fields. When the two differ, copy from there — it is generated from the deployment you are actually calling.
{% endhint %}

### Response — Instant tier

```json
{
  "data": {
    "executionId": "exec_…",
    "status": "completed",
    "result": { },
    "logs": [ ],
    "durationMs": 42
  }
}
```

### Response — Standard and Long tiers

`202 Accepted` with an execution id. Poll it, or have the workflow call you back.

---

## Unified endpoints

Where a [unified API](../build/unified-apis.md) covers an entity, call it directly rather than a specific connector.

```http
GET  /api/v1/unified/crm/account?page_size=50
GET  /api/v1/unified/crm/account/{recordId}
POST /api/v1/unified/crm/account
POST /api/v1/unified/crm/note
```

fastn routes to whichever provider the customer authorised. Each endpoint on the Unified APIs page has a **Copy curl** button with the correct headers filled in.

---

## Webhook endpoints

A [webhook trigger](../build/triggers.md) gives you a public URL. Whether callers must authenticate is set on the trigger:

| Authentication setting            | Caller must send                      |
| --------------------------------- | --------------------------------------- |
| **API Key (x-fastn-access-key)**  | `x-fastn-access-key: <your-key>`      |
| **None (public)**                 | Nothing                               |

---

## Embed tokens

Short-lived tokens that scope the widget to one customer. Mint them from your backend with your API key; never expose the API key to a browser. See [Embedding the widget](../embed/embedding.md).

---

## Rate limits

Per-day and per-minute ceilings on API calls and events are set by your plan and, per customer, by their tier. Current usage is on [Settings → Billing](../manage/billing.md). Going over stops new work rather than charging you, and nothing already running is interrupted.
