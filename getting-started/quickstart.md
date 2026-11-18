---
description: From an empty workspace to a workflow running on a real trigger.
---

# Quickstart: your first integration

This is the shortest path from an empty workspace to a running workflow. It takes about 20 minutes.

### Before you start

This guide is for a developer or admin at the SaaS company that embeds fastn. You need:

* **A fastn organization and a role that can build workflows.** Owner, Admin and Developer can create, publish and deploy workflows and set up alerts. Operator and Viewer cannot. See [Roles](../manage/roles.md).
* **Accounts in the systems you want to connect.** The example on this page uses HubSpot, QuickBooks and Slack. You need to be able to sign in to each one, or have an API key for it, so fastn can connect on your behalf. The trigger in step 6 needs an active HubSpot connection.

### 1. Describe what you want

Open **Build with AI** in the sidebar, or type what you want into the **What should your customers be able to do?** prompt on Home. Both land on the same screen.

The pane states the contract plainly:

> Describe what you need in plain words. fastn's agent picks the connectors, drafts the workflow, and shows you the diff before anything runs.

If you would rather start from a shape than a blank page, tap one of the example starter prompts beneath the box (these are seeded suggestions and vary by workspace) and edit it to fit.

Otherwise, write the integration the way you would explain it to a colleague:

> When a HubSpot deal moves to closed-won, create a customer and a draft invoice in QuickBooks, and post a line in our #sales Slack channel.

Name the systems, the trigger, and the fields that matter. The agent asks about anything ambiguous rather than guessing.

The **Approval mode** chip under the message box decides how much it does unattended: **Auto** is the default and does not ask; **Manual** asks before any create, update or delete. Leave it on Auto while you are exploring.

**You should see:** the agent replying in the chat, with questions about anything your description left ambiguous.

### 2. Let it set up connectors and auth

The agent checks whether connectors exist for the systems you named, creates any that are missing, and handles authentication in the chat: API-key fields inline, or an OAuth form with client ID, secret and pre-filled scopes.

Anything it creates shows up under [Connectors](../build/connectors/README.md) afterwards, so you can inspect it.

**You should see:** a connector for each system you named on the **Connectors** tab of **Build → Integrations**.

### 3. Review the draft

The agent produces a workflow and opens the editor: configuration on the left, the tool tabs on the right, and the code between them where code editing is turned on for your organization (it is off by default; see [The workflow editor](../build/workflows/the-editor.md)).

Work through it in this order:

1. **The code.** Where code editing is on, the middle column holds `<slug>.js`, a JavaScript module exporting `export default async function(ctx)`. This is the workflow; everything else on the screen describes, tests or deploys it. Where it is off, read the **Diagram** tab instead to see what the agent wrote.
2. **Diagram → Flow.** A read-only picture that AI generates from that code, with node kinds `TRIGGER`, `READ`, `PROCESS`, `WRITE`, `DECISION` and `DONE`. You cannot edit the graph. It regenerates when you open it after the code has changed, so it can lag a save for a moment. To refresh it right away, click the refresh icon (**Regenerate docs**).
3. **Contract.** Check the input and output shapes.
4. **Connectors.** The list is extracted from the `fastn.connectors.X.Y(…)` calls in your code when you save. Confirm the right actions are wired, and whether each connector is marked **Per customer**.
5. **Configuration** (left panel). For this example, set the tier to **Standard**. **Instant**, the default, is capped at 25 seconds and is for calls where something waits on the result.

**You should see:** the editor open on your new workflow, with **Standard** selected as its tier.

### 4. Test it

Open **Test**, click **Use contract** to populate a sample `ctx.input`, and choose a mode beside the run button. The button's label follows the mode: **Run Live**, **Run Partial Mock** or **Run Fully Mock**.

{% hint style="info" %}
Test with **Fully Mock** first. It serves every connector call from stored mock stubs, so nothing reaches HubSpot, QuickBooks or Slack. **Partial Mock** runs live wherever the connector has an active connection and mocks only the connectors that are not connected, so it can still write to a connected system. **Run Live** calls the real systems, and so do test API keys: a test key is a separate credential, not a sandbox (see [API keys](../manage/api-keys.md)).
{% endhint %}

If something is wrong, tell the agent rather than patching by hand. For example, type "Skip deals under $500" or "Add error handling when QuickBooks is down", and the agent rewrites the code, mappings and test cases together.

**You should see:** the run's result under the run button, with a **Trace** tab listing each step and an **Output** tab holding what the workflow returned.

### 5. Publish and deploy

In the left panel, under **PUBLISH & DEPLOY**:

* **Publish snapshot** freezes the current code and configuration as a version. The workflows list numbers them in its **Latest** column (`v1`, `v2`, …), and shows a dash there (tooltip "No published version yet.") until the first one exists.
* **Deploy to environment** sends that version to an environment so it starts handling real events.

Until a snapshot is published, the workflow's **Status** reads `Unpublished` and every call returns `WORKFLOW_NOT_PUBLISHED`.

**You should see:** the message "Published v1. Deploy it to make it live." after publishing, and "Deployed to <environment> successfully" after deploying.

### 6. Attach a trigger

A workflow with no trigger only runs when you call it. Go to **Build → Integrations → Triggers → Add trigger** and pick one:

<figure><img src="../.gitbook/assets/add-trigger-dialog.jpg" alt="The Add a trigger dialog, headed What should start the workflow?, with Webhook, Schedule and App event as three rows, each explained in a sentence and ending in an arrow"><figcaption>Three trigger types. A workflow with no trigger only runs when you call it.</figcaption></figure>

For the HubSpot example, choose **App event**. The form is progressive: name it, pick the HubSpot connector, then pick a connection and an event, then add a route pointing at your workflow. Two things to know before you start: the connector cannot be changed after the trigger is created, and you cannot get past the connector step without an active connection. Without one the form stops you:

> No active connection found for this connector. Connect first to use it as a trigger source.

Full field-by-field detail is in [Triggers](../build/triggers/README.md).

**You should see:** your new trigger listed on the **Triggers** tab.

### 7. Put it in front of customers

Open **Embed → Widget**, click **Add** under INTEGRATIONS, and pick the integration you just built. Then use the **Embed** tab to drop it into your product. See [Embedding the widget](../embed/embedding/README.md).

**You should see:** the integration listed under INTEGRATIONS in your widget.

### 8. Turn on failure alerts

Go to **Operate → Health → Alerts** and click **Turn on failure alerts**. One click turns on the two alerts most teams need: an email the moment a run fails (it goes out within about a minute) and a daily reliability check. For custom and threshold alerts, see [Alerts](../operate/alerts.md).

**You should see:** the **Sync failure notifications** card reading **On**.

{% hint style="info" %}
Deleted a connector or workflow by mistake while exploring? It is in [Settings → Trash](../manage/trash.md), restorable with its slug and history intact. Trash appears in the Settings sidebar for Owners, Admins and Developers alike, at `/settings/trash`.
{% endhint %}

## What you built

* A workflow, drafted by the agent from a plain-language description, that reads from HubSpot and writes to QuickBooks and Slack.
* Connectors and connections for each system, which you can reuse in later workflows.
* A published, deployed version of that workflow, started by a HubSpot app event.
* A widget entry your customers can use to turn the integration on, and an alert that tells you when a run fails.

## Next steps

* [Core concepts](concepts.md) explains the model underneath connectors, workflows, triggers and installations.
* [Workflows](../build/workflows/README.md) covers the editor, its tabs and the workflow lifecycle in full.
* [Connect your AI tool (MCP)](../build/mcp-gateway/README.md) covers exposing the same integrations to an AI client.
