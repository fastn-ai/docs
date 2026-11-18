---
description: "Find out if fastn fits your use case: create a free account, connect your AI agent to fastn, and ask it. The agent will be able to guide you on how your integration can be implemented using Fastn's capabilities."
---

# Find out if fastn fits your use case

Your AI agent can tell you whether fastn fits what your product needs to do with your customers' apps. The agent will be able to guide you on how your integration can be implemented using Fastn's capabilities. It takes four steps and no call with fastn.

**No account yet? You can still ask.** With the [fastn plugin](#optional-the-fastn-plugin-for-claude), your agent can tell you whether fastn fits your use case and how it would work, based on what fastn offers. Create an account and connect it (steps 1 and 2) when you want the agent to look at your own setup and help you build it.

### Step 1: Create a fastn account

Sign up at [app.fastn.dev](https://app.fastn.dev/?signup=1). The Launch plan is free: no card and no sales call. See [pricing](https://fastn.ai/pricing) for the other plans.

### Step 2: Connect your AI agent to fastn

AI tools connect to other services through MCP, a standard way to give an AI tool access to an app. Add fastn to your AI tool as an MCP server at `https://mcp.fastn.dev/fastn-workspace`, then sign in with your fastn account. No API key is needed.

Your fastn user needs the **Developer** role or higher. If it has a lower one, an Owner or Admin of your fastn account can change it in **Settings → People**: see [Changing a role](../manage/people.md#changing-a-role). [Roles](../manage/roles.md) lists what each role can do.

The steps for each AI tool: [Claude](../build/mcp-gateway/claude.md), [Claude Code](../build/mcp-gateway/claude-code.md), [ChatGPT](../build/mcp-gateway/chatgpt.md), [Cursor](../build/mcp-gateway/cursor.md), [VS Code](../build/mcp-gateway/vscode.md), [Codex](../build/mcp-gateway/codex.md), and others in [Connect your AI tool (MCP)](../build/mcp-gateway/README.md).

Once connected, your agent gets fastn's tools and skills through that connection. There is nothing else to install.

### Step 3: Ask your agent about fastn

Describe your product and what it should do with your customers' apps. For example:

> We sell an invoicing tool. When a deal closes in our customer's CRM, we want to create an invoice in our product. Can fastn do this?

The agent asks what it still needs, one short question at a time: which apps, read or write, right away or on a schedule, and who connects the account.

### Step 4: Read the answer

The agent checks whether a connector exists for each app, which actions and events it has, and which unified APIs cover your apps. Then it answers what fits, what does not, and the setup steps in order. An answer looks like this (the details depend on your apps):

> **Fits, with one gap.** Two of your three CRMs can tell fastn when a deal closes. Each customer connects their own CRM inside your product, and fastn then creates the invoice in your product. The third CRM cannot send that signal, so fastn checks it every 15 minutes instead. Setup: 1. Connect your product to fastn. 2. Build the integration. 3. Add the fastn widget to your product.

When the agent cannot confirm something, it says so. It never asks for a password or API key in the chat.

### When something does not fit

The agent says so, offers a workaround if there is one, and helps you write a request to fastn. Send it from the fastn dashboard: **Help (?)** → **Contact support**. To talk it through with a person, use the same place and include the agent's summary.

### Optional: the fastn plugin for Claude

The fastn plugin (`connect`, from the [fastn Claude plugins](https://github.com/fastn-ai/fastn-claude-plugins) repository) adds the fastn skills and the fastn connection in one go. It works before you have an account.

* **Claude desktop app or claude.ai:** go to **Settings** → **Customize** → **Plugins** → **Add** → **Add marketplace**, paste `fastn-ai/fastn-claude-plugins`, select **Sync**, then turn on **fastn Connect**.
* **Claude Code:** run these two commands, then start a new session.

  ```
  /plugin marketplace add fastn-ai/fastn-claude-plugins
  /plugin install connect@fastn
  ```

To learn what each part of fastn does, read [Concepts](concepts.md).
