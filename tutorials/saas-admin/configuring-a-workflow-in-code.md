---
description: >-
  Write workflows in the code editor using export default async function(ctx),
  configure execution tiers, and test with sample input.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Write a workflow in code

Write a workflow by hand in the code editor, test it with sample input, and create it.

### Before you start

* The [Quickstart: your first integration](../../getting-started/quickstart.md).
* Basic JavaScript.
* Code editing turned on for your organization. It is a per-organization entitlement, off by default and turned on by fastn. If your editor has no code column, ask fastn to turn it on, or build the workflow with the [fastn agent](../../build/agent/README.md) or [your AI tool](../../build/building-from-your-ai-agent.md) instead.

### Open the code editor

1. Go to **Integrations** and open the **Workflows** tab.
2. Click **Create workflow**.

**You should see:** the workflow editor, with three panels.

### The three panels

The editor has these panels:

#### 1. Configuration

| Field                 | What it does                                                                       |
| --------------------- | ---------------------------------------------------------------------------------- |
| **Name**              | Required. Placeholder: "e.g. Sync Contacts".                                        |
| **Slug**              | Required on create. Unique identifier, used in the API path. Placeholder: "sync-contacts". *Cannot be changed after creation.* |
| **Description**       | What the workflow does. Shown in the workflows table.                              |
| **Execution tier**    | **Instant** (the default; synchronous, max 25s, or 2 minutes with the "Increase Instant timeout" entitlement), **Standard** (async, up to 15 minutes), or **Long** (async, up to 36 hours) |
| **Execution timeout** | Max time before the run is cut off. The slider is constrained to the tier: 1s to 25s for Instant (up to 2 min with the entitlement), 5s to 15min for Standard, 30s to 36h for Long. |
| **Retry policy**      | Toggle on/off. When on, transient failures retry automatically, up to **Max attempts** (2-10, default 3). |

#### 2. Code editor

The editor shows `<slug>.js` with a default template:

```javascript
export default async function(ctx) {
  const { input, headers } = ctx;
  // Your workflow logic here
  return { result: "Hello from workflow!", input };
}
```

Every workflow exports a default async function that receives `ctx`, the context object.

#### 3. Tool tabs

On a new workflow there are three tabs:

* **Test** - run the workflow with sample input
* **Connectors** - the connectors the workflow calls
* **Contract** - the input and output contract

Once the workflow is saved, more tabs appear (Diagram, Test cases, Executions, Sync reports, API, and others). Diagram has a **Docs** view, but it documents this workflow, not the runtime; the runtime reference is in the code editor's autocomplete and in [Workflow runtime API](../../reference/workflow-runtime.md).

The Test tab has:

* **ctx.input** - JSON input your workflow receives (**Use contract** fills it from the input contract)
* **ctx.headers** - optional HTTP headers
* A mode select: **Live**, **Partial Mock**, or **Fully Mock**
* A run button that follows the mode: **Run Live**, **Run Partial Mock**, or **Run Fully Mock**. It executes the workflow without saving.

### The ctx object

Your workflow receives a context object with:

```javascript
const { input, headers } = ctx;
```

| Property  | What it contains                                                                     |
| --------- | ------------------------------------------------------------------------------------ |
| `input`   | The incoming data: the request body from a webhook, an event payload, or scheduler context |
| `headers` | HTTP headers from the incoming request (if triggered by webhook)                     |

### Write a workflow

#### Example: process incoming contacts

```javascript
export default async function(ctx) {
  const { input } = ctx;
  
  const contacts = input.contacts || [];
  const processed = [];
  
  for (const contact of contacts) {
    // Transform the contact data
    processed.push({
      email: contact.email?.toLowerCase(),
      name: `${contact.firstName} ${contact.lastName}`.trim(),
      source: "hubspot",
      syncedAt: new Date().toISOString()
    });
  }
  
  return {
    result: "success",
    count: processed.length,
    contacts: processed
  };
}
```

#### Example: conditional logic

```javascript
export default async function(ctx) {
  const { input } = ctx;
  const order = input.order;
  
  if (!order) {
    return { error: "No order data provided" };
  }
  
  if (order.total > 500) {
    // High-value order - needs review
    return {
      action: "review",
      reason: `Order total $${order.total} exceeds threshold`,
      order
    };
  }
  
  // Standard order - process normally
  return {
    action: "process",
    order
  };
}
```

### Test the workflow

{% hint style="warning" %}
Test runs in **Live** mode are real: connectors are called and side effects happen. Use **Fully Mock** to try the code without touching any app.
{% endhint %}

1. Click the **Test** tab in the right panel.
2. Enter sample JSON in **ctx.input**:

```json
{
  "contacts": [
    { "email": "Jane@Acme.com", "firstName": "Jane", "lastName": "Doe" },
    { "email": "john@widget.co", "firstName": "John", "lastName": "Smith" }
  ]
}
```

3. Optionally add headers in **ctx.headers**.
4. Pick a mode: **Live** (real calls to connected apps), **Partial Mock** (live where the connector has an active connection, a stored mock stub where it does not), or **Fully Mock** (stubs only).
5. Click the run button (**Run Live**, **Run Partial Mock**, or **Run Fully Mock**).

**You should see:** the output below the run button. Check that the result is what you expect.

### Choose an execution tier

| Tier         | Behavior                                                                          | Use when                                                             |
| ------------ | --------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Instant**  | Synchronous: the caller waits for the result. Max 25 seconds (2 minutes with the "Increase Instant timeout" entitlement). Returns result inline. | API endpoints that need a response, quick lookups, simple transforms |
| **Standard** | Asynchronous: returns `202` immediately, executes in background. Up to 15 minutes. | Data syncs, multi-step processes, most workflows                     |
| **Long**     | Asynchronous, for large data volumes and long-running processes. Up to 36 hours.   | Batch imports, full data backfills, large report generation          |

The Workflows list has filter pills for **All | Instant | Standard | Long** so you can filter by tier.

### Create the workflow

Once your code works in testing:

1. Fill in **Name**, **Slug**, and **Description** in the Configuration panel.
2. Select the appropriate **Execution tier**.
3. Set **Execution timeout** (for Instant, the slider tops out at 25s unless your organization has the extended Instant timeout).
4. Toggle **Retry policy** if you want automatic retries on failure.
5. Click **Create Workflow** (bottom of the Configuration panel).

**You should see:** the workflow in the Workflows list with status **Unpublished**. Until you publish it, every call returns `WORKFLOW_NOT_PUBLISHED`. Publish it from the **Publish & Deploy** section with **Publish snapshot**, then deploy it to an environment; see [Test and release](../../build/workflows/lifecycle.md).

### Edit an existing workflow

1. Go to **Integrations** and open the **Workflows** tab.
2. Click the workflow's row (or **Edit** in its `⋯` menu). The code editor opens with the existing code.
3. Make your changes and test them. Draft edits auto-save (**✓ Draft saved**); **Save workflow** saves explicitly.
4. Publish again to make the change runnable. Publishing immediately changes what triggers routed to **test (latest published)** run.

### What you've learned

* The three-panel code editor layout (Configuration, Code, tool tabs)
* The `ctx` object structure (`input`, `headers`)
* How to write workflow logic in JavaScript
* How to test with sample data before creating
* How to choose the right execution tier
* How to create and edit workflows

### Next steps

* Publish and deploy the workflow: [Test and release](../../build/workflows/lifecycle.md).
* Start it on events: [Set up triggers](setting-up-triggers.md).
* Call connectors and use state from code: [Workflow runtime API](../../reference/workflow-runtime.md).
