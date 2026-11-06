---
description: "Unified records, the catalog, and your own unified entities."
---

# Unified API

Base URL, authentication and errors are on the [REST API overview](README.md).

## Unified

### What unified did for one of your own request ids

```http
GET /v1/unified/calls
```

Single-provider calls (get, create, search, update, delete) sent with X-Fastn-Correlation-Id are recorded; this returns them for the caller's org (narrowed to the customer when the call is customer-scoped): provider, the connector service's execution id, the status the caller got, the error code when it failed, and duration. One row per real attempt, including a failure before the provider was called (e.g. 409 UNIFIED_CONNECTION_EXPIRED); replays are not recorded. Rows are kept for 30 days.

Operation: `listUnifiedCalls`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `correlation_id` | query | string | Yes |  |

**Responses**

* `200`: Up to 50 call records, newest first
* `400`: correlation_id missing

### List unified categories with their entities

```http
GET /v1/unified/categories
```

Lists the unified API categories and their entities visible to the caller (platform catalog plus the caller's org and ancestors' custom entities, with extensions applied). Requires unified.read.

Operation: `listUnifiedCategories`

**Responses**

* `200`: Categories with entities

### List canonical records

```http
GET /v1/unified/{category}/{entity}
```

fans out over every connected provider unless ?provider= or a cursor pins one Lists canonical records of a unified entity. Without provider, connection_id or cursor it fans out over every connected provider; a cursor is pinned to the provider that minted it and is rejected when it contradicts ?provider=. Requires unified.read.

Operation: `listUnifiedRecords`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `x-installation-id` | header | string | No | Installation whose widget config values (unifiedValues) apply to this call. Omit for a call with no widget identity. |
| `x-end-org-id` | header | string | No | Partner callers only: run the call for this customer (end-org id) and its connections. Must be a customer of the caller's org (403 otherwise); not with x-end-org-ref (400). Omitted = the caller's own scope, unchanged. |
| `x-end-org-ref` | header | string | No | Partner callers only: run the call for the customer registered under this external ref. 404 when the caller has no such customer; not with x-end-org-id (400). |
| `category` | path | string | Yes | Category slug, e.g. crm. |
| `entity` | path | string | Yes | Entity slug within the category, e.g. contacts. |
| `provider` | query | string | No | Connector slug to pin the call to. Omitted or empty = resolve from the caller's connected providers. 400 when not a connector slug. |
| `cursor` | query | string | No | Opaque cursor from a previous page. |
| `connection_id` | query | string | No | Which of the provider's connections to run against, when the org holds several accounts on the same connector. Ids come from GET /connections; one outside the caller's scope is rejected, not silently ignored. |
| `page_size` | query | integer | No | Clamped to 1-200. |
| `include_remote_data` | query | boolean | No | true adds the provider's raw record beside the canonical one. |
| `widget_id` | query | string | No | Widget whose unified config values (per connector) are applied to the call; ignored when the widget is not visible to the caller. |

**Responses**

* `200`: Single-provider { records, nextCursor, hasMore, provider } or slug-keyed multi-provider map. hasMore is true/false when the mapping can paginate (page token or page number) and null when it cannot - never false for a page that may have been truncated.
* `400`: Invalid cursor, or a cursor that contradicts ?provider=
* `404`: Unknown entity, no connected provider, or no such connection
* `502`: The provider failed (5xx, timeout, unreachable) or the connector platform refused the call (UNIFIED_PROVIDER_ERROR). Provider client errors are not 502: a provider 404/410 on a get, update or delete is 404 UNIFIED_PROVIDER_NOT_FOUND, any other provider 4xx except 405/408/415/423/425 is 400 UNIFIED_PROVIDER_REJECTED, 401/403 (or a 2xx body naming a revoked or invalid token) is 401 UNIFIED_PROVIDER_AUTH_FAILED and 429 is 429 UNIFIED_PROVIDER_RATE_LIMITED. Every provider error carries providerStatus (the provider's own status) and a truncated providerError; a platform refusal or a call the platform never answered carries none.

### Create a record from a canonical body via one provider

```http
POST /v1/unified/{category}/{entity}
```

Creates a record from a canonical body (any JSON object, mapped to the provider's fields) through one resolved provider. Requires unified.execute; 400 when the body is not a JSON object.

Operation: `createUnifiedRecord`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | string | No | Makes a retry safe: the same key on this route for the same org and customer answers from the first run for 24 hours (Idempotent-Replayed: true) instead of calling the provider again. A key still in flight is 409 IDEMPOTENCY_IN_PROGRESS; the same key sent with a different query string or body is 422 IDEMPOTENCY_KEY_REUSED. |
| `X-Fastn-Correlation-Id` | header | string | No | Your own id for this request (a call, a job). Echoed back, and the call is recorded under it: GET /api/v1/unified/calls?correlation_id=... |
| `x-installation-id` | header | string | No | Installation whose widget config values (unifiedValues) apply to this call. Omit for a call with no widget identity. |
| `x-end-org-id` | header | string | No | Partner callers only: run the call for this customer (end-org id) and its connections. Must be a customer of the caller's org (403 otherwise); not with x-end-org-ref (400). Omitted = the caller's own scope, unchanged. |
| `x-end-org-ref` | header | string | No | Partner callers only: run the call for the customer registered under this external ref. 404 when the caller has no such customer; not with x-end-org-id (400). |
| `category` | path | string | Yes | Category slug, e.g. crm. |
| `entity` | path | string | Yes | Entity slug within the category, e.g. contacts. |
| `provider` | query | string | No | Connector slug to pin the call to. Omitted or empty = resolve from the caller's connected providers. 400 when not a connector slug. |
| `connection_id` | query | string | No | Which of the provider's connections to run against, when the org holds several accounts on the same connector. Ids come from GET /connections; one outside the caller's scope is rejected, not silently ignored. |
| `widget_id` | query | string | No | Widget whose unified config values (per connector) are applied to the call; ignored when the widget is not visible to the caller. |

**Responses**

* `201`: Created canonical record
* `400`: Canonical validation failed
* `404`: Unknown entity, no connected provider, or no such connection
* `409`: UNIFIED_CONNECTION_EXPIRED when the pinned connection_id is yours but its login expired, or the connection the call ran on needs a new sign-in (ask for a fresh sign-in). Otherwise: Multiple providers connected; specify ?provider= (or ?connection_id= to pick one of several connections on the same provider)
* `502`: The provider failed (5xx, timeout, unreachable) or the connector platform refused the call (UNIFIED_PROVIDER_ERROR). Provider client errors are not 502: a provider 404/410 on a get, update or delete is 404 UNIFIED_PROVIDER_NOT_FOUND, any other provider 4xx except 405/408/415/423/425 is 400 UNIFIED_PROVIDER_REJECTED, 401/403 (or a 2xx body naming a revoked or invalid token) is 401 UNIFIED_PROVIDER_AUTH_FAILED and 429 is 429 UNIFIED_PROVIDER_RATE_LIMITED. Every provider error carries providerStatus (the provider's own status) and a truncated providerError; a platform refusal or a call the platform never answered carries none.

### List mapped providers and the caller's connection state

```http
GET /v1/unified/{category}/{entity}/providers
```

Lists the connectors mapped for one unified entity and whether the caller has a usable connection to each. Requires unified.read; 404 for an unknown entity.

Operation: `listUnifiedEntityProviders`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `x-end-org-id` | header | string | No | Partner callers only: run the call for this customer (end-org id) and its connections. Must be a customer of the caller's org (403 otherwise); not with x-end-org-ref (400). Omitted = the caller's own scope, unchanged. |
| `x-end-org-ref` | header | string | No | Partner callers only: run the call for the customer registered under this external ref. 404 when the caller has no such customer; not with x-end-org-id (400). |
| `category` | path | string | Yes | Category slug, e.g. crm. |
| `entity` | path | string | Yes | Entity slug within the category, e.g. contacts. |

**Responses**

* `200`: Providers with connected (credentials stored), verifyStatus and healthy (provider accepted them). No connection identifier is returned.
* `404`: Unknown entity

### Search records by filters via one provider

```http
POST /v1/unified/{category}/{entity}/search
```

Only for entities whose mapping offers search (discovery lists the accepted names in searchFilters). The body is the filters, e.g. {"phone": "+15550100"} or {"query": "jane@x.com", "time_min": "2026-10-16T00:00:00Z"}. Returns the first page of matches.

Operation: `searchUnifiedRecords`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `X-Fastn-Correlation-Id` | header | string | No | Your own id for this request (a call, a job). Echoed back, and the call is recorded under it: GET /api/v1/unified/calls?correlation_id=... |
| `x-installation-id` | header | string | No | Installation whose widget config values (unifiedValues) apply to this call. Omit for a call with no widget identity. |
| `x-end-org-id` | header | string | No | Partner callers only: run the call for this customer (end-org id) and its connections. Must be a customer of the caller's org (403 otherwise); not with x-end-org-ref (400). Omitted = the caller's own scope, unchanged. |
| `x-end-org-ref` | header | string | No | Partner callers only: run the call for the customer registered under this external ref. 404 when the caller has no such customer; not with x-end-org-id (400). |
| `category` | path | string | Yes | Category slug, e.g. crm. |
| `entity` | path | string | Yes | Entity slug within the category, e.g. contacts. |
| `provider` | query | string | No | Connector slug to pin the call to. Omitted or empty = resolve from the caller's connected providers. 400 when not a connector slug. |
| `connection_id` | query | string | No | Which of the provider's connections to run against, when the org holds several accounts on the same connector. Ids come from GET /connections; one outside the caller's scope is rejected, not silently ignored. |
| `page_size` | query | integer | No |  |

**Responses**

* `200`: { records, hasMore, provider, warnings? }
* `400`: Unknown filter or no filter (UNIFIED_VALIDATION_FAILED)
* `404`: Unknown entity, no connected provider, no such connection, or search not offered (UNIFIED_UNSUPPORTED_OPERATION)
* `409`: UNIFIED_CONNECTION_EXPIRED: the pinned connection_id is yours but its login expired, or the connection the call ran on needs a new sign-in; ask for a fresh sign-in rather than a different id. (Also UNIFIED_MULTIPLE_PROVIDERS when several providers are connected and none is pinned.)
* `502`: The provider failed (5xx, timeout, unreachable) or the connector platform refused the call (UNIFIED_PROVIDER_ERROR). Provider client errors are not 502: a provider 404/410 on a get, update or delete is 404 UNIFIED_PROVIDER_NOT_FOUND, any other provider 4xx except 405/408/415/423/425 is 400 UNIFIED_PROVIDER_REJECTED, 401/403 (or a 2xx body naming a revoked or invalid token) is 401 UNIFIED_PROVIDER_AUTH_FAILED and 429 is 429 UNIFIED_PROVIDER_RATE_LIMITED. Every provider error carries providerStatus (the provider's own status) and a truncated providerError; a platform refusal or a call the platform never answered carries none.

### Get one canonical record by remote id

```http
GET /v1/unified/{category}/{entity}/{id}
```

Fetches one canonical record by the provider's remote id through one resolved provider. Requires unified.read.

Operation: `getUnifiedRecord`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `x-installation-id` | header | string | No | Installation whose widget config values (unifiedValues) apply to this call. Omit for a call with no widget identity. |
| `x-end-org-id` | header | string | No | Partner callers only: run the call for this customer (end-org id) and its connections. Must be a customer of the caller's org (403 otherwise); not with x-end-org-ref (400). Omitted = the caller's own scope, unchanged. |
| `x-end-org-ref` | header | string | No | Partner callers only: run the call for the customer registered under this external ref. 404 when the caller has no such customer; not with x-end-org-id (400). |
| `category` | path | string | Yes | Category slug, e.g. crm. |
| `entity` | path | string | Yes | Entity slug within the category, e.g. contacts. |
| `id` | path | string | Yes | The provider's remote id. |
| `provider` | query | string | No | Connector slug to pin the call to. Omitted or empty = resolve from the caller's connected providers. 400 when not a connector slug. |
| `connection_id` | query | string | No | Which of the provider's connections to run against, when the org holds several accounts on the same connector. Ids come from GET /connections; one outside the caller's scope is rejected, not silently ignored. |
| `include_remote_data` | query | boolean | No | true adds the provider's raw record beside the canonical one. |
| `widget_id` | query | string | No | Widget whose unified config values (per connector) are applied to the call; ignored when the widget is not visible to the caller. |

**Responses**

* `200`: Canonical record
* `404`: UNIFIED_PROVIDER_NOT_FOUND when the provider has no record with this id (providerStatus carries its 404/410). Otherwise: unknown entity, no connected provider, or no such connection
* `409`: UNIFIED_CONNECTION_EXPIRED when the pinned connection_id is yours but its login expired, or the connection the call ran on needs a new sign-in (ask for a fresh sign-in). Otherwise: Multiple providers connected; specify ?provider= (or ?connection_id= to pick one of several connections on the same provider)
* `502`: The provider failed (5xx, timeout, unreachable) or the connector platform refused the call (UNIFIED_PROVIDER_ERROR). Provider client errors are not 502: a provider 404/410 on a get, update or delete is 404 UNIFIED_PROVIDER_NOT_FOUND, any other provider 4xx except 405/408/415/423/425 is 400 UNIFIED_PROVIDER_REJECTED, 401/403 (or a 2xx body naming a revoked or invalid token) is 401 UNIFIED_PROVIDER_AUTH_FAILED and 429 is 429 UNIFIED_PROVIDER_RATE_LIMITED. Every provider error carries providerStatus (the provider's own status) and a truncated providerError; a platform refusal or a call the platform never answered carries none.

### Update a record (partial canonical body) via one provider

```http
PATCH /v1/unified/{category}/{entity}/{id}
```

Only for entities whose mapping offers update. Sends only the fields named; unsent fields keep their value.

Operation: `updateUnifiedRecord`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | string | No | Makes a retry safe: the same key on this route for the same org and customer answers from the first run for 24 hours (Idempotent-Replayed: true) instead of calling the provider again. A key still in flight is 409 IDEMPOTENCY_IN_PROGRESS; the same key sent with a different query string or body is 422 IDEMPOTENCY_KEY_REUSED. |
| `X-Fastn-Correlation-Id` | header | string | No | Your own id for this request (a call, a job). Echoed back, and the call is recorded under it: GET /api/v1/unified/calls?correlation_id=... |
| `x-installation-id` | header | string | No | Installation whose widget config values (unifiedValues) apply to this call. Omit for a call with no widget identity. |
| `x-end-org-id` | header | string | No | Partner callers only: run the call for this customer (end-org id) and its connections. Must be a customer of the caller's org (403 otherwise); not with x-end-org-ref (400). Omitted = the caller's own scope, unchanged. |
| `x-end-org-ref` | header | string | No | Partner callers only: run the call for the customer registered under this external ref. 404 when the caller has no such customer; not with x-end-org-id (400). |
| `category` | path | string | Yes | Category slug, e.g. crm. |
| `entity` | path | string | Yes | Entity slug within the category, e.g. contacts. |
| `id` | path | string | Yes | The provider's remote id. |
| `provider` | query | string | No | Connector slug to pin the call to. Omitted or empty = resolve from the caller's connected providers. 400 when not a connector slug. |
| `connection_id` | query | string | No | Which of the provider's connections to run against, when the org holds several accounts on the same connector. Ids come from GET /connections; one outside the caller's scope is rejected, not silently ignored. |

**Responses**

* `200`: Updated canonical record
* `400`: Unknown, read-only or no field (UNIFIED_VALIDATION_FAILED)
* `404`: UNIFIED_PROVIDER_NOT_FOUND when the provider has no record with this id (providerStatus carries its 404/410). Otherwise: unknown entity, no connected provider, no such connection, or update not offered
* `409`: UNIFIED_CONNECTION_EXPIRED: the pinned connection_id is yours but its login expired, or the connection the call ran on needs a new sign-in; ask for a fresh sign-in rather than a different id. (Also UNIFIED_MULTIPLE_PROVIDERS when several providers are connected and none is pinned.)
* `502`: The provider failed (5xx, timeout, unreachable) or the connector platform refused the call (UNIFIED_PROVIDER_ERROR). Provider client errors are not 502: a provider 404/410 on a get, update or delete is 404 UNIFIED_PROVIDER_NOT_FOUND, any other provider 4xx except 405/408/415/423/425 is 400 UNIFIED_PROVIDER_REJECTED, 401/403 (or a 2xx body naming a revoked or invalid token) is 401 UNIFIED_PROVIDER_AUTH_FAILED and 429 is 429 UNIFIED_PROVIDER_RATE_LIMITED. Every provider error carries providerStatus (the provider's own status) and a truncated providerError; a platform refusal or a call the platform never answered carries none.

### Delete a record via one provider

```http
DELETE /v1/unified/{category}/{entity}/{id}
```

Only for entities whose mapping offers delete.

Operation: `deleteUnifiedRecord`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | string | No | Makes a retry safe: the same key on this route for the same org and customer answers from the first run for 24 hours (Idempotent-Replayed: true) instead of calling the provider again. A key still in flight is 409 IDEMPOTENCY_IN_PROGRESS; the same key sent with a different query string or body is 422 IDEMPOTENCY_KEY_REUSED. |
| `X-Fastn-Correlation-Id` | header | string | No | Your own id for this request (a call, a job). Echoed back, and the call is recorded under it: GET /api/v1/unified/calls?correlation_id=... |
| `x-installation-id` | header | string | No | Installation whose widget config values (unifiedValues) apply to this call. Omit for a call with no widget identity. |
| `x-end-org-id` | header | string | No | Partner callers only: run the call for this customer (end-org id) and its connections. Must be a customer of the caller's org (403 otherwise); not with x-end-org-ref (400). Omitted = the caller's own scope, unchanged. |
| `x-end-org-ref` | header | string | No | Partner callers only: run the call for the customer registered under this external ref. 404 when the caller has no such customer; not with x-end-org-id (400). |
| `category` | path | string | Yes | Category slug, e.g. crm. |
| `entity` | path | string | Yes | Entity slug within the category, e.g. contacts. |
| `id` | path | string | Yes | The provider's remote id. |
| `provider` | query | string | No | Connector slug to pin the call to. Omitted or empty = resolve from the caller's connected providers. 400 when not a connector slug. |
| `connection_id` | query | string | No | Which of the provider's connections to run against, when the org holds several accounts on the same connector. Ids come from GET /connections; one outside the caller's scope is rejected, not silently ignored. |

**Responses**

* `200`: { id, provider, deleted: true }
* `404`: UNIFIED_PROVIDER_NOT_FOUND when the provider has no record with this id (providerStatus carries its 404/410). Otherwise: unknown entity, no connected provider, no such connection, or delete not offered
* `409`: UNIFIED_CONNECTION_EXPIRED: the pinned connection_id is yours but its login expired, or the connection the call ran on needs a new sign-in; ask for a fresh sign-in rather than a different id. (Also UNIFIED_MULTIPLE_PROVIDERS when several providers are connected and none is pinned.)
* `502`: The provider failed (5xx, timeout, unreachable) or the connector platform refused the call (UNIFIED_PROVIDER_ERROR). Provider client errors are not 502: a provider 404/410 on a get, update or delete is 404 UNIFIED_PROVIDER_NOT_FOUND, any other provider 4xx except 405/408/415/423/425 is 400 UNIFIED_PROVIDER_REJECTED, 401/403 (or a 2xx body naming a revoked or invalid token) is 401 UNIFIED_PROVIDER_AUTH_FAILED and 429 is 429 UNIFIED_PROVIDER_RATE_LIMITED. Every provider error carries providerStatus (the provider's own status) and a truncated providerError; a platform refusal or a call the platform never answered carries none.

## Unified custom

### The caller's catalog orgs' own entities (with mappings) and extensions of platform...

```http
GET /v1/unified-custom
```

editable marks rows the caller's org owns. Returns the entities owned by the caller's catalog orgs (own org and ancestors, with mappings) and the extensions of platform entities; editable marks rows the caller's org owns. Requires unified.read.

Operation: `listUnifiedCustom`

**Responses**

* `200`: { data: { entities, extensions } }

### Create an entity owned by the caller's org in a platform category (unified.customize)

```http
POST /v1/unified-custom/entities
```

fromEntityId copies a visible entity's schema and enabled mappings, with the caller's extensions merged in. Creates an entity owned by the caller's org in a platform category; fromEntityId copies a visible entity's schema and enabled mappings. Requires unified.customize. 400 for an unknown categoryId or fromEntityId.

Operation: `createUnifiedCustomEntity`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `categoryId` | `string` | Yes |  |
| `slug` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `description` | `string` | No |  |
| `schema` | `object` | No |  |
| `fromEntityId` | `string` | No |  |

**Responses**

* `201`: Created, with any cloned mappings
* `409`: Slug already resolvable by the caller (platform or ancestor entity), or the per-org limit reached

### Update one of the caller org's entities (unified.customize)

```http
PUT /v1/unified-custom/entities/{id}
```

Updates an entity the caller's org owns. Requires unified.customize. 400 when no field is given; 404 when not found.

Operation: `updateUnifiedCustomEntity`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `schema` | `object` | No |  |

**Responses**

* `200`: Updated
* `404`: Not an entity of the caller's org

### Delete one of the caller org's entities and its mappings (unified.customize)

```http
DELETE /v1/unified-custom/entities/{id}
```

Deletes an entity the caller's org owns and its mappings. Requires unified.customize. 409 while a fork depends on it; 404 when not found.

Operation: `deleteUnifiedCustomEntity`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `404`: Not an entity of the caller's org

### Bind a connector mapping to one of the caller org's entities (unified.customize)

```http
POST /v1/unified-custom/entities/{id}/mappings
```

same body as the platform catalog mapping Binds a connector mapping to an entity the caller's org owns. Requires unified.customize. 409 when the connector is already mapped; 404 when the entity is not found.

Operation: `createUnifiedCustomMapping`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorSlug` | `string` | Yes |  |
| `enabled` | `boolean` | No | Default: `true`. |
| `events` | `object` | No |  |
| `operations` | `object` | No |  |
| `operations.list` | `object` | No |  |
| `operations.list.actionSlug` | `string` | Yes |  |
| `operations.list.staticInput` | `object` | No |  |
| `operations.list.paramMap` | `object` | No |  |
| `operations.list.paramMap.cursor` | `string` | No |  |
| `operations.list.paramMap.pageSize` | `string` | No |  |
| `operations.list.paramMap.page` | `string` | No |  |
| `operations.list.paramMap.offset` | `string` | No |  |
| `operations.list.paramMap.id` | `string` | No |  |
| `operations.list.recordsPath` | `string` | Yes |  |
| `operations.list.cursorPath` | `string` | No |  |
| `operations.list.totalPath` | `string` | No |  |
| `operations.list.remoteIdPath` | `string` | Yes |  |
| `operations.list.resolveInput` | `object` | No |  |
| `operations.get` | `object` | No |  |
| `operations.get.actionSlug` | `string` | Yes |  |
| `operations.get.staticInput` | `object` | No |  |
| `operations.get.paramMap` | `object` | No |  |
| `operations.get.paramMap.cursor` | `string` | No |  |
| `operations.get.paramMap.pageSize` | `string` | No |  |
| `operations.get.paramMap.page` | `string` | No |  |
| `operations.get.paramMap.offset` | `string` | No |  |
| `operations.get.paramMap.id` | `string` | No |  |
| `operations.get.recordsPath` | `string` | Yes |  |
| `operations.get.cursorPath` | `string` | No |  |
| `operations.get.totalPath` | `string` | No |  |
| `operations.get.remoteIdPath` | `string` | Yes |  |
| `operations.get.resolveInput` | `object` | No |  |
| `operations.create` | `object` | No |  |
| `operations.create.actionSlug` | `string` | Yes |  |
| `operations.create.staticInput` | `object` | No |  |
| `operations.create.paramMap` | `object` | No |  |
| `operations.create.paramMap.cursor` | `string` | No |  |
| `operations.create.paramMap.pageSize` | `string` | No |  |
| `operations.create.paramMap.page` | `string` | No |  |
| `operations.create.paramMap.offset` | `string` | No |  |
| `operations.create.paramMap.id` | `string` | No |  |
| `operations.create.recordsPath` | `string` | Yes |  |
| `operations.create.cursorPath` | `string` | No |  |
| `operations.create.totalPath` | `string` | No |  |
| `operations.create.remoteIdPath` | `string` | Yes |  |
| `operations.create.resolveInput` | `object` | No |  |
| `operations.update` | `object` | No |  |
| `operations.update.actionSlug` | `string` | Yes |  |
| `operations.update.staticInput` | `object` | No |  |
| `operations.update.paramMap` | `object` | No |  |
| `operations.update.paramMap.cursor` | `string` | No |  |
| `operations.update.paramMap.pageSize` | `string` | No |  |
| `operations.update.paramMap.page` | `string` | No |  |
| `operations.update.paramMap.offset` | `string` | No |  |
| `operations.update.paramMap.id` | `string` | No |  |
| `operations.update.recordsPath` | `string` | Yes |  |
| `operations.update.cursorPath` | `string` | No |  |
| `operations.update.totalPath` | `string` | No |  |
| `operations.update.remoteIdPath` | `string` | Yes |  |
| `operations.update.resolveInput` | `object` | No |  |

**Responses**

* `201`: Created
* `409`: Mapping for connector already exists

### Test-execute an entity the caller can see (own, ancestor's, or platform with the...

```http
POST /v1/unified-custom/entities/{id}/test
```

Runs list, get or create for an entity the caller can see against the caller's own connections. Requires unified.customize. 404 when the entity is not visible or has no enabled mappings.

Operation: `testUnifiedCustomEntity`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `op` | `string` | Yes | One of: `list`, `get`, `create`. |
| `provider` | `string` | Yes |  |
| `connectionId` | `string` | No |  |
| `params` | `object` | No |  |

**Responses**

* `200`: Engine result with remote data

### Create or replace the caller org's extension of a platform entity

```http
PUT /v1/unified-custom/extensions/{entityId}
```

extra canonical fields plus, per mapped connector, field mappings and staticInput values to append (e.g. HubSpot properties). Visible to the org and its customers only (unified.customize). Creates or replaces the caller org's extension of a platform entity. Requires unified.customize. 404 when the platform entity does not exist; 400 when the extension conflicts with the entity.

Operation: `upsertUnifiedExtension`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `entityId` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `schema` | `object` | No |  |
| `connectorOverrides` | `object` | No |  |

**Responses**

* `200`: Stored extension
* `400`: Redefines a platform field, names an unmapped connector, or maps onto an unknown field
* `404`: Not a platform entity

### Remove the caller org's extension of a platform entity (unified.customize)

```http
DELETE /v1/unified-custom/extensions/{entityId}
```

Removes the caller org's extension of a platform entity. Requires unified.customize. 404 when there is none.

Operation: `deleteUnifiedExtension`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `entityId` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `404`: No extension

### Update a mapping on one of the caller org's entities (unified.customize)

```http
PUT /v1/unified-custom/mappings/{id}
```

Updates a mapping on an entity the caller's org owns. Requires unified.customize. 404 when not found.

Operation: `updateUnifiedCustomMapping`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `enabled` | `boolean` | No |  |
| `events` | `object` | No |  |
| `operations` | `object` | No |  |
| `operations.list` | `object` | No |  |
| `operations.list.actionSlug` | `string` | Yes |  |
| `operations.list.staticInput` | `object` | No |  |
| `operations.list.paramMap` | `object` | No |  |
| `operations.list.paramMap.cursor` | `string` | No |  |
| `operations.list.paramMap.pageSize` | `string` | No |  |
| `operations.list.paramMap.page` | `string` | No |  |
| `operations.list.paramMap.offset` | `string` | No |  |
| `operations.list.paramMap.id` | `string` | No |  |
| `operations.list.recordsPath` | `string` | Yes |  |
| `operations.list.cursorPath` | `string` | No |  |
| `operations.list.totalPath` | `string` | No |  |
| `operations.list.remoteIdPath` | `string` | Yes |  |
| `operations.list.resolveInput` | `object` | No |  |
| `operations.get` | `object` | No |  |
| `operations.get.actionSlug` | `string` | Yes |  |
| `operations.get.staticInput` | `object` | No |  |
| `operations.get.paramMap` | `object` | No |  |
| `operations.get.paramMap.cursor` | `string` | No |  |
| `operations.get.paramMap.pageSize` | `string` | No |  |
| `operations.get.paramMap.page` | `string` | No |  |
| `operations.get.paramMap.offset` | `string` | No |  |
| `operations.get.paramMap.id` | `string` | No |  |
| `operations.get.recordsPath` | `string` | Yes |  |
| `operations.get.cursorPath` | `string` | No |  |
| `operations.get.totalPath` | `string` | No |  |
| `operations.get.remoteIdPath` | `string` | Yes |  |
| `operations.get.resolveInput` | `object` | No |  |
| `operations.create` | `object` | No |  |
| `operations.create.actionSlug` | `string` | Yes |  |
| `operations.create.staticInput` | `object` | No |  |
| `operations.create.paramMap` | `object` | No |  |
| `operations.create.paramMap.cursor` | `string` | No |  |
| `operations.create.paramMap.pageSize` | `string` | No |  |
| `operations.create.paramMap.page` | `string` | No |  |
| `operations.create.paramMap.offset` | `string` | No |  |
| `operations.create.paramMap.id` | `string` | No |  |
| `operations.create.recordsPath` | `string` | Yes |  |
| `operations.create.cursorPath` | `string` | No |  |
| `operations.create.totalPath` | `string` | No |  |
| `operations.create.remoteIdPath` | `string` | Yes |  |
| `operations.create.resolveInput` | `object` | No |  |
| `operations.update` | `object` | No |  |
| `operations.update.actionSlug` | `string` | Yes |  |
| `operations.update.staticInput` | `object` | No |  |
| `operations.update.paramMap` | `object` | No |  |
| `operations.update.paramMap.cursor` | `string` | No |  |
| `operations.update.paramMap.pageSize` | `string` | No |  |
| `operations.update.paramMap.page` | `string` | No |  |
| `operations.update.paramMap.offset` | `string` | No |  |
| `operations.update.paramMap.id` | `string` | No |  |
| `operations.update.recordsPath` | `string` | Yes |  |
| `operations.update.cursorPath` | `string` | No |  |
| `operations.update.totalPath` | `string` | No |  |
| `operations.update.remoteIdPath` | `string` | Yes |  |
| `operations.update.resolveInput` | `object` | No |  |
| `operations.delete` | `object` | No |  |

**Responses**

* `200`: Updated

### Delete a mapping on one of the caller org's entities (unified.customize)

```http
DELETE /v1/unified-custom/mappings/{id}
```

Deletes a mapping on an entity the caller's org owns. Requires unified.customize. 404 when not found.

Operation: `deleteUnifiedCustomMapping`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted

## Unified catalog

### List catalog categories (admin view)

```http
GET /v1/unified-catalog/categories
```

Lists the platform catalog's categories with their entity counts. Requires unified.read.

Operation: `listUnifiedCatalogCategories`

**Responses**

* `200`: Categories

### List catalog entities

```http
GET /v1/unified-catalog/entities
```

Lists the platform catalog's entities with their mapping counts. Requires unified.read.

Operation: `listUnifiedCatalogEntities`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `category` | query | string | No | Category id or slug. |

**Responses**

* `200`: Entities

### Get an entity with its connector mappings

```http
GET /v1/unified-catalog/entities/{id}
```

Returns a platform catalog entity with all its connector mappings. Requires unified.read; 404 when not found.

Operation: `getUnifiedCatalogEntity`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Entity with mappings
* `404`: Not found
