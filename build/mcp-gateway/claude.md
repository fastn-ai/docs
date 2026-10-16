---
description: Add fastn to Claude as a custom connector, then build integrations from a Claude chat.
---

# Claude

Add fastn once, switch it on in a chat, then ask for the integration in one sentence.

### Add fastn

1. In fastn, open **Connect an agent** and click **Add to Claude**. Claude opens the **Add custom connector** form with the name and URL already filled in.
2. Or add it by hand: in Claude, open **Customize** → **Connectors**, click **Add** → **Add custom connector**, enter **Name** `fastn` and **MCP server URL** `https://mcp.fastn.dev/fastn-workspace`, then click **Continue**.
3. Open the fastn connector. Claude shows *You're not connected to Fastn yet*. Click **Connect**.

<figure><img src="../../.gitbook/assets/mcp-claude-not-connected.png" alt="Claude's fastn connector page reading You're not connected to Fastn yet, with a Connect button"><figcaption>The fastn connector in Claude before you connect it.</figcaption></figure>

4. fastn opens **Choose what Claude can reach**. Pick your workspace, then choose which apps and tools Claude may use: **Select all**, **Reads only**, or tick them one by one. Click **Authorize Claude**.

<figure><img src="../../.gitbook/assets/mcp-claude-choose-access.png" alt="fastn's Choose what Claude can reach page: a workspace picker, a search box, apps and tools to tick with a count per app, Select all, Reads only and Clear links, and an Authorize Claude button"><figcaption>Apps marked <strong>Connect account</strong> can be linked later, the first time Claude uses one of their tools. Fewer tools selected means Claude picks the right one faster; you can change the list later.</figcaption></figure>

5. fastn now shows in your connector list as **Web · Custom · Individual**.

<figure><img src="../../.gitbook/assets/mcp-claude-connector-list.png" alt="Claude's Connectors list with Fastn shown as type Web, Custom, authorization Individual, and a check under Status"><figcaption>fastn in Claude's connector list (<strong>Customize</strong> → <strong>Connectors</strong>).</figcaption></figure>

On a Claude Team or Enterprise plan, only an organisation owner can add a custom connector. Members see the note below and connect their own account once the owner has added fastn.

<figure><img src="../../.gitbook/assets/mcp-claude-team-owner-only.png" alt="Claude's Add custom connector option greyed out, with the note Ask an organization owner to add this for your team"><figcaption>What a Team or Enterprise member sees in place of <strong>Add custom connector</strong>.</figcaption></figure>

Admins can click **Add for the whole organisation** in the same fastn dialog instead.

If you belong to more than one Claude workspace (for example Personal and a Team), add fastn in the workspace you chat in. A connector only shows in the workspace it was added to.

### Use it in a chat

1. In a new chat, click **+** → **Connectors** and switch **fastn** on.

<figure><img src="../../.gitbook/assets/mcp-claude-chat-connectors.png" alt="Claude's chat + menu open on Connectors, with Fastn switched on"><figcaption>Switch fastn on for the chat.</figcaption></figure>

2. Ask for the outcome in one sentence.

<figure><img src="../../.gitbook/assets/mcp-claude-prompt.png" alt="A Claude message reading: Using fastn, save invoice emails from Gmail to a Google Sheet. Test it, then add it to my widget."><figcaption>The prompt used for the screenshots on this page.</figcaption></figure>

Name the systems, what starts it and what moves. [Writing a good first message](../agent/README.md#writing-a-good-first-message) has examples.

3. Each time Claude wants to use a fastn tool, it asks: **Allow once**, **Always allow** or **Deny**. It starts with read-only checks of your workspace.

<figure><img src="../../.gitbook/assets/mcp-claude-tool-approval.png" alt="Claude asking to use FastnPlatform whoami from Fastn, with Deny, Always allow and Allow once buttons"><figcaption>The first call is a read-only check of who you are.</figcaption></figure>

4. Claude then asks only the business questions it can't answer itself. Its recommended answer is already selected.

<figure><img src="../../.gitbook/assets/mcp-claude-question-invoice.png" alt="Claude asking What counts as an invoice email?, with Subject or body mentions invoice marked recommended"><figcaption>A business question, with the recommended answer first.</figcaption></figure>

<figure><img src="../../.gitbook/assets/mcp-claude-question-accounts.png" alt="Claude asking Whose accounts does this run against?, with My own Gmail/Sheets marked recommended and My customers connect their own accounts as the other option"><figcaption>Whose accounts the integration runs against: yours, or your customers' connected accounts.</figcaption></figure>

From here Claude works through the same steps as every agent: see [Building from your AI agent](../building-from-your-ai-agent.md).

### Claude Code and Claude Desktop

* Claude Code: `claude mcp add --transport http fastn https://mcp.fastn.dev/fastn-workspace`
* Claude Desktop config file: add `fastn` under `mcpServers` with `npx -y mcp-remote https://mcp.fastn.dev/fastn-workspace`.

{% hint style="info" %}
This page is for your own team. Your customers reach their integrations from Claude a different way: see [Connecting Claude and other AI clients](../../tutorials/end-user/connecting-claude.md).
{% endhint %}
