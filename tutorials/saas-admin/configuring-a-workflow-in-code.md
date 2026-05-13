---
description: >-
  Write workflows in the code editor using export default async function(ctx),
  configure execution tiers, and test with sample input.
---

# Configuring a Workflow in Code

**Prerequisites:** [Your First Integration](https://claude.ai/getting-started/your-first-integration.md). Basic JavaScript familiarity.

### Opening the code editor

1. Go to **Integrations → Workflows**.
2. Click **Create Workflow**.
3. The workflow editor opens with three panels.

> **Screenshot needed:** Full workflow editor showing all three panels — Configuration (left), Code (center), Test (right).

### The three panels

The code editor consists of three panels which are as follows:

#### 1. Configuration

| Field                 | What it does                                                                       |
| --------------------- | ---------------------------------------------------------------------------------- |
| **Name**              | Workflow identifier (required). Example: "sync-contacts"                           |
| **Description**       | What the workflow does. Shown in the workflows table.                              |
| **Execution Tier**    | **Instant** (sync, max 60s), **Standard** (async, default), or **Long** (extended) |
| **Execution Timeout** | Max time before timeout. Slider: 1s–2min range for Instant tier.                   |
| **Retry Policy**      | Toggle on/off. When on, failed executions retry automatically.                     |

#### 2. Code editor

The editor shows `workflow.js` with a default template:

```javascript
export default async function(ctx) {
  const { input, headers } = ctx;
  // Your workflow logic here
  return { result: "Hello from workflow!", input };
}
```

Every workflow exports a default async function that receives `ctx` — the context object.

#### 3. Test panel

Two tabs:

* **Test** — run the workflow with sample input
* **Docs** — reference documentation

The Test tab has:

* **CTX.INPUT** — JSON input your workflow receives
* **CTX.HEADERS** — optional HTTP headers
* **Run** button — executes the workflow without saving

{% hint style="info" %}
**Note:** "Hit Run to execute without saving" — iterate on your code before committing.
{% endhint %}

### The ctx object

Your workflow receives a context object with:

```javascript
const { input, headers } = ctx;
```

| Property  | What it contains                                                                     |
| --------- | ------------------------------------------------------------------------------------ |
| `input`   | The incoming data — request body from a webhook, event payload, or scheduler context |
| `headers` | HTTP headers from the incoming request (if triggered by webhook)                     |

### Writing a workflow

#### Example: Process incoming contacts

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

#### Example: Conditional logic

```javascript
export default async function(ctx) {
  const { input } = ctx;
  const order = input.order;
  
  if (!order) {
    return { error: "No order data provided" };
  }
  
  if (order.total > 500) {
    // High-value order — needs review
    return {
      action: "review",
      reason: `Order total $${order.total} exceeds threshold`,
      order
    };
  }
  
  // Standard order — process normally
  return {
    action: "process",
    order
  };
}
```

### Testing

1. Click the **Test** tab in the right panel.
2. Enter sample JSON in **CTX.INPUT**:

```json
{
  "contacts": [
    { "email": "Jane@Acme.com", "firstName": "Jane", "lastName": "Doe" },
    { "email": "john@widget.co", "firstName": "John", "lastName": "Smith" }
  ]
}
```

3. Optionally add headers in **CTX.HEADERS**.
4. Click **Run**.
5. The output appears below — check the result matches your expectations.
6. Toggle between **Test** (sample data) and **Real** mode if available.

> **📷 Screenshot needed:** Test panel with sample input JSON and the output result after running.

### Choosing an execution tier

| Tier         | Behavior                                                                          | Use when                                                             |
| ------------ | --------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Instant**  | Synchronous — caller waits for the result. Max 60 seconds. Returns result inline. | API endpoints that need a response, quick lookups, simple transforms |
| **Standard** | Asynchronous — returns immediately, executes in background.                       | Data syncs, multi-step processes, most workflows                     |
| **Long**     | Extended async — for large data volumes and long-running processes.               | Batch imports, full data backfills, large report generation          |

The Workflows table has filter tabs for **All | Instant | Standard | Long** so you can filter by tier.

### Creating the workflow

Once your code works in testing:

1. Fill in **Name** and **Description** in the Configuration panel.
2. Select the appropriate **Execution Tier**.
3. Set **Execution Timeout** (default: 1 minute for Instant).
4. Toggle **Retry Policy** if you want automatic retries on failure.
5. Click **Create Workflow** (bottom of the Configuration panel).

The workflow appears in the Workflows table with status **active**.

> **📷 Screenshot needed:** Workflows table showing the newly created workflow with active status.

### Editing an existing workflow

1. Go to **Integrations → Workflows**.
2. Click on the workflow name in the table.
3. The code editor opens with the existing code.
4. Make your changes, test them, then save.

### What you've learned

* The three-panel code editor layout (Configuration, Code, Test)
* The `ctx` object structure (`input`, `headers`)
* How to write workflow logic in JavaScript
* How to test with sample data before creating
* How to choose the right execution tier
* How to create and edit workflows
