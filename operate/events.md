---
description: Everything moving in and out of your customers' apps, newest first.
---

# Events

**Activity → Events**

An event is one inbound arrival: a webhook fired, a schedule reached, or a manual run. This is the first place to look when something did not happen.

### The table

| Column     | Notes                                                          |
| ---------- | ---------------------------------------------------------------- |
| **Event**  | The source's name, with the connector underneath.             |
| **Source** | The kind of event, for example `webhook`.                     |
| **Status** | `Delivered`, `Active`, `Idle`, `Queued`, `Warning`, `Retrying` or `Failed`. `Delivered` is a successful hand-off. |
| **When**   | Timestamp, in your timezone.                                   |
| **Replay** | Re-delivers the row. See below.                                |

Filter chips carry live counts (**All**, **Webhook**, **Scheduled**, **Manual**) so you can see at a glance whether your schedules are firing. **Search events** narrows the list. A time range select (**All time**, **Last 1h**, **Last 24h**, **Last 7d**, **Last 30d**, **Last 90d**), an environment select (**All environments**) and a **Refresh** button sit beside it.

The list is paginated: **Rows per page** sets 25, 50 or 100. Click a row to expand it into a detail panel. To see what a run did with an event, go to [Executions](executions.md).

### Auto refresh

The toggle top-right is **off** by default. Turn it on to keep the list current without reloading (useful while you are testing a webhook from the sending app) and off again when you want to read a stable list.

### Replay

Owners, admins, developers and operators see **Replay** on each row, which re-delivers the same payload to the same workflow. It is disabled while the event is still pending. Use it after fixing a workflow that failed on an event you cannot ask the sender to resend.

{% hint style="warning" %}
Replay re-runs the workflow for real. If the workflow writes to an external app, and it has no deduplication key, replaying can create duplicates. Set a [deduplication key](../build/triggers/README.md) on the webhook trigger before you need it.
{% endhint %}

An event that exhausts its delivery attempts shows a failure state in the **Status** column and can be re-sent with **Replay** once the cause is fixed. Attempt count and backoff are configured on the trigger, not here.

### When nothing is listed

An empty filter gives you **Nothing matches that filter**, with:

> Events arrive as your customers use their connected apps. Widen the filter, or check that a trigger is listening.

and a **Show all events** button. Take the second half of that literally: an empty Events log with a trigger you expected to fire is a trigger problem, not an events problem. See [Triggers](../build/triggers/README.md).

### Events versus executions

An event is *something arrived*. An execution is *a workflow ran*. One event can produce several executions when a webhook fans out to multiple routes, and an event can be Delivered while the execution it started fails. Check both.
