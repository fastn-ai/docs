---
description: Add fastn to Lovable as a custom MCP server, sign in, and use your fastn tools from Lovable's chat.
---

# Lovable

In Lovable, fastn is a chat connector. It gives Lovable's chat your fastn tools while you build. It attaches to you and your chats, not to the app you publish.

{% hint style="info" %}
**Before you start:** custom MCP servers work on every Lovable plan. On Business and Enterprise, a workspace admin can turn them off; if **MCP server** is greyed out, ask your admin.
{% endhint %}

## Add fastn

{% stepper %}
{% step %}
#### Add a custom MCP server

In Lovable, open **Connectors** in the sidebar. Click **Add custom** at the top right and choose **MCP server**.
{% endstep %}

{% step %}
#### Enter fastn's URL

Enter **Server name** `fastn` and **Server URL** `https://mcp.fastn.dev/fastn-workspace`, leave **Authentication** on **OAuth (default)**, and click **Add & authorize**.

<figure><img src="../../.gitbook/assets/mcp-lovable-add-server.webp" alt="Lovable's Add MCP server form with Server name fastn, Server URL https://mcp.fastn.dev/fastn-workspace, Authentication set to OAuth (default) with Bearer token or API key and No authentication as the other options, and Cancel and Add and authorize buttons"><figcaption>Keep <strong>OAuth</strong>. fastn signs you in, so no token is needed.</figcaption></figure>
{% endstep %}

{% step %}
#### Pick the workspace

fastn opens in a popup. Sign in if asked, pick the workspace Lovable works in and click **Connect**.

<figure><img src="../../.gitbook/assets/mcp-lovable-choose-workspace.webp" alt="fastn's page titled Which workspace should Lovable (api.lovable.dev) use?, with The org selected in fastn chosen, a list of orgs and a Connect button"><figcaption><strong>The org selected in fastn</strong> follows whichever org you have open in the fastn dashboard; picking a named org pins Lovable to it.</figcaption></figure>

The popup closes and Lovable shows *MCP server added successfully*, with fastn marked **Connected** and its tools listed.

<figure><img src="../../.gitbook/assets/mcp-lovable-connected.webp" alt="Lovable's fastn connector page showing fastn Connected and Chat, an Always allow all tools from this connection toggle, and Manage my agent's permissions listing fastn tools such as fastnPlatform__cancelWorkflowPromotion, fastnPlatform__createAction and fastnPlatform__createAlert"><figcaption>Set per-tool approvals here, or turn on <strong>Always allow all tools from this connection</strong>.</figcaption></figure>
{% endstep %}
{% endstepper %}

## Use it

Start a chat or open a project and ask for the outcome in one sentence. To check the connection first, ask *Using the fastn connector, who am I in fastn?* Lovable answers with the org you picked when signing in.

<figure><img src="../../.gitbook/assets/mcp-lovable-answer.webp" alt="Lovable's chat answering Using the fastn connector, who am I in fastn? with Checked your identity in fastn and a list of name, email, role, organization, environment and plan"><figcaption>Read-only fastn tools run straight away. Lovable asks before any tool that changes something.</figcaption></figure>

From here Lovable works through the same steps as every agent: see [Building from your AI agent](../building-from-your-ai-agent.md).

## Troubleshooting

* **Nothing happens after Add & authorize.** Your browser blocked the sign-in popup. Allow popups for lovable.dev and click **Add & authorize** again.
* **Lovable doesn't use fastn.** Name it in your message, for example *Using the fastn connector, …*.
* **Lovable works on the wrong org.** Open fastn under **Connectors**, click **Disconnect fastn**, add it again and pick the workspace when you sign in.
