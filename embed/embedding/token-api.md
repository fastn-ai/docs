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

`x-org-id` always names one of your customers, never your own organization. Sending your own org id returns `404 IDENTITY_ORG_NOT_FOUND`. It names the customer (the API calls it an end org): either fastn's id for the customer, or the external reference you registered it under (the `orgId` you sent to `POST /api/v1/orgs`). If you created a customer without one, fastn stored its slug as the external reference at creation time.

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
    "endOrgId": "…",
    "userId": "user_123",
    "role": "end_user",
    "tierId": null,
    "expiresAt": "2026-11-04T18:00:00.000Z",
    "expiresIn": 28800
  }
}
```

Read the token as `response.data.token`. `expiresIn` is 28800 seconds: eight hours.

#### Body fields

All fields are optional; the customer must come from the header, the body or the key.

| Field | What it does |
| --- | --- |
| `endOrgId` | The customer, as fastn's id or your external reference. Use it instead of the header (for example when the API key is pinned to one customer). If you also send `x-org-id`, the two must agree |
| `userId` | The person at your customer. Per-user isolation keys on this id (or on an attested `x-user-id`). Without it, each token gets a random `embed_usr…` id, so nothing carries over between sessions |
| `userEmail`, `userName` | Display only |
| `createIfMissing` | Register the customer named by `endOrgId` if it does not exist yet, then mint for it. Needs the `customers.create` permission. Leave out `x-org-id` for a customer that doesn't exist yet (it is refused with `404` first), so this only works on a key without enforced identity verification |
| `customerName` | Display name for a customer created by `createIfMissing`. Defaults to the id |
| `roleOverride` | Per-user role override that your backend decides |
| `metadata` | Your own data, handed back in the widget's lifecycle callbacks for this session. At most 4 KB of JSON |
| `allowOrgLevel` | Mint an organization-level token with no customer. Only for previewing your own organization; never hand one to a customer |

If there is no customer in the header, the body or the key, and `allowOrgLevel` is not set, the call fails with `400` and code `EMBED_TOKEN_REQUIRES_END_ORG_ID`. An embed token cannot mint another embed token (`403`): mint from your backend with an API key, and use the refresh endpoint below to extend a live session.

Your API key never reaches the browser. See [API keys](../../manage/api-keys.md).

### Refresh, and the session cap

```http
POST /api/v1/embed/token/refresh
```

{% hint style="warning" %}
Refresh is capped at **seven days per session**. At the cap the widget posts `fastn:session-expired` to the parent window and stops. Long-lived sessions do not refresh indefinitely: listen for that message and start a new session by minting a fresh token.
{% endhint %}

The flow for production:

1. Your backend authenticates the user, as it already does.
2. It calls `POST /api/v1/embed/token` with your API key and the customer identifier.
3. It returns the token to your frontend.
4. The SDK mounts with that token and refreshes it, until the seven-day session cap.
