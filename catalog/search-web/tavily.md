---
description: "Tavily is a web search service for AI agents. Search the web, extract page content, and crawl and map sites."
hidden: true
---

# Tavily

<img src="../../.gitbook/assets/connectors/lg/tavily.png" alt="Tavily logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [tavily.com](https://tavily.com) |
| **Authentication** | Access token |
| **Slug** | `tavily` |

## Setup

Your customers enter their access token for Tavily when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Tavily from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Tavily**.
2. Select **Connect** on the Tavily card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Tavily's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Crawl</td><td><code>crawl</code></td><td>Crawl a website starting from a root URL and extract content from discovered pages (beta). Returns extracted content per crawled URL. Cost scales with pages crawled; instructions and advanced extract_depth increase credit cost.</td></tr><tr><td>Extract</td><td><code>extract</code></td><td>Extract cleaned page content from one or more URLs (max 20). extract_depth 'basic' = 1 credit per 5 URLs; 'advanced' = 2 credits per 5 URLs and pulls tables/embedded content. Returns raw_content per URL plus any failed URLs.</td></tr><tr><td>Get Usage</td><td><code>getUsage</code></td><td>Get credit usage for the API key and account (no credit cost). Returns per-key and account-level usage, plan limits, pay-as-you-go allocation, and per-endpoint breakdown.</td></tr><tr><td>Map</td><td><code>map</code></td><td>Map a website's URL structure starting from a root URL (beta). Returns a list of discovered URLs without extracting page content. Cheaper than crawl; instructions raise cost to 2 credits per 10 pages.</td></tr><tr><td>Search</td><td><code>search</code></td><td>Execute a real-time web search optimized for LLMs/AI agents. Use search_depth 'basic' (1 credit) for credit-safe runs; 'advanced' (2 credits) for deeper retrieval. Returns ranked results, an optional LLM answer, and optional images.</td></tr></tbody></table>

