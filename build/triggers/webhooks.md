---
description: A trigger that fires when another system calls a URL you give it.
---

# Webhook triggers

**Integrations → Triggers** - in your dashboard, `/integrations?tab=triggers`.

A webhook trigger fires when another system calls a URL you give it. Nothing is polled.

{% hint style="info" %}
**Looking for triggers somewhere else?** They used to sit under Settings and under Activity. Both of those paths now redirect to **Integrations**, which is the one place triggers are created and listed. Its tabs are **Connectors**, **Workflows**, **Triggers** and **Unified APIs**.
{% endhint %}

**Columns:** `Name`, `Type`, `Status`, `Auth`, `Routes`, `Created`, then the row actions.

* **`Auth`** reads `API key` where the webhook requires an API key in the `x-api-key` header, or `None (public)` where anyone with the URL can fire it. It is the column to scan if you are auditing exposure.

Unlike the Schedulers and App events tables, this one ships **no `Actions` header**: the row menu is still there at the end of each row, the column simply has no title. That is a quirk of the product, not a missing feature.

### Can Build with AI do this for me?

Yes. [Build with AI](../agent/README.md) can bind triggers as part of building a workflow - webhook, schedule and app-event triggers are all actions it can take, so "run this whenever my store sends an order webhook" is a reasonable thing to ask for in plain language rather than wiring by hand.

What Build with AI binds is the trigger-to-workflow connection. You still come to this screen to read the URL it created, to copy it as cURL while debugging, or to disable or delete it. Build it by hand when you want control over the routes, the delivery attempts and the auth up front; ask Build with AI when you want the workflow and its trigger created together.

### Create a webhook trigger by hand

{% stepper %}
{% step %}
#### Name it

From **Add trigger**, choose **Webhook**.

| Field           | Notes                                                       |
| --------------- | ------------------------------------------------------------- |
| **Name**        | Required. Shown in the list and on every execution record.   |
| **Description** | Optional.                                                   |
{% endstep %}

{% step %}
#### Add at least one route

A route says where a payload goes when it arrives. Routes are required. Add more with **Add route** to fan a single inbound call out to several workflows.

| Field           | Notes                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| **Workflow**    | Required. Which workflow this route runs.                                                                |
| **Environment** | Optional. `test (latest published)`, the default, runs the workflow's latest published version, so publishing a new version changes what this route runs without any deploy. **Any other option is one of your organization's named environments** (see [Environments](../../manage/environments.md)) and runs the version deployed there, and **if nothing is deployed there, the fire fails**. |
| **Headers**     | Optional key/value pairs sent with the request to the workflow. Use for a key the workflow needs to call back to the sender. |
{% endstep %}

{% step %}
#### Set delivery attempts

How many times in total fastn tries to deliver an event to the workflow, counting the first try. Once the attempts are exhausted the delivery is recorded as failed.

{% hint style="info" %}
**Failed deliveries live on the trigger.** Click the trigger's row to open its detail panel: the **Failed deliveries (N)** section lists each one with its route, status, attempts and error, and each entry's menu offers **Replay** and **Delete**.
{% endhint %}

| Field                | Range / options                                      | Default          |
| -------------------- | ------------------------------------------------------ | ---------------- |
| **Max attempts**     | 1-10. `1` means try once and never retry.             | 3                |
| **Backoff strategy** | `Exponential (1s, 2s, 4s…)`, `Linear`, `Fixed`        | Exponential      |
{% endstep %}

{% step %}
#### Set the advanced options, if you need them

| Field                 | Notes                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Webhook ID**        | Optional. Becomes part of the public webhook URL. Leave empty and one is generated.                                                      |
| **Authentication**    | **API Key (x-api-key)**, the default: callers must send an API key in the `x-api-key` header (the older `x-fastn-access-key` header is still accepted). **None (public)**: anyone with the URL can fire it. |
| **Execution mode**    | **Parallel**, the default: concurrent events run concurrently. **Sequential**: one at a time, in arrival order.                         |
| **Deduplication key** | Optional. A field in the incoming payload that uniquely identifies each event, so a retried delivery from the sender does not run the workflow twice. |
{% endstep %}

{% step %}
#### Create it, then hand out the URL

Select **Create trigger** (there is no Save button) and it joins the **Webhooks** list. Its row menu offers **Copy URL**, **Copy as cURL**, **Disable**, **Edit** and **Delete**: **Copy as cURL** is the fastest way to fire one by hand while you are debugging; with API key auth, the copied command sends an `x-api-key: <YOUR_API_KEY>` header for you to fill in.
{% endstep %}
{% endstepper %}

{% hint style="danger" %}
Only use **None (public)** when the sender genuinely cannot set a header, and pair it with a deduplication key and a workflow that validates its own payload.
{% endhint %}

{% hint style="success" %}
Sequential mode plus a deduplication key is the combination that makes a webhook-driven sync idempotent. Worth setting up front rather than after the first duplicate-record incident.
{% endhint %}
