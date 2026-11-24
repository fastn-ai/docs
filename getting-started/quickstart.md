---
description: Describe an integration, let the fastn agent build it, and run its test. About five minutes.
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

# Quickstart: your first integration

In this quickstart you describe an integration in plain words, the fastn agent builds it, and you run its test without touching real data. It takes about five minutes.

### Before you start

* A fastn account. Sign up at [app.fastn.dev](https://app.fastn.dev). The Launch plan is free.
* An account in each app you name, for example Slack. The agent asks you to sign in to it.

### 1. Describe the integration

Open **Build → Build with AI**, or type into the **What should your customers be able to do?** box on **Home**. Describe what should happen, naming the apps and what starts it:

> When a new contact is created in HubSpot, post their name and email in our #sales Slack channel.

Leave the **Approval mode** chip on **Auto**. The agent then works without stopping to ask before each step.

**You should see:** the agent replies with a plan: the connectors it will use and the workflow it will write.

### 2. Sign in to the apps

The agent checks that a connector exists for each app and asks you to connect any account it needs, in the chat: a form for an API key, or a sign-in window for OAuth.

**You should see:** each app marked as connected in the chat, and the agent moving on to build.

### 3. Let the agent build and test

The agent writes the workflow, generates test cases and runs them. When it finishes, it opens the workflow editor.

**You should see:** the workflow in the editor, with its test cases listed.

### 4. Run it without touching real data

Open the **Test** tab and click **Use contract** to fill in a sample input. Set the mode beside the run button to **Fully Mock**, then click **Run Fully Mock**. A fully mocked run uses stubs instead of calling the apps, so nothing is written to HubSpot or Slack.

**You should see:** the run's output, with each step and its result.

If something is wrong, tell the agent in the chat, for example *"Only post contacts that have an email"*. It updates the workflow and its tests together.

{% hint style="success" %}
You have built and tested your first integration. Nothing runs for real until you publish it and attach a trigger.
{% endhint %}

### Next steps

* **Publish and deploy it.** Until a version is published, every call returns `WORKFLOW_NOT_PUBLISHED`. See [Test and release](../build/workflows/lifecycle.md).
* **Run it on real events.** Attach a webhook, schedule or app event trigger. See [Triggers](../build/triggers/README.md).
* **Offer it to your customers.** Add it to your widget and embed the widget in your product. See [Build your widget](../tutorials/saas-admin/building-your-widget.md) and the [embedding quickstart](../tutorials/developer/embedding-quickstart.md).
* **Get told when it fails.** In **Health → Alerts**, click **Turn on failure alerts**. See [Alerts](../operate/alerts.md).
* **Build from your own AI tool instead.** Connect Claude or Cursor to the [fastn MCP server](../build/mcp-gateway/README.md) and build the same way from your chat.
