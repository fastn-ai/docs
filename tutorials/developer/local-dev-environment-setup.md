---
description: >-
  Clone the repo, run the full Fastn platform stack locally with Docker Compose,
  and use the CLI for development workflows.
---

# Local Dev Environment Setup

**Prerequisites:** Docker and Docker Compose installed. Node.js 18+. Git. **Time:** 30 minutes **Outcome:** The full Fastn platform running locally — dashboard, control plane, database, and all supporting services.

### What you'll run

The local development environment spins up the full Fastn stack as Docker containers:

| Service         | Port | Technology           | Purpose                                |
| --------------- | ---- | -------------------- | -------------------------------------- |
| Dashboard       | 5173 | React + Vite         | The web UI you see at `live.fastn.ai`  |
| Control Plane   | 3001 | Fastify + TypeScript | Primary API — all business logic       |
| Deploy Service  | 3002 | Fastify              | Build and deploy workflows             |
| Audit Service   | 3003 | Fastify              | Immutable audit event log              |
| Metrics Service | 3004 | Fastify              | SLA monitoring and execution metrics   |
| Mock Server     | 3005 | Fastify + Faker.js   | Realistic test data generation         |
| Keycloak        | 8080 | Java (Quarkus)       | OIDC/JWT identity provider             |
| PostgreSQL      | 5432 | pgvector/pg16        | Primary database with vector search    |
| Redis           | 6379 | Redis 7 Alpine       | Cache, streams, queues, working memory |

> **🖼Diagram needed:** Architecture diagram showing all 9 services with their ports, how they connect (Control Plane → PostgreSQL, Redis; Dashboard → Control Plane; Keycloak → Control Plane), and the developer's interaction points.

### Step 1: Clone the repository

```bash
git clone https://github.com/fastnai/fastn.git
cd fastn
```

> ⚠️ **VERIFY:** Confirm the repository URL and whether it's public or requires access from the Fastn team.

### Step 2: Install dependencies

The Docker Compose setup includes an installer container that handles npm dependencies, but you'll also want local dependencies for IDE support:

```bash
npm install
```

> ⚠️ **VERIFY:** Confirm whether the project uses npm, yarn, or pnpm, and whether there's a root-level package.json or a monorepo setup with workspaces.

### Step 3: Start the stack

```bash
docker compose up
```

This starts all 10 containers (9 services + the installer). First run takes a few minutes while images are pulled and dependencies are installed.

Once running:

* Dashboard: [http://localhost:5173](http://localhost:5173/)
* Control Plane API: [http://localhost:3001](http://localhost:3001/)
* Keycloak admin: [http://localhost:8080](http://localhost:8080/)

> **📷 Screenshot needed:** Terminal output showing all containers starting up successfully with health checks passing.

> **📷 Screenshot needed:** Dashboard running at localhost:5173 — the login screen or home page.

### Step 4: Keycloak authentication

The local environment uses a pre-configured Keycloak realm (`fastn`) with two clients:

| Client      | Type         | Purpose                      |
| ----------- | ------------ | ---------------------------- |
| `fastn-app` | Public       | Dashboard SPA authentication |
| `fastn-api` | Confidential | Service-to-service API calls |

Social login (GitHub, Google) is pre-configured in the local realm. You can log into the dashboard using:

* The Keycloak admin console at `http://localhost:8080` (default credentials are in the Docker Compose file)
* Or via the social login providers if configured

> **📷 Screenshot needed:** Keycloak login screen with the Fastn custom theme showing the login options.

> ⚠️ **VERIFY:** Confirm the default Keycloak admin credentials for local development and whether they're set in the docker-compose.yml or a .env file.

### Step 5: Database setup

PostgreSQL starts with the `pgvector` extension enabled. On first run, the migration script creates all 40+ tables, indexes, RLS policies, and seeds the default roles.

The migration file:

```bash
# Location of the full platform migration
001_full_platform.sql
```

To verify the database is set up correctly:

```bash
# Connect to the local PostgreSQL
docker compose exec postgres psql -U fastn -d fastn

# Check table count
\dt

# Verify RLS policies exist
SELECT tablename, policyname FROM pg_policies;
```

> ⚠️ **VERIFY:** Confirm the exact migration file path and the PostgreSQL connection credentials (username, database name).

### The Fastn CLI

The `@fastn/cli` package provides development commands:

| Command         | What it does                                                       |
| --------------- | ------------------------------------------------------------------ |
| `fastn dev`     | Start the local development server with hot reload (`tsx --watch`) |
| `fastn run`     | Run a specific workflow locally                                    |
| `fastn deploy`  | Deploy a workflow to Lambda or Cloud Run                           |
| `fastn logs`    | View workflow execution logs                                       |
| `fastn destroy` | Tear down deployed infrastructure                                  |

Install the CLI globally:

```bash
npm install -g @fastn/cli
```

Or run it via npx:

```bash
npx @fastn/cli dev
```

> ⚠️ **VERIFY:** Confirm that `@fastn/cli` is published to npm and available for installation. If it's a private package, document the access requirements.

### Development workflow

Once the stack is running, a typical dev cycle looks like:

1. **Edit a flow** in TypeScript (see [Writing a Workflow](https://claude.ai/chat/writing-a-workflow-typescript-dsl.md))
2. **Hot reload** picks up the change automatically (`tsx --watch`)
3. **Test** using the dashboard at localhost:5173 or via cURL against localhost:3001
4. **Check logs** in the terminal or via the Logs section in the dashboard
5. **Iterate** — changes reflect immediately without restarting containers

#### Using the Mock Server

The Mock Server (port 3005) generates realistic test data using Faker.js. Use it to simulate connector responses without needing real third-party API credentials:

```bash
# Example: fetch mock Shopify orders
curl http://localhost:3005/shopify/orders
```

> ⚠️ **VERIFY:** Confirm the mock server endpoint patterns and what connector data it simulates.

### Store backends

The platform supports three storage backends. Local development defaults to SQLite:

| Backend        | Use case                      | Configuration                       |
| -------------- | ----------------------------- | ----------------------------------- |
| **Memory**     | Unit testing, ephemeral dev   | In-memory hash maps, no persistence |
| **SQLite**     | Local development (default)   | File at `./data/fastn.db`           |
| **PostgreSQL** | Production and Docker Compose | Connection pooling, SSL, full RLS   |

Switch between backends via environment variables. The Docker Compose setup uses PostgreSQL. Running `fastn dev` outside of Docker defaults to SQLite.

### Troubleshooting

**Containers won't start:** Check Docker has enough memory allocated (at least 4GB recommended for the full stack). The PostgreSQL + Keycloak containers are the heaviest.

**Dashboard shows blank page:** Check the Control Plane is running on port 3001. The dashboard calls the API on startup — if the API isn't ready, the UI shows nothing.

**Keycloak errors:** The realm import happens on first start. If it fails, delete the Keycloak data volume and restart: `docker compose down -v && docker compose up`.

**Database migration fails:** Check the PostgreSQL logs: `docker compose logs postgres`. Common issue: the `pgvector` extension requires the container image to have it pre-installed.

### Package architecture

For reference, here's how the codebase is organized:

| Package             | Purpose                          | Key exports                                            |
| ------------------- | -------------------------------- | ------------------------------------------------------ |
| `@fastn/core`       | Shared types, schemas, utilities | Types, ID generators, error classes, logger, constants |
| `@fastn/builder`    | Workflow visual editor           | AST parser, canvas components, workflow store          |
| `@fastn/runtime`    | Execution engine                 | `executeWorkflow`, Lambda/Cloud Run handlers, tracing  |
| `@fastn/workflow`   | Workflow DSL                     | `workflow()`, `step()`, triggers, `defineConfig()`     |
| `@fastn/connectors` | Third-party integrations         | ConnectorRegistry, built-in connectors                 |
| `@fastn/cli`        | Developer tooling                | `dev`, `run`, `deploy`, `logs`, `destroy` commands     |

### What you've set up

* Full Fastn platform running locally (9 services)
* Keycloak authentication with pre-configured realm
* PostgreSQL with pgvector and all tables/RLS policies
* The Fastn CLI for development workflows
* Understanding of the package architecture
