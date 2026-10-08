---
description: "The Webhook config tab: how fastn subscribes to an app's events for each customer, the config table, and every field of the config form."
---

# Webhook config

A **webhook config** tells fastn how to subscribe to an app's events on behalf of each customer, so that an [app event trigger](../triggers/app-events.md) can start a workflow when something happens in the app. You set it up once per connector; every customer who connects then gets the subscription automatically.

> Tell fastn how to subscribe to HubSpot's events on behalf of each customer, so a trigger can fire when something happens there.

### How it works

1. A customer connects to the connector.
2. fastn runs the config's **Subscribe** code with that customer's connection. The code registers a webhook with the app that points at fastn.
3. The app sends events to fastn. fastn checks the request (see [Webhook verification](#webhook-verification)), works out which customer and which event it is, and fires the matching app event triggers.
4. When the customer disconnects, fastn runs the **Unsubscribe** code to remove the webhook.
5. For apps whose subscriptions expire, fastn runs the **Renew** code before they do.

### The config table

<figure><img src="../../.gitbook/assets/connector-tab-webhook-config.webp" alt="The HubSpot Webhook config tab with a New config button and a table with columns Type, Events, Registered, Subscription, Unsubscription, Created and Actions; one row: App, 28 events, 15/28, Defined, Defined, Jun 2, 2026"><figcaption>HubSpot has one config of type App covering 28 events.</figcaption></figure>

| Column | Meaning |
| --- | --- |
| **Type** | **App**: one webhook for the whole app. **Event Webhook**: one webhook per event. A **Hidden** badge means the config is switched off as a trigger source. |
| **Events** | How many events the config declares. |
| **Registered** | How many of those events are registered, for example `15/28`. Green when all are registered, amber when only some are. |
| **Subscription** / **Unsubscription** | `Defined` when the config has that code, `—` when it does not. |
| **Created** | When the config was created. |
| **Actions** | **Edit** and **Delete**, on connectors your workspace owns. Empty on managed connectors. |

Until a connector has a config, the tab reads:

<figure><img src="../../.gitbook/assets/connector-webhook-config-empty.webp" alt="The AbstractAPI Holidays Webhook config tab with a New config button and the empty state No webhook config yet: Until one exists, customers of this connector can be polled but cannot be notified. Most providers support one webhook for the whole app"><figcaption>Without a config, workflows can only poll this app.</figcaption></figure>

> No webhook config yet · Until one exists, customers of this connector can be polled but cannot be notified. Most providers support one webhook for the whole app.

{% hint style="info" %}
Webhook configs on **managed** connectors are maintained by fastn and are read-only in your workspace. **New config** opens the form below only on connectors your workspace owns.
{% endhint %}

### The config form

**New config** opens the form; **Edit** on a row opens the same form filled in.

#### General

| Field | Meaning |
| --- | --- |
| **Available as a trigger source** | On: the connector appears in the list of connectors you can pick for an app event trigger. Off: it is hidden there, but inbound webhooks and existing triggers keep working. |
| **Type** | **One webhook for the whole app**: *The provider sends every customer event to one URL and fastn routes it.* **One webhook per event**: *The provider registers a separate webhook for each event you subscribe to.* |
| **Auth provider** | *(App type only.)* *Which credential fastn uses to register the subscription.* |
| **Webhook URL** | *(App type only, once an auth provider is chosen.)* The fastn URL to give the app. *This URL is shared across all events for this connector.* |
| **Event key** | *(App type only.)* *The field in the incoming payload that says what happened. fastn reads it to decide which trigger to fire.* For example `event_type`. |

#### Code: Subscribe, Unsubscribe, Renew

> Three snippets: how to subscribe, how to stop, and how to renew.

Each snippet is JavaScript, for example `return await fastn.http.post(...)`.

| Snippet | When it runs |
| --- | --- |
| **Subscribe** | *Runs when a customer connects. Register the webhook and return its id.* |
| **Unsubscribe** | *Runs when they disconnect. Remove the webhook you registered.* |
| **Renew** | *Runs before the subscription expires, for providers that time out.* |

**Execution Input (JSON)** lets you test-run a snippet from the form with sample input before saving.

#### Events

The list of events the config can deliver. Each event has an **Event ID** (the app's own name for it, for example `invoice.created`), a **Label** and an optional **Description**. These are the events a user picks from when creating an app event trigger on this connector.

#### Inputs

> Define input parameters for the subscription code. `webhookUrl` and `event` are always auto-provided.

Each input has a **Key** and a **Default value**, and can be hidden.

#### Get User Account Action

Used when one webhook carries events for many customers (the **App** type). It tells fastn how to match an incoming event to the right customer:

* **Select an action**: an action that returns the customer's account, run against their connection when they set up an app trigger.
* **Label path** and **Value path**: dotted paths into that action's response, for example `data.response.user` and `data.response.user_id`. The value becomes the trigger's account ID.
* **Mapped to**: the field in the incoming webhook payload that must equal that account ID for the event to reach this customer's trigger, for example `portalId`.

#### Webhook verification

> How inbound webhook requests are authenticated and how URL-verification handshakes (e.g. Slack `url_verification`) are answered.

| Method | Use it when |
| --- | --- |
| **None — accept all requests** | The app does not sign its webhooks. |
| **HMAC signature** | The app signs each request with a shared secret. Set **Signature Header** (for example `x-slack-signature`), **Algorithm** (for example `sha256`), **Signature Prefix** (for example `v0=` or `sha256=`), **Signature Format**, **Signing Payload**, and optionally **Timestamp Header** and **Max Timestamp Age (ms)** (for example `300000`) to reject replayed requests. |
| **Verification token (Notion-style)** | The app sends a one-time token when the subscription is created. fastn answers it, stores the token as **Captured Token**, and uses it to verify later events. For Notion, paste the captured token into Notion under **Webhooks → Verify** to activate the subscription. |
| **Challenge-response only** | The app checks the URL with a challenge request. Set **Trigger Field** and **Trigger Value** (for example `type` = `url_verification`) and **Response Field** (for example `challenge`), the field fastn echoes back. |

The shared secret for HMAC is the `client_secret` of the connector's auth provider.

### Related

* [App event triggers](../triggers/app-events.md): using a connector's events to start a workflow.
* [Auth methods and providers](auth-methods.md): the provider whose credential registers the subscription.
