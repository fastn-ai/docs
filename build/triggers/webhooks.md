---
description: A trigger that fires when another app calls a URL you give it.
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

# Webhook triggers

**Build → Integrations → Triggers** → **Webhooks** · [Open in Fastn](https://app.fastn.dev/integrations?tab=triggers)

A **webhook trigger** gives you a URL. When another app sends an HTTP POST to that URL, the trigger passes the payload to your workflows. Nothing is polled, so the workflow runs the moment the event happens. For example, your store can send each new order to the URL, and the trigger runs your order workflow for it.

This page covers creating and configuring a webhook trigger. To call one from your backend, see [Call a webhook trigger](../../operate/triggers/using-a-webhook-trigger.md). To have your AI tool create one for you, see [Build a trigger with AI](README.md#build-a-trigger-with-ai).

### The Webhooks list

The list has these columns: `Name`, `Type`, `Status`, `Auth`, `Routes`, `Created`, then the row actions.

* **`Auth`:** `API key` where callers must send a Fastn API key, or `None (public)` where anyone with the URL can fire the trigger. Scan this column to audit which webhooks are public.
* **Row actions:** Unlike the Schedulers and App events tables, this column has no `Actions` header. The row menu is still at the end of each row.

### Create a webhook trigger

{% stepper %}
{% step %}
#### Name it

From **Add trigger**, choose **Webhook**.

* **Name:** Required. Shown in the list and on every execution record.
* **Description:** Optional.
{% endstep %}

{% step %}
#### Add at least one route

Each route sends the payload to one workflow. Add more routes with **Add route** to send one inbound call to several workflows. See [Routes](README.md#routes) for the **Workflow**, **Environment** and **Headers** fields.

On a webhook trigger, use a route's **Headers** for a key the workflow needs to call back to the sender.
{% endstep %}

{% step %}
#### Set delivery attempts

**Max attempts** sets how many times in total Fastn tries to deliver an event to the workflow, counting the first try. Once the attempts run out, the delivery is recorded as failed.

| Field                | Range / options                                      | Default          |
| -------------------- | ------------------------------------------------------ | ---------------- |
| **Max attempts**     | 1 to 10. `1` means try once and never retry.          | 3                |
| **Backoff strategy** | `Exponential (1s, 2s, 4s…)`, `Linear`, `Fixed`        | Exponential      |

Failed deliveries are listed on the trigger itself: select its row and look at **Failed deliveries (N)** in the detail panel, where you can **Replay** or **Delete** each one. See [Inspect a trigger](README.md#inspect-a-trigger).
{% endstep %}

{% step %}
#### Set the advanced options, if you need them

{% hint style="warning" %}
With **None (public)** authentication, anyone who has the URL can run your workflow. Use it only when the sender cannot set a header, and pair it with a deduplication key and a workflow that validates its own payload.
{% endhint %}

| Field                 | Notes                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Webhook ID**        | Optional. Becomes part of the public webhook URL. Leave it empty and one is generated.                                                   |
| **Authentication**    | **API Key (x-api-key)**, the default: callers must send a Fastn API key (`fsk_…`). See [Call a webhook trigger](../../operate/triggers/using-a-webhook-trigger.md) for the headers it accepts. **None (public)**: anyone with the URL can fire it. |
| **Execution mode**    | **Parallel**, the default: events that arrive together run at the same time. **Sequential**: one at a time, in arrival order.            |
| **Deduplication key** | Optional. A field in the incoming payload that uniquely identifies each event, so a delivery the sender retries does not run the workflow twice. |

Sequential mode plus a deduplication key is the combination that makes a webhook-driven sync idempotent. Set both up before the first duplicate record, not after.
{% endstep %}

{% step %}
#### Create it, then hand out the URL

Select **Create trigger** (there is no Save button), and the trigger joins the **Webhooks** list. Its row menu offers:

* **Copy URL:** The URL to give the sender.
* **Copy as cURL:** A ready-made command, the fastest way to fire the trigger by hand while you debug. With API key authentication, the command sends an `x-api-key: <YOUR_API_KEY>` header for you to fill in.
* **Disable**, **Edit** and **Delete:** See [Manage triggers](README.md#manage-triggers).
{% endstep %}
{% endstepper %}

### What's next

* [Call a webhook trigger](../../operate/triggers/using-a-webhook-trigger.md): send a request to the trigger from your backend.
* [Events](../../operate/events.md): check that the events arrived.
