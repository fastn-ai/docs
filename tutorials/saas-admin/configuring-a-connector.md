---
description: >-
  Create a connector, set up OAuth or API key auth, connect your own account,
  and run one of its actions.
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

# Configure a connector

**Build → Integrations → Connectors** · [Open in Fastn](https://app.fastn.dev/integrations)

Create a connector for an app, set up how people sign in to it, connect your own account and run one of its actions.

A [connector](../../build/connectors/README.md) is the definition of one app's API. Build one when the app you need isn't in the [catalog](../../build/connectors/the-catalogue.md). If it is, skip to step 4 and connect to it.

### Before you start

* **Who this is for:** an Owner, Admin, Developer or Operator. Viewers cannot create connectors.
* **What you need:** the app's API docs, and an account on the app you can sign in with or an API key for it. For an OAuth app of your own, its client ID and client secret.
* **What to know:** what connectors and connections are. The [Quickstart: your first integration](../../getting-started/quickstart.md) covers both.

### Steps

1. **Open the Create connector menu.** Go to **Build → Integrations → Connectors** · [Open in Fastn](https://app.fastn.dev/integrations), and select **Create connector** at the top right.

   **You should see:** **From scratch**, **Build in your AI tool**, **Build with fastn agent** and **Import from file**. **Build in your AI tool** and **Build with fastn agent** show only to roles that can use them.
2. **Create the connector.** Pick one way:
   * **Build in your AI tool (recommended):** connect your AI tool to the [Fastn MCP server](../../build/mcp-gateway/README.md), then describe the app (for example, "HubSpot CRM") and give it the vendor's API docs. It works on every plan and uses no Fastn AI credits.
   * **Build with fastn agent:** opens the [Fastn agent](../../build/agent/README.md). Describe the app and give it the API docs. It is on paid plans (Scale or Enterprise); on Launch the item reads *On paid plans. Upgrade to use it.*
   * **From scratch:** fill in the **Create a connector** dialog: **Name**, **Slug** and **Description** under **Identity**; **Protocol** (REST by default) and the app's **Domain** under **Connection**; and one block per auth method under **Authentication** (**Add method** adds another, and **Set as default** picks the one the connect dialog opens with). Then select **Create connector**. Every field, protocol and auth type is in [Create a connector](../../build/connectors/creating-a-connector.md).

   With either AI option, the AI researches the API, builds the actions and auth method, and tests them.

   **You should see:** the new connector in the catalog, badged `Custom`, with version `v1.0` in **Test**.
3. **Add your OAuth app (OAuth only).** Open the connector, go to the **Auth** tab and select **Manage providers**, then **+ Create Provider**. Add your app's client ID, client secret, scopes and endpoints, and make it the preferred app. Follow [Use your own OAuth app](../../build/connectors/auth-methods.md#use-your-own-oauth-app) for each field.

   A Fastn-managed connector already ships with a community app, so you can skip this step for one, unless you want your own app name on the consent screen.

   **You should see:** your provider on the **Auth Providers** page, marked **Preferred app**.
4. **Add a connection.** On the connector's card, select **Connect** (or **Add another connection** if it is already connected), then complete the sign-in:
   * **OAuth 2.0:** a window opens with the app's sign-in screen. Authorize, and you return to Fastn.
   * **API Key, Bearer Token or Basic Auth:** enter the key, token, or username and password, and select **Connect**.

   This connects your own account. Your customers connect theirs through the widget. See [Connect an app](../../build/connectors/connect-an-app.md).

   **You should see:** the connection under **Operate → Connections** · [Open in Fastn](https://app.fastn.dev/connections), with the status `Active`.
5. **Run an action.** Open the connector, select an action in the rail, then select **Run**. Leave **Mock** off, pick your connection under **Connection**, fill in the **Input**, and select **Run Action**. A connector created from scratch has no actions yet: [add one](../../build/connectors/editing-and-deleting.md#add-an-action) first.

   **You should see:** the HTTP status, the time taken, and the response. The action is marked **Live tested**. See [Run an action](../../build/connectors/action-detail.md#run-an-action).

### What's next

* Use the connector in a workflow: [Write a workflow in code](configuring-a-workflow-in-code.md).
* Start the workflow on events: [Set up triggers](setting-up-triggers.md).
* Every auth method in detail: [Auth methods and providers](../../build/connectors/auth-methods.md).
