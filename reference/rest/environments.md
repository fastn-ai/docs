---
description: "Environments, their config values, and secrets."
---

# Environments and secrets

Base URL, authentication and errors are on the [REST API overview](README.md).

## Environments

### List workflow environments

```http
GET /v1/environments
```

The org's workflow environments, ordered default first, then oldest first, then by id as a tiebreak (environments created together in one bulk call share a creation timestamp, so id is what makes the order total). Includes the built-in Live environment (slug 'live', isDefault true, isDeletable false), which every workflow-authoring org is seeded at creation, it is a real row, and its id is what /workflows/{id}/deploy and /workflows/{id}/promote accept. A customer workspace is deliberately not seeded one and can legitimately return an empty list. 'test' is a separate hardcoded environment with no row here; it is a valid env_slug for env-configs only, never a deploy target.

Operation: `listEnvironments`

**Responses**

* `200`: Environment list

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` | wenv_*, the only form /deploy and /promote accept as env_id |
| `data[].name` | `string` |  |
| `data[].slug` | `string` | 'live' for the built-in default environment |
| `data[].isDefault` | `boolean` | The org's production environment. Deploying here also moves the workflow's live code pointer, and /promote requires workflows.deploy_prod rather than deploy_test |
| `data[].isDeletable` | `boolean` | false for the built-in Live environment |
| `data[].requiresReview` | `boolean` | When true, deploys must go through /promote and a merged GitHub PR |
| `data[].createdAt` | `string` |  |

### Create workflow environment

```http
POST /v1/environments
```

Creates a custom (non-default, deletable) environment for the caller's org. The slug is lowercased; every character outside [a-z0-9-] is replaced with '-' one-for-one (hyphens are preserved and runs are NOT collapsed, so 'a  b' becomes 'a--b'); then leading and trailing hyphens are stripped, which is why 'live!' normalizes to 'live' and is rejected as reserved. 'test' and 'live' are both reserved and rejected with 400: 'test' has no row at all, and 'live' is the built-in production environment seeded at org creation, which this route would otherwise create with custom-env flags.

Operation: `createEnvironment`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `slug` | `string` | Yes |  |

**Responses**

* `201`: Created
* `400`: Missing name/slug, or a reserved slug
* `409`: An environment with that slug already exists in this org

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` | wenv_*, the only form /deploy and /promote accept as env_id |
| `data.name` | `string` |  |
| `data.slug` | `string` | 'live' for the built-in default environment |
| `data.isDefault` | `boolean` | The org's production environment. Deploying here also moves the workflow's live code pointer, and /promote requires workflows.deploy_prod rather than deploy_test |
| `data.isDeletable` | `boolean` | false for the built-in Live environment |
| `data.requiresReview` | `boolean` | When true, deploys must go through /promote and a merged GitHub PR |
| `data.createdAt` | `string` |  |

### Toggle review gating for an environment

```http
PATCH /v1/environments/{id}
```

Sets requiresReview. When true, /workflows/{id}/deploy refuses the environment with a 409 and the caller must use /workflows/{id}/promote, which opens a real PR against the org's connected GitHub repo.

Operation: `setEnvironmentReviewRequirement`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Environment id (wenv_*) |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `requiresReview` | `boolean` | Yes |  |

**Responses**

* `200`: Updated
* `400`: requiresReview must be a boolean
* `404`: No such environment in the caller's org

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` | wenv_*, the only form /deploy and /promote accept as env_id |
| `data.name` | `string` |  |
| `data.slug` | `string` | 'live' for the built-in default environment |
| `data.isDefault` | `boolean` | The org's production environment. Deploying here also moves the workflow's live code pointer, and /promote requires workflows.deploy_prod rather than deploy_test |
| `data.isDeletable` | `boolean` | false for the built-in Live environment |
| `data.requiresReview` | `boolean` | When true, deploys must go through /promote and a merged GitHub PR |
| `data.createdAt` | `string` |  |

### Delete workflow environment

```http
DELETE /v1/environments/{id}
```

Deletes a custom workflow environment (requires workflows.delete). The built-in Live environment cannot be deleted (400). 409 ENVIRONMENT_HAS_API_KEYS while an active API key is pinned to it; 403 ENV_NOT_PERMITTED for an API key pinned to a different environment.

Operation: `deleteEnvironment`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted
* `400`: The built-in Live environment cannot be deleted
* `404`: No such environment in the caller's org

## Env configs

### List environment configs

```http
GET /v1/env-configs
```

Every env-config key of the org with its value per environment slug (requires settings.read). Env-configs are plain, non-secret values read by running workflows; use secrets for credentials.

Operation: `listEnvironmentConfigs`

**Responses**

* `200`: { data: [{ key, values: { &lt;envSlug>: value }, updatedAt }] }

### Bulk upsert environment configs

```http
PUT /v1/env-configs
```

Upserts many env-config keys at once, optionally creating the environments they name first (requires workflows.update). Existing environments are kept, 'test' is skipped as built in, and every write is one transaction.

Operation: `bulkUpsertEnvironmentConfigs`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `environments` | `object[]` | No | Environments to ensure exist before writing values. |
| `environments[].name` | `string` | Yes |  |
| `environments[].slug` | `string` | Yes |  |
| `items` | `object[]` | Yes |  |
| `items[].key` | `string` | Yes |  |
| `items[].values` | `object` | Yes | env_slug -> value (any JSON). 'test' and 'live' are built in; any other slug must be an environment of this org (400 otherwise). |

**Responses**

* `200`: { data: { environmentsCreated, environmentsExisting, environmentsSkippedBuiltins, items } }
* `400`: Malformed items or environments, or an unknown env slug

### Get environment config

```http
GET /v1/env-configs/{key}
```

One env-config key with its value per environment slug (requires settings.read).

Operation: `getEnvConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | path | string | Yes |  |

**Responses**

* `200`: { data: { key, values, updatedAt } }
* `404`: Config key not found

### Create environment config

```http
POST /v1/env-configs/{key}
```

Creates a new env-config key with values per environment (requires workflows.update). 409 when the key already exists in any environment; use PUT to change an existing key.

Operation: `createEnvironmentConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `values` | `object` | Yes | env_slug -> value (any JSON). 'test' and 'live' are built in; any other slug must be an environment of this org (400 otherwise). |

**Responses**

* `201`: { data: { key, values } }
* `400`: Invalid key, missing values, or unknown environment
* `409`: Key already exists

### Upsert environment config

```http
PUT /v1/env-configs/{key}
```

Sets the key's value for each environment slug in values, creating the key if needed; environments not named keep their value (requires workflows.update).

Operation: `upsertEnvironmentConfig`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `values` | `object` | Yes | env_slug -> value (any JSON). 'test' and 'live' are built in; any other slug must be an environment of this org (400 otherwise). |

**Responses**

* `200`: { data: { key, values } }
* `400`: Invalid key, missing values, or unknown environment

### Delete environment config

```http
DELETE /v1/env-configs/{key}
```

Deletes the key from one environment when env is given, otherwise from every environment (requires workflows.delete).

Operation: `removeEnvironmentConfigKey`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | path | string | Yes |  |
| `env` | query | string | No | Environment slug; omit to delete the key everywhere. |

**Responses**

* `200`: { data: { deleted: true } }
* `400`: Unknown environment

## Secrets

### List org secrets (names only, values masked)

```http
GET /v1/secrets
```

Lists secret names and metadata (scope, type, orgId, environment); values are never returned. org_id narrows to that customer's secrets plus org-wide ones. An environment-pinned API key sees only its environment, test, and org-wide secrets.

Operation: `listSecrets`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `org_id` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `200`: Secret list

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].name` | `string` |  |
| `data[].type` | `string` | One of: `text`, `json`. |
| `data[].createdAt` | `string` |  |
| `data[].updatedAt` | `string` |  |

### Create a secret

```http
POST /v1/secrets
```

A type of json is validated as JSON on write and fastn.secrets.get() returns it parsed at workflow runtime; text (the default) round-trips the exact string. Value max 8192 characters.

Operation: `createSecret`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `value` | `string` | Yes |  |
| `type` | `string` | No | One of: `text`, `json`. Default: `"text"`. |
| `environment` | `string` | No |  |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `201`: Secret created
* `400`: Invalid JSON value for a json-typed secret, or malformed request body
* `413`: Request body exceeds the 64 KB limit

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` |  |
| `data.name` | `string` |  |
| `data.type` | `string` | One of: `text`, `json`. |
| `data.createdAt` | `string` |  |

### Update a secret value

```http
PUT /v1/secrets/{id}
```

type omitted keeps the stored type, which still decides whether the new value must parse as JSON.

Operation: `updateSecret`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | The secret's name (UPPER_SNAKE_CASE), not its generated id. |
| `org_id` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `environment` | query | string | No | Environment scope of the secret; omitted means no environment narrowing. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | `string` | Yes |  |
| `type` | `string` | No | One of: `text`, `json`. |

**Responses**

* `200`: Secret updated
* `400`: Invalid JSON value for a json-typed secret
* `404`: Not found
* `413`: Request body exceeds the 64 KB limit

### Delete a secret

```http
DELETE /v1/secrets/{id}
```

Deletes the secret with this name at exactly the given scope (org_id + environment; both omitted = the org-wide secret). 404 when no secret matches that scope; 403 when an environment-pinned API key targets another environment.

Operation: `deleteSecret`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | The secret's name (UPPER_SNAKE_CASE), not its generated id. |
| `org_id` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `environment` | query | string | No | Environment scope of the secret; omitted means no environment narrowing. |

**Responses**

* `200`: Secret deleted
* `404`: Not found
