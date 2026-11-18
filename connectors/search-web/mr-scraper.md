---
description: "MrScraper is an AI-powered web scraping platform with anti-bot bypass, browser rendering and residential proxies."
hidden: true
---

# MrScraper

<img src="../../.gitbook/assets/connectors/mr-scraper.png" alt="MrScraper logo" width="64">

MrScraper is an AI-powered web scraping platform with anti-bot bypass, browser rendering and residential proxies. Aligned with the MrScraper Python SDK v0.6.0: Scraper API (fetch a URL as HTML, Markdown or a screenshot), Web Search (Google SERP) and Account (identity, subscription, token usage and rate limits). Also covers Playground scraping (HTML, Markdown, screenshots, AI JSON extraction, listing pages, sitemap discovery), the Platform API (AI and manual scrapers, reruns, bulk cancellation, self-healing, results, analytics, proxy bandwidth), bulk submissions, and Marketplace sync and async scrapers such as Amazon product details and YouTube videos. Auth: MrScraper API token sent as x-api-token and Authorization: Bearer.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [mrscraper.com](https://mrscraper.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `mrScraper` |

## Use it

Add MrScraper from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mrScraper.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Account (Verify API Token) | `verifyApiToken` | Verifies the API token and returns the subscription account, including token limit and usage, plan details, concurrency and the account user. Same call as the MrScraper Python SDK account(); note the raw response also includes billing fields (stripeSubscriptionId etc.) that the SDK hides client-side. |
| Bulk Rerun AI Scraper | `bulkRerunAiScraper` | Runs an existing AI scraper across multiple URLs asynchronously and returns a bulk result ID to poll with Get Result for merged data and per-URL status. Consumes MrScraper tokens. |
| Bulk Rerun Manual Scraper | `bulkRerunManualScraper` | Runs an existing manual scraper across multiple URLs asynchronously and returns a bulk result ID to poll with Get Result. Consumes MrScraper tokens. |
| Cancel Bulk Result | `cancelBulkResult` | Cancels a running bulk scraping job using the bulk result ID returned by a bulk rerun. |
| Create And Run AI Scraper | `createAiScraper` | Creates a new AI scraper from a URL and natural-language instructions using the general, listing or map agent, runs it immediately and returns the result with the scraperId for later reruns. Consumes MrScraper tokens. |
| Create Async Google SERP Task | `createAsyncSerpTask` | Queues a Marketplace Google SERP scrape asynchronously and returns a task ID; fetch the result with Get Async Task Result or receive it at the callback URL. Consumes MrScraper tokens. |
| Get Analytic Statuses | `getAnalyticStatuses` | Returns scrape status counts (completed, pending, failed), success rate, requests per minute and average latency for a domain within a UTC date range, optionally filtered by action. |
| Get Async Task Result | `getAsyncTaskResult` | Retrieves the result of an asynchronous Marketplace scraper task by task ID. While the task runs the response reports PENDING with success false; poll until data is returned. |
| Get Bulk Submission | `getBulkSubmission` | Retrieves the progress and per-URL results of a bulk submission by its submission ID. |
| Get Proxy Bandwidth Usage | `getProxyBandwidthUsage` | Returns residential proxy bandwidth usage aggregated per proxy username within a date range, optionally in a given timezone and filtered by region. |

<details>

<summary>See 16 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Result | `getResult` | Retrieves a single scraping result by its ID, including extracted data, status, token usage and file paths. Also used to poll bulk rerun results by their bulk result ID. |
| Get Screenshot | `getScreenshot` | Renders a web page in a real browser and returns a base64-encoded JPEG screenshot of the full page, optionally with a full-page recording, HTML and Markdown. Consumes MrScraper tokens. |
| List Results | `listResults` | Lists scraping results with their data, status, token usage and file paths, with sorting, pagination, full-text search and date-range filtering. |
| Rerun AI Scraper | `rerunAiScraper` | Reruns an existing AI scraper on a URL, reusing cached results to reduce token usage. Map-agent scrapers also accept crawl depth, page and URL limits and include or exclude patterns. Consumes MrScraper tokens. |
| Rerun Manual Scraper | `rerunManualScraper` | Reruns an existing manual scraper on a URL, optionally overriding its workflow steps (extract, click, delay, wait, input, scroll, script, listen_network, follow_urls). Reuses cached results to reduce token usage. Consumes MrScraper tokens. |
| Run Bulk Submission | `runBulkSubmission` | Submits a custom scraper workflow to run against many URLs in one bulk job and returns a submission ID to poll with Get Bulk Submission. Consumes MrScraper tokens. |
| Scrape Amazon Product Details | `scrapeAmazonProduct` | Runs the Marketplace Amazon Product Details scraper synchronously on an Amazon product page URL and returns structured product information. Consumes MrScraper tokens. |
| Scrape HTML With Web Unblocker | `scrapeHtml` | Fetches the raw HTML of any web page through the Web Unblocker, with optional browser rendering, anti-bot bypass (super mode), geo-targeting, resource blocking and waiting for a CSS selector. Consumes MrScraper tokens. |
| Scrape JSON | `scrapeJson` | Extracts structured JSON from a single page with the AI general agent, guided by a natural-language prompt (optionally with an appended JSON schema) instead of CSS selectors. Consumes MrScraper tokens. |
| Scrape Listing Page | `scrapeListingPage` | Extracts repeating items from a multi-page listing, catalog or search results page with the AI listing agent, following numbered pagination, infinite scroll and Load More up to a page limit. Requires super mode. Consumes MrScraper tokens. |
| Scrape Markdown | `scrapeMarkdown` | Scrapes a web page and returns its content as clean, LLM-friendly Markdown with navigation, scripts and ads stripped. Supports browser rendering, super mode, screenshots, geo-targeting and a token cap. Consumes MrScraper tokens. |
| Scrape Sitemap | `scrapeSitemap` | Crawls a website's link structure with the AI map agent and returns the discovered URLs, controlled by crawl depth, page and URL limits and include or exclude patterns. Consumes MrScraper tokens. |
| Scrape YouTube Video | `scrapeYoutubeVideo` | Runs the Marketplace YouTube scraper synchronously on a video URL and returns the video title, author, duration, thumbnails, available formats and a download URL. Consumes MrScraper tokens. |
| Scraper API | `scraperApi` | Fetch a known URL through the MrScraper stealth browser and return HTML, Markdown, a screenshot, or a combination, with browser rendering, geolocation, proxy and retry controls. Same request as the MrScraper Python SDK scraper_api (v0.6.0): POST https://api.mrscraper.com with page options as query parameters and url/maxRetries/tokenCap in the JSON body. |
| Self-Heal Manual Scraper | `selfHealManualScraper` | Asks AI to repair a manual scraper's workflow after the target site changed its markup. The saved workflow is replaced only when a valid workflow is returned; check workflowUpdated in the response. Consumes MrScraper tokens. |
| Web Search (Google SERP) | `searchGoogleSerp` | Runs the Marketplace Google SERP scraper synchronously for a search query and returns parsed results as JSON or the result-page HTML, with region, language and page controls. Consumes MrScraper tokens. Same call as the MrScraper Python SDK web_search() (v0.6.0). |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Scrape Completed | `scrape_completed` | Fires when a scraper run finishes successfully. MrScraper has no webhook API, so set this up in the dashboard for each account: gear icon &gt; Webhooks &gt; + ; Request Type POST; Event 'Scraping Completed'; paste this fastn webhook URL as the URL; Submit. Then open the scraper, click the ellipsis (⋮) &gt; Webhooks, select the webhook under Webhook Settings and click Save Webhook Settings. The event name is in the top-level event field and the scrape result in data. MrScraper does not sign deliveries; add a static header in the webhook form if you need to authenticate it. Payload taken from the official docs example (no live delivery captured). |
| Scrape Failed | `scrape_failed` | Fires when a scraper run fails. Set up in the MrScraper dashboard: gear icon &gt; Webhooks &gt; + ; Request Type POST; Event 'Scraping Failed'; paste this fastn webhook URL; Submit; then attach the webhook to the scraper via ⋮ &gt; Webhooks &gt; Save Webhook Settings. The docs name only the completed event verbatim (scrape_completed); this event id follows the same documented naming and the payload is modelled on the completed example, so confirm the event value against your first delivery. |
| Scrape Started | `scrape_started` | Fires when a scraper run starts. Set up in the MrScraper dashboard: gear icon &gt; Webhooks &gt; + ; Request Type POST; Event 'Scraping Started'; paste this fastn webhook URL; Submit; then attach the webhook to the scraper via ⋮ &gt; Webhooks &gt; Save Webhook Settings. The docs name only the completed event verbatim (scrape_completed); this event id follows the same documented naming and the payload is modelled on the completed example, so confirm the event value against your first delivery. |
