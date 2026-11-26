---
description: "Making a connection step by step: open the connect dialog, choose the auth method, give the credential, and check that it worked."
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

# Connect an app, step by step

**Build → Integrations → Connectors** · [Open in Fastn](https://app.fastn.dev/integrations)

Make a connection, so a connector can call an app as your account.

A connection is what lets a connector call an app as a specific account. Connecting here signs in **your own** account, for your organization's workflows and for testing. It does not connect your customers: they connect their own accounts through the [widget](../../embed/README.md) you embed.

{% hint style="info" %}
**Do this from your AI tool.** Fastn recommends connecting your preferred AI agent, such as Claude, Cursor or VS Code, to the [Fastn MCP server](../mcp-gateway/README.md) and using its tools to connect apps. For example, ask it: *"Connect my HubSpot account."* You then sign in to the app in your browser. To connect your AI agent, see [Connect your AI tool](../mcp-gateway/README.md#open-the-connect-dialog), or the setup guide for [Claude](../mcp-gateway/claude.md), [Claude Code](../mcp-gateway/claude-code.md), [Cursor](../mcp-gateway/cursor.md), [VS Code](../mcp-gateway/vscode.md) or [any other MCP client](../mcp-gateway/README.md#how-your-ai-tool-connects).
{% endhint %}

### Before you start

* **Who this is for:** an Owner, Admin, Developer or Operator. Viewers cannot connect.
* **The connector** for the app, in the [catalog](the-catalogue.md) or [created by you](creating-a-connector.md).
* **Access to the app's account:** a sign-in that can approve access for OAuth, or the API key or other credential the auth method asks for.

### Where to connect from

These all open the same connect dialog:

* **Catalog card:** **Connect** on a connector's card in the [catalog](the-catalogue.md), or **Add another connection** on a card that is already connected.
* **Connector detail page:** **Connect** in the header, or on the **Connections** tab, of the [connector detail page](inside-a-connector.md).
* **Connections page:** **New connection** on **Operate → Connections** · [Open in Fastn](https://app.fastn.dev/connections), then pick the app.
* **Rail:** **⋯ → Connect** on the connector's row in the rail, for a connector your workspace owns.

### Connect

1. **Open the connect dialog.** Go to **Build → Integrations → Connectors** · [Open in Fastn](https://app.fastn.dev/integrations), find the app, and select **Connect** on its card, or use any of the entry points above.

   **You should see:** a dialog titled **Connect &lt;app&gt;**, with the chosen auth method shown next to the name.
2. **Choose the auth method.** If the connector offers more than one method, an **Auth Method** selector appears. It starts on the connector's default method. Pick another if you need to, for example a personal access token instead of OAuth. See [How the default method is chosen](auth-methods.md#how-the-default-method-is-chosen).

   **You should see:** the fields for the method you picked.
3. **Give the credential.** What the dialog asks for depends on the method:
   * **API key, bearer token, and other keyed methods:** the dialog shows one field per credential, for example **API Key**. Paste the value and click **Connect**.
   * **OAuth 2.0:** the dialog shows *You will authorize in a new window*, the **Auth provider** it uses, and **Scopes**. Click **Authorize**, sign in to the app in the new window, and approve access. The scope and provider options are explained in [Create a connection](../connections/creating-a-connection.md#connect-with-oauth).

   **You should see:** the card's badge change to **Connected** and its button to **Add another connection**.
4. **Check that it worked.** Open the connector's **Connections** tab, or **Operate → Connections** · [Open in Fastn](https://app.fastn.dev/connections).

   **You should see:** the new connection, with the status `Active`.

{% hint style="info" %}
Every credential is *Stored encrypted and scoped to this organization. Your customers never see it, and you can revoke it at any time.* When you connect on behalf of one customer, the note reads *Stored encrypted and scoped to this customer. Other customers cannot see or use it.* To revoke it, disconnect the connection; see [Inside a connection](../connections/inside-a-connection.md).
{% endhint %}

### What's next

* [Actions](action-detail.md#run-an-action): run an action with your new connection.
* [Connections](../connections/README.md): manage connections, including your customers'.
