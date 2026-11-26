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
* Code editing turned on for your organization. It is off by default, and Fastn turns it on if you ask. If your editor has no code column, ask Fastn, or build the workflow from [your AI tool](../../build/building-from-your-ai-agent.md) or with the [Fastn agent](../../build/agent/README.md) instead.

### Open the code editor

1. Go to **Build → Integrations → Workflows** ([Open in Fastn](https://app.fastn.dev/integrations?tab=workflows)).
2. Click **Create workflow**.

**You should see:** the workflow editor, with three panels.

### The three panels

* **Configuration (left):** the workflow's name, slug, execution tier, timeout and retries. Every setting is described in [Configuration panel](../../build/workflows/the-editor.md#configuration-panel).
* **Code (middle):** the `<slug>.js` file, which starts from this template:

  ```javascript
  export default async function(ctx) {
    const { input, headers } = ctx;
    // Your workflow logic here
    return { result: "Hello from workflow!", input };
  }
  ```

  Every workflow exports a default async function that receives `ctx`, the context object.
* **Tool tabs (right):** a new workflow shows **Test**, **Connectors** and **Contract**. More tabs appear once you save it. See [Editor tabs](../../build/workflows/the-tabs.md).

The runtime reference, everything `ctx` and `fastn.*` offer inside the function, is in the code editor's autocomplete and in [Workflow runtime API](../../reference/workflow-runtime.md).

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

A **Live** test is real: changes it makes in connected apps really happen. See [Test a workflow](../../build/workflows/testing.md).

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
4. Pick a mode: **Live**, **Partial Mock** or **Fully Mock**. See [Run a quick test](../../build/workflows/testing.md#run-a-quick-test) for what each one calls.
5. Click the run button (**Run Live**, **Run Partial Mock**, or **Run Fully Mock**).

**You should see:** the output below the run button. Check that the result is what you expect.

### Create the workflow

Once your code works in testing:

1. Fill in **Name**, **Slug**, and **Description** in the Configuration panel.
2. Select the **Execution tier**: **Instant** when the caller waits for the answer, **Standard** for most syncs, **Long** for large imports. See [Execution tiers](../../build/workflows/README.md#execution-tiers).
3. Set the **Execution timeout**.
4. Toggle **Retry policy** if you want automatic retries on failure.
5. Click **Create Workflow** (bottom of the Configuration panel).

**You should see:** the workflow in the Workflows list with status **Unpublished**. Until you publish it, every call returns `WORKFLOW_NOT_PUBLISHED`. Publish it from the **Publish & Deploy** section with **Publish snapshot**, then deploy it to an environment; see [Test and release](../../build/workflows/lifecycle.md).

### Edit an existing workflow

1. Go to **Build → Integrations → Workflows** ([Open in Fastn](https://app.fastn.dev/integrations?tab=workflows)).
2. Click the workflow's row (or **Edit** in its `⋯` menu). The code editor opens with the existing code.
3. Make your changes and test them. Draft edits auto-save (**✓ Draft saved**); **Save workflow** saves explicitly.
4. Publish again to make the change runnable. Publishing changes what triggers routed to **test (latest published)** run straight away. See [Test and release](../../build/workflows/lifecycle.md).

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
