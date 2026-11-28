---
description: "Browserless is a hosted headless browser. Capture screenshots and PDFs, export pages, download files and read page content."
hidden: true
---

# Browserless

<img src="../../.gitbook/assets/connectors/lg/browserless.png" alt="Browserless logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [browserless.io](https://browserless.io) |
| **Authentication** | API key |
| **Slug** | `browserless` |

## Setup

Your customers enter their API key for Browserless when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Browserless from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Browserless**.
2. Select **Connect** on the Browserless card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Browserless's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Capture Screenshot</td><td><code>captureScreenshot</code></td><td>Renders a URL or a raw HTML string in a headless browser and returns a PNG or JPEG screenshot as a binary file. Supports full-page capture, clipping to a region, capturing a single element by CSS selector, and auto-scrolling to trigger lazy-loaded content. Supply either url or html, not both.</td></tr><tr><td>Create Debugger Session</td><td><code>createDebuggerSession</code></td><td>Opens a new browser tab on the Browserless instance and returns its Chrome DevTools target, including the target id and a signed WebSocket debugger URL you can attach a CDP client to. The tab consumes a browser session until it is closed, so always release it afterwards with Kill Session.</td></tr><tr><td>Download File</td><td><code>downloadFile</code></td><td>Runs your JavaScript in a Browserless browser session and returns the file that the code causes the browser to download. Use it to capture a report, export or generated document that a site only produces through a browser download, rather than at a fetchable URL.</td></tr><tr><td>Export Page</td><td><code>exportPage</code></td><td>Loads a URL in a headless browser and returns a single self-contained HTML document with the page's stylesheets, images and fonts inlined, so the capture renders offline exactly as it did live. Use it to archive a page rather than just read its markup.</td></tr><tr><td>Generate PDF</td><td><code>generatePdf</code></td><td>Renders a URL or a raw HTML string in a headless browser and returns the page as a PDF file. Supports paper size and margins, landscape orientation, background graphics, header and footer templates, and page ranges. Supply either url or html, not both.</td></tr><tr><td>Get Browser Version</td><td><code>getBrowserVersion</code></td><td>Returns the Chrome DevTools Protocol version banner for the Browserless instance, including the browser build, the protocol version, the default User-Agent string, the V8 and WebKit versions, and a signed WebSocket debugger URL you can connect Puppeteer or a CDP client to.</td></tr><tr><td>Get DevTools Protocol Schema</td><td><code>getDevToolsProtocol</code></td><td>Returns the full Chrome DevTools Protocol schema supported by this Browserless browser build, listing every CDP domain with its commands, events and types. Use it to discover which CDP calls are available before driving a session. The response is large, around 1.2 MB.</td></tr><tr><td>Get Instance Metadata</td><td><code>getInstanceMetadata</code></td><td>Returns metadata about the Browserless instance: the Browserless version and the exact Chromium, Firefox and WebKit builds it runs, plus the Playwright and Puppeteer client versions it accepts. Use it to pick a client library version that will connect successfully.</td></tr><tr><td>Get Page Content</td><td><code>getPageContent</code></td><td>Loads a URL (or a raw HTML string) in a headless browser and returns the fully rendered HTML of the page after JavaScript has executed. Use it instead of a plain HTTP fetch when the page is client-side rendered. Supply either url or html, not both.</td></tr><tr><td>Kill Session</td><td><code>killSession</code></td><td>Terminates a running Browserless browser session and frees the concurrency slot it holds. Pass the session, target or tracking id to kill one session, or the literal value 'all' to terminate every session on the account.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Active Sessions</td><td><code>listActiveSessions</code></td><td>Liveness check for your Browserless account: calls, which Per the Browserless OpenAPI reference it does NOT return a list of sessions (Browserless cloud has no list-sessions endpoint); use it as a health probe before starting work.</td></tr><tr><td>Run Browser Function</td><td><code>runBrowserFunction</code></td><td>Runs your own JavaScript inside a Browserless browser session and returns whatever it resolves. The code receives a ready Puppeteer page and browser plus the context object you pass, and must export a default async function. Use it for multi-step automation that the single-purpose endpoints cannot express.</td></tr><tr><td>Run BrowserQL Query</td><td><code>runBrowserQlQuery</code></td><td>Executes a BrowserQL query against a Browserless browser session. BrowserQL is Browserless's GraphQL automation language: a single mutation chains steps such as goto, click, type, waitForSelector, solve and screenshot, and returns their results together. Use it for scripted flows without writing Puppeteer code. Check the errors field, since an invalid query still</td></tr><tr><td>Run Performance Audit</td><td><code>runPerformanceAudit</code></td><td>Runs a Google Lighthouse audit against a URL in a real headless browser and returns the full Lighthouse report, including the performance, accessibility, best-practices and SEO category scores plus every individual audit. Optionally restrict the run to specific categories or assert against performance budgets.</td></tr><tr><td>Scrape Elements</td><td><code>scrapeElements</code></td><td>Loads a URL or raw HTML in a headless browser and extracts structured data for each CSS selector you list, returning the text, inner HTML, attributes and bounding box of every matching element. Use it instead of Get Page Content when you want parsed fields rather than a whole document.</td></tr><tr><td>Unblock Page</td><td><code>unblockPage</code></td><td>Loads a URL in a hardened browser that works through bot-detection and CAPTCHA interstitials, then returns any combination of the page HTML, a screenshot, the resulting cookies, and a WebSocket endpoint for taking over the already-unblocked session with Puppeteer or Playwright. Use it for sites that reject ordinary headless traffic.</td></tr></tbody></table>

</details>

