---
description: "ZenRows web scraping platform: the Fetch universal scraper API (JS rendering, premium residential proxies, screenshots, markdown/plaintext/PDF output, CSS and…"
hidden: true
---

# ZenRows

<img src="../../.gitbook/assets/connectors/lg/zenrows.png" alt="ZenRows logo">

ZenRows web scraping platform: the Fetch universal scraper API (JS rendering, premium residential proxies, screenshots, markdown/plaintext/PDF output, CSS and AI extraction), the Batch/Jobs async scraping API, Extract prepared-domain management, HMAC webhook signing keys and account credit usage.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [zenrows.com](https://zenrows.com) |
| **Authentication** | API key |
| **Slug** | `zenrows` |

## Use it

Add ZenRows from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zenrows.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Tasks To Job | `addJobTasks` | Append up to 10,000 more URLs to an open batch scraping job. Send last_batch true on the final call to lock the job; adds after that return 409. Each task scrapes at the normal Fetch credit tier once the run processes it. |
| Cancel HMAC Key Rotation | `cancelHmacKeyRotation` | Discard the staged candidate webhook signing key without promoting it, leaving the currently active key in place. Costs no credits. |
| Cancel Job Run | `cancelJobRun` | Cancel the current run of a batch scraping job. This is the vendor's documented alias of Stop Job Run and behaves identically; it exists so integrations written against /cancel keep working. Costs no credits. |
| Capture Page Network Requests | `fetchNetworkRequests` | Return the XHR and Fetch calls the page made while loading, as JSON, instead of only its HTML (json_response, which requires js_render). Use it to read the API a site calls rather than parsing its markup. Costs 5 credits per successful request. |
| Capture Page Screenshot | `fetchScreenshot` | Render a page in a real browser and return an image of it (screenshot, which requires js_render). Capture above the fold by default, the whole page with Full Page, or one element with a CSS selector. Choose PNG or JPEG, and set a JPEG quality from 1 to 100. Costs 5 credits per successful request. |
| Close Job To New Tasks | `closeJob` | Lock an open batch scraping job so no further tasks can be added. This is the explicit alternative to sending last_batch true on the final Add Tasks To Job call; later adds return 409. Costs no credits. |
| Create CSV Job Input | `createJobInput` | Create an upload slot for a CSV of target URLs, for lists too large to inline (limits 50 MB and 100,000 rows; the slot lives 24 hours). Returns file_input_id plus a presigned upload url and the exact headers to PUT the file with; then pass file_input_id to Create Scraping Job. Costs no credits. |
| Create Scraping Job | `createJob` | Submit a batch scraping job to the ZenRows async Batch API. ZenRows fetches every task URL on its own infrastructure and stores the result for 14 days. Returns 201 for fewer than 10,000 inline tasks and 202 for larger or CSV-fed submissions; both carry job_id and latest_run. Each successful task costs the normal Fetch credit tier (1 basic, 5 js_render, 10 premium_proxy, 25 both). |
| Delete Job Run | `deleteJobRun` | Delete one run's stored result bodies while keeping the job and its other runs. Use it once you have downloaded what you need; results are removed automatically 14 days after a run finishes anyway. Idempotent. Costs no credits. |
| Delete Job Webhook | `deleteJobWebhook` | Detach the webhook receiver from a batch scraping job so ZenRows stops posting run.completed events for it. Idempotent. Costs no credits. |

<details>

<summary>See 47 more actions</summary>

* **Delete Scraping Job** `deleteJob`: Delete an entire batch scraping job including every run and every stored result. Deleting a job with an active run stops it first. After this the job 404s and disappears from List Scraping Jobs. Costs no credits and cannot be undone.
* **Download Task Content** `getTaskContent`: Download the scraped body ZenRows stored for a single task of a job, without going through the presigned link in the results page. Returns the page content exactly as the scraper produced it. Costs no credits; the stored body is kept for 14 days after the run finishes.
* **Finalize HMAC Key Rotation** `finalizeHmacKeyRotation`: Promote the staged candidate webhook signing key to active and retire the previous one. Run it only once every receiver accepts signatures made with the candidate secret. Costs no credits.
* **Get Account Subscription And Credit Usage** `getSubscriptionDetails`: Read the ZenRows account's current subscription: plan name, status, billing period, credit limit, credits consumed so far and per-product usage (Fetch/WebScraping API, Data APIs, Extract, Residential Proxies, Scraping Browser). Costs no credits.
* **Get Domain Preparation Allowance** `getPreparedDomainAllowance`: Read how many new Extract domain preparations this account may still request in the current UTC month: used, limit, remaining and the month the count applies to. Costs no credits.
* **Get Job Run** `getJobRun`: Read one specific run of a batch scraping job by its run id, including its status, trigger and the stats and spend for that run alone. Use it to inspect an older run after a rerun has replaced latest_run. Costs no credits.
* **Get Job Webhook** `getJobWebhook`: Read the webhook receiver currently attached to a batch scraping job, including whether HMAC signing is enabled. Returns 404 with code not_found and the detail "Job has no webhook configured." when none is set. Costs no credits.
* **Get Prepared Domain Status** `getPreparedDomain`: Read one domain's Extract preparation record: status (preparing, ready, failed), state, submitted and updated timestamps, and any failure reason. Poll this after requesting a domain preparation. Costs no credits.
* **Get Run Export** `getRunExport`: Poll a ZIP export of a run until its status is completed, then read download_url to fetch the archive. The URL is presigned fresh on every poll, so always use the one from the latest response. Costs no credits.
* **Get Scraping Job** `getJob`: Read one batch scraping job and the progress of its latest run. latest_run.stats carries total, completed, successful, failed and the spend object with the credits the run has actually consumed. Poll this until completed equals total. Costs no credits.
* **List Extract-Supported Domains** `listExtractDomains`: List every domain ZenRows Extract can already return structured JSON for, with each domain's content verticals and whether it is warm. Use it to check a site is supported before calling Scrape Structured Data. Costs no credits.
* **List HMAC Keys** `listHmacKeys`: List the metadata of the account's webhook HMAC signing keys - the active key and any staged candidate - with their ids and timestamps. Secrets are never returned here; a secret is shown only once, by Rotate HMAC Key. Costs no credits.
* **List Job Results** `listJobResults`: List the per-URL results of a job's latest run, filtered by status and paged with a cursor. Each row carries the task id, the target url, the HTTP status, a presigned content download link and a spend object with the credits that task consumed. Costs no credits.
* **List Job Runs** `listJobRuns`: List every run of a batch scraping job, newest first, paged with a cursor. A regular job has one run per rerun; a scheduled job gains a run each time its schedule fires. Costs no credits.
* **List Requested Prepared Domains** `listPreparedDomains`: List the domain preparation requests this ZenRows account has submitted, each with its status and state, alongside the current monthly allowance. Costs no credits.
* **List Scraping Jobs** `listJobs`: List the batch scraping jobs on this ZenRows account, newest first, optionally filtered by run status and job type. Page through with the cursor from next_cursor until it is null. Costs no credits.
* **Pause Job Run** `pauseJobRun`: Reversibly suspend the current run of a batch scraping job so no further tasks are picked up. Restart it with Resume Job Run. This acts on the run, not on a scheduled job's firing - use Set Job Schedule State for that. Costs no credits.
* **Replace Job Schedule** `replaceJobSchedule`: Replace the schedule of a scheduled batch scraping job. Supply exactly one of at (a one-shot wall-clock time), rate (an every/unit interval) or calendar (times_of_day plus a cadence), with a timezone for at and calendar. Times of day must be full hours and runs must be at least 60 minutes apart. Costs no credits; each fire spends credits for its tasks.
* **Request Domain Preparation** `requestDomainPreparation`: Ask ZenRows to prepare a domain for Extract so structured JSON can be returned for it. Returns 202 with the starting record. Each new domain consumes one slot of the monthly preparation allowance; resubmitting an already prepared domain returns its current record and consumes nothing. Send an Idempotency-Key to make retries safe.
* **Rerun Job** `rerunJob`: Replay a batch scraping job as a brand new run. Leave the status filter empty to re-scrape every task, or set it to failed to retry only the failures (append ,pending to also pick up tasks that never started). Every task the rerun scrapes successfully costs credits again at its Fetch tier.
* **Resume Job Run** `resumeJobRun`: Resume a paused run of a batch scraping job so its remaining tasks are picked up again. Returns the refreshed run object. Costs no credits.
* **Rotate HMAC Key** `rotateHmacKey`: Create the account's first webhook signing key, or stage a candidate alongside the active one. SECURITY: the generated secret is returned in this response and nowhere else - store it immediately and treat the response as sensitive. Promote the candidate with Finalize HMAC Key Rotation or discard it with Cancel HMAC Key Rotation. Costs no credits.
* **Scrape After Fixed Delay** `fetchAfterDelay`: Pause a fixed number of milliseconds after the page loads before capturing it (wait, which requires js_render). Use it for sites that render in stages when there is no single selector to wait on. Costs 5 credits per successful request.
* **Scrape After Running JavaScript** `fetchWithJsInstructions`: Run your own sequence of browser instructions on the page before capturing it - click, fill, scroll, evaluate, wait - then return the resulting HTML (js_instructions, which requires js_render). Use it to dismiss banners, submit a form or expand lazy content. Costs 5 credits per successful request.
* **Scrape After Waiting For Selector** `fetchWaitingForSelector`: Hold the browser open until a given CSS selector appears in the DOM, then capture the page (wait_for, which requires js_render). Use it for elements that load asynchronously at unpredictable times. Costs 5 credits per successful request.
* **Scrape Allowing Error Pages** `fetchAllowingErrorCodes`: Return the target's page content even when it answers with a status you list, instead of failing the request (allowed_status_codes). Use it to capture 404 or 410 pages, or to debug why a target is rejecting you. 1 credit.
* **Scrape From A Specific Country** `fetchFromCountry`: Scrape a page through a residential IP located in the country you name (proxy_country, which requires premium_proxy). Use it for geo-restricted pages and region-specific pricing or inventory. Costs 10 credits per successful request.
* **Scrape Keeping The Same IP** `fetchWithSession`: Reuse one exit IP across a series of requests for up to 10 minutes by passing the same session id (session_id). Essential for multi-step flows where the target ties state to the client address. Costs the normal tier of whatever other options you combine it with, 1 credit on its own.
* **Scrape Page As Markdown** `fetchPageMarkdown`: Scrape a page and get it back converted to Markdown instead of HTML (response_type=markdown). Ideal for feeding page content to an LLM or storing readable text. 1 credit.
* **Scrape Page As PDF** `fetchPagePdf`: Render a page in a real browser and return it as a PDF document (js_render=true and response_type=pdf). Useful for archiving or visual records. 5 credits (JavaScript rendering tier).
* **Scrape Page As Plain Text** `fetchPagePlaintext`: Scrape a page and get only its visible text, stripped of all HTML tags (response_type=plaintext). 1 credit.
* **Scrape Page HTML** `fetchPageHtml`: Fetch the raw HTML of any public web page through the ZenRows Fetch universal scraper API, with proxy rotation and anti-bot handling. Cheapest tier: 1 credit per successful request. Returns the page source as text.
* **Scrape Returning The Target's Status Code** `fetchWithOriginalStatus`: Pass the target site's own HTTP status code back instead of ZenRows' (original_status=true), so a 301, 404 or 503 on the target surfaces as that status. Use it when your logic branches on what the target actually answered. 1 credit.
* **Scrape Selected Output Types** `fetchWithOutputFilters`: Scrape a page and return only chosen data types pulled out of its HTML (outputs), such as emails, headings, links, images, tables, menus, metadata, phone_numbers, favicon or videos. Pass them comma-separated. 1 credit.
* **Scrape Structured Data With Extract** `fetchWithExtract`: Scrape a page and return structured JSON automatically, with no selectors to write (extract=auto). Works on domains ZenRows has prepared - check List Extract-Supported Domains first. Optionally narrow the payload with extract_fields. Free during beta: you pay only the underlying Fetch cost, 1 credit at the basic tier.
* **Scrape Through Residential Proxy** `fetchWithPremiumProxy`: Route the request through ZenRows' residential IP pool instead of its datacenter pool (premium_proxy=true), for sites with strong anti-bot protection. Costs 10 credits per successful request, or 25 when combined with JavaScript rendering.
* **Scrape With Adaptive Stealth Mode** `fetchWithStealthMode`: Let ZenRows choose the anti-bot configuration for you (mode=auto): it escalates from a plain fetch through JavaScript rendering and residential proxies until the target answers, and bills only the configuration that succeeded. Costs between 1 and 25 credits per successful request, so the price is not known in advance.
* **Scrape With Autoparse** `fetchWithAutoparse`: Scrape a page and let ZenRows apply its general-purpose parser to return structured JSON with no selectors (autoparse=true). Deprecated by the vendor in favour of Scrape Structured Data With Extract, but still supported for existing integrations. 1 credit.
* **Scrape With Blocked Resources** `fetchWithBlockedResources`: Stop chosen resource types loading in the browser to cut bandwidth and speed the scrape up (block_resources, which requires js_render). Blocking is on by default, so change it only when the page needs a type that is normally blocked. Costs 5 credits per successful request.
* **Scrape With CSS Selectors** `fetchWithCssExtractor`: Scrape a page and return only the fields you name, picked out with CSS selectors (css_extractor). Pass a JSON string mapping output field names to CSS selectors, for example a title mapped to h1 and links mapped to a @href. Returns JSON rather than HTML. 1 credit.
* **Scrape With Custom Request Headers** `fetchWithCustomHeaders`: Scrape a page while forwarding your own referer, user-agent and cookie headers to the target site (custom_headers=true), to simulate arriving from a specific page or to carry a session cookie. 1 credit. KNOWN LIMITATION: the fastn HTTP engine also appends every header-only input to the GET query string, and ZenRows rejects unknown query parameters with REQS004, so this action currently fails at the vendor. Until that is fixed, pass custom headers through Create Scraping Job instead, where they travel inside the JSON body as zenrows_params.custom_headers.
* **Scrape With JavaScript Rendering** `fetchWithJsRender`: Scrape a page in a real headless browser so client-side JavaScript runs before the HTML is captured (js_render=true). Use it for single-page apps, dashboards and any content injected after load. Costs 5 credits per successful request instead of 1.
* **Set Job Schedule State** `setJobScheduleState`: Pause or reactivate a scheduled batch scraping job so its schedule stops or starts firing new runs. This is distinct from Pause Job Run, which suspends the run that is already in flight. Costs no credits.
* **Set Job Webhook** `setJobWebhook`: Attach or replace the HTTPS receiver that ZenRows POSTs the run.completed event to when a batch scraping job's run finishes. Set signature true for HMAC-SHA256 signed deliveries, verified against the key from List HMAC Keys. Costs no credits.
* **Start Run Export** `createRunExport`: Bundle every stored result body of one run into a single ZIP archive. Returns an export_id and a status to poll with Get Run Export. Exports expire 12 hours after creation and a run whose results exceed 100 GiB fails rather than producing a partial archive. Costs no credits.
* **Stop Job Run** `stopJobRun`: Terminally stop the current run of a batch scraping job. No new tasks are picked up; tasks already in flight may still record a result and pending tasks are left untouched. Idempotent on an already stopped run, 409 if the run is completed or deleted. Costs no credits.
* **Test Webhook Receiver** `testWebhookReceiver`: Send a probe delivery to an HTTPS receiver before wiring it to a job, and read back whether ZenRows could deliver it and what status code the receiver returned. Use it to validate a webhook endpoint and its HMAC signature handling. Costs no credits.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Scraping Run Completed | `run.completed` | ZenRows POSTs this to the receiver attached to a batch scraping job when that job's run finishes, whether it succeeded, failed or was stopped. Deliveries are at-least-once, so deduplicate on the X-ZenRows-Event-Id header. When the webhook was registered with signature true, each delivery also carries X-Signature in the form t=&lt;unix&gt;,v1=&lt;hex&gt;,kid=&lt;key id&gt;, where v1 is HMAC-SHA256 over "&lt;t&gt;.&lt;raw body&gt;" using the base64 secret returned once by Rotate HMAC Key. PAYLOAD SCHEMA IS MODELLED FROM THE VENDOR'S DOCUMENTATION, NOT FROM A CAPTURED DELIVERY: ZenRows publishes the event name and the signing scheme but no sample body. Treat the run and job identifiers as authoritative and re-read the job with Get Scraping Job before acting. |
