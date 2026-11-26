---
description: Every credential Fastn uses, where each one lives, and how a call names the customer it acts for.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Authentication

Read this once before you embed the widget or call the API, then follow the links for the full detail on each credential.

<figure><img src="../../.gitbook/assets/diagrams/auth-flow.svg" alt="How authentication works: your backend mints an embed token from Fastn with your API key, passes only the token to your frontend, which opens the widget; the customer signs in to their app and Fastn saves the credential."><figcaption><p>Your API key stays on your backend. Only the short-lived token reaches the browser.</p></figcaption></figure>

1. Your backend calls Fastn with your **API key** and names the customer in `x-org-id`.
2. Fastn returns an **embed token** for that one customer. It lasts 8 hours.
3. Your backend passes only the token to your frontend.
4. Your frontend opens the widget with the token.
5. The customer signs in to their own app in the widget.
6. Fastn stores that **connection's credential**, encrypted and scoped to that customer.

### The credentials

| Credential | Where it lives | What it does | Details |
| --- | --- | --- | --- |
| **API key** (`fsk_test_…`, `fsk_live_…`) | Your backend only | Authenticates every call your backend makes to Fastn | [Below](#test-vs-live-keys), and [API keys](../../manage/api-keys.md) |
| **Identity secret** | Your backend only | Signs `x-org-id` and `x-user-id` as `x-identity-hmac`, so a call can't claim to be another customer | [Identity hash](../../manage/identity-verification.md) |
| **Embed token** | Your frontend, one page load | Opens the widget for one customer and user. Expires after 8 hours; refresh is capped at 7 days per session | [Generating embed tokens](generating-embed-tokens.md) |
| **Connection credential** | Fastn, encrypted | One customer's sign-in to one app. Every run for that customer reuses it | [Connections](../../build/connections/README.md) |
| **MCP sign-in** | Your AI tool | Connects Claude, Cursor, or another AI tool to the Fastn MCP server. You sign in to Fastn; no API key is needed | [Fastn MCP server](../../build/mcp-gateway/README.md) |
| **Customer MCP URL** | Your customer's AI tool | A one-time URL, valid for 10 minutes, that connects a customer's AI tool as that customer | [Customer MCP URL](../../embed/embedding/customer-mcp-url.md) |

### Naming the customer

A call acts for one of your customers when it sends `x-org-id`: your own id for the customer, or Fastn's id for it. Leave it out to act as your own organization. See [Find your org identifier](finding-your-org-identifier.md) and [Scoping a call to a customer](../../reference/api.md#scoping-a-call-to-a-customer).

### Where to find your keys

Go to **Embed → API keys**. Next to **Search keys**, filter pills read **All**, **Live**, and **Test**, and the keys table has a **Mode** column with a **Live** or **Test** badge on each key. Click **Create key** to open the **Create an API key** dialog. A key is shown once, when you create it. Copy it and store it securely.

In that dialog, the **Test** mode card says: "Refused unless the caller sends X-fastn-Test-Mode: true."

### Test vs live keys

Keys are in the `fsk_` format, with two variants:

| Variant | Prefix      | Use for                 |
| ------- | ----------- | ----------------------- |
| Test    | `fsk_test_` | Development and testing |
| Live    | `fsk_live_` | Production              |

#### Test keys require an extra header

Requests made with a `fsk_test_` key **must** include this header:

```
X-fastn-Test-Mode: true
```

Without it, the request is refused with `403` and the error `Test API keys require X-fastn-Test-Mode: true header`. If you're getting unexpected failures with a test key, this header is the first thing to check.

#### Live keys don't need that header

Requests with a `fsk_live_` key do not need `X-fastn-Test-Mode`. Send the header only with test keys.

### Example

Test key:

```javascript
headers: {
  "Authorization": "Bearer fsk_test_...",
  "Content-Type": "application/json",
  "X-fastn-Test-Mode": "true",   // required
}
```

Live key:

```javascript
headers: {
  "Authorization": "Bearer fsk_live_...",
  "Content-Type": "application/json",
  // no X-fastn-Test-Mode header
}
```

### Which header carries the key

| You call | Send the key as |
| -------- | --------------- |
| The platform API, `https://api.fastn.dev/api/v1/…` (a workflow's `/execute`, `/embed/token`, every other route) | `Authorization: Bearer fsk_…` or `X-API-Key: fsk_…` |
| A webhook trigger's URL | `X-API-Key: fsk_…`, `Authorization: Bearer fsk_…`, or `x-fastn-access-key: fsk_…` |
| A connector's webhook URL, with **Require API key** on | `X-API-Key: fsk_…` or `x-fastn-access-key: fsk_…` |

`X-API-Key` works on all three. `x-fastn-access-key` on the platform API, or `Authorization` on a connector's webhook URL, is answered `401`. No endpoint reads `x-fastn-api-key`.

### Keeping keys secure

* Store keys in environment variables, never in source code or client-side bundles.
* Use test keys in development and live keys only in production.
* Your backend uses the API key to mint embed tokens. The key must never reach the browser. See [Generate embed tokens](generating-embed-tokens.md).
