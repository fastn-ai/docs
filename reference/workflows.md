---
description: >-
  Code editor interface, ctx object, execution tiers, retry policy, workflow
  statuses, versioning, and trigger integration.
---

# Workflows

### Workflow editor

The Fastn workflow editor is **code-first** which consists of three panels:

1. **Configuration:**

* Name (required)
* Description
* Execution Tier (Instant / Standard / Long)
* Execution Timeout (slider: 1s–2min for Instant)
* Retry Policy (toggle on/off)

2. **Code editor** (`workflow.js`):

```javascript
export default async function(ctx) {
  const { input, headers } = ctx;
  // Your workflow logic here
  return { result: "Hello from workflow!", input };
}
```

3. **Test panel:**

* **Test** tab: CTX.INPUT (JSON), CTX.HEADERS (JSON), Run button
* **Docs** tab: Reference documentation

{% hint style="info" %}
"Hit Run to execute without saving" — test before committing.
{% endhint %}

### ctx object

Every workflow receives a context object:

```javascript
const { input, headers } = ctx;
```

| Property  | Type   | Description                                                                    |
| --------- | ------ | ------------------------------------------------------------------------------ |
| `input`   | object | Incoming data — request body from webhook, event payload, or scheduler context |
| `headers` | object | HTTP headers from the incoming request (if webhook-triggered)                  |

### Execution tiers

| Tier         | Behavior                                                    | Max timeout  | Use when                                         |
| ------------ | ----------------------------------------------------------- | ------------ | ------------------------------------------------ |
| **Instant**  | Synchronous — caller waits for result. Returns inline.      | 60 seconds   | API endpoints needing responses, quick lookups   |
| **Standard** | Asynchronous — returns immediately, executes in background. | Configurable | Data syncs, multi-step processes, most workflows |
| **Long**     | Extended async — for large data volumes.                    | Extended     | Batch imports, full backfills, large reports     |

The Workflows table has filter tabs: **All | Instant | Standard | Long**.

### Execution timeout

Configurable per workflow via a slider in the Configuration panel. Range depends on tier:

* Instant: 1s–2min
* Standard / Long: configurable with higher limits

### Retry policy

Toggle on/off in the Configuration panel. When enabled, failed executions retry automatically with backoff.

### Workflow statuses

| Status       | Badge           | Description                        |
| ------------ | --------------- | ---------------------------------- |
| **active**   | Green checkmark | Deployed and can be triggered      |
| **inactive** | —               | Exists but not processing triggers |

### Workflow versioning

Workflows track versions (v1, v2, etc.). The Workflows table shows a **VERSION** column. Each edit creates a new version.

### Workflows table

Columns in **Integrations → Workflows**:

| Column      | Description                        |
| ----------- | ---------------------------------- |
| **NAME**    | Workflow name + slug + description |
| **STATUS**  | active (green) or inactive         |
| **VERSION** | Current version (v1, v2, etc.)     |
| **UPDATED** | Last update date                   |
| **ACTIONS** | Run, Delete buttons                |

Filter tabs: **All | Instant | Standard | Long**

Buttons: **Create Workflow** (code editor), **Build with AI** (Standalone Workflow Builder)

### Execution log

Executions are logged under **Activity → Executions**:

| Column           | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| **TIME**         | Relative timestamp ("17h ago", "1d ago")                    |
| **WORKFLOW**     | Workflow name                                               |
| **TIER**         | Execution tier badge (INSTANT, STANDARD, LONG)              |
| **VERSION**      | Workflow version at time of execution                       |
| **STATUS**       | Running, Completed, Failed, Timeout                         |
| **DURATION**     | Execution time (79ms, 2.1s)                                 |
| **TRIGGERED BY** | What started it (agent-service, webhook, scheduler, manual) |

Filter tabs: **All | Running | Completed | Failed | Timeout**

Time range dropdown, workflow filter dropdown, Refresh button.

### Triggers (separate section)

Triggers are managed separately from workflows under **Integrations → Triggers**. Three types:

| Type          | Description                      | Configuration                                        |
| ------------- | -------------------------------- | ---------------------------------------------------- |
| **Webhook**   | HTTP POST from external services | Routes with workflow targets, JSON filters, headers  |
| **Scheduler** | Time-based execution             | Presets: Interval, Daily, Weekly, Monthly, Custom    |
| **App Event** | Events from connectors           | Select connector, connection, and event to subscribe |

A single webhook trigger can route to multiple workflows via different routes.

### Creating a workflow

#### Via code editor

1. **Integrations → Workflows → Create Workflow**
2. Write code, configure settings, test with sample data
3. Click **Create Workflow**

#### Via AI

1. **Integrations → Workflows → Build with AI**
2. Describe what you need in the Standalone Workflow Builder
3. Review and accept the generated code
