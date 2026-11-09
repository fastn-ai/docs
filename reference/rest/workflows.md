---
description: "Create, publish, run and inspect workflows."
---

# Workflows

Base URL, authentication and errors are on the [REST API overview](README.md).

## Workflows

### List workflows

```http
GET /v1/workflows
```

Lists the org's workflows (requires workflows.read). A customer also sees the parent org's workflows that were installed for it, with code stripped. Paginated only when limit or offset is passed; the response always carries pagination.total.

Operation: `listWorkflows`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `deleted` | query | boolean | No | Trash view: return ONLY soft-deleted workflows instead of live ones. Requires workflows.delete (developer and above); never cascades to the parent org. Restore one with POST /api/v1/workflows/{id}/restore. |
| `groupBy` | query | string | No | Pass `category` to order the page by category (uncategorised last) so a category's rows are contiguous and a group cannot straddle a page boundary and reappear under a second copy of its own header. Ordering only, it does not filter. The response's `categories` facet carries the per-category totals for the CURRENT filter, across every page. One of: `category`. |
| `label` | query | string | No | Filter by label id. Repeat to narrow: labels AND together, so ?label=a&label=b returns only workflows carrying BOTH. Ids are de-duplicated. Asking for more labels than a workflow can carry (5) is unsatisfiable and returns an empty page rather than a truncated filter. Ids from another workspace match nothing. |
| `status` | query | string | No | Filter by the status the list shows. unpublished: never published (dev_version 0, so /execute answers 409 WORKFLOW_NOT_PUBLISHED whatever enabled says) and no publish awaiting review. in_review: never published, with a publish waiting on its GitHub pull request (orgs that gate publishing). paused: disabled with a published version. published: enabled with a published version that is not deployed to the default (live) environment. live: enabled and deployed to the default environment. These five partition the set. active: enabled with a published version, the union of published and live. An unrecognised value is ignored rather than rejected, so a stale link narrows nothing instead of failing. One of: `unpublished`, `in_review`, `paused`, `published`, `live`, `active`. |
| `updatedWithin` | query | string | No | Only workflows whose updated_at falls inside this window, measured against the database clock. Relative, not an absolute dateFrom: the filter answers "what changed lately", so a shared link still answers it tomorrow. Unrecognised values are ignored. One of: `24h`, `7d`, `30d`. |
| `sort` | query | string | No | Order the list by a column: name (case-insensitive), status (Live, Published, Paused, In review, Unpublished), latest (the published dev_version, NOT the version save-counter) or updated. Applied in SQL because the list is paged - ordering the returned page would sort a page rather than a table. Omitted, the list keeps its default order (newest created first; most recently deleted first in the trash view). Unrecognised values are ignored. One of: `name`, `status`, `latest`, `updated`. |
| `dir` | query | string | No | Sort direction, default desc. Only 'asc' ascends; anything else descends. Ignored without ?sort=. Rows are always tie-broken by id so OFFSET paging cannot repeat or skip a row. One of: `asc`, `desc`. |
| `executionTier` | query | string | No | Only workflows of this tier. Unrecognised values are ignored. One of: `instant`, `standard`, `long`. |
| `search` | query | string | No | Case-insensitive substring match on name, slug and description (first 200 characters). |
| `limit` | query | integer | No | Page size, 1-200. Without limit or offset every workflow is returned. |
| `offset` | query | integer | No |  |

**Responses**

* `200`: Workflow list

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].name` | `string` |  |
| `data[].description` | `string` |  |
| `data[].status` | `string` |  |
| `data[].trigger` | `object` |  |
| `data[].createdAt` | `string` |  |
| `data[].updatedAt` | `string` |  |
| `total` | `integer` |  |

### Create workflow

```http
POST /v1/workflows
```

Creates a workflow (requires workflows.create). The connector manifest is extracted from `code` and merged with any connectorManifest entries sent. 409 when a live workflow in the org already has the slug; 403 quota_exceeded when the org holds its plan's workflow cap; 403 WF-CODE-READONLY when the org may read but not write workflow code.

Operation: `createWorkflow`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `categoryId` | `string` | No |  |
| `slug` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `description` | `string` | No |  |
| `code` | `string` | Yes |  |
| `inputSchema` | `object` | No |  |
| `outputSchema` | `object` | No |  |
| `inputExample` | `any` | No |  |
| `outputExample` | `any` | No |  |
| `executionTier` | `string` | No | One of: `instant`, `standard`, `long`. Default: `"instant"`. |
| `timeoutMs` | `integer` | No | Default: `120000`. |
| `retryPolicy` | `object` | No | Default: `{"maxAttempts": 1, "initialIntervalMs": 5000, "backoffCoefficient": 2, "maximumIntervalMs": 60000}`. |
| `retryPolicy.maxAttempts` | `integer` | No | Default: `1`. |
| `retryPolicy.initialIntervalMs` | `integer` | No | Default: `5000`. |
| `retryPolicy.backoffCoefficient` | `number` | No | Default: `2`. |
| `retryPolicy.maximumIntervalMs` | `integer` | No | Default: `60000`. |
| `escalateOnTimeout` | `boolean` | No | Default: `false`. |
| `enabled` | `boolean` | No | Default: `true`. |
| `testCases` | `object[]` | No |  |
| `testCases[].id` | `string` | Yes |  |
| `testCases[].group` | `string` | Yes |  |
| `testCases[].scenario` | `string` | Yes |  |
| `testCases[].pass` | `string` | Yes |  |
| `testCases[].mode` | `string` | No | One of: `live`, `mock`. |
| `testCases[].input` | `string` | No |  |
| `testCases[].headers` | `string` | No |  |
| `testCases[].mockScenarios` | `object` | No |  |
| `configId` | `string` | No |  |
| `testInput` | `string` | No |  |
| `testHeaders` | `string` | No |  |
| `connectorManifest` | `object[]` | No |  |
| `connectorManifest[].slug` | `string` | Yes |  |
| `connectorManifest[].connectorId` | `string` | No |  |
| `connectorManifest[].orgId` | `string` | No |  |
| `connectorManifest[].retryPolicy` | `object` | No |  |
| `connectorManifest[].retryPolicy.enabled` | `boolean` | No |  |
| `connectorManifest[].retryPolicy.maxAttempts` | `integer` | No |  |
| `connectorManifest[].retryPolicy.initialDelayMs` | `integer` | No |  |
| `connectorManifest[].retryPolicy.backoffMultiplier` | `number` | No |  |
| `connectorManifest[].retryPolicy.maxDelayMs` | `integer` | No |  |
| `connectorManifest[].retryPolicy.maxTotalDelayMs` | `integer` | No |  |
| `connectorManifest[].retryPolicy.retryOnStatuses` | `integer[]` | No |  |
| `connectorManifest[].retryPolicy.retryOnNetworkErrors` | `boolean` | No |  |
| `connectorManifest[].retryPolicy.respectRetryAfter` | `boolean` | No |  |
| `connectorManifest[].retryPolicy.methods` | `string[]` | No |  |
| `connectorManifest[].timeoutMs` | `integer` | No |  |
| `connectorManifest[].actions` | `object[]` | No |  |
| `connectorManifest[].actions[].slug` | `string` | Yes |  |
| `connectorManifest[].actions[].id` | `string` | No |  |
| `connectorManifest[].actions[].version` | `string` | No |  |
| `connectorManifest[].actions[].externalVersion` | `string` | No |  |
| `connectorManifest[].actions[].versionMajor` | `integer` | No |  |
| `connectorManifest[].actions[].manual` | `boolean` | No |  |
| `connectorManifest[].actions[].retryPolicy` | `object` | No |  |
| `connectorManifest[].actions[].retryPolicy.enabled` | `boolean` | No |  |
| `connectorManifest[].actions[].retryPolicy.maxAttempts` | `integer` | No |  |
| `connectorManifest[].actions[].retryPolicy.initialDelayMs` | `integer` | No |  |
| `connectorManifest[].actions[].retryPolicy.backoffMultiplier` | `number` | No |  |
| `connectorManifest[].actions[].retryPolicy.maxDelayMs` | `integer` | No |  |
| `connectorManifest[].actions[].retryPolicy.maxTotalDelayMs` | `integer` | No |  |
| `connectorManifest[].actions[].retryPolicy.retryOnStatuses` | `integer[]` | No |  |
| `connectorManifest[].actions[].retryPolicy.retryOnNetworkErrors` | `boolean` | No |  |
| `connectorManifest[].actions[].retryPolicy.respectRetryAfter` | `boolean` | No |  |
| `connectorManifest[].actions[].retryPolicy.methods` | `string[]` | No |  |
| `connectorManifest[].actions[].timeoutMs` | `integer` | No |  |
| `connectorManifest[].scope` | `string` | No | One of: `SAAS`, `MULTI_TENANT`. |
| `connectorManifest[].connectionId` | `string` | No |  |
| `connectorManifest[].stale` | `boolean` | No |  |

**Responses**

* `201`: Workflow created
* `400`: Validation error
* `403`: The org can read workflow code but not change it (WF-CODE-READONLY). Also returned with error quota_exceeded (dimension flows_per_tenant, plus current, limit, plan and a message) when the org already holds as many workflows as its plan allows; waiting does not clear it, which is why it is not a 429.
* `409`: A workflow with this slug already exists in the org

### List diff-engine run reports

```http
GET /v1/workflows/diff-reports
```

Sync run reports written by fastn.diff (per-run created/updated/deleted/unchanged stats plus capped field-level change details), read from the org's workspace schema.

Operation: `listWorkflowDiffReports`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `scope` | query | string | No | Logical baseline key (e.g. hubspot-company-sync) |
| `entity` | query | string | No |  |
| `workflow_id` | query | string | No |  |
| `limit` | query | integer | No |  |
| `before` | query | string | No | Only reports created before this instant (keyset paging) |

**Responses**

* `200`: Diff run reports (newest first)

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].scope` | `string` |  |
| `data[].entity` | `string` |  |
| `data[].runId` | `string` |  |
| `data[].executionId` | `string` |  |
| `data[].workflowId` | `string` |  |
| `data[].stats` | `object` |  |
| `data[].details` | `object[]` |  |
| `data[].createdAt` | `string` |  |

### List executions across all workflows

```http
GET /v1/workflows/executions
```

Org-wide execution list, newest first. eventId/triggerId match the x-fastn-event-id / x-fastn-trigger-id headers stamped by the event pipeline on every dispatch, so a trigger fire can be correlated to its execution in one query. sort=duration lists finished runs slowest first and needs dateFrom within 30 days of dateTo (400 otherwise). List rows are metadata: they omit input, output, logs and trace (hasTrace flags a trace), and requestHeaders carries only x-fastn-event-id / x-fastn-trigger-id; outputCounts reports the run's record counts. outcome is "skipped" for a completed run that ended through fastn.skip(reason), with the reason in skipReason (null for a role that cannot read run bodies); both are null on every other run. Fetch a run's bodies from the per-execution detail route.

Operation: `listWorkflowExecutions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |
| `status` | query | string | No | Comma-separated statuses; matches any of them. |
| `workflowId` | query | string | No |  |
| `installationId` | query | string | No |  |
| `eventId` | query | string | No |  |
| `triggerId` | query | string | No |  |
| `parentExecutionId` | query | string | No | Only the sub-flow runs this execution started (fastn.flow.invoke, invokeAsync, map); each row's parentExecutionId names its parent. Still inside the caller's org scope. Present but empty matches nothing rather than every execution. |
| `dateFrom` | query | string | No |  |
| `dateTo` | query | string | No |  |
| `search` | query | string | No | Case-insensitive match against workflow name/slug, execution id, status, triggered-by, error category, and the dispatched event and trigger ids. |
| `searchIn` | query | string | No | payload also matches search against each run's input body, e.g. a record id the sender put in a webhook, as a WHOLE value (75073605 does not match 1750736050). Ids are matched whole too, and workflow names by substring. Requires workflows.execute (403 otherwise), a search of at least 3 characters, and a dateFrom no more than 7 days before dateTo (or now); anything else is a 400. Applies to /workflows/executions/counts too. One of: `payload`. |
| `sort` | query | string | No | duration lists finished runs slowest first; it needs dateFrom within 30 days of dateTo (400 otherwise). Omitted, newest first. One of: `duration`. |

**Responses**

* `200`: Execution list rows with workflow name/slug/version/tier. Any `search` walks the window newest-first within a time budget and also returns `payloadSearch: { complete, searchedFrom, hasMore, unsearched }` (the name predates ordinary searches using it): `complete: false` with `hasMore: false` means it stopped at `searchedFrom` before reaching dateFrom. With a `search`, `pagination.total` is a floor (`totalIsLowerBound`), and with no dateFrom the search covers the last 90 days, the longest any run is retained. /workflows/executions/counts with a `search` caps at 1000 matches and sets isLowerBound.
* `400`: dateFrom/dateTo is not an ISO 8601 date or date-time (VALIDATION_ERROR), or searchIn=payload without a short enough window or a long enough search
* `403`: searchIn=payload from a role that cannot read execution bodies

### Count executions by status

```http
GET /v1/workflows/executions/counts
```

Per-status execution totals for the same scope and filters as GET /api/v1/workflows/executions, minus status, so each count is what that status filter would list (requires workflows.read). With a search the scan is capped and isLowerBound marks a floor.

Operation: `getWorkflowExecutionCounts`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `workflowId` | query | string | No | Comma-separated workflow ids. |
| `dateFrom` | query | string | No | ISO 8601 date or date-time; anything else is a 400. |
| `dateTo` | query | string | No | ISO 8601 date or date-time; anything else is a 400. |
| `search` | query | string | No | Same matching as the execution list's search. |
| `searchIn` | query | string | No | payload also matches search against run input bodies; same role and window limits as the execution list. One of: `payload`. |

**Responses**

* `200`: { data: { total, byStatus } }
* `400`: Invalid date or searchIn
* `403`: searchIn=payload from a role that cannot read execution bodies

### Search log lines across executions

```http
GET /v1/workflows/executions/logs
```

The fastn.loki and mirrored console.* lines of every run the caller can see, read from the log store: the newest `limit` matches, returned oldest first. Every line's run is re-checked against the executions the caller may read, and a line whose run is not visible is dropped, so `lines` can be shorter than `limit` while `truncated` is true. With `since` (the previous answer's `cursor`) it is a live-tail poll: the newest lines from 15s before that cursor, so lines that reached the log store late are not lost; drop the ones already shown. `since` is clamped inside the dateFrom/dateTo window, so it can never widen the search, and one past dateTo answers no lines. `cursor` is the newest line the log store answered (visible or not), never behind `since`, and with no lines the end of the window on the server's clock. The run-end line each run writes (`source: fastn.run`, the log store label `status`) is not returned. Lines are kept for the log store's retention (14 days on the run-logs instance), not the run's. Requires workflows.execute to see lines: other roles get 200 with `available: false, reason: redacted`. the log store unset or failing is 200 with `available: false` and a reason.

Operation: `searchExecutionLogs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `q` | query | string | No | Case-insensitive text matched literally against the whole line, message and logged data alike. |
| `workflowId` | query | string | No |  |
| `level` | query | string | No | One of: `debug`, `info`, `warn`, `error`. |
| `dateFrom` | query | string | No | Default: one hour before dateTo. At most 7 days before dateTo. |
| `dateTo` | query | string | No | Default: now. |
| `since` | query | string | No | Live tail: the previous answer's cursor (nanoseconds). Clamped to the window. |
| `limit` | query | integer | No |  |

**Responses**

* `200`: `{ source: [{ ts, tsNs, level, source, message, executionId, workflowId, data }], truncated, runs: { <executionId>: { workflowId, workflowName, status } }, cursor }`
* `400`: A window over 7 days or ending before it starts, an unknown level, a malformed since, or a limit outside 1-1000 (VALIDATION_ERROR)

### Get an execution by its id alone

```http
GET /v1/workflows/executions/{executionId}
```

The same execution detail as GET /api/v1/workflows/{id}/executions/{executionId}, for a caller that holds only the execution id (for example the X-Execution-Id header of an instant run). Same scope, same body gating, same response (requires workflows.read). 404 when the run does not exist or is not in the caller's scope.

Operation: `getExecutionById`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `executionId` | path | string | Yes |  |

**Responses**

* `200`: { data: execution, bodiesSource }
* `404`: Execution not found in the caller's scope

### Rate an execution's error diagnosis

```http
POST /v1/workflows/executions/{executionId}/feedback
```

Records whether the AI error diagnosis shown for a failed execution was helpful (requires workflows.read). helpful is required; rating outside 1-5 is ignored and comment is cut to 1000 characters.

Operation: `submitWorkflowExecutionFeedback`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `executionId` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `helpful` | `boolean` | Yes |  |
| `rating` | `integer` | No |  |
| `comment` | `string` | No |  |

**Responses**

* `200`: Feedback recorded
* `400`: helpful missing or not a boolean
* `404`: Execution not found

### List fastn.state keys

```http
GET /v1/workflows/state-keys
```

Discovery endpoint: lists existing fastn.state keys for the org so new workflows avoid key collisions.

Operation: `listWorkflowStateKeys`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `prefix` | query | string | No |  |
| `limit` | query | integer | No |  |

**Responses**

* `200`: State keys with values and last update time

### List workspace DB tables

```http
GET /v1/workflows/tables
```

Discovery endpoint: lists tables in the org's workspace schema, or inspects one table's columns and row count when tableName is passed.

Operation: `listWorkflowTables`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `tableName` | query | string | No |  |

**Responses**

* `200`: Table list or table detail
* `404`: Table not found

### Test workflow code (scratch-pad)

```http
POST /v1/workflows/test
```

Runs the code in the request body, in the sandbox, without saving it. NOTE this does not run a stored workflow: `code` is what executes, and it is required, see POST /api/v1/workflows/{id}/test to run a saved one. `workflowId` is optional context, used to resolve the same installation (connection pins and inline config) a real dispatch of that workflow would use; it must name a workflow in the caller's org, and 404s if not, so a mistyped id is not mistaken for a successful run. When it is passed and the run succeeds with a non-empty input, that workflow's inputSchema/inputExample are re-derived from the input and testInput/testHeaders are saved as its Test-panel defaults.

Operation: `runWorkflowCode`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes |  |
| `input` | `object` | No |  |
| `headers` | `object` | No |  |
| `mockMode` | `boolean` | No |  |
| `partialMock` | `boolean` | No |  |
| `mockScenarios` | `object` | No |  |
| `timeoutMs` | `integer` | No |  |
| `workflowId` | `string` | No | Optional. Runs the body's code in this workflow's installation context. Must exist in the caller's org. |
| `verification` | `object` | No | Optional. Runs contained: every connector call is mocked unless its `slug.action` is listed in liveReadActions; fastn.db statements run inside a transaction that is rolled back; fastn.state / checkpoint / envConfig writes stay in memory; fetch sends only GET/HEAD/OPTIONS and answers anything else locally; sub-flows, fastn.diff, unified writes, fastn.ai.complete (it would spend the customer's AI credits) and file uploads stop the run. The run is never saved as the workflow's test contract. The response carries a `verification` record: connectorCalls (slug, action, mode, input, ok, error), suppressed side effects, dbStatementsRolledBack, and isolationError when the run was stopped. |
| `verification.liveReadActions` | `string[]` | No | `slug.action` keys the caller vouches are reads; only these reach the vendor. |

**Responses**

* `200`: Run result with logs and trace
* `400`: Validation error, the body is not a JSON object, or `code` is missing or not a string. Code: VALIDATION_ERROR. Also refused with VALIDATION_ERROR when the session acts for a customer (an embed token or customer-scoped key, which carries a parent org) but names no customer and the body names no x-org-id, so the run would otherwise use the partner's connections.
* `403`: x-fastn-env named in the body headers is outside the caller's environment pin: a test key (or a token minted with it) may run only 'test', a key made for one environment only that environment and 'test'. The gateway never sees the body, so it is held to the pin here. Code: ENV_NOT_PERMITTED.
* `404`: workflowId was supplied but names no workflow in this org
* `408`: The run exceeded the synchronous test budget (25s by default, so the answer fits the gateway's request budget). Code: WF-TEST-TIMEOUT. Carries the trace and step summary.
* `413`: The workflow returned a result larger than WORKFLOW_MAX_RESULT_BYTES (default 8 MiB). Code: WF-RESULT-TOO-LARGE.
* `422`: The workflow itself failed: a throw or syntax error in its code, a connector call it did not handle, a top-level declaration of a name the sandbox already defines (fastn, Fastn, FastnClient, module), or the sandbox memory limit. Code: WF-CODE-ERROR, or WF-MEMORY-LIMIT for the memory limit. Carries error, stack, errorCategory, fixSuggestion, the trace and step summary.
* `429`: The org has used its monthly runs (error quota_exceeded, dimension executions_per_month), or its instant concurrency slots or this pod's sandbox slots are all in use (RATE_LIMITED, Retry-After 5). Test runs pass the same gates as POST /{id}/execute; a platform service calling directly is not metered.
* `500`: A platform fault, not the workflow. Code: WF-EXEC-FAILED, with the requestId to quote when reporting it.

### Get workflow

```http
GET /v1/workflows/{id}
```

Returns one workflow by id, including its labels (requires workflows.read). A customer may read a parent-owned workflow only when it was installed for it, and then without its code. 404 when not found or not visible.

Operation: `getWorkflow`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Workflow
* `404`: Not found

### Update workflow

```http
PUT /v1/workflows/{id}
```

Partial update of a workflow (requires workflows.update): only the fields sent are changed. `documentation` is rejected with 400; send documentationOverride to edit the partner-facing doc. A body carrying `code` is refused with 403 WF-CODE-READONLY when the org may read but not write workflow code. Changing only enabled, categoryId or documentationOverride does not bump the version.

Operation: `updateWorkflow`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `categoryId` | `string` | No |  |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `code` | `string` | No |  |
| `inputSchema` | `object` | No |  |
| `outputSchema` | `object` | No |  |
| `inputExample` | `any` | No |  |
| `outputExample` | `any` | No |  |
| `executionTier` | `string` | No | One of: `instant`, `standard`, `long`. |
| `timeoutMs` | `integer` | No |  |
| `retryPolicy` | `object` | No |  |
| `retryPolicy.maxAttempts` | `integer` | No | Default: `1`. |
| `retryPolicy.initialIntervalMs` | `integer` | No | Default: `5000`. |
| `retryPolicy.backoffCoefficient` | `number` | No | Default: `2`. |
| `retryPolicy.maximumIntervalMs` | `integer` | No | Default: `60000`. |
| `escalateOnTimeout` | `boolean` | No |  |
| `configId` | `string` | No |  |
| `enabled` | `boolean` | No |  |
| `testCases` | `object[]` | No |  |
| `documentationOverride` | `object` | No |  |
| `documentationOverride.audience` | `string` | Yes | One of: `end_user`, `technical`. |
| `documentationOverride.markdown` | `string` | Yes |  |
| `testInput` | `string` | No |  |
| `testHeaders` | `string` | No |  |
| `connectorManifest` | `object[]` | No |  |
| `connectorManifest[].slug` | `string` | Yes |  |
| `connectorManifest[].connectorId` | `string` | No |  |
| `connectorManifest[].orgId` | `string` | No |  |
| `connectorManifest[].retryPolicy` | `object` | No |  |
| `connectorManifest[].retryPolicy.enabled` | `boolean` | No |  |
| `connectorManifest[].retryPolicy.maxAttempts` | `integer` | No |  |
| `connectorManifest[].retryPolicy.initialDelayMs` | `integer` | No |  |
| `connectorManifest[].retryPolicy.backoffMultiplier` | `number` | No |  |
| `connectorManifest[].retryPolicy.maxDelayMs` | `integer` | No |  |
| `connectorManifest[].retryPolicy.maxTotalDelayMs` | `integer` | No |  |
| `connectorManifest[].retryPolicy.retryOnStatuses` | `integer[]` | No |  |
| `connectorManifest[].retryPolicy.retryOnNetworkErrors` | `boolean` | No |  |
| `connectorManifest[].retryPolicy.respectRetryAfter` | `boolean` | No |  |
| `connectorManifest[].retryPolicy.methods` | `string[]` | No |  |
| `connectorManifest[].timeoutMs` | `integer` | No |  |
| `connectorManifest[].actions` | `object[]` | No |  |
| `connectorManifest[].actions[].slug` | `string` | Yes |  |
| `connectorManifest[].actions[].id` | `string` | No |  |
| `connectorManifest[].actions[].version` | `string` | No |  |
| `connectorManifest[].actions[].externalVersion` | `string` | No |  |
| `connectorManifest[].actions[].versionMajor` | `integer` | No |  |
| `connectorManifest[].actions[].manual` | `boolean` | No |  |
| `connectorManifest[].actions[].retryPolicy` | `object` | No |  |
| `connectorManifest[].actions[].retryPolicy.enabled` | `boolean` | No |  |
| `connectorManifest[].actions[].retryPolicy.maxAttempts` | `integer` | No |  |
| `connectorManifest[].actions[].retryPolicy.initialDelayMs` | `integer` | No |  |
| `connectorManifest[].actions[].retryPolicy.backoffMultiplier` | `number` | No |  |
| `connectorManifest[].actions[].retryPolicy.maxDelayMs` | `integer` | No |  |
| `connectorManifest[].actions[].retryPolicy.maxTotalDelayMs` | `integer` | No |  |
| `connectorManifest[].actions[].retryPolicy.retryOnStatuses` | `integer[]` | No |  |
| `connectorManifest[].actions[].retryPolicy.retryOnNetworkErrors` | `boolean` | No |  |
| `connectorManifest[].actions[].retryPolicy.respectRetryAfter` | `boolean` | No |  |
| `connectorManifest[].actions[].retryPolicy.methods` | `string[]` | No |  |
| `connectorManifest[].actions[].timeoutMs` | `integer` | No |  |
| `connectorManifest[].scope` | `string` | No | One of: `SAAS`, `MULTI_TENANT`. |
| `connectorManifest[].connectionId` | `string` | No |  |
| `connectorManifest[].stale` | `boolean` | No |  |

**Responses**

* `200`: Updated
* `403`: Only when the body carries `code`: the org can read workflow code but not change it (WF-CODE-READONLY). A rename, description or enable-toggle that sends no `code` is unaffected.

### Delete workflow

```http
DELETE /v1/workflows/{id}
```

Soft-deletes by default: the row is retained with deleted=true, stays listable via GET /api/v1/workflows?deleted=true, and is restorable via POST /api/v1/workflows/{id}/restore. It stops being executable immediately (/execute filters deleted=false), so any live trigger routing to it stops delivering, a trigger whose every route points at trashed workflows answers 404 ROUTE_TARGET_GONE instead of 202 until one is restored. Pass permanent=true to drop the row and its executions irreversibly.

Operation: `deleteWorkflow`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `permanent` | query | boolean | No | Hard-delete the workflow and its executions. Not restorable. |

**Responses**

* `200`: Deleted
* `409`: Workflow has in-flight executions

### Edit workflow code by exact string replacement

```http
PATCH /v1/workflows/{id}/code
```

Replaces oldString with newString in the workflow's current code and publishes the result as a new version immediately, re-extracting its connector manifest from the new code as publishWorkflow does (requires workflows.update). oldString must occur exactly once unless replaceAll is true (409 on multiple matches, 404 when absent). The response carries a regressionGate when the workflow has test cases to re-run. 403 WF-CODE-READONLY when the org may read but not write workflow code.

Operation: `editWorkflowCode`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `oldString` | `string` | Yes |  |
| `newString` | `string` | No | Defaults to an empty string; must differ from oldString. |
| `replaceAll` | `boolean` | No | Default: `false`. |

**Responses**

* `200`: { data: { id, changedBytes, published, regressionGate, workflow, version } }
* `400`: oldString missing, or identical to newString
* `404`: Workflow not found, or oldString not found in its code
* `409`: oldString matches more than once and replaceAll is not true

### Deploy a published version to an environment

```http
POST /v1/workflows/{id}/deploy
```

Deploys a published workflow version (wv_*) to one environment. env_id must be a wenv_* id belonging to the caller's org, the environment slug is not accepted. Deploying to the default environment also updates the workflow's live code pointer. An environment with requiresReview set is refused here; use /promote.

Operation: `deployWorkflowVersion`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `env_id` | `string` | Yes | Environment id (wenv_*), from GET /api/v1/environments |
| `version_id` | `string` | Yes | Published version id (wv_*) |

**Responses**

* `200`: Deployed
* `400`: env_id or version_id missing
* `403`: The org can read workflow code but not change it (WF-CODE-READONLY). Deploying to the default environment rewrites the live code pointer, so it is refused for a read-only org.
* `404`: Environment not found in this org, or version not found for this workflow
* `409`: Environment requires review, use /promote

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` |  |
| `data.envId` | `string` |  |
| `data.envSlug` | `string` |  |
| `data.versionId` | `string` |  |
| `data.envVersion` | `integer` |  |
| `data.deployedAt` | `string` |  |

### List workflow deployments

```http
GET /v1/workflows/{id}/deployments
```

Deployment history of the workflow, grouped by environment slug, newest env_version first, with isActive marking what each environment runs (requires workflows.read).

Operation: `listWorkflowDeployments`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: { &lt;envSlug>: deployment[] } }

### Get workflow documentation

```http
GET /v1/workflows/{id}/docs
```

Returns the workflow's stored documentation for one audience. audience=end_user (default) is the operator-facing help-center doc plus flow-step and sequence artifacts; audience=technical is the solution-engineer doc covering connector actions used, the input/output contract, and reliability behavior. format=structured (default) additionally returns the workflow's live contract (triggers, connector actions, schemas, execution settings) so partners can re-render the content into their own help center; format=markdown returns just the doc text with freshness metadata. Every response carries generatedAt and a stale flag (true when the workflow changed after the doc was generated).

Operation: `getWorkflowDocs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Workflow id (wf_*) or slug |
| `audience` | query | string | No | One of: `end_user`, `technical`. |
| `format` | query | string | No | One of: `structured`, `markdown`. |

**Responses**

* `200`: Documentation
* `400`: Invalid audience or format
* `404`: Workflow not found, or that audience's doc has not been generated yet. The latter carries a hint plus lastGeneration - the outcome of the most recent generation attempt for that audience ({ status: 'ok' \| 'failed', at, error? }), or null when no attempt has been recorded. Generation is fire-and-forget behind a 202, so this is how a caller tells 'still running' from 'failed' rather than polling the 404 forever.

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.workflowId` | `string` |  |
| `data.audience` | `string` |  |
| `data.generatedAt` | `string` |  |
| `data.stale` | `boolean` |  |
| `data.workflowUpdatedAt` | `string` |  |
| `data.workflowVersion` | `integer` |  |
| `data.markdown` | `string` |  |
| `data.sections` | `object[]` | The doc split into its H2 sections (heading null = the H1 preamble), a derived view of markdown for template-based renderers |
| `data.sections[].heading` | `string` |  |
| `data.sections[].markdown` | `string` |  |
| `data.fieldMappings` | `object[]` | The Field mapping table as data; [] when the doc has no parseable table, a convenience view, markdown stays canonical |
| `data.fieldMappings[].source` | `string` |  |
| `data.fieldMappings[].destination` | `string` |  |
| `data.fieldMappings[].notes` | `string` |  |
| `data.slug` | `string` |  |
| `data.name` | `string` |  |
| `data.description` | `string` |  |
| `data.flowSteps` | `object[]` |  |
| `data.sequencePhases` | `object` |  |
| `data.sequenceMermaid` | `string` |  |
| `data.triggers` | `object[]` |  |
| `data.connectorActions` | `object[]` |  |
| `data.connectorActions[].slug` | `string` |  |
| `data.connectorActions[].actions` | `string[]` |  |
| `data.inputSchema` | `object` |  |
| `data.outputSchema` | `object` |  |
| `data.inputExample` | `any` |  |
| `data.executionTier` | `string` |  |
| `data.timeoutMs` | `integer` |  |

### List saved documentation versions

```http
GET /v1/workflows/{id}/docs/history
```

Every doc generation and every override save appends a version row (capped per workflow/audience/kind), so a bad regeneration is diffable and revertible. Returns metadata only, newest first; fetch one version's full content via /docs/history/{versionId}.

Operation: `listWorkflowDocVersions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `audience` | query | string | No | One of: `end_user`, `technical`. |
| `kind` | query | string | No | One of: `generated`, `override`. |
| `limit` | query | integer | No |  |

**Responses**

* `200`: Version metadata list
* `404`: Workflow not found

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].audience` | `string` |  |
| `data[].kind` | `string` |  |
| `data[].createdBy` | `string` |  |
| `data[].createdAt` | `string` |  |
| `data[].markdownLength` | `integer` |  |

### Get one saved documentation version

```http
GET /v1/workflows/{id}/docs/history/{versionId}
```

Returns one saved documentation version (generated or override) with its full content (requires workflows.read). The workflow may be named by id or slug. 404 when the workflow or version is not found.

Operation: `getWorkflowDocVersion`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `versionId` | path | string | Yes |  |

**Responses**

* `200`: Full version content
* `404`: Workflow or version not found

### Save workflow draft code

```http
PATCH /v1/workflows/{id}/draft
```

Saves code as the workflow's unpublished draft without publishing or changing what runs (requires workflows.update). POST /api/v1/workflows/{id}/publish makes the draft live. 403 WF-CODE-READONLY when the org may read but not write workflow code.

Operation: `saveWorkflowDraft`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes |  |

**Responses**

* `200`: { data: { saved: true } }
* `400`: code missing
* `404`: Workflow not found

### Execute workflow

```http
POST /v1/workflows/{id}/execute
```

Behaviour depends on the workflow's executionTier, and callers must handle both. STANDARD and LONG queue the run and return 202 with an executionId to poll. INSTANT runs synchronously and returns 200 with the finished result, it holds the HTTP request for the duration, which is the point of the tier, so there is nothing to poll. On the instant path the id appears ONLY in the X-Execution-Id response header, the body is the workflow's own return value and has nowhere to put it, so use that header to correlate a synchronous run. The queued path does not set that header; its id is in data.executionId. A caller written to poll unconditionally will break on an instant-tier workflow. An instant timeout on a workflow with escalateOnTimeout also returns 202, naming the escalated standard run in escalatedTo/escalatedFrom. Send Idempotency-Key to make a retry safe: a duplicate returns the existing execution for the same customer instead of running again, 200 once it has finished, 202 while it is still in flight, and resolves to the escalated run where a timeout escalated. By default that duplicate answer is the execution record ({ data: execution }, the run's return value under data.output); send x-fastn-idempotency-replay: output to get the same body the first call got instead.

Operation: `executeWorkflow`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `x-fastn-idempotency-replay` | header | string | No | Only with Idempotency-Key. 'output' makes a duplicate answer exactly as the original call did: an instant run's own return value as { data: &lt;return value> } with its status code (a run still in flight is 202 { data: { executionId, status } }; a failed run is its error). The same key sent with a different input or for a different workflow is refused with 400 IDEMPOTENCY_KEY_REUSED. Omitted, a duplicate returns the execution record, unchanged from before. One of: `output`. |
| `Idempotency-Key` | header | string | No | Client-supplied dedup key. Scoped to the execution's (owner org, customer); no expiry window beyond the execution's retention. The prefix fastn-event: is reserved for trigger dispatch and is refused with 400 (reserved_idempotency_key); keys with it replay only an in-flight or completed run from the last 24 hours. Rarely, concurrent requests under one key are answered 503 (idempotency_key_contended) with nothing created; retry. A fastn-event: key whose run exists but was not yet handed to an engine is answered 409 (dispatch_run_not_started); retry. |
| `x-fastn-env` | header | string | No | Which environment to execute against, and therefore WHICH CODE RUNS. 'test' runs the workflow's latest published version; any other slug runs the version actively deployed to that environment. Omitted, it defaults to the credential's own mode: a fsk_test_ key gets 'test', a fsk_live_ key gets 'live'. A test key may ONLY name 'test', asking for anything else is refused with 403 ENV_NOT_PERMITTED rather than quietly downgraded, so a 200 always means the environment you asked for is the one that ran. A live key pinned to an environment (workflowEnvId) defaults to that environment, may also name 'test', and is refused for any other. A live key made before keys were pinned may name any environment, including 'test'. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `input` | `object` | No |  |

**Responses**

* `200`: Instant tier only, the run finished synchronously and this IS the result. No polling. The executionId is in the X-Execution-Id response header.
* `202`: Standard and long tiers, the run was queued. Poll GET /api/v1/workflows/{id}/executions/{executionId} for the result, the workflow id is part of the path. No X-Execution-Id header on this path; read data.executionId.
* `403`: The credential may not execute against the requested x-fastn-env. A test-mode API key is pinned to the 'test' environment; use a live key to target a deployed environment. Code: ENV_NOT_PERMITTED.
* `404`: No active deployment exists for the requested environment. The workflow has been published but never deployed there, deploy a version to that environment, or call with x-fastn-env: test to run the latest published version.
* `408`: Instant tier only, the run exceeded its timeout. Carries executionId and durationMs.
* `409`: The workflow has no published version at all, so there is nothing to run. Publish a snapshot, or use POST /api/v1/workflows/{id}/test to run the draft. Code: WORKFLOW_NOT_PUBLISHED.
* `413`: The workflow returned a result larger than WORKFLOW_MAX_RESULT_BYTES (default 8 MiB). The run is recorded as failed with errorCategory 'configuration' and no output is stored - the oversized result is rejected, never truncated. Return a summary, paginate the response, or write the data to storage and return a reference to it.

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.executionId` | `string` |  |
| `data.workflowId` | `string` |  |
| `data.status` | `string` | One of: `pending`, `queued`. |
| `data.escalatedFrom` | `string` | Instant execution whose timeout triggered the escalation |
| `data.escalatedTo` | `string` | One of: `standard`. |
| `data.stepsTotal` | `integer` |  |
| `data.stepsCompleted` | `integer` |  |
| `data.startedAt` | `string` |  |
| `data.message` | `string` |  |

### List workflow executions

```http
GET /v1/workflows/{id}/executions
```

Execution history of one workflow, newest first (requires workflows.read). limit is capped at 100; a non-integer limit, offset or status_code is a 400.

Operation: `listExecutions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No | At most 1000 (400 otherwise); page deeper with cursor. Ignored with a cursor. |
| `cursor` | query | string | No | The previous page's pagination.nextCursor; the page starts after that run. Opaque. |
| `status` | query | string | No |  |
| `status_code` | query | integer | No |  |

**Responses**

* `200`: `{ data: Execution[], pagination: { limit, nextCursor } }`. nextCursor is null when the page came back short.
* `400`: A filter value is malformed, offset is over 1000, or the cursor was not issued by this list (VALIDATION_ERROR)

### Get execution with steps

```http
GET /v1/workflows/{id}/executions/{executionId}
```

One execution with its steps, logs and trace (requires workflows.read). id is the workflow id (wf_...) and executionId the run id (exec_...); both are required here. With only the run id, use GET /api/v1/workflows/executions/{executionId} (getExecutionById). Log and trace bodies are omitted for roles that cannot read execution bodies. 404 when the run is not in the caller's scope.

Operation: `getWorkflowExecution`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `executionId` | path | string | Yes |  |

**Responses**

* `200`: Execution detail. `bodiesSource` says where input, request headers, output, logs and trace came from: `outcome` is `skipped` for a completed run that ended through fastn.skip(reason), with the reason in `skipReason` (null for a role that cannot read run bodies).

### Cancel a running execution

```http
DELETE /v1/workflows/{id}/executions/{executionId}
```

Marks a pending, queued or running execution cancelled and stops its engine run (requires workflows.execute). A finished run is left unchanged; the response is still 200.

Operation: `cancelWorkflowExecution`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `executionId` | path | string | Yes |  |

**Responses**

* `200`: { data: { cancelled: true, id } }
* `404`: Execution not found in the caller's scope

### Get an execution's log lines from the log store

```http
GET /v1/workflows/{id}/executions/{executionId}/logs
```

The run's fastn.loki lines and mirrored console.* lines, read back from the log store: the most recent `limit` lines, returned oldest first. A run past its hourly shipping budget (5000 lines an hour) has a warn line for each hour it dropped lines, saying how many. Scoped exactly like the execution detail route. Lines an inline sub-flow (fastn.flow.invoke) wrote are included, each naming its own executionId. Never a 5xx for the log store trouble: false and a reason, and the run's stored console lines remain on the detail route. A role without workflows.execute gets available: false, reason: redacted, as for every other run body.

Operation: `getExecutionLogs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `executionId` | path | string | Yes |  |
| `limit` | query | integer | No | Lines to return. Absent or blank uses the default; anything outside 1-5000 is a 400. |

**Responses**

* `200`: Log lines, or why there are none
* `400`: `limit` is not a whole number between 1 and 5000
* `404`: Execution not found in the caller's scope

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.source` | `string` | Where this answer came from. this route reads nothing else. |
| `data.available` | `boolean` |  |
| `data.reason` | `string` | One of: `not_configured`, `query_failed`, `redacted`. |
| `data.truncated` | `boolean` | True when the page is full. |
| `data.lines` | `object[]` |  |
| `data.lines[].ts` | `string` |  |
| `data.lines[].level` | `string` | One of: `debug`, `info`, `warn`, `error`. |
| `data.lines[].source` | `string` | One of: `fastn.loki`, `console`. |
| `data.lines[].message` | `string` |  |
| `data.lines[].executionId` | `string` |  |
| `data.lines[].data` | `any` | The data object passed to fastn.loki, if any. |

### Replay a finished execution

```http
POST /v1/workflows/{id}/executions/{executionId}/replay
```

Re-runs a finished execution with its original input, request headers and customer/installation binding, at the tier that run actually used rather than the workflow's currently configured tier. Runs the current code for the resolved environment (x-fastn-env / ?env=), since executions do not record the version they ran. Refuses a run that is still pending/queued/running (409), and a run whose installation is no longer active (409). Instant-tier replays return 200 once the run finishes, with its outcome in the body; standard/long return 202 with the new executionId to poll.

Operation: `replayExecution`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `executionId` | path | string | Yes |  |
| `env` | query | string | No |  |

**Responses**

* `200`: Instant replay finished
* `202`: Async replay queued
* `400`: Workflow is disabled
* `404`: Execution, workflow, or environment deployment not found
* `409`: Run still in flight, or its installation is no longer active
* `429`: Execution quota exceeded
* `503`: Async execution engine unavailable

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.executionId` | `string` |  |
| `data.replayedFrom` | `string` |  |
| `data.tier` | `string` | One of: `instant`, `standard`, `long`. |
| `data.status` | `string` |  |
| `data.statusCode` | `integer` |  |
| `data.durationMs` | `integer` |  |
| `data.output` | `any` |  |
| `data.error` | `string` |  |
| `data.errorCategory` | `string` |  |
| `data.fixSuggestion` | `string` |  |

### Get or write a run's plain-language summary

```http
POST /v1/workflows/{id}/executions/{executionId}/summary
```

For a completed run that skipped records: answers the stored plain-language summary, writing it on the first call (copied from an earlier run with the same issues when there is one, otherwise generated by the model). Later calls are free. `data` is null when the run has nothing to summarize or the summary could not be written. When writing takes longer than the request waits (20 s), the answer is `{ data: null, pending: true }` and the write continues; ask again to get it.

Operation: `ensureExecutionSummary`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `executionId` | path | string | Yes |  |

**Responses**

* `200`: The summary (`kind: partial`, label, title, whatHappened, severity, howToFix, issueCount), or null
* `404`: Execution not found

### Fork an inherited workflow (and the sub-flows it calls) into your own org

```http
POST /v1/workflows/{id}/fork
```

Copies the parent's PUBLISHED code under the same slug (sub-flows are called by slug), publishes the copy and deploys it to every environment the source is live in that your org also has. Connector pins are dropped and connectors re-resolve in your org. The workflow must be reachable by your org (on an integration offered to it, or installed for it).

Operation: `forkWorkflow`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `orgId` | query | string | No | The customer: the id you gave it at creation (orgId), or fastn's id. Replaces orgId. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |

**Responses**

* `200`: Already forked
* `201`: data: { id, type, sourceId, name, reused, items, warnings }
* `409`: FORK_SLUG_CONFLICT

### Regenerate workflow documentation

```http
POST /v1/workflows/{id}/generate-docs
```

Fire-and-forget regeneration of the workflow's stored documentation from its current code, triggers, schemas, and connector actions. audience=end_user (default) rewrites the operator-facing doc and its visual artifacts; audience=technical writes a spec-only technical document under documentation.technical without touching the end-user doc. A generation that comes back empty is discarded and the previously saved doc is kept. When the inputs (code, schemas, triggers, connector actions) are the same as the ones the saved doc was generated from, nothing is regenerated unless force=true.

Operation: `generateWorkflowDocs`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `audience` | `string` | No | One of: `end_user`, `technical`. Default: `"end_user"`. |
| `force` | `boolean` | No | Regenerate even when the inputs are unchanged Default: `false`. |

**Responses**

* `202`: Generation started
* `400`: Workflow has no code or invalid audience
* `404`: Not found

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.generating` | `boolean` |  |
| `data.audience` | `string` |  |

### Set a workflow's labels

```http
PUT /v1/workflows/{id}/labels
```

Replaces the workflow's labels wholesale, send the full set, not a delta. Ids are de-duplicated BEFORE the cap is applied, so ["l1","l1"] is one label and is accepted. More than 5 distinct ids is refused with code WF-LABEL-LIMIT and no write. Every id must belong to the caller's workspace. The whole operation runs in one transaction behind a row lock on the workflow, so concurrent calls cannot interleave past the cap.

Operation: `setWorkflowLabels`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `labelIds` | `string[]` | Yes | Send [] to clear all labels. |

**Responses**

* `200`: Labels replaced
* `400`: More than 5 labels (code WF-LABEL-LIMIT), or an id not in this workspace
* `404`: Workflow not found

### Get connector manifest

```http
GET /v1/workflows/{id}/manifest
```

The workflow's connector manifest: one entry per connector its code calls, carrying the tenancy scope, the connection pin, the per-connector retry/timeout override, and the action entries with their version pins.

Operation: `getWorkflowConnectorManifest`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Workflow id (wf_*) |

**Responses**

* `200`: Connector manifest
* `404`: Workflow not found

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.workflowId` | `string` |  |
| `data.connectorManifest` | `object[]` |  |
| `data.connectorManifest[].slug` | `string` |  |
| `data.connectorManifest[].connectorId` | `string` |  |
| `data.connectorManifest[].orgId` | `string` | Owning org of the connector definition (e.g. org_platform, or a developer org). |
| `data.connectorManifest[].scope` | `string` | One of: `SAAS`, `MULTI_TENANT`. |
| `data.connectorManifest[].connectionId` | `string` | The pinned connection. Always null under MULTI_TENANT, where a connection is resolved per customer. |
| `data.connectorManifest[].retryPolicy` | `object` | This workflow's override for every action on this connector. |
| `data.connectorManifest[].retryPolicy.enabled` | `boolean` |  |
| `data.connectorManifest[].retryPolicy.maxAttempts` | `integer` | Total attempts INCLUDING the first. 1 = no retry. |
| `data.connectorManifest[].retryPolicy.initialDelayMs` | `integer` |  |
| `data.connectorManifest[].retryPolicy.backoffMultiplier` | `number` |  |
| `data.connectorManifest[].retryPolicy.maxDelayMs` | `integer` | Ceiling for any single backoff. |
| `data.connectorManifest[].retryPolicy.maxTotalDelayMs` | `integer` | Ceiling for all backoffs combined, the real guard on how long one call can hold a connector-concurrency slot while sleeping. |
| `data.connectorManifest[].retryPolicy.retryOnStatuses` | `integer[]` | Default: 408, 425, 429, 500, 502, 503, 504. |
| `data.connectorManifest[].retryPolicy.retryOnNetworkErrors` | `boolean` | Retry a request that never produced a response (DNS, reset, timeout). |
| `data.connectorManifest[].retryPolicy.respectRetryAfter` | `boolean` | Honour a Retry-After header in preference to the computed backoff, bounded by initialDelayMs/maxDelayMs at both ends. |
| `data.connectorManifest[].retryPolicy.methods` | `string[]` | null (the default) means every method, but unsafe methods then retry ONLY on a failure proving the provider never acted (425/429), a POST that 504s may already have created the record. Naming a method explicitly declares replaying it safe and lifts that restriction for it. One of: `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`. |
| `data.connectorManifest[].timeoutMs` | `integer` |  |
| `data.connectorManifest[].stale` | `boolean` | The saved code no longer calls this connector; kept for review rather than dropped. |
| `data.connectorManifest[].actions` | `object[]` |  |
| `data.connectorManifest[].actions[].slug` | `string` |  |
| `data.connectorManifest[].actions[].id` | `string` |  |
| `data.connectorManifest[].actions[].version` | `string` |  |
| `data.connectorManifest[].actions[].externalVersion` | `string` | The external system's contract version captured at save time (pin-on-build). |
| `data.connectorManifest[].actions[].versionMajor` | `integer` | Our breaking-revision axis, captured at save time. |
| `data.connectorManifest[].actions[].manual` | `boolean` | Added by hand from the UI, so it survives code-refresh merges. |
| `data.connectorManifest[].actions[].retryPolicy` | `object` |  |
| `data.connectorManifest[].actions[].timeoutMs` | `integer` |  |

### Refresh workflow connector manifest

```http
POST /v1/workflows/{id}/manifest/refresh
```

Re-extracts the connectors and actions the workflow's saved code calls, merges them into its connector manifest (keeping scope and connection pins) and re-resolves action ids and versions from the current catalog (requires workflows.update). Accepts the workflow id or slug.

Operation: `refreshWorkflowManifest`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: { connectorManifest } }
* `404`: Workflow not found

### Patch one connector manifest entry

```http
PATCH /v1/workflows/{id}/manifest/{slug}
```

Tunes ONE connector entry: tenancy scope + connection pin, the connector-level retry/timeout override, and per-action overrides. The surgical counterpart to PUT /workflows/{id}, which replaces the whole manifest array and so requires the caller to read and echo back every other entry. Applied as a partial at the FIELD level: an omitted field is left untouched, an explicit null clears that override so the entry inherits the connector row again, and at least one settable field must be present. A retryPolicy that is sent REPLACES the stored override rather than merging into it, merging would leave no way to remove a field from a stored layer. Identity fields (slug, connectorId, orgId, action id/version) are not settable, the code extractor owns them, and repointing one here would desync the manifest from the code it describes.

Operation: `setWorkflowConnectorScope`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Workflow id (wf_*) |
| `slug` | path | string | Yes | The manifest connector slug OR the connectorId, slug matched first, connectorId second. Matched against this workflow's manifest only, not the connector catalog. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `scope` | `string` | No | One of: `SAAS`, `MULTI_TENANT`. |
| `connectionId` | `string` | No |  |
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
| `actions` | `object[]` | No |  |
| `actions[].slug` | `string` | Yes |  |
| `actions[].retryPolicy` | `object` | No |  |
| `actions[].retryPolicy.enabled` | `boolean` | No |  |
| `actions[].retryPolicy.maxAttempts` | `integer` | No |  |
| `actions[].retryPolicy.initialDelayMs` | `integer` | No |  |
| `actions[].retryPolicy.backoffMultiplier` | `number` | No |  |
| `actions[].retryPolicy.maxDelayMs` | `integer` | No |  |
| `actions[].retryPolicy.maxTotalDelayMs` | `integer` | No |  |
| `actions[].retryPolicy.retryOnStatuses` | `integer[]` | No |  |
| `actions[].retryPolicy.retryOnNetworkErrors` | `boolean` | No |  |
| `actions[].retryPolicy.respectRetryAfter` | `boolean` | No |  |
| `actions[].retryPolicy.methods` | `string[]` | No |  |
| `actions[].timeoutMs` | `integer` | No |  |

**Responses**

* `200`: Entry patched; returns the full manifest after the write
* `400`: Empty patch (no settable field present); connectionId sent alone on a non-SAAS entry; a value outside the schema bounds; invalid JSON
* `404`: Workflow not found, connector absent from the manifest (knownSlugs + knownConnectorIds), or an action absent from the entry (knownActionSlugs)

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.workflowId` | `string` |  |
| `data.slug` | `string` | The entry's slug, even when it was addressed by connectorId |
| `data.scope` | `string` | One of: `SAAS`, `MULTI_TENANT`. |
| `data.connectorManifest` | `object[]` |  |
| `data.connectorManifest[].slug` | `string` |  |
| `data.connectorManifest[].connectorId` | `string` |  |
| `data.connectorManifest[].orgId` | `string` | Owning org of the connector definition (e.g. org_platform, or a developer org). |
| `data.connectorManifest[].scope` | `string` | One of: `SAAS`, `MULTI_TENANT`. |
| `data.connectorManifest[].connectionId` | `string` | The pinned connection. Always null under MULTI_TENANT, where a connection is resolved per customer. |
| `data.connectorManifest[].retryPolicy` | `object` | This workflow's override for every action on this connector. |
| `data.connectorManifest[].retryPolicy.enabled` | `boolean` |  |
| `data.connectorManifest[].retryPolicy.maxAttempts` | `integer` | Total attempts INCLUDING the first. 1 = no retry. |
| `data.connectorManifest[].retryPolicy.initialDelayMs` | `integer` |  |
| `data.connectorManifest[].retryPolicy.backoffMultiplier` | `number` |  |
| `data.connectorManifest[].retryPolicy.maxDelayMs` | `integer` | Ceiling for any single backoff. |
| `data.connectorManifest[].retryPolicy.maxTotalDelayMs` | `integer` | Ceiling for all backoffs combined, the real guard on how long one call can hold a connector-concurrency slot while sleeping. |
| `data.connectorManifest[].retryPolicy.retryOnStatuses` | `integer[]` | Default: 408, 425, 429, 500, 502, 503, 504. |
| `data.connectorManifest[].retryPolicy.retryOnNetworkErrors` | `boolean` | Retry a request that never produced a response (DNS, reset, timeout). |
| `data.connectorManifest[].retryPolicy.respectRetryAfter` | `boolean` | Honour a Retry-After header in preference to the computed backoff, bounded by initialDelayMs/maxDelayMs at both ends. |
| `data.connectorManifest[].retryPolicy.methods` | `string[]` | null (the default) means every method, but unsafe methods then retry ONLY on a failure proving the provider never acted (425/429), a POST that 504s may already have created the record. Naming a method explicitly declares replaying it safe and lifts that restriction for it. One of: `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`. |
| `data.connectorManifest[].timeoutMs` | `integer` |  |
| `data.connectorManifest[].stale` | `boolean` | The saved code no longer calls this connector; kept for review rather than dropped. |
| `data.connectorManifest[].actions` | `object[]` |  |
| `data.connectorManifest[].actions[].slug` | `string` |  |
| `data.connectorManifest[].actions[].id` | `string` |  |
| `data.connectorManifest[].actions[].version` | `string` |  |
| `data.connectorManifest[].actions[].externalVersion` | `string` | The external system's contract version captured at save time (pin-on-build). |
| `data.connectorManifest[].actions[].versionMajor` | `integer` | Our breaking-revision axis, captured at save time. |
| `data.connectorManifest[].actions[].manual` | `boolean` | Added by hand from the UI, so it survives code-refresh merges. |
| `data.connectorManifest[].actions[].retryPolicy` | `object` |  |
| `data.connectorManifest[].actions[].timeoutMs` | `integer` |  |

### Promote a version through review

```http
POST /v1/workflows/{id}/promote
```

Deploys a published version to an environment, taking one of two branches depending on that environment's requiresReview flag. requiresReview false (the DEFAULT, and the state of every built-in Live environment, ensureLiveEnvironment does not set the flag): this is a bit-for-bit passthrough to /deploy. It deploys immediately, opens no PR, writes no promotion record, and, because Live is the default environment, updates the workflow's live code pointer. There is no review step despite the operation name. requiresReview true: opens a PR against the org's connected GitHub repo and records a pending promotion; the deploy runs when that PR is merged. The 200 body differs per branch (see the response schema). env_id must be a wenv_* id belonging to the caller's org, obtained from GET /api/v1/environments; a slug is not accepted. Requires workflows.deploy_prod when the target is the default (Live) environment, workflows.deploy_test otherwise.

Operation: `promoteWorkflow`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `env_id` | `string` | Yes | Environment id (wenv_*) |
| `version_id` | `string` | Yes |  |
| `message` | `string` | No |  |

**Responses**

* `200`: Deployed immediately (requiresReview false), or promotion opened (requiresReview true), the two branches return different shapes
* `400`: env_id or version_id missing; or, on the review branch, no GitHub repository connected for this org, or the GitHub App is not configured on this platform
* `403`: The org can read workflow code but not change it (WF-CODE-READONLY). Promote goes through the same deploy mechanism that rewrites the live code pointer, so it is refused for a read-only org.
* `404`: Environment not found in this org, version not found for this workflow, or workflow not found
* `409`: A promotion is already awaiting review for this workflow and environment

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` |  |
| `data.envId` | `string` |  |
| `data.envSlug` | `string` |  |
| `data.versionId` | `string` |  |
| `data.envVersion` | `integer` |  |
| `data.deployedAt` | `string` |  |
| `data.status` | `string` | One of: `pending_review`. |
| `data.prUrl` | `string` |  |
| `data.promotionId` | `string` |  |

### List workflow promotions

```http
GET /v1/workflows/{id}/promotions
```

The workflow's last 50 review-gated publishes and promotions (GitHub pull requests) with their status, newest first (requires workflows.read).

Operation: `listWorkflowPromotions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Promotion list
* `404`: Workflow not found

### Cancel a pending promotion

```http
DELETE /v1/workflows/{id}/promotions/{promotionId}
```

Resolves a pending publish or promotion as rejected so the workflow can be published or promoted again, then closes its GitHub pull request on a best-effort basis (requires workflows.update).

Operation: `cancelWorkflowPromotion`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `promotionId` | path | string | Yes |  |

**Responses**

* `200`: { data: { status: 'rejected', promotionId, prClosed } }
* `404`: No pending promotion with that id

### Publish workflow

```http
POST /v1/workflows/{id}/publish
```

Publishes the workflow's draft (or current code when there is no draft) as a new immutable version and freezes its connector manifest (requires workflows.update). When the org requires review and has a GitHub repository connected, it instead opens a pull request and returns status pending_review; 409 when a publish is already awaiting review.

Operation: `publishWorkflow`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `message` | `string` | No | Version message; longer text is truncated. |

**Responses**

* `200`: The published version, or { status: 'pending_review', prUrl, promotionId }
* `404`: Workflow not found
* `409`: A publish is already awaiting review

### Restore a soft-deleted workflow

```http
POST /v1/workflows/{id}/restore
```

Undoes a non-permanent deleteWorkflow: clears deleted/deleted_at so the workflow is executable and listable again. Any trigger still routing to it resumes delivering on the next fire. Note: while the workflow was in the trash its webhook URL answered 404, so a sender that de-registered the endpoint during that window will not resume on its own and must be re-subscribed on the provider side. Returns { restored: false, reason: 'not_deleted' } when the workflow was never deleted. Requires workflows.delete. Note that unlike the ?deleted=true trash view, this route does not downgrade end_user, and end_user holds workflows.delete in the RBAC matrix - so a customer end_user can restore its own workflows.

Operation: `restoreWorkflow`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Restore result
* `404`: Workflow not found
* `409`: The slug is no longer free. A workflow created under it while this one sat in the trash owns it now, so clearing `deleted` would collide on idx_workflows_org_slug. Rename or delete the holder, then retry. `conflict` names it.

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.restored` | `boolean` |  |
| `data.reason` | `string` |  |

### Roll back an environment deployment

```http
POST /v1/workflows/{id}/rollback
```

Redeploys the version that was live at an earlier env_version of one environment, as a new deployment (requires workflows.update). env_version comes from GET /api/v1/workflows/{id}/deployments. 403 WF-CODE-READONLY when the org may read but not write workflow code.

Operation: `rollbackWorkflowDeployment`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `env_id` | `string` | Yes | Environment id (GET /api/v1/environments). |
| `env_version` | `number` | Yes | The deployment's envVersion to return to. |

**Responses**

* `200`: The new deployment
* `400`: env_id or env_version missing
* `404`: No deployment at that env_version

### Test saved workflow

```http
POST /v1/workflows/{id}/test
```

Runs a saved workflow synchronously in the sandbox. No execution row is recorded, so the run does not appear in execution history. It is still a run: it counts toward the monthly run quota (executions_per_month) and takes one of the org's instant concurrency slots, and is refused with 429 exactly as POST /{id}/execute is when either is spent. Skipping the history is the ONLY thing it avoids: the workflow's real code runs against real connections, so every side effect is real, fastn.db writes land in your workspace, connector actions hit the live provider, and records are genuinely created. mockMode:true narrows this but does NOT remove it: it routes fastn.connector.* calls to stored stubs, so the provider is not touched. fastn.db writes are unaffected and still land in your workspace, the sandbox db context never sees the flag. On success the tested input becomes the workflow's contract: inputSchema/inputExample are re-derived from a non-empty input, and the input/headers are saved as its testInput/testHeaders defaults.

Operation: `testSavedWorkflow`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `input` | `object` | No |  |
| `headers` | `object` | No |  |
| `mockMode` | `boolean` | No |  |
| `partialMock` | `boolean` | No |  |
| `mockScenarios` | `object` | No |  |

**Responses**

* `200`: Run result with logs and trace
* `400`: The body is not valid JSON, or is JSON but not an object (null, an array, a scalar). Code: VALIDATION_ERROR. Also refused with VALIDATION_ERROR when the session acts for a customer (an embed token or customer-scoped key, which carries a parent org) but names no customer and the body names no x-org-id, so the run would otherwise use the partner's connections.
* `403`: x-fastn-env named in the body headers is outside the caller's environment pin: a test key (or a token minted with it) may run only 'test', a key made for one environment only that environment and 'test'. The gateway never sees the body, so it is held to the pin here. Code: ENV_NOT_PERMITTED.
* `404`: Workflow not found
* `408`: The run exceeded the synchronous test budget (25s by default, so the answer fits the gateway's request budget). Code: WF-TEST-TIMEOUT. Carries the trace and step summary.
* `413`: The workflow returned a result larger than WORKFLOW_MAX_RESULT_BYTES (default 8 MiB). Code: WF-RESULT-TOO-LARGE.
* `422`: The workflow itself failed: a throw or syntax error in its code, a connector call it did not handle, a top-level declaration of a name the sandbox already defines (fastn, Fastn, FastnClient, module), or the sandbox memory limit. Code: WF-CODE-ERROR, or WF-MEMORY-LIMIT for the memory limit. Carries error, stack, errorCategory, fixSuggestion, the trace and step summary.
* `429`: The org has used its monthly runs (error quota_exceeded, dimension executions_per_month), or its instant concurrency slots or this pod's sandbox slots are all in use (RATE_LIMITED, Retry-After 5). Test runs pass the same gates as POST /{id}/execute; a platform service calling directly is not metered.
* `500`: A platform fault, not the workflow. Code: WF-EXEC-FAILED, with the requestId to quote when reporting it.

### Save workflow validation results

```http
PATCH /v1/workflows/{id}/validation
```

Stores the result of running the workflow's test cases as its last validation, stamped with the time and caller (requires workflows.update). Each result id should be a test-case id.

Operation: `saveWorkflowValidation`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | `string` | Yes | One of: `pass`, `partial`, `fail`. |
| `mode` | `string` | Yes | One of: `mock`, `live`. |
| `results` | `object[]` | Yes |  |
| `results[].id` | `string` | Yes |  |
| `results[].status` | `string` | Yes | One of: `pass`, `fail`, `skipped`, `partial`. |
| `results[].evidence` | `any` | No |  |
| `results[].error` | `string` | No |  |
| `results[].fix` | `string` | No |  |
| `cleanup` | `string` | No |  |

**Responses**

* `200`: The updated workflow
* `400`: Body does not match the schema
* `404`: Workflow not found

### List workflow versions

```http
GET /v1/workflows/{id}/versions
```

The workflow's last 50 published versions, newest first, without code unless include=code (requires workflows.read). A customer reading a parent-owned workflow never gets code.

Operation: `listWorkflowVersions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `include` | query | string | No | code adds each version's code. One of: `code`. |

**Responses**

* `200`: Version list
* `404`: Workflow not found

### Get one published version, with its code

```http
GET /v1/workflows/{id}/versions/{versionId}
```

Returns one immutable published snapshot (wv_*) of the workflow, including its code. The version list omits code; this is how a caller reads what a deployment runs, by the versionId from GET /workflows/{id}/deployments. A customer reading a workflow its partner owns gets 404, as the workflow read strips code for that caller. Requires workflows.read.

Operation: `getWorkflowVersion`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `versionId` | path | string | Yes |  |

**Responses**

* `200`: The version
* `404`: Workflow or version not found

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` |  |
| `data.versionNumber` | `integer` |  |
| `data.message` | `string` |  |
| `data.publishedBy` | `string` |  |
| `data.publishedAt` | `string` |  |
| `data.gitCommitSha` | `string` |  |
| `data.githubPrNumber` | `integer` |  |
| `data.githubReleaseId` | `string` |  |
| `data.githubReleaseUrl` | `string` |  |
| `data.code` | `string` |  |

## Execute

### Execute connector request

```http
POST /v1/execute
```

Raw HTTP passthrough: sends one request to an absolute http(s) URL and returns the provider's response. It resolves no connector base_url and attaches no credentials, so a relative path is a 400 and any auth must be supplied in headers; connectorId only labels the execution record and metrics. Sending connectionId is a 400 (to run a stored action against a connection use POST /api/v1/executions). method is uppercased and must be GET, POST, PUT, PATCH, DELETE, HEAD or OPTIONS. Private and internal addresses are refused. Requires connectors.read.

Operation: `executeRequest`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectorId` | `string` | Yes |  |
| `path` | `string` | Yes |  |
| `method` | `string` | No | Default: `"GET"`. |
| `headers` | `object` | No |  |
| `body` | `any` | No |  |
| `connectionId` | `string` | No |  |

**Responses**

* `200`: Execution result
* `400`: Relative path, disallowed URL, or connectionId supplied
* `429`: Quota exceeded

## Executions

### List executions

```http
GET /v1/executions
```

Connector action execution log for the caller's scope, newest first. Requires executions.read.

Operation: `listConnectorExecutions`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `actionId` | query | string | No |  |
| `connectionId` | query | string | No |  |
| `orgId` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `userId` | query | string | No |  |
| `limit` | query | integer | No |  |
| `offset` | query | integer | No |  |

**Responses**

* `200`: Execution list

### Get execution

```http
GET /v1/executions/{id}
```

One connector action execution with its input, output and timing. Requires executions.read.

Operation: `getConnectorExecution`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Execution

## Workflow categories

### List workflow categories

```http
GET /v1/workflow-categories
```

The workspace's category registry, alphabetical. A category is ONE per workflow and decides where that workflow sits in the list, unlike a label, which is many-per-workflow and filters. Capped per workspace by plan (quota dimension workflow_categories: Launch 2, Scale 10, Enterprise 15, or an admin override); `limit` carries the cap, -1 meaning unlimited. workflowCount excludes soft-deleted workflows.

Operation: `listWorkflowCategories`

**Responses**

* `200`: Categories with workflow counts

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].name` | `string` |  |
| `data[].colour` | `string` | A design-token name (chart-1, chart-2, chart-3, brand, success, info, warning, danger), never a hex value. |
| `data[].workflowCount` | `integer` | How many LIVE workflows sit in it. Soft-deleted ones are excluded. |
| `data[].createdAt` | `string` |  |
| `data[].updatedAt` | `string` |  |
| `limit` | `integer` | The per-workspace cap. |

### Create workflow category

```http
POST /v1/workflow-categories
```

Names are unique per workspace, case-insensitively. At the cap the request is refused with code WF-CATEGORY-LIMIT. Creates are serialised per workspace by an advisory lock held for the transaction, the counting subquery alone takes no lock under READ COMMITTED, so two sessions at 4 would both read 4 and both insert.

Operation: `createWorkflowCategory`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `colour` | `string` | Yes | Palette token name, one of: chart-1, chart-2, chart-3, brand, success, info, warning, danger |

**Responses**

* `201`: Category created
* `400`: Validation error, or the workspace is at its plan's category cap (code WF-CATEGORY-LIMIT, with limit)
* `409`: A category with that name already exists in this workspace

### Update workflow category

```http
PATCH /v1/workflow-categories/{id}
```

Rename or recolour. At least one of name/colour is required.

Operation: `updateWorkflowCategory`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `colour` | `string` | No | Palette token name, one of: chart-1, chart-2, chart-3, brand, success, info, warning, danger |

**Responses**

* `200`: Category updated
* `400`: Neither field supplied
* `404`: Category not found in this workspace
* `409`: A category with that name already exists

### Delete workflow category

```http
DELETE /v1/workflow-categories/{id}
```

The workflows in it are NOT deleted, workflows.category_id is ON DELETE SET NULL, so they fall back to Uncategorised. Deleting the thing you organise BY must never delete the things organised.

Operation: `deleteWorkflowCategory`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Category deleted; its workflows moved to Uncategorised
* `404`: Category not found in this workspace

## Workflow labels

### List workflow labels

```http
GET /v1/workflow-labels
```

The workspace's label registry, alphabetical. Labels are per-workspace (org_id) with NO inheritance: a customer never sees, renames or deletes its partner's labels. usageCount is how many LIVE workflows carry the label, soft-deleted ones are excluded, so the delete warning does not count workflows already in the trash. Capped per workspace by plan (quota dimension workflow_labels: Launch 2, Scale 10, Enterprise 15, or an admin override); `limit` carries the cap, -1 meaning unlimited.

Operation: `listWorkflowLabels`

**Responses**

* `200`: Labels with usage counts

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].name` | `string` |  |
| `data[].colour` | `string` | A design-token name (chart-1, chart-2, chart-3, brand, success, info, warning, danger), never a hex value, so a label follows the theme instead of freezing one colour into the database. |
| `data[].usageCount` | `integer` | How many LIVE workflows carry this label. Soft-deleted workflows are excluded. |
| `data[].createdAt` | `string` |  |
| `data[].updatedAt` | `string` |  |
| `limit` | `integer` | How many labels this workspace may define. -1 is unlimited. |

### Create workflow label

```http
POST /v1/workflow-labels
```

Names are unique per workspace, case-insensitively, creating `TikTok` when `tiktok` exists is a 409, so the registry cannot drift into three spellings of one label.

Operation: `createWorkflowLabel`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `colour` | `string` | Yes | Palette token name, one of: chart-1, chart-2, chart-3, brand, success, info, warning, danger |

**Responses**

* `201`: Label created
* `400`: Validation error, blank name, or a colour outside the palette, or the workspace is at its plan's label cap (code WF-LABEL-REGISTRY-LIMIT, with limit)
* `409`: A label with that name already exists in this workspace

### Update workflow label

```http
PATCH /v1/workflow-labels/{id}
```

Rename or recolour. At least one of name/colour is required.

Operation: `updateWorkflowLabel`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `colour` | `string` | No | Palette token name, one of: chart-1, chart-2, chart-3, brand, success, info, warning, danger |

**Responses**

* `200`: Label updated
* `400`: Validation error, or neither field supplied
* `404`: Label not found in this workspace
* `409`: A label with that name already exists in this workspace

### Delete workflow label

```http
DELETE /v1/workflow-labels/{id}
```

Removes the label from every workflow carrying it, via ON DELETE CASCADE on the link table. The workflows themselves are untouched, they simply lose the label.

Operation: `deleteWorkflowLabel`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Label deleted
* `404`: Label not found in this workspace

## Integrations

### Choose the repo or toggle the publish gate

```http
PATCH /v1/integrations/github
```

Sets the repository workflows sync to (repoOwner + repoName, which must be shared with the GitHub App) and/or gatePublish (publishing a workflow opens a pull request for review). 409 when a repo change would strand a pending sync or review. Requires settings.update.

Operation: `setGithubPublishGate`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `gatePublish` | `boolean` | No |  |
| `repoOwner` | `string` | No |  |
| `repoName` | `string` | No |  |

**Responses**

* `200`: Updated status
* `400`: Validation error or repo not shared with the app
* `404`: No active installation
* `409`: Pending sync or review blocks the change

### Disconnect the GitHub integration

```http
DELETE /v1/integrations/github
```

Marks the org's GitHub installation disconnected. 404 when none is active. Requires settings.update.

Operation: `disconnectGithubIntegration`

**Responses**

* `200`: { data: { disconnected: true } }
* `404`: No active installation

### Start the GitHub App install

```http
POST /v1/integrations/github/install
```

Returns the GitHub URL that installs the fastn GitHub App for this org; GitHub redirects back to the callback. 503 when the deployment has no GitHub App configured. Requires settings.update.

Operation: `startGithubInstallation`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `returnUrl` | `string` | No |  |
| `dashboardOrigin` | `string` | No |  |

**Responses**

* `200`: { data: { installUrl } }
* `503`: GitHub integration not configured

### List repositories shared with the GitHub App

```http
GET /v1/integrations/github/repositories
```

Repositories the org's GitHub App installation can access, to pick the sync target from. Requires settings.update.

Operation: `listGithubRepositories`

**Responses**

* `200`: Repository list
* `404`: No active installation
* `502`: GitHub could not be read

### List pending GitHub reviews

```http
GET /v1/integrations/github/reviews
```

Everything awaiting review on GitHub for the org: pending sync mirrors and workflow promotions or publishes, with their PR links. Requires workflows.read.

Operation: `listGithubReviews`

**Responses**

* `200`: { data: [review] }

### Get the GitHub integration status

```http
GET /v1/integrations/github/status
```

Whether the org has an active GitHub App installation, and its repository and publish-gate settings. Requires settings.read.

Operation: `getGithubIntegrationStatus`

**Responses**

* `200`: { data: { connected, ... } }

### Mirror workflows to GitHub

```http
POST /v1/integrations/github/sync
```

Opens a pull request mirroring every publishable workflow into the connected repository. Returns up_to_date when nothing changed. 409 with the blocking PR when a sync is already awaiting review. Requires workflows.update.

Operation: `syncWorkflowsToGithub`

**Responses**

* `200`: Sync status and PR url
* `400`: No repository connected, app not configured or nothing to sync
* `409`: A sync is already awaiting review

### Abandon a pending GitHub sync

```http
DELETE /v1/integrations/github/sync/{syncId}
```

Rejects a pending sync so new syncs are unblocked, closing its pull request when GitHub is reachable. Requires workflows.update.

Operation: `cancelGithubSync`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `syncId` | path | string | Yes |  |

**Responses**

* `200`: { data: { status: "rejected", syncId, prClosed } }
* `404`: No pending sync

### Connector health

```http
GET /v1/integrations/health
```

Per-connector health for the caller's org and the managed catalog: staleness findings, vendor changes and the workflows they affect. Requires connectors.read.

Operation: `listConnectorHealth`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorSlug` | query | string | No |  |
| `status` | query | string | No |  |
| `atRisk` | query | boolean | No | Only connectors with something at risk. |

**Responses**

* `200`: { data: [health] }

### Fork (duplicate) an inherited integration into your own org so you can customise it

```http
POST /v1/integrations/{id}/fork
```

For a child org (a customer) whose parent offers an integration (widget) it wants to change. The parent's integration can never be modified from a child org; this copies it into the caller's org and the copy is fully the caller's to edit. Copies the widget, its config template, every workflow it runs (lifecycle hooks, trigger targets, config option sources and every sub-flow they invoke, published, and deployed wherever the source is live), everything those workflows read by org at run time (env config values, secrets, the configs they name, the environments they run in), their category, labels, documentation and validation, its trigger templates (webhook, schedule and app-event, routed to the copied workflows, with the webhook configs and app registrations app events need) and the parent's CUSTOM connectors with their actions, auth methods, entities, mock stubs and OAuth providers including client secrets. Catalog connectors are shared by every org and stay referenced; so do all connectors when the caller's role cannot author connectors (end_user) - the response lists them in sharedConnectorIds. Every id is rewritten so the copy points at the copies. The parent's integration stays where it is and existing installations of it keep running. The customer sees ONE integration with two versions, their copy and the original: the copy becomes the active version, unless they already run the original, which then stays active until they switch (setWidgetActiveVersion). Idempotent: forking again returns the existing copies (200), and a fork that failed part-way resumes when repeated. Pass ?orgId=&lt;customer> from a partner session to fork into that customer. Use it when the caller wants to change an integration whose orgId is not their own org; ask them first. Afterwards change ONLY the copies named in data.items (type workflow: updateWorkflow or editWorkflowCode, then publishWorkflow, then run it), never the original ids. Tell the caller which connectors stay shared (sharedConnectorIds) and relay warnings. A copy deployed to live keeps running the previous version for live traffic until it is deployed again. If the customer already has a copy (a widget in listWidgets with version.kind = custom), change THAT copy; forking again returns it. If the original is still their active version, offer to switch (setWidgetActiveVersion): switching pauses their setup on the original and moves it to the copy with the same connected accounts.

Operation: `forkIntegration`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | The parent's widget id |
| `orgId` | query | string | No | The customer: the id you gave it at creation (orgId), or fastn's id. Replaces orgId. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No | Name for the copy; defaults to the original's name |

**Responses**

* `200`: Already forked; the existing copies are returned
* `201`: Forked. data: { widget, configId, sharedConnectorIds, items: [{ type, sourceId, forkId, reused, name }], warnings }
* `400`: FORK_NO_PARENT (the org has no parent), FORK_OWN_RESOURCE (already yours - edit it directly)
* `403`: FORK_NOT_CHILD (not inherited from your parent), or a missing workflows.create / events.create permission
* `404`: Not found or not offered to this org
* `409`: FORK_SLUG_CONFLICT: your org already has its own workflow or connector with a slug the copy must keep. partial lists what was already copied.
