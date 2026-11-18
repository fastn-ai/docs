---
description: "ScrapeGraphAI is an AI-powered web data extraction API."
hidden: true
---

# ScrapeGraphAI

<img src="../../.gitbook/assets/connectors/lg/scrapegraph-ai.png" alt="ScrapeGraphAI logo">

ScrapeGraphAI is an AI-powered web data extraction API. This connector covers the ScrapeGraphAI v2 API: multi-format page scraping, natural-language structured extraction, web search with inline content, asynchronous crawls with status, paginated pages, stop, resume and delete, scheduled monitors with change detection and webhook delivery, request history, credits, API key validation and health, plus the agent payment, offering discovery and agent enrollment endpoints.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [scrapegraphai.com](https://scrapegraphai.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `scrapegraphAi` |

## Use it

Add ScrapeGraphAI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.scrapegraphAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Buy Access With MPP | `buyAccessWithMpp` | Keyless purchase that mints a new ScrapeGraphAI account, API key and credit pack paid in USDC through the Machine Payments Protocol. Without a payment credential the API answers 402 with an MPP challenge; the returned API key is shown only once. |
| Buy Access With x402 | `buyAccessWithX402` | Keyless purchase over the x402 rail that mints an account, API key and credit pack paid in USDC on Base. Without a payment signature the API answers 402 with an x402 challenge; retry with the PAYMENT-SIGNATURE value from an x402 wallet. |
| Cancel Agent Subscription | `cancelAgentSubscription` | Cancels the InFlow agent subscription tied to the connected API key, stopping future billing. Paid access and subscription credits remain through the paid period; top-up credits and the API key are retained. |
| Create Monitor | `createMonitor` | Creates a monitor that fetches a URL on a cron schedule in the chosen formats, records change diffs between runs and optionally posts each tick payload to a webhook URL. Each tick is billed at the format cost, plus 5 credits when a change is detected. |
| Delete Crawl | `deleteCrawl` | Permanently deletes a crawl job record and its stored pages. This cannot be undone. |
| Delete Monitor | `deleteMonitor` | Permanently deletes a monitor and its tick history. |
| Enroll Agent | `enrollAgent` | Registers an AI agent's did:web identity with ScrapeGraphAI through the Agent Enrollment Protocol and provisions a free-plan account. Requires an AEP client assertion signed with the agent's did:web key. |
| Extract Data | `extractData` | Extracts structured JSON from a URL, raw HTML or markdown using a natural-language prompt and an optional JSON Schema, returning the typed result with raw model output, token usage and chunking metadata. Provide exactly one source: url, html or markdown. |
| Get AEP Document | `getAepDocument` | Returns the Agent Enrollment Protocol (AEP 1.0) inspect document: supported authentication and identity methods, commands, grant types, signing algorithms and the HTTP endpoint base. |
| Get Agent Payment Protocols | `getAgentPaymentProtocols` | Returns the agent payment discovery document: supported payment protocols and methods, keyless access, subscription, refill, balance and subscription management endpoints, available USDC credit packs and subscription plans. |

<details>

<summary>See 33 more actions</summary>

* **Get Agent Subscription** `getAgentSubscription`: Returns the InFlow agent subscription tied to the connected API key: status, plan, billing period, paid-through date, cancellation, renewal flag and separate subscription and top-up credit balances. Returns not found when the key has no agent subscription.
* **Get Crawl Pages** `getCrawlPages`: Returns a cursor-paginated slice of a crawl job's pages with each page's metadata and its resolved scrape result, such as markdown or links. Use pagination.nextCursor to fetch the next slice until it is null.
* **Get Crawl Status** `getCrawlStatus`: Returns the status, progress counters and lightweight per-page metadata of a crawl job, including each page's URL, depth, links and scrape reference ID. Poll every few seconds until the status is completed, failed or stopped.
* **Get Credits** `getCredits`: Returns the account's remaining and used credits, active plan name, and crawl and monitor job usage against plan limits. This call costs no credits.
* **Get DID Document** `getDidDocument`: Returns the did:web document for the ScrapeGraphAI API origin, which agents check to confirm the service identity matches the origin.
* **Get Health** `getHealth`: Checks ScrapeGraphAI service health, returning ok when its database and cache are reachable or degraded otherwise, with service uptime.
* **Get History Entry** `getHistoryEntry`: Retrieves the full record of a single past request by its ID, including the complete result payload. Accepts IDs returned by Scrape URL, Extract Data, Search Web, crawl page scrapeRefId values and monitor tick IDs.
* **Get Monitor** `getMonitor`: Retrieves a single monitor by its ID, including schedule, status and the resolved configuration.
* **Get Monitor Activity** `getMonitorActivity`: Returns recent ticks for a monitor with status, timing, change flag and per-format diffs, newest first, with cursor pagination for older ticks.
* **Get ODP Service Document** `getOdpServiceDocument`: Returns the Offering Discovery Protocol (ODP 1.0) service document for ScrapeGraphAI, describing the service, branding, documentation and the operations agents use to discover and buy offerings.
* **Get Offering** `getOffering`: Retrieves a single ScrapeGraphAI offering, such as a credit pack or subscription plan, by ID in ODP 1.0 format.
* **Get Offering Collection** `getOfferingCollection`: Retrieves a single ScrapeGraphAI offering collection by ID in ODP 1.0 format.
* **Get Service Info** `getServiceInfo`: Returns the ScrapeGraphAI service card with links to the documentation, the OpenAPI specification, the agent payment protocols and the agent discovery documents.
* **Get Subscription Attribute Schema** `getSubscriptionAttributeSchema`: Returns the JSON Schema describing ScrapeGraphAI agent subscription attributes such as plan ID, billing term, credits per month and term, credit grant, auto-renewal and features.
* **Grant Agent Credential** `grantAgentCredential`: Issues an SGAI-APIKEY session credential for an enrolled agent through the Agent Enrollment Protocol. Requires an AEP client assertion signed with the agent's did:web key.
* **List Collection Offerings** `listCollectionOfferings`: Lists the offerings inside a ScrapeGraphAI offering collection in ODP 1.0 format.
* **List History** `listHistory`: Lists recent API requests on the account, newest first, with service, status, parameters, result reference, error, timing, parent request and session ID. Filter by service or by a case-insensitive partial session ID, and page through results.
* **List Monitors** `listMonitors`: Lists all monitors on the account with their ID, schedule, status, failure counters, configuration and timestamps. The API returns a bare array, exposed here as items.
* **List Offering Collections** `listOfferingCollections`: Lists ScrapeGraphAI offering collections, such as credit packs and agent subscriptions, in ODP 1.0 format.
* **List Offerings** `listOfferings`: Lists purchasable ScrapeGraphAI offerings, credit packs and agent subscriptions, in ODP 1.0 format with ID, name, description, collections and USDC price.
* **Pause Monitor** `pauseMonitor`: Pauses a monitor so no further ticks run, while keeping the monitor record and its history.
* **Purchase Credit Pack** `purchaseCreditPack`: Buys a USDC credit pack for the connected account using the Machine Payments Protocol. Without a payment credential the API answers 402 Payment Required with a WWW-Authenticate Payment challenge; retry with the credential from an MPP wallet in Payment Credential to complete the purchase and receive the added credits.
* **Resume Crawl** `resumeCrawl`: Resumes a stopped or paused crawl job from its last frontier.
* **Resume Monitor** `resumeMonitor`: Resumes a paused monitor and puts it back on its schedule immediately.
* **Revoke Agent Credential** `revokeAgentCredential`: Revokes an enrolled agent's API key credentials through the Agent Enrollment Protocol; revoked API keys are deleted. Requires an AEP client assertion signed with the agent's did:web key.
* **Scrape URL** `scrapeUrl`: Fetches a public URL and returns its content in one or more formats in a single call: markdown, HTML, links, images, an AI summary, structured JSON extraction, branding, or a screenshot. Supports content type overrides, MIME allowlists, PDF page limits, fetch options such as JavaScript rendering, stealth proxies, headers, cookies, scrolls, wait time and country, and an optional session ID for grouping requests in history.
* **Search Web** `searchWeb`: Runs a web search, fetches the top results and returns each result's URL, title and inline content in markdown or HTML. Optionally runs an AI extraction across all results with a prompt and JSON Schema, with recency filters, country localization, MIME allowlists, PDF limits and fetch options.
* **Start Crawl** `startCrawl`: Starts an asynchronous multi-page crawl from a URL and immediately returns a crawl job ID. Controls include output formats per page, maximum pages, depth and links per page, external links, include and exclude URL patterns, MIME allowlist, PDF limits and fetch options. Poll Get Crawl Status and fetch content with Get Crawl Pages.
* **Stop Crawl** `stopCrawl`: Stops an in-flight crawl job. Pages already fetched remain available and no further URLs are expanded.
* **Subscribe With MPP** `subscribeWithMpp`: Keyless monthly agent subscription through InFlow MPP that provisions a separate account with a stable API key and the plan's monthly credits. Without a payment credential the API answers 402 with an inflow subscription challenge.
* **Subscribe With MPP For Billing Period** `subscribeWithMppBillingPeriod`: Keyless monthly or yearly agent subscription through InFlow MPP for a chosen plan, provisioning a separate account with a stable API key; yearly billing grants twelve months of credits at once. Without a payment credential the API answers 402 with a subscription challenge.
* **Update Monitor** `updateMonitor`: Updates a monitor's name, cron interval, formats, webhook URL or fetch options. Only the fields you send are changed.
* **Validate API Key** `validateApiKey`: Validates the connected API key and returns the email of the user who owns it.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Monitor Change Detected | `monitor.change.detected` | Fires when a ScrapeGraphAI monitor tick detects that the watched page changed compared with the previous run (the first tick always counts as a change). Subscribing creates a monitor through the ScrapeGraphAI API for the page in the monitorUrl input, on the cron schedule in interval (default every 30 minutes), capturing the format input (default markdown), with the fastn webhook URL as its webhookUrl; unsubscribing deletes that monitor. Each tick costs the format's credits plus 5 credits when a change is detected. The payload schema was captured from a real delivery; ScrapeGraphAI does not sign webhook requests. |
