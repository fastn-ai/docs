---
description: Minting and refreshing embed tokens from your backend, and the session cap.
---

# Tokens

An embed token identifies one of your customers to the widget. The dashboard shows a live 8-hour token so you can try things immediately. Mint your own from your backend for production.

### The Token API

```http
POST /api/v1/embed/token
Authorization: Bearer <API key>
x-org-id: <customer id or your external reference>
Content-Type: application/json
```

`x-org-id` names one of your customers: your own id for it (the `orgId` you sent to `POST /api/v1/orgs`), or fastn's id for it. A value that is not one of your customers returns `404 IDENTITY_ORG_NOT_FOUND`. Your own organization's id names no customer, so the mint is refused with `400 EMBED_TOKEN_REQUIRES_END_ORG_ID`. If you created a customer without one, fastn stored its slug as the external reference at creation time.

```json
{
  "userId": "user_123",
  "userEmail": "ana@acme.com",
  "userName": "Ana"
}
```

The response is wrapped in `data`:

```json
{
  "data": {
    "token": "emb_…",
    "userId": "user_123",
    "role": "end_user",
    "tierId": null,
    "expiresAt": "2026-11-04T18:00:00.000Z",
    "expiresIn": 28800,
    "orgId": "acme_customer_42"
  }
}
```

Read the token as `response.data.token`. `expiresIn` is 28800 seconds: eight hours. `orgId` is the customer, under your own id for it.

#### Signed headers or not: your key decides

Your API key's **Verify caller identity (HMAC)** setting (see [API keys](../../manage/api-keys.md)) decides how you name the customer:

| Your API key | Name the customer with |
| --- | --- |
| Set to **Enforce** | Signed headers: `x-org-id`, `x-user-id` and `x-identity-hmac`. The body can be empty. A request without identity headers is `401 IDENTITY_HEADERS_REQUIRED`, even when the body names the customer, and a missing or wrong hash is `401 IDENTITY_HMAC_INVALID` |
| Set to **Monitor only** | Either way. A missing or wrong hash is logged and the call goes through |
| No identity verification | `x-org-id` with no hash, as above, or `orgId` in the body |

With a key set to Enforce:

```http
POST /api/v1/embed/token
Authorization: Bearer <API key>
x-org-id: <your id for the customer>
x-user-id: <your id for the user>
x-identity-hmac: <hex HMAC-SHA256 of "<x-org-id>\n<x-user-id>", signed with the key's identity secret>
```

A key limited to a single customer already acts as that customer, and cannot have identity verification turned on. Name the customer with `orgId` in the body, set to fastn's id for it (see [Find your org identifier](../../tutorials/developer/finding-your-org-identifier.md)): with such a key your own id for the customer is `404 Tenant not found`.

#### Body fields

All fields are optional; the customer must come from the header or the body.

| Field | What it does |
| --- | --- |
| `orgId` | The customer: your own id for it, or fastn's id for it. Use it instead of the header on a key without enforced identity verification. If you also send `x-org-id`, the two must name the same customer, or the call fails with `400 IDENTITY_ORG_MISMATCH` |
| `userId` | The person at your customer. Per-user isolation keys on this id (or on an attested `x-user-id`). Without it, each token gets a random `embed_usr…` id, so nothing carries over between sessions |
| `userEmail`, `userName` | Display only |
| `createIfMissing` | Register the customer named by `orgId` if it does not exist yet, then mint for it. Needs the `customers.create` permission. Leave out `x-org-id` for a customer that doesn't exist yet (it is refused with `404` first). With a key set to Enforce, send `x-user-id` and sign an empty org id, as in [Register with an enforcing key](integration-flow.md#register-with-an-enforcing-key) |
| `customerName` | Display name for a customer created by `createIfMissing`. Defaults to the id |
| `roleOverride` | Per-user role override that your backend decides |
| `metadata` | Your own data, handed back in the widget's lifecycle callbacks for this session. At most 4 KB of JSON |
| `allowOrgLevel` | Mint an organization-level token with no customer. Only for previewing your own organization; never hand one to a customer |

If there is no customer in the header or the body, and `allowOrgLevel` is not set, the call fails with `400` and code `EMBED_TOKEN_REQUIRES_END_ORG_ID`. An embed token cannot mint another embed token (`403`): mint from your backend with an API key, and use the refresh endpoint below to extend a live session.

The hash code, a curl for each way and every error are in [Generate embed tokens](../../tutorials/developer/generating-embed-tokens.md). Your API key never reaches the browser. See [API keys](../../manage/api-keys.md).

### Refresh, and the session cap

```http
POST /api/v1/embed/token/refresh
Content-Type: application/json

{ "token": "emb_…" }
```

The token in the body is the credential: no API key. The answer carries `data.token`, `data.role`, `data.expiresAt` and `data.expiresIn`, with no `userId` or `tierId`, and the token you sent stops working.

{% hint style="warning" %}
Refresh is capped at **seven days per session**. At the cap the widget posts `fastn:session-expired` to the parent window and stops. Long-lived sessions do not refresh indefinitely: listen for that message and start a new session by minting a fresh token.
{% endhint %}

The flow for production:

1. Your backend authenticates the user, as it already does.
2. It calls `POST /api/v1/embed/token` with your API key and the customer identifier.
3. It returns the token to your frontend.
4. The SDK mounts with that token and refreshes it, until the seven-day session cap.
