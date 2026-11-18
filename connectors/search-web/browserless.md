---
description: "Browserless is a hosted headless-browser platform."
---

# Browserless

Browserless is a hosted headless-browser platform. Use it to render pages, capture screenshots and PDFs, scrape structured data, run Puppeteer/Playwright code remotely, audit page performance with Lighthouse, bypass bot detection, and drive BrowserQL automation flows against the Browserless v2 REST API.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [browserless.io](https://browserless.io) |
| **Authentication** | API key |
| **Actions** | 16 |
| **Events** | 0 |
| **Slug** | `browserless` |

## Use it

Add Browserless from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.browserless.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Capture Screenshot | `captureScreenshot` | Renders a URL or a raw HTML string in a headless browser and returns a PNG or JPEG screenshot as a binary file. Supports full-page capture, clipping to a region, capturing a single element by CSS selector, and auto-scrolling to trigger lazy-loaded content. Supply either url or html, not both. |
| Create Debugger Session | `createDebuggerSession` | Opens a new browser tab on the Browserless instance and returns its Chrome DevTools target, including the target id and a signed WebSocket debugger URL you can attach a CDP client to. The tab consumes a browser session until it is closed, so always release it afterwards with Kill Session. |
| Download File | `downloadFile` | Runs your JavaScript in a Browserless browser session and returns the file that the code causes the browser to download. Use it to capture a report, export or generated document that a site only produces through a browser download, rather than at a fetchable URL. |
| Export Page | `exportPage` | Loads a URL in a headless browser and returns a single self-contained HTML document with the page's stylesheets, images and fonts inlined, so the capture renders offline exactly as it did live. Use it to archive a page rather than just read its markup. |
| Generate PDF | `generatePdf` | Renders a URL or a raw HTML string in a headless browser and returns the page as a PDF file. Supports paper size and margins, landscape orientation, background graphics, header and footer templates, and page ranges. Supply either url or html, not both. |
| Get Browser Version | `getBrowserVersion` | Returns the Chrome DevTools Protocol version banner for the Browserless instance, including the browser build, the protocol version, the default User-Agent string, the V8 and WebKit versions, and a signed WebSocket debugger URL you can connect Puppeteer or a CDP client to. |
| Get DevTools Protocol Schema | `getDevToolsProtocol` | Returns the full Chrome DevTools Protocol schema supported by this Browserless browser build, listing every CDP domain with its commands, events and types. Use it to discover which CDP calls are available before driving a session. The response is large, around 1.2 MB. |
| Get Instance Metadata | `getInstanceMetadata` | Returns metadata about the Browserless instance: the Browserless version and the exact Chromium, Firefox and WebKit builds it runs, plus the Playwright and Puppeteer client versions it accepts. Use it to pick a client library version that will connect successfully. |
| Get Page Content | `getPageContent` | Loads a URL (or a raw HTML string) in a headless browser and returns the fully rendered HTML of the page after JavaScript has executed. Use it instead of a plain HTTP fetch when the page is client-side rendered. Supply either url or html, not both. |
| Kill Session | `killSession` | Terminates a running Browserless browser session and frees the concurrency slot it holds. Pass the session, target or tracking id to kill one session, or the literal value 'all' to terminate every session on the account. Returns HTTP 204 with no body on success. |
| List Active Sessions | `listActiveSessions` | Liveness check for your Browserless account: calls GET /active, which returns HTTP 204 with no body when the Browserless service is up and accepting your token. Per the Browserless OpenAPI reference it does NOT return a list of sessions (Browserless cloud has no list-sessions endpoint); use it as a health probe before starting work. |
| Run Browser Function | `runBrowserFunction` | Runs your own JavaScript inside a Browserless browser session and returns whatever it resolves. The code receives a ready Puppeteer page and browser plus the context object you pass, and must export a default async function. Use it for multi-step automation that the single-purpose endpoints cannot express. |
| Run BrowserQL Query | `runBrowserQlQuery` | Executes a BrowserQL query against a Browserless browser session. BrowserQL is Browserless's GraphQL automation language: a single mutation chains steps such as goto, click, type, waitForSelector, solve and screenshot, and returns their results together. Use it for scripted flows without writing Puppeteer code. Check the errors field, since an invalid query still returns HTTP 200. |
| Run Performance Audit | `runPerformanceAudit` | Runs a Google Lighthouse audit against a URL in a real headless browser and returns the full Lighthouse report, including the performance, accessibility, best-practices and SEO category scores plus every individual audit. Optionally restrict the run to specific categories or assert against performance budgets. |
| Scrape Elements | `scrapeElements` | Loads a URL or raw HTML in a headless browser and extracts structured data for each CSS selector you list, returning the text, inner HTML, attributes and bounding box of every matching element. Use it instead of Get Page Content when you want parsed fields rather than a whole document. |
| Unblock Page | `unblockPage` | Loads a URL in a hardened browser that works through bot-detection and CAPTCHA interstitials, then returns any combination of the page HTML, a screenshot, the resulting cookies, and a WebSocket endpoint for taking over the already-unblocked session with Puppeteer or Playwright. Use it for sites that reject ordinary headless traffic. |
