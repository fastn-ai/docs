---
description: From an empty workspace to a workflow running on a real trigger.
---

# Quickstart: your first integration

This walks the shortest honest path. Budget about twenty minutes.

### 1. Describe what you want

Go to **Integrations → Agent** and click **New session**, or type straight into the prompt on Home.

<figure><img src="../.gitbook/assets/agent-home.jpg" alt="The agent's start screen with example integrations"><figcaption></figcaption></figure>

Write the integration the way you would explain it to a colleague:

> When a HubSpot deal moves to closed-won, create a customer and a draft invoice in QuickBooks, and post a line in our #sales Slack channel.

Name the systems, the trigger, and the fields that matter. The agent asks about anything ambiguous rather than guessing.

The **Approval mode** control under the message box decides how much it does unattended. Leave it on **Auto** while you are exploring.

### 2. Let it set up connectors and auth

The agent checks whether connectors exist for the systems you named, creates any that are missing, and handles authentication in the chat — API-key fields inline, or an OAuth form with client ID, secret and pre-filled scopes.

Anything it creates shows up under [Connectors](../build/connectors.md) afterwards, so you can inspect it.

### 3. Review the draft

The agent produces a workflow and opens the editor. Work through it in this order:

<figure><img src="../.gitbook/assets/workflow-editor-diagram.jpg" alt="The workflow editor showing the flow diagram"><figcaption>The Diagram tab renders the whole workflow as a node graph.</figcaption></figure>

1. **Diagram** — read the flow end to end. Decision branches show both paths, including skips and error routes.
2. **Contract** — check the input and output shapes.
3. **Connectors** — confirm the right actions are wired, and whether each connector is per-customer or workspace-level.
4. **Configuration** (left panel) — set the execution tier and timeout.

### 4. Test it

<figure><img src="../.gitbook/assets/workflow-test.jpg" alt="The Test tab with ctx.input and ctx.headers"><figcaption></figcaption></figure>

Open **Test**, click **Use contract** to populate a sample `ctx.input`, and hit **Run Live**. Test runs execute without saving, so you can iterate freely. They are deliberately not recorded in Activity → Executions.

If something is wrong, do not hand-edit — tell the agent. *"Skip deals under $500"* or *"Add error handling when QuickBooks is down"* and it rewrites the workflow, mappings and test cases together.

### 5. Publish and deploy

In the left panel, under **Publish & deploy**:

* **Publish snapshot** freezes the current code and configuration as an immutable version (v1, v2, …).
* **Deploy to environment** sends that version to an environment so it starts handling real events.

### 6. Attach a trigger

A workflow with no trigger only runs when you call it. Go to **Integrations → Triggers → Add trigger** and pick one:

<figure><img src="../.gitbook/assets/add-trigger-dialog.jpg" alt="The add trigger dialog offering webhook, schedule and app event"><figcaption></figcaption></figure>

For the HubSpot example, choose **App event**, select the HubSpot connector, and point it at your workflow. Full field-by-field detail is in [Triggers](../build/triggers.md).

### 7. Put it in front of customers

Open **Widgets**, click **Add** under INTEGRATIONS, and pick the integration you just built. Then use the **Embed** tab to drop it into your product — see [Embedding the widget](../embed/embedding.md).

### 8. Make failure loud

Go to **Activity → Alerts** and click **Turn on failure alerts**. It takes one click and sends an email the moment a run fails, plus a daily reliability summary. A sync that fails quietly for six hours is a support ticket you could have avoided.

{% hint style="success" %}
Done. From here, [Core concepts](concepts.md) explains the model underneath, [Workflows](../build/workflows.md) covers the editor in full, and [MCP gateway](../build/mcp-gateway.md) covers exposing the same integrations to an AI client.
{% endhint %}

{% hint style="info" %}
Deleted a connector or workflow by mistake while exploring? It is in [Settings → Trash](../manage/trash.md), restorable with its slug and history intact.
{% endhint %}
