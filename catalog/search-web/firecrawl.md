---
description: "Firecrawl turns websites into clean data. Scrape pages, crawl and map sites, run batch scrapes and extract structured data."
hidden: true
---

# Firecrawl

<img src="../../.gitbook/assets/connectors/lg/firecrawl.png" alt="Firecrawl logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [firecrawl.dev](https://firecrawl.dev) |
| **Authentication** | Access token |
| **Slug** | `firecrawl` |

## Setup

Your customers enter their access token for Firecrawl when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Firecrawl from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Firecrawl**.
2. Select **Connect** on the Firecrawl card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Firecrawl's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Batch Scrape</td><td><code>batchScrape</code></td><td>Start an async batch scrape of many URLs with shared scrape options. Returns a job id; poll Get Batch Scrape Status. Supports an inline webhook: { url, headers, metadata, events }. IMPORTANT: webhook.events values are the bare names "started", "page", "completed", "failed" — the API rejects prefixed names like "batch_scrape.started". The delivered payload's own `type` field is the prefixed form (batch_scrape.started, batch_scrape.page, batch_scrape.completed, batch_scrape.failed).</td></tr><tr><td>Cancel Batch Scrape</td><td><code>cancelBatchScrape</code></td><td>Cancel an in-progress batch scrape job by id. Returns { status: 'cancelled' }.</td></tr><tr><td>Cancel Crawl</td><td><code>cancelCrawl</code></td><td>Cancel an in-progress crawl job by id. Returns { status: 'cancelled' }.</td></tr><tr><td>Crawl</td><td><code>crawl</code></td><td>Start an async crawl of an entire website from a base URL. Returns a job id; poll Get Crawl Status. Pass an inline webhook object to receive crawl events instead of polling: { url, headers, metadata, events }. IMPORTANT: webhook.events values are the bare names "started", "page", "completed", "failed" — the API rejects prefixed names like "crawl.started". The delivered payload's own `type` field is the prefixed form (crawl.started, crawl.page, crawl.completed, crawl.failed).</td></tr><tr><td>Crawl Params Preview</td><td><code>crawlParamsPreview</code></td><td>Preview the crawler options Firecrawl would auto-generate from a natural-language prompt for a given base URL, without starting a crawl. Use to inspect or tune crawl parameters before running Crawl.</td></tr><tr><td>Extract</td><td><code>extract</code></td><td>Start an async structured-data extraction from one or more URLs using a prompt and/or JSON schema. Returns a job id; poll Get Extract Status.</td></tr><tr><td>Get Active Crawls</td><td><code>getActiveCrawls</code></td><td>List all currently active (in-progress) crawl jobs for the team associated with the API key. Returns an array of running crawls with their ids and options.</td></tr><tr><td>Get Batch Scrape Errors</td><td><code>getBatchScrapeErrors</code></td><td>List per-URL errors and robots.txt-blocked URLs for a batch scrape job by id.</td></tr><tr><td>Get Batch Scrape Status</td><td><code>getBatchScrapeStatus</code></td><td>Get the status and accumulated page data of a batch scrape job by id. Use the 'next' URL to page through results larger than 10MB.</td></tr><tr><td>Get Crawl Errors</td><td><code>getCrawlErrors</code></td><td>List per-URL errors and robots.txt-blocked URLs for a crawl job by id.</td></tr></tbody></table>

<details>

<summary>View 10 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Crawl Status</td><td><code>getCrawlStatus</code></td><td>Get the status and accumulated page data of a crawl job by id. Use the 'next' URL to page through results larger than 10MB.</td></tr><tr><td>Get Credit Usage</td><td><code>getCreditUsage</code></td><td>Get the remaining credits on the account/team associated with the API key.</td></tr><tr><td>Get Credit Usage Historical</td><td><code>getCreditUsageHistorical</code></td><td>Get historical credit usage per billing period for the team associated with the API key. Optionally filter by number of billing periods.</td></tr><tr><td>Get Extract Status</td><td><code>getExtractStatus</code></td><td>Get the status and extracted data of an extract job by id.</td></tr><tr><td>Get Queue Status</td><td><code>getQueueStatus</code></td><td>Get the current job queue status for the team associated with the API key: total/active/waiting jobs, max concurrency, and most recent success time.</td></tr><tr><td>Get Token Usage</td><td><code>getTokenUsage</code></td><td>Get the remaining tokens on the account/team associated with the API key (used by Extract and json-format scrapes).</td></tr><tr><td>Get Token Usage Historical</td><td><code>getTokenUsageHistorical</code></td><td>Get historical token usage per billing period for the team associated with the API key.</td></tr><tr><td>Map</td><td><code>map</code></td><td>Quickly get a complete list of URLs from a website. Optionally order results by relevance to a search query.</td></tr><tr><td>Scrape</td><td><code>scrape</code></td><td>Scrape a single URL and return clean content in markdown, HTML, links, screenshot, or structured JSON. Supports browser actions, tag filtering, and main-content extraction.</td></tr><tr><td>Search</td><td><code>search</code></td><td>Search the web (web, news, images) and optionally scrape full page content of the results in any format.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Batch Scrape Completed</td><td><code>batch_scrape.completed</code></td><td>Sent when all URLs in a batch scrape have been processed.</td></tr><tr><td>Batch Scrape Failed</td><td><code>batch_scrape.failed</code></td><td>Sent when a batch scrape job errors. Carries an error message.</td></tr><tr><td>Batch Scrape Page</td><td><code>batch_scrape.page</code></td><td>Sent for each URL scraped during a batch scrape, carrying the page's incremental document payload.</td></tr><tr><td>Batch Scrape Started</td><td><code>batch_scrape.started</code></td><td>Sent when a batch scrape job begins processing. Configured inline via the 'webhook' param on the Batch Scrape action.</td></tr><tr><td>Crawl Completed</td><td><code>crawl.completed</code></td><td>Sent when all pages in a crawl have been processed.</td></tr><tr><td>Crawl Failed</td><td><code>crawl.failed</code></td><td>Sent when a crawl job errors. Carries an error message.</td></tr><tr><td>Crawl Page</td><td><code>crawl.page</code></td><td>Sent for each page scraped during a crawl, carrying the page's incremental document payload.</td></tr><tr><td>Crawl Started</td><td><code>crawl.started</code></td><td>Sent when a crawl job begins processing. Configured inline via the 'webhook' param on the Crawl action.</td></tr></tbody></table>
