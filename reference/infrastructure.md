---
description: >-
  Service topology, package architecture, database schema overview, and
  deployment options.
---

# Infrastructure

### Service topology

| Service             | Port | Technology           | Purpose                                        |
| ------------------- | ---- | -------------------- | ---------------------------------------------- |
| **Control Plane**   | 3001 | Fastify + TypeScript | Primary REST API, all business logic           |
| **Deploy Service**  | 3002 | Fastify              | Build and deploy workflows to Lambda/Cloud Run |
| **Audit Service**   | 3003 | Fastify              | Immutable audit event log                      |
| **Metrics Service** | 3004 | Fastify              | SLA monitoring, execution metrics              |
| **Mock Server**     | 3005 | Fastify + Faker.js   | Realistic test data generation                 |
| **Dashboard**       | 5173 | React + Vite         | Single-page application UI                     |
| **Keycloak**        | 8080 | Java (Quarkus)       | OIDC/JWT identity provider                     |
| **PostgreSQL**      | 5432 | pgvector/pg16        | Primary database with vector search            |
| **Redis**           | 6379 | Redis 7 Alpine       | Cache, streams, queues, working memory         |

### Package architecture

| Package             | Purpose                          | Key exports                                                                |
| ------------------- | -------------------------------- | -------------------------------------------------------------------------- |
| `@fastn/core`       | Shared types, schemas, utilities | Types, ID generators, error classes, logger, constants                     |
| `@fastn/builder`    | Workflow visual editor           | AST parser, canvas components, workflow store (Zustand)                    |
| `@fastn/runtime`    | Execution engine                 | `executeWorkflow`, `createLambdaHandler`, `createCloudRunHandler`, tracing |
| `@fastn/workflow`   | Workflow DSL                     | `workflow()`, `step()`, triggers, `defineConfig()`                         |
| `@fastn/connectors` | Third-party integrations         | `ConnectorRegistry`, built-in connectors                                   |
| `@fastn/cli`        | Developer tooling                | `dev`, `run`, `deploy`, `logs`, `destroy` commands                         |

### Database schema

40+ tables organized by domain. Primary database: PostgreSQL 16 with pgvector extension.

#### Core platform tables

| Table              | Purpose                    | Key columns                                                     |
| ------------------ | -------------------------- | --------------------------------------------------------------- |
| `saas_partners`    | SaaS partner organizations | id, name, domain, status, plan\_tier, company\_profile (JSONB)  |
| `tenants`          | End-user tenants           | id, saas\_partner\_id, name, status, plan\_tier, region, config |
| `platform_users`   | All platform users         | id, email, status, tenant\_id, saas\_partner\_id                |
| `signup_attempts`  | Signup validation results  | email, domain, outcome, classification\_data                    |
| `company_profiles` | Company analysis data      | domain, industry, tech\_stack, competitors                      |

#### RBAC tables

| Table                   | Purpose                                             |
| ----------------------- | --------------------------------------------------- |
| `roles`                 | System and custom roles with scope levels           |
| `permissions`           | Permission matrix: role + resource + action + scope |
| `actor_roles`           | Role assignments to users/service accounts/agents   |
| `si_tenant_assignments` | SI-to-tenant assignments with expiry                |

#### Integration & workflow tables

| Table             | Purpose                                            |
| ----------------- | -------------------------------------------------- |
| `connectors`      | Connector definitions with capabilities and config |
| `integrations`    | Tenant-connector bindings with status              |
| `flows`           | Workflow specifications (JSONB) with status        |
| `flow_executions` | Execution history with trigger events and results  |
| `field_mappings`  | Source-to-target field mappings with transforms    |
| `cdm_fields`      | CDM field definitions with pgvector embeddings     |

#### Sync & event tables

| Table                   | Purpose                                                |
| ----------------------- | ------------------------------------------------------ |
| `id_mappings`           | Cross-system ID mappings per tenant/integration/entity |
| `sync_state`            | Sync cursor and status per entity type                 |
| `backfill_jobs`         | Background data backfill tracking                      |
| `conflict_records`      | Sync conflict history and resolution                   |
| `entity_dependencies`   | Entity sync order dependencies                         |
| `event_outbox`          | Transactional outbox for event publishing              |
| `dead_letter_queue`     | Failed events with retry tracking                      |
| `webhook_registrations` | Webhook endpoint registrations                         |
| `poll_schedules`        | Adaptive polling schedules                             |
| `snapshot_index`        | Record hashes for change detection                     |

#### AI & memory tables

| Table                  | Purpose                                             |
| ---------------------- | --------------------------------------------------- |
| `agent_episodes`       | Episodic memory with pgvector embeddings (1536-dim) |
| `agent_facts`          | Semantic facts with confidence scoring              |
| `agent_procedures`     | Procedural memory with success rate tracking        |
| `api_entities`         | Discovered API entities per SaaS                    |
| `entity_fields`        | API fields with pgvector embeddings                 |
| `entity_relationships` | Entity relationship graph                           |

#### Platform tables

| Table                | Purpose                                      |
| -------------------- | -------------------------------------------- |
| `quota_limits`       | Per-scope quota configuration                |
| `usage_records`      | Timestamped usage events with cost           |
| `config_entries`     | Hierarchical config with optional encryption |
| `audit_log`          | Immutable audit trail                        |
| `notifications`      | User notifications with read tracking        |
| `hub_configs`        | SaaS partner hub customization               |
| `workflow_templates` | Reusable workflow templates                  |

### Store layer

Three storage backends with optional Redis caching:

| Backend         | Use case                      | Implementation                            |
| --------------- | ----------------------------- | ----------------------------------------- |
| **Memory**      | Testing, ephemeral dev        | In-memory hash maps, no persistence       |
| **SQLite**      | Local development (default)   | `better-sqlite3`, file: `./data/fastn.db` |
| **PostgreSQL**  | Production                    | pg driver, SSL, connection pooling        |
| **Redis Cache** | Optional layer on any backend | Read-through cache, configurable TTL      |

### Deployment options

#### Docker Compose (development)

Full-stack local environment with 10 containers including an installer container for npm dependencies. Named volumes for persistence (pgdata, redisdata, node\_modules).

#### Kubernetes

* Dedicated namespace: `fastn`
* Deployment manifests for all 5 services
* Ingress routing configuration
* Secrets via example templates
* Helm chart (v0.1.0) with configurable replicas, resources, and ingress

#### Cloud infrastructure (Pulumi)

| Provider | Database       | Cache             | Workflow execution |
| -------- | -------------- | ----------------- | ------------------ |
| **AWS**  | RDS PostgreSQL | ElastiCache Redis | Lambda             |
| **GCP**  | Cloud SQL      | Memorystore       | Cloud Run          |

Configuration-driven provider selection. Tag-based resource organization.

### Frontend architecture

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| React 18       | UI framework                  |
| React Router 7 | Routing                       |
| Zustand        | Global state management       |
| Keycloak-js    | Authentication                |
| @xyflow/react  | Workflow canvas visualization |
| Monaco Editor  | Inline code editing           |
| Vite           | Build and development server  |

### Observability

#### Metrics Service (port 3004)

* Workflow execution metrics: duration, success rate, failure patterns
* Step-level metrics for bottleneck identification
* Tenant overview with aggregated health indicators
* Time series data for trend analysis

#### Audit Service (port 3003)

* Immutable audit log
* Actor types: user, service\_account, agent, system
* Outcomes: success, failure, denied, partial
* Queryable by tenant, actor, resource, time range

#### Distributed tracing

* OpenTelemetry integration in `@fastn/runtime`
* Trace propagation across workflow steps
* Span attributes for connector, tenant, and execution context
