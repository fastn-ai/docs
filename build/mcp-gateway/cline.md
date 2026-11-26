---
description: Add Fastn to Cline in VS Code as a remote MCP server, sign in, and build integrations from a Cline task.
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

# Cline

Cline adds Fastn from its **MCP** settings as a remote server. Sign in once, then ask for the integration in a Cline task.

{% hint style="info" %}
**Before you start:** set Cline up with a model first (Cline's own sign-in, or your API key). Fastn exposes more than 128 tools, so pick a model that accepts that many; see [Troubleshooting](#troubleshooting).
{% endhint %}

## Add Fastn

{% stepper %}
{% step %}
#### Open Add Remote Server

In the Cline panel, click the MCP icon at the top. On the **MCP** tab under **Installed**, click **Add Remote Server**.
{% endstep %}

{% step %}
#### Enter Fastn's URL

Enter **Server Name** `fastn` and **Server URL** `https://mcp.fastn.dev/fastn-workspace`, leave **Transport Type** on **Streamable HTTP**, and click **Add Server**.

<figure><img src="../../.gitbook/assets/mcp-cline-add-remote.webp" alt="Cline's Add a remote MCP server form with Server Name, Server URL, Transport Type set to Streamable HTTP with SSE (Legacy) as the other option, and Add Server and Cancel buttons"><figcaption>Keep <strong>Streamable HTTP</strong>. Fastn does not serve the legacy SSE transport.</figcaption></figure>
{% endstep %}

{% step %}
#### Authenticate

Fastn shows *This MCP server requires authentication to get started.* Click **Authenticate**.

<figure><img src="../../.gitbook/assets/mcp-cline-needs-auth.webp" alt="Cline's MCP list with Fastn, a status dot, the message This MCP server requires authentication to get started, and Authenticate and Delete Server buttons"><figcaption>Cline signs in with OAuth, so no token is needed.</figcaption></figure>

Fastn opens in your browser. Sign in if asked. If you belong to more than one Fastn org, pick the workspace Cline works in and click **Connect**.

<figure><img src="../../.gitbook/assets/mcp-cline-choose-workspace.webp" alt="Fastn's page titled Which workspace should Cline use?, with The org selected in Fastn chosen, a list of orgs and a Connect button"><figcaption><strong>The org selected in Fastn</strong> follows whichever org you have open in the Fastn dashboard; picking a named org pins Cline to it.</figcaption></figure>

The browser shows *Authentication Successful* and closes itself. Back in VS Code, Fastn's dot turns green in Cline's list.
{% endstep %}
{% endstepper %}

## Use it

Start a new Cline task and ask for the outcome in one sentence. To check the connection first, ask *Who am I in Fastn?* Cline asks before it runs a Fastn tool; approve it, and it answers with the org you picked when signing in.

From here Cline works through the same steps as every AI tool: see [Build from your AI tool](../building-from-your-ai-agent.md).

## Add it by hand

Click **Edit Configuration** in Cline's **MCP** tab and add Fastn under `mcpServers`. The `type` must be `streamableHttp`, written exactly so:

```json
{
  "mcpServers": {
    "fastn": {
      "url": "https://mcp.fastn.dev/fastn-workspace",
      "type": "streamableHttp"
    }
  }
}
```

Then click **Authenticate** on Fastn's row, as in step 3.

<figure><img src="../../.gitbook/assets/mcp-fastn-tab-cline.webp" alt="Fastn's MCP server page with the Cline tile selected, showing a cline_mcp_settings.json snippet with a Fastn entry of type streamableHttp and a note that the type must be camelCase"><figcaption>The Cline tile under <strong>Connect your AI tool</strong> in Fastn has the same snippet.</figcaption></figure>

## Troubleshooting

* **`Invalid value for 'tools': maximum number of items is 128`.** The model Cline is using accepts at most 128 tools, and Fastn exposes more. Pick a different model in Cline's settings; the error comes from the model provider, not from Fastn.
* **Fastn fails with a 405 error.** The `type` is wrong. Use `streamableHttp` (camelCase), not `sse` or `streamable-http`.
* **Cline works on the wrong org.** Delete Fastn from Cline's **MCP** list, add it again, and pick the workspace when you authenticate.
