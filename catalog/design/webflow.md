---
description: "Webflow is a visual website builder. List the sites you can access and get the connected user."
hidden: true
---

# Webflow

<img src="../../.gitbook/assets/connectors/lg/webflow.png" alt="Webflow logo">

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [webflow.com](https://webflow.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `webflow` |

## Setup

Your customers sign in to Webflow through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Webflow from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Webflow**.
2. Select **Connect** on the Webflow card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Webflow and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Webflow's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Authorized User</td><td><code>getAuthorizedUser</code></td><td>Retrieves the Webflow user who authorized the current access token. Useful for identifying the connected account. Requires the authorized_user:read scope.</td></tr><tr><td>Introspect Token</td><td><code>introspectToken</code></td><td>Retrieves information about the current authorization, including the granted scopes, rate limit, and the sites, workspaces, and users the token is authorized to access, along with details of the Webflow application.</td></tr><tr><td>List Sites</td><td><code>listSites</code></td><td>Lists all Webflow sites the authorized token has access to. Returns an empty list when the token is not authorized to any site. Requires the sites:read scope.</td></tr></tbody></table>

