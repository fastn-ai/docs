---
description: "Google Programmable Search runs searches against a custom search engine. Search the web or a restricted set of sites."
hidden: true
---

# Google Programmable Search

<img src="../../.gitbook/assets/connectors/lg/google-programmable-search.png" alt="Google Programmable Search logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [programmablesearchengine.google.com](https://programmablesearchengine.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleProgrammableSearch` |

## Setup

Your customers sign in to Google Programmable Search through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Programmable Search from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Programmable Search**.
2. Select **Connect** on the Google Programmable Search card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Programmable Search and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Programmable Search's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search</td><td><code>search</code></td><td>Runs a query against a Programmable Search Engine and returns ranked results with title, snippet, display link and full link.</td></tr><tr><td>Search Site Restricted</td><td><code>searchSiteRestricted</code></td><td>Same as Search but against an engine configured to cover only specific sites; it has no daily query limit.</td></tr></tbody></table>

