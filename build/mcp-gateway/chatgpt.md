---
description: Add fastn to ChatGPT as a custom MCP plugin, sign in, and use your fastn tools from a ChatGPT chat.
---

# ChatGPT

ChatGPT adds fastn as a custom MCP server from its **Plugins** page. Sign in once, then ask for the integration in a chat.

## Add fastn

{% stepper %}
{% step %}
#### Open Plugins

In ChatGPT, click **Plugins** in the sidebar. At the top right, click **Add** and choose **Add custom MCP server**.

<figure><img src="../../.gitbook/assets/mcp-chatgpt-plugins-page.webp" alt="ChatGPT's Plugins page, reading Connect plugins to let ChatGPT work across your tools, with a Search plugins box and an Add button at the top right"><figcaption>The <strong>Add</strong> button is at the top right of the Plugins page.</figcaption></figure>
{% endstep %}

{% step %}
#### Enter fastn's URL

Enter **Name** `fastn`. Under **Connection**, keep **Server URL** and enter `https://mcp.fastn.dev/fastn-workspace`. Leave **Authentication** on **OAuth**, tick **I understand and want to continue** and click **Create as a plugin**.

<figure><img src="../../.gitbook/assets/mcp-chatgpt-add-server.webp" alt="ChatGPT's Add custom MCP server form with Name fastn, Connection set to Server URL https://mcp.fastn.dev/fastn-workspace, Authentication OAuth, an Advanced OAuth settings row, a risk notice, the I understand and want to continue box ticked, and Cancel and Create as a plugin buttons"><figcaption>Leave <strong>Advanced OAuth settings</strong> alone. ChatGPT finds fastn's sign-in by itself.</figcaption></figure>
{% endstep %}

{% step %}
#### Connect and pick the workspace

ChatGPT shows **Connect fastn**. Click **Connect fastn**.

<figure><img src="../../.gitbook/assets/mcp-chatgpt-connect-dialog.webp" alt="ChatGPT's Connect fastn dialog explaining what ChatGPT may share with the app, with Connect fastn and Cancel buttons"><figcaption>ChatGPT asks once per account.</figcaption></figure>

fastn opens in your browser. Sign in if asked, pick the workspace ChatGPT works in and click **Connect**.

<figure><img src="../../.gitbook/assets/mcp-chatgpt-choose-workspace.webp" alt="fastn's page titled Which workspace should ChatGPT (chatgpt.com) use?, with The org selected in fastn chosen, a list of orgs and a Connect button"><figcaption><strong>The org selected in fastn</strong> follows whichever org you have open in the fastn dashboard; picking a named org pins ChatGPT to it.</figcaption></figure>

ChatGPT lists fastn under **Plugins** with your account connected.
{% endstep %}
{% endstepper %}

## Use it

Start a new chat and ask for the outcome in one sentence. To check the connection first, ask *Using the fastn plugin, who am I in fastn?*

<figure><img src="../../.gitbook/assets/mcp-chatgpt-answer.webp" alt="ChatGPT's answer card titled Your FASTN identity, showing the signed-in user, role, organization, organization type, plan and organization ID"><figcaption>ChatGPT answers from the fastn workspace you picked.</figcaption></figure>

From here ChatGPT works through the same steps as every agent: see [Building from your AI agent](../building-from-your-ai-agent.md).

## Troubleshooting

* **`token_endpoint_auth_method "private_key_jwt" is not supported`.** ChatGPT sign-in failed this way on fastn before the fix for it reached your fastn. Click **Connect fastn** again.
* **ChatGPT doesn't use fastn.** Name it in your message, for example *Using the fastn plugin, …*.
* **ChatGPT works on the wrong org.** Open fastn under **Plugins**, remove your connected account, connect again and pick the workspace.
