---
description: "Simple Analytics is a privacy-friendly web analytics platform."
hidden: true
---

# Simple Analytics

<img src="../../.gitbook/assets/connectors/lg/simple-analytics.png" alt="Simple Analytics logo">

Simple Analytics is a privacy-friendly web analytics platform. This connector covers the Simple Analytics APIs: the Stats API for aggregated page views, visitors, histograms, referrers, UTM, device and event counts; the Export API for raw page view and event data points; the Admin API for listing and adding websites; and server-side collection of page views and events, including the no-JavaScript pixel.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [simpleanalytics.com](https://simpleanalytics.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `simpleAnalytics` |

## Use it

Add Simple Analytics from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.simpleAnalytics.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Website</td><td><code>addWebsite</code></td><td>Adds a website to the connected Simple Analytics dashboard with an optional time zone, public or private visibility and label. This endpoint requires a Business or Enterprise plan, and Simple Analytics upgrades the account automatically when it is used.</td></tr><tr><td>Export Data Points</td><td><code>exportDataPoints</code></td><td>Exports raw, unsampled data points (page views or custom events) for a website and date range from the Export API, returning only the selected fields such as timestamp, path, referrer, UTM values, device, browser, country and metadata. Supports daily ranges and single-hour exports, JSON or CSV output (CSV is returned as plain text), time zone and robot inclusion.</td></tr><tr><td>Get Website Stats</td><td><code>getWebsiteStats</code></td><td>Retrieves aggregated statistics for a website from the Stats API, the same data shown on the dashboard: page views, visitors, histogram, top pages, countries, referrers, UTM values, browsers, operating systems, device types, median time on page and custom event counts. Supports date ranges, time zones, result limits and filters by page, country, referrer, UTM, browser, OS and device type. Public websites can be read without owning them.</td></tr><tr><td>List Websites</td><td><code>listWebsites</code></td><td>Lists all websites on the connected Simple Analytics user account. This Admin API endpoint is available on all plans.</td></tr><tr><td>Record Page View Pixel</td><td><code>recordPageViewPixel</code></td><td>Records a page view through the Simple Analytics no-JavaScript tracking pixel, passing the hostname, path, protocol, user agent, UTM values, referrer, time zone and uniqueness as pixel parameters. The response is a transparent GIF image; always include hostname and path so the page view can be stored.</td></tr><tr><td>Send Event</td><td><code>sendEvent</code></td><td>Submits a server-side page view or custom event to Simple Analytics, for example from a backend or mobile app, with optional path, referrer, UTM values, screen and viewport sizes, language, time zone and metadata. Data appears in the dashboard within minutes. Use a real or custom user agent; library default user agents are treated as robots.</td></tr></tbody></table>
