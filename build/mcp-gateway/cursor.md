---
description: Add fastn to Cursor with one click, sign in, and build integrations from Cursor's agent.
---

# Cursor

Add fastn to Cursor from the fastn dashboard, sign in once, then ask Cursor's agent for the integration.

{% hint style="info" %}
**Before you start:** sign in to Cursor. Its agent needs a Cursor account before it can use MCP servers.
{% endhint %}

## Add fastn

{% stepper %}
{% step %}
#### Click Add to Cursor

In fastn, click **Connect AI tools** in the top bar (or open **Access** → **MCP server**), pick the **Cursor** tile and click **Add to Cursor**. When your browser asks to open Cursor, allow it.

<figure><img src="../../.gitbook/assets/mcp-fastn-tab-cursor.webp" alt="fastn's MCP server page with the Cursor tile selected, showing an Add to Cursor button, a note about project-scoped servers, and a ~/.cursor/mcp.json snippet with an mcpServers fastn entry"><figcaption>The Cursor tab also has the config file, if you prefer to add it by hand.</figcaption></figure>
{% endstep %}

{% step %}
#### Install the server

Cursor opens **Install MCP server?** with the name `fastn`, the type **Remote HTTPS** and the server URL `https://mcp.fastn.dev/fastn-workspace` filled in. Leave the headers and OAuth client fields empty and click **Install**.

<figure><img src="../../.gitbook/assets/mcp-cursor-install-dialog.webp" alt="Cursor's Install MCP server? dialog with Name fastn, Type Remote HTTPS, Server URL https://mcp.fastn.dev/fastn-workspace, empty HTTP headers, Client ID and Client Secret fields, and Cancel and Install buttons"><figcaption>fastn signs you in with OAuth, so no header or client ID is needed.</figcaption></figure>
{% endstep %}

{% step %}
#### Authenticate

Cursor lists fastn under **Needs Attention** with *Needs authentication*. Click **Authenticate**.

<figure><img src="../../.gitbook/assets/mcp-cursor-needs-auth.webp" alt="Cursor's MCPs list with fastn under Needs Attention, marked Needs authentication, and an Authenticate link"><figcaption>Find this list again under <strong>Customize</strong> → <strong>MCPs</strong>.</figcaption></figure>
{% endstep %}

{% step %}
#### Pick the workspace

fastn opens in your browser. Sign in if asked, pick the workspace Cursor works in and click **Connect**.

<figure><img src="../../.gitbook/assets/mcp-cursor-choose-workspace.webp" alt="fastn's page titled Which workspace should Cursor use?, with The org selected in fastn chosen, a list of orgs and a Connect button"><figcaption><strong>The org selected in fastn</strong> follows whichever org you have open in the fastn dashboard; picking a named org pins Cursor to it.</figcaption></figure>

The browser shows *Authorization complete!* Click **Return to Cursor**. fastn moves to **Connected** in Cursor's list.

<figure><img src="../../.gitbook/assets/mcp-cursor-auth-complete.webp" alt="A browser page reading Authorization complete! You can close this tab and return to Cursor, with a Return to Cursor link"><figcaption>You can close this tab.</figcaption></figure>
{% endstep %}
{% endstepper %}

## Use it

Start a new chat with Cursor's agent and ask for the outcome in one sentence. To check the connection first, ask *What can fastn do for me?* Cursor asks before it runs a fastn tool; approve it.

<figure><img src="../../.gitbook/assets/mcp-cursor-agent-answer.webp" alt="Cursor's agent answering What can fastn do for me? with Fastn is the integration layer you can drive from this chat, followed by a list: talk to connected apps, build integrations"><figcaption>Cursor answers from the fastn workspace you picked.</figcaption></figure>

From here Cursor works through the same steps as every agent: see [Building from your AI agent](../building-from-your-ai-agent.md).

## Add it by hand

Add fastn to `~/.cursor/mcp.json` for every project, or to `.cursor/mcp.json` in a repository for that project only:

```json
{
  "mcpServers": {
    "fastn": {
      "url": "https://mcp.fastn.dev/fastn-workspace"
    }
  }
}
```

Cursor then lists fastn under **Customize** → **MCPs** with **Authenticate**. Continue from step 3.

## Troubleshooting

* **fastn shows Connected but 0 tools enabled.** The tool list is still loading. Wait a few seconds or reopen **Customize** → **MCPs**.
* **The agent does not use fastn.** Check fastn is under **Connected** in **Customize** → **MCPs**, then name fastn in your message, for example *Using fastn, …*.
* **Cursor works on the wrong org.** Remove fastn from **Customize** → **MCPs**, add it again and pick the workspace when you authenticate.
