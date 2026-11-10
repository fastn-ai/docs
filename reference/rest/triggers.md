---
description: "Webhook, schedule and app event triggers, received events and the dead-letter queue."
---

# Triggers and events

Base URL, authentication and errors are on the [REST API overview](README.md).

## Triggers

### Org-wide trigger health

```http
GET /v1/triggers/monitoring
```

Health overview of every trigger (webhook, scheduler, app event) in the caller's org: pipeline counters, per-trigger delivery stats, DLQ depth and circuit-breaker state, with a computed health. order=oldest surfaces the longest-waiting triggers and is single-page (a cursor with it is a 400).

Operation: `getTriggersMonitoring`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `type` | query | string | No | Trigger type filter. |
| `status` | query | string | No | One of: `ACTIVE`, `DISABLED`. |
| `search` | query | string | No |  |
| `health` | query | string | No | Computed health filter. |
| `limit` | query | integer | No | Page size, clamped to 100. |
| `order` | query | string | No | Default newest. oldest cannot be combined with cursor. One of: `newest`, `oldest`. |
| `cursor` | query | string | No | nextCursor from the previous page. |

**Responses**

* `200`: Pipeline counters plus per-trigger stats, DLQ counts, circuit-breaker state, and the owning installationId / orgId (both null for a trigger created outside an installation)

### Reset circuit breaker

```http
POST /v1/triggers/{id}/circuit-breaker/reset
```

Force-closes every open circuit breaker on the trigger's routes so deliveries resume immediately instead of waiting out the cool-down. Requires events.update. Returns how many routes were reset.

Operation: `resetCircuitBreaker`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { routesReset }

### Replay a trigger's whole DLQ

```http
POST /v1/triggers/{id}/dlq/replay-all
```

Queues every dead-letter entry of one trigger for re-delivery at a throttled rate. Requires events.replay; 404 when the trigger is not in the caller's org.

Operation: `replayAllTriggerDlq`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: { enqueued, skipped, ratePerSecond } }
* `404`: Not found in the caller's org

### Fork an inherited trigger template (and the workflows it routes to) into your own org

```http
POST /v1/triggers/{id}/fork
```

Copies a webhook, schedule or app-event trigger TEMPLATE; per-installation instances are refused (FORK_TRIGGER_IS_INSTANCE). Routed workflows are forked first and the copy routes to them. A copied schedule does not run on create.

Operation: `forkTrigger`

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

### Per-trigger health

```http
GET /v1/triggers/{id}/monitoring
```

Health detail for one trigger: per-route delivery stats, circuit-breaker state per route, a page of its dead-letter entries (dlqLimit, max 100, default 20; dlqCursor to page) and the computed health. 404 when the trigger is not in the caller's org.

Operation: `getTriggerMonitoring`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `dlqLimit` | query | integer | No |  |
| `dlqCursor` | query | string | No |  |

**Responses**

* `200`: Per-route stats, DLQ entries, circuit-breaker state, computed health

### What happened to a trigger's events, end to end

```http
GET /v1/triggers/{id}/outcomes
```

Each event the trigger received in the window, classified by its workflow runs (including runs of any replay of it) and its dead-letter rows: succeeded first time, recovered (succeeded after a failed run, a retry or a replay), failedRun (a workflow failed and nothing re-ran it), notRun (no run, or its latest attempt is dead-lettered), inProgress. succeeded and recovered are disjoint. The window is the last days x 24 hours. Recomputed every few minutes; refreshedAt says when. Scheduler triggers have no stored events and report zeros.

Operation: `getTriggerOutcomes`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `days` | query | integer | No |  |

**Responses**

* `200`: { data: { days, totals, daily[], refreshedAt, countOnlyField } } with counts received, succeeded, recovered, failedRun, notRun, inProgress. countOnlyField is the payload key an event needs to be counted, null when every event counts
* `400`: days outside 1..30
* `404`: Trigger not found in the caller's org

### Choose which events Reporting counts

```http
PUT /v1/triggers/{id}/reporting
```

Count only the events whose payload is an object with this top-level key, so a provider's health checks posted to the same webhook stay out of the event figures. Reporting only: the trigger still accepts and routes every event. Null counts every event. A change recounts the trigger's held history: the last day within half an hour, older days over the following hours.

Operation: `setTriggerReporting`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `countOnlyField` | `string` | Yes |  |

**Responses**

* `200`: { data: { id, countOnlyField } }
* `400`: Invalid body
* `404`: Trigger not found in the caller's org

### Pause or resume a trigger

```http
PATCH /v1/triggers/{id}/status
```

Pauses (DISABLED) or resumes (ACTIVE) any trigger by id, whatever its type. Pausing a scheduler also unregisters its timer; resuming registers it again. Requires events.update; 404 when the trigger is not in the caller's org.

Operation: `setTriggerStatus`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `status` | `string` | Yes | One of: `ACTIVE`, `DISABLED`. |

**Responses**

* `200`: Updated
* `404`: Not found

### Connector webhook ingest (called by providers)

```http
POST /v1/triggers/{orgId}/webhooks/{connectorId}/{authProviderId}
```

The per-connector ingest URL of an APP-type webhook config with an auth provider. The provider posts events here; they are verified against the config and fanned out to the matching app-event triggers.

Operation: `receiveAppWebhook`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `orgId` | path | string | Yes |  |
| `connectorId` | path | string | Yes |  |
| `authProviderId` | path | string | Yes |  |

**Responses**

* `202`: { data: { status: 'accepted', dispatched } }
* `401`: Signature verification failed

### Webhook ingest (called by external systems)

```http
POST /v1/triggers/{orgId}/webhooks/{triggerId}
```

The public URL a webhook trigger hands out (its triggerUrl). Accepts any JSON or form body and dispatches it to the trigger's routes. A trigger with authMethod API_KEY requires a fastn API key header. Any other method is a 405.

Operation: `receiveWebhookTrigger`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `orgId` | path | string | Yes |  |
| `triggerId` | path | string | Yes |  |

**Responses**

* `202`: { data: { status: 'accepted', dispatched, warning? } }
* `401`: Missing or invalid API key
* `404`: Unknown or disabled trigger

### Send an app event to a connector's ingest URL

```http
POST /v1/triggers/{orgId}/{connectorId}/events
```

The ingest URL of a connector's app registration, which the provider posts events to; posting a synthetic event here fires the matching app-event triggers end to end. The registration's verification applies: a connector whose method needs a signature rejects an unsigned request with 401. The event type and account id are read from the body with the registration's extractors. triggerId restricts delivery to one trigger. Not authenticated by fastn credentials.

Operation: `sendTestAppEvent`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `orgId` | path | string | Yes | The org that owns the registration (org_platform for the shared catalog). |
| `connectorId` | path | string | Yes |  |
| `triggerId` | query | string | No | Deliver only to this app-event trigger. |

**Responses**

* `202`: { data: { status: 'accepted', matched, dispatched } }
* `401`: Signature verification failed
* `404`: No active registration for the connector
* `413`: Payload too large
* `429`: Rate limited

## Schedulers

### List schedulers

```http
GET /v1/schedulers
```

Lists scheduled triggers in the caller's org (or one customer's with org_id), newest first, cursor-paginated. Use include_customers=true before creating a schedule for a customer: it adds every customer's schedulers, labelled, so you can see the customer already has one and not create a duplicate. Without it the list is your own org's only. Requires events.read.

Operation: `listSchedulers`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `limit` | query | integer | No | Page size. Values above 100 are clamped to 100. |
| `cursor` | query | string | No | nextCursor from the previous page. |
| `search` | query | string | No |  |
| `status` | query | string | No | One of: `ACTIVE`, `DISABLED`. |
| `include_instances` | query | string | No | true also lists triggers created by installations (per-customer instances). One of: `true`, `false`. |
| `orgId` | query | string | No | The customer whose triggers to list: the id you gave it at creation (orgId), or fastn's id. Must be a customer of the caller's org, otherwise 403. Replaces org_id. |
| `org_id` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `include_customers` | query | string | No | true also lists every customer's schedulers: those you provisioned for a customer and those the customer made itself, never another partner's. Each row then carries customer ({ orgId, name }, null for your own) and isInstance. Add include_instances=true to also see schedulers a customer's setup (installation) created. Only for an owner, admin or developer listing its own org: 403 with org_id, from a customer-scoped caller, or from another role. Default false. One of: `true`, `false`. |

**Responses**

* `200`: { data: Scheduler[], nextCursor, hasMore, total }. nextCursor pages on (createdAt, id), so schedulers created at the same moment are not skipped.
* `403`: org_id is not a customer of the caller's org, or include_customers=true from a caller that may not list its customers (not owner, admin or developer of its own org, a customer-scoped caller, or with org_id)

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object[]` |  |
| `data[].id` | `string` |  |
| `data[].name` | `string` |  |
| `data[].orgId` | `string` | The customer this belongs to, under the id you gave it (its external ref); the account itself when it belongs to no customer. |
| `data[].installationId` | `string` |  |
| `data[].status` | `string` | One of: `ACTIVE`, `DISABLED`. |
| `data[].scheduler` | `object` | cron or rate, timezone, routes, run and failure state |
| `data[].customer` | `object` | Only with include_customers=true. The customer this scheduler belongs to, null for your own. |
| `data[].customer.name` | `string` |  |
| `data[].customer.orgId` | `string` | The customer this belongs to, under the id you gave it (its external ref); the account itself when it belongs to no customer. |
| `data[].isInstance` | `boolean` | Only with include_customers=true. true when an installation (a customer's setup of a widget) created it. |
| `nextCursor` | `string` |  |
| `hasMore` | `boolean` |  |
| `total` | `integer` |  |

### Create a scheduler

```http
POST /v1/schedulers
```

Creates a scheduled trigger that fires its routes on a 5-field cron expression or a fixed rate (exactly one of cron or rate). runOnCreate=true also fires it once immediately; omitted or false waits for the schedule. A scheduler auto-disabled by repeated failures is re-enabled after reenableAfterMinutes, unless the failures were its workflow being deleted or never published: that one stays disabled until it is turned back on. Leave routes[].env out unless the workflow is deployed to that environment; the response carries a warning when it is not. Requires events.create.

Operation: `createScheduler`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No |  |
| `name` | `string` | Yes |  |
| `status` | `string` | No | One of: `ACTIVE`, `DISABLED`. |
| `installationId` | `string` | No |  |
| `cron` | `object` | No |  |
| `cron.expression` | `string` | Yes |  |
| `rate` | `object` | No |  |
| `rate.value` | `integer` | Yes |  |
| `rate.unit` | `string` | Yes | One of: `minutes`, `hours`, `days`. |
| `delayMinutes` | `integer` | No | Default: `0`. |
| `timezone` | `string` | No | Default: `"UTC"`. |
| `startsAt` | `string` | No |  |
| `dlqConfiguration` | `object` | No |  |
| `dlqConfiguration.maxRetries` | `integer` | No | Default: `3`. |
| `dlqConfiguration.backoffStrategy` | `string` | No | One of: `exponential`, `linear`, `fixed`. Default: `"exponential"`. |
| `dlqConfiguration.backoffDelayMs` | `integer` | No |  |
| `additionalConfig` | `object` | No |  |
| `routes` | `object[]` | No |  |
| `routes[].routeId` | `string` | Yes |  |
| `routes[].routeType` | `string` | No | One of: `API`. Default: `"API"`. |
| `routes[].headers` | `object` | No |  |
| `routes[].payload` | `object` | No |  |
| `routes[].env` | `string` | No | Environment this route fires into. Omit it to run the latest published version (test), which is right for almost every trigger. Set it only to an environment the workflow is already deployed to: a route pinned to an environment with no active deployment dead-letters every event or scheduled fire, and a webhook, app-event or scheduler create/update answers with a warning naming the route. |
| `routes[].installationId` | `string` | No |  |
| `routes[].tenantResolver` | `object` | No |  |
| `routes[].tenantResolver.source` | `string` | Yes | One of: `header`, `body`. |
| `routes[].tenantResolver.field` | `string` | Yes |  |
| `reenableAfterMinutes` | `integer` | No | Default: `30`. |
| `runOnCreate` | `boolean` | No |  |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `201`: { data: scheduler, warning? }
* `400`: Invalid JSON or a body that fails validation
* `409`: A trigger with that id already exists

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `warning` | `string` | Present when the trigger was saved but will not deliver as configured: a route is pinned (routes[].env) to an environment the workflow has no active deployment in (or, for test, no published version), so every event or scheduled fire that route receives is dead-lettered; for a webhook trigger, also when it has no routes. Names the route, the environment and the fix: deploy the workflow there, or remove env from the route to run the latest published version (test). |

### Delete schedulers in bulk

```http
POST /v1/schedulers/bulk-delete
```

Deletes up to 100 schedulers by id and unregisters their timers. Ids that are not found are reported in failed. Requires events.delete.

Operation: `bulkDeleteSchedulers`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | `string[]` | Yes |  |

**Responses**

* `200`: { data: { deleted: string[], failed: { id, reason }[] } }
* `400`: Invalid JSON or a body that fails validation

### Disable every scheduler bound to a workflow

```http
POST /v1/schedulers/disable-by-route
```

Disables every active scheduler in the caller's org whose routes target any of routeIds (send both the workflow id and its slug), and unregisters their timers. Used when a workflow is deleted or unpublished. Requires events.update; an API key pinned to an environment is refused with 403.

Operation: `disableSchedulersByRoute`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `routeIds` | `string[]` | Yes |  |

**Responses**

* `200`: { data: { disabled, neutralized } }
* `400`: Invalid JSON or a body that fails validation
* `403`: API key environment pin forbids this

### Get a scheduler

```http
GET /v1/schedulers/{id}
```

Returns one scheduler with its schedule, routes and status. Requires events.read.

Operation: `getScheduler`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: scheduler }
* `404`: Not found in the caller's org

### Update a scheduler

```http
PUT /v1/schedulers/{id}
```

Partially updates a scheduler and re-registers its timer. cron and rate cannot both be sent. routes, when sent, replaces the whole binding list. The response carries a warning when a route is pinned to an environment the workflow is not deployed to. Requires events.update.

Operation: `updateScheduler`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `status` | `string` | No | One of: `ACTIVE`, `DISABLED`. |
| `cron` | `object` | No |  |
| `cron.expression` | `string` | Yes |  |
| `rate` | `object` | No |  |
| `rate.value` | `integer` | Yes |  |
| `rate.unit` | `string` | Yes | One of: `minutes`, `hours`, `days`. |
| `delayMinutes` | `integer` | No |  |
| `timezone` | `string` | No |  |
| `startsAt` | `string` | No |  |
| `dlqConfiguration` | `object` | No |  |
| `dlqConfiguration.maxRetries` | `integer` | No | Default: `3`. |
| `dlqConfiguration.backoffStrategy` | `string` | No | One of: `exponential`, `linear`, `fixed`. Default: `"exponential"`. |
| `dlqConfiguration.backoffDelayMs` | `integer` | No |  |
| `additionalConfig` | `object` | No |  |
| `routes` | `object[]` | No |  |
| `routes[].routeId` | `string` | Yes |  |
| `routes[].routeType` | `string` | No | One of: `API`. Default: `"API"`. |
| `routes[].headers` | `object` | No |  |
| `routes[].payload` | `object` | No |  |
| `routes[].env` | `string` | No | Environment this route fires into. Omit it to run the latest published version (test), which is right for almost every trigger. Set it only to an environment the workflow is already deployed to: a route pinned to an environment with no active deployment dead-letters every event or scheduled fire, and a webhook, app-event or scheduler create/update answers with a warning naming the route. |
| `routes[].installationId` | `string` | No |  |
| `routes[].tenantResolver` | `object` | No |  |
| `routes[].tenantResolver.source` | `string` | Yes | One of: `header`, `body`. |
| `routes[].tenantResolver.field` | `string` | Yes |  |
| `reenableAfterMinutes` | `integer` | No |  |

**Responses**

* `200`: { data: scheduler, warning? }
* `400`: Invalid JSON or a body that fails validation
* `404`: Not found in the caller's org

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `warning` | `string` | Present when the trigger was saved but will not deliver as configured: a route is pinned (routes[].env) to an environment the workflow has no active deployment in (or, for test, no published version), so every event or scheduled fire that route receives is dead-lettered; for a webhook trigger, also when it has no routes. Names the route, the environment and the fix: deploy the workflow there, or remove env from the route to run the latest published version (test). |

### Delete a scheduler

```http
DELETE /v1/schedulers/{id}
```

Deletes a scheduler and unregisters its timer. Requires events.delete.

Operation: `deleteScheduler`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: { deleted: true } }
* `404`: Not found in the caller's org

### Scheduler route stats

```http
GET /v1/schedulers/{id}/stats
```

Per-route delivery counters for one scheduler. Requires events.read.

Operation: `getSchedulerStats`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: route stats }
* `404`: Not found in the caller's org

### Fire scheduler now

```http
POST /v1/schedulers/{id}/trigger
```

Run-now: dispatches the scheduler's routes immediately. The returned eventId lands in the resulting execution's request headers (x-fastn-event-id), closing the trigger-to-execution verification loop.

Operation: `triggerSchedulerNow`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `202`: { eventId, status: dispatched }
* `400`: Disabled or no routes
* `404`: Not found
* `429`: QUOTA_EXCEEDED when the org that owns every route's workflow has used its executions_per_month (details.routes names the route ids; nothing is dispatched). Otherwise: Cooldown held, this scheduler was fired within the last SCHEDULER_MANUAL_FIRE_COOLDOWN_MS (10s default). Body is { error: { code: RATE_LIMITED, details: { reason: manual_fire_cooldown }, retryAfter } } with a Retry-After header. Applies per (calling org, scheduler); a fire that then 404s or 400s still consumes the window

## App triggers

### List app-event triggers

```http
GET /v1/app-triggers
```

Lists app-event triggers (triggers fired by a connector's events, e.g. a HubSpot contact.created) in the caller's org, newest first, cursor-paginated. Each row carries its ingest webhookUrl and the provider-side subscriptionStatus. Requires events.read.

Operation: `listAppEventTriggers`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `limit` | query | integer | No |  |
| `cursor` | query | string | No |  |
| `search` | query | string | No |  |
| `status` | query | string | No |  |
| `connectorId` | query | string | No |  |
| `include_instances` | query | string | No | One of: `true`, `false`. |
| `org_id` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `200`: Triggers with webhookUrl and subscriptionStatus

### Create an app-event trigger

```http
POST /v1/app-triggers
```

Binds workflows to events a connector emits (1-50 events from GET /api/v1/app-triggers/connectors/{connectorId}/events). The connector must have an app registration or a webhook config, otherwise 400. When the connector supports it the provider-side subscription is created too; the response says whether it was attempted and, when it was not, the ingest URL to register by hand. A POLL event makes the trigger a polling trigger. Leave routes[].env out unless the workflow is deployed to that environment; the response carries a warning when it is not. Requires events.create.

Operation: `createAppEventTrigger`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `status` | `string` | No | One of: `ACTIVE`, `DISABLED`. |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |
| `installationId` | `string` | No |  |
| `connectorId` | `string` | Yes |  |
| `connectorName` | `string` | Yes |  |
| `type` | `string` | No | One of: `WEBHOOK`, `POLLING`. Default: `"WEBHOOK"`. |
| `events` | `object[]` | Yes |  |
| `events[].id` | `string` | Yes |  |
| `events[].label` | `string` | Yes |  |
| `events[].description` | `string` | No |  |
| `events[].payloadSchema` | `any` | No |  |
| `routes` | `object[]` | No |  |
| `routes[].routeId` | `string` | Yes |  |
| `routes[].routeType` | `string` | No | One of: `API`. Default: `"API"`. |
| `routes[].headers` | `object` | No |  |
| `routes[].payload` | `object` | No |  |
| `routes[].env` | `string` | No | Environment this route fires into. Omit it to run the latest published version (test), which is right for almost every trigger. Set it only to an environment the workflow is already deployed to: a route pinned to an environment with no active deployment dead-letters every event or scheduled fire, and a webhook, app-event or scheduler create/update answers with a warning naming the route. |
| `routes[].installationId` | `string` | No |  |
| `routes[].tenantResolver` | `object` | No |  |
| `routes[].tenantResolver.source` | `string` | Yes | One of: `header`, `body`. |
| `routes[].tenantResolver.field` | `string` | Yes |  |
| `dlqConfiguration` | `object` | No |  |
| `dlqConfiguration.maxRetries` | `integer` | No | Default: `3`. |
| `dlqConfiguration.backoffStrategy` | `string` | No | One of: `exponential`, `linear`, `fixed`. Default: `"exponential"`. |
| `dlqConfiguration.backoffDelayMs` | `integer` | No |  |
| `additionalConfig` | `object` | No |  |
| `accountId` | `string` | No |  |
| `connectionId` | `string` | No |  |

**Responses**

* `201`: { data: trigger with webhookUrl, subscription, warning? }
* `400`: Invalid JSON or a body that fails validation

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `subscription` | `object` | Whether the provider-side subscription was attempted and its outcome; when it was not, the reason and the ingest url to register by hand. |
| `warning` | `string` | Present when the trigger was saved but will not deliver as configured: a route is pinned (routes[].env) to an environment the workflow has no active deployment in (or, for test, no published version), so every event or scheduled fire that route receives is dead-lettered; for a webhook trigger, also when it has no routes. Names the route, the environment and the fix: deploy the workflow there, or remove env from the route to run the latest published version (test). |

### Delete app-event triggers in bulk

```http
POST /v1/app-triggers/bulk-delete
```

Deletes up to 100 app-event triggers by id, removing provider-side subscriptions and polling timers best-effort. Ids that are not found are reported in failed. Requires events.delete.

Operation: `bulkDeleteAppEventTriggers`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | `string[]` | Yes |  |

**Responses**

* `200`: { data: { deleted: string[], failed: { id, reason }[] } }
* `400`: Invalid JSON or a body that fails validation

### List a connector's subscribable events

```http
GET /v1/app-triggers/connectors/{connectorId}/events
```

The event catalog an app-event trigger can subscribe to for this connector: events from its webhook configs (with whether each is registered) merged with those from its app registration. Use the ids in createAppEventTrigger. Requires events.read.

Operation: `listConnectorEvents`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | path | string | Yes |  |

**Responses**

* `200`: { data: { connectorId, events: { id, label, description, payloadSchema?, source }[] } }

### List a connector's webhook-config events

```http
GET /v1/app-triggers/connectors/{connectorId}/webhook-config-events
```

Only the events declared by this connector's webhook configs, each with its webhookConfigId and whether it is registered. Requires events.read.

Operation: `listConnectorWebhookConfigEvents`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectorId` | path | string | Yes |  |

**Responses**

* `200`: { data: { connectorId, events: { id, label, description, registered, webhookConfigId }[] } }

### Get app-event trigger

```http
GET /v1/app-triggers/{id}
```

Returns one app-event trigger: its subscribed events, route bindings, ingest webhookUrl and subscriptionStatus. 404 when the id is not in the caller's org scope.

Operation: `getAppEventTrigger`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Trigger with events, routes, webhookUrl, subscriptionStatus
* `404`: Not found

### Update an app-event trigger

```http
PUT /v1/app-triggers/{id}
```

Partially updates an app-event trigger. routes and events, when sent, replace the whole list. The response carries a warning when a route is pinned to an environment the workflow is not deployed to. Requires events.update.

Operation: `updateAppEventTrigger`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `status` | `string` | No | One of: `ACTIVE`, `DISABLED`. |
| `events` | `object[]` | No |  |
| `events[].id` | `string` | Yes |  |
| `events[].label` | `string` | Yes |  |
| `events[].description` | `string` | No |  |
| `events[].payloadSchema` | `any` | No |  |
| `routes` | `object[]` | No |  |
| `routes[].routeId` | `string` | Yes |  |
| `routes[].routeType` | `string` | No | One of: `API`. Default: `"API"`. |
| `routes[].headers` | `object` | No |  |
| `routes[].payload` | `object` | No |  |
| `routes[].env` | `string` | No | Environment this route fires into. Omit it to run the latest published version (test), which is right for almost every trigger. Set it only to an environment the workflow is already deployed to: a route pinned to an environment with no active deployment dead-letters every event or scheduled fire, and a webhook, app-event or scheduler create/update answers with a warning naming the route. |
| `routes[].installationId` | `string` | No |  |
| `routes[].tenantResolver` | `object` | No |  |
| `routes[].tenantResolver.source` | `string` | Yes | One of: `header`, `body`. |
| `routes[].tenantResolver.field` | `string` | Yes |  |
| `dlqConfiguration` | `object` | No |  |
| `dlqConfiguration.maxRetries` | `integer` | No | Default: `3`. |
| `dlqConfiguration.backoffStrategy` | `string` | No | One of: `exponential`, `linear`, `fixed`. Default: `"exponential"`. |
| `dlqConfiguration.backoffDelayMs` | `integer` | No |  |
| `additionalConfig` | `object` | No |  |
| `accountId` | `string` | No |  |

**Responses**

* `200`: { data: trigger, warning? }
* `400`: Invalid JSON or a body that fails validation
* `404`: Not found in the caller's org

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `warning` | `string` | Present when the trigger was saved but will not deliver as configured: a route is pinned (routes[].env) to an environment the workflow has no active deployment in (or, for test, no published version), so every event or scheduled fire that route receives is dead-lettered; for a webhook trigger, also when it has no routes. Names the route, the environment and the fix: deploy the workflow there, or remove env from the route to run the latest published version (test). |

### Delete an app-event trigger

```http
DELETE /v1/app-triggers/{id}
```

Deletes an app-event trigger, removing its provider-side subscription and polling timer best-effort first. Requires events.delete.

Operation: `deleteAppEventTrigger`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: { deleted: true } }
* `404`: Not found in the caller's org

### Retry upstream subscription

```http
POST /v1/app-triggers/{id}/retry-subscription
```

Re-runs the provider subscription for a FAILED/NONE app-event trigger. Answers 409 when a registration made with the trigger's previous input values could not be removed; force=true registers anyway once it has been removed at the provider.

Operation: `retryTriggerSubscription`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |
| `force` | query | string | No | true: register even though the previous registration could not be removed. Use it only once that registration is gone at the provider, or both fire the trigger. One of: `true`. |

**Responses**

* `200`: Updated trigger plus subscription {success, error, warning}. warning is set when the trigger's saved connection could no longer be used and the subscription ran on the customer's current connection: the trigger still names the old one, so recreate it
* `409`: SUBSCRIPTION_CONFLICT. A registration made with the previous input values could not be removed (force=true registers anyway), or the subscription changed while this retry waited (read the trigger first; force does not apply).

### App-event trigger route stats

```http
GET /v1/app-triggers/{id}/stats
```

Per-route delivery counters for one app-event trigger. Requires events.read.

Operation: `getAppEventTriggerStats`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: route stats }
* `404`: Not found in the caller's org

## Webhooks

### List webhook triggers

```http
GET /v1/webhooks
```

Lists inbound webhook triggers in the caller's org (or a customer's with org_id), cursor-paginated. Requires events.read.

Operation: `listWebhookTriggers`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `limit` | query | integer | No | Page size. Values above 100 are clamped to 100. |
| `cursor` | query | string | No | nextCursor from the previous page. |
| `search` | query | string | No |  |
| `status` | query | string | No | One of: `ACTIVE`, `DISABLED`. |
| `include_instances` | query | string | No | true also lists triggers created by installations (per-customer instances). One of: `true`, `false`. |
| `orgId` | query | string | No | The customer whose triggers to list: the id you gave it at creation (orgId), or fastn's id. Must be a customer of the caller's org, otherwise 403. Replaces org_id. |
| `org_id` | query | string | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `200`: { data: Trigger[], nextCursor, hasMore, total }
* `403`: org_id is not a customer of the caller's org

### Create a webhook trigger

```http
POST /v1/webhooks
```

Creates an inbound webhook trigger and returns its public triggerUrl, which is what you hand to the external system. routes bind it to workflows; a trigger created with no routes accepts events and delivers them nowhere, and a route pinned (env) to an environment the workflow is not deployed to dead-letters every event (the response carries a warning for either). authMethod API_KEY (default) makes callers send a fastn API key. orgId creates it for a customer of the caller's org. A custom id must be URL-safe; a taken id is a 409. Requires events.create.

Operation: `createWebhookTrigger`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | No |  |
| `name` | `string` | Yes |  |
| `status` | `string` | No | One of: `ACTIVE`, `DISABLED`. |
| `installationId` | `string` | No |  |
| `authMethod` | `string` | No | One of: `API_KEY`, `NONE`. Default: `"API_KEY"`. |
| `routeExecutionMode` | `string` | No | One of: `parallel`, `sequential`. Default: `"parallel"`. |
| `dlqConfiguration` | `object` | No |  |
| `dlqConfiguration.maxRetries` | `integer` | No | Default: `3`. |
| `dlqConfiguration.backoffStrategy` | `string` | No | One of: `exponential`, `linear`, `fixed`. Default: `"exponential"`. |
| `dlqConfiguration.backoffDelayMs` | `integer` | No |  |
| `additionalConfig` | `object` | No |  |
| `routes` | `object[]` | No |  |
| `routes[].routeId` | `string` | Yes |  |
| `routes[].routeType` | `string` | No | One of: `API`. Default: `"API"`. |
| `routes[].headers` | `object` | No |  |
| `routes[].payload` | `object` | No |  |
| `routes[].env` | `string` | No | Environment this route fires into. Omit it to run the latest published version (test), which is right for almost every trigger. Set it only to an environment the workflow is already deployed to: a route pinned to an environment with no active deployment dead-letters every event or scheduled fire, and a webhook, app-event or scheduler create/update answers with a warning naming the route. |
| `routes[].installationId` | `string` | No |  |
| `routes[].tenantResolver` | `object` | No |  |
| `routes[].tenantResolver.source` | `string` | Yes | One of: `header`, `body`. |
| `routes[].tenantResolver.field` | `string` | Yes |  |
| `orgId` | `string` | No | The customer: the id you gave it (its external ref), or its fastn id. |

**Responses**

* `201`: { data: trigger with triggerUrl, warning? }
* `400`: Invalid JSON or a body that fails validation
* `409`: A trigger with that id already exists

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `warning` | `string` | Present when the trigger was saved but will not deliver as configured: a route is pinned (routes[].env) to an environment the workflow has no active deployment in (or, for test, no published version), so every event or scheduled fire that route receives is dead-lettered; for a webhook trigger, also when it has no routes. Names the route, the environment and the fix: deploy the workflow there, or remove env from the route to run the latest published version (test). |

### Delete webhook triggers in bulk

```http
POST /v1/webhooks/bulk-delete
```

Deletes up to 100 webhook triggers by id. Ids that are not found are reported in failed rather than failing the request. Requires events.delete.

Operation: `bulkDeleteWebhookTriggers`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | `string[]` | Yes |  |

**Responses**

* `200`: { data: { deleted: string[], failed: { id, reason }[] } }
* `400`: Invalid JSON or a body that fails validation

### Get a webhook trigger

```http
GET /v1/webhooks/{id}
```

Returns one webhook trigger with its route bindings and public triggerUrl. Requires events.read.

Operation: `getWebhookTrigger`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: trigger with triggerUrl }
* `404`: Not found in the caller's org

### Update a webhook trigger

```http
PUT /v1/webhooks/{id}
```

Partially updates a webhook trigger. routes, when sent, replaces the whole binding list. Requires events.update.

Operation: `updateWebhookTrigger`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No |  |
| `status` | `string` | No | One of: `ACTIVE`, `DISABLED`. |
| `authMethod` | `string` | No | One of: `API_KEY`, `NONE`. |
| `routeExecutionMode` | `string` | No | One of: `parallel`, `sequential`. |
| `dlqConfiguration` | `object` | No |  |
| `dlqConfiguration.maxRetries` | `integer` | No | Default: `3`. |
| `dlqConfiguration.backoffStrategy` | `string` | No | One of: `exponential`, `linear`, `fixed`. Default: `"exponential"`. |
| `dlqConfiguration.backoffDelayMs` | `integer` | No |  |
| `additionalConfig` | `object` | No |  |
| `routes` | `object[]` | No |  |
| `routes[].routeId` | `string` | Yes |  |
| `routes[].routeType` | `string` | No | One of: `API`. Default: `"API"`. |
| `routes[].headers` | `object` | No |  |
| `routes[].payload` | `object` | No |  |
| `routes[].env` | `string` | No | Environment this route fires into. Omit it to run the latest published version (test), which is right for almost every trigger. Set it only to an environment the workflow is already deployed to: a route pinned to an environment with no active deployment dead-letters every event or scheduled fire, and a webhook, app-event or scheduler create/update answers with a warning naming the route. |
| `routes[].installationId` | `string` | No |  |
| `routes[].tenantResolver` | `object` | No |  |
| `routes[].tenantResolver.source` | `string` | Yes | One of: `header`, `body`. |
| `routes[].tenantResolver.field` | `string` | Yes |  |

**Responses**

* `200`: { data: trigger, warning? }
* `400`: Invalid JSON or a body that fails validation
* `404`: Not found in the caller's org

**Response fields**

| Field | Type | Description |
| --- | --- | --- |
| `data` | `object` |  |
| `warning` | `string` | Present when the trigger was saved but will not deliver as configured: a route is pinned (routes[].env) to an environment the workflow has no active deployment in (or, for test, no published version), so every event or scheduled fire that route receives is dead-lettered; for a webhook trigger, also when it has no routes. Names the route, the environment and the fix: deploy the workflow there, or remove env from the route to run the latest published version (test). |

### Delete a webhook trigger

```http
DELETE /v1/webhooks/{id}
```

Deletes a webhook trigger; its URL stops accepting events. Requires events.delete.

Operation: `deleteWebhookTrigger`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: { deleted: true } }
* `404`: Not found in the caller's org

### Webhook trigger route stats

```http
GET /v1/webhooks/{id}/stats
```

Per-route delivery counters for one webhook trigger. Requires events.read.

Operation: `getWebhookTriggerStats`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: route stats }
* `404`: Not found in the caller's org

## Dlq

### List dead-letter entries

```http
GET /v1/dlq
```

Lists dead-letter entries in the caller's org: deliveries that exhausted their retries, with the request payload, eventId, routeId, last error and attempt count. Filter by triggerId; cursor-paginated (limit max 100). Requires events.read.

Operation: `listDlq`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `limit` | query | integer | No |  |
| `cursor` | query | string | No |  |
| `triggerId` | query | string | No |  |

**Responses**

* `200`: Failed deliveries with request payload/eventId/routeId, error, attempts

### Delete a DLQ entry

```http
DELETE /v1/dlq/{id}
```

Discards one dead-letter entry without re-delivering it. Requires events.delete; 404 when the entry is not in the caller's org.

Operation: `deleteDlqEntry`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { data: { deleted: true } }
* `404`: Not found in the caller's org

### Replay DLQ entry

```http
POST /v1/dlq/{id}/replay
```

Queues one dead-letter entry's original payload for re-delivery to its route. Requires events.replay; 404 when the entry is not in the caller's org, 409 when the trigger or the route binding it targeted no longer exists.

Operation: `replayDlqEntry`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: { replayed: true, dispatchId }

## Events

### List received events

```http
GET /v1/events
```

Events the pipeline consumed, newest first, with the outcome each one got: dispatched (enqueued to its route bindings), no_routes (accepted but the trigger has no bindings, so delivered nowhere), dropped (the trigger was deleted or disabled between ingest and consumption), skipped_backlog (a scheduler fire not dispatched because a run it would start is already waiting for a concurrency slot; payload.skipped says which routes and why), or skipped_quota (a scheduler fire not dispatched because the org that owns the workflow has used its executions_per_month; payload.quotaExceeded names the route ids). An event whose every run so far ended through fastn.skip(reason) also carries runOutcome: "skipped" (absent otherwise). Scoped by org_id OR org_id.

Operation: `listEvents`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `since` | query | string | No |  |
| `triggerId` | query | string | No |  |
| `type` | query | string | No | One of webhook, scheduled, manual. Anything else is a 400 rather than an ignored filter. One of: `webhook`, `scheduled`, `manual`. |
| `env` | query | string | No | Environment slug (test, live, or a custom one). Events have no environment of their own, so this matches events whose trigger has a route into that environment; a route with no env runs in test. An event whose trigger fans out to two environments is listed under both. A malformed slug is a 400. |
| `search` | query | string | No | Case-insensitive needle over source, connectorId, id, status and type. |
| `limit` | query | integer | No | Rows per page. Default 20, max 100, an unparameterised call still gets the 20-row page it always did. |
| `offset` | query | integer | No | Zero-based row offset. Rows are ordered receivedAt DESC, id DESC so paging cannot repeat or skip rows that share a timestamp. |
| `delivery` | query | string | No | Lists the events behind a Reporting (Overview) count. dlq: dead-letter deliveries that will not be retried again (dead, or failed with every retry spent), first failed in [since, until), excluding routes to workflows labelled Internal or Staging. retrying: dead-letter deliveries still due another attempt, of any age unless since/until bound when they first failed. waiting: events received in the last hour, dispatched, with no workflow run yet (since/until are a 400 here). The Overview counts deliveries; this lists the distinct events they belong to, newest delivery first, so an event dead-lettered on two routes is one row. A delivery with no event id, or whose event is no longer kept, has no row. type, triggerId, env and search apply on top; /counts counts the same set. Anything else is a 400. One of: `dlq`, `retrying`, `waiting`. |
| `outcome` | query | string | No | Lists the events behind a Reporting (Overview) events or retry number, over the Overview's window (since = window.from, until = window.to, no until when it ends now) and customer. Event numbers: received, first_attempt, recovered, not_processed, in_progress, replayed, replay_succeeded, replay_failed, replayed_from_dlq, rerun_by_hand, event_replay, after_dlq: the events the trigger_event_outcomes rows summed for that number count, by the hour each was received in, classified again when listed (an event whose outcome changed since the summary's last pass is listed under its new one). Delivery numbers: recovered_by_retry, sent_to_dlq: the distinct events the counted deliveries carried. Every response carries countedAs { unit: events\|deliveries, count (the Overview's number), unlisted (deliveries with no event to list), note }. Cannot be combined with delivery. A customer-scoped session gets 403. Anything else is a 400. One of: `received`, `first_attempt`, `recovered`, `not_processed`, `in_progress`, `replayed`, `replay_succeeded`, `replay_failed`, `replayed_from_dlq`, `rerun_by_hand`, `event_replay`, `after_dlq`, `recovered_by_retry`, `sent_to_dlq`. |
| `until` | query | string | No | Exclusive upper bound on receivedAt (with delivery=dlq or retrying, on when the delivery first failed). A malformed timestamp is a 400. |
| `customer` | query | string | No | Narrows to one customer, inside the caller's scope. The caller's own org id: its events with no customer on them (with delivery, the dead letters of its own triggers). An customer of the caller: events whose orgId is that customer (with delivery=dlq/retrying, the dead letters its triggers hold). Anything else is a 404. A token scoped to an customer may name only that customer. |

**Responses**

* `200`: { data: Event[], pagination: { total, limit, offset, totalIsLowerBound } }, id, orgId, orgId, triggerId, type, source, payload, status, receivedAt (createdAt is an alias). total stops counting at 10000, at which point totalIsLowerBound is true.
* `400`: Malformed since, until or env, unknown type, delivery or outcome, outcome with delivery, or since/until with delivery=waiting
* `403`: outcome from a customer-scoped session
* `404`: customer is not the caller or one of its customers
* `503`: delivery=waiting could not be read

### List alert delivery targets

```http
GET /v1/events/alerts/channels/{connectionId}/targets
```

Lists where a messaging connection can post alerts (Slack channels, or Teams teams and channels), running the connector's list action as the caller. Roles: owner, admin, developer, end_user.

Operation: `listAlertChannelTargets`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `connectionId` | path | string | Yes |  |
| `connectorSlug` | query | string | Yes | Connector of the connection, e.g. slack or microsoft-teams. |
| `teamId` | query | string | No | Teams only: list the channels of this team. |

**Responses**

* `200`: { data: targets }
* `400`: connectorSlug missing
* `502`: The provider call failed

### Alert delivery limits

```http
GET /v1/events/alerts/limits
```

The alert cool-downs, per-minute send caps and watcher intervals the event service is running with. Roles: owner, admin, developer, end_user.

Operation: `getAlertLimits`

**Responses**

* `200`: { data: { cooldownMs, ruleSendsPerMinute, orgSendsPerMinute, testSendsPerMinute, failureWatchIntervalMs, codeWatchIntervalMs, evalIntervalMs } }

### Send a test alert

```http
POST /v1/events/alerts/{id}/test
```

Sends a one-off test notification for one alert rule to its configured channels. Returns 200 even when a channel failed; delivered and error say what happened. An end_user can only test its own customer's rules. Roles: owner, admin, developer, end_user.

Operation: `testAlert`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | Alert rule id |

**Responses**

* `200`: { data: { delivered, error? } }
* `404`: Alert rule not found in the caller's scope

### Count received events

```http
GET /v1/events/count
```

Counts received events matching the same filters as GET /api/v1/events, without the 10000 cap the list's total carries. Scoped by org_id OR org_id.

Operation: `countEvents`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `since` | query | string | No | Only events received at or after this ISO 8601 time. Malformed is a 400. |
| `triggerId` | query | string | No | Only this trigger's events. trigger_id is accepted as an alias. |
| `type` | query | string | No | Anything else is a 400. One of: `webhook`, `scheduled`, `manual`. |
| `env` | query | string | No | Environment slug; matches events whose trigger has a route into it. Malformed is a 400. |
| `search` | query | string | No | Case-insensitive needle over source, connectorId, id, status and type. |

**Responses**

* `200`: { data: { total } }
* `400`: Malformed since or env, or unknown type

### Per-type event totals

```http
GET /v1/events/counts
```

Totals for the events list's filter pills, over the whole scoped and filtered set rather than one page. Deliberately ignores ?type=, each count is what that pill would show if it were selected. Capped by the same 10000-row window as the list total, so the pills and the pager cannot report two different numbers for one set.

Operation: `eventCounts`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `since` | query | string | No |  |
| `triggerId` | query | string | No |  |
| `env` | query | string | No | Environment slug; same meaning as on the list. |
| `search` | query | string | No |  |
| `delivery` | query | string | No | Same meaning as on the list; the pills count the events the list shows. One of: `dlq`, `retrying`, `waiting`. |
| `outcome` | query | string | No | Same meaning as on the list; data carries countedAs. One of: `received`, `first_attempt`, `recovered`, `not_processed`, `in_progress`, `replayed`, `replay_succeeded`, `replay_failed`, `replayed_from_dlq`, `rerun_by_hand`, `event_replay`, `after_dlq`, `recovered_by_retry`, `sent_to_dlq`. |
| `until` | query | string | No | Same meaning as on the list. |
| `customer` | query | string | No | Same meaning as on the list. |

**Responses**

* `200`: { data: { total, byType: { webhook, scheduled, manual }, totalIsLowerBound } }
* `400`: Malformed since or until, unknown delivery or outcome, outcome with delivery
* `403`: outcome from a customer-scoped session
* `404`: customer is not the caller or one of its customers

### Get one received event

```http
GET /v1/events/{id}
```

Resolves the evt_ id the webhook ingest returned in its 202. replayOf is the event this one replays (POST /api/v1/events/{id}/replay mints a new id), null otherwise; replayedAt is set on an event that was replayed or redelivered from the dead-letter queue.

Operation: `getEvent`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: The event with its pipeline outcome, replayedAt and replayOf
* `404`: Not found or out of scope

### Failed deliveries of one event

```http
GET /v1/events/{id}/attempts
```

Every delivery of the event that failed, from the dead-letter queue: route, attempts of max, status, whether retries are exhausted, the last error, first failure, last attempt and next retry. A delivery that succeeded first time has no row; the run it started is listed by GET /api/v1/workflows/executions?eventId=.

Operation: `getEventAttempts`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `200`: Array of attempts, oldest first, at most 50
* `404`: Event not found in the caller's scope

### Replay a received event

```http
POST /v1/events/{id}/replay
```

Re-delivers the stored payload through the event's trigger as a NEW event (its own id and row), using the trigger's current routes. A webhook-trigger event re-enters the ingest stream; an app-trigger event is dispatched to its routes; a scheduled or manual event runs the scheduler now, shares Run now's cooldown and, like Run now, also requires events.create. Dispatched with the original's forwarded headers (minus credentials and signatures), so it runs for the same customer. Counts against the daily event quota. Sets replayedAt on the original (best-effort; null if it could not be recorded).

Operation: `replayEvent`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes |  |

**Responses**

* `202`: { eventId, replayedFrom, replayedAt, status: accepted }
* `400`: Malformed event id
* `403`: Caller lacks events.replay, or events.create for a scheduled/manual event
* `404`: Event not found or out of scope
* `409`: Nothing to replay into: TRIGGER_NOT_FOUND, TRIGGER_DISABLED, NO_ROUTES, ROUTE_TARGET_GONE (every bound workflow deleted or disabled) or NOT_REPLAYABLE (recorded without a trigger)
* `429`: QUOTA_EXCEEDED (daily event quota; for a scheduled or manual event, the run quota of the org that owns every route's workflow), or RATE_LIMITED (org ingest budget, or the scheduler was fired within its cooldown; Retry-After set)
