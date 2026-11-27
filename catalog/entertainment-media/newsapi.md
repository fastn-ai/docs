---
description: "NewsAPI collects articles and headlines from news sources and blogs worldwide. Search articles, get top headlines and list sources."
hidden: true
---

# NewsAPI

<img src="../../.gitbook/assets/connectors/lg/newsapi.png" alt="NewsAPI logo">

| | |
| --- | --- |
| **Category** | [Entertainment and media](README.md) |
| **Website** | [newsapi.org](https://newsapi.org) |
| **Authentication** | API key |
| **Slug** | `newsapi` |

## Setup

Your customers enter their API key for NewsAPI when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect NewsAPI from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **NewsAPI**.
2. Select **Connect** on the NewsAPI card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use NewsAPI's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List News Sources</td><td><code>listNewsSources</code></td><td>Lists the news publishers available through NewsAPI, optionally narrowed by category, language or country. Use the returned identifiers in the sources input of the other actions.</td></tr><tr><td>List Top Headlines</td><td><code>listTopHeadlines</code></td><td>Retrieves breaking-news headlines for a country, category or set of sources. The sources input cannot be combined with country or category, and at least one of country, category, sources or the search query must be supplied.</td></tr><tr><td>Search All Articles</td><td><code>searchEverything</code></td><td>Searches every article NewsAPI has indexed from over 150,000 publishers, with full-text keyword search, source and domain filters, a date range and sorting. At least one of the query, title query, sources or domains inputs must be supplied or the API returns a parametersMissing error.</td></tr></tbody></table>

