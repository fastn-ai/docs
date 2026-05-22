---
description: >-
  AI builder and code editor interface, ctx object, execution tiers, retry
  policy, workflow statuses, versioning, and trigger integration.
---

# Workflows

Workflows are the automation units in Fastn. Each workflow is a TypeScript function that receives a context object, executes logic using the Fastn runtime API, and returns a result. The primary way to create workflows is through the AI agent you describe what you need and the agent builds the workflow end-to-end. The code editor exists for inspection and manual fine-tuning.

### AI Workflow Builder

The AI agent is the primary path for creating and modifying workflows. It handles the full cycle: analyzing your request, setting up connectors, configuring authentication, mapping fields, generating test cases, and producing the workflow code.

#### Entry points

| Location                     | How to access                                            | What it does                                                                                             |
| ---------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Home page**                | AI assistant prompt on the Home page                     | Routes to the appropriate agent based on your request                                                    |
| **Integrations → Workflows** | Click **✦ Build with AI** in the sub-nav top-right       | Opens the Standalone Workflow Builder                                                                    |
| **Integrations page**        | Click **✦ Build with AI** on the Integrations page       | Opens the full integration builder ("Describe what you need and the AI agents will build it end-to-end") |
| **Setup Assistant**          | Home → Step 3: Workflows (during onboarding)             | Builds workflows as part of the initial setup pipeline                                                   |
| **Widget**                   | End user clicks a template card or uses the AI assistant | Launches an Integration Agent session inside the widget                                                  |

#### Builder variants

| Variant                   | Behavior                                                                                                                                                        |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Standalone Builder**    | Builds and validates a single workflow directly. Accessed via ✦ Build with AI on the Workflows page.                                                            |
| **Workflow Orchestrator** | Coordinates multiple agents — a Planner, Builder, and Test Case agent — for complex multi-step builds. Fastn routes to this automatically for complex requests. |

#### What the agent does

When you describe a workflow, the agent works through these stages:

| Stage                  | Description                                                                                                                                                                                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Analyze**         | Breaks down which systems are involved, what data needs to move, what transformations are needed, and what trigger to use.                                                                                                                                 |
| **2. Connector setup** | Checks if connectors exist for the systems you mentioned. Creates or configures them if needed.                                                                                                                                                            |
| **3. Inline auth**     | Handles authentication inside the chat. API Key auth shows input fields directly. OAuth shows a form with Client ID, Client Secret, pre-filled scopes, and a portal link.                                                                                  |
| **4. Field mapping**   | Generates field mappings between source and target systems. Shows a "WE'VE SET THIS UP FOR YOU" banner with mapping rows (source/target dropdowns, Change buttons, fixed value badges). Includes Record Matching Strategy, + Add Mapping, and Add Filters. |
| **5. Test cases**      | Creates test cases to validate the workflow. Shows count and live status (e.g., "Test Cases — 22, 2 Live") with MOCK/LIVE badges, scenario descriptions, Feedback fields, and Approve buttons.                                                             |
| **6. Code generation** | Produces the workflow code (`export default async function(ctx) { ... }`) using the runtime API. The code appears in the editor with the `Edited via agent` metadata.                                                                                      |

#### Iterating

Send follow-up messages to refine what the agent built:

* "Add error handling for when the API is down"
* "Filter out records without email addresses"
* "Change the schedule to every hour"
* "Add a Slack notification on failure"

The agent updates the workflow code, field mappings, and test cases. The **TASKS** panel in the left sidebar tracks completed and pending work.

#### Sessions and activity

The Standalone Builder has:

| Panel                        | Content                                                                                         |
| ---------------------------- | ----------------------------------------------------------------------------------------------- |
| **Left sidebar — SESSIONS**  | History of builder sessions. Each session preserves the full conversation.                      |
| **Right sidebar — ACTIVITY** | Real-time log of what the agent is doing (creating connectors, generating code, running tests). |

***

### Runtime API

Every workflow runs as an `export default async function(ctx)` and has access to the following:

#### ctx.input

The incoming data payload. Contents depend on what triggered the workflow:

* **Webhook trigger** — The HTTP request body
* **Scheduler trigger** — Scheduler context (schedule metadata)
* **App Event trigger** — The event payload from the connector
* **Manual trigger** — The JSON you provide in the Test tab

```javascript
const events = ctx.input;
const { propertyName, propertyValue, objectId } = events[0];
```

#### ctx.headers

HTTP headers from the incoming request (webhook-triggered workflows only). Auth headers are stripped for security — you won't see `Authorization` or `x-fastn-access-key` here.

```javascript
const contentType = ctx.headers['content-type'];
```

#### fastn.connector

Execute actions on any connected third-party app by connector slug. This is how workflows read from and write to external systems.

```javascript
// Initialize with connector references
const fastn = new Fastn({
  connectors: {
    hubspotCrm: { orgId: "managed" },
    gamma: { orgId: "custom" }
  }
});

// Execute a connector action
const profile = await fastn.connector.gmail.getProfile({ emailAddress: "me" });
const deal = await fastn.connector.hubspotCrm.getDeal({ dealId: objectId });
const result = await fastn.connector.gamma.createGeneration({ ... });
```

The connector slug matches the connector name in **Integrations → Connectors** (lowercase, hyphenated). Each connector exposes its own set of actions — check the connector's documentation or the Docs tab in the workflow editor for available methods.

#### fastn.db

Tenant-scoped SQL database access. Each tenant gets an isolated database context. Supports CREATE TABLE, SELECT, INSERT, UPDATE, DELETE with parameterized queries ($1, $2 placeholders).

```javascript
// Create a table (if needed)
await fastn.db.query(`
  CREATE TABLE IF NOT EXISTS sync_log (
    id SERIAL PRIMARY KEY,
    source_id TEXT,
    synced_at TIMESTAMP DEFAULT NOW()
  )
`);

// Insert a record
await fastn.db.query(
  `INSERT INTO sync_log (source_id) VALUES ($1)`,
  [record.id]
);

// Query records
const result = await fastn.db.query(
  `SELECT * FROM sync_log WHERE source_id = $1`,
  [record.id]
);
```

#### fastn.state

Durable key-value store for persisting data across workflow runs. Two scopes:

| Scope             | Behavior                                                                                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ORG** (default) | Shared across all runs of this workflow within the organization. Use for deduplication, tracking synced record IDs, or caching values between runs. |
| **INVOCATION**    | Scoped to a single run. Cleared after the workflow completes. Use for temporary state within a long-running workflow.                               |

Optional TTL (time-to-live) for automatic expiry.

```javascript
// Check if a record was already processed (deduplication)
const existing = await fastn.state.get(`deal:${dealId}`);
if (existing) {
  return { success: true, skipped: true, reason: "already_processed" };
}

// Mark as processed
await fastn.state.set(`deal:${dealId}`, { processedAt: new Date().toISOString() });
```

#### fastn.secrets

Read encrypted secrets stored in **Settings → Secrets**. Use for third-party API tokens, database credentials, or any sensitive values your workflow needs at runtime.

```javascript
const apiToken = await fastn.secrets.get("SHOPIFY_API_TOKEN");
```

Secrets are never logged, never included in execution output, and never exposed in error messages.

### Workflow Editor

Open any workflow from **Integrations → Workflows** to launch the three-panel editor.

#### Left panel — Configuration

| Field                 | Description                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| **Name**              | Human-readable workflow name (required).                                                          |
| **Slug**              | URL-safe identifier, auto-generated from the name (e.g., `hubspot-discovery-deal-to-gamma-deck`). |
| **Description**       | What the workflow does. Written by the AI agent or manually.                                      |
| **Execution Tier**    | Dropdown: Instant, Standard, or Long (see Execution Tiers below).                                 |
| **Execution Timeout** | Slider within the tier's allowed range.                                                           |
| **Status**            | Toggle: Enabled / Disabled. Disabled workflows won't process triggers.                            |
| **Retry Policy**      | Toggle ON to enable automatic retries (see Retry Policy below).                                   |

At the bottom of the left panel:

| Button                    | Action                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **Publish snapshot**      | Creates a versioned snapshot (v1, v2, etc.) of the current workflow code and configuration. |
| **Deploy to environment** | Sends the published version to a target environment so it starts handling real events.      |

Top navigation:

| Button            | Action                                                       |
| ----------------- | ------------------------------------------------------------ |
| **Discard**       | Abandons unsaved changes and returns to the workflow list.   |
| **Save Workflow** | Saves the current draft without publishing.                  |
| **Publish**       | Creates a new version snapshot (same as "Publish snapshot"). |

#### Center panel — Code editor

Displays the workflow code as a `.js` file (e.g., `hubspot-discovery-deal-to-gamma-deck.js`). The header shows `JavaScript · export default async function(ctx)`.

The editor footer displays metadata:

```
Latest: v2 — Edited via agent: 434 bytes
```

* **Version** — The current published version number.
* **Edited via agent** — Indicates the code was generated or last modified by the AI agent. Shows `Edited manually` if you changed it in the code editor.
* **Byte count** — Size of the workflow code.

#### Right panel — Five tabs

**▶ Test**

Run the workflow with sample data without saving or publishing.

| Field           | Description                                    |
| --------------- | ---------------------------------------------- |
| **CTX.INPUT**   | JSON payload simulating the incoming data.     |
| **CTX.HEADERS** | JSON object simulating HTTP headers.           |
| **Run**         | Executes the workflow with the provided input. |

The banner reads: "Hit Run to execute without saving" — this lets you iterate quickly.

**📄 Docs**

Three sub-tabs for understanding the workflow:

**Flow** — A visual flowchart rendering the entire workflow as a node graph. Each step appears as a connected node with labeled types:

| Node type | Represents                                     |
| --------- | ---------------------------------------------- |
| TRIGGER   | The event or schedule that starts the workflow |
| PROCESS   | A data transformation or computation step      |
| DECISION  | A conditional branch (if/else logic)           |
| READ      | Reading data from an external system           |
| WRITE     | Writing data to an external system             |
| DONE      | The workflow's end point                       |

Decision branches show both paths (e.g., "yes" → continue, "no" → skip). Skip and error paths are visible in the graph.

**Sequence** — The same logic as a step-by-step sequential timeline showing execution order.

**Docs** — Auto-generated reference documentation for the workflow.

**✏️ Test Cases**

Test cases generated by the AI agent during workflow creation. Each test case has:

| Element      | Description                                    |
| ------------ | ---------------------------------------------- |
| **Name**     | Descriptive scenario name                      |
| **Badge**    | MOCK (simulated data) or LIVE (hits real APIs) |
| **Scenario** | Detailed description of what's being tested    |
| **Feedback** | Field to flag issues with the test case        |
| **Approve**  | Green button to approve the test case          |

Test cases are grouped by scenario type. The header shows total count and live count (e.g., "Test Cases — 22, 2 Live").

**⬛ Executions**

Run history for this specific workflow. Columns:

| Column       | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| TIME         | Relative timestamp ("17h ago", "1d ago")                    |
| TIER         | Execution tier badge (INSTANT, STANDARD, LONG)              |
| VERSION      | Workflow version at time of execution                       |
| STATUS       | Running, Completed, Failed, Timeout                         |
| DURATION     | Execution time (79ms, 2.1s)                                 |
| TRIGGERED BY | What started it (agent-service, webhook, scheduler, manual) |

**🔗 API**

Shows how to call this workflow programmatically. Includes the endpoint URL and required headers:

```
x-fastn-access-key: wak_<your-key>
x-fastn-account-id: <your-account-id>
x-fastn-account-tenant-id: <tenant-id>
```

### Execution Tiers

| Tier         | Behavior                                                                | Returns       | Max timeout | Timeout range | Use when                                                              |
| ------------ | ----------------------------------------------------------------------- | ------------- | ----------- | ------------- | --------------------------------------------------------------------- |
| **Instant**  | Synchronous — caller waits for result                                   | Result inline | 60 seconds  | 1s – 2min     | API endpoints needing responses, quick lookups, real-time validations |
| **Standard** | Asynchronous via Temporal — returns immediately, executes in background | 202 Accepted  | 15 minutes  | 5s – 15min    | Data syncs, multi-step processes, most workflows                      |
| **Long**     | Asynchronous via Temporal — for large data volumes                      | 202 Accepted  | 6 hours     | 30s – 6hrs    | Batch imports, full backfills, large report generation                |

The timeout slider in the Configuration panel adjusts within the tier's allowed range.

### Retry Policy

Toggle ON in the Configuration panel to enable automatic retries for failed executions.

| Parameter               | Default | Description                                                                         |
| ----------------------- | ------- | ----------------------------------------------------------------------------------- |
| **Max Attempts**        | 3       | Total number of execution attempts (including the first).                           |
| **Initial Interval**    | 5000ms  | Wait time before the first retry.                                                   |
| **Backoff Coefficient** | 2       | Multiplier applied to the interval after each retry. With defaults: 5s → 10s → 20s. |
| **Max Interval**        | 60000ms | Upper limit on the wait time between retries, regardless of backoff.                |

### Workflow Lifecycle

```
Create → Save (draft) → Publish (versioned snapshot) → Deploy (to environment)
```

| Stage       | What happens                                                                                                                                  |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Create**  | New workflow with default `export default async function(ctx)` template. Via "Create Workflow" (manual) or "Build with AI" (agent-generated). |
| **Save**    | Persists the current code and configuration as a draft. Does not create a version or go live.                                                 |
| **Publish** | Creates a version snapshot (v1, v2, etc.). The version is immutable — you can roll back to any previous version.                              |
| **Deploy**  | Sends a published version to a target environment. The workflow starts processing triggers in that environment.                               |

#### Statuses

| Status       | Badge             | Description                                                                        |
| ------------ | ----------------- | ---------------------------------------------------------------------------------- |
| **active**   | ✓ green checkmark | Deployed and processing triggers.                                                  |
| **inactive** | —                 | Exists but not processing triggers. Toggle via the Status switch in Configuration. |

#### Versioning

Each Publish creates a new version (v1, v2, v3...). The Workflows table shows the current version in the **VERSION** column. The Executions tab records which version was running at the time of each execution.

### Workflows Table

**Location:** Integrations → Workflows

**Filter tabs:** All | Instant | Standard | Long

**Buttons:** Create Workflow (opens code editor), ✦ Build with AI (opens Standalone Workflow Builder)

| Column      | Description                              |
| ----------- | ---------------------------------------- |
| **NAME**    | Workflow name, slug, and description     |
| **STATUS**  | ✓ active (green) or inactive             |
| **VERSION** | Current published version (v1, v2, etc.) |
| **UPDATED** | Last update date                         |
| **ACTIONS** | Run, Delete buttons                      |

***

### Execution Log

**Location:** Activity → Executions

**Filter tabs:** All | Running | Completed | Failed | Timeout

**Controls:** Time range dropdown, workflow filter dropdown, Refresh button.

| Column           | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| **TIME**         | Relative timestamp ("17h ago", "1d ago")                    |
| **WORKFLOW**     | Workflow name                                               |
| **TIER**         | Execution tier badge (INSTANT, STANDARD, LONG)              |
| **VERSION**      | Workflow version at time of execution                       |
| **STATUS**       | Running, Completed, Failed, Timeout                         |
| **DURATION**     | Execution time (79ms, 2.1s)                                 |
| **TRIGGERED BY** | What started it (agent-service, webhook, scheduler, manual) |
