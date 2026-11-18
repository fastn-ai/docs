---
description: "Zenserp is a search engine results page (SERP) scraping API by APILayer."
hidden: true
---

# Zenserp

<img src="../../.gitbook/assets/connectors/lg/zenserp.png" alt="Zenserp logo">

Zenserp is a search engine results page (SERP) scraping API by APILayer. This connector covers the complete Zenserp API: Google web, image, video, maps, news and shopping search, reverse image search, Google Shopping product pages, YouTube, Bing and Yandex search, Google Trends and trending searches, the supported languages, countries, geo-locations and search-engine lookup lists, asynchronous batch jobs, and the remaining-requests status check. Every search request consumes one request from your plan quota.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [zenserp.com](https://zenserp.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `zenserp` |

## Use it

Add Zenserp from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zenserp.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bing Search | `bingSearch` | Runs a Bing web search (search_engine=bing.com) and returns organic results, ads and related content. Paginate with first and count. Consumes one request from your quota. |
| Create Batch | `createBatch` | Submits a batch of search jobs to be processed asynchronously. Each job carries the same parameters as the corresponding synchronous action (search, shopping or trends). Results are POSTed to webhook_url (required by the API) as each job completes, each carrying a job_id and any custom_id; they can also be polled with Get Batch. Every job consumes one request from your quota. |
| Get Batch | `getBatch` | Retrieves a single batch by id, including its processing status and every result that is available so far. Zenserp recommends the batch webhook for delivery, but this endpoint lets you poll manually. |
| Get Google Trends | `getGoogleTrends` | Returns Google Trends interest data for one to five keywords: interest over time, interest by region, related topics and related queries. Filter by category, timeframe, Google property, language and country. Consumes one request from your quota. |
| Get Shopping Product Page | `getShoppingProductPage` | Retrieves a Google Shopping product page by the product_id obtained from a Google Shopping Search. On its own product_id returns a single product variant; adding the gpc_id from the same search result returns the full product cluster across all merchants (description, seller offers, variations). A product_id and gpc_id from two different products is rejected with 400. Consumes one request from your quota. |
| Get Status | `getStatus` | Returns the number of API requests remaining on the plan quota for the connected Zenserp API key. This call does not consume a request. |
| Get Trending Searches | `getTrendingSearches` | Returns the currently trending Google searches, optionally filtered by category, language and country. Consumes one request from your quota. |
| Google Image Search | `googleImageSearch` | Runs a Google image search (tbm=isch) and returns the image results with their source pages, thumbnails and dimensions. There are always 100 images per page; use ijn to page. The start parameter is not supported for image search. Consumes one request from your quota. |
| Google Maps Search | `googleMapsSearch` | Runs a Google Maps / local search and returns local businesses and places with addresses, ratings and coordinates. Use tbm=lcl for the local pack (default) or tbm=map for a maps-specific search, which requires ll. The start parameter is not supported. Consumes one request from your quota. |
| Google News Search | `googleNewsSearch` | Runs a Google News search (tbm=nws) and returns news articles with titles, sources, URLs, snippets and publication dates. Consumes one request from your quota. |

<details>

<summary>See 11 more actions</summary>

* **Google Reverse Image Search** `googleReverseImageSearch`: Runs a Google reverse image search for a publicly reachable image URL and returns the pages that contain the image together with visually similar results. The start parameter is not supported. Consumes one request from your quota.
* **Google Search** `googleSearch`: Runs a Google web search and returns the parsed results page: organic results, paid results (ads), featured snippets, knowledge graph, related questions and more. Optionally switch the result type with tbm (images, videos, maps, news, shopping). Consumes one request from your quota.
* **Google Shopping Search** `googleShoppingSearch`: Runs a Google Shopping search (tbm=shop) and returns product listings with prices, merchants, ratings and product ids that can be passed to Get Shopping Product Page. The start parameter is not supported. Consumes one request from your quota.
* **Google Video Search** `googleVideoSearch`: Runs a Google video search (tbm=vid) and returns the video results with titles, URLs, descriptions and sources. Consumes one request from your quota.
* **List Batches** `listBatches`: Lists every asynchronous batch job submitted with the connected API key, with its status and job count.
* **List Countries** `listCountries`: Returns every supported Google country code (gl) with its display name, for use in the gl parameter of the search actions.
* **List Languages** `listLanguages`: Returns every supported Google interface language code (hl) with its display name, for use in the hl parameter of the search actions.
* **List Locations** `listLocations`: Returns every supported Google geo-location as a canonical name string (e.g. 'Cremona,Lombardy,Italy'), for use in the location parameter of the search actions. The full list is very large (several megabytes) and is not filterable server-side.
* **List Search Engines** `listSearchEngines`: Returns every supported Google search engine domain (e.g. google.com, google.de, google.co.uk), for use in the search_engine parameter of the Google search actions.
* **Yandex Search** `yandexSearch`: Runs a Yandex web search (search_engine=yandex.com) and returns the organic results. Paginate with p and numdoc; restrict by language and timeframe with lang and within. Consumes one request from your quota.
* **YouTube Search** `youtubeSearch`: Runs a YouTube search (search_engine=youtube.com) and returns the video results with titles, channels, view counts and URLs. Any YouTube filter can be supplied through the sp parameter. Consumes one request from your quota.

</details>
