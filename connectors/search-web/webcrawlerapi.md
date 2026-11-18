---
description: "WebCrawlerAPI crawls whole websites and scrapes single pages into Markdown, cleaned text, HTML or link lists."
hidden: true
---

# WebCrawlerAPI

<img src="../../.gitbook/assets/connectors/lg/webcrawlerapi.png" alt="WebCrawlerAPI logo">

WebCrawlerAPI crawls whole websites and scrapes single pages into Markdown, cleaned text, HTML or link lists. This connector covers the complete WebCrawlerAPI: asynchronous crawl jobs with status, discovered URLs, combined Markdown output and cancellation; synchronous and asynchronous single-page scraping with optional LLM prompts; scheduled change-monitoring feeds with RSS and JSON Feed output, pause, resume, force-run, webhook resend and deletion; AI agent runs that extract structured data; and organization balance and usage statistics.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [webcrawlerapi.com](https://webcrawlerapi.com) |
| **Authentication** | Bearer token |
| **Slug** | `webcrawlerapi` |

## Use it

Add WebCrawlerAPI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.webcrawlerapi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Crawl Job | `cancelCrawlJob` | Cancels a running crawl job. Pages that have not started are marked canceled and are not charged. |
| Create Feed | `createFeed` | Creates a scheduled feed that periodically crawls a website and detects new, changed, unavailable or erroring pages, delivering updates via RSS, JSON Feed or a webhook POST. Charged per page crawled on each run; at most 100 feeds per organization. |
| Delete Feed | `deleteFeed` | Permanently cancels a feed. This cannot be undone; historical runs and detected changes stay readable through the RSS and JSON endpoints for 30 days. |
| Get Agent Job | `getAgentJob` | Returns the status, spend and, once finished, the extracted data of an agent run. |
| Get Crawl Job | `getCrawlJob` | Returns a crawl job's status (new, in_progress, done or error), its configuration, webhook delivery status and the list of crawled page items with their content URLs, titles, status codes, costs and errors. |
| Get Crawl Job Markdown Content | `getCrawlJobMarkdownContent` | Downloads the combined Markdown of every successfully crawled page of a completed Markdown crawl job directly as text (text/markdown), each page separated by a '---- url: &lt;page_url&gt; ----' block. |
| Get Crawl Job Markdown Link | `getCrawlJobMarkdownLink` | Returns a stable URL to a single combined Markdown file containing every successfully crawled page of a completed Markdown crawl job, each page separated by a '---- url: &lt;page_url&gt; ----' block. |
| Get Crawl Job URLs | `getCrawlJobUrls` | Returns every URL discovered by a completed crawl job as a flat list plus path-based clusters showing how many URLs sit under each site section. Only available once the job has completed. |
| Get Feed | `getFeed` | Returns a feed's configuration, status, next and last run times, webhook delivery status and its recent run history with page counts and costs. |
| Get Feed JSON | `getFeedJson` | Returns the changes detected by a feed in JSON Feed 1.1 format, one item per new, changed, unavailable or erroring page with a WebCrawlerAPI extension carrying the change type, page status code, content URL and size. Paginated, newest first. |
| Get Feed RSS | `getFeedRss` | Returns the changes detected by a feed as an Atom 1.0 XML document (RFC 5005 paginated), one entry per new, changed, unavailable or erroring page, newest first. |
| Get Organization Balance | `getOrganizationBalance` | Returns the organization's current spendable balance in USD, combining prepaid credits and subscription credits. |
| Get Organization Usage | `getOrganizationUsage` | Returns aggregated usage statistics for the organization over a date range (default: the last 30 days): total cost in USD and number of requests, optionally with a per-day breakdown. The range may not exceed one year. |
| Get Scrape Result | `getScrapeResult` | Returns the status of an asynchronous scrape job and, once it is done, the scraped content in the requested formats. While the job is still running only the status is returned. |
| List Agent Jobs | `listAgentJobs` | Returns a paginated list of the organization's agent runs with their status, model, spend and success flag, plus the total count. |
| List Feeds | `listFeeds` | Lists every feed of the organization (active, paused and canceled), newest first, with each feed's configuration, status and run times. |
| Pause Feed | `pauseFeed` | Temporarily stops a feed from running its scheduled crawls; scheduled runs are skipped until the feed is resumed. |
| Resend Feed Webhook | `resendFeedWebhook` | Re-sends the webhook notification for a feed's latest completed run to the feed's configured webhook URL and reports the delivery status code. |
| Resume Feed | `resumeFeed` | Resumes a paused feed so scheduled crawls continue; the next run is scheduled from the current time. Canceled feeds cannot be resumed. |
| Run Agent | `runAgent` | Starts an AI agent that browses the given seed URLs, optionally follows relevant links, and extracts data according to a natural-language prompt and optional JSON Schema, within a USD spending cap. Runs asynchronously; poll Get Agent Job for the result. |
| Run Feed Now | `runFeedNow` | Triggers an immediate extra run of an active feed outside its regular schedule. Limited to one forced run per hour per feed and charged like a scheduled run; the organization needs a balance of at least $0.01. |
| Scrape Page | `scrapePage` | Scrapes a single web page synchronously and returns its content as Markdown, cleaned text, raw HTML and/or a list of links, optionally with structured data extracted by an LLM prompt. A failed scrape returns HTTP 200 with success false and an error code. Charged per page (plus tokens when a prompt is used). |
| Start Async Scrape | `startAsyncScrape` | Queues a single-page scrape and returns a job id immediately instead of waiting for the result; retrieve the content later with Get Scrape Result. Accepts the same options as Scrape Page. Charged per page. |
| Start Crawl Job | `startCrawlJob` | Starts an asynchronous crawl of a website from a seed URL, following links up to the page limit and depth you set and producing Markdown, cleaned text, HTML or link output for every page. Returns the job id; poll Get Crawl Job or supply a webhook URL to be notified when it finishes. Charged per page crawled. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Feed Changes Detected | `feed.changes_detected` | Fired after each scheduled or forced run of a WebCrawlerAPI change-monitoring feed when new, changed, unavailable or erroring pages were detected on the monitored website. Subscribing creates a feed for the URL you provide with the fastn webhook URL as its webhook_url; unsubscribing cancels that feed. The payload is the JSON Feed 1.1 document of the run: each item carries the page url, title, a summary, tags and a _webcrawlerapi object with change_type (new, changed, unavailable or error), page_status_code and content_url. Deliveries are unsigned. |
