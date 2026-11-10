---
---

# Generating Embed Tokens

Embed tokens are short-lived credentials that scope the fastn widget to a specific customer. They are generated from your backend using your API key and passed to the iframe.

This page is the full reference for the token request. [Embed the widget](../../getting-started/onboarding/embed-the-widget.md) and [Token API](../../embed/embedding/token-api.md) show the same request in short.

### The token endpoint

```
POST https://api.fastn.dev/api/v1/embed/token
```

**Headers:**

```
Authorization: Bearer <FASTN_API_KEY>     (or X-API-Key: <FASTN_API_KEY>)
Content-Type: application/json
X-fastn-Test-Mode: true                   (only for fsk_test_ keys; omit for fsk_live_)
```

The token is for one of your customers and, optionally, one person at that customer. Your API key's **Verify caller identity (HMAC)** setting (see [API keys](../../manage/api-keys.md)) decides how you name them:

| Your API key | Name the customer with | Body |
| ------------ | ---------------------- | ---- |
| Verify caller identity set to **Enforce** | Signed headers: `x-org-id`, `x-user-id` and `x-identity-hmac` | Empty, or the user fields |
| No identity verification | `x-org-id` with no hash, or `orgId` in the body | The user fields, plus `orgId` if you use it |

A key set to **Enforce** refuses a request without identity headers, even when the body names the customer (`401 IDENTITY_HEADERS_REQUIRED`), and a request whose hash is missing or wrong (`401 IDENTITY_HMAC_INVALID`). A key set to **Monitor only** takes either way, and logs a missing or wrong hash. A key with verification off trusts `x-org-id` and `x-user-id` as sent.

#### With identity verification: signed headers

| Header | Value |
| ------ | ----- |
| `x-org-id` | The customer: your own id for it (the `orgId` you sent to `POST /api/v1/orgs`), or fastn's id for it. It must be one of your customers: anything else is `404 IDENTITY_ORG_NOT_FOUND`, and your own organization's id names no customer (`400 EMBED_TOKEN_REQUIRES_END_ORG_ID`). |
| `x-user-id` | Optional. Your id for the person using the widget. |
| `x-identity-hmac` | The hex HMAC-SHA256 of `<x-org-id>`, a newline and `<x-user-id>`, signed with the key's identity secret. Use an empty string for a header you leave out. |

Compute the hash on your backend. The identity secret is shown once, when you create the key, and must never reach a browser.

```javascript
const crypto = require("crypto");

function identityHash(orgId = "", userId = "") {
  return crypto.createHmac("sha256", process.env.FASTN_IDENTITY_SECRET)
    .update(`${orgId}\n${userId}`)
    .digest("hex");
}
```

The same request with curl:

```bash
ORG_ID="northwind"    # your id for the customer
USER_ID="user_42"     # your id for the person
HMAC=$(printf '%s\n%s' "$ORG_ID" "$USER_ID" | openssl dgst -sha256 -hmac "$FASTN_IDENTITY_SECRET" -hex | sed 's/^.* //')

curl -X POST https://api.fastn.dev/api/v1/embed/token \
  -H "Authorization: Bearer $FASTN_API_KEY" \
  -H "Content-Type: application/json" \
  -H "x-org-id: $ORG_ID" \
  -H "x-user-id: $USER_ID" \
  -H "x-identity-hmac: $HMAC" \
  -d '{}'
```

The body can stay empty. If it also names `orgId` or `userId`, they must match the headers, or the call is refused with `400 IDENTITY_ORG_MISMATCH` or `400 IDENTITY_USER_MISMATCH`. The other body fields below still apply.

Register each customer before you mint for them (`POST /api/v1/orgs`): an `x-org-id` that names no customer is refused before the token request runs, so `createIfMissing` does not apply to it. To use `createIfMissing` with a key set to Enforce, leave out `x-org-id`, send `x-user-id`, sign an empty org id (`"\n" + userId`) and name the customer with `orgId` in the body, as in [Register with an enforcing key](../../embed/embedding/integration-flow.md#register-with-an-enforcing-key).

#### Without identity verification

Send `x-org-id` as above with no hash, or name the customer in the body:

```bash
curl -X POST https://api.fastn.dev/api/v1/embed/token \
  -H "Authorization: Bearer $FASTN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "orgId": "northwind",
    "userId": "user_42",
    "userEmail": "jane@example.com",
    "userName": "Jane Doe"
  }'
```

**Body:**

| Field             | Description |
| ----------------- | ----------- |
| `orgId`           | The customer the widget is for: your own id for it, or fastn's id for it. Required unless `x-org-id` names the customer or `allowOrgLevel` is `true`; without either, the call is `400 EMBED_TOKEN_REQUIRES_END_ORG_ID`. A value that matches none of your customers is `404 Tenant not found`, and another account's customer is `403`. See [Finding Your Org Identifier](finding-your-org-identifier.md). |
| `userId`          | Optional. Your id for the person using the widget. Per-user isolation keys on this (or on an attested `x-user-id`). Left out, each token gets a random `embed_usr…` id, so nothing carries over between sessions (see [Tenancy](understanding-tenancy.md)). |
| `userEmail`       | Optional. The person's email address. Display only. |
| `userName`        | Optional. The person's display name, up to 200 characters. Display only. |
| `createIfMissing` | Optional. `true` registers the customer named by `orgId` if your account does not have it yet, then mints the token. The value becomes the new customer's own id (its External ID), which the answer returns as `data.orgId`; fastn assigns its own id as well. The key needs the `customers.create` permission. |
| `customerName`    | Optional, with `createIfMissing`. The new customer's display name. Defaults to `orgId`. |
| `metadata`        | Optional. A JSON object of your own, at most 4 KB, handed back to you in the widget's lifecycle hooks for this session. |
| `roleOverride`    | Optional, for a customer on a tier. The role whose permissions this token carries, in place of the tier's role. It can narrow what the session may do, never widen it beyond `end_user`. |
| `allowOrgLevel`   | Optional. `true`, with no customer named, mints a token for your own organization instead of a customer, to preview the widget yourself. Never hand one to a customer. |

A key limited to a single customer already acts as that customer, and cannot have identity verification turned on. Name the customer with `orgId` in the body, set to fastn's id for it: with such a key your own id for the customer is `404 Tenant not found`. An `x-org-id` that names any other customer is refused: `403 API_KEY_SCOPE_MISMATCH`, or `400 IDENTITY_HEADERS_CONFLICT` on a key pinned to that customer. Such a key cannot set `metadata` (`403 EMBED_PARTNER_ONLY_FIELD`). A key limited to several customers must name one in `x-org-id` (`400 API_KEY_SCOPE_AMBIGUOUS` otherwise), not in the body.

**Response:**

```json
{
  "data": {
    "token": "emb_...",
    "userId": "user_42",
    "role": "end_user",
    "tierId": null,
    "expiresAt": "2026-11-04T18:00:00.000Z",
    "expiresIn": 28800,
    "orgId": "northwind"
  }
}
```

The token is nested under `data`: read `response.data.token`, not `response.token`. It is prefixed `emb_`. `orgId` is the customer, under your own id for it, even when you named it by fastn's id.

`expiresIn` is `28800` seconds: eight hours.

**Errors:**

| Response | Cause |
| -------- | ----- |
| `400 EMBED_TOKEN_REQUIRES_END_ORG_ID` | No customer named: no `x-org-id` header and no `orgId` in the body, or `x-org-id` names your own organization. |
| `400 IDENTITY_ORG_MISMATCH`, `400 IDENTITY_USER_MISMATCH` | The body names a different customer or user than the headers. |
| `400 IDENTITY_HEADERS_CONFLICT` | Your key is pinned to a single customer, and `x-org-id` names a different one. |
| `400 API_KEY_SCOPE_AMBIGUOUS` | Your key is limited to several customers, and no `x-org-id` names one. |
| `401 IDENTITY_HEADERS_REQUIRED` | The key is set to Enforce and the request has no identity headers. |
| `401 IDENTITY_HMAC_INVALID` | The key is set to Enforce and `x-identity-hmac` is missing or does not match. |
| `403 API_KEY_SCOPE_MISMATCH` | Your key is limited to some customers, and `x-org-id` names one outside that list. |
| `404 IDENTITY_ORG_NOT_FOUND` | `x-org-id` is not one of your customers. |
| `404 Tenant not found` | `orgId` matches none of your customers. |
| `403 TENANT_NOT_ACTIVE` | The customer, or your account, is suspended. |
| `403 EMBED_PARTNER_ONLY_FIELD` | `metadata` was sent with a key limited to a single customer. |
| `403 quota_exceeded` | With `createIfMissing`: your account is at its customer limit. The body's `dimension` is `tenants_per_saas`, and `message` says how to clear it. Retrying does not help. |
| `409 TENANT_SLUG_TAKEN` | With `createIfMissing`: the slug derived from `customerName` (or `orgId`) for the new customer is taken. Retry with a different `customerName`. |
| `403` | The request was made with an embed token. An embed token cannot mint another one: mint from your backend, and extend a live session with the refresh endpoint below. |

### Refreshing tokens

A session outlives its first token through the refresh endpoint:

```
POST https://api.fastn.dev/api/v1/embed/token/refresh
Content-Type: application/json

{ "token": "emb_..." }
```

The token in the body is the credential, so no API key is sent. The answer carries fewer fields than a mint: `data.token`, `data.role`, `data.expiresAt` and `data.expiresIn`, with no `userId` or `tierId`. `expiresIn` counts the seconds the new token has left, so it is below 28800 near the seven-day cap. The token you sent is retired: carry on with the new one. A token that expired less than 24 hours ago can still be refreshed. The widget calls this endpoint itself to keep its session going.

Sending a retired token again later is treated as a stolen token: the whole session is revoked (`401 EMBED_TOKEN_REUSED`).

{% hint style="warning" %}
A session cannot be refreshed past **seven days** from its first token. After that the endpoint answers `401 EMBED_SESSION_EXPIRED`: mint a new token from your backend. At the cap the widget posts `fastn:session-expired` to the parent window; listen for it. See [Token API](../../embed/embedding/token-api.md).
{% endhint %}

### Token lifecycle

**Tokens expire after 8 hours.** Generate a fresh token on each page load. Do not generate one and reuse it across sessions or store it for later.

**Generate tokens server-side.** The token is minted from your API key, and your API key must never appear in client-side code. The token request has to happen on your backend.

**Never hardcode a token.** A token pasted into frontend code works until it expires, then the iframe renders blank with no clear error. This is the most common embedding mistake. Always fetch a fresh token from your backend at render time.

### The recommended pattern

Put token generation in a server-side function that reads the API key and identity secret from environment variables, takes the signed-in person's customer and user id from your own session, and returns a fresh token per request:

```javascript
const crypto = require("crypto");

async function getFastnToken({ customerId, userId }) {
  const hmac = crypto.createHmac("sha256", process.env.FASTN_IDENTITY_SECRET)
    .update(`${customerId}\n${userId}`)
    .digest("hex");

  const res = await fetch("https://api.fastn.dev/api/v1/embed/token", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.FASTN_API_KEY}`,
      "Content-Type": "application/json",
      "x-org-id": customerId, // fastn id or your external reference
      "x-user-id": userId,
      "x-identity-hmac": hmac,
      // "X-fastn-Test-Mode": "true",   // only with a fsk_test_ key
    },
    body: "{}",
  });

  if (!res.ok) {
    throw new Error(`Token request failed: ${res.status}`);
  }

  const json = await res.json();
  return json.data.token;
}
```

With a key that has no identity verification, leave out `x-user-id` and `x-identity-hmac`, and send the user in the body instead: `JSON.stringify({ userId })`.

Expose this through an endpoint your frontend calls at render time. Return only the token, as `{ "token": "emb_..." }`, never the API key.

This pattern is what makes the embed reliable across different users and sessions. Hardcoding or caching tokens is what causes "works for me, fails for them" behavior.
