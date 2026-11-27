---
description: "Mediastack provides live and historical news from thousands of sources worldwide. Get live and past news and search news sources."
hidden: true
---

# Mediastack

<img src="../../.gitbook/assets/connectors/lg/mediastack.png" alt="Mediastack logo">

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [mediastack.com](https://mediastack.com) |
| **Authentication** | API key |
| **Slug** | `mediastack` |

## Setup

Your customers enter their API key for Mediastack when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Mediastack from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Mediastack**.
2. Select **Connect** on the Mediastack card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Mediastack's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Historical News</td><td><code>getHistoricalNews</code></td><td>Returns past news articles for a specific historical date or date range, optionally filtered by source, category, country, language, or keyword. Historical lookups are documented as a Standard-plan feature; on the connected Free-plan account this call was live-verified to succeed.</td></tr><tr><td>Get Live News</td><td><code>getLiveNews</code></td><td>Returns the most recent real-time news articles from Mediastack's worldwide sources, optionally filtered by source, category, country, language, or keyword. Free-plan accounts receive live news with a 30-minute publication delay.</td></tr><tr><td>Search News Sources</td><td><code>searchNewsSources</code></td><td>Searches Mediastack's directory of supported news sources by keyword, optionally filtered by country, language, or category. Returns source metadata including the source code used to filter live and historical news requests.</td></tr></tbody></table>

