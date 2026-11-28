---
description: "Simple Analytics is a privacy-friendly web analytics tool. Read website stats, export data points, add websites and send page views and events."
hidden: true
---

# Simple Analytics

<img src="../../.gitbook/assets/connectors/lg/simple-analytics.png" alt="Simple Analytics logo">

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [simpleanalytics.com](https://simpleanalytics.com) |
| **Authentication** | API key |
| **Slug** | `simpleAnalytics` |

## Setup

Your customers enter their API key for Simple Analytics when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Simple Analytics from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Simple Analytics**.
2. Select **Connect** on the Simple Analytics card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Simple Analytics's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Website</td><td><code>addWebsite</code></td><td>Adds a website to the connected Simple Analytics dashboard with an optional time zone, public or private visibility and label. This endpoint requires a Business or Enterprise plan, and Simple Analytics upgrades the account automatically when it is used.</td></tr><tr><td>Export Data Points</td><td><code>exportDataPoints</code></td><td>Exports raw, unsampled data points (page views or custom events) for a website and date range from the Export API, returning only the selected fields such as timestamp, path, referrer, UTM values, device, browser, country and metadata. Supports daily ranges and single-hour exports, JSON or CSV output (CSV is returned as plain text), time zone and robot inclusion.</td></tr><tr><td>Get Website Stats</td><td><code>getWebsiteStats</code></td><td>Retrieves aggregated statistics for a website from the Stats API, the same data shown on the dashboard: page views, visitors, histogram, top pages, countries, referrers, UTM values, browsers, operating systems, device types, median time on page and custom event counts. Supports date ranges, time zones, result limits and filters by page, country, referrer, UTM, browser, OS and device type. Public websites can be read without owning them.</td></tr><tr><td>List Websites</td><td><code>listWebsites</code></td><td>Lists all websites on the connected Simple Analytics user account. This Admin API endpoint is available on all plans.</td></tr><tr><td>Record Page View Pixel</td><td><code>recordPageViewPixel</code></td><td>Records a page view through the Simple Analytics no-JavaScript tracking pixel, passing the hostname, path, protocol, user agent, UTM values, referrer, time zone and uniqueness as pixel parameters. The response is a transparent GIF image; always include hostname and path so the page view can be stored.</td></tr><tr><td>Send Event</td><td><code>sendEvent</code></td><td>Submits a server-side page view or custom event to Simple Analytics, for example from a backend or mobile app, with optional path, referrer, UTM values, screen and viewport sizes, language, time zone and metadata. Data appears in the dashboard within minutes. Use a real or custom user agent; library default user agents are treated as robots.</td></tr></tbody></table>

