---
description: Minting and refreshing embed tokens from your backend, and the session cap.
---

# Tokens

An embed token identifies one of your customers to the widget. The dashboard shows a live 8-hour token so you can try things immediately. Mint your own from your backend for production.

### The Token API

```http
POST /api/v1/embed/token
Authorization: Bearer <API key>
x-org-id: <orgId>
```

```json
{
  "token": "emb_…",
  "endOrgId": "…",
  "role": "end_user",
  "expiresIn": 28800
}
```

`expiresIn` is 28800 seconds — eight hours.

If the API key is pinned to a particular customer, send the customer in the body instead of the header:

```json
{ "endOrgId": "…" }
```

Your API key never reaches the browser. See [API keys](../../manage/api-keys.md).

### Refresh, and the session cap

```http
POST /api/v1/embed/token/refresh
```

{% hint style="warning" %}
Refresh is capped at **seven days per session**. At the cap the widget posts `fastn:session-expired` to the parent window and stops. Long-lived sessions do not refresh indefinitely — listen for that message and start a new session by minting a fresh token.
{% endhint %}

The flow for production:

1. Your backend authenticates the user, as it already does.
2. It calls `POST /api/v1/embed/token` with your API key and the customer identifier.
3. It returns the token to your frontend.
4. The SDK mounts with that token and refreshes it, until the seven-day session cap.
