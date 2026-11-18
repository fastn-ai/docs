---
description: "Firecrawl web scraping, crawling, mapping, search, and structured-data extraction API (v2)."
hidden: true
---

# Firecrawl

Firecrawl web scraping, crawling, mapping, search, and structured-data extraction API (v2). Turns any website into clean markdown, HTML, or structured JSON for AI applications.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [firecrawl.dev](https://firecrawl.dev) |
| **Authentication** | Bearer token |
| **Actions** | 20 |
| **Events** | 8 |
| **Slug** | `firecrawl` |

## Use it

Add Firecrawl from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.firecrawl.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Scrape | `batchScrape` | Start an async batch scrape of many URLs with shared scrape options. Returns a job id; poll Get Batch Scrape Status. Supports an inline webhook: { url, headers, metadata, events }. IMPORTANT: webhook.events values are the bare names "started", "page", "completed", "failed" — the API rejects prefixed names like "batch_scrape.started". The delivered payload's own `type` field is the prefixed form (batch_scrape.started, batch_scrape.page, batch_scrape.completed, batch_scrape.failed). |
| Cancel Batch Scrape | `cancelBatchScrape` | Cancel an in-progress batch scrape job by id. Returns { status: 'cancelled' }. |
| Cancel Crawl | `cancelCrawl` | Cancel an in-progress crawl job by id. Returns { status: 'cancelled' }. |
| Crawl | `crawl` | Start an async crawl of an entire website from a base URL. Returns a job id; poll Get Crawl Status. Pass an inline webhook object to receive crawl events instead of polling: { url, headers, metadata, events }. IMPORTANT: webhook.events values are the bare names "started", "page", "completed", "failed" — the API rejects prefixed names like "crawl.started". The delivered payload's own `type` field is the prefixed form (crawl.started, crawl.page, crawl.completed, crawl.failed). |
| Crawl Params Preview | `crawlParamsPreview` | Preview the crawler options Firecrawl would auto-generate from a natural-language prompt for a given base URL, without starting a crawl. Use to inspect or tune crawl parameters before running Crawl. |
| Extract | `extract` | Start an async structured-data extraction from one or more URLs using a prompt and/or JSON schema. Returns a job id; poll Get Extract Status. |
| Get Active Crawls | `getActiveCrawls` | List all currently active (in-progress) crawl jobs for the team associated with the API key. Returns an array of running crawls with their ids and options. |
| Get Batch Scrape Errors | `getBatchScrapeErrors` | List per-URL errors and robots.txt-blocked URLs for a batch scrape job by id. |
| Get Batch Scrape Status | `getBatchScrapeStatus` | Get the status and accumulated page data of a batch scrape job by id. Use the 'next' URL to page through results larger than 10MB. |
| Get Crawl Errors | `getCrawlErrors` | List per-URL errors and robots.txt-blocked URLs for a crawl job by id. |
| Get Crawl Status | `getCrawlStatus` | Get the status and accumulated page data of a crawl job by id. Use the 'next' URL to page through results larger than 10MB. |
| Get Credit Usage | `getCreditUsage` | Get the remaining credits on the account/team associated with the API key. |
| Get Credit Usage Historical | `getCreditUsageHistorical` | Get historical credit usage per billing period for the team associated with the API key. Optionally filter by number of billing periods. |
| Get Extract Status | `getExtractStatus` | Get the status and extracted data of an extract job by id. |
| Get Queue Status | `getQueueStatus` | Get the current job queue status for the team associated with the API key: total/active/waiting jobs, max concurrency, and most recent success time. |
| Get Token Usage | `getTokenUsage` | Get the remaining tokens on the account/team associated with the API key (used by Extract and json-format scrapes). |
| Get Token Usage Historical | `getTokenUsageHistorical` | Get historical token usage per billing period for the team associated with the API key. |
| Map | `map` | Quickly get a complete list of URLs from a website. Optionally order results by relevance to a search query. |
| Scrape | `scrape` | Scrape a single URL and return clean content in markdown, HTML, links, screenshot, or structured JSON. Supports browser actions, tag filtering, and main-content extraction. |
| Search | `search` | Search the web (web, news, images) and optionally scrape full page content of the results in any format. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Batch Scrape Completed | `batch_scrape.completed` | Sent when all URLs in a batch scrape have been processed. |
| Batch Scrape Failed | `batch_scrape.failed` | Sent when a batch scrape job errors. Carries an error message. |
| Batch Scrape Page | `batch_scrape.page` | Sent for each URL scraped during a batch scrape, carrying the page's incremental document payload. |
| Batch Scrape Started | `batch_scrape.started` | Sent when a batch scrape job begins processing. Configured inline via the 'webhook' param on the Batch Scrape action. |
| Crawl Completed | `crawl.completed` | Sent when all pages in a crawl have been processed. |
| Crawl Failed | `crawl.failed` | Sent when a crawl job errors. Carries an error message. |
| Crawl Page | `crawl.page` | Sent for each page scraped during a crawl, carrying the page's incremental document payload. |
| Crawl Started | `crawl.started` | Sent when a crawl job begins processing. Configured inline via the 'webhook' param on the Crawl action. |
