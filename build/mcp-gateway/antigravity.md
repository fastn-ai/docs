---
description: Add Fastn to Google Antigravity through its MCP config file, sign in, and build integrations from the Antigravity agent.
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

# Antigravity

Google Antigravity has no install button for custom MCP servers: its **Add MCP** button only opens Google's MCP store. Add Fastn to Antigravity's MCP config file instead, then sign in from **Customizations**. The Antigravity app, the Antigravity IDE, and the Antigravity CLI all read the same file.

## Add Fastn

{% stepper %}
{% step %}
#### Add Fastn to the config file

Open `~/.gemini/config/mcp_config.json` in any editor (create it if it does not exist) and add Fastn under `mcpServers`. Keep any servers already in the file.

```json
{
  "mcpServers": {
    "fastn": {
      "serverUrl": "https://mcp.fastn.dev/fastn-workspace"
    }
  }
}
```

The key must be `serverUrl`. Antigravity does not read `url` or `httpUrl`, and a server written with them silently loads no tools.

<figure><img src="../../.gitbook/assets/mcp-fastn-tab-antigravity.webp" alt="Fastn's MCP server page with the Antigravity tile selected, showing a note that Antigravity's remote field is serverUrl and a ~/.gemini/config/mcp_config.json snippet with a Fastn serverUrl entry"><figcaption>The Antigravity tile under <strong>Connect your AI tool</strong> in Fastn has the same snippet with a Copy button.</figcaption></figure>

In the Antigravity IDE you can open the same file from the agent panel: the **…** menu at the top, then **MCP Servers** → **Manage MCP Servers** → **View raw config**. For one workspace only, use `.agents/mcp_config.json` in that folder.
{% endstep %}

{% step %}
#### Load it and click Authenticate

In Antigravity, open **Customizations** in the sidebar (in the IDE: **Antigravity User Settings** → **Customizations**). Under **MCP Servers**, click refresh if Fastn is not listed yet.

Fastn shows a red dot and an *Unauthorized* error until you sign in. Click **Authenticate**.

<figure><img src="../../.gitbook/assets/mcp-antigravity-authenticate.webp" alt="Antigravity's MCP Servers section listing Fastn with a red status dot, an Authenticate button, the error calling initialize: Unauthorized, and an Enter authorization code field with Submit and Cancel"><figcaption>The <em>Unauthorized</em> error is expected before you sign in.</figcaption></figure>
{% endstep %}

{% step %}
#### Pick the workspace

Fastn opens in your browser. Sign in if asked. If you belong to more than one Fastn org, pick the workspace Antigravity works in and click **Connect**.

<figure><img src="../../.gitbook/assets/mcp-antigravity-choose-workspace.webp" alt="Fastn's page titled Which workspace should Google Antigravity (antigravity.google) use?, with The org selected in Fastn chosen, a list of orgs and a Connect button"><figcaption><strong>The org selected in Fastn</strong> follows whichever org you have open in the Fastn dashboard; picking a named org pins Antigravity to it.</figcaption></figure>
{% endstep %}

{% step %}
#### Paste the code back into Antigravity

Google shows *Paste this code into your application to complete authentication*. Click **Copy to Clipboard**, go back to Antigravity, paste the code into **Enter authorization code…**, and click **Submit**.

<figure><img src="../../.gitbook/assets/mcp-antigravity-code.webp" alt="Google Antigravity's callback page reading Paste this code into your application to complete authentication, with a code box and a Copy to Clipboard button"><figcaption>The code works once and expires quickly. Paste it straight away.</figcaption></figure>

Fastn's dot turns green and the row shows its tools.

<figure><img src="../../.gitbook/assets/mcp-antigravity-connected.webp" alt="Antigravity's MCP Servers section listing Fastn with a green status dot, a Sign out button and 178 tools enabled"><figcaption>Fastn is connected. <strong>Sign out</strong> on this row disconnects it.</figcaption></figure>
{% endstep %}
{% endstepper %}

## Use it

Start a **New Conversation** and ask for the outcome in one sentence. To check the connection first, ask *Who am I in Fastn?*

The first time the agent calls a Fastn tool, Antigravity asks **Allow using this MCP tool?** Pick **Yes, allow this time**, or one of the always-allow options, and click **Submit**.

<figure><img src="../../.gitbook/assets/mcp-antigravity-tool-approval.webp" alt="Antigravity asking Allow using this MCP tool? for Fastn/fastnPlatform__whoami, with options Yes allow this time, Yes and always allow in this conversation, Yes and always allow when not in a project, Yes and always allow, and No, plus Skip and Submit buttons"><figcaption>The prompt names the server and the tool.</figcaption></figure>

From here Antigravity works through the same steps as every AI tool: see [Build from your AI tool](../building-from-your-ai-agent.md).

## Antigravity CLI

The CLI reads the same `~/.gemini/config/mcp_config.json`. Run `agy`, then type `/mcp` to check Fastn is listed.

## Troubleshooting

* **Fastn never appears in Customizations.** Check the file uses `serverUrl` and is valid JSON, then click refresh under **MCP Servers**.
* **The code is rejected.** Codes are single use. Click **Authenticate** again and paste the new code.
* **Antigravity works on the wrong org.** Click **Sign out** on the Fastn row, then **Authenticate**, and pick the workspace again.
