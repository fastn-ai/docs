---
description: A trigger that fires when something changes in a connected app.
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

# App event triggers

**Build → Integrations → Triggers** → **App events** · [Open in Fastn](https://app.fastn.dev/integrations?tab=triggers)

An **app event trigger** runs your workflows when something changes in a connected app, such as a HubSpot deal moving or a GitHub pull request merging. You pick the event from the app's [connector](../connectors/README.md), and Fastn subscribes to it with the app for you. There is no URL to hand out and nothing is polled.

The trade is one extra thing to check. Because Fastn manages the subscription with the app, the subscription itself can fail, which the other two trigger types can't. See [Check the subscription](#check-the-subscription).

This page covers creating and configuring an app event trigger. To watch the events it receives, see [Operate → Triggers](../../operate/triggers/README.md).

{% hint style="info" %}
**Do this from your AI tool.** Fastn recommends connecting your preferred AI agent, such as Claude, Cursor or VS Code, to the [Fastn MCP server](../mcp-gateway/README.md) and using its tools to create app event triggers. For example, ask it: *"Run the sync-new-contacts workflow whenever a contact is created in HubSpot."* To connect your AI agent, see [Connect your AI tool](../mcp-gateway/README.md#open-the-connect-dialog), or the setup guide for [Claude](../mcp-gateway/claude.md), [Claude Code](../mcp-gateway/claude-code.md), [Cursor](../mcp-gateway/cursor.md), [VS Code](../mcp-gateway/vscode.md) or [any other MCP client](../mcp-gateway/README.md#how-your-ai-tool-connects).
{% endhint %}

### The App events list

The list has these columns: `Name`, `Connector`, `Type`, `Events`, `Status`, `Subscription`, `Routes`, `Created`, `Actions`.

* **`Status`:** Whether you have turned the trigger on.
* **`Subscription`:** Whether Fastn registered for the event with the app. It reads `Subscribed`, `Pending`, `Failed`, `Not subscribed`, `Unsubscribed` or `Shared` (sharing another trigger's provider webhook for the same events and connection).

The two are separate, so a trigger can be `Active` and still never fire.

The row menu holds **Copy ingest URL**, **Edit**, **Disable** (or **Enable** on a disabled trigger), **Retry Subscription** (only when the subscription is `Failed`) and **Delete**. When you delete the trigger, Fastn unsubscribes from the app.

### Create an app event trigger

The form shows one question at a time, and each answer reveals the next: name, connector, connection, event and routes. If nothing is connected for the connector yet, the form stops before the connection.

{% stepper %}
{% step %}
#### Name it

From **Add trigger**, choose **App event**, and give it a **Name** (required).
{% endstep %}

{% step %}
#### Choose the connector

**Connector** is required and searchable, for example `Cin7 Core`. You can't change it after the trigger is created, so choose carefully.
{% endstep %}

{% step %}
#### Connect the app, if needed

Without an active connection for that connector, the form stops here with *No active connection found for this connector. Connect first to use it as a trigger source.* Make the [connection](../connections/README.md) first, then continue.
{% endstep %}

{% step %}
#### Pick the connection

**Connection** is required: the authorized connection this trigger listens on. Like the connector, you can't change it after the trigger is created.
{% endstep %}

{% step %}
#### Pick the event

**Event** is required. The list has **Search events...**, and each event shows:

* **Type:** A `WEBHOOK` badge.
* **State:** `Registered` or `Not Subscribed`.
* **Event key:** The raw key, for example `Sale/Created`.
* **Payload Schema:** An expander that shows the data the event sends.
{% endstep %}

{% step %}
#### Add routes

Add at least one route. See [Routes](README.md#routes) for the **Workflow**, **Environment** and **Headers** fields.
{% endstep %}

{% step %}
#### Create it

Select **Create trigger** (there is no Save button), and the trigger joins the **App events** list. Then check its subscription, as below.
{% endstep %}
{% endstepper %}

### Check the subscription

Creating the trigger asks Fastn to register for the event with the app. That registration can fail on its own, after the form has closed without an error. Look at the new row's `Subscription` column before you consider the job done.

{% hint style="info" %}
**`Active` with `Subscription: Failed` means the trigger never fires.** Fastn couldn't register for events with the app, so no events arrive. Because `Status` still reads `Active`, the list looks healthy at a glance.
{% endhint %}

To recover, select **Retry Subscription** in the row menu. If it fails again, the problem is outside the trigger: check that the [connection](../connections/README.md) is still active and that its credential still has the scopes the event needs.

### What's next

* [Operate → Health](../../operate/health.md): see any customer's trigger that is not listening.
* [Events](../../operate/events.md): check that the app's events arrive.
