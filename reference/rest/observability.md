---
description: "Alert rules, traces and the audit log."
---

# Alerts and observability

The format of `deliveries` on an alert rule is in [Set deliveries through the API](../../operate/alerts.md#set-deliveries-through-the-api).

Base URL, authentication and errors are on the [REST API overview](README.md).

## Alerts

### List alert rules

```http
GET /v1/alerts
```

Lists the alert rules in the caller's scope (newest first, 200 max). An end_user sees only their customer's rules. Roles: owner, admin, developer, end_user.

Operation: `listAlerts`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `endOrgId` | query | string | No | Act on this customer's own alert rules ("view as customer"). Alerts are not inherited: each org has its own. |

**Responses**

* `200`: Alert list

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].name` | `string` | Also the name workflow code passes to fastn.alerts.send for a code rule. |
| `data[].mode` | `string` | threshold: a metric crosses a threshold (polled). instant: a watched workflow run fails. code: workflow code raises it with fastn.alerts.send. One of: `threshold`, `instant`, `code`. |
| `data[].metric` | `string` | threshold rules only; instant and code rules carry failed_runs. |
| `data[].condition` | `string` | One of: `gt`, `lt`. |
| `data[].threshold` | `number` |  |
| `data[].window` | `string` | One of: `1h`, `24h`, `7d`, `30d`. |
| `data[].workflowIds` | `string[]` | Workflows the rule watches; null = all. Not allowed on code rules. |
| `data[].workflowNames` | `string[]` |  |
| `data[].deliveries` | `object[]` |  |
| `data[].deliveries[].type` | `string` | One of: `email`, `webhook`, `slack`, `connection`. |
| `data[].deliveries[].to` | `string` | email: the address |
| `data[].deliveries[].url` | `string` | webhook / slack: the URL |
| `data[].deliveries[].connectionId` | `string` | connection: the connected account to send through |
| `data[].deliveries[].target` | `string` | connection: the channel / chat to post to |
| `data[].deliveries[].subject` | `string` | email, or a connection through Gmail: optional subject, one line, at most 200 characters |
| `data[].deliveries[].targetName` | `string` | connection: optional display name of the target, at most 200 characters |
| `data[].enabled` | `boolean` |  |
| `data[].throttle` | `boolean` | instant and code rules: true = at most one notification per workflow (and alert key) per cooldown window, the rest counted and summarized; false = every failure or raised alert is its own notification. Every rule stays inside the per-rule and per-org send budget. Always true for threshold rules. |
| `data[].endOrgId` | `string` |  |
| `data[].lastFiredAt` | `string` | When a notification last reached at least one channel. |
| `data[].createdAt` | `string` |  |
| `data[].updatedAt` | `string` |  |

### Create alert rule

```http
POST /v1/alerts
```

mode=threshold (default) fires when the metric crosses the threshold over the window, evaluated periodically. mode=code fires only when workflow code calls fastn.alerts.send('&lt;rule name>', { title, message, severity, key, data }), within seconds, and never on a failure or threshold. mode=instant fires within about a minute of each failed/timeout workflow run, with the workflow name, the classified reason, and a deep link; extra failures inside the cooldown are counted and sent as one summary when the window ends, unless throttle=false, which sends every failure (or, for threshold rules, every breaching evaluation) as its own notification. workflowIds scopes the rule to a set of workflows (instant rules and execution-based threshold metrics only); null or empty = all workflows.

Operation: `createAlert`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `endOrgId` | query | string | No | Act on this customer's own alert rules ("view as customer"). Alerts are not inherited: each org has its own. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `mode` | `string` | No | One of: `threshold`, `instant`, `code`, `processing`. Default: `"threshold"`. |
| `metric` | `string` | No | Default: `"failed_runs"`. |
| `condition` | `string` | No | One of: `gt`, `lt`. Default: `"gt"`. |
| `threshold` | `number` | No | Default: `0`. |
| `window` | `string` | No |  |
| `workflowIds` | `string[]` | No |  |
| `deliveries` | `object[]` | No |  |
| `deliveries[].type` | `string` | Yes | One of: `email`, `webhook`, `slack`, `connection`. |
| `deliveries[].to` | `string` | No | email: the address |
| `deliveries[].url` | `string` | No | webhook / slack: the URL |
| `deliveries[].connectionId` | `string` | No | connection: the connected account to send through |
| `deliveries[].target` | `string` | No | connection: the channel / chat to post to |
| `deliveries[].subject` | `string` | No | email, or a connection through Gmail: optional subject, one line, at most 200 characters |
| `deliveries[].targetName` | `string` | No | connection: optional display name of the target, at most 200 characters |
| `enabled` | `boolean` | No |  |
| `throttle` | `boolean` | No |  |

**Responses**

* `201`: Alert created
* `400`: Invalid metric, window, workflow scope (including any scope on a code rule), or delivery
* `403`: throttle=false from a role other than owner, admin or developer

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` |  |
| `data.name` | `string` | Also the name workflow code passes to fastn.alerts.send for a code rule. |
| `data.mode` | `string` | threshold: a metric crosses a threshold (polled). instant: a watched workflow run fails. code: workflow code raises it with fastn.alerts.send. One of: `threshold`, `instant`, `code`. |
| `data.metric` | `string` | threshold rules only; instant and code rules carry failed_runs. |
| `data.condition` | `string` | One of: `gt`, `lt`. |
| `data.threshold` | `number` |  |
| `data.window` | `string` | One of: `1h`, `24h`, `7d`, `30d`. |
| `data.workflowIds` | `string[]` | Workflows the rule watches; null = all. Not allowed on code rules. |
| `data.workflowNames` | `string[]` |  |
| `data.deliveries` | `object[]` |  |
| `data.deliveries[].type` | `string` | One of: `email`, `webhook`, `slack`, `connection`. |
| `data.deliveries[].to` | `string` | email: the address |
| `data.deliveries[].url` | `string` | webhook / slack: the URL |
| `data.deliveries[].connectionId` | `string` | connection: the connected account to send through |
| `data.deliveries[].target` | `string` | connection: the channel / chat to post to |
| `data.deliveries[].subject` | `string` | email, or a connection through Gmail: optional subject, one line, at most 200 characters |
| `data.deliveries[].targetName` | `string` | connection: optional display name of the target, at most 200 characters |
| `data.enabled` | `boolean` |  |
| `data.throttle` | `boolean` | instant and code rules: true = at most one notification per workflow (and alert key) per cooldown window, the rest counted and summarized; false = every failure or raised alert is its own notification. Every rule stays inside the per-rule and per-org send budget. Always true for threshold rules. |
| `data.endOrgId` | `string` |  |
| `data.lastFiredAt` | `string` | When a notification last reached at least one channel. |
| `data.createdAt` | `string` |  |
| `data.updatedAt` | `string` |  |

### List alert delivery channels

```http
GET /v1/alerts/channels
```

Lists the caller's active connections that alerts can deliver to (e.g. Slack), with the target field each sender needs. includeInactive=true also returns connections that need reconnecting (status other than ACTIVE). Roles: owner, admin, developer, end_user.

Operation: `listAlertChannels`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `endOrgId` | query | string | No | Act on this customer's own alert rules ("view as customer"). Alerts are not inherited: each org has its own. |
| `includeInactive` | query | string | No | Also return connections whose status is not ACTIVE One of: `true`, `false`. |

**Responses**

* `200`: { data: [{ connectionId, connectorSlug, connectorName, connectionName, account, status, targetField, targetKind }] }. status is one of ACTIVE, EXPIRED, INACTIVE; only ACTIVE can deliver, and without includeInactive=true every row is ACTIVE.

### Enable starter alerts (one click)

```http
POST /v1/alerts/defaults
```

Idempotently seeds the two rules most teams need when the caller's scope has no alert rules yet: an instant sync-failure alert (email on each failed run, cooldown-batched) and a daily reliability check (error_rate above 10 percent over 24h). Uses the caller's email unless one is passed. Creates nothing when any rule already exists for the scope.

Operation: `enableDefaultAlerts`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `endOrgId` | query | string | No | Act on this customer's own alert rules ("view as customer"). Alerts are not inherited: each org has its own. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | `string` | No |  |

**Responses**

* `200`: Scope already has rules; nothing created
* `201`: Default rules created
* `400`: No delivery email available

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.created` | `object[]` |  |
| `data.alreadyConfigured` | `boolean` |  |

### Alert rule catalog

```http
GET /v1/alerts/metrics
```

Returns the metrics, windows, conditions, modes, sender apps and workflow-scopable metrics an alert rule may use. Roles: owner, admin, developer, end_user.

Operation: `getAlertCatalog`

**Responses**

* `200`: { data: { metrics, windows, conditions, senders, modes, scopableMetrics, processingMinutes } }

### Update alert rule

```http
PUT /v1/alerts/{id}
```

Partial update: omit a field to leave it unchanged. Cross-field rules apply to the rule's final state: a code rule cannot carry workflowIds, and a rule that is (or becomes) a threshold rule stores throttle=true.

Operation: `updateAlert`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Alert rule id. |
| `endOrgId` | query | string | No | Act on this customer's own alert rules ("view as customer"). Alerts are not inherited: each org has its own. |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `mode` | `string` | No | One of: `threshold`, `instant`, `code`, `processing`. |
| `metric` | `string` | No |  |
| `condition` | `string` | No | One of: `gt`, `lt`. |
| `threshold` | `number` | No |  |
| `window` | `string` | No |  |
| `workflowIds` | `string[]` | No |  |
| `deliveries` | `object[]` | No |  |
| `enabled` | `boolean` | No |  |
| `throttle` | `boolean` | No |  |

**Responses**

* `200`: Updated
* `400`: Invalid field, or a workflow scope on a code rule
* `403`: throttle=false from a role other than owner, admin or developer
* `404`: Alert rule not found

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `data.id` | `string` |  |
| `data.name` | `string` | Also the name workflow code passes to fastn.alerts.send for a code rule. |
| `data.mode` | `string` | threshold: a metric crosses a threshold (polled). instant: a watched workflow run fails. code: workflow code raises it with fastn.alerts.send. One of: `threshold`, `instant`, `code`. |
| `data.metric` | `string` | threshold rules only; instant and code rules carry failed_runs. |
| `data.condition` | `string` | One of: `gt`, `lt`. |
| `data.threshold` | `number` |  |
| `data.window` | `string` | One of: `1h`, `24h`, `7d`, `30d`. |
| `data.workflowIds` | `string[]` | Workflows the rule watches; null = all. Not allowed on code rules. |
| `data.workflowNames` | `string[]` |  |
| `data.deliveries` | `object[]` |  |
| `data.deliveries[].type` | `string` | One of: `email`, `webhook`, `slack`, `connection`. |
| `data.deliveries[].to` | `string` | email: the address |
| `data.deliveries[].url` | `string` | webhook / slack: the URL |
| `data.deliveries[].connectionId` | `string` | connection: the connected account to send through |
| `data.deliveries[].target` | `string` | connection: the channel / chat to post to |
| `data.deliveries[].subject` | `string` | email, or a connection through Gmail: optional subject, one line, at most 200 characters |
| `data.deliveries[].targetName` | `string` | connection: optional display name of the target, at most 200 characters |
| `data.enabled` | `boolean` |  |
| `data.throttle` | `boolean` | instant and code rules: true = at most one notification per workflow (and alert key) per cooldown window, the rest counted and summarized; false = every failure or raised alert is its own notification. Every rule stays inside the per-rule and per-org send budget. Always true for threshold rules. |
| `data.endOrgId` | `string` |  |
| `data.lastFiredAt` | `string` | When a notification last reached at least one channel. |
| `data.createdAt` | `string` |  |
| `data.updatedAt` | `string` |  |

### Delete alert rule

```http
DELETE /v1/alerts/{id}
```

Deletes an alert rule in the caller's scope. 404 when the rule does not exist there.

Operation: `deleteAlert`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Alert rule id. |
| `endOrgId` | query | string | No | Act on this customer's own alert rules ("view as customer"). Alerts are not inherited: each org has its own. |

**Responses**

* `200`: Deleted

### List an alert rule's firings

```http
GET /v1/alerts/{id}/events
```

Returns the last 50 firings of an alert rule in the caller's scope, newest first, with delivery status. Instant firings carry the failed workflow/execution in context. 404 when the rule is not in scope.

Operation: `listAlertEvents`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Alert rule id. |
| `endOrgId` | query | string | No | Act on this customer's own alert rules ("view as customer"). Alerts are not inherited: each org has its own. |

**Responses**

* `200`: { data: [{ id, metric, observedValue, threshold, condition, window, firedAt, delivered, deliveryError, context }] }
* `404`: Alert rule not found

## Traces

### List traces

```http
GET /v1/traces
```

One trace per workflow execution that called a connected system, newest first (100 max). `spans` are the connector calls within the run, offset from its start. connectorId filters by connector slug; status is one of success, error, pending.

Operation: `listTraces`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | query | string | No |  |
| `status` | query | string | No | One of: `success`, `error`, `pending`. |

**Responses**

* `200`: Trace list

### Get trace

```http
GET /v1/traces/{id}
```

The id is the workflow execution's id. 404 when the execution is out of scope, missing, or made no connector calls.

Operation: `getTrace`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Trace
* `404`: Not found

## Audit log

### List audit log entries

```http
GET /v1/audit-log
```

Lists audit log entries, newest first, with the total the filters match. owner and admin only; scoped to the caller's org and its customers. from/to must be ISO timestamps (400 otherwise).

Operation: `listAuditLog`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `action` | query | string | No | Exact action, e.g. workflow.update. |
| `userId` | query | string | No | Actor user id. |
| `endOrgId` | query | string | No | Only events of this customer (customer). |
| `resourceType` | query | string | No |  |
| `search` | query | string | No | Case-insensitive substring over action, resource type, resource id and details. |
| `excludeAction` | query | string[] | No | Action to leave out; repeatable. |
| `from` | query | string | No | Earliest created_at (inclusive). |
| `to` | query | string | No | Latest created_at (inclusive). |
| `limit` | query | integer | No | Page size, clamped to 1-200. |
| `offset` | query | integer | No |  |

**Responses**

* `200`: Audit entries, newest first
* `400`: A search shorter than 3 characters, a bad from/to, or a malformed cursor

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].action` | `string` |  |
| `data[].userId` | `string` |  |
| `data[].userName` | `string` |  |
| `data[].resourceType` | `string` |  |
| `data[].resource` | `string` |  |
| `data[].targetName` | `string` |  |
| `data[].outcome` | `string` |  |
| `data[].details` | `object` |  |
| `data[].orgId` | `string` |  |
| `data[].endOrgId` | `string` |  |
| `data[].createdAt` | `string` |  |
| `pagination` | `object` |  |
| `pagination.total` | `integer` | Exact up to 10,000, then 10,000 with totalIsLowerBound |
| `pagination.limit` | `integer` |  |
| `pagination.offset` | `integer` |  |
| `pagination.totalIsLowerBound` | `boolean` |  |
| `pagination.nextCursor` | `string` |  |

### List distinct audit log action types

```http
GET /v1/audit-log/actions
```

Lists every distinct action present in the audit log. owner and admin only; scoped to the caller's org and its customers.

Operation: `listAuditLogActions`

**Responses**

* `200`: Distinct action strings

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `string[]` |  |

### List distinct audit log resource types

```http
GET /v1/audit-log/resource-types
```

Lists every distinct resource_type present in the audit log. owner and admin only; scoped to the caller's org and its customers.

Operation: `listAuditLogResourceTypes`

**Responses**

* `200`: { data: string[] }

### List distinct audit log actors

```http
GET /v1/audit-log/users
```

Lists the distinct actor user ids present in the audit log (ids only, no names). owner and admin only; scoped to the caller's org and its customers.

Operation: `listAuditLogUsers`

**Responses**

* `200`: { data: string[] }
