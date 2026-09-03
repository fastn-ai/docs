---
description: A trigger that fires when something changes in a connected system.
---

# App event triggers

An app event trigger fires when something changes in a connected system — a HubSpot deal moves, a GitHub PR merges.

**Columns:** `Name`, `Tenant`, `Connector`, `Type`, `Events`, `Status`, `Subscription` (`Subscribed` or `Failed`), `Routes`, `Created`, `Actions`. The row menu offers **Copy ingest URL**.

### Create an app event trigger

The form is progressive — each answer reveals the next question — and it needs five things, not two.

{% stepper %}
{% step %}
#### Name it

From **Add trigger**, choose **App event**, and give it a **Name** (required).

<figure><img src="../../.gitbook/assets/app-event-trigger-form.jpg" alt="The new app event trigger form"><figcaption></figcaption></figure>
{% endstep %}

{% step %}
#### Choose the connector

**Connector** is required, searchable, and **immutable after the trigger is created** — choose carefully, because you cannot change it later.
{% endstep %}

{% step %}
#### Clear the connection gate

Without a live connection for that connector the form stops here: *No active connection found for this connector. Connect first to use it as a trigger source.* Make the [connection](../connections/README.md) first, then continue.
{% endstep %}

{% step %}
#### Pick the connection

**Connection** is required — which authorised link this trigger listens on.
{% endstep %}

{% step %}
#### Pick the event

**Event** is required: a radio list with **Search events...**, a `WEBHOOK` badge, a `Registered` or `Not Subscribed` state, the raw event key, and a **Payload Schema** expander so you can see what will arrive.
{% endstep %}

{% step %}
#### Add routes

**Routes** are required, and the same shape as a webhook's, minus the JSON payload field.
{% endstep %}
{% endstepper %}

App events are the cleanest option when the connector supports them — no URL to hand out, no polling, and fastn manages the subscription with the upstream provider on your behalf. The subscription state is visible in the list's `Subscription` column.
