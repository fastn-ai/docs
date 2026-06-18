---
description: >-
  Webhook triggers with routes and filters, scheduler presets, app event
  subscriptions, and trigger management.
---

# Triggers

Triggers start the workflows you build. They are managed separately from workflows under **Integrations → Triggers**, then routed to one or more workflows. The page header reads "Manage webhook and scheduler triggers for your workflows."

Most triggers are set up by the AI agent when you build a workflow ("on every new order," "daily at 6 AM"). This page documents the trigger types and their configuration for when you need to create or adjust one directly.

### Trigger types

The page has three tabs, each showing a count of existing triggers:

| Tab            | Starts a workflow when...                               |
| -------------- | ------------------------------------------------------- |
| **Webhooks**   | An external service sends an HTTP POST to your endpoint |
| **Schedulers** | A time-based schedule fires                             |
| **App Events** | An event occurs in a connected app                      |

Click **Add Trigger** (top-right) to open the "Select trigger type" panel, which has three cards: Webhook, Scheduler, App Event.

### Webhook triggers

A webhook trigger receives HTTP POST requests from external services and routes them to workflows.

**Fields:**

* **Name** (required)
* **Description** (optional)
* **Routes** (required) — Map incoming requests to workflows. Click **Add route** to add more.

Each route has:

* **Workflow** (required) — The target workflow.
* **Headers** — Key/value pairs.
* **Optional JSON filters** — Route based on the payload contents (a single webhook can route to different workflows based on different filters).

**Advanced options** (expander) reveal:

| Option                   | Default                 | Description                                           |
| ------------------------ | ----------------------- | ----------------------------------------------------- |
| Webhook ID               | (optional UUID)         | A specific ID for the webhook                         |
| Authentication           | API Key (`x-fastn-key`) | How the incoming request is authenticated             |
| Execution Mode           | Parallel                | How matched workflows execute                         |
| Deduplication Key        | (optional)              | Prevents duplicate processing of the same event       |
| Enable Dead Letter Queue | (checkbox)              | Captures failed events for later inspection or replay |

### Scheduler triggers

A scheduler trigger fires workflows on a time-based schedule.

**Presets:** Interval, Daily, Weekly, Monthly, Custom.

For **Interval**, you set "Run every \[n] minutes / hours / days," an optional "Starts at" time, and the form shows a live preview of the schedule (e.g., "Every 5 minutes").

Schedulers also have **Routes** with a Workflow target, Headers, and a Payload (JSON) passed to the workflow.

### App Event triggers

An app event trigger subscribes to events from a connected app and routes them to workflows.

**Creation fields:**

* **Name**
* **Connector** — A dropdown of available connectors (\~75).

Selecting a connector with no active connection shows: "No active connection found for this connector. Connect first to use it as a trigger source," with a Connect button. An active connection is required.

**The App Events list** shows these columns:

| Column       | Description                                         |
| ------------ | --------------------------------------------------- |
| NAME         | The trigger name                                    |
| CONNECTOR    | The source connector                                |
| TYPE         | The event type                                      |
| EVENTS       | The specific event (e.g., `Calendar.Events.Exists`) |
| WEBHOOK URL  | The endpoint the app posts to                       |
| STATUS       | The trigger's status                                |
| SUBSCRIPTION | Subscription state (e.g., ACTIVE)                   |
| ROUTES       | Routed workflows                                    |
| CREATED      | Creation date                                       |
| ACTIONS      | Edit/delete                                         |

