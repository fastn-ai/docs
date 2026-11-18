---
description: "ScreenshotAPI.net renders any URL or raw HTML into a PNG, JPG, WebP or PDF, records scrolling screenshots as MP4/WebM/GIF, and scrapes page text, HTML,…"
hidden: true
---

# Screenshot API

<img src="../../.gitbook/assets/connectors/lg/screenshot-api.png" alt="Screenshot API logo">

ScreenshotAPI.net renders any URL or raw HTML into a PNG, JPG, WebP or PDF, records scrolling screenshots as MP4/WebM/GIF, and scrapes page text, HTML, Markdown and image URLs. This connector covers the render endpoint on shot.screenshotapi.net/v3 with every documented capture family (viewport and full page, element capture and cropping, file type and quality, caching, lazy loading and delay, CSS and JavaScript injection, device and locale emulation, resource blocking, PDF rendering, scrolling video, proxying and bring-your-own-bucket storage) plus the account endpoint and the bulk screenshot API on api.screenshotapi.net/v1.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [screenshotapi.net](https://screenshotapi.net) |
| **Authentication** | Credentials you enter |
| **Slug** | `screenshotApi` |

## Use it

Add Screenshot API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.screenshotApi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Bulk Job | `cancelBulkJob` | Stops a running bulk screenshot job for good. Bulk job control is a paid-plan feature; free-trial accounts get 403 {"error":"This feature is available on paid plans only"}. |
| Capture Cached Screenshot | `captureCachedScreenshot` | Captures a page with caching controls, so repeat requests for the same URL and options can be served from a previously stored file for a configurable time to live instead of rendering again. |
| Capture Element Screenshot | `captureElementScreenshot` | Captures a single element matched by a CSS selector instead of the whole page, with optional cropping, element removal, blurring and clicking before the shot is taken. Consumes one screenshot from the account quota. |
| Capture Full Page Screenshot | `captureFullPageScreenshot` | Captures the entire scrollable height of a page rather than just the viewport, scrolling the page to trigger lazily loaded content on the way down. Consumes one screenshot from the account quota. |
| Capture Lazy Loaded Page | `captureLazyLoadedPage` | Captures a page that loads content as you scroll, by scrolling it first and waiting a configurable delay and browser event before the shot is taken. Use it for infinite feeds and image galleries that render blank otherwise. |
| Capture Screenshot Via Legacy Endpoint | `captureScreenshotLegacy` | Calls the older unversioned /screenshot path on shot.screenshotapi.net, which ScreenshotAPI still serves for integrations written before the v3 rollout. Behaviour and parameters match the current render endpoint; new work should use Capture Website Screenshot instead. |
| Capture Through A Proxy | `captureThroughProxy` | Routes the headless browser through a proxy server you supply, so the target site sees the proxy's IP and country. Useful for geo-specific renders and for reaching pages that block data-centre traffic. |
| Capture To Your Own Storage Bucket | `captureToOwnBucket` | Captures a page and writes the file straight into your own Amazon S3, Wasabi or Google Cloud bucket instead of ScreenshotAPI storage. The bucket must already be configured and tested on the Storage Integrations tab of the dashboard. |
| Capture Website Screenshot | `captureScreenshot` | Renders a URL in a real browser and returns the captured image. With output=JSON (the default) the response is metadata containing a public 'screenshot' URL; with output=image the raw PNG, JPG, WebP or PDF bytes are returned instead. Each successful capture consumes one screenshot from the account quota. |
| Capture With Device And Locale Emulation | `captureWithEmulation` | Captures a page while emulating a specific browser identity and locale - user agent, accepted languages, time zone, geolocation, dark mode, grayscale, incognito mode, custom request headers and cookies - so localized or personalized variants of a page can be rendered. |

<details>

<summary>See 43 more actions</summary>

* **Capture With Injected CSS And JavaScript** `captureWithInjectedCode`: Captures a page after injecting custom CSS and JavaScript, supplied either inline or as a remote file URL. Used to hide elements, restyle a page or dismiss overlays before the screenshot is taken.
* **Capture With Resource Blocking** `captureWithResourceBlocking`: Captures a page while blocking selected network resource classes - ads, trackers, chat widgets, cookie banners, images, stylesheets, fonts, media, XHR, fetch, websockets and more - to produce a faster or cleaner screenshot.
* **Create Billing Portal Session** `createBillingPortalSession`: Opens a Stripe customer billing portal session for the account and returns its one-time URL, which the account owner can follow to manage payment methods, invoices and the subscription. Creates no charge.
* **Download Bulk Job Results** `downloadBulkJobResults`: Downloads the finished bulk job as a CSV that repeats the submitted rows and adds the screenshot URL and per-row status. An unknown uuid returns 404 {"error":"Bulk request not found"}.
* **Extract Image URLs From Page** `extractImageUrls`: Captures the page and additionally returns the source URLs of every image found on it, for asset auditing and scraping workflows.
* **Extract Page HTML** `extractPageHtml`: Captures the page and additionally writes its fully rendered HTML, after JavaScript has executed, to a stored .html file, returning that file's URL as extracted_html. Not supported when file_type is pdf.
* **Extract Page Markdown** `extractPageMarkdown`: Captures the page and additionally writes its content as Markdown to a stored .md file, returning that file's URL as markdown_file. Useful for feeding a web page to an LLM. Not supported when file_type is pdf.
* **Extract Page Text** `extractPageText`: Captures the page and additionally writes its rendered plain text to a stored .txt file, returning that file's URL as extracted_text alongside the screenshot URL. Not supported when file_type is pdf.
* **Get Account And Usage** `getAccount`: Returns the authenticated ScreenshotAPI user and their team, including the screenshot quota counters screenshotsThisMonth and totalScreenshots, the plan, trial start date and Stripe customer id. SECURITY: the response also contains Team.apiToken, which is the account's own API key in plaintext.
* **Get Bulk Job Status** `getBulkJobStatus`: Polls a bulk screenshot job by uuid and returns its progress, including percent_complete, successful_urls and failed_urls. An unknown uuid returns 404 {"error":"Bulk request not found"}.
* **Get Daily Screenshot Usage** `getDailyUsage`: Returns the account's screenshot consumption broken down by day, with successful and failed counts per day plus running totals. This is the meter to read before driving a large capture workload.
* **Get Invoice Email Preference** `getInvoiceEmailPreference`: Returns whether a given user has opted in to receiving invoice emails.
* **Get My Permissions** `getMyPermissions`: Returns the permission matrix of the user the API key belongs to, covering the s3, team, user, admin and alert areas with get, create, update and delete flags.
* **Get Overage Allowance Setting** `getOverageAllowance`: Returns whether the team is allowed to keep capturing past its plan allowance and be billed for the overage. Subscription is null while the team has no paid plan.
* **Get Plan Quota Status** `getPlanQuotaStatus`: Returns how much of the paid plan's screenshot allowance has been consumed in the current billing period. Trial accounts with no subscription get 404 {"error":"no subscription found."} - use Get Daily Screenshot Usage instead.
* **Get Subscription Details** `getSubscriptionDetails`: Returns the account's current paid subscription. An account on the free trial with no subscription gets 400 {"error":"this team doesn't have a subscription","errorType":"no-subscription"}.
* **Get Team API Token** `getTeamApiToken`: Returns the team record including its current API token. SECURITY: the response contains Team.apiToken, the account's live API key in plaintext - anything that can call this action can read the credential. Treat the output as secret.
* **Get Team Member By Id** `getTeamMemberById`: Returns one team member's name, email and role through the team endpoint. The bare path with no id returns a vendor 500, so always supply a numeric user id.
* **Get Team Member Profile** `getTeamMemberProfile`: Returns the public profile of one user on your ScreenshotAPI team by numeric user id: first name, last name, email and role. Use Get Account And Usage to find your own id.
* **Get Trial Status** `getTrialStatus`: Returns whether the free trial is still active, when it ends and how many days remain.
* **Get Usage Notification History** `getUsageNotifications`: Returns the team's quota-usage alert settings and the history of usage-threshold emails already sent.
* **Get User Permissions** `getUserPermissions`: Returns the permission matrix of one team member by numeric user id.
* **List Billing Invoices** `listBillingInvoices`: Lists the invoices raised against the ScreenshotAPI account. Returns an empty list for accounts that are still on the free trial and have never been billed.
* **List Bulk Screenshot Jobs** `listBulkJobs`: Lists the bulk screenshot jobs submitted by the account, each with its uuid, state and counts. The uuid returned here is what Get Bulk CSV Job Status and Download Bulk CSV Results expect.
* **List Cookie Templates** `listCookieTemplates`: Lists the saved cookie templates for a team. A template id from here is what the template_id capture parameter expects, so a page behind a login can be rendered with a stored browser state. Templates are created in the dashboard under Cookies Template, not through the API.
* **List Scheduled Screenshot Requests** `listScheduledRequests`: Lists the team's recurring scheduled screenshot jobs with their cadence and target URLs. Schedules are created, started, stopped and deleted in the dashboard under Scheduled Requests; the API exposes this read only.
* **List Screenshot History** `listScreenshotHistory`: Lists the account's past captures, newest first, each with the requested URL, creation time, stored file URL, the role of the user who requested it, status and any error. Paginated; the page parameter is required because the unpaginated form can time out.
* **List Sitemap Snapshot Jobs** `listSitemapSnapshotJobs`: Lists the team's Sitemap Snapshot jobs, which crawl a site's sitemap and capture every page. Each row carries the job uuid, state and counts.
* **List Storage Integrations** `listStorageIntegrations`: Lists the team's configured bring-your-own-bucket storage destinations - Amazon S3, Wasabi and Google Cloud - whose service and bucket names the Capture To Your Own Storage Bucket action needs. Buckets are added in the dashboard under Storage Integrations, not through the API.
* **List Subscription Plans** `listSubscriptionPlans`: Lists the ScreenshotAPI subscription plans available for purchase, grouped into monthly and yearly, as Stripe price objects with their product, amount, currency and included screenshot allowance.
* **List Team Invitations** `listTeamInvitations`: Lists pending invitations to join the ScreenshotAPI team.
* **Pause Bulk Job** `pauseBulkJob`: Temporarily halts a running bulk screenshot job; Resume Bulk Job continues it. Bulk job control is a paid-plan feature; free-trial accounts get 403 {"error":"This feature is available on paid plans only"}.
* **Record Scrolling Screenshot Video** `recordScrollingScreenshot`: Records a video of the page scrolling from top to bottom and returns an MP4, WebM or GIF. Controls cover scroll speed, clip duration, scrolling back to the top and starting before the page finishes loading. Consumes one screenshot from the account quota.
* **Record Scrolling Screenshots At Multiple Sizes** `recordMultiSizeScrollingScreenshot`: Records the same scrolling screenshot at several viewport sizes in one call. VENDOR DEFECT (verified 2026-09-22): multiple_scrolling=true answers 200 but returns "screenshot":{} with no file URLs, for gif and mp4 and for both documented shapes of the sizes array, so the call currently produces nothing. Use Record Scrolling Screenshot Video once per size until ScreenshotAPI fixes it.
* **Render Custom HTML To Image** `renderCustomHtml`: Renders a block of raw HTML supplied in the request instead of navigating to a URL, and returns the captured image. Useful for social cards, invoices and generated reports. Consumes one screenshot from the account quota.
* **Render Web Page To PDF** `renderPdf`: Renders a page as a PDF document with paper format, orientation, print background and page range control through the pdf_options parameters. Consumes one screenshot from the account quota.
* **Resume Bulk Job** `resumeBulkJob`: Continues a bulk screenshot job that was paused. Bulk job control is a paid-plan feature; free-trial accounts get 403 {"error":"This feature is available on paid plans only"}.
* **Roll Team API Token** `rollTeamApiToken`: Issues a brand new ScreenshotAPI key for the team and immediately revokes the old one. DESTRUCTIVE AND IRREVERSIBLE: the key this connection authenticates with stops working the moment it succeeds, and every other integration using it breaks. Only run it as a deliberate rotation, and update the connection's API Key afterwards with the value returned here.
* **Start Bulk Job With Completion Webhook** `startBulkJobWithWebhook`: Submits a bulk screenshot job the way the ScreenshotAPI dashboard does, and is the only place a webhook can be registered: supply webhookUrl and ScreenshotAPI POSTs the finished results to it instead of only emailing a download link. The registered URL is then visible as webhook_url on the job row returned by List Bulk Screenshot Jobs. Bulk processing is a paid-plan feature; free-trial accounts get 403 "Bulk processing is available on paid plans only".
* **Start Bulk Screenshot Job From CSV** `startBulkCsvJob`: Uploads a CSV whose required url column lists the pages to capture, with optional file_type, width, height, delay and fresh columns, and starts a bulk job. Bulk processing is a paid-plan feature; free-trial accounts receive 403 "Bulk processing is available on paid plans only".
* **Start Bulk Screenshot Job From URL List** `startBulkJsonJob`: Submits up to 50 URLs, each with its own rendering options, as a single bulk screenshot job and returns the job uuid. Bulk processing is a paid-plan feature; free-trial accounts receive 403 "Bulk processing is available on paid plans only".
* **Start Sitemap Snapshot Job** `startSitemapSnapshotJob`: Submits a Sitemap Snapshot job, which captures every page listed for a site. Paid-plan feature; free-trial accounts get 403 "Sitemap Screenshot is available on paid plans only".
* **Validate Billing Coupon** `validateBillingCoupon`: Checks a ScreenshotAPI promotional coupon code against the account's billing profile and returns the coupon's discount when it is valid. The endpoint always answers 200: an unusable code comes back as {"sucess":false,"coupon":null,"error":"Invalid coupon code"} (the misspelling of 'success' is the vendor's), so read the body rather than the status.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Bulk screenshot job completed | `bulk.completed` | Fires once a ScreenshotAPI bulk screenshot job finishes and the result set is ready to download. REGISTRATION: ScreenshotAPI has no standalone webhook API - a callback URL can only be attached to an individual bulk job at submission time. Either (a) call the action 'Start Bulk Job With Completion Webhook' and pass your fastn webhook URL as webhookUrl, or (b) in the ScreenshotAPI dashboard at https://app.screenshotapi.net open the Bulk tab, click Webhook to expand the panel, paste the URL into the 'https://your-webhook-url.com' field, then upload the CSV - the dashboard rejects any value that does not begin with http:// or https://. Confirm registration by calling 'List Bulk Screenshot Jobs': the job row then carries webhook_url. To unsubscribe there is no API call - cancel the job with 'Cancel Bulk Job', or submit future jobs without webhookUrl. BOTH paths require a paid plan: on a free trial every bulk submission returns 403 'Bulk processing is available on paid plans only', so no delivery could be captured. PAYLOAD SCHEMA BELOW IS MODELLED from the dashboard's own bulk-history fields (queue_id, webhook_url, percent_complete, successful_urls, failed_urls) and from the documented CSV download shape - it has NOT been verified against a real delivery. |
