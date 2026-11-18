---
description: "Find out if fastn fits your use case: create a free account, connect your AI agent to fastn through MCP, and ask it. It checks your live workspace and tells you what fits, what does not, and how to set it up."
---

# Find out if fastn fits your use case

Your AI agent can tell you whether fastn fits what your product needs to do with your customers' apps. It checks a real fastn workspace, so the answer is based on what is really there, not on a guess. It takes four steps and no call with fastn.

### Step 1: Create a fastn account

Sign up at [app.fastn.dev](https://app.fastn.dev/?signup=1). The Launch plan is free: no card and no sales call. See [pricing](https://fastn.ai/pricing) for the other plans.

### Step 2: Connect your AI agent to your fastn workspace

Add fastn to your AI tool as an MCP server at `https://mcp.fastn.dev/fastn-workspace`, then sign in with your fastn account. No API key is needed. You need the **Developer** role or above.

The steps for each tool: [Claude](../build/mcp-gateway/claude.md), [Claude Code](../build/mcp-gateway/claude-code.md), [ChatGPT](../build/mcp-gateway/chatgpt.md), [Cursor](../build/mcp-gateway/cursor.md), [VS Code](../build/mcp-gateway/vscode.md), [Codex](../build/mcp-gateway/codex.md), and others in [Connect your AI tool (MCP)](../build/mcp-gateway/README.md).

Once connected, your agent gets fastn's tools and skills from the MCP server itself. There is nothing else to install.

### Step 3: Ask your agent about fastn

Describe your product and what it should do with your customers' apps. For example:

> We sell an invoicing tool. When a deal closes in our customer's CRM, we want to create an invoice in our product. Can fastn do this?

The agent asks what it still needs, one short question at a time: which apps, read or write, right away or on a schedule, and who connects the account.

### Step 4: Read the answer

The agent checks your live workspace: whether a connector exists for each app, which actions and events it has, and which unified APIs cover your apps. Then it answers what fits, what does not, and the setup steps in order. An answer looks like this (the details depend on your apps and workspace):

> **Fits, with one gap.** Two of your three CRMs have a connector with a "deal closed" event (checked). Each customer connects their own CRM through the widget, and an app event trigger starts a workflow that creates the invoice in your product. The third CRM lists no such event, so a schedule trigger checks it every 15 minutes instead. Setup: 1. Connect your product. 2. Build the workflow. 3. Add the widget to your product.

It says **supported** only for what it checked. Anything it could not check is marked **not checked**. It never asks for a password or API key in the chat.

### When something does not fit

The agent says so, offers a workaround if there is one, and helps you write a request to fastn. Send it from the dashboard: **Help (?)** → **Contact support**. To talk it through with a person, use the same place and include the agent's summary.

### Optional: other ways in

Not needed if you followed the steps above.

* **Claude plugin.** In Claude Code, install the `connect` plugin from the [fastn Claude plugins](https://github.com/fastn-ai/fastn-claude-plugins) repository. It adds the skill and the MCP connection in one go:

  ```
  /plugin marketplace add fastn-ai/fastn-claude-plugins
  /plugin install connect@fastn
  ```
* **No MCP at all.** Paste this at the start of a chat in any AI tool. Without a connection it cannot check anything, so every answer is **not checked**:

  ```
  You are a fastn solution architect. fastn lets a SaaS product offer integrations
  with the apps its customers use, set up by the customers themselves.
  Ask one short question at a time about the user's product, the apps involved,
  read or write, when it should run, and who connects the account.
  Use only facts from https://docs.fastn.ai. Never guess limits or prices.
  Mark every answer "not checked", and say that connecting fastn as an MCP server
  at https://mcp.fastn.dev/fastn-workspace would let you check the workspace.
  Never ask for a password, API key or secret in the chat.
  Answer with: fits / fits with gaps / does not fit today, a short summary, the
  fastn pieces for each need, the gaps with workarounds, and the setup order.
  ```

To see what each fastn piece does, read [Concepts](concepts.md).
