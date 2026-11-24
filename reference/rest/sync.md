---
description: "Jobs that sync records with a connected app, and their runs."
---

# Sync jobs

Base URL, authentication and errors are on the [REST API overview](README.md).

## Sync

### List sync jobs

```http
GET /v1/sync/jobs
```

Lists the org's sync jobs, newest first (requires workflows.read).

Operation: `listSyncJobs`

**Responses**

* `200`: Job list

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].connectorId` | `string` |  |
| `data[].direction` | `string` | One of: `inbound`, `outbound`, `bidirectional`. |
| `data[].entity` | `string` |  |
| `data[].status` | `string` | One of: `active`, `paused`, `running`, `error`. |
| `data[].lastSyncAt` | `string` |  |
| `data[].recordsSynced` | `integer` |  |
| `data[].recordsProcessed` | `integer` |  |
| `data[].recordsFailed` | `integer` |  |
| `data[].recordsSkipped` | `integer` |  |
| `total` | `integer` |  |

### Create sync job

```http
POST /v1/sync/jobs
```

Creates an active sync job for a connector entity (requires workflows.create). direction defaults to inbound; the name is derived from connectorId and entity.

Operation: `createSyncJob`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `entity` | `string` | Yes |  |
| `direction` | `string` | No | One of: `inbound`, `outbound`, `bidirectional`. |

**Responses**

* `201`: Job created

### Get sync job

```http
GET /v1/sync/jobs/{id}
```

Returns one sync job (requires workflows.read). 404 when it is not in the org.

Operation: `getSyncJob`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Job

### Delete sync job

```http
DELETE /v1/sync/jobs/{id}
```

Deletes a sync job (requires workflows.delete). 404 when it is not in the org.

Operation: `deleteSyncJob`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Deleted

### Cancel a parallel sync run

```http
POST /v1/sync/jobs/{id}/cancel
```

Cancels an in-flight parallel sync run. Currently refused with 403 for every caller: the handler checks a permission string the RBAC layer cannot parse.

Operation: `cancelSyncJob`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `runId` | `string` | Yes | The runId returned by POST /api/v1/sync/jobs/{id}/trigger-parallel. |

**Responses**

* `200`: { data: { cancelled: true, syncJobId, runId } }
* `400`: runId missing

### List sync partitions

```http
GET /v1/sync/jobs/{id}/partitions
```

Partition progress of a parallel sync job, optionally for one run, with a summary of counts and processed records. Currently refused with 403 for every caller: the handler checks a permission string the RBAC layer cannot parse.

Operation: `listSyncPartitions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `runId` | query | string | No |  |

**Responses**

* `200`: { data: { summary, partitions } }
* `404`: Sync job not found

### Pause a parallel sync run

```http
POST /v1/sync/jobs/{id}/pause
```

Pauses an in-flight parallel sync run. Currently refused with 403 for every caller: the handler checks a permission string the RBAC layer cannot parse.

Operation: `pauseSyncJob`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `runId` | `string` | Yes | The runId returned by POST /api/v1/sync/jobs/{id}/trigger-parallel. |

**Responses**

* `200`: { data: { paused: true, syncJobId, runId } }
* `400`: runId missing

### Resume a parallel sync run

```http
POST /v1/sync/jobs/{id}/resume
```

Resumes a paused parallel sync run. Currently refused with 403 for every caller: the handler checks a permission string the RBAC layer cannot parse.

Operation: `resumeSyncJob`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `runId` | `string` | Yes | The runId returned by POST /api/v1/sync/jobs/{id}/trigger-parallel. |

**Responses**

* `200`: { data: { resumed: true, syncJobId, runId } }
* `400`: runId missing

### Trigger sync (legacy alias for /run)

```http
POST /v1/sync/jobs/{id}/trigger
```

Runs the sync engine for the job synchronously (requires workflows.execute) and returns the updated job with syncResult (processed, failed, skipped, errors).

Operation: `triggerSync`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Triggered

### Start a parallel sync run

```http
POST /v1/sync/jobs/{id}/trigger-parallel
```

poll the partitions route for progress. batchSize defaults to 500 and maxConcurrency to 20. Currently refused with 403 for every caller: the handler checks a permission string the RBAC layer cannot parse.

Operation: `triggerSyncParallel`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `batchSize` | `integer` | No |  |
| `maxConcurrency` | `integer` | No |  |

**Responses**

* `202`: { data: { syncJobId, runId, workflowId, status, batchSize, maxConcurrency } }
* `404`: Sync job not found
