---
description: "Diffbot turns web pages into structured data and exposes a Knowledge Graph of organizations, people, articles and products."
hidden: true
---

# Diffbot

<img src="../../.gitbook/assets/connectors/diffbot.png" alt="Diffbot logo" width="64">

Diffbot turns web pages into structured data and exposes a Knowledge Graph of organizations, people, articles and products. This connector covers the full Diffbot API surface: the Extract APIs (analyze, article, product, image, video, discussion, event, list, job, plus raw-HTML POST extraction), Custom APIs, Crawl, Bulk Extract, Web Search, Knowledge Graph Search (DQL) with coverage reports, Enhance (single, combine and bulk), the Natural Language API, and the Account API.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [diffbot.com](https://diffbot.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `diffbot` |

## Use it

Add Diffbot from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.diffbot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Analyze Text | `analyzeText` | Run Diffbot's Natural Language API over a block of text (1-100,000 characters) to get named entities linked to Knowledge Graph URIs with confidence, salience and sentiment; extracted facts with evidence; structured records; document sentiment; a generated summary; and IAB/Diffbot category labels. |
| Analyze URL | `analyzeUrl` | Visit a page, classify its page-type (article, product, image, discussion, job, event, video or list) and automatically route it to the matching Extract API, returning the structured result plus the detected type. Use this when the page type is not known in advance. Costs 1 Diffbot credit per call. |
| Combine Person With Employer | `combinePersonWithEmployer` | Enrich a person and return both the matched Person entity and their current employer Organization in a single call - up to two entities per request. Identify the person with any combination of name, email, phone, employer, title, school, location, url or ip. The size parameter is not supported here. Consumes Knowledge Graph credits. |
| Create Bulk Enhance Job | `createBulkEnhanceJob` | Submit many records to be matched against the Knowledge Graph asynchronously. The body is a JSON array of entity stubs, each with a type and whatever identifying fields are known. Returns HTTP 202 with a job_id to poll with getBulkEnhanceStatus, and can call a webhook when finished. Consumes Knowledge Graph credits per record matched. |
| Create Bulk Job | `createBulkJob` | Submit a list of URLs to be extracted asynchronously in one batch. Each URL is processed by the Extract API given in apiUrl and the results are collected under the job name. Diffbot accepts the parameters by GET or POST; paid plans enforce a minimum batch size (50 URLs on Startup) while the free plan accepts small batches. Each processed URL costs 1 Diffbot credit. Note: api.diffbot.com/v3/bulk sends no Content-Type header, so the JSON body is delivered as a raw JSON string; the schema below documents the parsed shape. |
| Create Crawl | `createCrawl` | Start a Crawlbot job: spider one or more seed URLs, follow links that match the crawl pattern, and run every matching page through an Extract API into a named collection. Diffbot accepts the same parameters by GET or POST. Crawls obey robots.txt. Each processed page costs 1 Diffbot credit, so cap maxToCrawl/maxToProcess on a trial run. Note: api.diffbot.com/v3/crawl sends no Content-Type header, so the JSON body is delivered as a raw JSON string; the schema below documents the parsed shape. |
| Create Or Update Custom API | `createOrUpdateCustomApi` | Create a Custom API, or update an existing one, by posting a ruleset. Matching on urlPattern plus api updates the existing Custom API; changing either value creates a new one. The rules array fully replaces the previous rules, so send the complete set. Pass the whole definition as a JSON string in the definition input. Free. |
| Delete Custom API | `deleteCustomApi` | Permanently delete a Custom API from this token, identified by the same api and urlPattern pair used to create it. Deletion is irreversible - back the definition up with listCustomApis first. Free. |
| Enhance Entity | `enhanceEntity` | Match a person or organization you already know something about (name, email, phone, URL, employer, location, IP) against the Knowledge Graph and return the enriched entity with a match score. Set refresh to re-crawl the entity's origins and search to look for new origins on the web. Consumes Knowledge Graph credits. |
| Enhance Entity (POST) | `enhanceEntityPost` | Same single-entity Knowledge Graph enrichment as enhanceEntity, submitted as a JSON body so that long field lists, multi-valued name/url/email inputs and long JsonPath filters are not limited by URL length. Consumes Knowledge Graph credits. |

<details>

<summary>See 23 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Extract Article | `extractArticle` | Extract clean article content from a news story, blog post or other text-heavy page: title, author, date, plain text, HTML, images, tags, sentiment and categories. Costs 1 Diffbot credit per call. |
| Extract Discussion | `extractDiscussion` | Extract a forum thread, comment section or review list as structured posts: author, date, text, votes, nesting and sentiment, with automatic pagination across the thread. Costs 1 Diffbot credit per call. |
| Extract Event | `extractEvent` | Extract event details from an event listing page: event name, description, start and end date/time, venue, address, organiser, performers and ticket/offer information. Costs 1 Diffbot credit per call. |
| Extract From Raw HTML | `extractFromRawHtml` | POST raw HTML (or plain text) directly to an Extract API instead of asking Diffbot to fetch a live URL - useful for pages behind a login, local files or content you already have in hand. Set apiType to the Extract API to run (article, product, image, video, discussion, event, job, list or analyze) and pass the markup in html. The url input is only a label used for relative-link resolution. Costs 1 Diffbot credit per call. |
| Extract Image | `extractImage` | Extract the images from an image-heavy page or a direct image URL, returning URL, dimensions, caption/alt text, mime type and (optionally) computer-vision derived classifications and colour data. Costs 1 Diffbot credit per call. |
| Extract Job Posting | `extractJob` | Extract a job posting page into structured fields: job title, employer, location, employment type, salary, description, required skills and posting date. Costs 1 Diffbot credit per call. |
| Extract List | `extractList` | Extract a listing/index page (search results, category page, directory) into its repeated items, returning each item's title, link, summary and image so the links can be fed to another Extract API or to Crawl. Costs 1 Diffbot credit per call. |
| Extract Product | `extractProduct` | Extract product data from an e-commerce page: title, description, brand, offer price, regular price, availability, SKU, MPN, UPC, specs, images and breadcrumbs. Costs 1 Diffbot credit per call. |
| Extract Video | `extractVideo` | Extract video metadata from a video page (YouTube, Vimeo and similar): title, description, author, duration, view count, embed URL, thumbnail and the direct video URL where available. Costs 1 Diffbot credit per call. |
| Extract With Custom API | `extractWithCustomApi` | Run one of your own Custom APIs against a URL. Works exactly like the standard Extract APIs but applies your custom rules, returning the custom fields and collections alongside the base fields. Set apiName to the Custom API's name. Costs 1 Diffbot credit per call. |
| Get Account | `getAccount` | Return the Diffbot account tied to the token: plan name, plan credit allowance, plan start date, account creation date and a day-by-day usage breakdown (credits, extractions, entities, nlp, proxies, videos, subtitles, refresh, facets). Free and consumes no credits - the cheapest call to verify a token. Note: api.diffbot.com/v4/account sends no Content-Type header, so the JSON body is delivered as a raw JSON string; the schema below documents the parsed shape. |
| Get Bulk Enhance Status | `getBulkEnhanceStatus` | Poll an asynchronous bulk enhance job: how many records have been matched, the job state (NOT_STARTED, IN_PROCESS, COMPLETE, FAILED), the estimated time remaining, result counts and any coverage reports generated for the job. Diffbot returns a top-level JSON ARRAY of status objects (one per matching job), which is documented under `jobs` below because an action output contract must be an object. Free. |
| Get Coverage Report By ID | `getCoverageReportById` | Download a previously generated coverage report by its reportId - the id returned when a DQL search is run with report=true. Returns the report as CSV. Responds 404 when the id is unknown or the report has expired. |
| Get Coverage Report By Query | `getCoverageReportByQuery` | Generate a coverage report for a DQL query: a CSV showing, for the entities the query matches, how completely each requested field is populated in the Knowledge Graph. Use exportspec to choose the columns. KNOWN VENDOR ISSUE (verified 2026-09-16 both through this connector and with a direct curl, with and without exportspec): kg.diffbot.com/kg/v3/dql/report responds HTTP 500 {"code":500,"message":"HTTP 500 Internal Server Error"} for every query. Until Diffbot fixes it, generate the report by calling searchKnowledgeGraph with report=true and then download it with getCoverageReportById, which both work. |
| List Custom APIs | `listCustomApis` | Return every Custom API defined on this token with its full ruleset - the base Extract API it extends, the urlPattern it matches, its testUrl and each extraction rule. The response body is a top-level JSON array of definitions. Use it to back up Custom API definitions before updating them, because updates overwrite rules irreversibly. Free. |
| Manage Bulk Job | `manageBulkJob` | View, pause, resume, restart or delete Bulk Extract jobs. With no inputs it lists every bulk job on the token with its status code (0 initializing, 6 paused, 7 in progress, 9 completed), success counts and timestamps. Restarting erases previously processed data; deleting is irreversible. Note: api.diffbot.com/v3/bulk sends no Content-Type header, so the JSON body is delivered as a raw JSON string; the schema below documents the parsed shape. |
| Manage Crawl | `manageCrawl` | View, pause, resume, restart, start a new round of, or delete Crawlbot jobs. Called with no inputs it lists every crawl job on the token with its status code (0 initializing, 2 reached maxToCrawl, 6 paused, 9 complete, 11 paused for crawl inefficiency), counters and timestamps. Deleting a job also deletes its collected data and cannot be undone. Note: api.diffbot.com/v3/crawl sends no Content-Type header, so the JSON body is delivered as a raw JSON string; the schema below documents the parsed shape. |
| Retrieve Bulk Job Data | `retrieveBulkJobData` | Download the extracted results of a Bulk Extract job as JSON (default) or CSV, or the diagnostic URL Report with type=urls. Free - the credits were spent when the job ran. Returns HTTP 400 when no job matches the name. |
| Retrieve Crawl Data | `retrieveCrawlData` | Download the structured results a crawl job has collected, as JSON (default) or CSV. Set type to 'urls' to download the diagnostic URL Report instead, listing every URL the crawl attempted with its HTTP status and processing outcome. Free - the credits were spent during the crawl. |
| Search Knowledge Graph | `searchKnowledgeGraph` | Query the Diffbot Knowledge Graph with a DQL query string and get back matching Organization, Person, Article, Product or other entities with their full fact set and a relevance score. Supports field filtering with JsonPath, paging, article de-duplication and CSV/Excel export. Consumes Knowledge Graph credits. |
| Search Knowledge Graph (POST) | `searchKnowledgeGraphPost` | Same Knowledge Graph DQL search as searchKnowledgeGraph, but with the query and options sent as a JSON body so that very long queries and long JsonPath filter lists are not limited by URL length. Pass the body as a JSON string. Consumes Knowledge Graph credits. |
| Web Search | `webSearch` | Search the live web through Diffbot's index and get back ranked results with a relevance score, page URL, title, a highlighted content excerpt and (where known) the publication date. The query supports the after:, before:, site: and url: operators. Authenticates with a Bearer token rather than the token query parameter. Caution: a small maxTokens (observed at 150 and below) makes Diffbot return an empty search_results array rather than shortened excerpts - leave maxTokens unset unless you have verified the value returns results. |
| Web Search (POST) | `webSearchPost` | Same live web search as webSearch, but submitted as a JSON body so that longer queries and up to five simultaneous query strings can be sent. Pass the body as a JSON string, e.g. {"text":["diffbot","site:diffbot.com pricing"],"size":5}. Authenticates with a Bearer token. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Bulk Enhance job finished | `enhance.bulk.completed` | Diffbot calls the URL given in the webhookurl query parameter of the Create Bulk Enhance Job action when an asynchronous Knowledge Graph bulk-enhance job finishes. Again there is no registration API - the customer passes this trigger's URL per job. The payloadSchema is the real bulk-enhance status object captured from this connector's Get Bulk Enhance Status action (execution 0c8a9acb); Diffbot's documentation does not publish the callback body separately, so treat the shape as modelled on that status object. |
| Bulk Extract job finished | `bulk.completed` | Diffbot POSTs the finished bulk job's JSON metadata when a Bulk Extract job completes. As with crawls, there is no registration API: the customer passes this trigger's URL as the notifyWebhook parameter on the Create Bulk Job action. The payloadSchema is the real bulk job object captured from this connector's Create Bulk Job action (execution 4a91e32f) with the parent 'jobs' wrapper removed. |
| Crawl job finished | `crawl.completed` | Diffbot POSTs the finished crawl job's JSON metadata when a Crawlbot job completes or hits its maxToCrawl / maxToProcess limit. Diffbot has NO webhook-registration API: the customer supplies this trigger's URL per job, by passing it as the notifyWebhook parameter on the Create Crawl action (Diffbot dashboard: Crawlbot &gt; the job &gt; Advanced Settings &gt; Notify Webhook). The POST carries X-Crawl-Name and X-Crawl-Status HTTP HEADERS and the individual job object as the body - the parent 'jobs' wrapper is not sent. The payloadSchema below is the real job object captured from this connector's Manage Crawl action (execution 25ca78c3) with the wrapper removed. |
