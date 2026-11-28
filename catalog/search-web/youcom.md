---
description: "You.com is a web search service for AI apps. Search the web and news, fetch page contents and run research."
hidden: true
---

# You.com

<img src="../../.gitbook/assets/connectors/lg/youcom.png" alt="You.com logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [you.com](https://you.com) |
| **Authentication** | API key |
| **Slug** | `youcom` |

## Setup

Your customers enter their API key for You.com when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect You.com from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **You.com**.
2. Select **Connect** on the You.com card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use You.com's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Contents</td><td><code>getContents</code></td><td>Contents API — POST https://ydc-index.io/v1/contents. Fetches full page content for a list of URLs as HTML, markdown, and/or metadata. Useful after a Search to retrieve full article text.</td></tr><tr><td>Research</td><td><code>research</code></td><td>Research API — POST https://api.you.com/v1/research. Deep-search agent that returns a grounded answer with cited sources for a research question. research_effort controls depth/cost (lite/standard/deep/exhaustive). source_control filters domains/freshness/country; output_schema returns structured JSON (requires standard+). This is the MOST EXPENSIVE endpoint — avoid for casual validation.</td></tr><tr><td>Search</td><td><code>search</code></td><td>Search API — GET https://ydc-index.io/v1/search. Returns LLM-optimized web and news results for a query. Supports freshness, country/language, safesearch, domain include/exclude/boost, and optional livecrawl to fetch full-page HTML/markdown. CHEAPEST endpoint ($5/1000 calls) — use this (count=1, no livecrawl) for credit-safe validation.</td></tr></tbody></table>

