---
description: >-
  This page walks you through embedding the fastn widget for your customers:
  register a customer organization, retrieve an embed token, and load the
  widget.
---

# Integration flow

Terms used on this page are defined in the [Glossary](../../reference/glossary.md).

### Pre-requisites

Before you start, you need an API key. We also recommend two optional security measures:

* Enable caller identity verification (HMAC) on the API key.
* Compute an identity hash on your backend and send it with every customer-specific request. The hash is recommended; it is required only when the key's identity verification is set to **Enforce**.

#### Creating an API key

1. Go to **Embed** → **API keys and MCP** → **API keys** (`/access`).

<figure><img src="../../.gitbook/assets/api-key-settings-page.webp" alt="The Settings API Keys page in the earlier dashboard layout, with Test and Live tabs and a Create API Key button"><figcaption></figcaption></figure>

2. Click **Create key**. The **Create an API key** dialog opens.
3. In the dialog:
   * **Name**: give it something identifiable.
   * **Mode**: select **Live** for production use or **Test** for development. A live key also needs an **Environment**.
   * Set **permissions** (the **Embed backend** preset fits a backend that mints tokens), **allowed IP addresses**, **rate limit** and **expiry** as needed.
   * Enable **caller identity verification (HMAC)**. This is optional but recommended for security.
4. Click **Create key**.

<figure><img src="../../.gitbook/assets/api-key-create-dialog.webp" alt="The Create an API key dialog: Name set to Test, Mode with Test and Live cards, Permissions set to Viewer and the What it can touch matrix"><figcaption></figcaption></figure>

#### Creating an identity hash (recommended)

Sending an identity hash with customer-specific requests is optional, but we recommend it for security. The hash confirms that the org ID and user ID you're sending are ones your backend actually authorized.

If you skip this section, omit the `x-identity-hmac` header from your requests and don't enable HMAC on your API key.

**1. Get your identity-verification secret**

When you create an API key with HMAC enabled, a dialog appears showing the secret along with code snippets for generating the hash.

<figure><img src="../../.gitbook/assets/api-key-identity-secret.webp" alt="The dialog shown after creating a key with HMAC enabled: the new key, the identity-verification secret, both blanked out here, and How to use code tabs for Node, Python and Go"><figcaption></figcaption></figure>

**Safety precautions:**

* The secret is shown only once. If you lose it, you'll need to generate a new one.
* Never ship the secret to the client. It must live only on your backend. If it appears in frontend code, anyone can forge a valid hash for any org or user.

**2. Compute the hash**

The hash is an HMAC-SHA256 of the org ID and user ID, joined with a newline and signed with your secret:

```js
const crypto = require("crypto");
const IDV_SECRET = process.env.IDV_SECRET;

function identityHash(orgId = '', userId = '') {
  return crypto.createHmac("sha256", IDV_SECRET)
    .update(`${orgId}\n${userId}`)
    .digest("hex");
}
```

**3. Send it with the identity headers**

Attach the result as `x-identity-hmac`, alongside the plaintext `x-org-id` header and, if you use it, the optional `x-user-id` header:

```
x-org-id: <org-id>
x-user-id: <user-id>  // optional
x-identity-hmac: <identityHash(orgId, userId)>  // optional, recommended
```

The user ID is optional. If you don't send `x-user-id`, call `identityHash(orgId)` so the user ID defaults to an empty string.

The plaintext headers tell the gateway which identity is being claimed, and the hash proves that your backend authorized that specific claim. With the key set to **Enforce**, the gateway rejects any call whose hash is missing or doesn't match the one it recomputes from the plaintext values. With **Monitor only**, it logs mismatches and lets the call through.

### Integration steps

#### Sign up a customer

**1. Register the customer organization**

From your backend server, call Create a Customer Organization to register the customer org in fastn. See [API Reference: Create a Customer Organization](#create-a-customer-organization).

#### Integrate the widget

**2. Retrieve an embed token**

From your backend server, call Generate Embed Token to get the authentication token for the customer. The token is in the response's `data` object: read it as `data.token`. See [API Reference: Generate Embed Token](#generate-embed-token).

**3. Load the widget**

Pass the token to your frontend and embed the iframe:

```html
<iframe
  src="https://api.fastn.dev/api/v1/embed/iframe?token=<token>"
  style="width:100%;height:600px;border:none"
  allow="clipboard-write"
  referrerpolicy="strict-origin-when-cross-origin">
</iframe>
```

### API Reference

#### Create a Customer Organization

**Endpoint**

```
POST https://api.fastn.dev/api/v1/orgs
```

**Headers**

```
authorization: Bearer <YOUR_API_KEY>
content-type: application/json
```

**Body**

```json
{
  "name": "<ORG_NAME>",
  "orgId": "<ORG_ID>",
  "tier": "<TIER_NAME>", //optional
  "limits": { //optional
    "connections": <MAX_CONNECTION_COUNT>
  }
}
```

#### Generate Embed Token

**Endpoint**

```
POST https://api.fastn.dev/api/v1/embed/token
```

**Headers**

```
authorization: Bearer <YOUR_API_KEY>
content-type: application/json
x-org-id: <ORG_ID>
x-user-id: <USER_ID>  // optional
x-identity-hmac: <IDENTITY_HASH>  // optional, recommended for security
```

`x-org-id` is the customer: fastn's id for it, or the `orgId` you registered it under above.

**Body**

```json
{ "userId": "<USER_ID>" }
```

Send `userId` (or an attested `x-user-id`) so each person at the customer gets their own session; without one, every token gets a random user id. The full field list is on [Tokens](token-api.md).

**Response**

```json
{
  "data": {
    "token": "emb_…",
    "endOrgId": "…",
    "userId": "<USER_ID>",
    "role": "end_user",
    "tierId": null,
    "expiresAt": "…",
    "expiresIn": 28800
  }
}
```

#### Create a SaaS Connection (optional)

**Note:** You only need this if fastn must access your product's APIs.

**Endpoint**

```
POST https://api.fastn.dev/api/v1/connections
```

**Headers**

```
authorization: Bearer <YOUR_API_KEY>
content-type: application/json
accept: application/json
x-org-id: <ORG_ID>
x-user-id: <USER_ID>  // optional
x-identity-hmac: <IDENTITY_HASH>  // optional, recommended for security
```

**Body**

```json
{
  "connectorId": "<CONNECTOR_ID>",
  "authMethodId": "<AUTH_METHOD_ID>",
  "credentials": {
    "access_token": "<YOUR_API_KEY>"
  },
  "name": "<CONNECTION_NAME>",
  "connectionScope": "<CONNECTION_SCOPE_NAME>"
}
```
