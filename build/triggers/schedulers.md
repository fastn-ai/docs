---
description: A trigger that fires on a clock you set.
---

# Schedule triggers

A schedule trigger fires on a clock you set: nightly reconciliation, hourly pulls, anything time-based.

**Columns:** `Name`, `Schedule`, `Next run`, `Last run`, `Status`, `Failures`, `Timezone`, `Routes`, `Created`, `Actions`.

Two of those are worth knowing before you scan the table:

* **`Schedule`** shows `Every N unit` (for example `Every 5 minutes`) for an interval schedule, and the cron expression for every other mode.
* **`Failures`** counts *consecutive* failures, and resets on a success. A number climbing here is the early warning that fastn is about to disable the trigger for you. See [when fastn disables a trigger](README.md#when-fastn-disables-a-trigger-for-you).

### Create a schedule trigger

{% stepper %}
{% step %}
#### Name it

From **Add trigger**, choose **Schedule**, and give it a **Name** (and an optional **Description**).

{% endstep %}

{% step %}
#### Pick a mode and set the schedule

Five modes:

| Mode         | Configure                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------- |
| **Interval** | The default. **Run every** *n* + `minutes` / `hours` / `days`, with a live preview: *Every 5 minutes*. |
| **Daily**    | **Time**, defaulting to 09:00.                                                                     |
| **Weekly**   | S - M - T - W - T - F - S toggles, and a time.                                                                 |
| **Monthly**  | **Day of month**, 1-31 (one day, not several) and a time.                                        |
| **Custom**   | **Cron expression**, required. *Standard 5-field cron: minute hour day-of-month month day-of-week*  |

**An interval is stored as a rate; every other mode is stored as a cron expression**, and the list's `Schedule` column shows whichever was stored. A trigger built with *Interval, every 5 minutes* displays `Every 5 minutes`; one built with *Daily, 06:00* displays `0 6 * * *`. **Custom** is the escape hatch for schedules the other four cannot express.
{% endstep %}

{% step %}
#### Set the timezone and start

**Timezone** is required. A new schedule defaults to your organization's default timezone (set under **Settings → General**) if one is set, otherwise to your browser's zone. It does not use the one on [your profile](../../manage/profile.md). An existing schedule keeps the zone it was saved with. Two more fields sit alongside it: **Starts at**, optional, and **Run immediately on create**, a checkbox.
{% endstep %}

{% step %}
#### Add routes, with a payload if the workflow needs one

At least one route is required, and each route needs a **Workflow**. Each route also has an optional **Environment** (defaulting to **test (latest published)**, which runs the latest published version) and optional **Headers** (key/value). Routes on a schedule trigger carry one field the other two do not: **Payload** (JSON), optional, which is the body handed to the workflow when there is no inbound request to supply one.
{% endstep %}

{% step %}
#### Set the advanced options, if you need them

| Field                     | Notes                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Scheduler ID**          | Optional. Leave it empty and one is generated.                                                  |
| **Delay (minutes)**       | Default `0`. Holds the run back by this many minutes after the scheduled moment: useful when an upstream system needs a head start. |
| **Keep failed deliveries** | Off by default. Tick it to retry failed deliveries and keep them for inspection; it reveals **Max attempts** and **Backoff strategy** (Exponential, Linear or Fixed). Left off, each scheduled run gets one attempt with no delivery retries. |
{% endstep %}

{% step %}
#### Create it

Select **Create trigger** (there is no Save button) and it joins the **Schedulers** list. **Trigger Now** fires it immediately without waiting for the next scheduled moment; it sits in the footer of the trigger's detail panel, which opens when you click the row.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Every time on this form is interpreted in the timezone you pick, not the viewer's. If your team is spread out, agree on one and stay with it.
{% endhint %}
