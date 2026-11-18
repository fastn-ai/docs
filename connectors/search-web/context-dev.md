---
description: "Context.dev is a web data API for AI agents and applications."
hidden: true
---

# Context.dev

<img src="../../.gitbook/assets/connectors/lg/context-dev.png" alt="Context.dev logo">

Context.dev is a web data API for AI agents and applications. This connector covers the complete Context.dev v1 REST surface: scraping webpages to Markdown, HTML, raw bytes, images, fonts, screenshots and design styleguides; crawling websites and sitemaps; extracting structured data against a JSON Schema; web search, company-news search and sourced research answers; document parsing; brand retrieval by domain, name, email, ticker, ISIN or transaction descriptor, brand search, AI website queries and product extraction; competitor discovery; NAICS and SIC industry classification; person enrichment and retrieval; company funding; prefetch warming; asynchronous batch jobs; website change monitors with runs, changes and signed webhooks; WebDB collections that keep extracted rows in sync with their source pages, with row history, snapshots, runs, rejections and WebDB webhooks; webhook delivery inspection and retries; and request logs.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [context.dev](https://context.dev) |
| **Authentication** | Bearer token |
| **Slug** | `contextDev` |

## Use it

Add Context.dev from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.contextDev.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Answer Research Task | `answerResearchTask` | Researches the live web and returns a sourced answer in the JSON shape you request. Mode fast uses a smaller research budget for 10 credits (30 second limit); ultra uses deeper reasoning for 100 credits (50 second limit) and is the default. Only successful requests consume credits. |
| Cancel Batch | `cancelBatch` | Stops a batch from starting new pages. Pages already in progress finish, and credits for the unused pages are refunded. |
| Capture Screenshot | `captureScreenshot` | Captures a PNG screenshot of a website, either of an exact URL or of a page type resolved from a domain, with controls for viewport size, full-page capture, scroll offset, color scheme, popup dismissal, wait time and proxy country. |
| Classify NAICS Industries | `classifyNaics` | Classifies a brand into 2022 NAICS industry codes from its domain or company name, returning the candidate codes with confidence scores. |
| Classify SIC Industries | `classifySic` | Classifies a brand into Standard Industrial Classification (SIC) codes from its domain or company name, using either the original 1987 system or the current SEC-published list. |
| Crawl Sitemap | `crawlSitemap` | Reads a website's public sitemaps and returns the discovered page URLs without rendering each page, with optional subdomain discovery, an explicit sitemap URL, a URL regex filter and a relevance search phrase. |
| Crawl Website | `crawlWebsite` | Crawls a website section starting from a URL and returns each crawled page as Markdown in a single response, up to 500 pages. Use Submit Batch for larger crawls that should run in the background. |
| Create Monitor | `createMonitor` | Creates a monitor that watches a page, a sitemap or a structured extract on a schedule and reports detected changes, optionally delivering signed change events to a webhook. The monitor runs immediately after creation to establish its baseline. |
| Create WebDB Collection | `createWebdbCollection` | Creates a WebDB collection: a continuously synced table of rows extracted from web pages. Define the row schema as JSON Schema, the targets that supply pages (single URL, URL list, sitemap or crawl), and optional eligibility rules, sync schedule, change tracking, credit budget and stale-row handling. The initial sync consumes credits per page. |
| Create WebDB Webhook | `createWebdbWebhook` | Registers an HTTPS endpoint that receives WebDB events (row.created, row.updated, row.removed, row.error, row.cap_consumed, run.completed, run.failed, credits.low, credits.exhausted) for one collection or for all collections, delivered instantly or in batches. The response includes the signing secret used to verify deliveries. |
| Delete Batch | `deleteBatch` | VENDOR BLOCKER - do not call. Deletes a finished batch. DELETE /v1/batch/{batch_id} is documented but the DELETE verb is NOT routed by the live API: it returns 404 ENDPOINT_NOT_FOUND even for a batch id that GET /v1/batch/{batch_id} resolves successfully. Batches cannot be deleted through the API; their results expire on the vendor's own schedule. |
| Delete Monitor | `deleteMonitor` | Permanently removes a monitor and stops all of its scheduled runs. |
| Delete WebDB Collection | `deleteWebdbCollection` | Permanently deletes a WebDB collection together with its rows, runs and change history, and stops its scheduled syncs. |
| Delete WebDB Row | `deleteWebdbRow` | Deletes a single WebDB row. Set purge to also delete the row's change history and saved page snapshots. |
| Delete WebDB Webhook | `deleteWebdbWebhook` | Deletes a WebDB webhook so that no further events are delivered to its URL. |
| Enrich Person | `enrichPerson` | Finds and normalizes the best matching person from additive identity clues - social profile URLs, name, work email, company, education and location - and returns an identity match score from 0 to 100. Available on paid plans; a successful request costs 20 credits. Disposable and free email addresses are rejected with a 422. |
| Extract Brand Products | `extractBrandProducts` | Analyzes a brand's website and returns a list of its products with details such as name, description, image, pricing and features. Supply either a domain or a direct starting URL. |
| Extract Product From URL | `extractProductFromUrl` | Determines whether a URL is a product detail page and, if so, extracts normalized product fields such as name, description, image, pricing and features. |
| Extract Structured Data | `extractStructuredData` | Crawls the pages of a website that are relevant to your instructions and returns a single object matching the JSON Schema you supply, with controls for grounding, page coverage and cache freshness. |
| Find Competitors | `findCompetitors` | Analyzes a company's landing page and web search evidence to return its direct competitors for the same product or market. Costs 10 credits and is in private alpha, so accounts without access receive an error. |
| Get Batch | `getBatch` | Retrieves a batch job by ID, showing its progress and, once it finishes, the download links for its results. |
| Get Batch Results | `getBatchResults` | Pages through a finished batch's per-page results as JSON instead of downloading the NDJSON result files. A page can close early to stay under about 8 MB, so follow the next cursor rather than counting records. |
| Get Change | `getChange` | Retrieves the full details of a detected change: text diff and before/after excerpts for page targets, added and removed URLs for sitemap targets, semantic evidence, confidence and importance. |
| Get Monitor | `getMonitor` | Retrieves a single monitor by ID, including its target, change detection settings, schedule, webhook configuration, status and current baseline. |
| Get Monitor Credit Usage | `getMonitorCreditUsage` | Returns the credits charged per monitor over an optional time window, biggest spenders first, together with the total across all monitors. |
| Get Monitor Limits | `getMonitorLimits` | Returns how many monitors the account currently has, the maximum its plan allows and the plan tier the limit was resolved from. |
| Get Monitor Run | `getMonitorRun` | VENDOR BLOCKER - do not call. Retrieves a single monitor run by ID. GET /v1/monitors/{monitor_id}/runs/{run_id} is documented in Context.dev's OpenAPI spec but is NOT routed by the live API: it returns 404 ENDPOINT_NOT_FOUND, byte-identical to a garbage path, while the sibling GET /v1/monitors/{monitor_id}/runs returns a resource-level "Monitor not found". Use List Monitor Runs and filter by run id until Context.dev ships this route. |
| Get Request Log | `getRequestLog` | Retrieves one logged API call by its request ID, including the request input and the response body it returned. |
| Get WebDB Collection | `getWebdbCollection` | Retrieves a WebDB collection by ID with its full configuration (schema, targets, eligibility, sync, change tracking, budgets), status, row count, last run and credit usage. |
| Get WebDB Row | `getWebdbRow` | Retrieves a single WebDB row by ID with its extracted fields, status, source URL and metadata such as version, change count, eligibility score and extraction confidence. |
| Get WebDB Row History | `getWebdbRowHistory` | Returns the recorded change history of a WebDB row, newest first, with the event type, version and changed field values of each change, using cursor pagination. |
| Get WebDB Row Snapshot | `getWebdbRowSnapshot` | Downloads the saved page snapshot behind a WebDB row and returns it as raw Markdown or HTML text. Pass format=markdown for the Markdown rendering or format=html for the archived HTML. The response body is the snapshot itself, not JSON. |
| Get WebDB Run | `getWebdbRun` | Retrieves a single WebDB collection run by ID with its status, trigger, per-target results, statistics, errors and timing. |
| Get WebDB Usage | `getWebdbUsage` | Returns WebDB usage for your organization: credit balance and period consumption, a per-collection breakdown, total rows and snapshot storage in gigabytes, optionally limited to a date range. |
| Get WebDB Webhook | `getWebdbWebhook` | Retrieves a single WebDB webhook by ID, including its URL, subscribed events, watched collection, delivery settings, signing secret and status. |
| Get Webhook Delivery | `getWebhookDelivery` | Retrieves a single batch or monitor webhook delivery, including its status and latest attempt. Costs no credits. |
| Identify Brand From Transaction | `identifyBrandFromTransaction` | Identifies the brand behind a bank or card transaction descriptor, optionally helped by country, city, merchant category code and phone number, and returns its brand profile. Set high_confidence_only to add extra verification. Costs 10 credits. |
| List Account Changes | `listAccountChanges` | Returns an account-wide feed of detected changes across all monitors, filterable by monitor, target type, change detection type, tag and time window, with cursor pagination. |
| List Account Runs | `listAccountRuns` | Returns an account-wide feed of monitor runs across all monitors in your organization, with optional status filtering and cursor pagination. |
| List Batches | `listBatches` | Lists your batch jobs newest first, with optional filtering by status, free-text search and tags, and cursor pagination. |
| List Monitor Changes | `listMonitorChanges` | Lists the changes a single monitor has detected, filterable by tag and time window, with cursor pagination. |
| List Monitor Runs | `listMonitorRuns` | Lists a monitor's run history with lifecycle status, timing, credits charged and any detected change per run, with optional status filtering and cursor pagination. |
| List Monitors | `listMonitors` | Lists the monitors on your organization, with free-text search, status, target-type, change-detection-type and tag filters, and cursor pagination. |
| List Request Logs | `listRequestLogs` | Lists your organization's API requests newest first, defaulting to the last 24 hours, with filters for time window, endpoint path, API key, status code, error code, tags and a free-text search over the request query and body. |
| List WebDB Collection Changes | `listWebdbCollectionChanges` | Lists the recorded row changes (created, updated, removed, error, cap_consumed) of a WebDB collection with the changed field values, using cursor pagination. |
| List WebDB Collection Rejections | `listWebdbCollectionRejections` | Lists the pages of a WebDB collection that did not become rows, with the stage (fetch, prefilter, semantic or validation), score and reason for each rejection, using cursor pagination. |
| List WebDB Collection Runs | `listWebdbCollectionRuns` | Lists the sync, reprocess and purge runs of a WebDB collection with their status, trigger, statistics and errors, using cursor pagination. |
| List WebDB Collections | `listWebdbCollections` | Lists the WebDB collections in your organization with their status, row counts, sync schedule and credit usage, using cursor pagination. |
| List WebDB Webhook Deliveries | `listWebdbWebhookDeliveries` | Lists the event deliveries made by a WebDB webhook with their status, attempt count, next retry time and last error, using cursor pagination. |
| List WebDB Webhooks | `listWebdbWebhooks` | Lists the WebDB webhooks registered in your organization with their URL, subscribed events, watched collection, delivery mode and status, using cursor pagination. |
| List Webhook Deliveries | `listWebhookDeliveries` | Lists your batch or monitor webhook deliveries newest first. Choose the delivery source with type, then optionally narrow by batch, monitor, run, status or creation time, with cursor pagination. Costs no credits. |
| List Webhook Delivery Attempts | `listWebhookDeliveryAttempts` | Lists the attempts made for a webhook delivery, newest first, with the trigger, HTTP status and any error of each attempt. Costs no credits. |
| Parse Document | `parseDocument` | Converts raw document content - plain text, source code, HTML, XML, CSV, JSON, Markdown and similar text formats - into LLM-usable Markdown. Send the document as text in Content and give the matching Extension hint. Binary formats such as PDF, Office documents and images are supported by the Context.dev API but cannot be uploaded through this connector, because the fastn HTTP engine does not transmit non-UTF-8 bytes intact. |
| Prefetch Brand By Domain | `prefetchBrandByDomain` | Signals that brand data for a domain will be requested soon so Context.dev can warm its cache and reduce the latency of the eventual retrieval. Free of charge, but available to subscribers only. |
| Prefetch Brand By Email | `prefetchBrandByEmail` | Extracts the domain from a work email address, rejects free and disposable providers, and queues that domain for brand-data prefetching to reduce later latency. Free of charge, but available to subscribers only. |
| Prefetch Data | `prefetchData` | Signals that brand or styleguide data for a target will be fetched soon so Context.dev can warm its cache, reducing the latency of the eventual request. |
| Preview WebDB Extraction | `previewWebdbExtraction` | Dry-runs WebDB extraction against up to 5 URLs with a row schema and optional eligibility rules, returning the row each page would produce, per-field extraction details and any eligibility rejection, without creating a collection. |
| Purge WebDB Rows | `purgeWebdbRows` | Permanently deletes the rows of a WebDB collection whose source URL matches any of the given URL patterns (exact URLs, *, ** and :name path segments are supported), including their history and saved pages. |
| Query Brand Website With AI | `queryBrandWebsiteWithAi` | Crawls a brand's website and uses AI to extract the specific data points you describe (text, number, date, boolean, list or URL), optionally limited to particular page types such as pricing, about or careers. Costs 10 credits. |
| Query WebDB Collection | `queryWebdbCollection` | Queries the rows of a WebDB collection with field filters, sorting, field selection and cursor pagination. Each row carries the extracted fields plus system fields _id, _url, _status, _collection and _meta. |
| Remove Monitor Webhook | `removeMonitorWebhook` | Detaches the webhook from a monitor so that no further change.detected or run.completed events are delivered for it. The monitor itself keeps running on its schedule. |
| Reprocess WebDB Collection | `reprocessWebdbCollection` | Re-extracts rows of a WebDB collection from their stored page snapshots without fetching the pages again, for example after changing the row schema. Pass a where filter to limit which rows are reprocessed; omit it to reprocess every row. |
| Retrieve Brand | `retrieveBrand` | Retrieves a structured brand profile - logos, backdrops, colors, industry, description and company details - by resolving exactly one lookup identifier. Set Lookup Type and then supply only the matching identifier field: a domain, company name, work email, stock ticker, transaction descriptor, or direct URL. |
| Retrieve Brand By Domain | `retrieveBrandByDomain` | Retrieves a full brand profile - logos, backdrops, colors, description, slogan, address, socials, employees, industries and key links - by exactly one of domain, company name or stock ticker, with controls for speed and cache freshness. Costs 10 credits. |
| Retrieve Brand By Email | `retrieveBrandByEmail` | Retrieves a full brand profile from a work email address by extracting its domain. Free email providers (gmail.com, yahoo.com) and disposable addresses are rejected with a 422. Costs 10 credits. |
| Retrieve Brand By ISIN | `retrieveBrandByIsin` | Retrieves a full brand profile from a 12-character International Securities Identification Number (ISIN), with controls for speed and cache freshness. Costs 10 credits. |
| Retrieve Brand By Name | `retrieveBrandByName` | Retrieves a full brand profile from a company name (3-30 characters), optionally biased towards a country, with controls for speed and cache freshness. Costs 10 credits. |
| Retrieve Brand By Ticker | `retrieveBrandByTicker` | Retrieves a full brand profile from a stock ticker symbol, optionally disambiguated by exchange, with controls for speed and cache freshness. Costs 10 credits. |
| Retrieve Company Funding | `retrieveCompanyFunding` | VENDOR BLOCKER - do not call. Returns a company's funding history by domain. POST /v1/company/funding was documented in an earlier Context.dev spec but is NOT routed by the live API (404 ENDPOINT_NOT_FOUND), and no variant resolves (GET /company/funding, /companies/funding, /funding, /company). The current published spec no longer lists it. Use Retrieve Brand By Domain for company data instead. |
| Retrieve Person | `retrievePerson` | Retrieves and normalises a person profile from known identifiers such as a LinkedIn profile URL, including education and experience entries enriched with organisation data. Costs 50 credits and is in private alpha, so accounts without access receive an error. |
| Retrieve Simplified Brand | `retrieveSimplifiedBrand` | Returns a lightweight brand record for a domain containing only the essentials - domain, title, colors, logos and backdrops - optimised for fast responses, with an optional light or dark theme preference for asset selection. Costs 10 credits. |
| Retry Webhook Delivery | `retryWebhookDelivery` | Queues a manual retry of a webhook delivery within seven days of its creation. Set force to resend a delivery that already succeeded. |
| Rotate Monitor Webhook Secret | `rotateMonitorWebhookSecret` | Generates a new signing secret for a monitor's webhook and returns the updated monitor including the new webhook.secret. The previous secret stops signing deliveries immediately, so update your endpoint before rotating. |
| Run Monitor Now | `runMonitorNow` | Queues an immediate run of a monitor outside its normal schedule. The run is processed asynchronously; poll List Monitor Runs with the returned run ID to follow it. |
| Scrape Fonts | `scrapeFonts` | Extracts the font families a website uses, with usage statistics, fallback stacks and element and word counts, from either a domain or an exact URL. |
| Scrape HTML | `scrapeHtml` | Scrapes a single webpage and returns its rendered HTML, with controls for main-content extraction, iframe inlining, CSS selector scoping, PDF parsing, cache freshness, browser wait time and proxy country. The base request costs one credit, or two with browser actions. |
| Scrape Images | `scrapeImages` | Extracts an image manifest from a webpage, covering standard image URLs, inline SVGs, data URIs, responsive sources, CSS backgrounds, video posters and embeds, with optional per-image enrichment and perceptual deduplication. |
| Scrape Markdown | `scrapeMarkdown` | Scrapes a single webpage and returns its content as clean, LLM-ready Markdown, with controls for link and image handling, main-content extraction, iframe rendering, CSS selector scoping, cache freshness, browser wait time and proxy country. |
| Scrape Raw Bytes | `scrapeRawBytes` | Downloads a resource such as an image, PDF or HTML page and returns its bytes base64-encoded without conversion or text extraction. Follows public redirects and retries through proxies. Downloads are not cached; the maximum resource size is 20 MB. Costs one credit. |
| Scrape Screenshot | `scrapeScreenshot` | Captures a PNG screenshot of an exact HTTP or HTTPS URL and returns a hosted image URL plus the viewport size and cache status. Set fullScreenshot to true for a full-page capture instead of the default 1920x1080 viewport. Costs 1 credit per uncached capture. Use Capture Screenshot instead when you want to resolve a page type from a bare domain. |
| Scrape Styleguide | `scrapeStyleguide` | Extracts a website's design system as structured data - colors, typography, spacing, shadows, buttons and other UI components - from either a domain or an exact URL. |
| Search Brands | `searchBrands` | Searches the indexed brand database by company name or domain and returns matching brands with their domain, name and hosted logo URL. |
| Search Company News | `searchCompanyNews` | Searches live and historical news for one company identified by name, domain, stock ticker or ISIN, with optional filters on publisher, country, language, article type and publication date, and cursor pagination. |
| Search Web | `searchWeb` | Searches the web and optionally scrapes each result to Markdown in the same round-trip, with domain allow and block lists, freshness and country localization, and query fan-out for broader recall. |
| Submit Batch | `submitBatch` | Submits an asynchronous batch job that scrapes up to 25,000 URLs or crawls a large website in the background. Returns a batch ID to poll with Get Batch, and can notify a completion webhook when the batch settles. |
| Sync WebDB Collection | `syncWebdbCollection` | Queues an immediate sync run of a WebDB collection outside its schedule and returns the queued run ID. |
| Update Monitor | `updateMonitor` | Updates a monitor's name, tags, status, target, change detection, schedule or webhook. Changing the target or change detection makes the monitor create a new baseline, and unsupported target and detection combinations are rejected. |
| Update WebDB Collection | `updateWebdbCollection` | Updates a WebDB collection's name, description, row schema, eligibility, targets (complete replacement), sync schedule, change tracking, budgets, stale handling, or pauses and resumes syncing via status. Only the fields you pass are changed. |
| Update WebDB Webhook | `updateWebdbWebhook` | Updates a WebDB webhook's URL, subscribed events, watched collection, field filter, delivery mode or batch settings. Only the fields you pass are changed. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Monitor Change Detected | `change.detected` | Sent when a Context.dev monitor detects a change on its page, sitemap or extract target. Registered by attaching the fastn webhook URL to the monitor given in the monitorId input. Payload modelled from the official MonitorsChangeDetectedWebhookPayload schema (docs.context.dev/api-reference/monitors/webhook-payload). |
| Monitor Run Completed | `run.completed` | Sent after every completed run of a Context.dev monitor, including runs that found no change (change_detected false, change null). Registered by attaching the fastn webhook URL to the monitor given in the monitorId input. Payload modelled from the official MonitorsRunCompletedWebhookPayload schema (docs.context.dev/api-reference/monitors/webhook-run-completed). |
