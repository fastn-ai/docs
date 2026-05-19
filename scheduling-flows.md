---
description: >-
  Run flows automatically on a timer whether daily syncs, hourly checks, weekly
  reports.
hidden: true
---

# Scheduling Flows

Scheduled flows run automatically at intervals you define. Use them for recurring jobs like data syncs, report generation, cleanup tasks, or periodic health checks that should happen without anyone triggering them manually.

### Two ways to set up a schedule

Fastn gives you two paths to run flows on a timer. They achieve the same result but start from different places.

#### Option A: Create a flow with the On Schedule trigger

This is the most common approach. You build the flow and define the schedule as part of the flow itself.

1. Click **Create** → **Flow** → **Start from Scratch**.
2. Name your flow (e.g., `daily_sync`).
3. Under **Select a starting point**, choose **On Schedule.**
4. Click **Build**.

The flow builder opens with a **Trigger on Specific Schedule** step on the canvas. Click this step to open its configuration panel on the right.

<figure><img src=".gitbook/assets/Area.gif" alt="Animated demo of creating a new flow with the On Schedule trigger and opening the flow builder"><figcaption></figcaption></figure>

#### Option B: Create a schedule in the Triggers section

This approach registers the schedule first, then links it to an existing flow. It follows a two-step process: **Register**, then configure the **Trigger**.

**Step 1 - Register the trigger**

1. Click **Triggers** in the left sidebar.
2. Click the **Schedules** tab (the Triggers section has three tabs: **Webhooks**, **Schedules**, **Apps**).
3. Click **+ Add a Schedule** (top-right corner).
4. Enter a **Name** for your schedule (e.g., `daily_sync`).
5. Under **Select an Event Model**, select **Json (default)**.
6. Click **Register**.

<figure><img src=".gitbook/assets/scheduling part 2.gif" alt="Animated demo of registering a new schedule trigger from the Triggers section"><figcaption></figcaption></figure>

**Step 2 — Configure the Trigger**

After registering, you advance to the **Trigger** step where you configure the schedule interval and link the flow to trigger.

<figure><img src=".gitbook/assets/scheduling intervals part 2.png" alt="Trigger configuration panel showing Schedule Type, Value, Unit of time, and Select destination fields"><figcaption></figcaption></figure>

Use Option B when you already have a flow built and want to add a schedule to it afterward, or when you want to manage all your schedules from one place without opening each flow individually.

> **Which should I use?** For most cases, **Option A** is simpler — you build the flow and its schedule together. Use **Option B** when you need to manage schedules separately from the flows (e.g., one flow triggered by multiple different schedules, or an ops team managing schedules without editing flow logic).

### Configuring schedule intervals

When you click the **Trigger on Specific Schedule** step on the canvas, the right panel shows two scheduling modes under **Trigger on**: **Date/Time** and **Interval**. Pick whichever fits your use case.

#### Interval mode

Use this when you want a flow to repeat at a fixed frequency (e.g., every 60 minutes, every 24 hours).

The panel shows two fields:

* **Trigger on** — a number input (e.g., `60`)
* **Unit dropdown** — `minutes` (select the unit that matches your interval)

To run a flow every hour, set the value to `60` and the unit to `minutes`. To run every 15 minutes, set it to `15` minutes.

<figure><img src=".gitbook/assets/scheduling intervals.png" alt="Flow builder canvas with a Trigger on Specific Schedule step and the interval configuration panel on the right"><figcaption></figcaption></figure>

#### Date/Time mode

Use this when you want a flow to run at a specific time (e.g., every day at 6:00 AM, or on the 1st of every month).

The panel shows four dropdown fields:

| Field       | Values    | What it controls                                   |
| ----------- | --------- | -------------------------------------------------- |
| **Minutes** | Any, 0–59 | The minute of the hour the flow runs               |
| **Hours**   | Any, 0–23 | The hour of the day the flow runs (24-hour format) |
| **Day**     | Any, 1–31 | The day of the month the flow runs                 |
| **Month**   | Any, 1–12 | The month the flow runs                            |

**"Any"** means "every", it it acts as a wildcard. Setting all four to Any runs the flow every minute. Setting only Hours to `6` and leaving the rest as Any runs the flow at the start of every minute during the 6 AM hour, every day, every month.

**Common examples:**

| Goal                                 | Minutes                                                                | Hours | Day | Month |
| ------------------------------------ | ---------------------------------------------------------------------- | ----- | --- | ----- |
| Every day at 6:00 AM                 | 0                                                                      | 6     | Any | Any   |
| Every day at 9:00 AM and 5:00 PM     | Requires two schedules: one with Hours=9, one with Hours=17            |       |     |       |
| First day of every month at midnight | 0                                                                      | 0     | 1   | Any   |
| Every Monday at 9:00 AM              | Not directly supported — use Interval mode or a webhook-based schedule |       |     |       |

> **Note:** The Date/Time mode does not have a "day of week" field. If you need to run a flow on specific weekdays (e.g., every Monday), use the Interval mode and set an appropriate minute interval, or create a webhook-based schedule with external cron tooling.

#### Additional schedule configuration

Both modes share additional configuration below the schedule settings:

* **Headers** — optionally add custom headers that will be included when the schedule triggers the flow. Click **+ Add Header** to define key-value pairs.
* **API Event Payload** — optionally define a JSON payload that gets sent to the flow each time the schedule fires. This is useful when your flow expects input data. The default is `{}` (empty).
* **Save** — click Save after configuring the schedule.

### Managing schedules

#### Viewing active schedules

All active schedules are visible in one place:

1. Click **Triggers** in the left sidebar.
2. Click the **Schedules** tab.

This shows every schedule with its **Name**, **Total** runs, **Processed**, **Failed**, **Missed**, **Last updated**, and **Trigger URL**. Use the search box ("Find your Schedule") to filter if you have many.

#### Pausing a schedule

If you need to temporarily stop a flow from running without deleting the schedule, you can pause it from the **Triggers → Schedules** tab. The schedule stays configured but does not fire until you resume it.

#### Editing a schedule

To change the interval:

* **If you used Option A (On Schedule trigger):** Open the flow, click the trigger step, change the interval in the right panel, click Save, then **Deploy**.
* **If you used Option B (Triggers → Schedules):** Go to Triggers → Schedules, find the schedule, and edit it directly.

> **Important:** After editing a schedule inside a flow, you must redeploy the flow. The schedule runs based on the deployed version, not the draft. If you change the interval but forget to deploy, the old interval keeps running.

### Monitoring scheduled flows

Because scheduled flows run without user interaction, monitoring is essential.

#### Check execution logs

1. Click **Logs** in the left sidebar.
2. Search for your flow name (e.g., `daily_record_sync`) using the search box ("Search by flow name & tenant").
3. Each execution shows: **Flow Name**, **Request Time**, **Duration (s)**, **HTTP Status Code**, and **tenantId**.
4. Click **View logs** on any row to see the step-by-step execution details.

Look for:

* **HTTP Status Code 200** = successful execution.
* **Any non-200 code** = something failed. Click into the logs to see which step broke.
* **Gaps in execution times** = the schedule may have stopped. Check if the flow is still deployed and the schedule is active.

#### Set up failure notifications

Do not rely solely on checking logs manually. Add an alert step inside your flow so failures are visible immediately.

Recommended pattern: After your main logic, add a Switch step. If any upstream step failed, route to a Connector step that posts to Slack, sends an email, or writes to a monitoring tool.

### Common issues

| Problem                                 | Cause                                              | Fix                                                                                                                                                                                   |
| --------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scheduled flow is not running           | Flow is not deployed, or schedule is paused        | Check the flow's status on the Flows list — it must be **Live** (green dot). Check Triggers → Schedules to confirm the schedule is active, not paused.                                |
| Flow runs at the wrong time             | Timezone mismatch                                  | Verify which timezone the schedule uses. If you set Hours to `6`, the platform may run it at 6:00 UTC, not your local time.                                                           |
| Flow runs but produces no output        | External API returns no data at the scheduled time | Add a Logger step after the Connector to inspect what data is returned. The source app may have no new records since the last run.                                                    |
| Duplicate processing                    | No deduplication logic                             | Add a Database step that tracks the last-processed record ID or timestamp. On each run, only fetch records newer than the last checkpoint.                                            |
| Schedule stopped after editing the flow | Flow not redeployed after changes                  | Click **Deploy** again. The schedule runs the last deployed version. If the status shows "Changes Pending", the schedule is still using the old version.                              |
| Too many executions consuming resources | Interval set too aggressively                      | Increase the interval. If you do not need data fresher than 1 hour, do not schedule every 15 minutes. Align the interval to your actual business need.                                |
| Flow partially completes then times out | Too many records to process in one run             | Add pagination to your Connector query. Process a fixed batch per run (e.g., 100 records) and store a cursor in the Database for the next run to pick up where the last one left off. |
