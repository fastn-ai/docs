---
description: "Endpoints of yours that fastn delivers events to."
---

# Event subscriptions

Base URL, authentication and errors are on the [REST API overview](README.md).

## Event subscriptions

### List event subscriptions

```http
GET /v1/event-subscriptions
```

The org's registered event endpoints. The signing secret is never returned here. Owner, admin or developer of the partner org (not a customer workspace).

Operation: `listEventSubscriptions`

**Responses**

* `200`: { data: [subscription] }

### Create an event subscription

```http
POST /v1/event-subscriptions
```

Registers an https endpoint for signed events (X-Fastn-Timestamp, X-Fastn-Signature = sha256=HMAC(secret, "&lt;timestamp>.&lt;body>"), X-Fastn-Event-Id). Deliveries retry with backoff for 24 hours; the event id never changes, so drop repeats by id. The secret (whsec_...) is returned ONCE. Private, internal and non-https URLs are refused. Owner, admin or developer of the partner org (not a customer workspace).

Operation: `createEventSubscription`

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | `string` | Yes | https endpoint |
| `eventTypes` | `string[]` | No | Event types to send. Empty or omitted: every account and setup-link event (connection.*, setup_link.*). connector.event, unified.event and workflow.event are sent only when listed. One of: `connection.connected`, `connection.revoked`, `connection.expired`, `setup_link.completed`, `setup_link.expired`, `connector.event`, `unified.event`, `workflow.event`. |
| `connectors` | `string[]` | No | connector.event only: send provider events from these connectors (slug or connector id). Empty or omitted: every connector. |
| `providerEvents` | `string[]` | No | connector.event only: send only these provider event names (as the connector lists them, e.g. leadgen). Empty or omitted: every event. |
| `entities` | `string[]` | No | unified.event only: send unified events for these entities only, as "category/entity" (e.g. crm/contact). Empty or omitted: every entity. |
| `connectorCategories` | `string[]` | No | connector.event, unified.event and workflow.event: send events from connectors in these catalog categories (e.g. project-management). An event matches when its connector is in connectors OR its connector's category is here. Both empty or omitted: every connector. One of: `ai-ml`, `developer-tools`, `search-web`, `data-database`, `cloud-devops`, `crm-sales`, `marketing`, `finance-payments`, `ecommerce`, `communication`, `social-media`, `productivity`, `project-management`, `docs-knowledge`, `analytics-monitoring`, `security`, `it-service`, `design`, `maps-location`, `entertainment-media`, `other`. |
| `workflowEvents` | `string[]` | No | workflow.event only: send only events workflow code emits under these names (fastn.events.emit("ticket.created", ...)). Empty or omitted: every name. The connectors filter applies too, matched against the connector the code named. |
| `payloadTemplate` | `object` | No | workflow.event only: send the body in the endpoint's own schema. { connectors?: { &lt;connector slug or id>: schema }, default?: schema }, where schema is a JSON Schema object: { type: "object", properties: { &lt;field>: { type?, "x-source"?: &lt;dotted path into the event, e.g. payload.finding.id>, const?, default?, properties? } }, required?: [&lt;field>] }. The event's connector picks the schema, else default. type (string, number, integer, boolean, object, array) converts what it can; an empty optional field is left out; an event that cannot fill a required field is not sent and its delivery records why. With no schema (or null) the standard body is sent. Headers are unchanged; the signature covers the body actually sent. |
| `endOrgId` | `string` | No | Only events about this customer (a child of the org): fastn's org id, or the id you gave the customer at creation (orgId / externalRef). Omit for every customer. |
| `description` | `string` | No |  |
| `enabled` | `boolean` | No |  |

**Responses**

* `201`: { data: subscription & { secret } }
* `400`: Validation error, URL refused, or endOrgId is not the org's customer
* `403`: Role not allowed

### Replay a delivery

```http
POST /v1/event-subscriptions/deliveries/{id}/replay
```

Sends a delivery again (same event id, marked as a redelivery), including one that was given up on. Owner, admin or developer of the partner org (not a customer workspace).

Operation: `replayEventDelivery`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | evd_ id |

**Responses**

* `202`: { data: { id, status: 'pending' } }
* `404`: Not found

### Get an event subscription

```http
GET /v1/event-subscriptions/{id}
```

One subscription, without its secret. Owner, admin or developer of the partner org (not a customer workspace).

Operation: `getEventSubscription`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | esub_ id |

**Responses**

* `200`: { data: subscription }
* `404`: Not found

### Update an event subscription

```http
PATCH /v1/event-subscriptions/{id}
```

Change the URL, event types, filters, payload template (null clears it), description, or pause it (enabled: false; events queue and are sent when it is enabled again, within 24 hours). Owner, admin or developer of the partner org (not a customer workspace).

Operation: `updateEventSubscription`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | esub_ id |

**Request body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | `string` | No |  |
| `eventTypes` | `string[]` | No | Event types to send. Empty or omitted: every account and setup-link event (connection.*, setup_link.*). connector.event, unified.event and workflow.event are sent only when listed. One of: `connection.connected`, `connection.revoked`, `connection.expired`, `setup_link.completed`, `setup_link.expired`, `connector.event`, `unified.event`, `workflow.event`. |
| `connectors` | `string[]` | No |  |
| `providerEvents` | `string[]` | No |  |
| `entities` | `string[]` | No |  |
| `connectorCategories` | `string[]` | No | connector.event, unified.event and workflow.event: send events from connectors in these catalog categories (e.g. project-management). An event matches when its connector is in connectors OR its connector's category is here. Both empty or omitted: every connector. One of: `ai-ml`, `developer-tools`, `search-web`, `data-database`, `cloud-devops`, `crm-sales`, `marketing`, `finance-payments`, `ecommerce`, `communication`, `social-media`, `productivity`, `project-management`, `docs-knowledge`, `analytics-monitoring`, `security`, `it-service`, `design`, `maps-location`, `entertainment-media`, `other`. |
| `workflowEvents` | `string[]` | No | workflow.event only: send only events workflow code emits under these names (fastn.events.emit("ticket.created", ...)). Empty or omitted: every name. The connectors filter applies too, matched against the connector the code named. |
| `payloadTemplate` | `object` | No | workflow.event only: send the body in the endpoint's own schema. { connectors?: { &lt;connector slug or id>: schema }, default?: schema }, where schema is a JSON Schema object: { type: "object", properties: { &lt;field>: { type?, "x-source"?: &lt;dotted path into the event, e.g. payload.finding.id>, const?, default?, properties? } }, required?: [&lt;field>] }. The event's connector picks the schema, else default. type (string, number, integer, boolean, object, array) converts what it can; an empty optional field is left out; an event that cannot fill a required field is not sent and its delivery records why. With no schema (or null) the standard body is sent. Headers are unchanged; the signature covers the body actually sent. |
| `description` | `string` | No |  |
| `enabled` | `boolean` | No |  |

**Responses**

* `200`: { data: subscription }
* `400`: Validation error or URL refused
* `404`: Not found

### Delete an event subscription

```http
DELETE /v1/event-subscriptions/{id}
```

Removes the endpoint and its queued deliveries. Owner, admin or developer of the partner org (not a customer workspace).

Operation: `deleteEventSubscription`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | esub_ id |

**Responses**

* `200`: { data: { deleted: true } }
* `404`: Not found

### List deliveries

```http
GET /v1/event-subscriptions/{id}/deliveries
```

Recent deliveries to this endpoint with status (pending, delivered, dead), attempts and the last error. Owner, admin or developer of the partner org (not a customer workspace).

Operation: `listEventDeliveries`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | esub_ id |
| `status` | query | string | No | One of: `pending`, `delivered`, `dead`. |
| `limit` | query | integer | No |  |

**Responses**

* `200`: { data: [delivery] }
* `404`: Not found

### Rotate a subscription's signing secret

```http
POST /v1/event-subscriptions/{id}/rotate-secret
```

Issues a new secret, returned once. Deliveries sent after this are signed with it. Owner, admin or developer of the partner org (not a customer workspace).

Operation: `rotateEventSubscriptionSecret`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | esub_ id |

**Responses**

* `200`: { data: { id, secret } }
* `404`: Not found

### Send a test event

```http
POST /v1/event-subscriptions/{id}/test
```

Queues one signed endpoint.test event to the endpoint. Owner, admin or developer of the partner org (not a customer workspace).

Operation: `testEventSubscription`

**Parameters**

| Name | In | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | path | string | Yes | esub_ id |

**Responses**

* `202`: { data: { eventId } }
* `404`: Not found
