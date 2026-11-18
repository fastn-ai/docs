---
description: "Autom is a SERP and web-data API: structured results from Google Search, Google Search Light, Autocomplete, Images, News, Videos, Shopping, Jobs and Maps,…"
hidden: true
---

# Autom

<img src="../../.gitbook/assets/connectors/lg/autom.png" alt="Autom logo">

Autom is a SERP and web-data API: structured results from Google Search, Google Search Light, Autocomplete, Images, News, Videos, Shopping, Jobs and Maps, plus Bing and Brave search, with credit-based billing. This connector covers the complete Autom REST API v1: every search engine endpoint with pagination, localisation (gl, hl, location, uule) and the global fields and is_async parameters, the free Finder lookups for Google countries, languages and locations, asynchronous job retrieval, account usage and quota, and platform infrastructure stats.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [autom.dev](https://autom.dev) |
| **Authentication** | API key |
| **Slug** | `autom` |

## Use it

Add Autom from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.autom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bing Search | `bingSearch` | Queries Bing Search and returns structured organic results (title, link, domain, snippet, position) with pagination info and localisation by location, GPS coordinates, market or country. Costs 1 credit per call. Known vendor defect (verified 2026-09-16): sending the documented page parameter, with any value, makes Autom return HTTP 500 Internal Error; omit page until Autom fixes it. |
| Brave Search | `braveSearch` | Queries Brave Search and returns structured organic results (title, link, domain, snippet, position) with pagination. Costs 1 credit per call. |
| Find Google Countries | `findGoogleCountries` | Looks up Google country codes by a case-insensitive search string matched against country code or name. Free Finder endpoint (no credits). Use the returned country_code as the gl parameter of search actions. |
| Find Google Languages | `findGoogleLanguages` | Looks up Google language codes whose names contain a case-insensitive search string. Free Finder endpoint (no credits). Use the returned language_code as the hl parameter of search actions. |
| Find Google Locations | `findGoogleLocations` | Finds supported Google locations (cities, regions, countries) matching a query, ordered by reach, with location id, canonical name, country code, GPS coordinates and target type. Free Finder endpoint (no credits). Use the canonical_name as the location parameter of search actions. |
| Get Job | `getJob` | Retrieves the result of an asynchronous request started with is_async=true on any search action. Polling is always free; the job is billed only when it completes successfully. Returns the job status while pending and the endpoint's normal response body once finished. Note: the live route is /v1/jobs/{job_id} (the docs' unversioned /jobs path returns 403). |
| Get Stats | `getStats` | Returns a platform-wide infrastructure health snapshot (operational, degraded or down), success rate and average response time over the last hour for an API engine or a specific endpoint path. Not account-scoped and free of credits. Provide at least one of engine or path. API Stats is enabled per account: HTTP 403 means it is not active on your account and support must activate it. |
| Get Usage | `getUsage` | Returns your remaining API quota, extra credits, billing period, rate limits, account and API key details. Free: never consumes credits. The subscription object reports the combined API quota (subscription allowance plus remaining top-ups). |
| Google Images Search | `googleImagesSearch` | Searches Google Images and returns image results with image URL, source page link, title, domain, position and dimensions. Supports country, language and Google domain selection. Costs 1 credit per call. Known vendor defect (verified 2026-09-16): sending the documented page parameter, with any value, makes Autom return HTTP 500 Internal Error; omit page until Autom fixes it. |
| Google Jobs Search | `googleJobsSearch` | Scrapes Google Jobs and returns structured job listings (title, company, location, source, extensions, share link, job id) with token-based pagination. Supports remote-only filtering, search radius, encoded filter chips and localisation. Costs 1 credit per call. |

<details>

<summary>See 7 more actions</summary>

* **Google Maps Search** `googleMapsSearch`: Searches Google Maps (experimental endpoint) and returns place results with feature id, coordinates, title, address, website and phone number. Supports pagination, language, country and a map-centre hint. Costs 1 credit per call.
* **Google News Search** `googleNewsSearch`: Searches Google News and returns structured news results (date, title, link, domain, source, snippet, position) with pagination and country/language localisation. Costs 1 credit per call.
* **Google Search** `googleSearch`: Scrapes Google Search results for a query and returns structured SERP data: organic results (title, link, domain, snippet, position), knowledge graph and pagination. Supports advanced operators (site:, inurl:, intitle:), time filters (tbs), localisation by country, language and location. Costs 1 credit per call. Pass is_async=true to receive a job_id and fetch the result with Get Job.
* **Google Search Autocomplete** `googleSearchAutocomplete`: Returns Google Search autocomplete suggestions for a query, optionally at a given cursor position and localised by country and language. Costs 1 credit per call.
* **Google Search Light** `googleSearchLight`: Fast, cost-efficient Google Search that returns organic results only (title, link, source, snippet, position) with optional country and language localisation. Costs 1 credit per call.
* **Google Shopping Search** `googleShoppingSearch`: Searches Google Shopping and returns structured product listings with price, rating, rating count, merchant, image and product id, with pagination and localisation by country, language and location. Costs 1 credit per call.
* **Google Videos Search** `googleVideosSearch`: Searches Google Videos and returns structured video results (title, link, channel, duration, date, snippet, video id, position) with pagination and localisation. The page number is required by Autom. Costs 1 credit per call.

</details>
