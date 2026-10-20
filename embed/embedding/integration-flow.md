---
description: Register a customer organization, retrieve an embed token, and load the widget, with the API calls each step uses.
---

# Integration flow

### Pre-requisites

* An API key with caller identity verification (HMAC) turned on: see [API keys](../../manage/api-keys.md).
* The identity hash for each tenant-specific request: see [Identity hash](../../manage/api-keys.md#identity-hash).

Terms used on this page (organization, user, identity hash, widget) are defined in the [Glossary](../../reference/glossary.md).

## User Sign-up

### 1. Register the tenant

Call Create a Customer Organization (see [API Reference: Create a Customer Organization](#create-a-customer-organization)) from your backend server to register the customer org in Fastn.

## Widget Integration

### 2. Retrieve a token

Call Generate Embed Token (see [API Reference: *Generate Embed Token*](#generate-embed-token)), from your backend server to get the authentication token for the tenant.

### 3. Load the widget

Pass the token to your frontend and embed the iframe:

```html
<iframe
  src="https://api.fastn.dev/api/v1/embed/iframe?token=<token>"
  style="width:100%;height:600px;border:none"
  allow="clipboard-write">
</iframe>
```

## API Reference

### Generate Embed Token

**Endpoint**

```
POST https://api.fastn.dev/api/v1/embed/token
```

**Headers**

```
authorization: Bearer <YOUR_API_KEY>
content-type: application/json
x-org-id: <ORG_ID>
x-user-id: <USER_ID>  //optional
x-identity-hmac: <IDENTITY_HASH>
```

**Body**

```json
{ }
```

### Create a Customer Organization

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
  "tier": "<TIER_NAME>",
  "limits": {
    "connections": <MAX_CONNECTION_COUNT>
  }
}
```

### Create a SaaS Connection (Optional)

**Note:** Only needed if access to your product APIs from Fastn is required.

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
x-user-id: <USER_ID>  //optional
x-identity-hmac: <IDENTITY_HASH>
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
