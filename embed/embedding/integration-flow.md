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

2. Click **Create key**. The **Create an API key** dialog opens.
3. In the dialog:
   * **Name**: give it something identifiable.
   * **Mode**: select **Live** for production use or **Test** for development. A live key also needs an **Environment**.
   * Set **permissions** (the **Embed backend** preset fits a backend that mints tokens), **allowed IP addresses**, **rate limit** and **expiry** as needed.
   * Enable **caller identity verification (HMAC)**. This is optional but recommended for security.
4. Click **Create key**.

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

Register the customer once from your backend with Create a Customer Organization, before you mint its first token. That endpoint needs an **Admin** key (full access), and the **Embed backend** key that mints tokens gets `403`. Identity verification off is simplest. A key set to enforce needs [identity headers on this call too](#register-with-an-enforcing-key). See [API Reference: Create a Customer Organization](#create-a-customer-organization).

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

{% hint style="info" %}
This endpoint needs an API key with full access (the **Admin** preset). An **Embed backend** key cannot call it. Use a key with identity verification off, or see [Register with an enforcing key](#register-with-an-enforcing-key).
{% endhint %}

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

`name` is the only required field. `plan` is not needed: a paid plan here is refused with `403`.

#### Register with an enforcing key

A key set to **Enforce** refuses a call with no identity headers (`401 IDENTITY_HEADERS_REQUIRED`), and this customer does not exist yet. Send `x-user-id` and leave out `x-org-id`. No end user exists yet, so use any stable id for your provisioning service. The hash signs an empty org id:

```js
const hmac = identityHash("", userId);   // the same as HMAC of "\n" + userId
```

```
x-user-id: <USER_ID>
x-identity-hmac: <hmac>
```

Do not send the new customer's id as `x-org-id`. It names a customer that must already exist, so the call returns `404 IDENTITY_ORG_NOT_FOUND`.

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

Send `userId` (or an attested `x-user-id`) so each person at the customer gets their own session; without one, every token gets a random user id. `x-identity-hmac` is required when the API key's identity verification is set to Enforce. The full field list is on [Tokens](token-api.md), and every error, with a curl for each way of naming the customer, is in [Generate embed tokens](../../tutorials/developer/generating-embed-tokens.md).

**Response**

```json
{
  "data": {
    "token": "emb_…",
    "userId": "<USER_ID>",
    "role": "end_user",
    "tierId": null,
    "expiresAt": "…",
    "expiresIn": 28800,
    "orgId": "<ORG_ID>"
  }
}
```

#### Create a connection for a customer

**Note:** You only need this if you already hold the customer's credentials, such as a token for your own product. Otherwise the customer connects in the widget.

{% hint style="info" %}
This call needs a key with `connections.create`, and the lookups below need `connectors.read` and `settings.read`. The **Embed backend** key has neither `connections.create` nor `settings.read`, so use your **Admin** key.
{% endhint %}

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
    "<FIELD_NAME>": "<VALUE>"
  },
  "name": "<CONNECTION_NAME>"
}
```

| Field | Required | Meaning |
| --- | --- | --- |
| `connectorId` | Yes | The connector. For your own product, `GET /api/v1/saas-connectors` lists it. |
| `authMethodId` | Yes | The auth method on that connector. `GET /api/v1/auth-methods?connectorId=<CONNECTOR_ID>` lists them. |
| `credentials` | Yes | The values for that auth method. |
| `orgId` | No | The customer, if you do not send `x-org-id`: your own id for it, or fastn's id for it. If you send both, they must match. **With neither, the connection is created on your own organization, not a customer's.** |
| `name` | No | A display name, unique per connector and customer. A name already in use returns `409`. Leave it out and fastn generates one. |

`connectionScope` is not accepted on this call and returns `400`.

**The field names in `credentials` come from the auth method.** Each method lists them under `inputContract.properties`, so read them before you build this call. A method whose contract has a `token` field takes `{ "token": "..." }`:

```bash
curl "https://api.fastn.dev/api/v1/auth-methods?connectorId=$CONNECTOR_ID" \
  -H "Authorization: Bearer $FASTN_API_KEY"
```

```json
{
  "data": [
    {
      "id": "<AUTH_METHOD_ID>",
      "type": "API_KEY",
      "inputContract": {
        "type": "object",
        "required": ["token"],
        "properties": { "token": { "type": "string" } }
      }
    }
  ]
}
```

A complete call for one customer:

```bash
curl -X POST https://api.fastn.dev/api/v1/connections \
  -H "Authorization: Bearer $FASTN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connectorId": "<CONNECTOR_ID>",
    "authMethodId": "<AUTH_METHOD_ID>",
    "orgId": "northwind",
    "name": "Northwind production",
    "credentials": { "token": "<THE_CUSTOMERS_TOKEN>" }
  }'
```

The call answers `201` with the new connection. It only creates: to replace a customer's credentials, such as when rotating a token, call `PUT /api/v1/connections/{id}` with the new `credentials`. Other answers:

| Response | Means |
| --- | --- |
| `400` `IDENTITY_ORG_MISMATCH` | `orgId` in the body names a different customer from `x-org-id`. |
| `401` `IDENTITY_HEADERS_REQUIRED` or `IDENTITY_HMAC_INVALID` | The key is set to enforce, and the identity headers are missing or wrong. |
| `403` `Access denied` | `orgId` in the body is not one of your customers. |
| `403` `CONNECTION_LIMIT_REACHED` | This customer is at the connection limit you set for it. |
| `403` `quota_exceeded` | Your customers already have as many connections as your plan includes. |
| `403` | The key lacks `connections.create`. |
| `404` `IDENTITY_ORG_NOT_FOUND` | `x-org-id` is not one of your customers. |
| `409` | That `name` is already in use for this connector. |
| `422` | The app rejected these credentials, so nothing was saved. Check the field names and values. |
| `504` | fastn timed out while saving. The response says whether it is safe to try again. |

**With an Enforce key, every call needs identity headers, including the two lookups above.** For the lookups, sign `x-user-id` with an empty org id, as in [Register with an enforcing key](#register-with-an-enforcing-key). For this call, send and sign `x-org-id` as well and leave `orgId` out of the body, so the hash covers the customer.
