---
description: "Zenserp returns search results as structured data. Search Google and Bing, get trends and shopping pages, and run batches."
hidden: true
---

# Zenserp

<img src="../../.gitbook/assets/connectors/lg/zenserp.png" alt="Zenserp logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [zenserp.com](https://zenserp.com) |
| **Authentication** | API key |
| **Slug** | `zenserp` |

## Setup

Your customers enter their API key for Zenserp when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Zenserp from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Zenserp**.
2. Select **Connect** on the Zenserp card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Zenserp's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Bing Search</td><td><code>bingSearch</code></td><td>Runs a Bing web search (search_engine=bing.com) and returns organic results, ads and related content. Paginate with first and count. Consumes one request from your quota.</td></tr><tr><td>Create Batch</td><td><code>createBatch</code></td><td>Submits a batch of search jobs to be processed asynchronously. Each job carries the same parameters as the corresponding synchronous action (search, shopping or trends). Results are POSTed to webhook_url (required by the API) as each job completes, each carrying a job_id and any custom_id; they can also be polled with Get Batch. Every job consumes one request from your quota.</td></tr><tr><td>Get Batch</td><td><code>getBatch</code></td><td>Retrieves a single batch by id, including its processing status and every result that is available so far. Zenserp recommends the batch webhook for delivery, but this endpoint lets you poll manually.</td></tr><tr><td>Get Google Trends</td><td><code>getGoogleTrends</code></td><td>Returns Google Trends interest data for one to five keywords: interest over time, interest by region, related topics and related queries. Filter by category, timeframe, Google property, language and country. Consumes one request from your quota.</td></tr><tr><td>Get Shopping Product Page</td><td><code>getShoppingProductPage</code></td><td>Retrieves a Google Shopping product page by the product_id obtained from a Google Shopping Search. On its own product_id returns a single product variant; adding the gpc_id from the same search result returns the full product cluster across all merchants (description, seller offers, variations). A product_id and gpc_id from two different products is rejected with 400. Consumes one request from your quota.</td></tr><tr><td>Get Status</td><td><code>getStatus</code></td><td>Returns the number of API requests remaining on the plan quota for the connected Zenserp API key. This call does not consume a request.</td></tr><tr><td>Get Trending Searches</td><td><code>getTrendingSearches</code></td><td>Returns the currently trending Google searches, optionally filtered by category, language and country. Consumes one request from your quota.</td></tr><tr><td>Google Image Search</td><td><code>googleImageSearch</code></td><td>Runs a Google image search (tbm=isch) and returns the image results with their source pages, thumbnails and dimensions. There are always 100 images per page; use ijn to page. The start parameter is not supported for image search. Consumes one request from your quota.</td></tr><tr><td>Google Maps Search</td><td><code>googleMapsSearch</code></td><td>Runs a Google Maps / local search and returns local businesses and places with addresses, ratings and coordinates. Use tbm=lcl for the local pack (default) or tbm=map for a maps-specific search, which requires ll. The start parameter is not supported. Consumes one request from your quota.</td></tr><tr><td>Google News Search</td><td><code>googleNewsSearch</code></td><td>Runs a Google News search (tbm=nws) and returns news articles with titles, sources, URLs, snippets and publication dates. Consumes one request from your quota.</td></tr></tbody></table>

<details>

<summary>View 11 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Google Reverse Image Search</td><td><code>googleReverseImageSearch</code></td><td>Runs a Google reverse image search for a publicly reachable image URL and returns the pages that contain the image together with visually similar results. The start parameter is not supported. Consumes one request from your quota.</td></tr><tr><td>Google Search</td><td><code>googleSearch</code></td><td>Runs a Google web search and returns the parsed results page: organic results, paid results (ads), featured snippets, knowledge graph, related questions and more. Optionally switch the result type with tbm (images, videos, maps, news, shopping). Consumes one request from your quota.</td></tr><tr><td>Google Shopping Search</td><td><code>googleShoppingSearch</code></td><td>Runs a Google Shopping search (tbm=shop) and returns product listings with prices, merchants, ratings and product ids that can be passed to Get Shopping Product Page. The start parameter is not supported. Consumes one request from your quota.</td></tr><tr><td>Google Video Search</td><td><code>googleVideoSearch</code></td><td>Runs a Google video search (tbm=vid) and returns the video results with titles, URLs, descriptions and sources. Consumes one request from your quota.</td></tr><tr><td>List Batches</td><td><code>listBatches</code></td><td>Lists every asynchronous batch job submitted with the connected API key, with its status and job count.</td></tr><tr><td>List Countries</td><td><code>listCountries</code></td><td>Returns every supported Google country code (gl) with its display name, for use in the gl parameter of the search actions.</td></tr><tr><td>List Languages</td><td><code>listLanguages</code></td><td>Returns every supported Google interface language code (hl) with its display name, for use in the hl parameter of the search actions.</td></tr><tr><td>List Locations</td><td><code>listLocations</code></td><td>Returns every supported Google geo-location as a canonical name string (e.g. 'Cremona,Lombardy,Italy'), for use in the location parameter of the search actions. The full list is very large (several megabytes) and is not filterable server-side.</td></tr><tr><td>List Search Engines</td><td><code>listSearchEngines</code></td><td>Returns every supported Google search engine domain (e.g. google.com, google.de, google.co.uk), for use in the search_engine parameter of the Google search actions.</td></tr><tr><td>Yandex Search</td><td><code>yandexSearch</code></td><td>Runs a Yandex web search (search_engine=yandex.com) and returns the organic results. Paginate with p and numdoc; restrict by language and timeframe with lang and within. Consumes one request from your quota.</td></tr><tr><td>YouTube Search</td><td><code>youtubeSearch</code></td><td>Runs a YouTube search (search_engine=youtube.com) and returns the video results with titles, channels, view counts and URLs. Any YouTube filter can be supplied through the sp parameter. Consumes one request from your quota.</td></tr></tbody></table>

</details>

