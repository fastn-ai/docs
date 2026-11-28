---
description: "Ceramic AI is a web search service built for AI agents. Run keyword or natural-language web searches."
hidden: true
---

# Ceramic AI

<img src="../../.gitbook/assets/connectors/lg/ceramic-ai.png" alt="Ceramic AI logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [ceramic.ai](https://ceramic.ai) |
| **Authentication** | Access token |
| **Slug** | `ceramicAi` |

## Setup

Your customers enter their access token for Ceramic AI when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Ceramic AI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Ceramic AI**.
2. Select **Connect** on the Ceramic AI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Ceramic AI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Search Web</td><td><code>searchWeb</code></td><td>Searches the web with Ceramic Search and returns ranked results, each with a page title, URL and a content snippet. The query should be in keyword form and contain between 1 and 50 words. Each call consumes one search credit.</td></tr></tbody></table>

