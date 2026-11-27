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

Your AI agent can tell you whether Fastn fits your use case, and how you'd build it. You don't need a sales call, and you can start before you have a Fastn account.

### Choose how to start

* **Quickest, in any AI tool:** paste one line into your AI tool. See [Paste one line](#paste-one-line).
* **In Claude, without an account:** install the Fastn plugin. See [The Fastn plugin for Claude](#optional-the-fastn-plugin-for-claude).
* **Full setup:** create a Fastn account and connect your AI tool, so the agent can check your own workspace and help you build. Follow [steps 1 to 4](#step-1-create-a-fastn-account).

### Paste one line

Copy this line into your AI tool:

```
Fetch and execute the instructions to set me up for fastn from https://raw.githubusercontent.com/fastn-ai/fastn-claude-plugins/main/agent-setup/prompt.md
```

Your agent loads Fastn's setup instructions, then asks what your product needs to do. If your AI tool isn't connected to Fastn yet, the agent answers from Fastn's docs. If it is connected, the agent checks your own workspace. It brings up accounts only when you want to build. You can [read the instructions](https://github.com/fastn-ai/fastn-claude-plugins/blob/main/agent-setup/prompt.md) before you paste the line.

**You should see:** the agent asks what your product does, and what it should do with your customers' apps.

### Step 1: Create a Fastn account

Sign up at [app.fastn.dev](https://app.fastn.dev/?signup=1). The Launch plan is free: no card and no sales call. See [pricing](https://fastn.ai/pricing) for the other plans.

**You should see:** the Fastn dashboard.

### Step 2: Connect your AI agent to Fastn

AI tools connect to other services through MCP, a standard way to give an AI tool access to an app. Add Fastn to your AI tool as an MCP server at `https://mcp.fastn.dev/fastn-workspace`, then sign in with your Fastn account. No API key is needed.

The steps for each AI tool: [Claude](../build/mcp-gateway/claude.md), [Claude Code](../build/mcp-gateway/claude-code.md), [ChatGPT](../build/mcp-gateway/chatgpt.md), [Cursor](../build/mcp-gateway/cursor.md), [VS Code](../build/mcp-gateway/vscode.md), [Codex](../build/mcp-gateway/codex.md), and others in [Connect your AI tool (MCP)](../build/mcp-gateway/README.md).

Once connected, your agent gets Fastn's tools through that connection. There is nothing else to install.

**You should see:** Fastn's tools listed in your AI tool.

{% hint style="info" %}
**If you joined an existing Fastn account:** your Fastn user needs the **Developer** role or higher. An Owner or Admin of the account can change your role in **Settings → People**. See [Change a role](../manage/people.md#change-a-role), and [Roles](../manage/roles.md) for what each role can do.
{% endhint %}

### Step 3: Ask your agent about Fastn

Describe your product and what it should do with your customers' apps. For example:

> We sell an invoicing tool. When a deal closes in our customer's CRM, we want to create an invoice in our product. Can Fastn do this?

The agent asks what it still needs, one short question at a time: which apps, read or write, right away or on a schedule, and who connects the account.

**You should see:** the agent's first question about your use case.

### Step 4: Read the answer

The agent checks whether a connector exists for each app, which actions and events it has, and which unified APIs cover your apps. Then it answers what fits, what does not, and the setup steps in order. An answer looks like this (the details depend on your apps):

> **Fits, with one gap.** Two of your three CRMs can tell Fastn when a deal closes. Each customer connects their own CRM inside your product, and Fastn then creates the invoice in your product. The third CRM cannot send that signal, so Fastn checks it every 15 minutes instead. Setup: 1. Connect your product to Fastn. 2. Build the integration. 3. Add the Fastn widget to your product.

When the agent can't confirm something, it says so. It never asks for a password or API key in the chat.

### When something does not fit

The agent says so, offers a workaround if there is one, and helps you write a request to Fastn. Send it from the Fastn dashboard: **Help (?)** → **Contact support**. To talk it through with a person, use the same place and include the agent's summary.

### Optional: the Fastn plugin for Claude

The Fastn plugin (`connect`, from the [Fastn Claude plugins](https://github.com/fastn-ai/fastn-claude-plugins) repository) adds the Fastn skills and the Fastn connection in one go. It works before you have an account.

* **Claude desktop app or claude.ai:** go to **Settings** → **Customize** → **Plugins** → **Add** → **Add marketplace**, paste `fastn-ai/fastn-claude-plugins`, select **Sync**, then turn on **Fastn Connect**.
* **Claude Code:** run these two commands, then start a new session.

  ```
  /plugin marketplace add fastn-ai/fastn-claude-plugins
  /plugin install connect@fastn
  ```

To learn what each part of Fastn does, read [Core concepts](concepts.md).
