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

First, give your agent access to Fastn in one of three ways:

| Way | Works in | Fastn account | What your agent can do |
| --- | --- | --- | --- |
| [Paste a setup line](#paste-a-setup-line) | Any AI tool | Not needed | Answer from Fastn's docs |
| [Install the Fastn plugin](#install-the-fastn-plugin-for-claude) | Claude and Claude Code | Not needed | Answer from Fastn's docs, and check your workspace once you sign in |
| [Connect to the Fastn MCP server](#connect-your-ai-tool-to-fastn) | Any AI tool that supports MCP | Needed (free plan) | Check your own workspace, and help you build |

Then [ask your agent about your use case](#ask-your-agent-about-your-use-case).

### Paste a setup line

The quickest way. It works in any AI tool.

1. Open a new chat in your AI tool.
2. Paste this line and send it:

   ```
   Fetch and execute the instructions to set me up for fastn from https://raw.githubusercontent.com/fastn-ai/fastn-claude-plugins/main/agent-setup/prompt.md
   ```

Your agent loads Fastn's setup instructions. If your AI tool isn't connected to Fastn, the agent answers from Fastn's docs. If it is connected, it checks your workspace. It brings up accounts only when you want to build. You can [read the instructions](https://github.com/fastn-ai/fastn-claude-plugins/blob/main/agent-setup/prompt.md) before you paste the line.

**You should see:** the agent asks what your product does, and what it should do with your customers' apps.

### Install the Fastn plugin for Claude

The Fastn plugin adds Fastn's skills and connection to Claude in one go. It comes from the [Fastn Claude plugins](https://github.com/fastn-ai/fastn-claude-plugins) repository.

**In the Claude desktop app or claude.ai:**

1. Go to **Settings** → **Customize** → **Plugins**.
2. Select **Add** → **Add marketplace**, paste `fastn-ai/fastn-claude-plugins`, and select **Sync**.
3. Turn on **Fastn Connect**.
4. Open a new chat.

**In Claude Code:**

1. Run these two commands:

   ```
   /plugin marketplace add fastn-ai/fastn-claude-plugins
   /plugin install connect@fastn
   ```
2. Start a new session.

**You should see:** the Fastn plugin listed among your plugins.

### Connect your AI tool to Fastn

The full setup. Your agent can then check your own workspace, such as the connectors and connections you have, and help you build once you're ready.

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
3. Read the answer. The agent checks whether Fastn has a connector for each app, which actions and events it has, and which unified APIs cover your apps. Then it tells you what fits, what doesn't, and the setup steps in order.

An answer looks like this (the details depend on your apps):

> **Fits, with one gap.** Two of your three CRMs can tell Fastn when a deal closes. Each customer connects their own CRM inside your product, and Fastn then creates the invoice in your product. The third CRM cannot send that signal, so Fastn checks it every 15 minutes instead. Setup: 1. Connect your product to Fastn. 2. Build the integration. 3. Add the Fastn widget to your product.

When the agent can't confirm something, it says so. It never asks for a password or API key in the chat.

### When something doesn't fit

The agent says so, offers a workaround if there is one, and helps you write a request to Fastn. Send it from the Fastn dashboard: **Help (?)** → **Contact support**. To talk it through with a person, use the same place and include the agent's summary.

To learn what each part of Fastn does, read [Core concepts](concepts.md).
