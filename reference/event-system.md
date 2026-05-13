---
description: >-
  Event pipeline stages, webhook receiver, Flow Router, Dead Letter Queue, and
  Synthetic Event Engine.
---

# Event System

Fastn uses an event-driven architecture for processing integration triggers. Events flow through a multi-stage pipeline ensuring reliability and at-least-once delivery.

### Event pipeline

Events pass through 6 stages:

| Stage            | What happens                                                                    | Technology                         |
| ---------------- | ------------------------------------------------------------------------------- | ---------------------------------- |
| **1. Receive**   | External events arrive via webhook receiver or synthetic polling                | Fastify HTTP server                |
| **2. Outbox**    | Events are written to the PostgreSQL outbox table within a database transaction | PostgreSQL transactional guarantee |
| **3. Fan-out**   | Outbox poller publishes events to Redis Streams using `FOR UPDATE SKIP LOCKED`  | Redis Streams                      |
| **4. Normalize** | Event normalizer creates a NormalizedEvent with a SHA-256 idempotency key       | In-memory processing               |
| **5. Route**     | Flow Router matches events to registered triggers using condition AST           | In-memory trigger index            |
| **6. Execute**   | Matched flows are dispatched to BullMQ for workflow execution                   | BullMQ job queue                   |

### Webhook receiver

Receives and validates incoming webhooks from third-party apps.

#### Verification

| Check                      | Method          | Details                                                                      |
| -------------------------- | --------------- | ---------------------------------------------------------------------------- |
| **Signature verification** | HMAC SHA-256    | Configurable secret per connector. Rejects requests with invalid signatures. |
| **Timestamp freshness**    | 5-minute window | Rejects webhooks older than 5 minutes to prevent replay attacks.             |
| **Deduplication**          | Redis-based     | Prevents duplicate processing of the same webhook.                           |

#### Webhook registration

Each connector-tenant pair has a registered webhook endpoint:

```
POST /api/v1/webhooks/{connector}/{tenant_id}
```

The webhook receiver extracts the connector and tenant context from the URL, validates the signature, and passes the payload to the event pipeline.

### Flow Router

Matches incoming events to registered triggers and dispatches flows for execution.

#### Trigger index

An in-memory index of all active triggers. When an event arrives, the router checks every trigger's conditions against the event data.

#### Condition AST operators

| Operator   | Description                  | Example                              |
| ---------- | ---------------------------- | ------------------------------------ |
| `eq`       | Equals                       | `status eq "completed"`              |
| `neq`      | Not equals                   | `status neq "cancelled"`             |
| `gt`       | Greater than                 | `total gt 100`                       |
| `lt`       | Less than                    | `quantity lt 0`                      |
| `in`       | Value in list                | `status in ["completed", "shipped"]` |
| `contains` | String contains              | `email contains "@company.com"`      |
| `exists`   | Field exists and is not null | `trackingNumber exists`              |

#### Priority routing

| Priority | Type           | Description                                      |
| -------- | -------------- | ------------------------------------------------ |
| **P1**   | User-triggered | API requests, manual triggers — highest priority |
| **P2**   | Event-driven   | Webhook events, app events                       |
| **P3**   | Background     | Scheduled workflows, batch processing            |
| **P4**   | Polling        | Synthetic events from polling — lowest priority  |

Higher priority events are processed first when the system is under load.

#### Dynamic trigger management

Triggers are registered and removed dynamically:

* When a flow is deployed, its trigger is registered in the index
* When a flow is undeployed or deleted, its trigger is removed
* Changes take effect immediately — no restart required

### Dead Letter Queue (DLQ)

Failed events that cannot be processed are captured in the DLQ.

#### What goes to the DLQ

* Events that fail processing after all retry attempts
* Events with invalid payloads that can't be normalized
* Events that match no registered trigger (configurable — can be dropped instead)

#### DLQ record schema

| Field           | Description                              |
| --------------- | ---------------------------------------- |
| `id`            | Unique DLQ entry ID                      |
| `event_payload` | Full original event data                 |
| `error_message` | Why processing failed                    |
| `error_context` | Stack trace, step name, connector info   |
| `tenant_id`     | Which tenant's event failed              |
| `connector`     | Source connector                         |
| `created_at`    | When the event entered the DLQ           |
| `retry_count`   | How many times replay has been attempted |
| `status`        | pending, replayed, expired               |

#### DLQ operations

* **Manual replay** — Retry a specific failed event
* **Automated replay** — Configure automatic retry policies
* **Retention** — Configurable cleanup policies for old DLQ entries
* **Depth monitoring** — DLQ depth is tracked and triggers alerts when thresholds are exceeded

### Synthetic Event Engine

Detects changes in external systems that don't support webhooks.

#### How it works

1. **Poll** — Fetch records from the external system at configurable intervals
2. **Hash** — Generate SHA-256 hash of each record
3. **Compare** — Compare current hashes against stored hashes in Redis (7-day TTL)
4. **Diff** — Field-level diffing identifies what changed
5. **Emit** — Generate synthetic events for new, updated, or deleted records

#### Adaptive polling

Polling intervals adjust automatically based on:

| Factor                | Effect                                      |
| --------------------- | ------------------------------------------- |
| **Changes detected**  | More changes → shorter intervals            |
| **Rate limiting**     | Rate limit responses → longer intervals     |
| **Business hours**    | More frequent polling during business hours |
| **Activity patterns** | Learning from historical change patterns    |

Base intervals are configurable per entity type.

#### Deletion detection

The engine detects deleted records by comparing the current snapshot against the previous one. Records present in the previous snapshot but absent in the current one are flagged as deleted.

#### Scheduling

Polling schedules are managed via Redis sorted sets for efficient scheduling across many tenants and entity types.
