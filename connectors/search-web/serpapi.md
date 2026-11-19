---
description: "SerpAPI returns search engine results as structured data. Search Google, Bing, Amazon, eBay, app stores and more."
hidden: true
---

# SerpAPI

<img src="../../.gitbook/assets/connectors/lg/serpapi.png" alt="SerpAPI logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [serpapi.com](https://serpapi.com) |
| **Authentication** | API key |
| **Slug** | `serpapi` |

## Setup

Your customers enter their API key for SerpAPI when they connect. Nothing else needs setting up.

## Use it

Add SerpAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.serpapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Amazon Search</td><td><code>amazonSearch</code></td><td>Amazon product search via SerpAPI (engine=amazon). NOTE: query param is 'k'. Returns organic_results, product_ads. Consumes 1 credit.</td></tr><tr><td>Apple App Store Search</td><td><code>appleAppStoreSearch</code></td><td>Apple App Store search via SerpAPI (engine=apple_app_store). NOTE: query param is 'term'. Returns organic_results. Consumes 1 credit.</td></tr><tr><td>Baidu Search</td><td><code>baiduSearch</code></td><td>Baidu web search via SerpAPI (engine=baidu). Returns organic_results, related_searches. Consumes 1 credit.</td></tr><tr><td>Bing Search</td><td><code>bingSearch</code></td><td>Bing web search via SerpAPI (engine=bing). Returns organic_results, ads, related_searches. Paginate with 'first'. Consumes 1 credit.</td></tr><tr><td>DuckDuckGo Search</td><td><code>duckduckgoSearch</code></td><td>DuckDuckGo web search via SerpAPI (engine=duckduckgo). Returns organic_results, knowledge_graph, related_searches. Consumes 1 credit.</td></tr><tr><td>eBay Search</td><td><code>ebaySearch</code></td><td>eBay search via SerpAPI (engine=ebay). NOTE: query param is '_nkw'. Returns organic_results. Consumes 1 credit.</td></tr><tr><td>Get Account</td><td><code>getAccount</code></td><td>Retrieve SerpAPI account information: plan, monthly search quota, credits left, and current usage. FREE — this call does NOT consume search credits. Ideal for validating a connection.</td></tr><tr><td>Get Search Archive</td><td><code>getSearchArchive</code></td><td>Retrieve the JSON results of a previously executed search by its search_id (from search_metadata.id). FREE — re-fetching an archived search does not consume credits. Results stay available for up to 31 days.</td></tr><tr><td>Google Images Search</td><td><code>googleImagesSearch</code></td><td>Google Images search via SerpAPI (engine=google_images). Returns images_results plus suggested/related searches. Consumes 1 credit.</td></tr><tr><td>Google Jobs Search</td><td><code>googleJobsSearch</code></td><td>Google Jobs via SerpAPI (engine=google_jobs). Returns jobs_results and filters. Paginate with next_page_token. Consumes 1 credit.</td></tr></tbody></table>

<details>

<summary>View 15 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Google Local Search</td><td><code>googleLocalSearch</code></td><td>Google Local results via SerpAPI (engine=google_local). Returns local_results (the local pack). Consumes 1 credit.</td></tr><tr><td>Google Maps Search</td><td><code>googleMapsSearch</code></td><td>Google Maps search via SerpAPI (engine=google_maps). type=search returns local_results; type=place returns place_results. Consumes 1 credit.</td></tr><tr><td>Google News Search</td><td><code>googleNewsSearch</code></td><td>Google News via SerpAPI (engine=google_news). Use q for keyword search, or topic_token/publication_token/story_token/section_token to browse. Returns news_results. Consumes 1 credit.</td></tr><tr><td>Google Patents Search</td><td><code>googlePatentsSearch</code></td><td>Google Patents via SerpAPI (engine=google_patents). Returns organic_results of patents. Consumes 1 credit.</td></tr><tr><td>Google Play Search</td><td><code>googlePlaySearch</code></td><td>Google Play Store via SerpAPI (engine=google_play). store selects apps/games/movies/books. Returns organic_results / top_charts. Consumes 1 credit.</td></tr><tr><td>Google Scholar Search</td><td><code>googleScholarSearch</code></td><td>Google Scholar via SerpAPI (engine=google_scholar). Returns scholarly organic_results with citation info. Consumes 1 credit.</td></tr><tr><td>Google Search</td><td><code>googleSearch</code></td><td>Google web search via SerpAPI (engine=google). Returns organic results, knowledge graph, ads, related searches/questions. Consumes 1 credit.</td></tr><tr><td>Google Shopping Search</td><td><code>googleShoppingSearch</code></td><td>Google Shopping via SerpAPI (engine=google_shopping). Returns shopping_results and filters. Consumes 1 credit.</td></tr><tr><td>Google Trends</td><td><code>googleTrends</code></td><td>Google Trends via SerpAPI (engine=google_trends). data_type selects TIMESERIES/GEO_MAP/RELATED_TOPICS/RELATED_QUERIES. Consumes 1 credit.</td></tr><tr><td>Home Depot Search</td><td><code>homeDepotSearch</code></td><td>Home Depot product search via SerpAPI (engine=home_depot). Returns products. Consumes 1 credit.</td></tr><tr><td>Search (Generic)</td><td><code>search</code></td><td>Generic SerpAPI search. Select the source with the 'engine' parameter (e.g. google, bing, google_maps, youtube, amazon). Supports all universal SERP parameters. Consumes 1 search credit per call. Use engine-specific convenience actions when available for clearer parameter modeling.</td></tr><tr><td>Search Locations</td><td><code>searchLocations</code></td><td>Look up supported locations for use in the 'location' search parameter. FREE — does not consume search credits. Returns an array of locations ordered by reach (top-level JSON array).</td></tr><tr><td>Walmart Search</td><td><code>walmartSearch</code></td><td>Walmart search via SerpAPI (engine=walmart). NOTE: query param is 'query'. Returns organic_results. Consumes 1 credit.</td></tr><tr><td>Yahoo Search</td><td><code>yahooSearch</code></td><td>Yahoo web search via SerpAPI (engine=yahoo). NOTE: query param is 'p'. Returns organic_results, related_searches. Consumes 1 credit.</td></tr><tr><td>YouTube Search</td><td><code>youtubeSearch</code></td><td>YouTube search via SerpAPI (engine=youtube). NOTE: query param is 'search_query'. Returns video_results, channel_results, etc. Consumes 1 credit.</td></tr></tbody></table>

</details>

## Events

SerpAPI has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
