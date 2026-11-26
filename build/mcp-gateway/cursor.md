---
description: Add Fastn to Cursor with one click, sign in, and build integrations from Cursor's agent.
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

# Cursor

Add Fastn to Cursor from the Fastn dashboard, sign in once, then ask Cursor's agent for the integration.

{% hint style="info" %}
**Before you start:** sign in to Cursor. Its agent needs a Cursor account before it can use MCP servers.
{% endhint %}

## Add Fastn

{% stepper %}
{% step %}
#### Click Add to Cursor

In Fastn, click **Connect your AI tool** in the top bar (or open **Embed → MCP server**), pick the **Cursor** tile and click **Add to Cursor**. When your browser asks to open Cursor, allow it.

<figure><img src="../../.gitbook/assets/mcp-fastn-tab-cursor.webp" alt="Fastn's MCP server page with the Cursor tile selected, showing an Add to Cursor button, a note about project-scoped servers, and a ~/.cursor/mcp.json snippet with an mcpServers Fastn entry"><figcaption>The Cursor tile also has the config file, if you prefer to add it by hand.</figcaption></figure>
{% endstep %}

{% step %}
#### Install the server

Cursor opens **Install MCP server?** with the name `fastn`, the type **Remote HTTPS**, and the server URL `https://mcp.fastn.dev/fastn-workspace` filled in. Leave the headers and OAuth client fields empty and click **Install**.

<figure><img src="../../.gitbook/assets/mcp-cursor-install-dialog.webp" alt="Cursor's Install MCP server? dialog with Name fastn, Type Remote HTTPS, Server URL https://mcp.fastn.dev/fastn-workspace, empty HTTP headers, Client ID and Client Secret fields, and Cancel and Install buttons"><figcaption>Fastn signs you in with OAuth, so no header or client ID is needed.</figcaption></figure>
{% endstep %}

{% step %}
#### Authenticate

Cursor lists Fastn under **Needs Attention** with *Needs authentication*. Click **Authenticate**.

<figure><img src="../../.gitbook/assets/mcp-cursor-needs-auth.webp" alt="Cursor's MCPs list with Fastn under Needs Attention, marked Needs authentication, and an Authenticate link"><figcaption>Find this list again under <strong>Customize</strong> → <strong>MCPs</strong>.</figcaption></figure>
{% endstep %}

{% step %}
#### Pick the workspace

Fastn opens in your browser. Sign in if asked. If you belong to more than one Fastn org, pick the workspace Cursor works in and click **Connect**.

<figure><img src="../../.gitbook/assets/mcp-cursor-choose-workspace.webp" alt="Fastn's page titled Which workspace should Cursor use?, with The org selected in Fastn chosen, a list of orgs and a Connect button"><figcaption><strong>The org selected in Fastn</strong> follows whichever org you have open in the Fastn dashboard; picking a named org pins Cursor to it.</figcaption></figure>

The browser shows *Authorization complete!* Click **Return to Cursor**. Fastn moves to **Connected** in Cursor's list.

<figure><img src="../../.gitbook/assets/mcp-cursor-auth-complete.webp" alt="A browser page reading Authorization complete! You can close this tab and return to Cursor, with a Return to Cursor link"><figcaption>You can close this tab.</figcaption></figure>
{% endstep %}
{% endstepper %}

## Use it

Start a new chat with Cursor's agent and ask for the outcome in one sentence. To check the connection first, ask *What can Fastn do for me?* Cursor asks before it runs a Fastn tool; approve it.

<figure><img src="../../.gitbook/assets/mcp-cursor-agent-answer.webp" alt="Cursor's agent answering What can Fastn do for me? with Fastn is the integration layer you can drive from this chat, followed by a list: talk to connected apps, build integrations"><figcaption>Cursor answers from the Fastn workspace you picked.</figcaption></figure>

From here Cursor works through the same steps as every AI tool: see [Build from your AI tool](../building-from-your-ai-agent.md).

## Add it by hand

Add Fastn to `~/.cursor/mcp.json` for every project, or to `.cursor/mcp.json` in a repository for that project only:

```json
{
  "mcpServers": {
    "fastn": {
      "url": "https://mcp.fastn.dev/fastn-workspace"
    }
  }
}
```

Cursor then lists Fastn under **Customize** → **MCPs** with **Authenticate**. Continue from step 3.

## Troubleshooting

* **Fastn shows Connected but 0 tools enabled.** The tool list is still loading. Wait a few seconds or reopen **Customize** → **MCPs**.
* **The agent does not use Fastn.** Check Fastn is under **Connected** in **Customize** → **MCPs**, then name fastn in your message, for example *Using Fastn, …*.
* **Cursor works on the wrong org.** Remove Fastn from **Customize** → **MCPs**, add it again, and pick the workspace when you authenticate.
