---
description: Describe an integration, let an AI agent build it, and run its test. About five minutes.
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

In this quickstart, you describe an integration in plain words, an AI agent builds it, and you test it without touching real data. It takes about five minutes and needs no code.

By the end, you'll have a workflow that posts each new HubSpot contact to a Slack channel, tested and ready to publish.

### Before you start

* **A Fastn account.** Sign up at [app.fastn.dev](https://app.fastn.dev). The free Launch plan is enough.
* **An account in each app you name,** for example HubSpot and Slack. You sign in to them during step 2.
* **An AI agent to build with.** Fastn recommends your own AI tool, such as Claude or Cursor, connected to the [Fastn MCP server](../build/mcp-gateway/README.md). It works on every plan and uses no Fastn AI credits. On a paid plan (Scale or Enterprise), you can use the Fastn agent in the dashboard instead. It uses Fastn AI credits.

### 1. Describe the integration

{% tabs %}
{% tab title="Your AI tool (every plan)" %}
Connect your AI tool once: in the Fastn dashboard, click **Connect your AI tool** in the top bar and follow the steps for your tool. For details, see [Fastn MCP server](../build/mcp-gateway/README.md).

<figure><img src="../.gitbook/assets/screens/connect-your-ai-tool.webp" alt="The Connect your AI tool dialog: Claude recommended with Add to Claude, tiles for other AI tools, the MCP server URL https://mcp.fastn.dev/fastn-workspace with Copy, and OAuth 2.0 sign-in with no API key"><figcaption>Click <strong>Connect your AI tool</strong> in the top bar to open this dialog.</figcaption></figure>

Then, in a new chat, describe what should happen, naming the apps and what starts it:

> Using Fastn, when a new contact is created in HubSpot, post their name and email in our #sales Slack channel.
{% endtab %}

{% tab title="Fastn agent (paid plans)" %}
Type into the **What should your customers be able to do?** box on **Home**, or open **Integrations → Create integration → Build with fastn agent**. Describe what should happen, naming the apps and what starts it:

> When a new contact is created in HubSpot, post their name and email in our #sales Slack channel.

Leave the **Approval mode** chip on **Auto**. The agent then works without stopping to ask before each step.
{% endtab %}
{% endtabs %}

**You should see:** the agent replies with a plan: the connectors to use and the workflow to write.

### 2. Sign in to the apps

The agent checks that Fastn has a connector for each app, then asks you to sign in to any account it needs:

* **Your AI tool** gives you a link. Open it and sign in to the app in your browser. Never paste passwords or API keys into the chat.
* **The Fastn agent** asks you to sign in from the chat.

**You should see:** each app marked as connected, and the agent moving on to build.

### 3. Let the agent build and test

The agent writes the workflow, creates test cases for it, and runs them. Your AI tool may first ask you to approve the field mappings and test cases on a review page.

**You should see:** the workflow in **Build → Integrations → Workflows** ([Open in Fastn](https://app.fastn.dev/integrations?tab=workflows)), with its test cases listed.

### 4. Run it without touching real data

Open the workflow, then:

1. On the **Test** tab, click **Use contract** to fill in a sample input.
2. Set the mode beside the run button to **Fully Mock**.
3. Click **Run Fully Mock**.

A fully mocked run uses stored sample responses instead of calling the apps, so nothing is written to HubSpot or Slack.

**You should see:** the run's output, with each step and its result.

{% hint style="warning" %}
Only **Fully Mock** keeps every call away from the apps. The other modes can write to your real HubSpot and Slack. See [Test a workflow](../build/workflows/testing.md#run-a-quick-test).
{% endhint %}

If something is wrong, tell the agent in the chat, for example *"Only post contacts that have an email"*. It updates the workflow and its tests together.

**You've built and tested your first integration.** Nothing runs for real until you publish it and attach a trigger.

### What's next

* **Publish and deploy it:** ask your AI tool to publish the workflow. Deploying to `live` from your AI tool needs your approval in the browser. See [Test and release](../build/workflows/lifecycle.md).
* **Run it on real events:** attach a webhook, schedule or app event trigger. See [Triggers](../build/triggers/README.md).
* **Offer it to your customers:** add it to your widget and put the widget in your product. See [Build your widget](../tutorials/saas-admin/building-your-widget.md) and the [Embedding quickstart](../tutorials/developer/embedding-quickstart.md).
* **Get told when it fails:** in **Operate → Health → Alerts** ([Open in Fastn](https://app.fastn.dev/health?tab=alerts)), click **Turn on failure alerts**. See [Alerts](../operate/alerts.md).
