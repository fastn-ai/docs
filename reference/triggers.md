---
description: >-
  Webhook triggers with routes and filters, scheduler presets, app event
  subscriptions, and trigger management.
---

# Triggers

Triggers start workflows. They're managed separately under **Integrations → Triggers** and consist of three types:

### Webhook triggers

Receive events from external services via HTTP POST.

#### Configuration

| Field                | Required         | Description                |
| -------------------- | ---------------- | -------------------------- |
| **Name**             | Yes              | Trigger identifier         |
| **Description**      | No               | What this webhook receives |
| **Routes**           | Yes (at least 1) | Map payloads to workflows  |
| **Advanced options** | No               | Additional configuration   |

#### Routes

Each route maps incoming payloads to a workflow:

| Field           | Description                                                                 |
| --------------- | --------------------------------------------------------------------------- |
| **Workflow**    | Target workflow (dropdown of active workflows)                              |
| **Key / Value** | JSON filter — only payloads matching this key-value pair trigger this route |
| **Header**      | Optional headers to forward to the workflow                                 |

A single webhook trigger can have **multiple routes**. Different payloads go to different workflows through the same endpoint.

#### Example: Route by event type

```
Route 1: Workflow = "process-orders"     Key = event_type  Value = order.created
Route 2: Workflow = "update-inventory"   Key = event_type  Value = inventory.updated
Route 3: Workflow = "sync-contacts"      Key = event_type  Value = contact.updated
```

### Scheduler triggers

Trigger workflows on a time-based schedule.

#### Configuration

| Field           | Required | Description                                      |
| --------------- | -------- | ------------------------------------------------ |
| **Name**        | Yes      | Trigger identifier                               |
| **Description** | No       | What the scheduler does                          |
| **Schedule**    | Yes      | Frequency configuration                          |
| **Starts at**   | No       | Date/time to begin (leave empty for immediately) |

#### Schedule presets

| Preset       | Configuration                                          |
| ------------ | ------------------------------------------------------ |
| **Interval** | Run every X minutes/hours. Set number + unit dropdown. |
| **Daily**    | Run once per day at a specific time.                   |
| **Weekly**   | Run once per week on a specific day and time.          |
| **Monthly**  | Run once per month on a specific date and time.        |
| **Custom**   | Enter a cron expression for complex schedules.         |

### App Event triggers

Subscribe to events from connected third-party apps.

#### Configuration

| Field          | Required | Description                             |
| -------------- | -------- | --------------------------------------- |
| **Name**       | Yes      | Trigger identifier                      |
| **Connector**  | Yes      | Which connector to listen to (dropdown) |
| **Connection** | Yes      | Which authenticated connection to use   |
| **Event**      | Yes      | Which event to subscribe to             |

#### Event list

The event list shows available events from the selected connector:

| Element                 | Description                                         |
| ----------------------- | --------------------------------------------------- |
| **Event name**          | Human-readable name (e.g., "Sale Created")          |
| **Type badge**          | WEBHOOK — indicates the event mechanism             |
| **Subscription status** | **Not Subscribed** (red) or **Subscribed** (green)  |
| **Event path**          | Technical path (e.g., "Sale/Created")               |
| **Payload Schema**      | Expandable section showing the event data structure |

When you create the trigger, Fastn subscribes to the webhook on the third-party app automatically. Deleting the trigger unsubscribes.

### Trigger management

#### Tabs

| Tab            | Count shown | Contents                      |
| -------------- | ----------- | ----------------------------- |
| **Webhooks**   | e.g., "(0)" | Webhook triggers with routes  |
| **Schedulers** | e.g., "(1)" | Time-based triggers           |
| **App Events** | e.g., "(3)" | Connector event subscriptions |

#### Each tab has

* Search bar
* Status filter ("All statuses")
* Trigger list with edit/delete actions
