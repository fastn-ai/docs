---
description: >-
  Create webhook, schedule, and app event triggers under Integrations →
  Triggers and route them to your workflows.
---

# Setting Up Triggers

Triggers are what start your workflows. In fastn, triggers are managed **separately from workflows**: you create a trigger under **Integrations → Triggers**, then route it to one or more workflows.

1. Go to **Integrations** and open the **Triggers** tab.
2. The page has three tabs:
   * **Webhooks** - HTTP POST endpoints for external events
   * **Schedulers** - Time-based triggers (interval, daily, weekly, monthly, custom cron)
   * **App events** - Subscribe to events from your connectors
3. Click **Add trigger** to create a new trigger.
4. The **Add a trigger** picker asks *What should start the workflow?* Choose **Webhook**, **Schedule** or **App event**.

Every trigger type sends its fires through **routes**. A route names a **Workflow** (required) and an **Environment**. The environment defaults to **test (latest published)**, which runs the workflow's latest published version: publishing a new version changes what that route runs straight away, with no deploy step. Pick a named environment such as `live` if the route should only run what you have deployed there.

### Webhook triggers

Webhooks receive events from external services via HTTP POST. When a third-party app sends a webhook to your endpoint, the trigger routes the payload to your workflow.

#### Creating a webhook trigger

1. Click **Add trigger** → **Webhook**.
2. Enter a **Name** and optional **Description**.
3. Configure **Routes** (at least one is required). Each route has:

| Field           | What it does                                                                 |
| --------------- | ---------------------------------------------------------------------------- |
| **Workflow**    | Required. The target workflow.                                               |
| **Environment** | Optional. **test (latest published)** by default, or one of your named environments, which runs the version deployed there. |
| **Headers**     | Optional key/value pairs sent with the request to the workflow.              |

4. Click **Add route** to add more routes. A single webhook trigger can fan out to **multiple workflows**: every route receives every payload.
5. Set **Max attempts** and **Backoff strategy** for delivery, and expand **Advanced options** for the Webhook ID, Authentication, Execution mode and Deduplication key.
6. Click **Create trigger**.

#### Example: Fan one webhook out to two workflows

A single webhook endpoint that two workflows need to react to:

**Route 1:** Workflow = "process-new-orders"

**Route 2:** Workflow = "update-inventory"

Both workflows receive every payload sent to the webhook URL. If a workflow should only act on certain events, have it check the payload (for example `ctx.input.event_type`) and return early for the others.

### Schedule triggers

Schedule triggers run workflows on a time-based schedule.

#### Creating a schedule trigger

1. Click **Add trigger** → **Schedule**.
2. Enter a **Name** (required) and optional **Description**.
3. Configure the schedule using the mode buttons:

| Mode         | Configuration                                   |
| ------------ | ----------------------------------------------- |
| **Interval** | Run every X minutes, hours or days. Set number and unit. |
| **Daily**    | Run once per day at a specific time.            |
| **Weekly**   | Run on selected days of the week at a time.     |
| **Monthly**  | Run once per month on a specific day and time.  |
| **Custom**   | Enter a custom cron expression.                 |

4. For **Interval**: set "Run every \[number] \[minutes/hours/days]".
5. Set the **Timezone** (required). It defaults to your organization's default timezone if one is set, otherwise to your browser's.
6. Optionally set **Starts at** - a date/time to begin - and tick **Run immediately on create** if you want a first run straight away.
7. Add at least one **Route** and pick its **Workflow** (required). A route can also carry an **Environment**, **Headers** and a JSON **Payload** to hand to the workflow.
8. Click **Create trigger**.

#### Example schedules

* "Run every 5 minutes" - Interval mode, 5 minutes
* "Daily at 6 AM" - Daily mode, 06:00
* "Every Monday at 9 AM" - Weekly mode, Monday 09:00
* "First of every month" - Monthly mode, day 1

### App event triggers

App events subscribe to events from your connected third-party apps. When something happens in the app (new sale, contact update), fastn receives the event and triggers your workflow.

#### Creating an app event trigger

1. Click **Add trigger** → **App event**.
2. Enter a **Name**.
3. Select the **Connector** (for example "Cin7 Core"). It cannot be changed after the trigger is created.
4. Select the **Connection** - which authorized connection to use for this trigger. If there is none, connect one first.
5. Browse the **Event** list (with **Search events...**), which shows available events from the connector:
   * Each event shows: event name, type badge (**WEBHOOK**), and whether it is **Registered** or **Not Subscribed**
   * The raw event key (for example "Sale/Created")
   * Expandable **Payload Schema** showing the event data structure
6. Select the event you want to subscribe to.
7. Add at least one **Route**: **Workflow** (required), plus optional **Environment** and **Headers**.
8. Click **Create trigger**.

#### Event subscription

When you create an app event trigger, fastn subscribes to the webhook on the third-party app automatically. Check the new row's **Subscription** column: it reads `Subscribed`, `Pending`, `Failed`, `Not subscribed`, `Unsubscribed` or `Shared`. If it reads `Failed`, the trigger will never fire; use **Retry Subscription** from the row menu. When you delete the trigger, fastn unsubscribes.

### Managing triggers

#### Viewing triggers

Each tab (Webhooks, Schedulers, App events) shows a list of triggers with:

* Search bar
* Status filter (**All statuses**, **Active**, **Disabled**)
* Trigger count in the tab label

#### Editing and deleting

Click a trigger's row to open its detail panel, then **Edit** to change its configuration, routes or schedule; **Edit** is also in the row's menu. Delete triggers you no longer need from the row menu - this stops the webhook/schedule and unsubscribes from app events.

### What you've learned

* Triggers are managed separately from workflows under Integrations → Triggers
* Three trigger types: Webhook (with routes), Schedule (with modes), App event (with connector event subscription)
* A single trigger can route to multiple workflows, and each route picks the environment it runs in
* Schedules use friendly modes (not raw cron by default)
* App event triggers show subscription status and payload schemas
