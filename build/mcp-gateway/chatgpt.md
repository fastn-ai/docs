---
description: Add fastn to ChatGPT as a custom MCP plugin, sign in, and use your fastn tools from a ChatGPT chat.
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

# ChatGPT

ChatGPT adds fastn as a custom MCP server from its **Plugins** page. Sign in once, then ask for the integration in a chat.

{% hint style="info" %}
**Before you start:** custom MCP servers work in ChatGPT on the web, not in the mobile apps. You don't need to turn on **Developer mode**.

* **Business:** only workspace admins and owners can add a custom MCP server. An admin can give others the **Create plugins with MCPs** permission.
* **Enterprise and Edu:** admins and owners can add one, and admins can let selected members do it too.
* **Pro:** a custom MCP server gets read and fetch access only, so fastn's tools that change things aren't available.
{% endhint %}

## Add fastn

{% stepper %}
{% step %}
#### Open Plugins

In ChatGPT on the web, click **Plugins** in the sidebar. At the top right, click the plus button (**Add**) and choose **Add custom MCP server**.

<figure><img src="../../.gitbook/assets/mcp-chatgpt-plugins-page.webp" alt="ChatGPT's Plugins page, reading Connect plugins to let ChatGPT work across your tools, with a Search plugins box and an Add button at the top right"><figcaption>The <strong>Add</strong> button is at the top right of the Plugins page.</figcaption></figure>
{% endstep %}

{% step %}
#### Enter fastn's URL

Enter **Name** `fastn`. Under **Connection**, keep **Server URL** and enter `https://mcp.fastn.dev/fastn-workspace`. Leave **Authentication** on **OAuth** and leave the client ID and secret empty: fastn uses dynamic client registration, so ChatGPT registers itself. Tick **I understand and want to continue** and click **Create as a plugin**.

<figure><img src="../../.gitbook/assets/mcp-chatgpt-add-server.webp" alt="ChatGPT's Add custom MCP server form with Name fastn, Connection set to Server URL https://mcp.fastn.dev/fastn-workspace, Authentication OAuth, an Advanced OAuth settings row, a risk notice, the I understand and want to continue box ticked, and Cancel and Create as a plugin buttons"><figcaption>Leave <strong>Advanced OAuth settings</strong> alone. ChatGPT finds fastn's sign-in by itself.</figcaption></figure>
{% endstep %}

{% step %}
#### Connect and pick the workspace

ChatGPT shows **Connect fastn**. Click **Connect fastn**.

<figure><img src="../../.gitbook/assets/mcp-chatgpt-connect-dialog.webp" alt="ChatGPT's Connect fastn dialog explaining what ChatGPT may share with the app, with Connect fastn and Cancel buttons"><figcaption>ChatGPT asks once per account.</figcaption></figure>

fastn opens in your browser. Sign in if asked. If you belong to more than one fastn org, pick the workspace ChatGPT works in, then click **Connect**.

<figure><img src="../../.gitbook/assets/mcp-chatgpt-choose-workspace.webp" alt="fastn's page titled Which workspace should ChatGPT (chatgpt.com) use?, with The org selected in fastn chosen, a list of orgs and a Connect button"><figcaption><strong>The org selected in fastn</strong> follows whichever org you have open in the fastn dashboard; picking a named org pins ChatGPT to it.</figcaption></figure>

ChatGPT lists fastn under your plugins on the **Plugins** page with your account connected. If it shows fastn as not installed, open it and install it before you use it.
{% endstep %}
{% endstepper %}

## Use it

Start a new chat, type `@` in the prompt box and select **fastn**. Then ask for the outcome in one sentence. To check the connection first, ask *Using the fastn plugin, who am I in fastn?* ChatGPT asks you to confirm any fastn tool that changes something.

<figure><img src="../../.gitbook/assets/mcp-chatgpt-answer.webp" alt="ChatGPT's answer card titled Your FASTN identity, showing the signed-in user, role, organization, organization type, plan and organization ID"><figcaption>ChatGPT answers from the fastn workspace you picked.</figcaption></figure>

From here ChatGPT works through the same steps as every AI tool: see [Build from your AI tool](../building-from-your-ai-agent.md).

## Troubleshooting

* **`token_endpoint_auth_method "private_key_jwt" is not supported`.** ChatGPT sign-in failed this way on fastn before the fix for it reached your fastn. Click **Connect fastn** again.
* **ChatGPT doesn't use fastn.** Type `@`, select **fastn**, and name it in your message, for example *Using the fastn plugin, …*.
* **There's no Add custom MCP server option.** On Business, Enterprise and Edu, ask a workspace admin for permission to create plugins with MCPs, or ask them to add fastn for you.
* **ChatGPT works on the wrong org.** Open fastn under **Plugins**, remove your connected account, connect again and pick the workspace.
