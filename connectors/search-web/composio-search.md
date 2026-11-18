---
description: "Composio Search is Composio's hosted search toolkit: web, news, image, scholar, shopping, finance, trends, events, flights, hotels, maps, travel and…"
---

# Composio Search

Composio Search is Composio's hosted search toolkit: web, news, image, scholar, shopping, finance, trends, events, flights, hotels, maps, travel and SEC-filing search, plus page-content extraction and fast LLM inference, all without connecting a third-party account. This connector calls the Composio Connect Tool Router over HTTPS (JSON-RPC) and exposes every COMPOSIO_SEARCH tool as its own action.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [composio.dev](https://composio.dev) |
| **Authentication** | API key |
| **Actions** | 22 |
| **Events** | 0 |
| **Slug** | `composioSearch` |

## Use it

Add Composio Search from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.composioSearch.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Fetch URL Content | `fetchUrlContent` | Fetches one or more public web pages and returns clean, readable markdown. Use it to read the full text behind a search result or a documentation link. Supply HTML page URLs only - direct links to images, PDFs or other binary files are not supported. |
| Find Similar Links | `findSimilarLinks` | Given one URL, finds pages across the web that are similar to it. Supports keyword, neural or automatic search modes, a content category, and domain include and exclude lists. The four date-bound fields are currently broken on Composio's side - supplying any of them fails the call with 'Object of type datetime is not JSON serializable' - so leave them empty until Composio fixes it. |
| Get Answer With Citations | `getAnswerWithCitations` | Answers a question from live web sources and returns the answer with its citations. Composio marks this tool deprecated and recommends Search Web instead; it is included for completeness and for callers still on the older flow. |
| Look Up Healthcare Provider | `lookUpHealthcareProvider` | Looks up United States healthcare providers in the CMS NPI Registry (NPPES) by NPI number or by name, organisation, location and specialty, and returns normalised provider details. State cannot be the only filter - combine it with at least one other field. |
| Run Groq Chat Completion | `runGroqChatCompletion` | Runs a chat completion on Groq's fast inference hardware. Put persona and instructions in a system message and keep it short. If the response reports a finish reason of 'length' the output was truncated, so raise the token limit or generate in sections. Note that reasoning models spend the token budget on a reasoning field before writing content, so allow generous headroom. |
| Search Amazon | `searchAmazon` | Searches the Amazon product catalogue, with a choice of international marketplace. Each marketplace domain serves a different country and currency. |
| Search Events | `searchEvents` | Finds upcoming events such as concerts, festivals and conferences, filtered by location, date window and event type. CURRENTLY UNAVAILABLE: Composio's search provider has retired the underlying google_events engine, so every call - with or without filters - returns 'Invalid parameters: Unsupported `google_events` search engine'. The action is kept so it works again the moment Composio restores the engine. The query must name a specific event type; generic values like 'events' return noise. |
| Search Finance | `searchFinance` | Returns real-time quotes, market data and company information for stocks, indices, cryptocurrencies, currency pairs and ETFs, with a selectable historical window. Use exact ticker formats - natural-language names return empty results even when the call succeeds. |
| Search Flights | `searchFlights` | Finds available flights between cities or airports with pricing, schedules and airlines. Either give a natural-language query, or give the origin and destination airport codes; the airport codes are required when no query is supplied. |
| Search Google Maps | `searchGoogleMaps` | Searches Google Maps for places and local businesses. Include the city or region and a category in the query to avoid ambiguous or wrong-region matches, and always check the name and full address of a result before using it. |
| Search Hotels | `searchHotels` | Searches hotels and vacation rentals for a location and date range, with guest counts, price bounds, star rating, free-cancellation and sort filters. If very few results come back, widen the location before changing anything else. |
| Search Images | `searchImages` | Searches Google Images and returns image metadata and URLs, not the binary image data. Supports a result count and page-based pagination. |
| Search News | `searchNews` | Searches news-oriented sources for recent articles and current events, with country, language, recency and pagination filters. Blogs, documentation and company pages are excluded. A call can succeed and still report no results, so widen the query or relax the time filter before concluding there is no coverage. |
| Search Scholar | `searchScholar` | Searches Google Scholar for academic papers and scholarly articles. Short, focused keyphrases work better than long quoted phrases; adding author names, field qualifiers or a year range improves relevance. |
| Search SEC Filings | `searchSecFilings` | Retrieves SEC EDGAR filing metadata for a company and builds the index and primary-document URLs for each filing. Accepts a ticker or a CIK and can be narrowed to specific form types such as 10-K, 10-Q or 8-K. |
| Search Shopping | `searchShopping` | Searches Google Shopping for products, with price-range, sale, free-shipping, location and sort filters. Use it to compare prices across retailers or to find local availability. |
| Search Trends | `searchTrends` | Reads Google Trends data for one or more topics: interest over time, regional breakdowns, and related topics or queries. Interest is normalised from 0 to 100 and is relative to the topics in the same request, so it is not an absolute search volume. |
| Search TripAdvisor | `searchTripAdvisor` | Searches TripAdvisor for attractions, restaurants, hotels, destinations, vacation rentals and forum threads, with no TripAdvisor account required. Ambiguous queries can return several locations, so check both the title and the location of a result before using it. |
| Search Walmart | `searchWalmart` | Searches the Walmart catalogue across groceries, electronics, clothing, home goods, pharmacy and auto services, with optional price-range filtering in US dollars. |
| Search Web | `searchWeb` | Runs a web search through Composio and returns a narrative answer with cited sources. Include qualifiers such as year, region, platform or intent for better results; very broad queries return generic content and excessive site: or quoted-term filters can return nothing. |
| Search With DuckDuckGo | `searchWithDuckDuckGo` | Runs a web search through DuckDuckGo and returns the organic result list. Supports offset pagination for walking past the first page of results. |
| Search With Tavily | `searchWithTavily` | Runs a search through the Tavily engine with domain include and exclude lists, a choice of search depth, and optional direct answers, images and raw page content. Use it when you need finer control over the result set than Search Web offers. |
