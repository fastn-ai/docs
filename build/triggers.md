---
description: What starts a workflow — an inbound webhook, a schedule, or an event from a connected system.
---

# Triggers

**Integrations → Triggers**

<figure><img src="../.gitbook/assets/triggers.jpg" alt="The triggers page"><figcaption></figcaption></figure>

A workflow with no trigger only runs when something calls it. A trigger is what makes it run on its own.

The page splits into three tabs — **Webhooks**, **Schedulers**, **App events** — each with a count and a status filter (All / Active / Disabled).

### Choosing a type

<figure><img src="../.gitbook/assets/add-trigger-dialog.jpg" alt="The add trigger dialog"><figcaption></figcaption></figure>

| Type          | Fires when                                                     | Reach for it when                                            |
| ------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| **Webhook**   | Another system calls a URL you give it. Nothing is polled.     | The sender can push, and you want it immediate.               |
| **Schedule**  | A clock you set.                                               | Nightly reconciliation, hourly pulls, anything time-based.    |
| **App event** | Something changes in a connected system.                       | A HubSpot deal moves, a GitHub PR merges.                     |

---

## Webhook triggers

<figure><img src="../.gitbook/assets/webhook-trigger-form.jpg" alt="The new webhook trigger form"><figcaption></figcaption></figure>

### Identity

| Field           | Notes                                                       |
| --------------- | ------------------------------------------------------------- |
| **Name**        | Required. Shown in the list and on every execution record.   |
| **Description** | Optional.                                                   |

### Routes

A route says where a payload goes when it arrives. **Add route** creates more than one, which fans a single inbound call out to several workflows.

| Field           | Notes                                                                                                                                        |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Workflow**    | Required. Which workflow this route runs.                                                                                                     |
| **Environment** | Optional. `test (latest published)` runs the workflow's latest published version. A named environment runs the version deployed there, and the fire fails if nothing is deployed to it. |
| **Headers**     | Optional key/value pairs sent with the request to the workflow. Use for a key the workflow needs to call back to the sender.                  |

### Delivery attempts

How many times in total fastn tries to deliver an event to the workflow, counting the first try. After the last attempt the event is parked under **Failed deliveries**, where you can inspect and replay it.

| Field                | Range / options                                            | Default          |
| -------------------- | ------------------------------------------------------------ | ---------------- |
| **Max attempts**     | 1–10. `1` means try once and never retry.                   | 3                |
| **Backoff strategy** | Exponential (1s, 2s, 4s…), Linear (1s, 2s, 3s…), Fixed (1s, 1s, 1s…) | Exponential |

### Advanced options

<figure><img src="../.gitbook/assets/webhook-advanced-options.jpg" alt="Webhook advanced options"><figcaption></figcaption></figure>

| Field                 | Notes                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Webhook ID**        | Becomes part of the public webhook URL. Leave empty and one is generated.                                                                 |
| **Authentication**    | **API Key (x-fastn-access-key)** — callers must send the header. **None (public)** — anyone with the URL can fire it.                     |
| **Execution mode**    | **Parallel** — concurrent events run concurrently. **Sequential** — one at a time, in arrival order.                                      |
| **Deduplication key** | A field in the incoming payload that uniquely identifies each event, so a retried delivery from the sender does not run the workflow twice. Dotted paths and array indexes work: `data.event.id`, `items[0].id`. |

{% hint style="danger" %}
Only use **None (public)** when the sender genuinely cannot set a header, and pair it with a deduplication key and a workflow that validates its own payload.
{% endhint %}

{% hint style="success" %}
Sequential mode plus a deduplication key is the combination that makes a webhook-driven sync idempotent. Worth setting up front rather than after the first duplicate-record incident.
{% endhint %}

---

## Schedule triggers

<figure><img src="../.gitbook/assets/schedule-trigger-form.jpg" alt="The new schedule trigger form"><figcaption></figcaption></figure>

Name and description as above, then a schedule. Five modes:

| Mode         | Configure                                        |
| ------------ | -------------------------------------------------- |
| **Interval** | Run every *n* minutes / hours / days.             |
| **Daily**    | A time of day.                                    |
| **Weekly**   | Days of the week, and a time.                     |
| **Monthly**  | Days of the month, and a time.                    |
| **Custom**   | A cron expression, for anything the others miss.  |

**Timezone** is required and defaults to your organisation's, set under [General](../manage/general.md). A preview underneath summarises the effective schedule, so you can check it before saving.

{% hint style="info" %}
Every time on this form is interpreted in the timezone you pick, not the viewer's. If your team is spread out, agree on one and stay with it.
{% endhint %}

---

## App event triggers

<figure><img src="../.gitbook/assets/app-event-trigger-form.jpg" alt="The new app event trigger form"><figcaption></figcaption></figure>

The shortest form: a **Name** and a **Connector**. Choosing the connector reveals the events that system publishes, and you pick which one fires the workflow.

App events are the cleanest option when the connector supports them — no URL to hand out, no polling, and fastn manages the subscription with the upstream provider on your behalf.

### Managing triggers

The status filter separates active from disabled. Disabling a trigger stops it firing without losing its configuration — the right move while you fix a workflow, and better than deleting it.
