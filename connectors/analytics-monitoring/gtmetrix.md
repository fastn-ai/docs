---
description: "GTmetrix is a web page performance testing service."
---

# GTmetrix

GTmetrix is a web page performance testing service. This connector covers the GTmetrix REST API 2.0: starting page tests, polling test state, reading performance reports and their resources (screenshots, filmstrip, HAR, Lighthouse JSON, PDF, video), managing tested pages and their report history, retesting, and looking up test locations, browsers, simulated devices and API credit status.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [gtmetrix.com](https://gtmetrix.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 28 |
| **Events** | 0 |
| **Slug** | `gtmetrix` |

## Use it

Add GTmetrix from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.gtmetrix.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Page | `deletePage` | Permanently deletes a page and all of its associated reports by page ID. Not available to Team plan Viewer roles. |
| Delete Report | `deleteReport` | Permanently deletes a performance report by its ID. Not available to Team plan API keys with the Viewer role. |
| Get API Status | `getApiStatus` | Returns the API credit balance, next refill time and plan capabilities for the account that owns the API key. GTmetrix responds with the JSON:API media type, which fastn returns as a base64-encoded file reference. |
| Get Browser | `getBrowser` | Retrieves a single test browser by its ID, including its platform and supported analysis features. |
| Get Location | `getLocation` | Retrieves a single GTmetrix test location by its ID. |
| Get Page | `getPage` | Retrieves a tested page by its ID, including its URL, location, browser, monitoring frequency, report count and latest report. |
| Get Page Latest Report | `getPageLatestReport` | Retrieves the most recent report for a page by page ID, with the same grade, score, metric and resource-link fields as Get Report. |
| Get Report | `getReport` | Retrieves a completed performance report by its ID, including GTmetrix grade and scores, Web Vitals, timing metrics, page size and request counts, and links to report resources such as screenshots, HAR and Lighthouse JSON. |
| Get Report Filmstrip | `getReportFilmstrip` | Retrieves the filmstrip for a report: the list of page-load frames with their timings and frame image URLs. Set base64 to 1 to embed the frame images as base64 data. |
| Get Report Filmstrip Frame | `getReportFilmstripFrame` | Downloads a single filmstrip frame image for a report by frame index, returned as a JPEG file reference. |
| Get Report HAR | `getReportHar` | Downloads the HTTP Archive (HAR) of all network requests recorded during the report's page load. Returned as a file reference; set pretty to 1 for indented JSON. |
| Get Report Lighthouse JSON | `getReportLighthouse` | Downloads the raw Lighthouse result JSON for a report generated with the lighthouse report type. Returned as a file reference; optionally compressed or pretty-printed. |
| Get Report PDF | `getReportPdf` | Renders and downloads the report as a PDF file reference. Charged 0.2 API credits per request (0.3 for the full PDF). Not available to Team plan Viewer roles. |
| Get Report Resource | `getReportResource` | Downloads any report resource by its file name, such as report.pdf, screenshot.jpg, net.har, lighthouse.json, filmstrip.json, video.mp4, pagespeed.json, yslow.json, pagespeed-files.zip, or the legacy optimized image bundle. Returned as a file reference. PDF resources incur credit charges. |
| Get Report Resource Summary | `getReportResourceSummary` | Retrieves the resource summary JSON for a report: request counts and byte totals broken down by resource type such as HTML, JavaScript, CSS, images and fonts. |
| Get Report Screenshot | `getReportScreenshot` | Downloads the page screenshot captured for a report as a JPEG image, returned as a file reference. Optionally request the full-page screenshot or the shareable version. |
| Get Report Video | `getReportVideo` | Downloads the page-load video (MP4) for a report whose test was started with the video option. Returned as a file reference; reports without video respond with 404. |
| Get Simulated Device | `getSimulatedDevice` | Retrieves a single simulated device by its ID, including its user agent, viewport size and pixel ratio. |
| Get Test | `getTest` | Retrieves the state of a test by its ID. Poll this until state is completed, then read the report ID from the response and fetch it with Get Report. |
| List Browsers | `listBrowsers` | Lists the browsers available for testing, with each browser's platform and the analysis features it supports (AdBlock, Lighthouse, cookies, DNS, throttling, video and more). |
| List Locations | `listLocations` | Lists all GTmetrix test locations with their region, supported browsers, server IPs, availability and whether your plan has access to each. |
| List Page Reports | `listPageReports` | Lists the reports generated for a page, newest first by default, with pagination, sorting and filters on source, location, browser, grade, scores, timestamps and key performance metrics. Each filter accepts a value for the named comparison (eq, gt, gte, lt, lte). |
| List Pages | `listPages` | Lists the pages (unique URL, location and browser combinations) that have been tested on the account, with pagination, sorting and filters on location, browser, monitoring frequency, URL and timestamps. |
| List Simulated Devices | `listSimulatedDevices` | Lists the simulated devices (phones and tablets) that can be used with the simulate_device test option, including each device's user agent, viewport size and pixel ratio. |
| List Tests | `listTests` | Lists tests on the account with pagination, sorting and filters on source, state, location, browser and created, started or finished timestamps. By default only API-started tests are returned; set filter[source] to any to include on-demand and monitored tests. |
| Retest Page | `retestPage` | Starts a new test for an existing page using the page's URL, location and browser. Consumes API credits like Start Test and returns the queued test. |
| Retest Report | `retestReport` | Starts a new test using the same URL and analysis options as an existing report. Consumes API credits like Start Test and returns the queued test. |
| Start Test | `startTest` | Starts a new GTmetrix page performance test with the given URL and analysis options. Consumes API credits depending on the report type and add-ons. Returns the queued test whose state can be polled with Get Test; on a Basic account only two tests may run concurrently (HTTP 429 otherwise). |
