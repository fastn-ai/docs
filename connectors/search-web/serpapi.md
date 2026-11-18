---
description: "SerpAPI — scrape Google and other search engines in real time and get structured JSON results."
---

# SerpAPI

SerpAPI — scrape Google and other search engines in real time and get structured JSON results. Wraps the SerpAPI Search API (GET /search with an engine selector), Search Archive, Account, and Locations endpoints. Covers Google web/maps/images/news/scholar/jobs/shopping/trends/local/patents/play, plus Bing, DuckDuckGo, Yahoo, Baidu, YouTube, eBay, Walmart, Amazon, Home Depot, and the Apple App Store.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [serpapi.com](https://serpapi.com) |
| **Authentication** | API key |
| **Actions** | 25 |
| **Events** | 0 |
| **Slug** | `serpapi` |

## Use it

Add SerpAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.serpapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Amazon Search | `amazonSearch` | Amazon product search via SerpAPI (engine=amazon). NOTE: query param is 'k'. Returns organic_results, product_ads. Consumes 1 credit. |
| Apple App Store Search | `appleAppStoreSearch` | Apple App Store search via SerpAPI (engine=apple_app_store). NOTE: query param is 'term'. Returns organic_results. Consumes 1 credit. |
| Baidu Search | `baiduSearch` | Baidu web search via SerpAPI (engine=baidu). Returns organic_results, related_searches. Consumes 1 credit. |
| Bing Search | `bingSearch` | Bing web search via SerpAPI (engine=bing). Returns organic_results, ads, related_searches. Paginate with 'first'. Consumes 1 credit. |
| DuckDuckGo Search | `duckduckgoSearch` | DuckDuckGo web search via SerpAPI (engine=duckduckgo). Returns organic_results, knowledge_graph, related_searches. Consumes 1 credit. |
| eBay Search | `ebaySearch` | eBay search via SerpAPI (engine=ebay). NOTE: query param is '_nkw'. Returns organic_results. Consumes 1 credit. |
| Get Account | `getAccount` | Retrieve SerpAPI account information: plan, monthly search quota, credits left, and current usage. FREE — this call does NOT consume search credits. Ideal for validating a connection. |
| Get Search Archive | `getSearchArchive` | Retrieve the JSON results of a previously executed search by its search_id (from search_metadata.id). FREE — re-fetching an archived search does not consume credits. Results stay available for up to 31 days. |
| Google Images Search | `googleImagesSearch` | Google Images search via SerpAPI (engine=google_images). Returns images_results plus suggested/related searches. Consumes 1 credit. |
| Google Jobs Search | `googleJobsSearch` | Google Jobs via SerpAPI (engine=google_jobs). Returns jobs_results and filters. Paginate with next_page_token. Consumes 1 credit. |
| Google Local Search | `googleLocalSearch` | Google Local results via SerpAPI (engine=google_local). Returns local_results (the local pack). Consumes 1 credit. |
| Google Maps Search | `googleMapsSearch` | Google Maps search via SerpAPI (engine=google_maps). type=search returns local_results; type=place returns place_results. Consumes 1 credit. |
| Google News Search | `googleNewsSearch` | Google News via SerpAPI (engine=google_news). Use q for keyword search, or topic_token/publication_token/story_token/section_token to browse. Returns news_results. Consumes 1 credit. |
| Google Patents Search | `googlePatentsSearch` | Google Patents via SerpAPI (engine=google_patents). Returns organic_results of patents. Consumes 1 credit. |
| Google Play Search | `googlePlaySearch` | Google Play Store via SerpAPI (engine=google_play). store selects apps/games/movies/books. Returns organic_results / top_charts. Consumes 1 credit. |
| Google Scholar Search | `googleScholarSearch` | Google Scholar via SerpAPI (engine=google_scholar). Returns scholarly organic_results with citation info. Consumes 1 credit. |
| Google Search | `googleSearch` | Google web search via SerpAPI (engine=google). Returns organic results, knowledge graph, ads, related searches/questions. Consumes 1 credit. |
| Google Shopping Search | `googleShoppingSearch` | Google Shopping via SerpAPI (engine=google_shopping). Returns shopping_results and filters. Consumes 1 credit. |
| Google Trends | `googleTrends` | Google Trends via SerpAPI (engine=google_trends). data_type selects TIMESERIES/GEO_MAP/RELATED_TOPICS/RELATED_QUERIES. Consumes 1 credit. |
| Home Depot Search | `homeDepotSearch` | Home Depot product search via SerpAPI (engine=home_depot). Returns products. Consumes 1 credit. |
| Search (Generic) | `search` | Generic SerpAPI search. Select the source with the 'engine' parameter (e.g. google, bing, google_maps, youtube, amazon). Supports all universal SERP parameters. Consumes 1 search credit per call. Use engine-specific convenience actions when available for clearer parameter modeling. |
| Search Locations | `searchLocations` | Look up supported locations for use in the 'location' search parameter. FREE — does not consume search credits. Returns an array of locations ordered by reach (top-level JSON array). |
| Walmart Search | `walmartSearch` | Walmart search via SerpAPI (engine=walmart). NOTE: query param is 'query'. Returns organic_results. Consumes 1 credit. |
| Yahoo Search | `yahooSearch` | Yahoo web search via SerpAPI (engine=yahoo). NOTE: query param is 'p'. Returns organic_results, related_searches. Consumes 1 credit. |
| YouTube Search | `youtubeSearch` | YouTube search via SerpAPI (engine=youtube). NOTE: query param is 'search_query'. Returns video_results, channel_results, etc. Consumes 1 credit. |
