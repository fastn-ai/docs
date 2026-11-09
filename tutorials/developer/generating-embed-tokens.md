---
---

# Generating Embed Tokens

Embed tokens are short-lived credentials that scope the fastn widget to a specific customer. They are generated from your backend using your API key and passed to the iframe.

### The token endpoint

```
POST https://api.fastn.dev/api/v1/embed/token
```

**Headers:**

```
Authorization: Bearer <FASTN_API_KEY>
Content-Type: application/json
X-fastn-Test-Mode: true        (only for fsk_test_ keys; omit for fsk_live_)
x-org-id: <customer id>        (fastn's id for the customer, or your external reference)
```

**Body:**

```json
{
  "userId": "<your user id>",
  "userEmail": "user@example.com",
  "userName": "User Name"
}
```

| Field       | Description                                                                                                                                                                                                                   |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `orgId`     | The customer, if you do not send the `x-org-id` header: your own id for it, or fastn's id for it. If you send both, they must name the same customer. See [Finding Your Org Identifier](finding-your-org-identifier.md). |
| `userId`    | Your id for the person at the customer. Per-user isolation keys on this (or on an attested `x-user-id` header). Without it, each token gets a random `embed_usr…` id, so nothing carries over between sessions (see [Tenancy](understanding-tenancy.md)). |
| `userEmail` | The person's email. Display only.                                                                                                                                                                                             |
| `userName`  | The person's display name. Display only.                                                                                                                                                                                      |
| `roleOverride` | Optional. A per-user role override your backend decides.                                                                                                                                                              |
| `metadata`  | Optional. Your own data, handed back in the widget's lifecycle callbacks for this session. At most 4 KB of JSON.                                                                                                             |
| `allowOrgLevel` | Optional. Mint an organization-level token with no customer, for previewing your own organization only. Never hand one to a customer.                                                                                |

With no customer in the header or body and no `allowOrgLevel`, the request fails with `400` and code `EMBED_TOKEN_REQUIRES_END_ORG_ID`. An embed token cannot be used to mint another one (`403`).

**Response:**

```json
{
  "data": {
    "token": "emb_...",
    "userId": "<your user id>",
    "role": "end_user",
    "tierId": null,
    "expiresAt": "2026-11-04T18:00:00.000Z",
    "expiresIn": 28800,
    "orgId": "<your id for the customer>"
  }
}
```

The embed token is prefixed `emb_`. The response is wrapped in `data`: read `response.data.token`, not `response.token`.

`expiresIn` is `28800` seconds, which is 8 hours.

### Refreshing tokens

Because tokens expire after 8 hours, a long-lived embed session needs the token refreshed before it expires. The platform provides a refresh endpoint, and the Embed tab notes that tokens auto-refresh:

```
POST https://api.fastn.dev/api/v1/embed/token/refresh
```

Refresh is capped at seven days per session. At the cap the widget posts `fastn:session-expired` to the parent window; listen for it and mint a new token. See [Token API](../../embed/embedding/token-api.md).

Use the refresh endpoint to obtain a new token before the current one expires, or generate a fresh token from your backend on each load for shorter sessions.

### Token lifecycle

**Tokens expire after 8 hours.** Generate a fresh token on each page load. Do not generate one and reuse it across sessions or store it for later.

**Generate tokens server-side.** The token is minted from your API key, and your API key must never appear in client-side code. The token request has to happen on your backend.

**Never hardcode a token.** A token pasted into frontend code works until it expires, then the iframe renders blank with no clear error. This is the most common embedding mistake. Always fetch a fresh token from your backend at render time.

### The recommended pattern

Put token generation in a server-side function that reads the API key from an environment variable, takes the signed-in person's customer and user id, and returns a fresh token per request:

```javascript
async function getFastnToken({ customerId, userId, userEmail, userName }) {
  const res = await fetch("https://api.fastn.dev/api/v1/embed/token", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.FASTN_API_KEY}`,
      "Content-Type": "application/json",
      "X-fastn-Test-Mode": "true", // omit for live keys
      "x-org-id": customerId, // fastn id or your external reference
    },
    body: JSON.stringify({
      userId,
      userEmail,
      userName,
    }),
  });

  if (!res.ok) {
    throw new Error(`Token request failed: ${res.status}`);
  }

  const json = await res.json();
  return json.data.token;
}
```

Expose this through an endpoint your frontend calls at render time. Return only the token, as `{ "token": "emb_..." }`, never the API key.

This pattern is what makes the embed reliable across different users and sessions. Hardcoding or caching tokens is what causes "works for me, fails for them" behavior.
