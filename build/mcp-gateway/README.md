---
description: Letting an AI client reach your connectors as tools.
---

# MCP gateway

Everything you build in fastn (connectors, actions, workflows) can be used from an AI client over the Model Context Protocol. The client sees your fastn workflows and the fastn platform tools, and reaches your connectors' actions through those platform tools, with the same customer scoping and the same permission model as everything else. Your agent can also build new integrations for you, right in the chat: see [Building from your AI agent](../building-from-your-ai-agent.md).

### Connecting

Click **Connect AI tools** in the top bar, or open **Embed → API keys and MCP** and the **MCP server** tab. Both show the same picker: **Use fastn from Claude or any MCP client**. Both need the **Developer** role or above; below that, neither is shown.

<figure><img src="../../.gitbook/assets/mcp-connect-ai-tools-dialog.webp" alt="fastn's dialog titled Use fastn from Claude or any MCP client, reading Add fastn as an MCP server and Claude, ChatGPT, Cursor or any MCP client can build integrations for you, right in the chat, with Claude recommended and an Add to Claude button"><figcaption><strong>Add to Claude</strong> is the one-click path. The tiles under <strong>Other</strong> give each client's own steps.</figcaption></figure>

Every client uses the same MCP server URL, shown at the bottom of the dialog with a **Copy** button:

```
https://mcp.fastn.dev/fastn-workspace
```

### How your agent connects

You add fastn as an MCP server at that URL and sign in. The client sends you to fastn, where you sign in, so no API key is needed. If you belong to more than one fastn org, fastn also asks which workspace the client works in; with one org it connects straight away.

| Client | Where you add fastn |
| --- | --- |
| [Claude](claude.md) | **Settings** → **Connectors** → **Add custom connector**, or **Add to Claude** in fastn |
| [Claude Code](claude-code.md) | `claude mcp add --transport http fastn <URL>` |
| [ChatGPT](chatgpt.md) | Turn on **Developer mode** (**Settings** → **Apps & Connectors** → **Advanced settings**), then **Add custom connector** |
| [Cursor](cursor.md) | **Add to Cursor** in fastn, or **Customize** → **MCPs** |
| [VS Code](vscode.md) | **Install in VS Code** in fastn, or `.vscode/mcp.json` |
| [Codex](codex.md) | `codex mcp add fastn --url <URL>` |
| [Antigravity](antigravity.md) | `~/.gemini/config/mcp_config.json`, then **Customizations** → **Authenticate** |
| [Devin](devin.md) | **Customize** → **MCPs** → **New MCP** |
| [Cline](cline.md) | **MCP** → **Add Remote Server**, or `cline_mcp_settings.json` |
| [Lovable](lovable.md) | **Connectors** → **Chat connectors** → **New MCP server** |
| [Bolt](bolt.md) | **Connectors (MCP)** → **Custom MCP server** |

#### Any other MCP client

Any client that speaks Streamable HTTP and OAuth can add fastn the same way: give it the URL above and sign in when it asks.

### Scoping

A client that signs in acts as you. Its fastn tools run in the workspace you signed in to (or picked, if you belong to more than one org), with your own role in that org, so it can do what you can do in the dashboard and nothing more. Picking **The org selected in fastn** makes it follow whichever org you switch to in the dashboard; picking a named org pins it there.

{% hint style="warning" %}
An MCP client can change real things in your org, the same as you can. Approve tool calls you don't expect to see, and sign the client out when you stop using it.
{% endhint %}

### Watching it

Gateway activity lands in the same places as everything else: runs appear in **Operate → Activity → [Executions](../../operate/executions.md)**, with the calling identity in the **Triggered by** column.

An MCP client spends no fastn AI credits. The **By agent** breakdown in the credits popover in the top bar covers fastn's own agents, such as Build with AI, not your AI tool.

### The A2A option

The widget's Embed tab lists **A2A** (agent-to-agent), alongside Iframe and SDK, marked *soon*. That is the customer-facing counterpart: your customer's own agent reaching the integrations you offer. See [Embedding the widget](../../embed/embedding/README.md).

### In this section

* [From your backend](from-your-backend.md)
* [Claude](claude.md)
* [Claude Code](claude-code.md)
* [ChatGPT](chatgpt.md)
* [Cursor](cursor.md)
* [VS Code](vscode.md)
* [Codex](codex.md)
* [Antigravity](antigravity.md)
* [Devin](devin.md)
* [Cline](cline.md)
* [Lovable](lovable.md)
* [Bolt](bolt.md)
