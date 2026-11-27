---
description: Ask your AI agent whether Fastn fits your use case, and how you'd build it. No sales call needed, and you can start before you have an account.
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

# Find out if Fastn fits your use case

Your AI agent can tell you whether Fastn fits your use case, and how you'd build it. You don't need a sales call.

There are two ways to start:

* **[Without a Fastn account](#without-a-fastn-account):** paste one line into any AI tool. Your agent designs a solution for your use case, based on what Fastn can do.
* **[With a Fastn account](#with-a-fastn-account):** connect your AI tool to Fastn. Your agent also reviews your workspace and anything you've already set up, builds that into the solution, and helps you build it.

Then [ask your agent about your use case](#ask-your-agent-about-your-use-case).

### Without a Fastn account

1. Open a new chat in your AI tool.
2. Paste this line and send it:

   ```
   Fetch and execute the instructions to set me up for fastn from https://raw.githubusercontent.com/fastn-ai/fastn-claude-plugins/main/agent-setup/prompt.md
   ```

Your agent loads Fastn's setup instructions and asks about your use case. You can [read the instructions](https://github.com/fastn-ai/fastn-claude-plugins/blob/main/agent-setup/prompt.md) before you paste the line. When you're ready to build, create an account and connect, as described in the next section.

**You should see:** the agent asks what your product does, and what it should do with your customers' apps.

### With a Fastn account

Connect your AI tool to Fastn, so your agent can review your workspace, such as the connectors and connections you already have, and help you build the solution.

1. **Create a Fastn account.** Sign up at [app.fastn.dev](https://app.fastn.dev/?signup=1). The Launch plan is free, with no card needed. See [pricing](https://fastn.ai/pricing) for the other plans.
2. **Add the Fastn MCP server to your AI tool.** MCP is a standard way to give an AI tool access to an app. Use this server URL:

   ```
   https://mcp.fastn.dev/fastn-workspace
   ```

   The steps for each AI tool: [Claude](../build/mcp-gateway/claude.md), [Claude Code](../build/mcp-gateway/claude-code.md), [ChatGPT](../build/mcp-gateway/chatgpt.md), [Cursor](../build/mcp-gateway/cursor.md), [VS Code](../build/mcp-gateway/vscode.md), [Codex](../build/mcp-gateway/codex.md), and [others](../build/mcp-gateway/README.md).
3. **Sign in with your Fastn account** when your AI tool asks. No API key is needed, and there is nothing else to install.

**You should see:** Fastn's tools listed in your AI tool.

{% hint style="info" %}
**If you joined an existing Fastn account:** your Fastn user needs the **Developer** role or higher. An Owner or Admin of the account can change your role in **Settings → People**. See [Change a role](../manage/people.md#change-a-role), and [Roles](../manage/roles.md) for what each role can do.
{% endhint %}

### Ask your agent about your use case

1. Describe your product and what it should do with your customers' apps. For example:

   > We sell an invoicing tool. When a deal closes in our customer's CRM, we want to create an invoice in our product. Can Fastn do this?
2. Answer the agent's questions. It asks one short question at a time: which apps, read or write, right away or on a schedule, and who connects the account.
3. Read the answer. The agent checks whether Fastn has a connector for each app, which actions and events it has, and which unified APIs cover your apps. Then it designs a solution: what fits, what doesn't, and the setup steps in order.

An answer looks like this (the details depend on your apps):

> **Fits, with one gap.** Two of your three CRMs can tell Fastn when a deal closes. Each customer connects their own CRM inside your product, and Fastn then creates the invoice in your product. The third CRM cannot send that signal, so Fastn checks it every 15 minutes instead. Setup: 1. Connect your product to Fastn. 2. Build the integration. 3. Add the Fastn widget to your product.

When the agent can't confirm something, it says so. It never asks for a password or API key in the chat.

### When something doesn't fit

The agent says so, offers a workaround if there is one, and helps you write a request to Fastn. Send it from the Fastn dashboard: **Help (?)** → **Contact support**. To talk it through with a person, use the same place and include the agent's summary.

To learn what each part of Fastn does, read [Core concepts](concepts.md).
