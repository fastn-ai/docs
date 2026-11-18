---
description: "Olostep is a web search, scraping and crawling API built for AI applications."
hidden: true
---

# Olostep

<img src="../../.gitbook/assets/connectors/lg/olostep.png" alt="Olostep logo">

Olostep is a web search, scraping and crawling API built for AI applications. This connector covers single-page scrapes, large asynchronous batches, website crawls and URL maps, AI answers and web search, stored content retrieval, change monitors, JSON context files, scheduled API calls, AirOps enrichment batches and credit balance information.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [olostep.com](https://olostep.com) |
| **Authentication** | Bearer token |
| **Slug** | `olostep` |

## Use it

Add Olostep from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.olostep.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Complete File Upload | `completeFileUpload` | Finalises a file upload after the JSON content has been PUT to the pre-signed URL. Verifies the file exists, validates that it is well-formed JSON under 200 MB and marks it completed. |
| Create AirOps Batch | `createAiropsBatch` | Starts an enrichment batch that scrapes each URL, extracts page metadata, analyses which fields are missing and fills the gaps with LLM extraction: page type, author, publish and modified dates, and mentions of the brands you list. |
| Create Answer | `createAnswer` | Asks Olostep's AI to answer a task by searching and browsing the live web, returning the answer with its sources. Optionally shape the result with a JSON template or a description of the fields you want. Typically takes 3 to 30 seconds. |
| Create Batch | `createBatch` | Starts an asynchronous batch that scrapes many URLs at once and returns a batch id. Poll Get Batch until the status is completed, then read results with List Batch Items. Optionally applies a parser, collects links on each page, and posts a batch.completed notification to a webhook URL. |
| Create Crawl | `createCrawl` | Starts an asynchronous crawl from a start URL that follows links up to a page and depth limit and scrapes every page found. Poll Get Crawl until completed and read pages with List Crawl Pages. Supports include and exclude path patterns, subdomains, relevance ordering by search query, robots.txt control, per-page scrape options and a crawl.completed webhook. |
| Create File Upload | `createFileUpload` | Creates a file record and returns a pre-signed URL, valid for 10 minutes, for uploading a JSON file with an HTTP PUT. After uploading, call Complete File Upload to validate and finalise the file. |
| Create Map | `createMap` | Discovers the URLs on a website and returns them, optionally filtered by path patterns and ordered by relevance to a search query. Large sites are paginated with a cursor; complex sites can take up to two minutes. |
| Create Monitor | `createMonitor` | Creates a web monitor from a natural-language query that runs on a schedule, takes snapshots of the tracked pages and alerts on changes by email, Slack, SMS or webhook. Returns JSON with status provisioning; the monitor becomes active once planning has resolved what to track (poll Get Monitor). The optional server-sent-events streaming mode of this endpoint is not offered here. |
| Create Schedule | `createSchedule` | Schedules an Olostep API call to run once at a future time or on a recurring cron schedule. Provide exactly one timing option: Execute At for a one-time run, or Cron Expression (with Expression Timezone) or natural-language Text for a recurring run - a request with none of them is rejected. POST endpoints may use the short form, for example v1/scrapes. |
| Create Scrape | `createScrape` | Scrapes a single web page and returns its content as Markdown, HTML, text, structured JSON, a raw PDF or a screenshot. Supports browser actions before capture, residential country routing, parsers and LLM extraction, link extraction, screen size and cached results. |

<details>

<summary>See 36 more actions</summary>

* **Create Search** `createSearch`: Searches the web with a natural-language query and returns a deduplicated list of relevant links with titles and descriptions. Results can be restricted to or exclude specific domains, run in a low-latency fast mode, and optionally include the scraped content of every returned page (billed per page).
* **Delete File** `deleteFile`: Permanently deletes a file and its stored content.
* **Delete Monitor** `deleteMonitor`: Soft-deletes a monitor, setting its status to deleted and removing its schedule and agent so no further runs occur.
* **Delete Schedule** `deleteSchedule`: Deletes a schedule so that no further executions run.
* **Get AirOps Batch** `getAiropsBatch`: Returns the overall status of an AirOps enrichment batch and the progress of its scraping, analysis and enrichment phases.
* **Get Answer** `getAnswer`: Retrieves a previously completed answer by its id, including the result and its sources.
* **Get Batch** `getBatch`: Returns the status and progress of a batch, including how many URLs have completed and the credits consumed. Poll it until the status is completed.
* **Get Crawl** `getCrawl`: Returns the status and progress of a crawl, including the pages crawled so far, current depth and credits consumed.
* **Get Credit Info** `getCreditInfo`: Returns the team's credit balance with a per-lot breakdown, the active subscription and whether API usage is currently allowed. Useful as a pre-flight check before large jobs.
* **Get Dataset (Legacy)** `getDatasetLegacy`: Retrieves the stored Markdown and/or HTML of a legacy scrape by its dataset id, as returned by Scrape Page (Legacy).
* **Get File** `getFile`: Returns the metadata of a file by its id, including its filename, size, purpose and upload status.
* **Get File Content** `getFileContent`: Returns a pre-signed download URL for the content of a completed file. The URL lifetime defaults to 10 minutes and can be changed with Expires In.
* **Get Map** `getMap`: Retrieves a previously completed map by its id, including the discovered URLs.
* **Get Monitor** `getMonitor`: Returns a monitor by id, including its tracked targets, schedule, notification settings, last run and, by default, the total snapshot count. Optionally includes a Mermaid diagram of the monitor's workflow.
* **Get Monitor Planning** `getMonitorPlanning`: Returns the workflow specification and planner graph generated for a monitor, showing how its natural-language query was turned into concrete tracking steps.
* **Get Monitor Run** `getMonitorRun`: Returns the snapshot metadata and parsed agent log events for a single monitor run.
* **Get Schedule** `getSchedule`: Returns a single schedule by its id, including its endpoint, payload and timing.
* **Get Scrape** `getScrape`: Retrieves the stored result of a previously created scrape by its id, including the content formats that were requested.
* **Get Search** `getSearch`: Retrieves a previously completed search by its id, including any scraped per-link content stored at search time. It never re-runs or re-bills the search.
* **List AirOps Batch Items** `listAiropsBatchItems`: Returns every item of an AirOps enrichment batch with its extracted page type, author, dates and brand mentions, plus success and failure counts.
* **List Batch Items** `listBatchItems`: Lists the processed items of a batch, optionally only completed or only failed ones, with cursor pagination. Each item carries a retrieve_id to fetch its content with Retrieve Content.
* **List Crawl Pages** `listCrawlPages`: Lists the pages processed by a crawl with cursor pagination, optionally ordered by relevance to a search query. Each page carries a retrieve_id to fetch its content with Retrieve Content.
* **List Files** `listFiles`: Lists the team's completed files, optionally only those with a given purpose. Files still waiting for upload completion are not included.
* **List Monitor Events** `listMonitorEvents`: Lists a monitor's snapshot events, newest first, with short-lived pre-signed snapshot URLs and cursor pagination. With Count Only set, returns just the total number of events.
* **List Monitors** `listMonitors`: Lists the team's monitors. Deleted monitors are excluded unless Include Deleted is true.
* **List Recent Batches** `listRecentBatches`: Lists the most recent batches for the team, newest first, optionally filtered by the source that created them.
* **List Schedules** `listSchedules`: Lists the team's schedules with their configuration and status. Deleted schedules are excluded unless Include Deleted is true.
* **Pause Monitor** `pauseMonitor`: Pauses an active monitor by disabling its future scheduled runs and setting its status to paused.
* **Purchase Credit Top-Up** `purchaseCreditTopup`: Charges the team's saved card and purchases a pack of credits in one step, with no checkout page. Requires a saved card on the account and allows one attempt every 60 seconds. Credits are added once payment is confirmed; check Get Credit Info afterwards. This spends real money.
* **Quick Connect Partner User** `quickConnectPartnerUser`: For approved Olostep integration partners: creates or links an Olostep user for a verified email address and returns their account details. Requires the partner key Olostep issues during partner onboarding and an idempotency key per logical operation; a customer API key alone is not accepted.
* **Resume Monitor** `resumeMonitor`: Resumes a paused monitor by re-enabling its scheduled runs and setting its status to active.
* **Retrieve Content** `retrieveContent`: Fetches the stored content of a scraped, batched or crawled page by its retrieve id. Returns every stored format by default, or only the format named in Formats.
* **Scrape Page (Legacy)** `scrapePageLegacy`: Scrapes a web page through Olostep's original agent endpoint using query-string options for timeouts, wait time, HTML and Markdown output, CSS selector removal and image removal. Returns the content inline together with a dataset id. Prefer Create Scrape for new integrations.
* **Stream Monitor Agent Logs** `streamMonitorAgentLogs`: Tails the agent logs for a monitor as a server-sent event stream, filtered to lines that mention the monitor, starting from a given time (default the last 30 minutes).
* **Update Batch Metadata** `updateBatchMetadata`: Updates the metadata of a batch using merge semantics: new keys are added, existing keys are overwritten and keys set to an empty string are removed. Only metadata can be changed after a batch is created.
* **Update Monitor** `updateMonitor`: Updates a monitor's frequency, metadata, notification settings or webhook. Changing the frequency recreates the schedule. Rejected with 409 while the monitor is still provisioning.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Batch Completed | `event.batch.completed` | Fires when a batch finishes processing, with all items completed or failed. Olostep sends this per batch rather than through a standing subscription: pass this trigger's webhook URL as the Webhook URL input of Create Batch. Deliveries are retried up to 5 times over 30 minutes and are not signed; deduplicate on id. The schema below was captured from a real delivery. |
| Crawl Completed | `event.crawl.completed` | Fires when a crawl finishes and all discovered pages have been processed. Olostep sends this per crawl: pass this trigger's webhook URL as the Webhook URL input of Create Crawl. Deliveries are retried up to 5 times over 30 minutes and are not signed; deduplicate on id. The schema below was captured from a real delivery. |
| Monitor Fired | `monitor.run` | Fires when an Olostep monitor created for this trigger posts to its webhook after a scheduled run. Subscribing creates a monitor from the monitorQuery input (and optional monitorFrequency) with this trigger's URL as its webhook; unsubscribing deletes that monitor. Olostep does not document the monitor webhook body and no run completed during validation, so the schema below is a recommended minimum modelled on the monitor resource, not a captured delivery. |
