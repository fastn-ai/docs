---
description: "Crawlbase is a web crawling and scraping platform with headless-browser rendering, residential proxies, anti-bot bypass and built-in scrapers."
---

# Crawlbase

Crawlbase is a web crawling and scraping platform with headless-browser rendering, residential proxies, anti-bot bypass and built-in scrapers. This connector covers the Crawlbase REST API: the Crawling API (GET, POST and PUT crawls with JSON, HTML or Markdown output, screenshots, scrapers and async mode), the Enterprise Crawler queue and its management endpoints (create, get, update, stats, pause, unpause, purge, delete, delete job, find job by RID, push URLs), Cloud Storage (get, bulk get, delete, bulk delete, list RIDs, total count), the Account usage API, the free User Agents API and the legacy Scraper, Screenshots and Leads APIs.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [crawlbase.com](https://crawlbase.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 25 |
| **Events** | 1 |
| **Slug** | `crawlbase` |

## Use it

Add Crawlbase from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.crawlbase.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Delete Stored Pages | `bulkDeleteStoredPages` | Deletes a list of stored pages by request id in one call and returns a per-RID status (Deleted, Not Found or Failed). Deletion is irreversible. |
| Bulk Get Stored Pages | `bulkGetStoredPages` | Retrieves up to 100 stored pages by request id in one call, optionally deleting each returned entry from storage. Each item's body is base64-encoded, gzip-compressed page content. |
| Crawl URL | `crawlUrl` | Crawls a web page through the Crawling API and returns its content as a JSON envelope (default), raw HTML or Markdown, with optional JavaScript rendering, geo-routing, device emulation, custom headers and cookies, built-in scrapers, screenshots, Cloud Storage persistence and async delivery to a callback URL. Each call is billed as one request (JavaScript-rendered and scrolled requests cost more). |
| Crawl URL With POST Body | `crawlUrlWithPostBody` | Sends a POST request to the target URL through the Crawling API with the body you provide (form fields or JSON) and returns the response as a JSON envelope, raw HTML or Markdown. Normal token only; supports geo-routing, scrapers, storage and async delivery. Do not use it to spam or attack target sites. |
| Crawl URL With PUT Body | `crawlUrlWithPutBody` | Sends a PUT request to the target URL through the Crawling API and returns the response as a JSON envelope, raw HTML or Markdown. Note: in live testing Crawlbase forwarded the PUT method but delivered an empty body to the target (verified with curl as well), so treat the body as best-effort. Normal token only. |
| Create Crawler | `createCrawler` | Creates a named Enterprise Crawler queue. Provide a callback URL to receive each crawl result by webhook POST, or omit it to have results persisted to Cloud Storage. Delivery mode is fixed at creation. |
| Delete Crawler | `deleteCrawler` | Permanently removes a crawler and everything still queued in it, so it no longer appears in your console or stats. There is no undo. |
| Delete Crawler Job | `deleteCrawlerJob` | Drops a single queued URL from a crawler by its request id (rid). |
| Delete Stored Page | `deleteStoredPage` | Deletes a single stored page from Cloud Storage by request id. Returns a success message, or an error of 'Not Found' when the RID is not in storage. |
| Find Crawler Job By RID | `findCrawlerJobByRid` | Looks up where a pushed request stands in a crawler: QUEUED with its queued metadata while pending, or NOT_QUEUED once it has been crawled or was never enqueued. |
| Get Account Usage | `getAccountUsage` | Returns the current month's usage statistics for one Crawlbase product: successful and failed requests, amount due, remaining credits (subscription products) and per-domain success rates, optionally with the previous month for comparison. Rate-limited to one request per five minutes; cache the result. |
| Get Crawler | `getCrawler` | Returns a crawler's configuration, status (active or paused) and queue statistics. |
| Get Crawler Stats | `getCrawlerStats` | Returns a summary across all your crawlers: concurrency, queue depth, completed and failed counts and a history breakdown, optionally limited to a date range. |
| Get Domain Leads (Legacy) | `getDomainLeadsLegacy` | Legacy Leads API: returns publicly visible email addresses associated with a bare domain, with source URLs. Billed at 1 credit per 10 emails. Closed to accounts created after 1 October 2024, which receive a 403; the email-extractor scraper on Crawl URL is the modern alternative. |
| Get Storage Total Count | `getStorageTotalCount` | Returns how many pages are currently held in your Cloud Storage area. |
| Get Stored Page | `getStoredPage` | Retrieves a page persisted in Cloud Storage by its request id (rid) or by its original URL (most recent version), as raw HTML or as a JSON envelope with metadata. Retrieval is free; stored pages are kept for 14 days by default. |
| Get User Agents | `getUserAgents` | Returns random User-Agent strings optimised for web crawling, optionally filtered by device class. Free on every plan; rate-limited to 1 request per second. |
| List Stored RIDs | `listStoredRids` | Lists the request ids currently in your Cloud Storage area, newest first by default, with optional scroll-based pagination: pass scroll=true on the first call and replay the returned scroll_id on follow-ups (scroll sessions expire after about 15 seconds of inactivity). |
| Pause Crawler | `pauseCrawler` | Stops a crawler from picking up new work while keeping its queue; pushed URLs continue to enqueue until the crawler is unpaused. |
| Purge Crawler Queue | `purgeCrawlerQueue` | Empties a crawler's queue immediately, dropping every still-pending URL, while keeping the crawler itself. There is no undo. |
| Push URL To Crawler | `pushUrlToCrawler` | Enqueues a URL into a named Enterprise Crawler queue and returns its request id (rid) immediately. The crawl runs in the background and the result is delivered to the crawler's callback URL or persisted to Cloud Storage, depending on how the crawler was created. Accepts the same rendering, geo and scraper options as Crawl URL. |
| Scrape URL (Legacy) | `scrapeUrlLegacy` | Legacy standalone Scraper API: applies a named built-in scraper (e.g. amazon-product-details, google-serp, linkedin-profile) to a URL and returns parsed JSON. Closed to accounts created after 1 October 2024, which receive a 403; new integrations should use Crawl URL with the scraper parameter. |
| Take Screenshot (Legacy) | `takeScreenshotLegacy` | Legacy standalone Screenshots API: renders a URL in headless Chrome and returns the image bytes (PNG by default) for the viewport or the full page. Requires a JavaScript token and is closed to accounts created after 1 November 2024, which receive a 403; new integrations should use Crawl URL with screenshot=true. |
| Unpause Crawler | `unpauseCrawler` | Resumes a paused crawler so it starts processing its queue again. |
| Update Crawler | `updateCrawler` | Changes a crawler's callback URL without restarting it. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Crawl Result Delivered | `crawl.completed` | Fired by the Enterprise Crawler for every URL pushed to the crawler that fastn registered with your webhook URL (push URLs with the Push URL To Crawler action, using the same crawler name). The delivery is a gzip-compressed POST from 'Crawlbase Delivery Bot 1.0'. With format=json on the push the body is the JSON envelope shown here; with the default html format the body is the raw page and the metadata (rid, url, cb-status, original-status) travels in request headers instead. Crawlbase also POSTs monitoring probes with rid 'dummyrequest' and User-Agent 'Crawlbase Monitoring Bot 1.0'; ignore those. Crawlbase sends no event-type field, so this single event type receives every delivery. Payload captured from a real delivery. |
