---
description: Add fastn to Bolt as a custom MCP connector, sign in, and use your fastn tools from Bolt's chat.
---

# Bolt

In bolt.new, fastn is a custom MCP connector. Sign in once, turn fastn on for a project, then ask for the integration in Bolt's chat.

## Add fastn

{% stepper %}
{% step %}
#### Open Connectors (MCP)

In bolt.new, click **+** in the chat box, then **Connectors** → **Manage connectors**. On the **Connectors (MCP)** page, click **Custom MCP server**.

<figure><img src="../../.gitbook/assets/mcp-bolt-custom-server.webp" alt="Bolt's Connectors (MCP) settings page with a Custom MCP server card next to pre-configured servers such as Notion, Linear, Miro, Context7, GitHub, Sentry, Granola, Shaders and Jira"><figcaption><strong>Custom MCP server</strong> is the first card.</figcaption></figure>
{% endstep %}

{% step %}
#### Enter fastn's URL

Enter **Name** `fastn` and **URL** `https://mcp.fastn.dev/fastn-workspace`, leave **Transport Type** on **HTTP**, set **Authentication** to **MCP OAuth** and click **Add MCP server**.

<figure><img src="../../.gitbook/assets/mcp-bolt-add-server.webp" alt="Bolt's New MCP server form with Name fastn, URL https://mcp.fastn.dev/fastn-workspace, Transport Type HTTP, Authentication MCP OAuth, an Automatically enable for new projects toggle, and Cancel and Add MCP server buttons"><figcaption>Turn on <strong>Automatically enable for new projects</strong> to skip step 4 in new projects.</figcaption></figure>
{% endstep %}

{% step %}
#### Choose Fastn Workspace and authorize

fastn opens in a new tab. Sign in if asked. On **Choose what Bolt can reach**, search for **Fastn Workspace**, tick it and click **Authorize Bolt**.

<figure><img src="../../.gitbook/assets/mcp-bolt-consent.webp" alt="fastn's page titled Choose what Bolt can reach, with the search box set to Fastn Workspace, Fastn Workspace ticked with 212 of 212 tools, Gateway Tools ticked, 215 tools selected and an Authorize Bolt button"><figcaption>Tick <strong>Fastn Workspace</strong>. If you leave it unticked, Bolt gets no fastn tools.</figcaption></figure>

Bolt shows a different screen from other clients here: it doesn't tell fastn which URL it is connecting to, so fastn asks which apps it may reach rather than which workspace to use. Bolt then lists fastn as **Connected** with its tools.

<figure><img src="../../.gitbook/assets/mcp-bolt-connected.webp" alt="Bolt's fastn connector page listing tools such as fastnPlatform__cancelSetupLink, fastnPlatform__cancelWorkflowPromotion and fastnPlatform__claimOnboardingCredits with their descriptions, and a View more button"><figcaption>Every tool is on by default. To turn some off, open the <strong>…</strong> menu and choose <strong>Edit</strong>.</figcaption></figure>
{% endstep %}

{% step %}
#### Turn fastn on for the project

In the chat box, click **+** → **Connectors** and switch **fastn** on.

<figure><img src="../../.gitbook/assets/mcp-bolt-enable-in-chat.webp" alt="Bolt's chat box menu open on Connectors, showing fastn with its toggle switched on and a Manage connectors link"><figcaption>Bolt turns connectors on per project.</figcaption></figure>
{% endstep %}
{% endstepper %}

## Use it

Ask for the outcome in one sentence. To check the connection first, ask *Using the fastn connector, who am I in fastn? Just answer, don't build anything.*

<figure><img src="../../.gitbook/assets/mcp-bolt-answer.webp" alt="Bolt's chat answering Using the fastn connector, who am I in fastn? with Used Fastn fastnPlatform whoami and a reply naming the signed-in user, role, workspace, plan and environment"><figcaption>Bolt shows which fastn tool it used above the answer.</figcaption></figure>

From here Bolt works through the same steps as every agent: see [Building from your AI agent](../building-from-your-ai-agent.md).

## Troubleshooting

* **Bolt lists only connection, skill and feedback.** **Fastn Workspace** wasn't ticked when you authorized. Remove fastn under **Connectors (MCP)**, add it again and tick **Fastn Workspace**.
* **Bolt doesn't use fastn.** Check fastn is switched on under **+** → **Connectors** in this project, then name it in your message, for example *Using the fastn connector, …*.
* **fastn shows Checking or needs sign-in.** Open fastn under **Connectors (MCP)** and connect it again.
