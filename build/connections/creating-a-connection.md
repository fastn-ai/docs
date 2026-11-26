---
description: "Connect an app for your organization with New connection: pick the app, give the credential or sign in with OAuth, and check the result."
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

# Create a connection

**Operate → Connections** → **New connection** · [Open in Fastn](https://app.fastn.dev/connections)

At the end of this page, your organization has an active connection to an app, ready for your workflows to use.

Use **New connection** for accounts your organization owns, such as your own Slack workspace or data warehouse. It is also the quickest way to test a connector end to end.

Don't make your **customers'** connections here. Customers connect their own accounts through the [widget](../../embed/README.md) you embed, which keeps their credentials theirs.

### Before you start

* **Who this is for:** an Owner, Admin, Developer or Operator. Viewers cannot connect.
* **The connector** for the app, from the [catalog](../connectors/the-catalogue.md) or [created by you](../connectors/creating-a-connector.md).
* **Access to the app's account:** a sign-in that can approve access for OAuth, or the API key or other credential the auth method asks for.

### Connect an app

1. Go to **Operate → Connections** ([Open in Fastn](https://app.fastn.dev/connections)) and select **New connection** (top right).

   **You should see:** the app picker, *Pick the app your customers use. You can add more later.* The list can take a few seconds to load.
2. Type in the search box to narrow the grid, then select the app. The footer counts how many apps match.

   **You should see:** the dialog **Connect** followed by the app's name, tagged with the selected auth method. **←** goes back to the picker.
3. If the connector offers more than one method, choose one in **Auth Method**. It starts on the default.

   **You should see:** the form change to match the method. For example, Airtable's **Bearer Token** method replaces the OAuth sign-in with a single **Bearer Token** field.
4. Give the credential:
   * **API key, bearer token, basic auth and custom methods:** fill in the fields the connector asks for, then select **Connect**. The placeholder usually says where to find the value.
   * **OAuth:** choose the **Auth provider** and **Scopes** (see [Connect with OAuth](#connect-with-oauth)), then select **Authorize**. A new window opens on the app's sign-in and consent page. Sign in and approve access. *Nothing is stored here until you come back.*

   **You should see:** for OAuth, the sign-in window return you to Fastn. For the other methods, go on to the next step.
5. Check the result.

   **You should see:** the new connection in the **My organization** view of [Connections](README.md) and on the connector's **Connections** tab, with the status `Active`.

{% hint style="info" %}
Every credential is *Stored encrypted and scoped to this organization. Your customers never see it, and you can revoke it at any time.* To revoke it, open the connection and select **Disconnect**. See [Inside a connection](inside-a-connection.md#disconnect).
{% endhint %}

You can also open the same connect dialog from a connector's card or detail page. See [Connect an app, step by step](../connectors/connect-an-app.md).

### Connect with OAuth

For an OAuth method, the dialog has these parts:

| Part | Meaning |
| --- | --- |
| **Auth Method** | Shown when the connector offers more than one method. Starts on the default. |
| **Auth provider** | The OAuth app that sends you to the consent screen. **Default** marks the connector's preferred provider. If there are several, **⋯ → Change provider** picks another. See [Auth methods and providers](../connectors/auth-methods.md). |
| **Scopes** | With the default provider: *These are the permissions this connection will ask for on the consent screen. Pick only what you need - you can reconnect with more later.* With any other provider: *Pick only what your OAuth app has enabled - asking for a scope it was not granted makes the consent screen reject the whole connection.* With nothing selected (**All scopes (default)**), every scope the provider declares is requested, and the dialog warns: *Nothing selected, so every scope this provider declares will be requested.* |

### What's next

* [Inside a connection](inside-a-connection.md): check the new connection's token, activity and connection ID.
* [Statuses](statuses.md): what to do when a connection stops working.
