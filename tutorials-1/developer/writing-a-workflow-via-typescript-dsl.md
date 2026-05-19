---
description: >-
  Write workflows as async functions using the Fastn code editor model — ctx
  object, execution tiers, testing, and deployment patterns.
---

# Writing a Workflow via TypeScript DSL

**Prerequisites:** [Local Dev Environment Setup](local-dev-environment-setup.md). TypeScript/JavaScript experience.

Fastn workflows are code-first. Every workflow is a JavaScript/TypeScript file that exports a default async function receiving a context object. No visual canvas, no drag-and-drop you write the logic directly.

### The workflow function

Every workflow has the same structure:

```typescript
export default async function(ctx) {
  const { input, headers } = ctx;
  
  // Your workflow logic here
  
  return { result: "done" };
}
```

The function receives `ctx` and must return a result object. Whatever you return is the workflow's output visible in the execution log and returned to the caller for Instant-tier workflows.

### The ctx object

| Property  | Type   | Description                                                                                                |
| --------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| `input`   | object | Incoming data — request body from a webhook trigger, event payload from an app event, or scheduler context |
| `headers` | object | HTTP headers from the incoming request (if triggered by a webhook)                                         |

### Examples

#### Process incoming data

```typescript
export default async function(ctx) {
  const { input } = ctx;
  
  const contacts = input.contacts || [];
  const processed = contacts.map(c => ({
    email: c.email?.toLowerCase(),
    name: `${c.firstName} ${c.lastName}`.trim(),
    source: "hubspot",
    syncedAt: new Date().toISOString()
  }));
  
  return {
    result: "success",
    count: processed.length,
    contacts: processed
  };
}
```

#### Conditional logic

```typescript
export default async function(ctx) {
  const { input } = ctx;
  const order = input.order;
  
  if (!order) {
    return { error: "No order data provided" };
  }
  
  if (order.total > 500) {
    return {
      action: "review",
      reason: `Order total $${order.total} exceeds threshold`,
      order
    };
  }
  
  return {
    action: "process",
    order
  };
}
```

#### Fetch external data

```typescript
export default async function(ctx) {
  const { input } = ctx;
  
  // Call an external API
  const response = await fetch(`https://api.example.com/orders/${input.orderId}`, {
    headers: { "Authorization": `Bearer ${input.apiToken}` }
  });
  
  if (!response.ok) {
    return { error: `API returned ${response.status}` };
  }
  
  const order = await response.json();
  
  return {
    result: "fetched",
    order,
    fetchedAt: new Date().toISOString()
  };
}
```

#### Batch processing

```typescript
export default async function(ctx) {
  const { input } = ctx;
  const items = input.items || [];
  
  const results = [];
  const errors = [];
  
  for (const item of items) {
    try {
      // Process each item
      const result = await processItem(item);
      results.push(result);
    } catch (err) {
      errors.push({ item: item.id, error: err.message });
    }
  }
  
  return {
    processed: results.length,
    failed: errors.length,
    errors: errors.length > 0 ? errors : undefined
  };
}

async function processItem(item) {
  // Your item processing logic
  return { id: item.id, status: "processed" };
}
```

### Workflow configuration

When creating a workflow in the editor, the Configuration panel has:

| Setting               | Options                      | Description                    |
| --------------------- | ---------------------------- | ------------------------------ |
| **Name**              | Free text                    | Workflow identifier (required) |
| **Description**       | Free text                    | What the workflow does         |
| **Execution Tier**    | Instant, Standard, Long      | Determines execution behavior  |
| **Execution Timeout** | 1s–2min slider (for Instant) | Max execution time             |
| **Retry Policy**      | Toggle on/off                | Automatic retry on failure     |

#### Execution tiers

| Tier         | Behavior                                                            | Use when                                         |
| ------------ | ------------------------------------------------------------------- | ------------------------------------------------ |
| **Instant**  | Synchronous — caller waits for the result. Returns inline. Max 60s. | API responses, quick lookups, simple transforms  |
| **Standard** | Asynchronous — returns immediately, executes in background.         | Data syncs, multi-step processes, most workflows |
| **Long**     | Extended async — for large data volumes.                            | Batch imports, backfills, large reports          |

### Testing in the editor

The right panel has a **Test** tab:

1. Enter sample JSON in **CTX.INPUT**:

```json
{
  "contacts": [
    { "email": "jane@acme.com", "firstName": "Jane", "lastName": "Doe" }
  ]
}
```

2. Optionally add headers in **CTX.HEADERS**.
3. Click **Run** — executes without saving.
4. Review the output below.
5. Iterate until the result is correct.
6. Click **Create Workflow** to save and deploy.

### Testing locally

For local development with the Fastn CLI:

```bash
# Start the dev server with hot reload
fastn dev

# Run a specific workflow with input
fastn run my-workflow --input '{"orderId": "12345"}'
```

The dev server uses `tsx --watch` — every code change triggers an automatic restart.

### Connecting to triggers

Workflows don't contain their own triggers in Fastn. Triggers are managed separately under **Integrations → Triggers**. After creating your workflow:

1. Go to **Integrations → Triggers**
2. Click **Add Trigger**
3. Select type (Webhook, Scheduler, or App Event)
4. Route the trigger to your workflow

A single trigger can route to multiple workflows, and a single workflow can be targeted by multiple triggers.

### Monitoring executions

After your workflow runs, check results under **Activity → Executions**:

| Column           | What to check                                               |
| ---------------- | ----------------------------------------------------------- |
| **Status**       | Completed (green) or Failed (red)                           |
| **Duration**     | How long it took                                            |
| **Tier**         | Which execution tier was used                               |
| **Triggered By** | What started it (webhook, scheduler, agent-service, manual) |

Click an execution row for detailed output including your return object.

### What you've learned

* Fastn workflows are `export default async function(ctx)` — code-first, no visual canvas
* The ctx object provides `input` and `headers`
* Execution tiers (Instant/Standard/Long) control sync vs async behavior
* Testing happens in the editor's Test panel before creating
* Triggers are managed separately and routed to workflows
* Executions are monitored under Activity → Executions
