---
description: >-
  Create webhook, scheduler, and app event triggers under Integrations →
  Triggers and route them to your workflows.
---

# Setting Up Triggers

Triggers are what start your workflows. In Fastn, triggers are managed **separately from workflows,** you create a trigger under **Integrations → Triggers**, then route it to one or more workflows.

1. Go to **Integrations → Triggers**.
2. The page has three tabs:
   * **Webhooks** — HTTP POST endpoints for external events
   * **Schedulers** — Time-based triggers (interval, daily, weekly, monthly)
   * **App Events** — Subscribe to events from your connectors
3. Click **Add Trigger** to create a new trigger.
4. Select the trigger type: **Webhook**, **Scheduler**, or **App Event**.

> **Screenshot needed:** Triggers page showing the three tabs and the Add Trigger type selection panel.

### Webhook triggers

Webhooks receive events from external services via HTTP POST. When a third-party app sends a webhook to your endpoint, the trigger routes the payload to your workflow.

#### Creating a webhook trigger

1. Click **Add Trigger** → **Webhook**.
2. Enter a **Name** and optional **Description** ("Describe what this webhook receives...").
3. Configure **Routes**:

Routes map incoming webhooks to workflows. Each route has:

| Field           | What it does                                                                 |
| --------------- | ---------------------------------------------------------------------------- |
| **Workflow**    | Select the target workflow from the dropdown                                 |
| **Key / Value** | Optional JSON filter — only payloads matching this filter trigger this route |
| **Header**      | Optional headers to forward to the workflow                                  |

4. Click **+ Add route** to add more routes. A single webhook trigger can route to **multiple workflows** based on different payload filters.
5. Expand **Advanced options** for additional configuration.
6. Click **Create**.

> **Screenshot needed:** Webhook trigger configuration showing Routes with workflow dropdown, Key/Value filter, and Header fields.

#### Example: Route by event type

A single webhook endpoint receiving different event types:

**Route 1:** Workflow = "process-new-orders", Filter Key = `event_type`, Value = `order.created` **Route 2:** Workflow = "update-inventory", Filter Key = `event_type`, Value = `inventory.updated`

Different payloads go to different workflows through the same webhook URL.

### Scheduler triggers

Schedulers trigger workflows on a time-based schedule.

#### Creating a scheduler trigger

1. Click **Add Trigger** → **Scheduler**.
2. Enter a **Name** (required) and optional **Description**.
3. Configure the **Schedule** using preset buttons:

| Preset       | Configuration                                   |
| ------------ | ----------------------------------------------- |
| **Interval** | Run every X minutes/hours. Set number and unit. |
| **Daily**    | Run once per day at a specific time.            |
| **Weekly**   | Run once per week on a specific day and time.   |
| **Monthly**  | Run once per month on a specific date and time. |
| **Custom**   | Enter a custom cron expression.                 |

4. For **Interval**: set "Run every \[number] \[minutes/hours]".
5. Optionally set **Starts at** — a date/time to begin. Leave empty to start immediately.
6. Click **Create**.

> **📷 Screenshot needed:** Scheduler trigger configuration showing the preset buttons (Interval, Daily, Weekly, Monthly, Custom) and the interval settings.

#### Example schedules

* "Run every 5 minutes" — Interval preset, 5 minutes
* "Daily at 6 AM" — Daily preset, 06:00
* "Every Monday at 9 AM" — Weekly preset, Monday 09:00
* "First of every month" — Monthly preset, day 1

### App Event triggers

App Events subscribe to events from your connected third-party apps. When something happens in the app (new sale, contact update), Fastn receives the event and triggers your workflow.

#### Creating an app event trigger

1. Click **Add Trigger** → **App Event**.
2. Enter a **Name**.
3. Select the **Connector** (e.g., "Cin7 Core") from the dropdown.
4. Select the **Connection** — which authenticated connection to use for this trigger.
5. Browse the **Event** list — shows available events from the connector:
   * Each event shows: event name, type badge (**WEBHOOK**), subscription status (**Not Subscribed** / **Subscribed**)
   * Event path (e.g., "Sale/Created")
   * Expandable **Payload Schema** showing the event data structure
6. Select the event you want to subscribe to.
7. Click **Create**.

> **Screenshot needed:** App Event trigger configuration showing the Connector dropdown, Connection dropdown, and the event list with event names, WEBHOOK badges, and subscription status.

#### Event subscription

When you create an App Event trigger, Fastn subscribes to the webhook on the third-party app automatically. The subscription status changes from "Not Subscribed" to "Subscribed". When you delete the trigger, Fastn unsubscribes.

### Managing triggers

#### Viewing triggers

Each tab (Webhooks, Schedulers, App Events) shows a list of triggers with:

* Search bar
* Status filter ("All statuses")
* Trigger count in the tab label (e.g., "Webhooks (0)", "Schedulers (1)", "App Events (3)")

#### Editing and deleting

Click on a trigger to edit its configuration, routes, or schedule. Delete triggers you no longer need — this stops the webhook/schedule and unsubscribes from app events.

### What you've learned

* Triggers are managed separately from workflows under Integrations → Triggers
* Three trigger types: Webhook (with routes and filters), Scheduler (with presets), App Event (with connector event subscription)
* A single webhook trigger can route to multiple workflows
* Schedulers use friendly presets (not raw cron by default)
* App Event triggers show subscription status and payload schemas
