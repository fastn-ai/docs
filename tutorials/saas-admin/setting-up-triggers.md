---
description: >-
  Create webhook, schedule, and app event triggers under Build → Integrations →
  Triggers and route them to your workflows.
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

# Set up triggers

At the end, you have a trigger that starts one of your workflows on its own: when another app calls a URL, on a schedule, or when something changes in a connected app.

A trigger lives separately from the workflows it runs. You create it under **Build → Integrations → Triggers**, then route it to one or more workflows. For what triggers are and how routes work, see [Triggers](../../build/triggers/README.md).

{% hint style="info" %}
**Do this from your AI tool.** Fastn recommends connecting your preferred AI agent, such as Claude, Cursor or VS Code, to the [Fastn MCP server](../../build/mcp-gateway/README.md) and using its tools to create and test triggers. For example, ask it: *"Create a webhook trigger for the sync-new-contacts workflow and test it."* To connect your AI agent, see [Connect your AI tool](../../build/mcp-gateway/README.md#open-the-connect-dialog), or the setup guide for [Claude](../../build/mcp-gateway/claude.md), [Claude Code](../../build/mcp-gateway/claude-code.md), [Cursor](../../build/mcp-gateway/cursor.md), [VS Code](../../build/mcp-gateway/vscode.md) or [any other MCP client](../../build/mcp-gateway/README.md#how-your-ai-tool-connects).
{% endhint %}

### Before you start

* **Who this is for:** An Owner, Admin or Developer. Operators can pause, resume and replay triggers, but can't create them.
* **A published workflow** to route the trigger to. See [Test and release](../../build/workflows/lifecycle.md).
* **For an app event trigger:** A [connection](../../build/connections/README.md) to the app the event comes from.

{% hint style="info" %}
You can also ask your AI tool, through the [Fastn MCP server](../../build/mcp-gateway/README.md), or the [Fastn agent](../../build/agent/README.md), to create the trigger while it builds the workflow. See [Build a trigger with AI](../../build/triggers/README.md#build-a-trigger-with-ai).
{% endhint %}

### Steps

1. **Open the triggers.** Go to **Build → Integrations → Triggers** · [Open in Fastn](https://app.fastn.dev/integrations?tab=triggers).

   **You should see:** three tabs, **Webhooks**, **Schedulers** and **App events**, and an **Add trigger** button.

2. **Choose a type.** Select **Add trigger**, then choose **Webhook**, **Schedule** or **App event**. To pick one, see [Trigger types](../../build/triggers/README.md#trigger-types).

   **You should see:** the form for that type, starting with **Name**.

3. **Name the trigger.** Enter a **Name**, and a **Description** if the form offers one.

   **You should see:** the rest of the form. On an app event trigger, the form reveals each question after you answer the one before.

4. **Set what fires it.** Fill in the settings for your type:

   * **Webhook:** Set **Max attempts** and **Backoff strategy** for delivery. Under **Advanced options**, check **Authentication** and add a **Deduplication key** if the sender may send the same event twice. [Every webhook option](../../build/triggers/webhooks.md)
   * **Schedule:** Pick a mode (**Interval**, **Daily**, **Weekly**, **Monthly** or **Custom**), set the time, and set the **Timezone**. [Every schedule option](../../build/triggers/schedulers.md)
   * **App event:** Choose the **Connector**, the **Connection** and the **Event**. You can't change the connector or the connection later. [Every app event option](../../build/triggers/app-events.md)

   **You should see:** on a schedule in **Interval** mode, a live preview such as *Every 5 minutes*. On an app event, the event you picked, with its **Payload Schema**.

5. **Add a route.** Under **Routes**, pick the **Workflow** to run. Leave **Environment** on **test (latest published)** while you try it out, or pick a named environment such as `live`. To run more than one workflow, select **Add route** for each. See [Routes](../../build/triggers/README.md#routes).

   **You should see:** one route row per workflow, each with a workflow selected.

6. **Create the trigger.** Select **Create trigger**.

   **You should see:** the new trigger in its tab. On a webhook trigger, **Copy URL** in the row menu gives you the URL to hand to the sender. On an app event trigger, the `Subscription` column should read `Subscribed`. If it reads `Failed`, see [Check the subscription](../../build/triggers/app-events.md#check-the-subscription).

### What's next

* [Call a webhook trigger](../../operate/triggers/using-a-webhook-trigger.md): send a request to a webhook trigger from your backend.
* [Start an integration from your product's events](../../how-to/events-from-your-product.md): fire a webhook trigger when something happens in your product.
* [Logs](../../operate/README.md): watch the runs your trigger starts.
