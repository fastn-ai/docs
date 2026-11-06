---
description: "Connectors, actions, auth methods, webhook configs and mock stubs."
---

# Connectors

Base URL, authentication and errors are on the [REST API overview](README.md).

## Connectors

### List connectors

```http
GET /v1/connectors
```

The connector catalog visible to the caller: its own org's connectors, the shared library and what its parent org offers it. slug resolves one connector exactly (own org first, then ancestors, then the shared library). deleted=true (the trash) needs connectors.delete. Requires connectors.read.

Operation: `listConnectors`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `search` | query | string | No | Fuzzy match on name/slug. |
| `slug` | query | string | No | Exact slug lookup; returns at most one connector. |
| `visibility` | query | string | No | One of: `private`, `public`. |
| `categoryKey` | query | string | No | Browse-taxonomy key (see @fastn/core CONNECTOR_CATEGORIES: crm-sales, communication, ai-ml, ...). NOT the `category` field on the connector, which carries the tier. An unrecognised key is ignored and the full list is returned. |
| `labels` | query | string | No | Comma-separated labels; a connector must carry them. |
| `addedFrom` | query | string | No |  |
| `addedTo` | query | string | No |  |
| `includeDeleted` | query | boolean | No | Include soft-deleted rows alongside live ones. |
| `deleted` | query | boolean | No | Trash view: only soft-deleted rows the caller's user or org owns. |
| `orgId` | query | string | No | org_platform lists only the managed catalog. |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |
| `cursor` | query | string | No | Opaque page cursor (from the previous page); not available to a resource-scoped token. |

**Responses**

* `200`: Connector list

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].name` | `string` |  |
| `data[].description` | `string` |  |
| `data[].category` | `string` | The connector's TIER, not its browse category: `managed` for a platform-owned row, `Custom` for an org's own. Browse by `categoryKey`. |
| `data[].categoryKey` | `string` | Browse-taxonomy key from @fastn/core CONNECTOR_CATEGORIES. Resolved on read (authored category, then a curated slug map) and never empty, an unrecognised connector resolves to `other` so it stays browsable. |
| `data[].icon` | `string` |  |
| `data[].authType` | `string` | The label of the connector's default auth method (one of oauth2, oauth1, api_key, bearer, jwt, basic, digest, aws, none), or a value the connector's owner set. Open, not an enum: an owner-set value is theirs and is returned as written. A connection body accepts one of the nine labels or a method type that names the same kind of auth as the connection's auth method or the connector's default method; an owner-set value is not accepted on a connection. |
| `data[].status` | `string` | One of: `active`, `beta`, `deprecated`. |
| `data[].version` | `string` |  |
| `pagination` | `object` | Pagination metadata returned alongside `data` on list endpoints. When the caller omits limit/offset the full set is returned as a single page (limit === total). |
| `pagination.total` | `integer` | Total rows matching the scoped query, across all pages. |
| `pagination.limit` | `integer` | Page size in effect. |
| `pagination.offset` | `integer` | Zero-based offset of the returned page. |
| `categories` | `object[]` | Browse-category facet counts, taken over the set the other filters left and BEFORE categoryKey narrows it, so the counts still describe where else the caller can go once a category is selected. Only categories with at least one match appear. |
| `categories[].key` | `string` |  |
| `categories[].count` | `integer` |  |

### Create a connector

```http
POST /v1/connectors
```

Creates a connector in the caller's org with its auth methods. 409 when the slug is taken in the org. Requires connectors.create.

Operation: `createConnector`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `slug` | `string` | No |  |
| `description` | `string` | No |  |
| `icon` | `string` | No |  |
| `domain` | `string` | No |  |
| `visibility` | `string` | No | One of: `private`, `public`. |
| `ownerLevel` | `string` | No | One of: `fastn`, `account`, `tenant`. |
| `authMethods` | `object[]` | Yes |  |
| `authMethods[].id` | `string` | No |  |
| `authMethods[].type` | `string` | Yes | One of: `NO_AUTH`, `BASIC`, `DIGEST`, `BEARER`, `API_KEY`, `OAUTH`, `INPUT`, `JWT_BEARER`, `AWS_SIGNATURE`, `OAUTH_1`, `OAUTH_2`. |
| `authMethods[].title` | `string` | Yes |  |
| `authMethods[].isDefault` | `boolean` | No |  |
| `authMethods[].inputContract` | `object` | No |  |
| `authMethods[].inputContract.type` | `string` | Yes | Always `object`. |
| `authMethods[].inputContract.properties` | `object` | Yes |  |
| `authMethods[].inputContract.required` | `string[]` | Yes |  |
| `authMethods[].authConfig` | `object` | No |  |
| `authMethods[].authProviderId` | `string` | No |  |
| `authMethods[].docsUrl` | `string` | No |  |
| `labels` | `string[]` | No |  |
| `category` | `string` | No |  |
| `isMultiConnection` | `boolean` | No |  |
| `rateLimit` | `object` | No |  |
| `rateLimit.enabled` | `boolean` | Yes |  |
| `rateLimit.limits` | `object[]` | Yes |  |
| `rateLimit.limits[].requests` | `integer` | Yes |  |
| `rateLimit.limits[].strategy` | `string` | Yes | One of: `FIXED_WINDOW`, `SLIDING_WINDOW`, `CONCURRENCY`. |
| `rateLimit.limits[].window` | `integer` | Yes |  |
| `rateLimit.limits[].burstLimit` | `integer` | No |  |
| `retryPolicy` | `object` | No |  |
| `retryPolicy.enabled` | `boolean` | No |  |
| `retryPolicy.maxAttempts` | `integer` | No |  |
| `retryPolicy.initialDelayMs` | `integer` | No |  |
| `retryPolicy.backoffMultiplier` | `number` | No |  |
| `retryPolicy.maxDelayMs` | `integer` | No |  |
| `retryPolicy.maxTotalDelayMs` | `integer` | No |  |
| `retryPolicy.retryOnStatuses` | `integer[]` | No |  |
| `retryPolicy.retryOnNetworkErrors` | `boolean` | No |  |
| `retryPolicy.respectRetryAfter` | `boolean` | No |  |
| `retryPolicy.methods` | `string[]` | No |  |
| `timeoutMs` | `integer` | No |  |
| `additionalFields` | `object` | No |  |
| `protocol` | `string` | No | One of: `REST`, `MCP`, `FTP`, `DB`. |
| `mcpServerUrl` | `string` | No |  |
| `dbConnectionConfig` | `object` | No |  |
| `dbConnectionConfig.dbType` | `string` | Yes | One of: `postgres`, `redshift`, `mysql`, `mssql`, `mongodb`. |
| `dbConnectionConfig.host` | `string` | No |  |
| `dbConnectionConfig.port` | `integer` | No |  |
| `dbConnectionConfig.database` | `string` | No |  |
| `dbConnectionConfig.username` | `string` | No |  |
| `dbConnectionConfig.password` | `string` | No |  |
| `dbConnectionConfig.ssl` | `boolean or string` | No |  |
| `dbConnectionConfig.authSource` | `string` | No |  |
| `ftpConnectionConfig` | `object` | No |  |
| `ftpConnectionConfig.protocol` | `string` | Yes | One of: `ftp`, `ftps`, `sftp`. |
| `ftpConnectionConfig.host` | `string` | No |  |
| `ftpConnectionConfig.port` | `integer` | No |  |
| `ftpConnectionConfig.username` | `string` | No |  |
| `ftpConnectionConfig.password` | `string` | No |  |
| `ftpConnectionConfig.privateKey` | `string` | No |  |
| `ftpConnectionConfig.secure` | `boolean` | No |  |
| `ftpConnectionConfig.rejectUnauthorized` | `boolean` | No |  |
| `redisConnectionConfig` | `object` | No |  |
| `redisConnectionConfig.host` | `string` | No |  |
| `redisConnectionConfig.port` | `integer` | No |  |
| `redisConnectionConfig.password` | `string` | No |  |
| `redisConnectionConfig.tls` | `boolean` | No |  |
| `redisConnectionConfig.db` | `integer` | No |  |
| `connectionVerifyActionId` | `string` | No |  |

**Responses**

* `201`: Created connector
* `400`: Validation error
* `403`: Not allowed to publish publicly
* `409`: Slug already exists

### Export several connectors

```http
POST /v1/connectors/export
```

A bundle of several connectors; ids the caller cannot see are listed in notFound. Includes OAuth client secrets unless includeSecrets is false (then connectors.read suffices; otherwise owner/admin/developer).

Operation: `exportConnectors`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | `string[]` | Yes |  |
| `includeSecrets` | `boolean` | No | Default: `true`. |

**Responses**

* `200`: Bundle
* `400`: ids missing

### Import a connector bundle

```http
POST /v1/connectors/import
```

Imports a bundle produced by export into the caller's org: { connector, actions, webhookConfigs, authProviders, slug?, name? } for one, or { connectors: [...] } for several. slug/name override the single connector's identity. ownerLevel: owner, admin or developer.

Operation: `importConnectors`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connector` | `object` | No |  |
| `actions` | `object[]` | No |  |
| `webhookConfigs` | `object[]` | No |  |
| `authProviders` | `object[]` | No |  |
| `connectors` | `object[]` | No | Several bundles, each { connector, actions, webhookConfigs, authProviders }. |
| `slug` | `string` | No |  |
| `name` | `string` | No |  |
| `ownerLevel` | `string` | No | One of: `fastn`. |

**Responses**

* `200`: Import result
* `400`: Invalid bundle

### Get a connector's workspace request headers

```http
GET /v1/connectors/{connectorSlug}/request-headers
```

Workspace request headers: extra HTTP headers this workspace adds to every call it makes through a connector, shared catalog connectors included, applied to action executes and workflow runs after the action's own headers. The connector definition is never changed and other workspaces are unaffected. Values are never logged. A change reaches direct executes within about a minute, and workflow runs within about 5 minutes (each run caches a connector definition for up to 4 minutes). A caller scoped to one customer (a customer-pinned API key or customer-scoped token) gets 403 TENANT_SCOPED_CALLER. Returns this workspace's config for the connector: { connectorId, connectorSlug, workspace, headers, actions }, empty when none is set. Requires connectors.read and an owner, admin or developer role.

Operation: `getConnectorRequestHeaders`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | path | string | Yes | Connector slug (e.g. grafanaCloud) or id. |

**Responses**

* `200`: { data: { connectorId, connectorSlug, workspace, headers, actions } }
* `403`: Role or permission missing, or a caller scoped to one customer (TENANT_SCOPED_CALLER)
* `404`: Connector not found or not visible to this workspace

### Set a connector's workspace request headers

```http
PUT /v1/connectors/{connectorSlug}/request-headers
```

Workspace request headers: extra HTTP headers this workspace adds to every call it makes through a connector, shared catalog connectors included, applied to action executes and workflow runs after the action's own headers. The connector definition is never changed and other workspaces are unaffected. Values are never logged. A change reaches direct executes within about a minute, and workflow runs within about 5 minutes (each run caches a connector definition for up to 4 minutes). A caller scoped to one customer (a customer-pinned API key or customer-scoped token) gets 403 TENANT_SCOPED_CALLER. REPLACES this workspace's whole config for the connector, so read it with getConnectorRequestHeaders first and send everything to keep. connectorSlug "grafanaCloud", body { "headers": { "X-Disable-Provenance": "true" } }. Per action: { "actions": { "&lt;actionSlug>": { "X-Disable-Provenance": "true" } } }; an action value of null removes a connector-level header for that action only. Refused (400): Authorization, Cookie, Host, Content-Type, Content-Length, Transfer-Encoding, X-API-Key, Proxy-*, x-gateway-*, x-jwt-*, any header the connector's own authentication sets, values with line breaks or templates, more than 20 headers per map or 100 action overrides, and action slugs the connector does not have. {} clears the config. Requires connectors.update and an owner, admin or developer role.

Operation: `setConnectorRequestHeaders`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | path | string | Yes | Connector slug (e.g. grafanaCloud) or id. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `headers` | `object` | No |  |
| `actions` | `object` | No |  |

**Responses**

* `200`: { data: { connectorId, connectorSlug, workspace, headers, actions } } after the write
* `400`: VALIDATION_ERROR with details[{ path, message }]: a header that may not be set, an invalid name or value, an unknown action slug, or over a cap
* `403`: Role or permission missing, or a caller scoped to one customer (TENANT_SCOPED_CALLER)
* `404`: Connector not found or not visible to this workspace

### Clear a connector's workspace request headers

```http
DELETE /v1/connectors/{connectorSlug}/request-headers
```

Workspace request headers: extra HTTP headers this workspace adds to every call it makes through a connector, shared catalog connectors included, applied to action executes and workflow runs after the action's own headers. The connector definition is never changed and other workspaces are unaffected. Values are never logged. A change reaches direct executes within about a minute, and workflow runs within about 5 minutes (each run caches a connector definition for up to 4 minutes). A caller scoped to one customer (a customer-pinned API key or customer-scoped token) gets 403 TENANT_SCOPED_CALLER. Removes every header this workspace set for the connector, per-action overrides included. Requires connectors.update and an owner, admin or developer role.

Operation: `clearConnectorRequestHeaders`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | path | string | Yes | Connector slug (e.g. grafanaCloud) or id. |

**Responses**

* `200`: { data: { connectorId, connectorSlug, workspace, headers: {}, actions: {} } }
* `403`: Role or permission missing, or a caller scoped to one customer (TENANT_SCOPED_CALLER)
* `404`: Connector not found or not visible to this workspace

### Get connector

```http
GET /v1/connectors/{id}
```

Reads one connector with its auth methods, from the caller's org, its ancestors or the shared library. 404 when it is not visible to the caller. Requires connectors.read.

Operation: `getConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Connector
* `404`: Not found

### Update connector

```http
PUT /v1/connectors/{id}
```

Updates a connector the caller's org owns. Requires connectors.update.

Operation: `updateConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `version` | `string` | No |  |
| `description` | `string` | No |  |
| `icon` | `string` | No |  |
| `domain` | `string` | No |  |
| `visibility` | `string` | No | One of: `private`, `public`. |
| `featured` | `boolean` | No |  |
| `featuredRank` | `integer` | No |  |
| `authMethods` | `object[]` | No |  |
| `authMethods[].id` | `string` | No |  |
| `authMethods[].type` | `string` | Yes | One of: `NO_AUTH`, `BASIC`, `DIGEST`, `BEARER`, `API_KEY`, `OAUTH`, `INPUT`, `JWT_BEARER`, `AWS_SIGNATURE`, `OAUTH_1`, `OAUTH_2`. |
| `authMethods[].title` | `string` | Yes |  |
| `authMethods[].isDefault` | `boolean` | No |  |
| `authMethods[].inputContract` | `object` | No |  |
| `authMethods[].inputContract.type` | `string` | Yes | Always `object`. |
| `authMethods[].inputContract.properties` | `object` | Yes |  |
| `authMethods[].inputContract.required` | `string[]` | Yes |  |
| `authMethods[].authConfig` | `object` | No |  |
| `authMethods[].authProviderId` | `string` | No |  |
| `authMethods[].docsUrl` | `string` | No |  |
| `labels` | `string[]` | No |  |
| `category` | `string` | No |  |
| `isMultiConnection` | `boolean` | No |  |
| `rateLimit` | `object` | No |  |
| `rateLimit.enabled` | `boolean` | Yes |  |
| `rateLimit.limits` | `object[]` | Yes |  |
| `rateLimit.limits[].requests` | `integer` | Yes |  |
| `rateLimit.limits[].strategy` | `string` | Yes | One of: `FIXED_WINDOW`, `SLIDING_WINDOW`, `CONCURRENCY`. |
| `rateLimit.limits[].window` | `integer` | Yes |  |
| `rateLimit.limits[].burstLimit` | `integer` | No |  |
| `retryPolicy` | `object` | No |  |
| `retryPolicy.enabled` | `boolean` | No |  |
| `retryPolicy.maxAttempts` | `integer` | No |  |
| `retryPolicy.initialDelayMs` | `integer` | No |  |
| `retryPolicy.backoffMultiplier` | `number` | No |  |
| `retryPolicy.maxDelayMs` | `integer` | No |  |
| `retryPolicy.maxTotalDelayMs` | `integer` | No |  |
| `retryPolicy.retryOnStatuses` | `integer[]` | No |  |
| `retryPolicy.retryOnNetworkErrors` | `boolean` | No |  |
| `retryPolicy.respectRetryAfter` | `boolean` | No |  |
| `retryPolicy.methods` | `string[]` | No |  |
| `timeoutMs` | `integer` | No |  |
| `additionalFields` | `object` | No |  |
| `commit` | `string` | No |  |
| `protocol` | `string` | No | One of: `REST`, `MCP`, `FTP`, `DB`. |
| `mcpServerUrl` | `string` | No |  |
| `ftpConnectionConfig` | `object` | No |  |
| `ftpConnectionConfig.protocol` | `string` | Yes | One of: `ftp`, `ftps`, `sftp`. |
| `ftpConnectionConfig.host` | `string` | No |  |
| `ftpConnectionConfig.port` | `integer` | No |  |
| `ftpConnectionConfig.username` | `string` | No |  |
| `ftpConnectionConfig.password` | `string` | No |  |
| `ftpConnectionConfig.privateKey` | `string` | No |  |
| `ftpConnectionConfig.secure` | `boolean` | No |  |
| `ftpConnectionConfig.rejectUnauthorized` | `boolean` | No |  |
| `dbConnectionConfig` | `object` | No |  |
| `dbConnectionConfig.dbType` | `string` | Yes | One of: `postgres`, `redshift`, `mysql`, `mssql`, `mongodb`. |
| `dbConnectionConfig.host` | `string` | No |  |
| `dbConnectionConfig.port` | `integer` | No |  |
| `dbConnectionConfig.database` | `string` | No |  |
| `dbConnectionConfig.username` | `string` | No |  |
| `dbConnectionConfig.password` | `string` | No |  |
| `dbConnectionConfig.ssl` | `boolean or string` | No |  |
| `dbConnectionConfig.authSource` | `string` | No |  |
| `redisConnectionConfig` | `object` | No |  |
| `redisConnectionConfig.host` | `string` | No |  |
| `redisConnectionConfig.port` | `integer` | No |  |
| `redisConnectionConfig.password` | `string` | No |  |
| `redisConnectionConfig.tls` | `boolean` | No |  |
| `redisConnectionConfig.db` | `integer` | No |  |
| `connectionInitActionId` | `string` | No |  |
| `credentialMapping` | `object` | No |  |
| `generateKeyPair` | `boolean` | No |  |
| `connectionVerifyActionId` | `string` | No |  |
| `verifySuccessPath` | `string` | No |  |

**Responses**

* `200`: Updated connector
* `400`: No description.
* `403`: No description.
* `404`: Not found

### Delete connector (soft by default)

```http
DELETE /v1/connectors/{id}
```

Soft-deletes a connector the caller's org owns (restorable with restoreConnector); hard=true deletes it permanently. Its connections are removed with it. 409 when a fork in another org still depends on it. Requires connectors.delete.

Operation: `deleteConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `hard` | query | boolean | No | Delete permanently instead of moving to trash. |

**Responses**

* `200`: Deleted. Both paths also delete the connector's connections for real, a credential has no meaning without the connector it is bound to, and there is no soft-delete state for one; deletedConnections reports how many went. Restoring a soft-deleted connector does not bring them back: reconnect. Scoped to the connector's owning org and its customers; a platform-owned (org_platform) connector cascades nothing, since its connections belong to every customer.
* `404`: Not found

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.deleted` | `boolean` |  |
| `data.hard` | `boolean` |  |
| `data.deletedConnections` | `integer` |  |

### Create an action on a connector

```http
POST /v1/connectors/{id}/actions
```

Same as createAction; the path's connector id replaces any connectorId in the body.

Operation: `createConnectorAction`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Connector id. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `slug` | `string` | Yes |  |
| `description` | `string` | No |  |
| `type` | `string` | Yes | One of: `HTTP`, `GRPC`, `FTP`, `LAMBDA`, `DB`. |
| `method` | `string` | No | One of: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `PROPFIND`, `MKCOL`, `MOVE`, `COPY`, `LOCK`, `UNLOCK`. |
| `path` | `string` | No |  |
| `headers` | `object` | No |  |
| `queryParams` | `object` | No |  |
| `bodyTemplate` | `string` | No |  |
| `httpConfig` | `object` | No |  |
| `httpConfig.url` | `string` | Yes |  |
| `httpConfig.method` | `string` | Yes | One of: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `PROPFIND`, `MKCOL`, `MOVE`, `COPY`, `LOCK`, `UNLOCK`. |
| `httpConfig.path` | `string` | No |  |
| `httpConfig.headers` | `object` | No |  |
| `httpConfig.queryParams` | `object` | No |  |
| `httpConfig.body` | `any` | No |  |
| `httpConfig.bodyType` | `string` | No | One of: `none`, `json`, `text`, `raw`, `form-data`, `form-urlencoded`, `binary`, `multipart-related`, `graphql`. |
| `httpConfig.bodyTemplate` | `any` | No |  |
| `grpcConfig` | `object` | No |  |
| `grpcConfig.target` | `string` | Yes |  |
| `grpcConfig.serviceName` | `string` | Yes |  |
| `grpcConfig.methodName` | `string` | Yes |  |
| `grpcConfig.jsonRequest` | `object` | No |  |
| `grpcConfig.metadata` | `object[]` | No |  |
| `grpcConfig.metadata[].key` | `string` | Yes |  |
| `grpcConfig.metadata[].value` | `string` | Yes |  |
| `grpcConfig.authConfig` | `object` | No |  |
| `grpcConfig.timeout` | `integer` | No |  |
| `ftpConfig` | `object` | No |  |
| `ftpConfig.operation` | `string` | Yes | One of: `list`, `download`, `upload`, `delete`, `rename`, `mkdir`, `exists`. |
| `ftpConfig.remotePath` | `string` | Yes |  |
| `ftpConfig.transferMode` | `string` | No | One of: `binary`, `ascii`. |
| `ftpConfig.renameTo` | `string` | No |  |
| `redisConfig` | `object` | No |  |
| `redisConfig.operation` | `string` | Yes | One of: `get`, `set`, `del`, `exists`, `expire`, `ttl`, `keys`, `incr`, `decr`, `mget`, `mset`, `hget`, `hset`, `hgetall`, `hdel`, `lpush`, `rpush`, `lpop`, `rpop`, `lrange`, `llen`, `publish`, `incrby`, `setnx`, `hmget`, `hmset`, `hexists`, `hincrby`, `hlen`, `ltrim`, `lrem`, `lindex`, `sadd`, `srem`, `smembers`, `sismember`, `scard`, `zadd`, `zrem`, `zrange`, `zrangebyscore`, `zscore`, `zcard`, `persist`, `type`, `ping`. |
| `redisConfig.key` | `string` | No |  |
| `redisConfig.field` | `string` | No |  |
| `redisConfig.value` | `string` | No |  |
| `redisConfig.ttl` | `integer` | No |  |
| `redisConfig.start` | `integer` | No |  |
| `redisConfig.stop` | `integer` | No |  |
| `redisConfig.pattern` | `string` | No |  |
| `redisConfig.channel` | `string` | No |  |
| `redisConfig.values` | `string[]` | No |  |
| `redisConfig.member` | `string` | No |  |
| `redisConfig.members` | `string[]` | No |  |
| `redisConfig.score` | `number` | No |  |
| `redisConfig.min` | `string` | No |  |
| `redisConfig.max` | `string` | No |  |
| `redisConfig.count` | `integer` | No |  |
| `redisConfig.amount` | `integer` | No |  |
| `redisConfig.fields` | `string[]` | No |  |
| `lambdaConfig` | `object` | No |  |
| `lambdaConfig.functionArn` | `string` | Yes |  |
| `lambdaConfig.region` | `string` | No |  |
| `lambdaConfig.payload` | `object` | No |  |
| `lambdaConfig.invocationType` | `string` | No | One of: `RequestResponse`, `Event`, `DryRun`. |
| `dbConfig` | `object` | No |  |
| `dbConfig.operation` | `string` | Yes | One of: `query`. |
| `dbConfig.dbType` | `string` | Yes | One of: `postgres`, `redshift`, `mysql`, `mssql`, `mongodb`. |
| `dbConfig.query` | `string` | No |  |
| `authConfig` | `object` | No |  |
| `inputContract` | `object` | No |  |
| `inputContract.type` | `string` | Yes | Always `object`. |
| `inputContract.properties` | `object` | Yes |  |
| `inputContract.required` | `string[]` | No |  |
| `outputContract` | `object` | No |  |
| `outputContract.type` | `string` | Yes | Always `object`. |
| `outputContract.properties` | `object` | Yes |  |
| `outputContract.required` | `string[]` | No |  |
| `language` | `string` | No | One of: `PYTHON`, `JS`. |
| `code` | `string` | No |  |
| `rateLimit` | `object` | No |  |
| `rateLimit.enabled` | `boolean` | Yes |  |
| `rateLimit.limits` | `object[]` | Yes |  |
| `rateLimit.limits[].requests` | `integer` | Yes |  |
| `rateLimit.limits[].strategy` | `string` | Yes | One of: `FIXED_WINDOW`, `SLIDING_WINDOW`, `CONCURRENCY`. |
| `rateLimit.limits[].window` | `integer` | Yes |  |
| `rateLimit.limits[].burstLimit` | `integer` | No |  |
| `stage` | `string` | No | One of: `test`, `live`. |
| `folderId` | `string` | No |  |
| `externalVersion` | `string` | No |  |
| `apiVersion` | `string` | No |  |
| `isDefaultExternalVersion` | `boolean` | No |  |
| `versionMajor` | `integer` | No |  |
| `submissionNote` | `string` | No |  |

**Responses**

* `201`: Created action
* `400`: Validation or contract-lint error
* `404`: Not found

### Export a connector's actions (path form)

```http
GET /v1/connectors/{id}/actions/export
```

Same as exportActions with the connector in the path.

Operation: `exportConnectorActions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Export
* `404`: Not found

### Import actions (path form)

```http
POST /v1/connectors/{id}/actions/import
```

Same as importActions with the connector in the path.

Operation: `importConnectorActions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | `string` | No | Public URL of the spec to fetch (https:// is assumed when no scheme is given). |
| `content` | `string` | No | The spec as a string (JSON or YAML). |
| `format` | `string` | No | Format hint; detected when omitted. One of: `openapi`, `postman`, `hub`, `fastn`. |
| `baseUrl` | `string` | No | Overrides the spec's server URL. |
| `conflictResolution` | `string` | No | What to do when an action slug already exists. One of: `skip`, `overwrite`, `rename`. Default: `"skip"`. |
| `preview` | `boolean` | No | Parse and return the actions without creating them. |
| `selectedSlugs` | `string[]` | No | Import only these slugs. |

**Responses**

* `200`: Per-action results (created, skipped, overwritten, renamed, error), or the preview
* `400`: Invalid JSON, no connectorId, unparseable spec or a private URL
* `404`: Not found

### Diff two versions of an action

```http
GET /v1/connectors/{id}/actions/{actionSlug}/version-diff
```

Contract diff between two versions of one action (added, removed and changed input/output fields, required-field shifts). Compare external versions with from/to or internal majors with fromMajor/toMajor. {id} is the connector slug. Requires connectors.read.

Operation: `getActionVersionDiff`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Connector slug. |
| `actionSlug` | path | string | Yes |  |
| `from` | query | string | No | External version, e.g. v1. |
| `to` | query | string | No |  |
| `fromMajor` | query | integer | No |  |
| `toMajor` | query | integer | No |  |

**Responses**

* `200`: Diff
* `400`: Missing or invalid version selectors
* `404`: Not found

### Activate connector for customer

```http
POST /v1/connectors/{id}/activate
```

Marks a connector active for a customer (the caller's own customer, or endOrgId for a partner-side call). 403 when endOrgId differs from the caller's customer. Requires connections.create.

Operation: `activateConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `endOrgId` | `string` | No |  |

**Responses**

* `201`: Activation created
* `404`: Connector not found

### Analyze a connector's entities

```http
GET /v1/connectors/{id}/entities
```

Groups a connector's actions into entities with derived primary and natural keys and execution order. {id} is the connector id or slug. Requires connectors.read.

Operation: `getConnectorEntities`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Connector id or slug. |

**Responses**

* `200`: Entities
* `404`: Not found

### Export a connector bundle

```http
GET /v1/connectors/{id}/export
```

The connector with its actions, webhook configs and auth providers as a portable bundle. Includes OAuth client secrets unless includeSecrets=false; with secrets it is owner/admin/developer only, without it connectors.read.

Operation: `exportConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `includeSecrets` | query | boolean | No |  |

**Responses**

* `200`: Connector bundle
* `404`: Not found

### Fork a parent's custom connector into your own org, secrets included

```http
POST /v1/connectors/{id}/fork
```

Copies the connector with its actions, action folders, auth methods, OAuth providers (client secrets included), webhook configs and app registrations, keeping its slug so your workflows resolve to the copy. Requires connectors.create. A shared catalog connector answers 400 FORK_CONNECTOR_CATALOG: every org already uses the same one.

Operation: `forkConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `endOrgId` | query | string | No | Partner preview: act for this customer as its embed would |

**Responses**

* `200`: Already forked
* `201`: data: { id, ... }
* `400`: FORK_CONNECTOR_CATALOG
* `409`: FORK_SLUG_CONFLICT

### List a connector's methods

```http
GET /v1/connectors/{id}/methods
```

A connector's actions (slug, name, HTTP method, path) with its scope and auth methods. {id} is the connector id or slug. Requires connectors.read.

Operation: `getConnectorMethods`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Connector id or slug. |

**Responses**

* `200`: Methods
* `404`: Not found

### Promote a connector

```http
POST /v1/connectors/{id}/promote
```

Moves a connector to a stage (live by default) and snapshots the version. Refused (400) when an action the connector needs has not been verified. Requires connectors.update.

Operation: `promoteConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Connector id. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `stage` | `string` | No | Default: `"live"`. |
| `commit` | `string` | No | Change note recorded with the version. |

**Responses**

* `200`: Promoted connector
* `400`: Invalid JSON or unverified actions
* `404`: Not found

### Publish a connector version

```http
POST /v1/connectors/{id}/publish-version
```

Applies a stored version snapshot to the live connector. Not supported for managed connectors (409); use promote. Requires connectors.update.

Operation: `publishConnectorVersion`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Connector id. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `versionId` | `string` | Yes | connector_version id to apply (from GET /connectors/{id}/versions). |
| `commit` | `string` | No |  |

**Responses**

* `200`: Updated connector
* `400`: versionId missing or unverified actions
* `404`: Version not found
* `409`: managed connector

### Restore a soft-deleted connector

```http
POST /v1/connectors/{id}/restore
```

Restores a soft-deleted connector and its actions from the trash. Requires connectors.delete.

Operation: `restoreConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Restored
* `404`: Not found

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.restored` | `boolean` |  |
| `data.restoredActions` | `integer` | Count of actions cascade-restored alongside the connector |

### Revert a connector to a version

```http
POST /v1/connectors/{id}/revert
```

Restores the connector's test stage from a stored version snapshot. Not supported for managed connectors (409). Requires connectors.update.

Operation: `revertConnector`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Connector id. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `versionId` | `string` | Yes | connector_version id to apply (from GET /connectors/{id}/versions). |

**Responses**

* `200`: Reverted connector
* `400`: versionId missing
* `404`: Version not found
* `409`: managed connector

### Sync an MCP connector's tools

```http
POST /v1/connectors/{id}/sync-mcp-tools
```

Discovers the tools of an MCP-protocol connector's server and upserts them as actions. Requires connectors.update.

Operation: `syncMcpTools`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Sync result
* `404`: Not found

### Who uses a connector version

```http
GET /v1/connectors/{id}/version-usage
```

Per-customer pins and workflows whose saved manifest references this connector, optionally narrowed to one externalVersion. For deprecation and upgrade planning. {id} is the connector slug. Requires connectors.read.

Operation: `getConnectorVersionUsage`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Connector slug. |
| `externalVersion` | query | string | No |  |

**Responses**

* `200`: Pins and workflows

### List connector versions

```http
GET /v1/connectors/{id}/versions
```

Version snapshots of a connector, newest first. Seeds an initial snapshot from the current state when there is none. Requires connectors.read.

Operation: `listConnectorVersions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Connector id. |
| `stage` | query | string | No | One of: `test`, `live`. |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |

**Responses**

* `200`: Version list

### Get a connector version

```http
GET /v1/connectors/{id}/versions/{versionId}
```

Reads one connector version snapshot. Requires connectors.read.

Operation: `getConnectorVersion`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `versionId` | path | string | Yes |  |

**Responses**

* `200`: Version snapshot
* `404`: Not found

### List a connector's webhook configs

```http
GET /v1/connectors/{id}/webhook-config
```

Webhook configs (events, subscription code, inputs, verification) of a connector. Requires connectors.read.

Operation: `listWebhookConfigs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |

**Responses**

* `200`: { data: [webhookConfig] }

### Create a webhook config

```http
POST /v1/connectors/{id}/webhook-config
```

Adds a webhook config to a connector: EVENT_WEBHOOK (subscription code registers the webhook with the provider) or APP (manually registered, routed by eventKey). Requires connectors.create.

Operation: `createWebhookConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | One of: `APP`, `EVENT_WEBHOOK`. |
| `subscription` | `string` | No |  |
| `unsubscription` | `string` | No |  |
| `resubscription` | `string` | No |  |
| `events` | `object[]` | No |  |
| `events[].id` | `string` | Yes |  |
| `events[].label` | `string` | Yes |  |
| `events[].description` | `string` | No |  |
| `events[].payloadSchema` | `any` | No |  |
| `inputs` | `object[]` | No |  |
| `inputs[].key` | `string` | Yes |  |
| `inputs[].value` | `string` | Yes |  |
| `inputs[].hidden` | `boolean` | No | Default: `false`. |
| `requiredActions` | `object[]` | No |  |
| `requiredActions[].actionId` | `string` | Yes |  |
| `requiredActions[].label` | `string` | Yes |  |
| `requiredActions[].value` | `string` | Yes |  |
| `requiredActions[].mappedTo` | `string` | No |  |
| `authProviderId` | `string` | No |  |
| `eventKey` | `string` | No |  |
| `verification` | `object` | No |  |
| `verification.eventsVerification` | `object` | Yes |  |
| `verification.eventsVerification.method` | `string` | Yes | One of: `HMAC`, `CHALLENGE_RESPONSE`, `NONE`, `VERIFICATION_TOKEN`, `HEADER_TOKEN`. |
| `verification.eventsVerification.signatureHeader` | `string` | No |  |
| `verification.eventsVerification.algorithm` | `string` | No |  |
| `verification.eventsVerification.timestampHeader` | `string` | No |  |
| `verification.eventsVerification.maxTimestampAgeMs` | `integer` | No |  |
| `verification.eventsVerification.signaturePrefix` | `string` | No |  |
| `verification.eventsVerification.signatureFormat` | `string` | No | One of: `hex`, `stripe`. |
| `verification.eventsVerification.signingPayload` | `string` | No | One of: `body`, `hubspot_v1`, `hubspot_v2`, `hubspot_v3`, `slack_v0`, `stripe_v1`. |
| `verification.challengeDetection` | `object` | No |  |
| `verification.challengeDetection.field` | `string` | Yes |  |
| `verification.challengeDetection.value` | `string` | Yes |  |
| `verification.challengeDetection.responseField` | `string` | Yes |  |
| `verification.tokenHandshake` | `object` | No |  |
| `verification.tokenHandshake.field` | `string` | Yes |  |
| `verification.getChallenge` | `object` | No |  |
| `verification.getChallenge.source` | `string` | No | One of: `query`, `header`. |
| `verification.getChallenge.param` | `string` | No |  |
| `verification.getChallenge.verifyParam` | `string` | No |  |
| `verification.getChallenge.responseType` | `string` | No | One of: `text`, `json`. |
| `verification.getChallenge.responseField` | `string` | No |  |
| `verification.headerPayload` | `object` | No |  |
| `verificationSecret` | `string` | No |  |
| `enabled` | `boolean` | No | Default: `true`. |
| `endOrgRouting` | `object` | No |  |
| `endOrgRouting.source` | `string` | Yes | One of: `header`, `body`. |
| `endOrgRouting.field` | `string` | Yes |  |
| `requireApiKey` | `boolean` | No | Default: `false`. |

**Responses**

* `201`: Created webhook config
* `400`: Validation error
* `404`: Not found

### List a connector's actions by slug

```http
GET /v2/connectors/{connector}/actions
```

Lists the actions of a connector addressed by slug, resolving the caller's own connector first, then inherited and platform ones. Returns id, slug, name, version and description per action. Requires connectors.read.

Operation: `listConnectorActionsBySlug`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connector` | path | string | Yes | Connector slug |

**Responses**

* `200`: { data: { id, slug, name, version, description }[] }
* `404`: Connector not found

### Execute a connector action by slug

```http
POST /v2/connectors/{connector}/actions/{action}/execute
```

Runs one action, addressed by connector and action slug, with the resolved connection's credentials and returns its output. The connection is chosen by connectionId if given, else by installationId's connection map, else the default connection of the caller's org (connectionOrgId / userId narrow it). mockMode answers from the action's mock stubs and uses no credential. Missing required input fields are a 400. Requires connectors.read.

Operation: `executeConnectorActionBySlug`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connector` | path | string | Yes | Connector slug |
| `action` | path | string | Yes | Action slug |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `input` | `object` | No | Action input, validated against its inputContract. Default {}. |
| `connectionId` | `string` | No | Run with exactly this connection. |
| `installationId` | `string` | No | Resolve the connection from this installation's connection map. |
| `connectionOrgId` | `string` | No | Org whose connection to use, when acting for a customer. |
| `userId` | `string` | No | Prefer this user's connection. |
| `mockMode` | `boolean` | No | Serve the response from mock stubs instead of calling the provider. |
| `version` | `string` | No | Pin the connector's internal version. |
| `externalVersion` | `string` | No | Pin the action's external (provider API) version. apiVersion is accepted as an alias. |
| `versionMajor` | `integer or string` | No | Pin the action's breaking revision. A non-integer is a 400. |
| `orgScope` | `string` | No | managed resolves only the platform catalog connector; custom only the caller's own. One of: `managed`, `custom`. |

**Responses**

* `200`: { data: { id, output, success, status, durationMs, warnings? } }
* `400`: Invalid JSON, invalid version pin, missing required input, or the action lacks the configuration its protocol needs
* `404`: Connector, action or connection not found

### Get an action's input/output contract

```http
GET /v2/connectors/{connector}/actions/{action}/schema
```

Returns an action's inputContract and outputContract (JSON Schema) without executing it. Requires connectors.read.

Operation: `getConnectorActionSchema`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connector` | path | string | Yes | Connector slug |
| `action` | path | string | Yes | Action slug |

**Responses**

* `200`: { data: { slug, name, inputContract, outputContract } }
* `404`: Connector or action not found

### Is this connector connected?

```http
GET /v2/connectors/{connector}/connection-status
```

Says whether the caller's org (or customer) has an ACTIVE or EXPIRED connection for the connector, preferring an ACTIVE one, and returns it. An unknown connector answers connected=false rather than 404. Requires connectors.read.

Operation: `getConnectorConnectionStatus`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connector` | path | string | Yes | Connector slug |

**Responses**

* `200`: { data: { connected: false } } or { data: { connected: true, connection: { id, name, status, connectorId } } }

### Discover an MCP connector's tools

```http
GET /v2/connectors/{connector}/mcp/discover
```

Connects to an MCP-protocol connector's server and lists the tools it exposes. 400 when the connector is not an MCP connector. Requires connectors.read.

Operation: `discoverMcpConnectorTools`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connector` | path | string | Yes | Connector slug |

**Responses**

* `200`: { data: { tools } }
* `400`: Not an MCP connector
* `404`: Connector not found
* `502`: MCP server unreachable

## Actions

### List actions

```http
GET /v1/actions
```

Actions of the connectors visible to the caller, or of one connector. The default light view omits contracts; view=contracts adds input/output contracts and view=full returns everything (use it only for a single connector). deleted=true (the trash) needs connectors.delete. Requires connectors.read.

Operation: `listActions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | query | string | No |  |
| `search` | query | string | No | Match on name/slug. |
| `slugs` | query | string | No | Comma-separated exact slugs. |
| `view` | query | string | No | One of: `light`, `contracts`, `full`. |
| `order` | query | string | No | resolver: the version-resolution order instead of by name. One of: `resolver`. |
| `includeDeleted` | query | boolean | No |  |
| `deleted` | query | boolean | No | Trash view: only soft-deleted actions. |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |

**Responses**

* `200`: { data: [action], pagination? }

### Create an action

```http
POST /v1/actions
```

The contract linter may refuse a bodyTemplate that does not match the inputContract (400). Requires connectors.create.

Operation: `createAction`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `slug` | `string` | Yes |  |
| `description` | `string` | No |  |
| `type` | `string` | Yes | One of: `HTTP`, `GRPC`, `FTP`, `LAMBDA`, `DB`. |
| `method` | `string` | No | One of: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `PROPFIND`, `MKCOL`, `MOVE`, `COPY`, `LOCK`, `UNLOCK`. |
| `path` | `string` | No |  |
| `headers` | `object` | No |  |
| `queryParams` | `object` | No |  |
| `bodyTemplate` | `string` | No |  |
| `httpConfig` | `object` | No |  |
| `httpConfig.url` | `string` | Yes |  |
| `httpConfig.method` | `string` | Yes | One of: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `PROPFIND`, `MKCOL`, `MOVE`, `COPY`, `LOCK`, `UNLOCK`. |
| `httpConfig.path` | `string` | No |  |
| `httpConfig.headers` | `object` | No |  |
| `httpConfig.queryParams` | `object` | No |  |
| `httpConfig.body` | `any` | No |  |
| `httpConfig.bodyType` | `string` | No | One of: `none`, `json`, `text`, `raw`, `form-data`, `form-urlencoded`, `binary`, `multipart-related`, `graphql`. |
| `httpConfig.bodyTemplate` | `any` | No |  |
| `grpcConfig` | `object` | No |  |
| `grpcConfig.target` | `string` | Yes |  |
| `grpcConfig.serviceName` | `string` | Yes |  |
| `grpcConfig.methodName` | `string` | Yes |  |
| `grpcConfig.jsonRequest` | `object` | No |  |
| `grpcConfig.metadata` | `object[]` | No |  |
| `grpcConfig.metadata[].key` | `string` | Yes |  |
| `grpcConfig.metadata[].value` | `string` | Yes |  |
| `grpcConfig.authConfig` | `object` | No |  |
| `grpcConfig.timeout` | `integer` | No |  |
| `ftpConfig` | `object` | No |  |
| `ftpConfig.operation` | `string` | Yes | One of: `list`, `download`, `upload`, `delete`, `rename`, `mkdir`, `exists`. |
| `ftpConfig.remotePath` | `string` | Yes |  |
| `ftpConfig.transferMode` | `string` | No | One of: `binary`, `ascii`. |
| `ftpConfig.renameTo` | `string` | No |  |
| `redisConfig` | `object` | No |  |
| `redisConfig.operation` | `string` | Yes | One of: `get`, `set`, `del`, `exists`, `expire`, `ttl`, `keys`, `incr`, `decr`, `mget`, `mset`, `hget`, `hset`, `hgetall`, `hdel`, `lpush`, `rpush`, `lpop`, `rpop`, `lrange`, `llen`, `publish`, `incrby`, `setnx`, `hmget`, `hmset`, `hexists`, `hincrby`, `hlen`, `ltrim`, `lrem`, `lindex`, `sadd`, `srem`, `smembers`, `sismember`, `scard`, `zadd`, `zrem`, `zrange`, `zrangebyscore`, `zscore`, `zcard`, `persist`, `type`, `ping`. |
| `redisConfig.key` | `string` | No |  |
| `redisConfig.field` | `string` | No |  |
| `redisConfig.value` | `string` | No |  |
| `redisConfig.ttl` | `integer` | No |  |
| `redisConfig.start` | `integer` | No |  |
| `redisConfig.stop` | `integer` | No |  |
| `redisConfig.pattern` | `string` | No |  |
| `redisConfig.channel` | `string` | No |  |
| `redisConfig.values` | `string[]` | No |  |
| `redisConfig.member` | `string` | No |  |
| `redisConfig.members` | `string[]` | No |  |
| `redisConfig.score` | `number` | No |  |
| `redisConfig.min` | `string` | No |  |
| `redisConfig.max` | `string` | No |  |
| `redisConfig.count` | `integer` | No |  |
| `redisConfig.amount` | `integer` | No |  |
| `redisConfig.fields` | `string[]` | No |  |
| `lambdaConfig` | `object` | No |  |
| `lambdaConfig.functionArn` | `string` | Yes |  |
| `lambdaConfig.region` | `string` | No |  |
| `lambdaConfig.payload` | `object` | No |  |
| `lambdaConfig.invocationType` | `string` | No | One of: `RequestResponse`, `Event`, `DryRun`. |
| `dbConfig` | `object` | No |  |
| `dbConfig.operation` | `string` | Yes | One of: `query`. |
| `dbConfig.dbType` | `string` | Yes | One of: `postgres`, `redshift`, `mysql`, `mssql`, `mongodb`. |
| `dbConfig.query` | `string` | No |  |
| `authConfig` | `object` | No |  |
| `inputContract` | `object` | No |  |
| `inputContract.type` | `string` | Yes | Always `object`. |
| `inputContract.properties` | `object` | Yes |  |
| `inputContract.required` | `string[]` | No |  |
| `outputContract` | `object` | No |  |
| `outputContract.type` | `string` | Yes | Always `object`. |
| `outputContract.properties` | `object` | Yes |  |
| `outputContract.required` | `string[]` | No |  |
| `language` | `string` | No | One of: `PYTHON`, `JS`. |
| `code` | `string` | No |  |
| `rateLimit` | `object` | No |  |
| `rateLimit.enabled` | `boolean` | Yes |  |
| `rateLimit.limits` | `object[]` | Yes |  |
| `rateLimit.limits[].requests` | `integer` | Yes |  |
| `rateLimit.limits[].strategy` | `string` | Yes | One of: `FIXED_WINDOW`, `SLIDING_WINDOW`, `CONCURRENCY`. |
| `rateLimit.limits[].window` | `integer` | Yes |  |
| `rateLimit.limits[].burstLimit` | `integer` | No |  |
| `stage` | `string` | No | One of: `test`, `live`. |
| `folderId` | `string` | No |  |
| `externalVersion` | `string` | No |  |
| `apiVersion` | `string` | No |  |
| `isDefaultExternalVersion` | `boolean` | No |  |
| `versionMajor` | `integer` | No |  |
| `submissionNote` | `string` | No |  |

**Responses**

* `201`: Created action
* `400`: Validation or contract-lint error
* `404`: Not found

### Delete several actions

```http
POST /v1/actions/batch-delete
```

Soft-deletes the given actions (hard=true deletes permanently) and returns the ids actually deleted; ids the caller may not delete are skipped. Requires connectors.delete.

Operation: `batchDeleteActions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `hard` | query | boolean | No |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | `string[]` | Yes |  |

**Responses**

* `200`: Deleted ids
* `400`: ids missing or empty

### Export a connector's actions

```http
GET /v1/actions/export
```

All actions of a connector in the fastn export format (re-importable with importActions). Requires connectors.read.

Operation: `exportActions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | query | string | Yes |  |

**Responses**

* `200`: Export
* `400`: connectorId missing
* `404`: Not found

### Import actions

```http
POST /v1/actions/import
```

Imports actions from an OpenAPI/Swagger, Postman, API Blueprint, hub/marketplace or fastn-export spec, given by url, by content, or as the request body itself. preview returns the parsed actions without creating them. Requires connectors.create.

Operation: `importActions`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `url` | `string` | No | Public URL of the spec to fetch (https:// is assumed when no scheme is given). |
| `content` | `string` | No | The spec as a string (JSON or YAML). |
| `format` | `string` | No | Format hint; detected when omitted. One of: `openapi`, `postman`, `hub`, `fastn`. |
| `baseUrl` | `string` | No | Overrides the spec's server URL. |
| `conflictResolution` | `string` | No | What to do when an action slug already exists. One of: `skip`, `overwrite`, `rename`. Default: `"skip"`. |
| `preview` | `boolean` | No | Parse and return the actions without creating them. |
| `selectedSlugs` | `string[]` | No | Import only these slugs. |

**Responses**

* `200`: Per-action results (created, skipped, overwritten, renamed, error), or the preview
* `400`: Invalid JSON, no connectorId, unparseable spec or a private URL
* `404`: Not found

### Get an action

```http
GET /v1/actions/{id}
```

Reads one action with its contracts and request configuration. Requires connectors.read.

Operation: `getAction`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Action
* `404`: Not found

### Update an action

```http
PUT /v1/actions/{id}
```

Updates an action of a connector the caller's org owns. The contract linter may refuse a bodyTemplate that does not match the inputContract (400). Requires connectors.update.

Operation: `updateAction`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `description` | `string` | Yes |  |
| `authMethodId` | `string` | No |  |
| `authConfig` | `object` | No |  |
| `inputContract` | `object` | No |  |
| `inputContract.type` | `string` | Yes | Always `object`. |
| `inputContract.properties` | `object` | Yes |  |
| `inputContract.required` | `string[]` | No |  |
| `outputContract` | `object` | No |  |
| `outputContract.type` | `string` | Yes | Always `object`. |
| `outputContract.properties` | `object` | Yes |  |
| `outputContract.required` | `string[]` | No |  |
| `httpConfig` | `object` | No |  |
| `httpConfig.url` | `string` | Yes |  |
| `httpConfig.method` | `string` | Yes | One of: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `PROPFIND`, `MKCOL`, `MOVE`, `COPY`, `LOCK`, `UNLOCK`. |
| `httpConfig.path` | `string` | No |  |
| `httpConfig.headers` | `object` | No |  |
| `httpConfig.queryParams` | `object` | No |  |
| `httpConfig.body` | `any` | No |  |
| `httpConfig.bodyType` | `string` | No | One of: `none`, `json`, `text`, `raw`, `form-data`, `form-urlencoded`, `binary`, `multipart-related`, `graphql`. |
| `httpConfig.bodyTemplate` | `any` | No |  |
| `grpcConfig` | `object` | No |  |
| `grpcConfig.target` | `string` | Yes |  |
| `grpcConfig.serviceName` | `string` | Yes |  |
| `grpcConfig.methodName` | `string` | Yes |  |
| `grpcConfig.jsonRequest` | `object` | No |  |
| `grpcConfig.metadata` | `object[]` | No |  |
| `grpcConfig.metadata[].key` | `string` | Yes |  |
| `grpcConfig.metadata[].value` | `string` | Yes |  |
| `grpcConfig.authConfig` | `object` | No |  |
| `grpcConfig.timeout` | `integer` | No |  |
| `ftpConfig` | `object` | No |  |
| `ftpConfig.operation` | `string` | Yes | One of: `list`, `download`, `upload`, `delete`, `rename`, `mkdir`, `exists`. |
| `ftpConfig.remotePath` | `string` | Yes |  |
| `ftpConfig.transferMode` | `string` | No | One of: `binary`, `ascii`. |
| `ftpConfig.renameTo` | `string` | No |  |
| `redisConfig` | `object` | No |  |
| `redisConfig.operation` | `string` | Yes | One of: `get`, `set`, `del`, `exists`, `expire`, `ttl`, `keys`, `incr`, `decr`, `mget`, `mset`, `hget`, `hset`, `hgetall`, `hdel`, `lpush`, `rpush`, `lpop`, `rpop`, `lrange`, `llen`, `publish`, `incrby`, `setnx`, `hmget`, `hmset`, `hexists`, `hincrby`, `hlen`, `ltrim`, `lrem`, `lindex`, `sadd`, `srem`, `smembers`, `sismember`, `scard`, `zadd`, `zrem`, `zrange`, `zrangebyscore`, `zscore`, `zcard`, `persist`, `type`, `ping`. |
| `redisConfig.key` | `string` | No |  |
| `redisConfig.field` | `string` | No |  |
| `redisConfig.value` | `string` | No |  |
| `redisConfig.ttl` | `integer` | No |  |
| `redisConfig.start` | `integer` | No |  |
| `redisConfig.stop` | `integer` | No |  |
| `redisConfig.pattern` | `string` | No |  |
| `redisConfig.channel` | `string` | No |  |
| `redisConfig.values` | `string[]` | No |  |
| `redisConfig.member` | `string` | No |  |
| `redisConfig.members` | `string[]` | No |  |
| `redisConfig.score` | `number` | No |  |
| `redisConfig.min` | `string` | No |  |
| `redisConfig.max` | `string` | No |  |
| `redisConfig.count` | `integer` | No |  |
| `redisConfig.amount` | `integer` | No |  |
| `redisConfig.fields` | `string[]` | No |  |
| `lambdaConfig` | `object` | No |  |
| `lambdaConfig.functionArn` | `string` | Yes |  |
| `lambdaConfig.region` | `string` | No |  |
| `lambdaConfig.payload` | `object` | No |  |
| `lambdaConfig.invocationType` | `string` | No | One of: `RequestResponse`, `Event`, `DryRun`. |
| `dbConfig` | `object` | No |  |
| `dbConfig.operation` | `string` | Yes | One of: `query`. |
| `dbConfig.dbType` | `string` | Yes | One of: `postgres`, `redshift`, `mysql`, `mssql`, `mongodb`. |
| `dbConfig.query` | `string` | No |  |
| `language` | `string` | No |  |
| `code` | `string` | No |  |
| `rateLimit` | `object` | No |  |
| `rateLimit.enabled` | `boolean` | Yes |  |
| `rateLimit.limits` | `object[]` | Yes |  |
| `rateLimit.limits[].requests` | `integer` | Yes |  |
| `rateLimit.limits[].strategy` | `string` | Yes | One of: `FIXED_WINDOW`, `SLIDING_WINDOW`, `CONCURRENCY`. |
| `rateLimit.limits[].window` | `integer` | Yes |  |
| `rateLimit.limits[].burstLimit` | `integer` | No |  |
| `stage` | `string` | No | One of: `test`, `live`. |
| `commit` | `string` | No |  |
| `folderId` | `string` | No |  |
| `externalVersion` | `string` | No |  |
| `apiVersion` | `string` | No |  |
| `isDefaultExternalVersion` | `boolean` | No |  |
| `deprecated` | `boolean` | No |  |
| `sunsetAt` | `string` | No |  |
| `successorActionId` | `string` | No |  |

**Responses**

* `200`: Updated action
* `400`: Validation or contract-lint error
* `404`: Not found

### Delete an action

```http
DELETE /v1/actions/{id}
```

Soft-deletes an action (restorable with restoreAction); hard=true deletes it permanently. Requires connectors.delete.

Operation: `deleteAction`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `hard` | query | boolean | No |  |

**Responses**

* `200`: Deleted
* `404`: Not found

### Execute a connector action

```http
POST /v1/actions/{id}/execute
```

Runs one action by id against a connection and returns the provider's response. The gateway forwards the body unchanged to the connector runtime, which requires connectors.read. Name the connection with connectorId + connectionName, or pin it with connectionId / installationId; mockMode runs a stub instead of calling the provider.

Operation: `executeAction`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | No | Connector the action belongs to. Required unless mockMode is true. |
| `connectionName` | `string` | No | Display name of the connection to run with. Required unless mockMode is true. |
| `connectionId` | `string` | No | Pin an exact connection. A hard constraint: an unusable id fails rather than falling back. |
| `installationId` | `string` | No | Run with the connection bound to this installation. |
| `userId` | `string` | No | Run with this user's connection. |
| `input` | `object` | No | Action input, validated against the action's inputContract. |
| `externalVersion` | `string` | No | External contract version of the action to run. |
| `versionMajor` | `integer or string` | No | Internal major version of the action to run. |
| `mockMode` | `boolean` | No | Run against the action's mock stubs instead of the provider. No credential is used. |

**Responses**

* `200`: Action output
* `400`: Invalid JSON, missing connectorId/connectionName, or the action has no runnable configuration
* `404`: Action or connection not found
* `500`: Upstream failure

### Export one action

```http
GET /v1/actions/{id}/export
```

One action in the fastn export format. Requires connectors.read.

Operation: `exportAction`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Export
* `404`: Not found

### Generate a mock response

```http
POST /v1/actions/{id}/mock
```

Validates the body against the action's inputContract and returns a response generated from its outputContract, without calling the provider. 400 lists the input contract violations. Requires connectors.read.

Operation: `mockAction`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Mock output
* `400`: Invalid JSON or input contract violations
* `404`: Not found

### Save a response as a mock stub

```http
POST /v1/actions/{id}/mock-stub
```

Stores a recorded request/response pair as the action's live-capture mock stub, for mockMode executions, replacing any earlier live capture of that action. A capture someone has since edited (input matchers or response) is kept. The action must belong to the caller or the caller's org, and connectorId must be its connector. Requires connectors.update.

Operation: `saveActionMockStub`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `method` | `string` | No |  |
| `requestBody` | `any` | No |  |
| `responseStatus` | `number` | Yes |  |
| `responseBody` | `any` | No |  |

**Responses**

* `200`: Stub
* `400`: connectorId is not this action's connector
* `403`: Action is not writable in this scope

### Fork a new action version

```http
POST /v1/actions/{id}/new-version
```

Forks an action into a new major version (bump=major) or onto a new external API contract version (bump=external). Requires connectors.create.

Operation: `createActionVersion`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `bump` | `string` | Yes | One of: `major`, `external`. |
| `externalVersion` | `string` | No |  |
| `makeDefault` | `boolean` | No |  |
| `deprecatePrevious` | `boolean` | No |  |
| `sunsetAt` | `string` | No |  |

**Responses**

* `201`: New action version
* `400`: Validation error
* `404`: Not found
* `409`: That version already exists

### Promote an action to live

```http
POST /v1/actions/{id}/promote
```

Moves an action from test to live. 400 when it is already live. Requires connectors.update.

Operation: `promoteAction`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Promoted action
* `400`: Already live
* `404`: Not found

### Propose a change to a managed action

```http
POST /v1/actions/{id}/propose-update
```

Submits a change to a Fastn-managed (org_platform) action for platform review instead of editing it. Requires connectors.create.

Operation: `proposeActionUpdate`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `description` | `string` | Yes |  |
| `authMethodId` | `string` | No |  |
| `authConfig` | `object` | No |  |
| `inputContract` | `object` | No |  |
| `inputContract.type` | `string` | Yes | Always `object`. |
| `inputContract.properties` | `object` | Yes |  |
| `inputContract.required` | `string[]` | No |  |
| `outputContract` | `object` | No |  |
| `outputContract.type` | `string` | Yes | Always `object`. |
| `outputContract.properties` | `object` | Yes |  |
| `outputContract.required` | `string[]` | No |  |
| `httpConfig` | `object` | No |  |
| `httpConfig.url` | `string` | Yes |  |
| `httpConfig.method` | `string` | Yes | One of: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `PROPFIND`, `MKCOL`, `MOVE`, `COPY`, `LOCK`, `UNLOCK`. |
| `httpConfig.path` | `string` | No |  |
| `httpConfig.headers` | `object` | No |  |
| `httpConfig.queryParams` | `object` | No |  |
| `httpConfig.body` | `any` | No |  |
| `httpConfig.bodyType` | `string` | No | One of: `none`, `json`, `text`, `raw`, `form-data`, `form-urlencoded`, `binary`, `multipart-related`, `graphql`. |
| `httpConfig.bodyTemplate` | `any` | No |  |
| `grpcConfig` | `object` | No |  |
| `grpcConfig.target` | `string` | Yes |  |
| `grpcConfig.serviceName` | `string` | Yes |  |
| `grpcConfig.methodName` | `string` | Yes |  |
| `grpcConfig.jsonRequest` | `object` | No |  |
| `grpcConfig.metadata` | `object[]` | No |  |
| `grpcConfig.metadata[].key` | `string` | Yes |  |
| `grpcConfig.metadata[].value` | `string` | Yes |  |
| `grpcConfig.authConfig` | `object` | No |  |
| `grpcConfig.timeout` | `integer` | No |  |
| `ftpConfig` | `object` | No |  |
| `ftpConfig.operation` | `string` | Yes | One of: `list`, `download`, `upload`, `delete`, `rename`, `mkdir`, `exists`. |
| `ftpConfig.remotePath` | `string` | Yes |  |
| `ftpConfig.transferMode` | `string` | No | One of: `binary`, `ascii`. |
| `ftpConfig.renameTo` | `string` | No |  |
| `redisConfig` | `object` | No |  |
| `redisConfig.operation` | `string` | Yes | One of: `get`, `set`, `del`, `exists`, `expire`, `ttl`, `keys`, `incr`, `decr`, `mget`, `mset`, `hget`, `hset`, `hgetall`, `hdel`, `lpush`, `rpush`, `lpop`, `rpop`, `lrange`, `llen`, `publish`, `incrby`, `setnx`, `hmget`, `hmset`, `hexists`, `hincrby`, `hlen`, `ltrim`, `lrem`, `lindex`, `sadd`, `srem`, `smembers`, `sismember`, `scard`, `zadd`, `zrem`, `zrange`, `zrangebyscore`, `zscore`, `zcard`, `persist`, `type`, `ping`. |
| `redisConfig.key` | `string` | No |  |
| `redisConfig.field` | `string` | No |  |
| `redisConfig.value` | `string` | No |  |
| `redisConfig.ttl` | `integer` | No |  |
| `redisConfig.start` | `integer` | No |  |
| `redisConfig.stop` | `integer` | No |  |
| `redisConfig.pattern` | `string` | No |  |
| `redisConfig.channel` | `string` | No |  |
| `redisConfig.values` | `string[]` | No |  |
| `redisConfig.member` | `string` | No |  |
| `redisConfig.members` | `string[]` | No |  |
| `redisConfig.score` | `number` | No |  |
| `redisConfig.min` | `string` | No |  |
| `redisConfig.max` | `string` | No |  |
| `redisConfig.count` | `integer` | No |  |
| `redisConfig.amount` | `integer` | No |  |
| `redisConfig.fields` | `string[]` | No |  |
| `lambdaConfig` | `object` | No |  |
| `lambdaConfig.functionArn` | `string` | Yes |  |
| `lambdaConfig.region` | `string` | No |  |
| `lambdaConfig.payload` | `object` | No |  |
| `lambdaConfig.invocationType` | `string` | No | One of: `RequestResponse`, `Event`, `DryRun`. |
| `dbConfig` | `object` | No |  |
| `dbConfig.operation` | `string` | Yes | One of: `query`. |
| `dbConfig.dbType` | `string` | Yes | One of: `postgres`, `redshift`, `mysql`, `mssql`, `mongodb`. |
| `dbConfig.query` | `string` | No |  |
| `language` | `string` | No |  |
| `code` | `string` | No |  |
| `rateLimit` | `object` | No |  |
| `rateLimit.enabled` | `boolean` | Yes |  |
| `rateLimit.limits` | `object[]` | Yes |  |
| `rateLimit.limits[].requests` | `integer` | Yes |  |
| `rateLimit.limits[].strategy` | `string` | Yes | One of: `FIXED_WINDOW`, `SLIDING_WINDOW`, `CONCURRENCY`. |
| `rateLimit.limits[].window` | `integer` | Yes |  |
| `rateLimit.limits[].burstLimit` | `integer` | No |  |
| `submissionNote` | `string` | No |  |

**Responses**

* `201`: Proposal created
* `400`: Validation error
* `403`: Not a managed action, or not allowed to propose
* `404`: Not found
* `409`: A proposal is already pending

### Restore a soft-deleted action

```http
POST /v1/actions/{id}/restore
```

Restores a soft-deleted action from the trash. Requires connectors.delete.

Operation: `restoreAction`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Restored
* `404`: Not found
* `409`: Parent connector is still soft-deleted

### Get an action's review

```http
GET /v1/actions/{id}/review
```

Review status and comments of an action submitted for platform review.  Requires connectors.read; the caller's org must own the action.

Operation: `getActionReview`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Review
* `403`: Not the owning org
* `404`: Not found

### Comment on an action review

```http
POST /v1/actions/{id}/review/comments
```

Adds a comment (max 1000 characters) to an action's review thread. Requires connectors.read; the caller's org must own the action.

Operation: `createActionReviewComment`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `body` | `string` | Yes |  |

**Responses**

* `201`: Comment
* `400`: body missing
* `404`: Not found

### Record an action test result

```http
PATCH /v1/actions/{id}/test-result
```

Stamps an action as passed or failed with the evidence of the test run. Requires connectors.update.

Operation: `setActionTestResult`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `testStatus` | `string` | Yes | One of: `passed`, `failed`. |
| `lastTestEvidence` | `object` | No |  |

**Responses**

* `200`: Updated action
* `404`: Not found

### List action versions

```http
GET /v1/actions/{id}/versions
```

Version history of an action. Requires connectors.read.

Operation: `listActionVersions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Versions
* `404`: Not found

### Get an action version

```http
GET /v1/actions/{id}/versions/{versionId}
```

One version of an action. Requires connectors.read.

Operation: `getActionVersion`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `versionId` | path | string | Yes |  |

**Responses**

* `200`: Version
* `404`: Not found

## Action folders

### List action folders

```http
GET /v1/action-folders
```

Lists the org's action folders, alphabetically. Requires connectors.read.

Operation: `listActionFolders`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | query | string | No | Only folders of this connector. |

**Responses**

* `200`: { data: [folder], total }

### Create an action folder

```http
POST /v1/action-folders
```

Creates a folder to group a connector's actions; parentId nests it. Requires connectors.create.

Operation: `createActionFolder`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `description` | `string` | No |  |
| `parentId` | `string` | No |  |

**Responses**

* `201`: Created folder
* `400`: Validation error

### Get an action folder

```http
GET /v1/action-folders/{id}
```

Reads one of the org's action folders. Requires connectors.read.

Operation: `getActionFolder`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Folder
* `404`: Not found

### Update an action folder

```http
PUT /v1/action-folders/{id}
```

Renames, re-describes or re-parents a folder. Requires connectors.update.

Operation: `updateActionFolder`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `parentId` | `string` | No |  |

**Responses**

* `200`: Updated folder
* `404`: Not found

### Delete an action folder

```http
DELETE /v1/action-folders/{id}
```

Deletes a folder; its actions stay and become unfiled. Requires connectors.delete.

Operation: `deleteActionFolder`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: { id, deleted: true } }
* `404`: Not found

## Auth methods

### List auth methods

```http
GET /v1/auth-methods
```

Auth methods of the connectors visible to the caller, or of one connector. Requires connectors.read.

Operation: `listAuthMethods`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | query | string | No |  |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |

**Responses**

* `200`: { data: [authMethod] }

### Create an auth method

```http
POST /v1/auth-methods
```

Adds an auth method (OAuth2, API key, Basic, Bearer, JWT, AWS SigV4, INPUT, ...) to a connector. Requires connectors.create.

Operation: `createAuthMethod`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `type` | `string` | Yes | One of: `NO_AUTH`, `BASIC`, `DIGEST`, `BEARER`, `API_KEY`, `OAUTH`, `INPUT`, `JWT_BEARER`, `AWS_SIGNATURE`, `OAUTH_1`, `OAUTH_2`. |
| `title` | `string` | Yes |  |
| `isDefault` | `boolean` | No |  |
| `inputContract` | `object` | No |  |
| `inputContract.type` | `string` | Yes | Always `object`. |
| `inputContract.properties` | `object` | Yes |  |
| `inputContract.required` | `string[]` | No |  |
| `authConfig` | `object` | No |  |
| `authConfig.clientId` | `string` | No |  |
| `authConfig.clientSecret` | `string` | No |  |
| `authConfig.accessType` | `string` | No |  |
| `authConfig.responseType` | `string` | No |  |
| `authConfig.prompt` | `string` | No |  |
| `authConfig.apiKeyName` | `string` | No |  |
| `authConfig.userName` | `string` | No |  |
| `authConfig.authorizationUrl` | `string` | No |  |
| `authConfig.tokenUrl` | `string` | No |  |
| `authConfig.scopes` | `string[]` | No |  |
| `authConfig.grantType` | `string` | No |  |
| `authConfig.clientAuthMethod` | `string` | No | One of: `basic`, `body`. |
| `authConfig.bodyFormat` | `string` | No | One of: `form`, `json`. |
| `authConfig.tokenRequestHeaders` | `object` | No |  |
| `authConfig.tokenParams` | `object` | No |  |
| `authConfig.pkce` | `boolean` | No |  |
| `authConfig.tokenExpiry` | `integer` | No |  |
| `authConfig.rotation` | `string` | No | One of: `none`, `always`, `detect`. |
| `authConfig.authorization` | `object` | No |  |
| `authConfig.authorization.grantType` | `string` | No |  |
| `authConfig.authorization.tokenUrl` | `string` | No |  |
| `authConfig.authorization.tokenGrantType` | `string` | No |  |
| `authConfig.authorization.tokenRequestMethod` | `string` | No | One of: `GET`, `POST`. |
| `authConfig.authorization.tokenParamsIn` | `string` | No | One of: `body`, `query`. |
| `authConfig.authorization.tokenResponsePath` | `string` | No |  |
| `authConfig.authorization.tokenParamNames` | `object` | No |  |
| `authConfig.authorization.tokenExpiresInField` | `string` | No |  |
| `authConfig.authorization.refreshTokenUrl` | `string` | No |  |
| `authConfig.params` | `object` | No |  |
| `authConfig.params.scope` | `string` | No |  |
| `authConfig.params.response_type` | `string` | No |  |
| `authConfig.params.access_type` | `string` | No |  |
| `authConfig.params.prompt` | `string` | No |  |
| `authConfig.requiredAttributes` | `string` | No |  |
| `authConfig.requestSigning` | `object` | No |  |
| `authConfig.requestSigning.algorithm` | `string` | Yes | One of: `HMAC-SHA256`, `HMAC-SHA1`, `HMAC-SHA512`. |
| `authConfig.requestSigning.encoding` | `string` | No | One of: `hex`, `base64`. |
| `authConfig.requestSigning.secretField` | `string` | Yes |  |
| `authConfig.requestSigning.injectParams` | `object` | No |  |
| `authConfig.requestSigning.canonical` | `object` | Yes |  |
| `authConfig.requestSigning.canonical.prefix` | `string` | No |  |
| `authConfig.requestSigning.canonical.suffix` | `string` | No |  |
| `authConfig.requestSigning.canonical.includeMethod` | `boolean` | No |  |
| `authConfig.requestSigning.canonical.includePath` | `boolean` | No |  |
| `authConfig.requestSigning.canonical.includeSortedQuery` | `boolean` | No |  |
| `authConfig.requestSigning.canonical.querySeparator` | `string` | No |  |
| `authConfig.requestSigning.canonical.excludeParams` | `string[]` | No |  |
| `authConfig.requestSigning.canonical.includeBody` | `boolean` | No |  |
| `authConfig.requestSigning.canonical.bodySkipMethods` | `string[]` | No |  |
| `authConfig.requestSigning.expiresInSeconds` | `integer` | No |  |
| `authConfig.requestSigning.output` | `object` | Yes |  |
| `authConfig.requestSigning.output.in` | `string` | Yes | One of: `query`, `header`. |
| `authConfig.requestSigning.output.name` | `string` | Yes |  |
| `authConfig.requestSigning.output.template` | `string` | No |  |
| `authProviderId` | `string` | No |  |
| `docsUrl` | `string` | No |  |

**Responses**

* `201`: Created auth method
* `400`: Validation error

### Get an auth method

```http
GET /v1/auth-methods/{id}
```

Reads one auth method. Requires connectors.read.

Operation: `getAuthMethod`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Auth method
* `404`: Not found

### Update an auth method

```http
PUT /v1/auth-methods/{id}
```

Updates an auth method of a connector the caller's org owns. Requires connectors.update.

Operation: `updateAuthMethod`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No |  |
| `type` | `string` | No | One of: `NO_AUTH`, `BASIC`, `DIGEST`, `BEARER`, `API_KEY`, `OAUTH`, `INPUT`, `JWT_BEARER`, `AWS_SIGNATURE`, `OAUTH_1`, `OAUTH_2`. |
| `title` | `string` | No |  |
| `isDefault` | `boolean` | No |  |
| `inputContract` | `object` | No |  |
| `inputContract.type` | `string` | Yes | Always `object`. |
| `inputContract.properties` | `object` | Yes |  |
| `inputContract.required` | `string[]` | No |  |
| `authConfig` | `object` | No |  |
| `authConfig.clientId` | `string` | No |  |
| `authConfig.clientSecret` | `string` | No |  |
| `authConfig.accessType` | `string` | No |  |
| `authConfig.responseType` | `string` | No |  |
| `authConfig.prompt` | `string` | No |  |
| `authConfig.apiKeyName` | `string` | No |  |
| `authConfig.userName` | `string` | No |  |
| `authConfig.authorizationUrl` | `string` | No |  |
| `authConfig.tokenUrl` | `string` | No |  |
| `authConfig.scopes` | `string[]` | No |  |
| `authConfig.grantType` | `string` | No |  |
| `authConfig.clientAuthMethod` | `string` | No | One of: `basic`, `body`. |
| `authConfig.bodyFormat` | `string` | No | One of: `form`, `json`. |
| `authConfig.tokenRequestHeaders` | `object` | No |  |
| `authConfig.tokenParams` | `object` | No |  |
| `authConfig.pkce` | `boolean` | No |  |
| `authConfig.tokenExpiry` | `integer` | No |  |
| `authConfig.rotation` | `string` | No | One of: `none`, `always`, `detect`. |
| `authConfig.authorization` | `object` | No |  |
| `authConfig.authorization.grantType` | `string` | No |  |
| `authConfig.authorization.tokenUrl` | `string` | No |  |
| `authConfig.authorization.tokenGrantType` | `string` | No |  |
| `authConfig.authorization.tokenRequestMethod` | `string` | No | One of: `GET`, `POST`. |
| `authConfig.authorization.tokenParamsIn` | `string` | No | One of: `body`, `query`. |
| `authConfig.authorization.tokenResponsePath` | `string` | No |  |
| `authConfig.authorization.tokenParamNames` | `object` | No |  |
| `authConfig.authorization.tokenExpiresInField` | `string` | No |  |
| `authConfig.authorization.refreshTokenUrl` | `string` | No |  |
| `authConfig.params` | `object` | No |  |
| `authConfig.params.scope` | `string` | No |  |
| `authConfig.params.response_type` | `string` | No |  |
| `authConfig.params.access_type` | `string` | No |  |
| `authConfig.params.prompt` | `string` | No |  |
| `authConfig.requiredAttributes` | `string` | No |  |
| `authConfig.requestSigning` | `object` | No |  |
| `authConfig.requestSigning.algorithm` | `string` | Yes | One of: `HMAC-SHA256`, `HMAC-SHA1`, `HMAC-SHA512`. |
| `authConfig.requestSigning.encoding` | `string` | No | One of: `hex`, `base64`. |
| `authConfig.requestSigning.secretField` | `string` | Yes |  |
| `authConfig.requestSigning.injectParams` | `object` | No |  |
| `authConfig.requestSigning.canonical` | `object` | Yes |  |
| `authConfig.requestSigning.canonical.prefix` | `string` | No |  |
| `authConfig.requestSigning.canonical.suffix` | `string` | No |  |
| `authConfig.requestSigning.canonical.includeMethod` | `boolean` | No |  |
| `authConfig.requestSigning.canonical.includePath` | `boolean` | No |  |
| `authConfig.requestSigning.canonical.includeSortedQuery` | `boolean` | No |  |
| `authConfig.requestSigning.canonical.querySeparator` | `string` | No |  |
| `authConfig.requestSigning.canonical.excludeParams` | `string[]` | No |  |
| `authConfig.requestSigning.canonical.includeBody` | `boolean` | No |  |
| `authConfig.requestSigning.canonical.bodySkipMethods` | `string[]` | No |  |
| `authConfig.requestSigning.expiresInSeconds` | `integer` | No |  |
| `authConfig.requestSigning.output` | `object` | Yes |  |
| `authConfig.requestSigning.output.in` | `string` | Yes | One of: `query`, `header`. |
| `authConfig.requestSigning.output.name` | `string` | Yes |  |
| `authConfig.requestSigning.output.template` | `string` | No |  |
| `authProviderId` | `string` | No |  |
| `docsUrl` | `string` | No |  |

**Responses**

* `200`: Updated auth method
* `404`: Not found

### Delete an auth method

```http
DELETE /v1/auth-methods/{id}
```

Deletes an auth method. Requires connectors.delete.

Operation: `deleteAuthMethod`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `404`: Not found

## Auth providers

### List auth providers

```http
GET /v1/auth-providers
```

OAuth apps visible to the caller (its own org's and the shared catalog's), without client secrets. Requires connectors.read.

Operation: `listAuthProviders`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | query | string | No |  |
| `includeDeleted` | query | boolean | No |  |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |

**Responses**

* `200`: { data: [provider] }

### Create an auth provider

```http
POST /v1/auth-providers
```

Creates an OAuth app (client id/secret, URLs, scopes) a connector's OAuth auth method connects through. Without connectorId it is independent and reusable. A Fastn-managed connector's OAuth app cannot be replaced (403). Requires connectors.create.

Operation: `createAuthProvider`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | No |  |
| `name` | `string` | Yes |  |
| `slug` | `string` | No |  |
| `description` | `string` | No |  |
| `clientId` | `string` | No |  |
| `clientSecret` | `string` | No |  |
| `authorizationUrl` | `string` | No |  |
| `params` | `object` | No |  |
| `params.scope` | `string` | No |  |
| `params.response_type` | `string` | No |  |
| `authorization` | `object` | No |  |
| `authorization.tokenUrl` | `string` | No |  |
| `authorization.grantType` | `string` | No |  |
| `authorization.tokenGrantType` | `string` | No |  |
| `authorization.tokenRequestMethod` | `string` | No | One of: `GET`, `POST`. |
| `authorization.tokenParamsIn` | `string` | No | One of: `body`, `query`. |
| `authorization.tokenResponsePath` | `string` | No |  |
| `authorization.tokenParamNames` | `object` | No |  |
| `authorization.tokenExpiresInField` | `string` | No |  |
| `authorization.refreshTokenUrl` | `string` | No |  |
| `additionalFields` | `object` | No |  |
| `scopeConfig` | `object` | No |  |
| `scopeConfig.scopes` | `object[]` | Yes |  |
| `scopeConfig.scopes[].id` | `string` | Yes |  |
| `scopeConfig.scopes[].label` | `string` | No |  |
| `scopeConfig.scopes[].description` | `string` | No |  |
| `scopeConfig.scopes[].required` | `boolean` | No |  |
| `scopeConfig.scopes[].groupId` | `string` | No |  |
| `scopeConfig.groups` | `object[]` | No |  |
| `scopeConfig.groups[].id` | `string` | Yes |  |
| `scopeConfig.groups[].name` | `string` | Yes |  |
| `scopeConfig.groups[].description` | `string` | No |  |
| `scopeConfig.defaultScopes` | `string[]` | No |  |
| `scopeConfig.minimumScopes` | `string[]` | No |  |
| `scopeConfig.allowCustomScopes` | `boolean` | No |  |
| `oauthVariables` | `object[]` | No |  |
| `oauthVariables[].key` | `string` | Yes |  |
| `oauthVariables[].label` | `string` | Yes |  |
| `oauthVariables[].description` | `string` | No |  |
| `oauthVariables[].placeholder` | `string` | No |  |
| `oauthVariables[].defaultValue` | `string` | No |  |
| `oauthVariables[].hidden` | `boolean` | No |  |
| `isDefault` | `boolean` | No |  |
| `platformProviderId` | `string` | No |  |
| `pkce` | `boolean` | No |  |

**Responses**

* `201`: Created provider
* `400`: Validation error
* `403`: connectorId names a Fastn-managed connector

### Get an auth provider

```http
GET /v1/auth-providers/{id}
```

One OAuth app, without its client secret. Requires connectors.read.

Operation: `getAuthProvider`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Provider
* `404`: Not found

### Update an auth provider

```http
PUT /v1/auth-providers/{id}
```

Updates an OAuth app. Requires connectors.update.

Operation: `updateAuthProvider`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `clientId` | `string` | No |  |
| `clientSecret` | `string` | No |  |
| `pkce` | `boolean` | No |  |
| `authorizationUrl` | `string` | No |  |
| `params` | `object` | No |  |
| `params.scope` | `string` | No |  |
| `params.response_type` | `string` | No |  |
| `authorization` | `object` | No |  |
| `authorization.tokenUrl` | `string` | No |  |
| `authorization.grantType` | `string` | No |  |
| `authorization.tokenGrantType` | `string` | No |  |
| `authorization.tokenRequestMethod` | `string` | No | One of: `GET`, `POST`. |
| `authorization.tokenParamsIn` | `string` | No | One of: `body`, `query`. |
| `authorization.tokenResponsePath` | `string` | No |  |
| `authorization.tokenParamNames` | `object` | No |  |
| `authorization.tokenExpiresInField` | `string` | No |  |
| `authorization.refreshTokenUrl` | `string` | No |  |
| `additionalFields` | `object` | No |  |
| `scopeConfig` | `object` | No |  |
| `scopeConfig.scopes` | `object[]` | Yes |  |
| `scopeConfig.scopes[].id` | `string` | Yes |  |
| `scopeConfig.scopes[].label` | `string` | No |  |
| `scopeConfig.scopes[].description` | `string` | No |  |
| `scopeConfig.scopes[].required` | `boolean` | No |  |
| `scopeConfig.scopes[].groupId` | `string` | No |  |
| `scopeConfig.groups` | `object[]` | No |  |
| `scopeConfig.groups[].id` | `string` | Yes |  |
| `scopeConfig.groups[].name` | `string` | Yes |  |
| `scopeConfig.groups[].description` | `string` | No |  |
| `scopeConfig.defaultScopes` | `string[]` | No |  |
| `scopeConfig.minimumScopes` | `string[]` | No |  |
| `scopeConfig.allowCustomScopes` | `boolean` | No |  |
| `oauthVariables` | `object[]` | No |  |
| `oauthVariables[].key` | `string` | Yes |  |
| `oauthVariables[].label` | `string` | Yes |  |
| `oauthVariables[].description` | `string` | No |  |
| `oauthVariables[].placeholder` | `string` | No |  |
| `oauthVariables[].defaultValue` | `string` | No |  |
| `oauthVariables[].hidden` | `boolean` | No |  |
| `isDefault` | `boolean` | No |  |

**Responses**

* `200`: Updated provider
* `403`: Shared-catalog provider
* `404`: Not found

### Delete an auth provider

```http
DELETE /v1/auth-providers/{id}
```

Deletes an OAuth app. Requires connectors.delete.

Operation: `deleteAuthProvider`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `403`: Shared-catalog provider
* `404`: Not found

### List an auth provider's scopes

```http
GET /v1/auth-providers/{id}/scopes
```

The OAuth scopes (and scope groups) a provider offers for selection at connect time. Requires connectors.read.

Operation: `listAuthProviderScopes`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Scope configuration
* `404`: Not found

## Entities

### List connector entities

```http
GET /v1/entities
```

Entities defined on connectors. Requires connectors.read.

Operation: `listConnectorEntities`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | query | string | No |  |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |

**Responses**

* `200`: { data: [entity] }

### Create a connector entity

```http
POST /v1/entities
```

Defines a named entity (a data type such as Contact) on a connector. Requires connectors.create.

Operation: `createConnectorEntity`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `slug` | `string` | Yes |  |
| `description` | `string` | No |  |

**Responses**

* `201`: Created entity
* `400`: Validation error

### Get a connector entity

```http
GET /v1/entities/{id}
```

Reads one entity. Requires connectors.read.

Operation: `getConnectorEntity`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Entity
* `404`: Not found

### Update a connector entity

```http
PUT /v1/entities/{id}
```

Requires connectors.update.

Operation: `updateConnectorEntity`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `description` | `string` | No |  |

**Responses**

* `200`: Updated entity
* `404`: Not found

### Delete a connector entity

```http
DELETE /v1/entities/{id}
```

Requires connectors.delete.

Operation: `deleteConnectorEntity`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `404`: Not found

## Webhook configs

### List connectors with webhook triggers

```http
GET /v1/webhook-configs/connectors
```

Connectors that offer enabled webhook configs (app-event trigger sources) to the caller, with their events and required actions, ordered by name. Includes the parent org's when its catalog is enabled. Requires connectors.read.

Operation: `listWebhookConfigConnectors`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | query | string | No | Resolve exactly this connector, ignoring paging. |
| `search` | query | string | No |  |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |

**Responses**

* `200`: { data: [connector], pagination }

### Get a webhook config

```http
GET /v1/webhook-configs/{id}
```

One webhook config, including the provider's decrypted verification token when one was stored. Requires connectors.read.

Operation: `getWebhookConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Webhook config
* `404`: Not found

### Update a webhook config

```http
PUT /v1/webhook-configs/{id}
```

Requires connectors.update.

Operation: `updateWebhookConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | No | One of: `APP`, `EVENT_WEBHOOK`. |
| `subscription` | `string` | No |  |
| `unsubscription` | `string` | No |  |
| `resubscription` | `string` | No |  |
| `events` | `object[]` | No |  |
| `events[].id` | `string` | Yes |  |
| `events[].label` | `string` | Yes |  |
| `events[].description` | `string` | No |  |
| `events[].payloadSchema` | `any` | No |  |
| `inputs` | `object[]` | No |  |
| `inputs[].key` | `string` | Yes |  |
| `inputs[].value` | `string` | Yes |  |
| `inputs[].hidden` | `boolean` | No | Default: `false`. |
| `requiredActions` | `object[]` | No |  |
| `requiredActions[].actionId` | `string` | Yes |  |
| `requiredActions[].label` | `string` | Yes |  |
| `requiredActions[].value` | `string` | Yes |  |
| `requiredActions[].mappedTo` | `string` | No |  |
| `registeredEvents` | `object[]` | No |  |
| `registeredEvents[].eventId` | `string` | Yes |  |
| `registeredEvents[].subscribedAt` | `string` | No |  |
| `registeredEvents[].subscriptionId` | `string` | No |  |
| `authProviderId` | `string` | No |  |
| `eventKey` | `string` | No |  |
| `verification` | `object` | No |  |
| `verification.eventsVerification` | `object` | Yes |  |
| `verification.eventsVerification.method` | `string` | Yes | One of: `HMAC`, `CHALLENGE_RESPONSE`, `NONE`, `VERIFICATION_TOKEN`, `HEADER_TOKEN`. |
| `verification.eventsVerification.signatureHeader` | `string` | No |  |
| `verification.eventsVerification.algorithm` | `string` | No |  |
| `verification.eventsVerification.timestampHeader` | `string` | No |  |
| `verification.eventsVerification.maxTimestampAgeMs` | `integer` | No |  |
| `verification.eventsVerification.signaturePrefix` | `string` | No |  |
| `verification.eventsVerification.signatureFormat` | `string` | No | One of: `hex`, `stripe`. |
| `verification.eventsVerification.signingPayload` | `string` | No | One of: `body`, `hubspot_v1`, `hubspot_v2`, `hubspot_v3`, `slack_v0`, `stripe_v1`. |
| `verification.challengeDetection` | `object` | No |  |
| `verification.challengeDetection.field` | `string` | Yes |  |
| `verification.challengeDetection.value` | `string` | Yes |  |
| `verification.challengeDetection.responseField` | `string` | Yes |  |
| `verification.tokenHandshake` | `object` | No |  |
| `verification.tokenHandshake.field` | `string` | Yes |  |
| `verification.getChallenge` | `object` | No |  |
| `verification.getChallenge.source` | `string` | No | One of: `query`, `header`. |
| `verification.getChallenge.param` | `string` | No |  |
| `verification.getChallenge.verifyParam` | `string` | No |  |
| `verification.getChallenge.responseType` | `string` | No | One of: `text`, `json`. |
| `verification.getChallenge.responseField` | `string` | No |  |
| `verification.headerPayload` | `object` | No |  |
| `verificationSecret` | `string` | No |  |
| `connectorSlug` | `string` | No |  |
| `enabled` | `boolean` | No |  |
| `endOrgRouting` | `object` | No |  |
| `endOrgRouting.source` | `string` | Yes | One of: `header`, `body`. |
| `endOrgRouting.field` | `string` | Yes |  |
| `requireApiKey` | `boolean` | No |  |

**Responses**

* `200`: Updated webhook config
* `404`: Not found

### Delete a webhook config

```http
DELETE /v1/webhook-configs/{id}
```

Requires connectors.delete.

Operation: `deleteWebhookConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `404`: Not found

### Run a webhook subscription

```http
POST /v1/webhook-configs/{id}/execute-subscription
```

Runs the config's subscription code for one event, registering webhookUrl (which must be a public host) with the provider. Requires connectors.update.

Operation: `executeWebhookSubscription`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `eventId` | `string` | Yes |  |
| `webhookUrl` | `string` | Yes | Must point to a public host. |
| `additionalInputs` | `object` | No |  |

**Responses**

* `200`: Subscription result
* `400`: Validation error or subscription failed
* `404`: Not found

## Connector version pins

### List connector version pins

```http
GET /v1/connector-version-pins
```

The org's per-customer connector version pins. Requires connectors.read.

Operation: `listConnectorVersionPins`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | query | string | No |  |
| `endOrgId` | query | string | No |  |

**Responses**

* `200`: { data: [pin] }

### Pin a customer to a connector version

```http
POST /v1/connector-version-pins
```

Routes one customer (end org) to a provider externalVersion of a connector; requests that name no version resolve through the pin. Upserts. Requires connectors.update.

Operation: `upsertConnectorVersionPin`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorSlug` | `string` | Yes |  |
| `endOrgId` | `string` | Yes |  |
| `externalVersion` | `string` | No |  |
| `apiVersion` | `string` | No |  |
| `versionMajor` | `integer` | No |  |

**Responses**

* `200`: Pin
* `400`: Validation error, endOrgId not a customer of the org, or the version does not exist for the connector

### Remove a connector version pin

```http
DELETE /v1/connector-version-pins/{id}
```

Removes a pin; the customer goes back to the default version. Requires connectors.delete.

Operation: `deleteConnectorVersionPin`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `404`: Not found

## Mock

### Get what is needed to write mock stubs for an action

```http
GET /v1/mock/connectors/{connectorSlug}/actions/{actionSlug}
```

Returns the action's HTTP shape, input/output contracts and existing stubs, with instructions for the five stubs to create via POST .../stubs. Requires connectors.read; 404 for an unknown connector or action.

Operation: `generateActionMock`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | path | string | Yes | Connector slug (or id). |
| `actionSlug` | path | string | Yes |  |
| `connectorId` | query | string | No | Disambiguates the connector when the slug is not unique to the caller. |

**Responses**

* `200`: { data: { instructions, connector, action, inputContract, outputContract, existingStubs } }
* `404`: Connector or action not found

### Execute an action against its mock stubs

```http
POST /v1/mock/connectors/{connectorSlug}/actions/{actionSlug}/execute
```

Runs an action without calling the provider: the response comes from its mock stubs, chosen by mockStubId, else by a stub whose name contains scenario, else by matching input against the stubs' matchers. No credential is used. Missing required input fields are a 400. Requires connectors.read.

Operation: `executeMockAction`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | path | string | Yes | Connector slug |
| `actionSlug` | path | string | Yes | Action slug |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `input` | `object` | No | Action input. Default {}. |
| `mockStubId` | `string` | No | Serve exactly this stub. |
| `scenario` | `string` | No | Serve the stub whose name contains this text, e.g. "not found" or "rate limited". |
| `version` | `string` | No | Pin the connector's internal version. |
| `orgScope` | `string` | No | managed resolves only the platform catalog connector; custom only the caller's own. One of: `managed`, `custom`. |

**Responses**

* `200`: { data: { id, output, success, status, mock: true, durationMs } }
* `400`: Missing required input, or the action has no HTTP configuration
* `404`: Connector, action, stub or scenario not found

### List an action's mock stubs

```http
GET /v1/mock/connectors/{connectorSlug}/actions/{actionSlug}/stubs
```

Lists the mock stubs (test-case responses) of a connector action, in match priority order. Requires connectors.read.

Operation: `listMockStubs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | path | string | Yes | Connector slug (or id). |
| `actionSlug` | path | string | Yes |  |
| `connectorId` | query | string | No | Disambiguates the connector when the slug is not unique to the caller. |

**Responses**

* `200`: { data: stubs }
* `404`: Connector or action not found

### Create a mock stub

```http
POST /v1/mock/connectors/{connectorSlug}/actions/{actionSlug}/stubs
```

Adds a stub that mock executions of the action return when the input matches inputMatchers. Requires connectors.update; 400 when name, response.status or response.body is missing.

Operation: `createMockStub`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | path | string | Yes | Connector slug (or id). |
| `actionSlug` | path | string | Yes |  |
| `connectorId` | query | string | No | Disambiguates the connector when the slug is not unique to the caller. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `description` | `string` | No |  |
| `inputMatchers` | `object` | No | Input field -> value the call must carry for this stub to match; none = default stub. |
| `response` | `object` | Yes |  |
| `response.status` | `integer` | Yes | HTTP status the stub returns. |
| `response.body` | `any` | Yes | JSON body the stub returns. |
| `response.headers` | `object` | No |  |

**Responses**

* `200`: The created stub
* `400`: Missing name or response
* `404`: Connector or action not found

### Regenerate an action's default mock stub

```http
POST /v1/mock/connectors/{connectorSlug}/actions/{actionSlug}/stubs/regenerate
```

Regenerates the action's default stubs, one per scenario, from its output contract. Deterministic: no model is called. Stubs the author wrote are kept. Requires connectors.update; 400 when the action has no HTTP configuration.

Operation: `regenerateMockStubs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | path | string | Yes | Connector slug (or id). |
| `actionSlug` | path | string | Yes |  |
| `connectorId` | query | string | No | Disambiguates the connector when the slug is not unique to the caller. |

**Responses**

* `200`: Regeneration result
* `400`: Action has no HTTP configuration

### Update a mock stub

```http
PUT /v1/mock/connectors/{connectorSlug}/actions/{actionSlug}/stubs/{stubId}
```

Partially updates a stub; omitted fields keep their value. Requires connectors.update; 404 when the stub does not exist.

Operation: `updateMockStub`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | path | string | Yes | Connector slug (or id). |
| `actionSlug` | path | string | Yes |  |
| `connectorId` | query | string | No | Disambiguates the connector when the slug is not unique to the caller. |
| `stubId` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `inputMatchers` | `object` | No | Input field -> value the call must carry for this stub to match; none = default stub. |
| `response` | `object` | No |  |
| `response.status` | `integer` | No | HTTP status the stub returns. |
| `response.body` | `any` | No | JSON body the stub returns. |
| `response.headers` | `object` | No |  |

**Responses**

* `200`: The updated stub
* `404`: Stub not found

### Delete a mock stub

```http
DELETE /v1/mock/connectors/{connectorSlug}/actions/{actionSlug}/stubs/{stubId}
```

Deletes a stub. Requires connectors.update; 404 when the stub does not exist.

Operation: `deleteMockStub`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | path | string | Yes | Connector slug (or id). |
| `actionSlug` | path | string | Yes |  |
| `connectorId` | query | string | No | Disambiguates the connector when the slug is not unique to the caller. |
| `stubId` | path | string | Yes |  |

**Responses**

* `200`: { data: { id, deleted: true } }
* `404`: Stub not found

## Probes

### Probe a connector action's fields

```http
POST /v1/probes
```

Runs a read-only connector action, infers its output fields with sample values, and caches the result for 30 minutes under the returned probeId (for field mapping). Requires connectors.read; 400 for a non-read-only action; 403 when endOrgId is not a customer of the caller.

Operation: `probeConnector`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes | Connector id or slug. |
| `actionSlug` | `string` | Yes | A read-only action: its slug must start with list, get, search, fetch, describe, find, retrieve or read. |
| `params` | `object` | No | Action input. |
| `connectionId` | `string` | No |  |
| `endOrgId` | `string` | No | Customer whose connection to use; must descend from the caller's org. |
| `installationId` | `string` | No |  |

**Responses**

* `200`: { data: { probeId, connectorSlug, actionSlug, fieldCount, isPropertyEndpoint, fields } }
* `400`: Missing or non-read-only action
* `403`: Access denied

### Merge sub-entity probes into a parent probe

```http
POST /v1/probes/merge
```

Replaces each expanded array field of a cached parent probe with the fields of a sub-entity probe, prefixed (prefix.field). Requires connectors.read; 404 when the parent probe expired.

Operation: `mergeProbes`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `parentProbeId` | `string` | Yes |  |
| `subProbes` | `object[]` | Yes |  |
| `subProbes[].probeId` | `string` | Yes |  |
| `subProbes[].prefix` | `string` | Yes | The parent field this sub-entity expands. |

**Responses**

* `200`: { data: { parentProbeId, totalFields, mergedSubEntities } }
* `400`: Missing parentProbeId or subProbes
* `404`: Parent probe not found or expired

### Fetch sample values from a connector action

```http
POST /v1/probes/values
```

Runs a read-only connector action and returns its raw sample values and inferred fields, without caching. Requires connectors.read; same input rules as POST /probes.

Operation: `probeConnectorValues`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes | Connector id or slug. |
| `actionSlug` | `string` | Yes | A read-only action: its slug must start with list, get, search, fetch, describe, find, retrieve or read. |
| `params` | `object` | No | Action input. |
| `connectionId` | `string` | No |  |
| `endOrgId` | `string` | No | Customer whose connection to use; must descend from the caller's org. |
| `installationId` | `string` | No |  |

**Responses**

* `200`: { data: { connectorSlug, actionSlug, values, fields } }
* `400`: Missing or non-read-only action
* `403`: Access denied
