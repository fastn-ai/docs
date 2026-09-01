---
description: Everything moving in and out of your customers' systems, newest first.
---

# Events

**Activity → Events**

<figure><img src="../.gitbook/assets/activity-events.jpg" alt="The events log"><figcaption></figcaption></figure>

An event is one inbound arrival: a webhook fired, a schedule reached, or a manual run. This is the first place to look when something did not happen.

### The table

| Column     | Notes                                                          |
| ---------- | ---------------------------------------------------------------- |
| **Event**  | The event identifier.                                          |
| **Source** | `webhook`, `scheduled` or `manual`.                            |
| **Status** | Delivered, or a failure state.                                 |
| **When**   | Timestamp, in your timezone.                                   |

Filter chips carry live counts — **All**, **Webhook**, **Scheduled**, **Manual** — so you can see at a glance whether your schedules are firing.

### Auto refresh

The toggle top-right keeps the list current without reloading. Useful while you are testing a webhook from the sending system; turn it off when you want to read a stable list.

### Replay

Every row has **Replay**, which re-delivers the same payload to the same workflow. Use it after fixing a workflow that failed on an event you cannot ask the sender to resend.

{% hint style="warning" %}
Replay re-runs the workflow for real. If the workflow writes to an external system, and it has no deduplication key, replaying can create duplicates. Set a [deduplication key](../build/triggers.md) on the webhook trigger before you need it.
{% endhint %}

### Failed deliveries

When a webhook trigger exhausts its delivery attempts, the event is parked under **Failed deliveries**, where you can inspect the payload and replay it once the cause is fixed. Attempt count and backoff are configured on the trigger.

### Events versus executions

An event is *something arrived*. An execution is *a workflow ran*. One event can produce several executions when a webhook fans out to multiple routes, and an event can be Delivered while the execution it started fails. Check both.
