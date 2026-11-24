---
description: Add fastn to GitHub Copilot in your editor, sign in, and use your fastn tools from Copilot Chat in agent mode.
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

# GitHub Copilot

GitHub Copilot uses the MCP servers you add in the editor it runs in, not on github.com. Add fastn to that editor once, sign in, then ask Copilot for the integration in Copilot Chat's **Agent** mode.

{% hint style="info" %}
**Before you start:** you need a Copilot license and an up-to-date Copilot extension or plugin. On Copilot Business or Enterprise, your organization must turn on the **MCP servers in Copilot** policy, which is off by default. Copilot Free, Pro, Pro+ and Max aren't affected by this policy.
{% endhint %}

## Add fastn in VS Code

In fastn, click **Connect your AI tool** in the top bar (or open **Embed → MCP server**), pick the **GitHub Copilot** tile and click **Install in VS Code**. Then follow [VS Code](vscode.md) from the **Install the server** step: install fastn, start it, and sign in.

## Add fastn in another editor

Each editor stores its MCP servers in an `mcp.json` file under the key `servers`. Add fastn with only its URL. fastn signs you in with OAuth 2.0 and dynamic client registration, so leave out any token, header, client ID or client secret.

```json
{
  "servers": {
    "fastn": {
      "url": "https://mcp.fastn.dev/fastn-workspace"
    }
  }
}
```

{% tabs %}
{% tab title="Visual Studio" %}
1. Click **View** → **GitHub Copilot Chat** and set the mode at the bottom of the chat panel to **Agent**.
2. Click the tools icon, then the plus icon in the tool picker.
3. In **Configure MCP server**, enter `fastn` as the server ID, set the type to **HTTP/SSE**, enter `https://mcp.fastn.dev/fastn-workspace` as the URL, and click **Save**.
4. In `mcp.json`, click **Auth** above the fastn entry and sign in to fastn in the browser.
{% endtab %}

{% tab title="JetBrains IDEs" %}
1. Click the Copilot icon at the bottom right and choose **Open Chat**. Make sure the chat is in **Agent** mode.
2. Click the tools icon (**Configure your MCP server**), then **Add MCP Tools**. `mcp.json` opens.
3. Add the fastn entry above and save the file.
4. Sign in to fastn in the browser when Copilot asks.
{% endtab %}

{% tab title="Xcode" %}
1. Click **Editor** → **GitHub Copilot** → **Open GitHub Copilot for Xcode Settings**.
2. Open the **MCP** tab and click **Edit Config**.
3. Add the fastn entry above and save the file.
4. Sign in to fastn in the browser when Copilot asks.
{% endtab %}

{% tab title="Eclipse" %}
1. Click the Copilot icon in the status bar and choose **Open Chat**, then click the **Configure Tools...** icon. You can also open the preferences and go to **GitHub Copilot** → **MCP**.
2. Under **Server Configurations**, add the fastn entry above and save.
3. Sign in to fastn in the browser when Copilot asks.
{% endtab %}
{% endtabs %}

If you belong to more than one fastn org, fastn asks which workspace Copilot works in. Pick it and click **Connect**. **The org selected in fastn** follows whichever org you have open in the fastn dashboard; picking a named org pins Copilot to it.

## Use it

1. Open Copilot Chat and set the mode to **Agent**. Ask and Edit modes don't use MCP servers.
2. Click the tools icon in the chat box and check that **fastn** is listed and turned on.
3. Ask for the outcome in one sentence. To check the connection first, ask *Who am I in fastn?*
4. Copilot asks before it runs a fastn tool. Approve it to continue.

From here Copilot works through the same steps as every AI tool: see [Build from your AI tool](../building-from-your-ai-agent.md).

## Copilot cloud agent

Copilot's cloud agent (the coding agent that works on issues and pull requests on github.com) and Copilot code review can't use fastn. They read MCP servers from a repository's **Settings** → **Copilot** → **MCP servers** page, and they don't support remote servers that sign in with OAuth. fastn has no API key or token to put in a header instead, so use fastn from Copilot in your editor.

## Troubleshooting

* **fastn is added but Copilot never uses it.** Check that the chat is in **Agent** mode and that fastn is turned on under the tools icon.
* **The tools icon or the MCP settings are missing.** On Copilot Business or Enterprise, ask an organization owner to turn on the **MCP servers in Copilot** policy. Then update the Copilot extension or plugin.
* **Copilot works on the wrong org.** Remove fastn from `mcp.json`, sign out of fastn in the editor, then add it again and pick the workspace when you sign in. In VS Code, follow the steps in [VS Code](vscode.md#troubleshooting).
