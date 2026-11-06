---
description: "Connected accounts and how they are created."
---

# Connections

Base URL, authentication and errors are on the [REST API overview](README.md).

## Connections

### List connections

```http
GET /v1/connections
```

Connections the caller can reach: their own pool, plus their child customers' for admin/owner. Credentials are never returned. Each row carries endOrgId and endOrgName so a cross-customer list can name the customer it belongs to.

Operation: `listConnections`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `endOrgId` | query | string | No | Customer whose connections to list: fastn's org id, or the id you gave the customer at creation (orgId / externalRef). Omit for the caller's own pool. |
| `orgId` | query | string | No | Alternate spelling of the customer org (the customer detail page uses this). Takes the same values as endOrgId. |
| `userId` | query | string | No | Filter to one external user reference. |
| `connectionScope` | query | string | No | Filter by SaaS-connector connection scope (e.g. inventory). Distinct from scope=saasPool. |
| `scope` | query | string | No | Which pool. saasPool = the caller's own connections. customers = every child customer's connections and none of the caller's own (the partner Connections page's customer view) - account-tier roles only, and refused for a customer-scoped session. One of: `saasPool`, `customers`. |
| `groupBy` | query | string | No |  |
| `includePartnerPool` | query | string | No | Include the partner's shared pool alongside a customer's own rows. |
| `allOrgs` | query | string | No | One of: `true`. |

**Responses**

* `200`: Connections
* `403`: Org outside the caller's scope

### Store connector credentials

```http
POST /v1/connections
```

Creates (or upserts) a connection. Partner backends select the customer org either via the identity headers (x-org-id + x-user-id, proven with x-identity-hmac when the API key's identity-verification mode requires it) or via orgId/endOrgId in the body (customer's fastn org id or its external_ref). When identity headers are present, body orgId/userId must agree with the claim. Upserts by name, or by scope when `connectionScope` is set (re-provisioning a scope rotates that row's credentials); `connectionScope` requires a customer (endOrgId) and must be one of the connector's allowed scopes in the org's SaaS-connector registry.

Operation: `storeConnections`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `x-org-id` | header | string | No | Customer org the request acts for, the customer's fastn org id or the external_ref the partner registered it under. Requires API-key auth on a multi-customer key; always ownership-checked against the key's account. When the key's identity-verification mode is not off, must be proven with x-identity-hmac. |
| `x-user-id` | header | string | No | End-user identifier the partner's backend authorized for this request. May accompany x-org-id or stand alone; covered by x-identity-hmac when the key enforces identity verification. |
| `x-identity-hmac` | header | string | No | Hex HMAC-SHA256 of "{x-org-id}\n{x-user-id}" (the header values exactly as sent, newline-joined; an absent header is the empty string) signed with the API key's identity-verification secret. Required when the key's idv mode is 'required' (missing/invalid = 401); logged-only under 'optional'; ignored when 'off'. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `authMethodId` | `string` | Yes |  |
| `authType` | `string` | No | One of: `OAUTH`, `OAUTH_2`, `OAUTH_1`, `API_KEY`, `INPUT`, `BEARER`, `JWT_BEARER`, `BASIC`, `DIGEST`, `AWS_SIGNATURE`, `NO_AUTH`, `NONE`, `oauth2`, `oauth1`, `api_key`, `bearer`, `jwt`, `basic`, `digest`, `aws`, `none`. |
| `credentials` | `object` | Yes |  |
| `name` | `string` | No |  |
| `expiresAt` | `string` | No |  |
| `userId` | `string` | No |  |
| `userEmail` | `string` | No |  |
| `userName` | `string` | No |  |
| `endOrgId` | `string` | No |  |
| `orgId` | `string` | No |  |
| `authProvider` | `string` | No |  |
| `connectionScope` | `string` | No |  |

**Responses**

* `200`: Existing connection updated (upsert)
* `201`: Connection created
* `400`: Validation error / invalid connectionScope / connectionScope without endOrgId / IDENTITY_ORG_MISMATCH / IDENTITY_USER_MISMATCH
* `401`: Missing or invalid x-identity-hmac on a key whose identity-verification mode is required (IDENTITY_HMAC_INVALID)
* `403`: The partner's customers already have as many app connections as its plan includes ({ error: "quota_exceeded", dimension: "customer_connections", current, limit, limitSource, message }), or this customer is at the connections limit its partner set on it (CONNECTION_LIMIT_REACHED). Another account of an app the customer already connected is not refused
* `404`: x-org-id does not match a customer org (IDENTITY_ORG_NOT_FOUND)
* `502`: The connector service could not be read to count connections or name this one; nothing was stored
* `504`: Storing the credential timed out and a read-back did not find it (TIMEOUT). The error says whether it was confirmed absent (safe to retry) or could not be confirmed

### Find a connection by name

```http
GET /v1/connections/by-name/{connectorId}/{name}
```

Looks up one of the caller's connections by connector id and display name. A display name is unique only per address, so prefer selecting by connection id. Requires connections.read.

Operation: `getConnectionByName`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | path | string | Yes |  |
| `name` | path | string | Yes |  |

**Responses**

* `200`: Connection
* `404`: Not found

### Get a connection

```http
GET /v1/connections/{id}
```

Reads one connection's metadata (never its credentials). 404 when it is outside the caller's org, customer or user scope. Requires connections.read.

Operation: `getConnection`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Connection
* `404`: Connection not found (or outside the caller's scope)

### Update a connection

```http
PUT /v1/connections/{id}
```

Renames a connection, reconnects it with new credentials, or makes it the connector's default (isDefault: true). For a managed connection only those three are supported (400 otherwise). 409 when the new name is already used at the same address. Requires connections.create.

Operation: `updateConnection`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `credentials` | `object` | No |  |
| `authType` | `string` | No | One of: `OAUTH`, `OAUTH_2`, `OAUTH_1`, `API_KEY`, `INPUT`, `BEARER`, `JWT_BEARER`, `BASIC`, `DIGEST`, `AWS_SIGNATURE`, `NO_AUTH`, `NONE`, `oauth2`, `oauth1`, `api_key`, `bearer`, `jwt`, `basic`, `digest`, `aws`, `none`. |
| `expiresAt` | `string` | No |  |
| `isDefault` | `boolean` | No |  |
| `connectionScope` | `string` | No |  |

**Responses**

* `200`: Connection updated
* `404`: Connection not found (or outside the caller's scope)
* `409`: A connection of that name already exists for this connector at the same address. Names are unique per connector and address: per (connector, org, end-org) for a customer-scoped connection, and per (connector, user, org) for an org-level one.

### Disconnect, delete a connection and its stored credential

```http
DELETE /v1/connections/{id}
```

The disconnect endpoint. Takes the connection id from GET /api/v1/connections, not a connector id.

Operation: `deleteConnections`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `404`: Connection not found (or outside the caller's scope)

### Make a connection the default

```http
PATCH /v1/connections/{id}/default
```

Makes this connection the default for its connector, unsetting the previous default. use updateConnection with isDefault: true for those. Requires connections.update.

Operation: `setDefaultConnection`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | for a managed connection). |

**Responses**

* `200`: Updated connection
* `404`: Not found

### Refresh this connection's OAuth tokens now

```http
POST /v1/connections/{id}/refresh
```

Returns the new access token. status is 'not_refreshed' when nothing was rotated: token still current, no refresh token on the credential (Slack bot tokens, API keys), or the provider declined. Requires connections.share (the same gate as /access-token, since it returns the same secret); not available to embed sessions.

Operation: `refreshConnection`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { status: 'refreshed' \| 'not_refreshed', connectionId, access_token?, expires_at? }. not_refreshed is the owner declining to rotate for any reason it does not itself report as an error: no refresh token on the credential, a provider refusal, or no such credential in its vault.
* `403`: Embed session, or insufficient role
* `404`: Connection not found in the caller's scope
* `409`: No description.

## Connect links

### Create a connect link

```http
POST /v1/connect-links
```

Returns a dashboard URL where a user connects, reconnects or fixes the credentials of one connector without signing in; connectionName preselects a connection. Lifetime defaults to CONNECT_LINK_DEFAULT_TTL_MINUTES (20) and can be set per link with expiresInMinutes up to CONNECT_LINK_MAX_TTL_MINUTES (default and ceiling 7 days = 10080; a deployment may set it lower, never higher); the response carries expiresAt. The connection is made at the caller's own workspace and customer. Requires connections.create.

Operation: `createConnectLink`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `connectionName` | `string` | No |  |
| `expiresInMinutes` | `integer` | No |  |

**Responses**

* `200`: { data: { connectUrl, expiresAt } }
* `400`: Validation error, or expiresInMinutes above the deployment max (CONNECT_LINK_TTL_TOO_LONG)

## Oauth

### Start an OAuth connection

```http
POST /v1/oauth/initiate
```

Starts an OAuth connect (or reconnect, with connectionId) for a connector and returns the provider authorization URL to open in a browser. connectionName (optional, max 64) names a NEW account; a name another active account of this connector already uses is refused with 409 CONNECTION_NAME_TAKEN, and without it the auto name (default, connection-1, ...) is kept. setupLinkId (optional) is sent by the setup page so the connection.connected event carries that link's metadata. Requires connections.create.

Operation: `initiateOauthConnection`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `authMethodId` | `string` | No |  |
| `authProviderId` | `string` | No |  |
| `connectionName` | `string` | Yes |  |
| `connectionId` | `string` | No |  |
| `setupLinkId` | `string` | No |  |
| `scopes` | `string[]` | No |  |
| `oauthProxyUrl` | `string` | No |  |
| `returnUrl` | `string` | No |  |
| `dashboardOrigin` | `string` | No |  |
| `oauthVariables` | `object` | No |  |
| `endOrgId` | `string` | No |  |
| `source` | `string` | No |  |
| `connectionScope` | `string` | No |  |

**Responses**

* `200`: { data: { flowId, authorizationUrl } }
* `400`: Validation error or connector has no OAuth method
* `403`: The partner's customers already have as many app connections as its plan includes: { error: "quota_exceeded", code, dimension: "customer_connections", current, limit, limitSource, message }. Not checked for a reconnect (connectionId)
* `404`: Not found
* `502`: The connector service could not be read to name the connection or count the partner's customer connections; nothing was started

## Saas connectors

### List the org's SaaS connectors and their allowed connection scopes

```http
GET /v1/saas-connectors
```

Lists the connectors the caller's org designated as SaaS connectors, with their allowed connection scopes. Requires settings.read.

Operation: `listSaasConnectors`

**Responses**

* `200`: SaaS-connector registry entries

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `saasConnectors` | `object[]` |  |
| `saasConnectors[].id` | `string` |  |
| `saasConnectors[].connectorId` | `string` |  |
| `saasConnectors[].connectorSlug` | `string` |  |
| `saasConnectors[].connectorName` | `string` |  |
| `saasConnectors[].connectorIcon` | `string` |  |
| `saasConnectors[].scopes` | `string[]` |  |
| `saasConnectors[].createdAt` | `string` |  |
| `saasConnectors[].updatedAt` | `string` |  |

### Designate a connector as a SaaS connector and set its allowed connection scopes

```http
PUT /v1/saas-connectors/{connectorId}
```

Admin/owner only (settings.update). connectorId may be the connector's id or its slug; the registration always stores the id. Scopes validate customer connection creation and drive the widget editor's connection-scope picker.

Operation: `upsertSaasConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `scopes` | `string[]` | Yes |  |

**Responses**

* `200`: Upserted
* `404`: Connector not found or not visible to this org

### Remove the SaaS-connector designation

```http
DELETE /v1/saas-connectors/{connectorId}
```

Removes the SaaS-connector designation (and its scopes) from a connector of the caller's org. Requires settings.update; 404 when the connector is not designated.

Operation: `deleteSaasConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `404`: Not found

### List end customers' scoped connections for a registered SaaS connector

```http
GET /v1/saas-connectors/{connectorId}/connections
```

The customers' connections carrying a connectionScope for this connector, owned by the caller's org, newest first, with the owning customer and how many non-archived installations pin each. Unscoped connections are excluded. Paginated (default 20/page); the response carries pagination.total. Disconnect via DELETE /api/v1/connections/{id}.

Operation: `listSaasConnectorConnections`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | path | string | Yes |  |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |

**Responses**

* `200`: Scoped customer connections

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `pagination` | `object` |  |
| `pagination.total` | `integer` |  |
| `pagination.limit` | `integer` |  |
| `pagination.offset` | `integer` |  |
| `connections` | `object[]` |  |
| `connections[].id` | `string` |  |
| `connections[].name` | `string` |  |
| `connections[].connectionScope` | `string` |  |
| `connections[].status` | `string` |  |
| `connections[].verifyStatus` | `string` |  |
| `connections[].endOrgId` | `string` |  |
| `connections[].endOrgName` | `string` |  |
| `connections[].endOrgSlug` | `string` |  |
| `connections[].pinnedInstallations` | `integer` |  |
| `connections[].createdAt` | `string` |  |
| `connections[].updatedAt` | `string` |  |
