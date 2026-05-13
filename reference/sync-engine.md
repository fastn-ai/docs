---
description: >-
  ID mapping, dependency resolution, and conflict resolution strategies for
  cross-system data synchronization.
---

# Sync Engine

The Sync Engine manages bidirectional data synchronization between connected systems. It handles the three hardest problems in integration: mapping IDs across systems, determining sync order, and resolving conflicts.

### ID Mapping

Every record that syncs between systems gets an ID mapping entry that links the source ID to the target ID.

#### Mapping record

| Field            | Description                                  |
| ---------------- | -------------------------------------------- |
| `source_id`      | Record ID in the source system               |
| `target_id`      | Corresponding record ID in the target system |
| `tenant_id`      | Tenant scope                                 |
| `integration_id` | Integration scope                            |
| `entity_type`    | CDM entity type (contact, order, etc.)       |
| `status`         | pending, mapped, failed, stale               |
| `created_at`     | When the mapping was created                 |
| `updated_at`     | When the mapping was last verified           |

#### Storage

* **Redis cache** for fast lookups during flow execution
* **PostgreSQL** for persistent storage and recovery
* Read-through caching: check Redis first, fall back to PostgreSQL, populate cache on miss

#### Status lifecycle

```
pending → mapped (successful sync)
pending → failed (sync error)
mapped → stale (target record deleted or modified externally)
stale → mapped (re-synced successfully)
```

### Dependency Resolution

Some entities must sync before others. You can't sync an Order's line items before the Products they reference exist in the target system.

#### How it works

Fastn uses **Kahn's algorithm** (topological sort) to determine sync order from the entity dependency graph.

#### Default dependency order

```
1. Contact        (no dependencies)
2. Product        (no dependencies)
3. InventoryLevel (depends on: Product)
4. Order          (depends on: Contact, Product)
5. Invoice        (depends on: Contact, Order)
6. Fulfillment    (depends on: Order)
```

#### Cycle detection

If the dependency graph contains a cycle (A depends on B, B depends on A), the engine reports a clear error with the cycle path. Cycles must be resolved by the SaaS Admin before sync can proceed.

#### Per-partner configuration

Entity dependency graphs are configurable per SaaS partner. Different business models may have different dependency relationships.

### Conflict Resolution

When the same record is modified in both source and target systems between syncs, a conflict occurs. Fastn supports 5 strategies:

| Strategy          | Behavior                                                                           | Best for                           |
| ----------------- | ---------------------------------------------------------------------------------- | ---------------------------------- |
| `source_wins`     | Source value always takes precedence. Target changes are overwritten.              | Source is the authoritative system |
| `target_wins`     | Target value is preserved. Source changes are ignored for conflicting fields.      | Target is the authoritative system |
| `last_write_wins` | Most recent timestamp wins. Whichever system was updated last takes precedence.    | Eventually consistent systems      |
| `merge`           | Field-level merge of both values. Non-conflicting fields from both sides are kept. | Complementary data sources         |
| `manual`          | Flag the record for human review. No automatic resolution.                         | High-value or ambiguous conflicts  |

#### Conflict record schema

| Field                | Description                                            |
| -------------------- | ------------------------------------------------------ |
| `id`                 | Unique conflict ID                                     |
| `entity_type`        | CDM entity type                                        |
| `source_record`      | Full source record data                                |
| `target_record`      | Full target record data                                |
| `conflicting_fields` | List of fields with different values                   |
| `strategy_applied`   | Which resolution strategy was used                     |
| `resolution`         | The resolved values (or `pending` for manual strategy) |
| `tenant_id`          | Tenant scope                                           |
| `resolved_by`        | System (automatic) or user ID (manual)                 |
| `created_at`         | When the conflict was detected                         |
| `resolved_at`        | When the conflict was resolved                         |

#### Configuration

Conflict resolution strategy is set per integration, per entity type:

```
Integration: Shopify ↔ Xero
  Contact: source_wins (Shopify is authoritative for customer data)
  Order: source_wins (Shopify is authoritative for orders)
  Invoice: target_wins (Xero is authoritative for invoices)
```

Strategy can also be overridden at the tenant level for specific customers with different requirements.
