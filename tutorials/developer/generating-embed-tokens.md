# Generating Embed Tokens

Embed tokens are short-lived credentials that scope the Fastn widget to a specific customer. They are generated from your backend using your API key and passed to the iframe.

### The token endpoint

```
POST https://live.gcp.fastn.ai/api/v1/embed/token
```

**Headers:**

```
Authorization: Bearer <FASTN_API_KEY>
Content-Type: application/json
X-fastn-Test-Mode: true        (only for fsk_test_ keys; omit for fsk_live_)
```

**Body:**

```json
{
  "endOrgId": "<customer-org-uuid>",
  "userEmail": "user@example.com",
  "userName": "User Name"
}
```

| Field       | Description                                                                                                                                                                                                                   |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `endOrgId`  | The internal UUID of the customer the widget is for. Must be the UUID — the slug and External ID both return 404. See [Finding Your Org Identifier](https://claude.ai/fastn/tutorials/developer/finding-your-org-identifier). |
| `userEmail` | The email of the individual user. Used for user-level tenancy (see [Tenancy](https://claude.ai/fastn/tutorials/developer/tenancy)).                                                                                           |
| `userName`  | The display name of the individual user.                                                                                                                                                                                      |

**Response:**

```json
{
  "data": {
    "token": "emb_...",
    "endOrgId": "<customer-org-uuid>",
    "expiresIn": 900
  }
}
```

The embed token is prefixed `emb_`. In the hands-on integration, the token was nested under `data` — read `response.data.token`, not `response.token`.

`expiresIn` is `900` seconds — 15 minutes.

> **VERIFY:** The Embed tab UI shows the token request with only `Authorization: Bearer YOUR_API_KEY` and references a `YOUR_CUSTOMER_ID` parameter, while the hands-on integration used a body of `{ endOrgId, userEmail, userName }` and read the token from `data.token`. Confirm the exact request body and response shape against the current API before publishing — the UI snippet and the hands-on result should be reconciled.

### Refreshing tokens

Because tokens expire after 15 minutes, a long-lived embed session needs the token refreshed before it expires. The platform provides a refresh endpoint, and the Embed tab notes that tokens auto-refresh:

```
POST https://live.gcp.fastn.ai/api/v1/embed/token/refresh
```

Use the refresh endpoint to obtain a new token before the current one expires, or generate a fresh token from your backend on each load for shorter sessions.

> **VERIFY:** The refresh endpoint exists (confirmed on the platform). Confirm its exact request and response shape, and whether the SDK (when it ships) handles auto-refresh automatically.

### Token lifecycle

**Tokens expire after 15 minutes.** Generate a fresh token on each page load. Do not generate one and reuse it across sessions or store it for later.

**Generate tokens server-side.** The token is minted from your API key, and your API key must never appear in client-side code. The token request has to happen on your backend.

**Never hardcode a token.** A token pasted into frontend code works until it expires, then the iframe renders blank with no clear error. This is the most common embedding mistake. Always fetch a fresh token from your backend at render time.

### The recommended pattern

Put token generation in a server-side function that reads the API key and org ID from environment variables and returns a fresh token per request:

```javascript
async function getFastnToken({ userEmail, userName }) {
  const res = await fetch("https://live.gcp.fastn.ai/api/v1/embed/token", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.FASTN_API_KEY}`,
      "Content-Type": "application/json",
      "X-fastn-Test-Mode": "true", // omit for live keys
    },
    body: JSON.stringify({
      endOrgId: process.env.FASTN_END_ORG_ID,
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

Expose this through an endpoint your frontend calls at render time. Return only the token.

This pattern is what makes the embed reliable across different users and sessions. Hardcoding or caching tokens is what causes "works for me, fails for them" behavior.
