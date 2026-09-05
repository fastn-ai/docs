---
description: >-
  Monitor events, connector traces, workflow executions, and alert rules across
  your entire workspace.
---

# Activity

The **Activity** section is where you, as a SaaS admin, monitor everything happening across your integrations, events, connector traces, workflow executions, and alert rules.

This is distinct from the widget's Insights tab, which shows a single customer their own activity. Activity covers everything across your workspace.

The section has four tabs: **Events, Traces, Alerts, Executions**.

### Events

Heading: "Events" — "Monitor incoming and outgoing integration events."

Tracks the integration events flowing through your workspace.

* **Filters:** All, Webhook, Scheduled, Manual
* **Auto-refresh:** A checkbox in the top-right (unchecked by default) that keeps the list updating
* **Empty state:** "No events match the selected filter."

### Traces

Heading: "Traces" — "Monitor connector execution traces and performance."

A trace represents a connector execution. Use this tab to inspect connector-level performance and diagnose issues.

* **Filters:** All, Success, Error, Pending
* **Empty state:** "No traces found."

### Executions

Heading: "Executions" — "Monitor workflow executions across all workflows."

This is the cross-workflow execution log — every run of every workflow in one place. (For the executions of a single workflow, the workflow editor has its own Executions tab.)

**Columns:**

| Column       | Description                      | Example                                |
| ------------ | -------------------------------- | -------------------------------------- |
| TIME         | When the execution ran, relative | "11m ago"                              |
| WORKFLOW     | The workflow name                | Slack Messages to Supabase Hourly Sync |
| TIER         | Execution tier badge             | STANDARD                               |
| VERSION      | The workflow version that ran    | v5                                     |
| STATUS       | The execution result             | completed                              |
| DURATION     | How long it took                 | 29.1s (29127ms)                        |
| TRIGGERED BY | What started it                  | agent-service                          |

**Filters:**

* Status pills: All, Running, Completed, Failed, Timeout
* An **All workflows** dropdown to filter by a specific workflow
* An **All time** dropdown (time-range filter)
* A **Refresh** button

### Alerts

Heading: "Alert Rules" — "Configure alert rules to monitor connector and workflow performance."

Create rules that notify you when a metric crosses a threshold. A **Create Alert** button is in the top-right; the empty state reads "No alert rules configured" with a "Create your first alert" button.

For the full list of alert conditions and how to create one, see [Alerts](https://claude.ai/fastn/reference/alerts).
