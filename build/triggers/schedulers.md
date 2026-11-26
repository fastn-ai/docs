---
description: A trigger that fires on a clock you set.
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

# Schedule triggers

**Build → Integrations → Triggers** → **Schedulers** · [Open in Fastn](https://app.fastn.dev/integrations?tab=triggers)

A **schedule trigger** runs your workflows on a clock you set. Use it for anything time-based, such as a nightly reconciliation or an hourly pull of new records. In the app, the same thing is also labeled **Scheduler** (see [Triggers](README.md#trigger-types)).

This page covers creating and configuring a schedule trigger. To check its runs, see [Operate → Triggers](../../operate/triggers/README.md).

### The Schedulers list

The list has these columns: `Name`, `Schedule`, `Next run`, `Last run`, `Status`, `Failures`, `Timezone`, `Routes`, `Created`, `Actions`. Two are worth knowing before you scan it:

* **`Schedule`:** `Every N unit` (for example `Every 5 minutes`) for an interval schedule, and the cron expression for every other mode.
* **`Failures`:** Counts *consecutive* failures, and resets on a success. A rising number warns you that Fastn is about to disable the trigger. See [When Fastn disables a trigger for you](README.md#when-fastn-disables-a-trigger-for-you).

### Create a schedule trigger

{% stepper %}
{% step %}
#### Name it

From **Add trigger**, choose **Schedule**, and give it a **Name** (required) and an optional **Description**.
{% endstep %}

{% step %}
#### Pick a mode and set the schedule

There are five modes:

| Mode         | Configure                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------- |
| **Interval** | The default. **Run every** *n* + `minutes` / `hours` / `days`, with a live preview: *Every 5 minutes*. |
| **Daily**    | **Time**, defaulting to 09:00.                                                                     |
| **Weekly**   | One toggle per day of the week (S M T W T F S), and a time.                                       |
| **Monthly**  | **Day of month**, 1 to 31 (one day, not several), and a time.                                     |
| **Custom**   | **Cron expression**, required. *Standard 5-field cron: minute hour day-of-month month day-of-week*  |

An interval is stored as a rate, and every other mode is stored as a cron expression. The list's `Schedule` column shows whichever was stored. A trigger built with *Interval, every 5 minutes* shows `Every 5 minutes`, and one built with *Daily, 06:00* shows `0 6 * * *`. Use **Custom** for schedules the other four can't express.

Some examples:

* **Every 5 minutes:** Interval mode, 5 minutes.
* **Daily at 6 AM:** Daily mode, 06:00.
* **Every Monday at 9 AM:** Weekly mode, Monday, 09:00.
* **First of every month:** Monthly mode, day 1.
{% endstep %}

{% step %}
#### Set the timezone and start

* **Timezone:** Required. A new schedule defaults to your organization's default timezone (set under **Settings → General**) if one is set, and otherwise to your browser's zone. It doesn't use the timezone on [your profile](../../manage/profile.md). An existing schedule keeps the zone it was saved with.
* **Starts at:** Optional. The date and time to begin.
* **Run immediately on create:** A checkbox. Select it for a first run right away.

Every time on this form is read in the timezone you pick, not the viewer's. If your team works across timezones, agree on one and keep to it.
{% endstep %}

{% step %}
#### Add routes, with a payload if the workflow needs one

Add at least one route. See [Routes](README.md#routes) for the **Workflow**, **Environment** and **Headers** fields.

Routes on a schedule trigger have one more field: **Payload** (JSON), optional. It is the body handed to the workflow, since a scheduled run has no inbound request to supply one.
{% endstep %}

{% step %}
#### Set the advanced options, if you need them

| Field                     | Notes                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| **Scheduler ID**          | Optional. Leave it empty and one is generated.                                                  |
| **Delay** (minutes)       | Default `0`. Holds the run back by this many minutes after the scheduled time. Useful when an upstream app needs time to finish first. |
| **Keep failed deliveries** | Off by default. Select it to retry failed deliveries and keep them for inspection. It shows **Max attempts** and **Backoff strategy** (Exponential, Linear or Fixed). Left off, each scheduled run gets one attempt with no delivery retries. |
{% endstep %}

{% step %}
#### Create it

Select **Create trigger** (there is no Save button), and the trigger joins the **Schedulers** list.

To run it without waiting for the next scheduled time, select its row and use **Trigger Now** in the footer of the detail panel.
{% endstep %}
{% endstepper %}

### What's next

* [Inspect a trigger](README.md#inspect-a-trigger): read a schedule's next run, last run and status history.
* [Operate → Triggers](../../operate/triggers/README.md): watch the runs it starts.
