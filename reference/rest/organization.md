---
description: "Customers, people, roles, teams and API keys."
---

# Organization and access

The `/v1/orgs` routes are how you create and manage your customers.

Base URL, authentication and errors are on the [REST API overview](README.md).

## Orgs

### List customers

```http
GET /v1/orgs
```

Lists the caller's own org and its child orgs (owner/admin only; Filters narrow by type, tier and parent; include_usage adds lifetime usage counters per org.

Operation: `listOrgs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `type` | query | string | No | company \| partner \| end_org \| personal (account is accepted as an alias of company). |
| `tier` | query | string | No | account or tenant; any other value is a 400. One of: `account`, `tenant`. |
| `parent_id` | query | string | No | Only children of this org. |
| `parentId` | query | string | No | Alias of parent_id, used when parent_id is absent. |
| `include_usage` | query | string | No | 1 or true adds executions, events, storage_gb, overage, credits, integrations and users per org. With no metered executions the count of runs is used, capped at 100,000; a capped row also carries executionsIsLowerBound: true. One of: `1`, `true`. |
| `include_connections` | query | string | No | 1 or true adds connectionsCount (live connections, read from the connector layer) to each customer of the one partner the list is scoped to. Omitted on a row when it could not be counted. Combines with include_usage. One of: `1`, `true`. |

**Responses**

* `200`: Org list

### Create customer organization

```http
POST /v1/orgs
```

Creates an org. Partner-API callers register a customer (customer) with just name + orgId + tier: orgId is the PARTNER'S identifier for the customer, stored as external_ref (fastn generates its own id), and tier (id or display name of an entry in the account's customer_tiers) is written to the org config. slug is derived from name when omitted.

Operation: `createTenant`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `orgId` | `string` | No | Partner-supplied external reference for this customer org, stored as external_ref. Usable later as x-org-id / orgId. |
| `external_ref` | `string` | No | Alias of orgId. Rejected when it differs from orgId. |
| `externalRef` | `string` | No | Alias of orgId. Rejected when it differs from orgId. |
| `tier` | `string` | No | Customer tier: id or display name from the account's customer_tiers. |
| `limits` | `object` | No | Per-customer limit overrides layered over the tier's limits, e.g. {"connections": 2}. 0 means none allowed. |
| `slug` | `string` | No | Derived from name when omitted. |
| `plan` | `string` | No | Launch, Scale and Enterprise are the tiers on offer; 'growth' and 'free' are retired names still carried by existing orgs and still accepted. One of: `launch`, `scale`, `enterprise`, `growth`, `free`. Default: `"launch"`. |
| `type` | `string` | No | account is a legacy alias of company. One of: `company`, `partner`, `end_org`, `personal`, `account`. |
| `parentId` | `string` | No | Defaults to the caller's org. |
| `domain` | `string` | No |  |
| `ownerEmail` | `string` | No | REQUIRED when type resolves to company or partner, an account cannot exist without an owner. Ignored for end_org. |
| `owner_email` | `string` | No | Alias of ownerEmail. |

**Responses**

* `201`: Org created. Account-tier responses carry an `owner` object ({ userId, email, inviteStatus }, `inviteStatus` is `accepted` when the named owner already had a fastn account they had verified, so it is not a 'somebody must act' flag); `inviteSent: false` is added only when the invite email failed to send.
* `400`: Validation error / slug already exists / orgId vs externalRef mismatch / ownerEmail missing on an account / PERSONAL_ORG_NOT_ALLOWED: a customer is created with type end_org
* `403`: This caller cannot set a paid plan, or account cap reached
* `500`: Owner assignment failed and the partial org could not be removed, its slug stays in use
* `502`: Owner assignment failed; nothing was written and the call can be retried

### Get customer

```http
GET /v1/orgs/{id}
```

Returns one org. Requires settings.read.

Operation: `getTenant`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | The customer: fastn's org id, or the id you gave the customer at creation (orgId / externalRef). |

**Responses**

* `200`: Customer
* `404`: Not found

### Update customer

```http
PUT /v1/orgs/{id}
```

Updates an org the caller may manage. status may be changed by an owner/admin on its own child org. external_ref is immutable: resending the stored value is a no-op, any other value is a 400.

Operation: `updateTenant`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | The customer: fastn's org id, or the id you gave the customer at creation (orgId / externalRef). |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `plan` | `string` | No | One of: `launch`, `scale`, `enterprise`, `growth`, `free`. |
| `status` | `string` | No | One of: `active`, `suspended`, `pending_review`, `blocked`. |
| `adminEmail` | `string` | No | null or blank clears it. |
| `adminUserId` | `string` | No |  |
| `external_ref` | `string` | No | Must equal the stored value. |
| `externalRef` | `string` | No | Alias of external_ref. |

**Responses**

* `200`: Updated

### Delete customer (suspended only)

```http
DELETE /v1/orgs/{id}
```

Deletes an org that is already suspended (400 otherwise) and has no child orgs. Requires org.delete on the caller's own org or a child of it.

Operation: `deleteTenant`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | The customer: fastn's org id, or the id you gave the customer at creation (orgId / externalRef). |

**Responses**

* `200`: Deleted
* `400`: Must be suspended first

### Assign an org admin

```http
POST /v1/orgs/{id}/admin
```

Makes the user with this email the org's admin, creating and inviting them when they have no account. Requires users.create on the caller's own org or a child of it.

Operation: `assignOrgAdmin`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | `string` | Yes |  |

**Responses**

* `200`: Existing user assigned
* `201`: User created and invited; inviteSent: false when the email failed
* `400`: email missing or invalid JSON
* `403`: Access denied
* `404`: Org not found
* `502`: Owner could not be assigned

### Get org config document

```http
GET /v1/orgs/{id}/config
```

Requires settings.update on this org or its parent; 404 when the org does not exist.

Operation: `getOrgConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Config document
* `403`: Requires settings.update on this org or its parent
* `404`: Org not found

### Update org config document

```http
PUT /v1/orgs/{id}/config
```

`orgName` is not a config key: it is written through to the org's `name` column (readable at GET /api/v1/orgs/{id}) and never stored in the document. Accepted at the top level or nested under `config`, and must be a non-blank string of at most 200 characters with no control characters, angle brackets or invisible characters. A value that differs from the current name is a rename and requires org.update; resending the name the org already has is a no-op and needs only settings.update, so a form that posts the name on every save still works. Omit it to leave the name unchanged; a blank value is rejected rather than clearing the saved name. The rename and the config write commit together. Only some keys may be changed, by who is writing: on its own org, timezone, setupLinkRedirectUrls and setupLinkDefaultTtlMinutes; an account on its own org also customer_tiers; a partner on one of its customers also tier, limits and roleOverride; A key outside that set is refused with 403 CONFIG_KEY_NOT_ALLOWED (a key sent with its stored value is ignored). roleOverride and a tier roleId cannot name an account-level role.

Operation: `updateOrgConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `orgName` | `string` | No | Renames the org. Written to orgs.name, not to the config document. |
| `timezone` | `string` | No | IANA time zone name, e.g. Asia/Karachi. Own org; any caller with settings.update. |
| `setupLinkRedirectUrls` | `string[]` | No | Where a setup link may send the customer when it is done: https URLs (http only on localhost). A setup link's redirectUrl must be one of them. Own org. |
| `setupLinkDefaultTtlMinutes` | `integer` | No | Default lifetime of a new setup link, in minutes, capped by the deployment maximum. Own org. |
| `customer_tiers` | `object[]` | No | An account's catalogue of customer tiers, on its own org. Replaces the whole list, and a tier left out is also cleared from every customer on it in the same write: read the current list with getOrgConfig first and send every tier to keep. A customer is put on one with `tier`. |
| `customer_tiers[].id` | `string` | Yes | Stable id, e.g. free or pro |
| `customer_tiers[].name` | `string` | Yes | Display name |
| `customer_tiers[].roleId` | `string` | Yes | The role a customer on this tier gets. Account-level roles (owner, admin, developer) are refused with CUSTOMER_ROLE_TOO_HIGH |
| `customer_tiers[].limits` | `object` | No | Ceilings for a customer on this tier by dimension, e.g. { connections: 4, integrations: 4, users: 2 }; -1 is unlimited. Never above the account's own plan |
| `customer_tiers[].resources` | `object` | No | What a customer on this tier may use |
| `customer_tiers[].resources.connectors` | `object` | No |  |
| `customer_tiers[].resources.connectors.only` | `string[]` | No | Connector ids a customer on this tier may connect |
| `tier` | `string` | No | A partner writing one of its customers: the id of one of the partner's customer_tiers. |
| `limits` | `object` | No | A partner writing one of its customers: that customer's own ceilings by dimension, overriding its tier's; -1 is unlimited, never above the partner's own plan. |
| `roleOverride` | `string` | No | A partner writing one of its customers: a customer-level role that replaces its tier's roleId. Account-level roles are refused with CUSTOMER_ROLE_TOO_HIGH. |

**Responses**

* `200`: The stored config document, without orgName
* `400`: Invalid JSON, a blank / oversized / unsafe / non-string / conflicting orgName, or CUSTOMER_ROLE_TOO_HIGH: a roleOverride or tier roleId naming owner, admin or developer
* `403`: Requires settings.update on this org or its parent, and org.update to send orgName; or CONFIG_KEY_NOT_ALLOWED with the keys this caller may not change
* `404`: Org not found

### Get the org's database config

```http
GET /v1/orgs/{id}/db-config
```

Where this org's fastn.db calls go (your own Postgres database or the shared schema). Never returns a password. owner/admin/developer.

Operation: `getOrgDbConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: The org's database config (never a password; a developer gets username and hasCaCert stripped too)
* `400`: Invalid body, or the org type cannot hold a database config
* `403`: Not the org itself or its parent, or role below owner/admin (developer may read)
* `404`: Organisation not found

### Save the org's database config

```http
PUT /v1/orgs/{id}/db-config
```

Saves connection details and/or pool limits; does not enable external routing (see enableOrgDbConfig). owner/admin only.

Operation: `updateOrgDbConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `poolMax` | `integer` | No |  |
| `connectTimeoutMs` | `integer` | No |  |
| `statementTimeoutMs` | `integer` | No |  |
| `idleTimeoutMs` | `integer` | No |  |
| `host` | `string` | No |  |
| `port` | `integer` | No |  |
| `database` | `string` | No |  |
| `username` | `string` | No |  |
| `password` | `string` | No | Omit to keep the stored password; only honoured when host, port, database and username are unchanged. |
| `sslMode` | `string` | No | One of: `disable`, `no-verify`, `prefer`, `require`, `verify-full`. |
| `caCert` | `string` | No | PEM CA bundle; null clears it. |
| `customSchema` | `string` | No |  |
| `limits` | `object` | No |  |
| `limits.poolMax` | `integer` | No |  |
| `limits.connectTimeoutMs` | `integer` | No |  |
| `limits.statementTimeoutMs` | `integer` | No |  |
| `limits.idleTimeoutMs` | `integer` | No |  |

**Responses**

* `200`: The org's database config (never a password; a developer gets username and hasCaCert stripped too)
* `400`: Invalid body, or the org type cannot hold a database config
* `403`: Not the org itself or its parent, or role below owner/admin (developer may read)
* `404`: Organisation not found

### Revert to the shared database

```http
DELETE /v1/orgs/{id}/db-config
```

Reverts the org to the shared schema and forgets the stored credentials. owner/admin only; 409 when the credentials cannot be removed.

Operation: `deleteOrgDbConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: The org's database config (never a password; a developer gets username and hasCaCert stripped too)
* `400`: Invalid body, or the org type cannot hold a database config
* `403`: Not the org itself or its parent, or role below owner/admin (developer may read)
* `404`: Organisation not found
* `409`: Credentials could not be removed

### Disable the external database

```http
POST /v1/orgs/{id}/db-config/disable
```

Routes the org's fastn.db calls back to the shared schema, keeping the stored credentials. owner/admin only.

Operation: `disableOrgDbConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: The org's database config (never a password; a developer gets username and hasCaCert stripped too)
* `400`: Invalid body, or the org type cannot hold a database config
* `403`: Not the org itself or its parent, or role below owner/admin (developer may read)
* `404`: Organisation not found

### Enable the external database

```http
POST /v1/orgs/{id}/db-config/enable
```

Re-tests the stored connection, then routes the org's fastn.db calls to it. owner/admin only; 409 when nothing is stored or the test fails.

Operation: `enableOrgDbConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: The org's database config (never a password; a developer gets username and hasCaCert stripped too)
* `400`: Invalid body, or the org type cannot hold a database config
* `403`: Not the org itself or its parent, or role below owner/admin (developer may read)
* `404`: Organisation not found
* `409`: No usable stored connection

### List workspace database overrides

```http
GET /v1/orgs/{id}/db-config/overrides
```

The workspaces under this org whose database config differs from the org's. owner/admin/developer.

Operation: `listOrgDbConfigOverrides`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: The org's database config (never a password; a developer gets username and hasCaCert stripped too)
* `400`: Invalid body, or the org type cannot hold a database config
* `403`: Not the org itself or its parent, or role below owner/admin (developer may read)
* `404`: Organisation not found

### Test a database connection

```http
POST /v1/orgs/{id}/db-config/test
```

Tests the given connection merged over the stored one without saving. A failed connection is a 200 with ok: false and the driver message. owner/admin only; 20 tests per minute per org.

Operation: `testOrgDbConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `poolMax` | `integer` | No |  |
| `connectTimeoutMs` | `integer` | No |  |
| `statementTimeoutMs` | `integer` | No |  |
| `idleTimeoutMs` | `integer` | No |  |
| `host` | `string` | No |  |
| `port` | `integer` | No |  |
| `database` | `string` | No |  |
| `username` | `string` | No |  |
| `password` | `string` | No | Omit to keep the stored password; only honoured when host, port, database and username are unchanged. |
| `sslMode` | `string` | No | One of: `disable`, `no-verify`, `prefer`, `require`, `verify-full`. |
| `caCert` | `string` | No | PEM CA bundle; null clears it. |
| `customSchema` | `string` | No |  |
| `limits` | `object` | No |  |
| `limits.poolMax` | `integer` | No |  |
| `limits.connectTimeoutMs` | `integer` | No |  |
| `limits.statementTimeoutMs` | `integer` | No |  |
| `limits.idleTimeoutMs` | `integer` | No |  |

**Responses**

* `200`: { ok, message }
* `400`: Invalid body, or the org type cannot hold a database config
* `403`: Not the org itself or its parent, or role below owner/admin (developer may read)
* `404`: Organisation not found
* `429`: Too many connection tests

### Get account domain/access settings

```http
GET /v1/orgs/{id}/settings
```

Returns the org's domain, autoApproveDomain and defaultMemberRole. Requires org.read and, outside the caller's own org.

Operation: `getAccountSettings`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Settings

### Update account domain/access settings

```http
PUT /v1/orgs/{id}/settings
```

Updates the org's claimed domain and domain auto-join settings (caller's own org, settings.update). A public mailbox domain is a 400, a domain another company already claims is a 409; enabling autoApproveDomain needs a defaultMemberRole.

Operation: `updateAccountSettings`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `domain` | `string` | No | Normalised before validation; null clears it. Changing it switches domain auto-join off until re-established. |
| `autoApproveDomain` | `boolean` | No |  |
| `defaultMemberRole` | `string` | No | Role a domain-matched joiner gets. |

**Responses**

* `200`: Updated

### Transfer org ownership

```http
POST /v1/orgs/{id}/transfer-ownership
```

Atomically makes an existing admin of the org its owner and demotes the current owner to admin. the target must be an admin member other than the caller.

Operation: `transferOrgOwnership`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `targetUserId` | `string` | Yes |  |

**Responses**

* `200`: Transferred
* `400`: targetUserId missing, not an admin, or the caller
* `403`: Caller is not the owner
* `404`: Target user not in this org

## Api keys

### List API keys

```http
GET /v1/api-keys
```

Lists the org's API keys (prefix and metadata, never the key itself). A customer-scoped caller sees only its customer's keys and unscoped ones. Requires settings.read.

Operation: `listApiKeys`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `mode` | query | string | No | One of: `test`, `live`. |

**Responses**

* `200`: Key list (no secrets)

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].name` | `string` |  |
| `data[].prefix` | `string` |  |
| `data[].workflowEnvId` | `string` | The workflow environment a live key is pinned to; null on a test key or a live key made before keys were pinned. |
| `data[].workflowEnvironment` | `object` |  |
| `data[].workflowEnvironment.id` | `string` |  |
| `data[].workflowEnvironment.name` | `string` |  |
| `data[].workflowEnvironment.slug` | `string` |  |
| `data[].envReach` | `string` | test: test environment only. pinned: workflowEnvironment plus test. all: a legacy live key, any environment. One of: `test`, `pinned`, `all`. |
| `data[].permissions` | `string[]` |  |
| `data[].expiresAt` | `string` |  |
| `data[].lastUsedAt` | `string` |  |
| `data[].createdAt` | `string` |  |

### Create API key

```http
POST /v1/api-keys
```

Creates an API key. By default the key belongs to the caller's own org. Pass `orgId` to target a different org the caller is an active member of; the grant is then capped by the caller's role in that org, and callers whose target-org role cannot create keys are rejected. Pinned credentials (API keys, customer/embed sessions) cannot retarget. Note: a key created into another org is only listable/manageable from a session in that org, this session cannot see or revoke it afterward.

Operation: `createApiKey`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `mode` | `string` | No | One of: `test`, `live`. |
| `environment` | `string` | No | One of: `production`, `staging`, `development`. |
| `workflowEnvId` | `string` | No |  |
| `permissions` | `string[]` | No |  |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `orgScope` | `string[]` | No |  |
| `ipWhitelist` | `string[]` | No |  |
| `rateLimit` | `integer` | No |  |
| `expiresAt` | `string` | No |  |
| `allowedOrigins` | `string[]` | No |  |
| `idvMode` | `string` | No | One of: `off`, `optional`, `required`. |

**Responses**

* `201`: Key created (full key returned once)
* `403`: Also returned with error quota_exceeded (dimension api_keys_per_tenant, plus current, limit, plan, limitSource and a message) when the org already holds as many live keys as its plan or an admin override allows. Waiting does not clear it, which is why it is not a 429; revoke a key or raise the limit. limitSource is plan or override.

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` |  |
| `data.name` | `string` |  |
| `data.key` | `string` | Full API key value, only returned on creation |
| `data.prefix` | `string` |  |
| `data.workflowEnvId` | `string` | The workflow environment a live key is pinned to; null on a test key or a live key made before keys were pinned. |
| `data.workflowEnvironment` | `object` |  |
| `data.workflowEnvironment.id` | `string` |  |
| `data.workflowEnvironment.name` | `string` |  |
| `data.workflowEnvironment.slug` | `string` |  |
| `data.envReach` | `string` | test: test environment only. pinned: workflowEnvironment plus test. all: a legacy live key, any environment. One of: `test`, `pinned`, `all`. |
| `data.permissions` | `string[]` |  |
| `data.orgId` | `string` | The org the key was created in (effective target org). |
| `data.expiresAt` | `string` |  |
| `data.createdAt` | `string` |  |
| `data.idvMode` | `string` | One of: `off`, `optional`, `required`. |
| `data.idvSecret` | `string` | Identity-verification HMAC secret, only returned when idvMode was enabled at creation (shown once). |
| `data.idvSecretPrefix` | `string` |  |

### Get API key

```http
GET /v1/api-keys/{id}
```

Reads one API key's metadata (never the key itself). 404 when it is not in the caller's org; 403 when it belongs to another customer than the caller's. Requires settings.read.

Operation: `getApiKey`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Key details

### Update API key

```http
PUT /v1/api-keys/{id}
```

Updates name, permissions, IP allowlist, rate limit, expiry and allowed origins. A key's mode and workflow environment are fixed at creation: sending a different `mode` or `workflowEnvId` is refused with 400 API_KEY_IMMUTABLE_FIELD; create a new key instead.

Operation: `updateApiKey`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `permissions` | `string[]` | No |  |
| `ipWhitelist` | `string[]` | No |  |
| `rateLimit` | `integer` | No |  |
| `expiresAt` | `string` | No |  |
| `allowedOrigins` | `string[]` | No |  |

**Responses**

* `200`: Updated

### Revoke API key

```http
DELETE /v1/api-keys/{id}
```

Revokes an API key. A key that is already revoked, or any key with ?permanent=true, is deleted outright. Requires settings.update.

Operation: `revokeApiKey`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `permanent` | query | boolean | No | Delete the key instead of only revoking it. |

**Responses**

* `200`: Revoked

### Configure identity verification (HMAC) for a key

```http
PUT /v1/api-keys/{id}/identity-verification
```

Enables, disables, or rotates the per-key identity-verification secret used to sign x-org-id/x-user-id identity headers (x-identity-hmac = hex HMAC-SHA256 of "{org}\n{user}"). Modes: off = trust the headers (ownership-checked only), optional = verify and log mismatches without blocking (rollout shake-out), required = reject a missing/invalid hash with 401. Enabling with no secret yet, or passing rotate:true, mints a new secret returned ONCE; the previous secret keeps verifying until the next rotation. Setting mode off deletes the stored secrets. Only valid on multi-customer keys, a customer-pinned or single-customer key is rejected with 400.

Operation: `setApiKeyIdentityVerification`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `mode` | `string` | Yes | One of: `off`, `optional`, `required`. |
| `rotate` | `boolean` | No |  |

**Responses**

* `200`: Updated (idvSecret present only when a new secret was minted, shown once)
* `400`: Not a multi-customer key / revoked key / validation error
* `404`: Key not found

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` |  |
| `data.idvMode` | `string` | One of: `off`, `optional`, `required`. |
| `data.idvConfigured` | `boolean` |  |
| `data.idvSecretPrefix` | `string` |  |
| `data.idvSecret` | `string` | Only when minted, shown once. |

### Roll an API key

```http
POST /v1/api-keys/{id}/roll
```

Issues a new secret for an API key, keeping its configuration, and returns the new key once. 400 for a revoked key; 403 when the key belongs to another customer. Requires settings.update.

Operation: `rollApiKey`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: The rolled key, including the new secret
* `400`: Invalid id or revoked key
* `404`: Not found

## Me

### Get the caller's resolved identity

```http
GET /v1/me
```

Who you are talking to. Answers from the gateway's resolved context, so it works for every credential a caller can arrive with, a dashboard JWT, an API key, an embed (widget) token and a share link alike; Call it before your first substantive reply and adapt to the answer, including `signupProfile` for how to word replies to this person and what they first came to build. Two independent axes, and do not collapse them: `actor` is WHICH CREDENTIAL, `actingAsTenant` is WHOSE WORKSPACE. `actingAsTenant: true` means the credential was minted for a customer of a parent org, `org` is that customer's own workspace and `parentOrg` is the partner whose product they are using, so speak in business terms about their own connections and not about building the platform. Their provider's integrations are theirs to use, and to customise by forking a copy into their own workspace (forkIntegration) - never in place. It is true for a partner's customer in an embedded widget AND for a customer-scoped API key, so it does not on its own mean a human is present; read `actor` for that. `actingAsTenant: false` means the caller is acting as the org itself, which for `actor: user` is the partner's own staff in the dashboard, with `role` naming the persona. `permissions` reports three layers rather than one merged list, because enforcement is a layered predicate and a merged copy would drift from it: `role` is the enforced baseline for the persona, `structured` narrows it when present (an action needs both; it is reported already intersected with the role, so it is the effective set), and `apiKeyGrant` is a ceiling over both and never widens them. Retired-resource entries may appear in `role` and govern nothing. Every tool call you make executes under this identity, so a 403 means this persona lacks the permission rather than a fault worth retrying. One limitation.

Operation: `whoami`

**Responses**

* `200`: Caller identity
* `401`: Unauthenticated

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.actor` | `string` | Which credential the caller authenticated with One of: `user`, `api_key`, `embed_user`, `share_link`. |
| `data.surface` | `string` | Where the caller is acting One of: `dashboard`, `embed`, `api`. |
| `data.actingAsTenant` | `boolean` | True when the credential was minted for a customer of a parent org: a partner's customer in an embedded widget, or a customer-scoped API key. Read `actor` to tell those apart. False means the caller acts as the org itself |
| `data.role` | `string` | The caller's persona. Always end_user for an embed token |
| `data.sub` | `string` | The gateway-resolved subject |
| `data.user` | `object` | The person, when one is named. Display name and email are partner-supplied at mint and are often absent |
| `data.user.id` | `string` |  |
| `data.user.displayName` | `string` |  |
| `data.user.email` | `string` |  |
| `data.org` | `object` | The org the caller acts in. When actingAsTenant is true this is the customer's workspace, not the partner |
| `data.org.id` | `string` |  |
| `data.org.name` | `string` |  |
| `data.org.type` | `string` | platform, company, partner, end_org or personal |
| `data.org.externalRef` | `string` | The partner's own id for this org, when they set one |
| `data.parentOrg` | `object` | The partner org, when the caller acts inside one of its customers. Null otherwise |
| `data.parentOrg.id` | `string` |  |
| `data.parentOrg.name` | `string` | When actingAsTenant is true: the partner's PRODUCT name, or null when it has none. Never the partner's workspace name, which is internal and can be built from an email. Call the provider by this name, or "your provider" when it is null |
| `data.parentOrg.type` | `string` |  |
| `data.parentOrg.externalRef` | `string` |  |
| `data.installationId` | `string` | Echoed from the request, not attested: unlike every other field here it is a client-supplied header on the public partner contract |
| `data.environment` | `string` | The execution environment resolved for THIS request (test or live), not a standing property of the caller |
| `data.permissions` | `object` |  |
| `data.permissions.role` | `string[]` | The enforced baseline for the persona, verbatim. May contain retired resources, which govern nothing |
| `data.permissions.structured` | `object` | Per-resource permissions carried by the token, intersected with the role. When present it NARROWS the role baseline and never widens it: an action is allowed only if both the role and this map allow it |
| `data.permissions.apiKeyGrant` | `string[]` | An API key's stored grant. A ceiling only |
| `data.capability` | `object` | Set when the caller arrived on a scoped hand-off link, binding it to one action and resource |
| `data.capability.action` | `string` |  |
| `data.capability.resourceId` | `string` |  |
| `data.plan` | `object` | The plan the caller's widgets are held to (the workspace's: a customer of a partner gets the partner's plan). Read connectorsPerWidget before building an integration: one widget connects at most 2 apps (the product and one other) on every plan, so give each further app its own widget. null when it could not be resolved. |
| `data.plan.id` | `string` | launch, scale, growth or enterprise (free reads as launch) |
| `data.plan.limits` | `object` |  |
| `data.plan.limits.connectorsPerWidget` | `integer` | Most distinct connectors one widget may list: null = unlimited. A write past it is refused with 403 quota_exceeded, dimension connectors_per_widget. |
| `data.signupProfile` | `object` | What the person said at signup. Null for an API key, embed token or share link, and for anyone who skipped the questions. Read `hint` before using it: `jobRole` sets how technical your wording is, `useCase` is what they first came to build and may already be built, so check their existing workflows before offering it |
| `data.signupProfile.jobRole` | `string` | One of: `engineering_lead`, `product_manager`, `solutions_architect`, `cto_vp_engineering`, `developer`, `devops_sre`, `founder`, `other`. |
| `data.signupProfile.useCase` | `string` | Their signup use case, in their words or as a category |
| `data.signupProfile.hint` | `string` | How to use these answers |
| `data.apiKey` | `object` |  |
| `data.apiKey.mode` | `string` |  |
| `data.apiKey.environment` | `string` |  |

### Get current user's feature entitlements

```http
GET /v1/me/entitlements
```

The resolved feature-entitlement map (key -> boolean) for the caller's org. Any authenticated caller.

Operation: `getMyEntitlements`

**Responses**

* `200`: Entitlement map

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` | Map of feature key to boolean entitlement flag |

### Get the caller's own org/SaaS domain

```http
GET /v1/me/org-domain
```

Caller-context read of the caller's own SaaS domain (any authenticated user). Prefers the user-confirmed onboarding domain over the org-creation domain. Used by agents/MCP to apply the partners-only widget rule.

Operation: `getMyOrgDomain`

**Responses**

* `200`: Org domain

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.domain` | `string` | The caller's own SaaS domain, or null for a personal org / no onboarding |

### Personalized home-screen suggestions for the caller's org

```http
GET /v1/me/suggestions
```

Four org-specific integration suggestions for the home screen, derived from the company's domain research, the integration-complaint corpus, and what the org has connected, built and asked the build agent about. Org-scoped: every member reads the same set, regardless of who onboarded. Regeneration is fired in the background when the set is missing or older than 3 days and is never awaited, the response always returns what is stored, which may be an empty array. Requires operator or above, matching the roles that can launch the orchestrator.

Operation: `getMySuggestions`

**Responses**

* `200`: Suggestion set
* `401`: Unauthenticated
* `403`: Operator or above required

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.suggestions` | `object[]` |  |
| `data.suggestions[].label` | `string` | Chip text, at most 28 characters |
| `data.suggestions[].prompt` | `string` | What is sent to the build agent when the chip is clicked |
| `data.writing` | `boolean` | Whether a set is on its way: true while a generation run is under way, and when none has been tried yet (this read starts one); false once a set is stored, or when the last run wrote nothing (for example a workspace with no domain to research and too short a use case). The onboarding tour shows its loading state only while this is true. |

## Users

### List users in account/customer

```http
GET /v1/users
```

Lists members of the caller's org (paginated on memberships, with user profiles). Requires users.read.

Operation: `listUsers`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `limit` | query | integer | No | Page size, clamped to 1-200. |
| `offset` | query | integer | No |  |
| `org_id` | query | string | No | list this org's members instead of the caller's. |

**Responses**

* `200`: User list

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].email` | `string` |  |
| `data[].firstName` | `string` |  |
| `data[].lastName` | `string` |  |
| `data[].role` | `string` |  |
| `data[].status` | `string` |  |
| `data[].emailVerified` | `boolean` |  |
| `data[].inviteStatus` | `string` | Whether this person still has an invite outstanding. somebody part-way through a two-factor or passkey setup, or carrying a forced password change, is `accepted`, they already have access. Consequence worth planning for: `emailVerified: false` can appear beside `inviteStatus: "accepted"`, because accounts created outside the invite paths hold full access without a verified address. Do not treat this field as an email-verification signal. `unknown` means this member's user profile could not be read at all, it is NOT a synonym for accepted, and clients must not render it as one. One of: `pending`, `accepted`, `unknown`. |
| `data[].createdAt` | `string` | When the membership was created. |
| `data[].expiresAt` | `string` | Membership end date, or null for permanent access. |
| `total` | `integer` |  |

### Invite user to account

```http
POST /v1/users/invite
```

role may also be a custom role id (cr_...) of the target org.

Operation: `inviteUser`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | `string` | Yes |  |
| `firstName` | `string` | No | Must not contain &lt;, >, or invisible characters. |
| `lastName` | `string` | No | Must not contain &lt;, >, or invisible characters. |
| `role` | `string` | No | One of owner, admin, developer, operator, viewer, end_user, or a custom role id (cr_...) of the target org. Default: `"viewer"`. |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `expiresAt` | `string` | No | Time-limited access: when the membership stops being valid. Must be in the future and carry a UTC offset. Omit for permanent access. |

**Responses**

* `200`: The address already had an account, so it was granted membership rather than created. Same shape as the 201.  `emailSent` is the one field a caller must not skip: the invite and the notification are separate steps, and the membership is committed before the mail is attempted, so `emailSent: false` means this person HAS access and has not been told. It is reported, never assumed, it reflects what the mail provider said it did with the message, not merely that some upstream request was accepted. It is false too when the sign-in link could not be built into something the identity provider will honour, in which case nothing was sent rather than something unusable. When it is false, `emailNote` carries a sentence to show the admin, and the right UI is to keep them on the screen and tell them to follow up rather than to render success.
* `201`: User invited. Carries `inviteStatus`: `pending` for a brand-new account, and for an address that already had one whatever its real state is, `accepted` when that person has already verified, so a caller must not assume an invite response means somebody has to act. Whether this person still has an invite outstanding. somebody part-way through a two-factor or passkey setup, or carrying a forced password change, is `accepted`, they already have access. Consequence worth planning for: `emailVerified: false` can appear beside `inviteStatus: "accepted"`, because accounts created outside the invite paths hold full access without a verified address. Do not treat this field as an email-verification signal. Also carries `emailSent`, and a caller that reports "invited" without reading it will tell an admin something untrue. See the 200 response for what it means.
* `400`: Validation error, includes an expires_at that is not ISO-8601 or is in the past

### List current user's account memberships

```http
GET /v1/users/me/memberships
```

Auto-provisions personal account on first call for new users. `data` is ordered for DISPLAY (platform first, then company, then by name) and is NOT a resolution input, read `activeOrgId` to know which org the caller's requests are scoped to.

Operation: `getMyMemberships`

**Responses**

* `200`: List of memberships

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` | Active memberships, display order. |
| `data[].id` | `string` |  |
| `data[].orgId` | `string` |  |
| `data[].orgName` | `string` |  |
| `data[].orgSlug` | `string` |  |
| `data[].orgType` | `string` |  |
| `data[].orgDomain` | `string` |  |
| `data[].parentOrgId` | `string` | NULL for a partner-level org, set for a customer workspace. |
| `data[].role` | `string` |  |
| `data[].isDefault` | `boolean` |  |
| `data[].status` | `string` | One of: `active`, `pending`. |
| `data[].createdAt` | `string` |  |
| `pending` | `object[]` | Memberships awaiting approval. |
| `pending[].id` | `string` |  |
| `pending[].orgId` | `string` |  |
| `pending[].orgName` | `string` |  |
| `pending[].orgSlug` | `string` |  |
| `pending[].orgType` | `string` |  |
| `pending[].orgDomain` | `string` |  |
| `pending[].parentOrgId` | `string` | NULL for a partner-level org, set for a customer workspace. |
| `pending[].role` | `string` |  |
| `pending[].isDefault` | `boolean` |  |
| `pending[].status` | `string` | One of: `active`, `pending`. |
| `pending[].createdAt` | `string` |  |
| `activeOrgId` | `string` | The org the gateway resolves this caller's requests to, from the token's org_id claim falling back to the user's default membership. Null only when the user has no active membership (mid-signup). Clients must act as this org rather than picking one out of `data`. |

### Get the caller's UI preferences

```http
GET /v1/users/me/preferences
```

Returns the calling person's stored dashboard preferences object ({} when none are stored).

Operation: `getMyPreferences`

**Responses**

* `200`: { data: preferences object }

### Merge-update the caller's UI preferences

```http
PATCH /v1/users/me/preferences
```

Shallow-merges the body's keys into the calling person's preferences and returns the result. Unknown keys are stored as-is; nav_layout must be "top" or "side".

Operation: `updateMyPreferences`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `nav_layout` | `string` | No | One of: `top`, `side`. |

**Responses**

* `200`: { data: merged preferences }
* `400`: Body is not a JSON object, or nav_layout is invalid

### Approve pending membership

```http
POST /v1/users/memberships/{id}/approve
```

Approves a pending membership request in the caller's org, making it active. Requires users.invite; 404 when the membership is not pending in this org.

Operation: `approvePendingUser`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Membership id, from GET /api/v1/users/pending |

**Responses**

* `200`: Membership approved; it becomes the user's default org
* `404`: No pending membership with that id in the caller's org
* `409`: Already decided, or the request carries a role a domain join may not grant (owner)

### Reject pending membership

```http
POST /v1/users/memberships/{id}/reject
```

Rejects a pending membership request in the caller's org. Requires users.invite; 404 when the membership is not pending in this org.

Operation: `rejectPendingUser`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Membership id, from GET /api/v1/users/pending |

**Responses**

* `200`: Membership rejected
* `404`: No pending membership with that id in the caller's org
* `409`: Already decided

### List pending membership requests

```http
GET /v1/users/pending
```

Lists membership requests awaiting approval in the caller's org (for example a domain-join). Requires users.read.

Operation: `listPendingUsers`

**Responses**

* `200`: Pending membership requests

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].email` | `string` |  |
| `data[].requestedAt` | `string` |  |

### Get user details

```http
GET /v1/users/{userId}
```

Returns one member of the caller's org with role, status and invite state. userId may be "me" for the calling person; an API key or embed session gets 400 for "me" because it has no fastn user.

Operation: `getUser`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `userId` | path | string | Yes |  |

**Responses**

* `200`: User details, including `inviteStatus` (`pending` or `accepted` only, unlike the list, this route fails the request rather than answering `unknown`) and `emailVerified`. Whether this person still has an invite outstanding. somebody part-way through a two-factor or passkey setup, or carrying a forced password change, is `accepted`, they already have access. Consequence worth planning for: `emailVerified: false` can appear beside `inviteStatus: "accepted"`, because accounts created outside the invite paths hold full access without a verified address. Do not treat this field as an email-verification signal.
* `403`: The user exists but belongs to another org.
* `404`: Not found

### Remove user from account

```http
DELETE /v1/users/{userId}
```

Deactivates the user's membership in the caller's org (suspends it); Refuses the caller themselves, a user ranked above the caller, and the org's only owner.

Operation: `removeUser`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `userId` | path | string | Yes |  |

**Responses**

* `200`: User removed

### List a user's memberships

```http
GET /v1/users/{userId}/memberships
```

Lists the user's account memberships. other roles see only the membership in their own org, and roles below developer may only query themselves.

Operation: `listUserMemberships`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `userId` | path | string | Yes | user id. |
| `limit` | query | integer | No | Page size, clamped to 1-200. |
| `offset` | query | integer | No |  |

**Responses**

* `200`: { data: memberships, total }
* `403`: Caller may only view their own memberships

### Remove a user's membership

```http
DELETE /v1/users/{userId}/memberships/{membershipId}
```

Deletes one membership of the user in an org the caller can write to (its own or a customer beneath it), promoting another default if needed; Refuses the caller's own membership, a user ranked above the caller, and the org's only owner.

Operation: `removeUserMembership`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `userId` | path | string | Yes | user id. |
| `membershipId` | path | string | Yes |  |

**Responses**

* `200`: Membership removed
* `403`: Out of scope, higher role, or last owner
* `404`: Membership not found

### Get a user's permission overrides

```http
GET /v1/users/{userId}/permissions
```

Returns the user's role in the caller's org, its base role (for a custom role), the per-user permission override map, and a custom role's effective permissions. Requires users.read.

Operation: `getUserPermissions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `userId` | path | string | Yes | user id. |

**Responses**

* `200`: { data: { userId, orgId, role, baseRole, customRoleId, customRoleName, permissions, rolePermissions } }
* `404`: No active membership in the current org

### Set a user's permission overrides

```http
PUT /v1/users/{userId}/permissions
```

Replaces the per-user permission override map on the user's membership in the caller's org; permissions: null clears it. owner and admin only; refuses the caller themselves and users ranked above the caller.

Operation: `updateUserPermissions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `userId` | path | string | Yes | user id. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `permissions` | `object` | No | Map of resource id -> { actions, only? }. Resource ids and actions must be ones the RBAC engine knows; retired resource ids are dropped silently. |

**Responses**

* `200`: { data: { userId, permissions } }
* `400`: Unknown resource or action
* `403`: Self or higher-ranked user
* `404`: No active membership in the current org

### Reactivate a suspended user

```http
POST /v1/users/{userId}/reactivate
```

Requires users.remove; 404 when there is no suspended membership here.

Operation: `reactivateUser`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `userId` | path | string | Yes | user id. |

**Responses**

* `200`: { data: { id, reactivated: true } }
* `404`: No suspended membership in this org

### Resend a member's invite email

```http
POST /v1/users/{userId}/resend-invite
```

Re-sends the sign-in invite email to an active member of the caller's org (or the caller's customer). Requires users.invite; 404 when the user is not a member there.

Operation: `resendInvite`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `userId` | path | string | Yes | user id. |

**Responses**

* `200`: { data: { emailSent, email } }
* `404`: Not a member of this organisation

### Update user role

```http
PUT /v1/users/{userId}/role
```

Changes a member's role in the caller's org. Cannot change your own role, assign owner (use ownership transfer), or assign a role above your own.

Operation: `updateUserRole`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `userId` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `role` | `string` | Yes | A system role, or a custom role id (cr_...) of the target org, which is governed by the rules of the role it narrows. |
| `orgId` | `string` | No |  |

**Responses**

* `200`: Role updated

## Roles

### List custom roles for the account

```http
GET /v1/roles
```

Returns the system roles with their permission lists, and the org's custom roles. other members get an empty custom list and zero counts.

Operation: `listRoles`

**Responses**

* `200`: Role list

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].name` | `string` |  |
| `data[].permissions` | `string[]` |  |
| `data[].createdAt` | `string` |  |

### Create a custom role

```http
POST /v1/roles
```

Creates a custom role in the caller's org that narrows a system role (baseRole, default viewer). Requires settings.update; 400 for an unknown resource or action, an empty permission map, a baseRole above the caller's, or a duplicate name.

Operation: `createRole`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `description` | `string` | No |  |
| `permissions` | `object` | Yes | Map of resource id -> { actions, only? }. Resource ids and actions must be ones the RBAC engine knows; retired resource ids are dropped silently. |
| `baseRole` | `string` | No | The system role this custom role narrows. Cannot be above the caller's own role. One of: `owner`, `admin`, `developer`, `operator`, `viewer`, `end_user`. Default: `"viewer"`. |

**Responses**

* `201`: Role created

### Get a role

```http
GET /v1/roles/{id}
```

Returns a system role's permissions, or a custom role of the caller's org with its permission map and baseRole. owner and admin only.

Operation: `getRole`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | A system role name or a custom role id (cr_...). |

**Responses**

* `200`: Role details
* `404`: Custom role not found in this org

### Update a custom role

```http
PUT /v1/roles/{id}
```

Updates a custom role's name, description, permissions or baseRole; omitted fields are unchanged. System roles cannot be modified. Requires settings.update.

Operation: `updateRole`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | A system role name or a custom role id (cr_...). |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `permissions` | `object` | No | Map of resource id -> { actions, only? }. Resource ids and actions must be ones the RBAC engine knows; retired resource ids are dropped silently. |
| `baseRole` | `string` | No | The system role this custom role narrows. Cannot be above the caller's own role. One of: `owner`, `admin`, `developer`, `operator`, `viewer`, `end_user`. Default: `"viewer"`. |

**Responses**

* `200`: Updated

### Delete a custom role

```http
DELETE /v1/roles/{id}
```

Deletes a custom role. Refused for system roles and for a role still assigned to any active member. Requires settings.update.

Operation: `deleteRole`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | A system role name or a custom role id (cr_...). |

**Responses**

* `200`: Deleted

## Grants

### List custom grants

```http
GET /v1/grants
```

Operation: `listGrants`

**Responses**

* `200`: Grant list

### Create custom grant

```http
POST /v1/grants
```

Operation: `createGrant`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `description` | `string` | No |  |
| `permissions` | `string[]` | Yes |  |
| `connectorScope` | `string[]` | No |  |

**Responses**

* `201`: Grant created

### List system-defined grants

```http
GET /v1/grants/system
```

Operation: `listSystemGrants`

**Responses**

* `200`: System grants

### Update grant

```http
PUT /v1/grants/{id}
```

Operation: `updateGrant`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Updated

### Delete grant

```http
DELETE /v1/grants/{id}
```

Operation: `deleteGrant`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted

## Teams

### List teams

```http
GET /v1/teams
```

Operation: `listTeams`

**Responses**

* `200`: Team list

### Create team

```http
POST /v1/teams
```

Operation: `createTeam`

**Responses**

* `201`: Team created

### Get team with members

```http
GET /v1/teams/{id}
```

Operation: `getTeam`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Team

### Update team

```http
PUT /v1/teams/{id}
```

Operation: `updateTeam`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Updated

### Delete team

```http
DELETE /v1/teams/{id}
```

Operation: `deleteTeam`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted

### Add team member

```http
POST /v1/teams/{id}/members
```

Operation: `addTeamMember`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `201`: Member added

### Remove team member

```http
DELETE /v1/teams/{id}/members/{userId}
```

Operation: `removeTeamMember`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `userId` | path | string | Yes |  |

**Responses**

* `200`: Removed
