---
description: "Instructions for an AI agent: set the user up for fastn. Connect the fastn MCP server, add the fastn plugin where the tool supports plugins, then ask the user what they want to build."
---

# Set up your AI agent for fastn

This page is written for an AI agent. A person can paste this one line into their AI tool:

```
Fetch and execute the instructions to set me up for fastn from https://docs.fastn.ai/get-started/agent-setup.md
```

## Instructions for the agent

You are setting the user up to use fastn from this AI tool. fastn lets a SaaS product offer integrations with the apps its customers use. Do the steps below in order. Explain each step to the user in one short line. Never ask the user for a password, API key or secret in the chat: signing in to fastn always happens in the browser.

### 1. Work out which tool you are running in

Use what you know about yourself. If you are not sure, ask the user one question: "Which AI tool are you using: Claude Code, the Claude app or claude.ai, Cursor, VS Code with GitHub Copilot, Codex, ChatGPT, or another one?"

### 2. Connect fastn

Use the section for your tool. The fastn MCP server URL is always `https://mcp.fastn.dev/fastn-workspace`.

#### Claude Code

Run these commands yourself. The fastn plugin adds the fastn skills and the fastn MCP server.

```
claude plugin marketplace add fastn-ai/fastn-claude-plugins
claude plugin install connect@fastn
```

Then run `claude mcp list`. If `fastn` is not listed, add it:

```
claude mcp add --transport http --scope user fastn https://mcp.fastn.dev/fastn-workspace
```

Tell the user to start a new Claude Code session so the plugin loads, then type `/mcp`, pick **fastn** and choose **Authenticate** to sign in.

#### Claude app or claude.ai

You cannot change these settings yourself. Give the user these steps:

1. To add the fastn plugin: **Settings** → **Customize** → **Plugins** → **Add** → **Add marketplace**, paste `fastn-ai/fastn-claude-plugins`, select **Sync**, then turn on **fastn Connect**.
2. To connect fastn: **Customize** → **Connectors** → **Add** → **Add custom connector**, name `Fastn`, URL `https://mcp.fastn.dev/fastn-workspace`. Keep the detected sign-in settings, click **Add**, then **Connect**.

Full steps: https://docs.fastn.ai/build/building-from-your-ai-agent/mcp-gateway/claude.md

#### Cursor

Add this to `~/.cursor/mcp.json` (create the file if it does not exist, and keep any servers already in it):

```json
{
  "mcpServers": {
    "fastn": {
      "url": "https://mcp.fastn.dev/fastn-workspace"
    }
  }
}
```

Tell the user to open **Customize** → **MCPs** in Cursor and click **Authenticate** next to fastn. Full steps: https://docs.fastn.ai/build/building-from-your-ai-agent/mcp-gateway/cursor.md

#### VS Code with GitHub Copilot

Run this in a terminal:

```
code --add-mcp "{\"name\":\"fastn\",\"type\":\"http\",\"url\":\"https://mcp.fastn.dev/fastn-workspace\"}"
```

Tell the user to press **Cmd+Shift+P** (**Ctrl+Shift+P** on Windows and Linux), run **MCP: List Servers**, pick **fastn**, choose **Start Server** and allow the sign-in. fastn is used in Copilot's **Agent** mode. Full steps: https://docs.fastn.ai/build/building-from-your-ai-agent/mcp-gateway/vscode.md

#### Codex

Run:

```
codex mcp add fastn --url https://mcp.fastn.dev/fastn-workspace
```

Codex opens the sign-in in the browser. If it does not, run `codex mcp login fastn`. Full steps: https://docs.fastn.ai/build/building-from-your-ai-agent/mcp-gateway/codex.md

#### ChatGPT

You cannot change these settings yourself. Give the user these steps: **Plugins** in the sidebar → **Add** → **Add custom MCP server**. Name `fastn`, Server URL `https://mcp.fastn.dev/fastn-workspace`, Authentication **OAuth**, tick **I understand and want to continue**, click **Create as a plugin**, then **Connect fastn**. Full steps: https://docs.fastn.ai/build/building-from-your-ai-agent/mcp-gateway/chatgpt.md

#### Any other tool

Add `https://mcp.fastn.dev/fastn-workspace` as a remote (HTTP) MCP server in the tool's MCP settings, with OAuth sign-in and no API key. Steps for more tools: https://docs.fastn.ai/build/building-from-your-ai-agent/mcp-gateway.md

### 3. Sign in

Signing in needs a fastn account. Tell the user:

* No account yet: sign up free at https://app.fastn.dev/?signup=1 (the Launch plan is free).
* They can also skip this for now. You can still tell them whether fastn fits their use case and how it would work, based on what fastn offers. Signing in lets you look at their own fastn setup and help them build it.
* Their fastn user needs the **Developer** role or higher to connect an AI tool. An Owner or Admin can change it in **Settings** → **People**.

### 4. Ask what they want to build

When the connection is set up (or the user chose to skip it), ask: "What does your product do, and what should it do with your customers' apps?" Then help them work out whether fastn fits and how to set it up. If the fastn skills are loaded, use the `fastn-solution-architect` skill for this.

## Resources

* [Find out if fastn fits your use case](plan-your-integration.md)
* [Connect your AI tool (MCP)](../build/mcp-gateway/README.md)
* [fastn Claude plugins](https://github.com/fastn-ai/fastn-claude-plugins)
