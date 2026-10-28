---
description: Add fastn to Claude Code with one command, sign in, and build integrations from the terminal.
---

# Claude Code

Claude Code adds fastn as a remote MCP server with one command. Sign in once, then ask for the integration in a Claude Code session.

<figure><img src="../../.gitbook/assets/mcp-fastn-tab-claude-manual.webp" alt="fastn's MCP server page with the second Claude tile selected, showing the steps to add fastn by hand, a Claude Code command claude mcp add --transport http fastn https://mcp.fastn.dev/fastn-workspace, a Claude Desktop config snippet and an Add for the whole organization link"><figcaption>The command is on the second <strong>Claude</strong> tile under <strong>Connect AI tools</strong> in fastn.</figcaption></figure>

## Add fastn

{% stepper %}
{% step %}
#### Run the command

```
claude mcp add --transport http fastn https://mcp.fastn.dev/fastn-workspace
```

Claude Code prints *Added HTTP MCP server fastn with URL: https://mcp.fastn.dev/fastn-workspace to local config*. By default the server is added for the current project only. Add `--scope user` to use fastn in every project.
{% endstep %}

{% step %}
#### Sign in

```
claude mcp login fastn
```

Or, inside a Claude Code session, type `/mcp`, pick **fastn** and choose **Authenticate**.

fastn opens in your browser. Sign in if asked, pick the workspace Claude Code works in and click **Connect**.

<figure><img src="../../.gitbook/assets/mcp-claude-code-choose-workspace.webp" alt="fastn's page titled Which workspace should Claude Code (claude.ai) use?, with The org selected in fastn chosen, a list of orgs and a Connect button"><figcaption><strong>The org selected in fastn</strong> follows whichever org you have open in the fastn dashboard; picking a named org pins Claude Code to it.</figcaption></figure>

The terminal prints *Authenticated with "fastn". Its tools are now available in Claude Code.*
{% endstep %}

{% step %}
#### Check it

```
claude mcp list
```

```
fastn: https://mcp.fastn.dev/fastn-workspace (HTTP) - ✔ Connected
```
{% endstep %}
{% endstepper %}

## Use it

Start `claude` and ask for the outcome in one sentence. To check the connection first, ask *Use fastn to tell me which org I'm in.* Claude Code asks before it runs a fastn tool; approve it, and it answers with the org you picked when signing in.

From here Claude Code works through the same steps as every agent: see [Building from your AI agent](../building-from-your-ai-agent.md).

## Claude Desktop config file

The Claude desktop app normally uses the connector you add in claude.ai: see [Claude](claude.md). If you manage it through `claude_desktop_config.json` instead, that file only starts local servers, so bridge to fastn with `mcp-remote`:

```json
{
  "mcpServers": {
    "fastn": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.fastn.dev/fastn-workspace"]
    }
  }
}
```

A `"url"` entry in that file is ignored, and no fastn tools appear.

## Troubleshooting

* **`fastn ... ! Needs authentication` in `claude mcp list`.** Run `claude mcp login fastn`.
* **The browser shows `{"error":"redirect_uri mismatch"}`.** Claude Code sign-in failed this way on fastn before 27 October 2026. Run `claude mcp login fastn` again.
* **Claude Code works on the wrong org.** Run `claude mcp logout fastn`, then `claude mcp login fastn` and pick the workspace again.
