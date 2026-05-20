---
description: >-
  Deploy TypeScript workflows to AWS Lambda or GCP Cloud Run using the Fastn CLI
  and Pulumi-managed infrastructure.
---

# Deploying to Lamba/Cloud Run

**Prerequisites:** [Writing a Workflow (TypeScript DSL)](writing-a-workflow-via-typescript-dsl.md). An AWS or GCP account with appropriate permissions.

Locally, workflows run on a Fastify server with hot reload. For production, Fastn supports two deployment targets i.e. AWS Lambda and GCP Cloud Run.

### Deployment targets

| Target            | Handler                   | Infrastructure                  | Best for                                  |
| ----------------- | ------------------------- | ------------------------------- | ----------------------------------------- |
| **AWS Lambda**    | `createLambdaHandler()`   | Pulumi-managed Lambda functions | Event-driven, short-running workflows     |
| **GCP Cloud Run** | `createCloudRunHandler()` | Docker-based Cloud Run services | Longer-running workflows, container-based |
| **Local**         | Fastify server            | `tsx --watch` with hot reload   | Development and testing                   |

### Preparing your workflow for deployment

Wrap your workflow in the appropriate handler for your target:

#### AWS Lambda

```typescript
import { createLambdaHandler } from '@fastn/runtime';
import syncOrders from './workflows/sync-orders';

export const handler = createLambdaHandler(syncOrders);
```

#### GCP Cloud Run

```typescript
import { createCloudRunHandler } from '@fastn/runtime';
import syncOrders from './workflows/sync-orders';

createCloudRunHandler(syncOrders);
```

The handler wraps your workflow with the execution runtime — step ordering (topological sort), retry logic, context building, input/output propagation, and OpenTelemetry tracing.

### Deploying with the CLI

#### To AWS Lambda

```bash
# Configure AWS credentials
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_REGION=us-east-1

# Deploy
fastn deploy --target lambda --workflow sync_orders
```

Pulumi provisions:

* A Lambda function with your workflow code
* An API Gateway endpoint for webhook/API triggers
* IAM roles with least-privilege permissions
* CloudWatch log groups for monitoring

#### To GCP Cloud Run

```bash
# Configure GCP credentials
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
export GCP_PROJECT_ID=your-project

# Deploy
fastn deploy --target cloudrun --workflow sync_orders
```

Pulumi provisions:

* A Cloud Run service with your workflow as a Docker container
* A URL endpoint for triggering the workflow
* IAM bindings for service invocation

> **Screenshot:** Terminal output showing a successful `fastn deploy` command with the deployed endpoint URL.

### Managing deployments

```bash
# View logs for a deployed workflow
fastn logs sync_orders

# Destroy deployed infrastructure
fastn destroy sync_orders
```

The `destroy` command tears down all Pulumi-managed resources for that workflow — Lambda functions, API Gateways, Cloud Run services, and associated IAM roles.

### Execution runtime

Regardless of deployment target, the runtime provides:

**Step ordering** — Steps execute in topological order. Dependencies between steps are resolved automatically based on `ctx.steps` references.

**Retry with backoff** — Failed steps retry with configurable backoff strategy. Set retry count and backoff per step or per workflow.

**Distributed tracing** — OpenTelemetry integration traces execution across steps. Each step creates a span with connector, tenant, and execution context as attributes.

**Status tracking** — Executions report status in real-time: `pending`, `running`, `completed`, `failed`, `cancelled`, `timed_out`.

### Environment-specific configuration

Use the 5-level configuration hierarchy to manage differences between environments:

```typescript
// In your workflow
const apiUrl = ctx.config.externalApiUrl;
// Resolves to different values based on environment:
// dev: http://localhost:3005/mock
// staging: https://staging-api.myapp.com
// production: https://api.myapp.com
```

Set environment-specific values in **Settings → Configurations** with the appropriate scope.

### What you've done

* Wrapped a workflow in a Lambda or Cloud Run handler
* Deployed to AWS or GCP using the Fastn CLI
* Understood the Pulumi-managed infrastructure that gets provisioned
* Learned how to view logs and tear down deployments
* Configured environment-specific settings
