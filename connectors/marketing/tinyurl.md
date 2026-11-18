---
description: "TinyURL is a link-management service for shortening long URLs into branded short links, organising them with aliases and tags, and measuring the clicks they…"
hidden: true
---

# TinyURL

<img src="../../.gitbook/assets/connectors/lg/tinyurl.png" alt="TinyURL logo">

TinyURL is a link-management service for shortening long URLs into branded short links, organising them with aliases and tags, and measuring the clicks they receive. This connector covers the TinyURL v2 REST API: link create, update, repoint, archive, delete, list and count; bulk batch processing; per-link analytics settings; and the full click-analytics reporting family (raw logs, timeline, browser/OS/device, weekday and hourly popularity, top sources, top languages and geography).

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Authentication** | Credentials you enter |
| **Slug** | `tinyurl` |

## Use it

Add TinyURL from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tinyurl.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive TinyURL | `archiveTinyUrl` | Toggles a TinyURL between archived and available. Archiving hides the link from the active list while keeping it resolvable. |
| Change Long URL | `changeTinyUrlDestination` | Points an existing TinyURL at a different destination long URL, keeping the same short link. |
| Count TinyURLs | `countTinyUrls` | Returns the number of available or archived TinyURLs on the account, honouring the same date-range and search filters as the list action. |
| Create Bulk Request | `createBulkRequest` | Submits a batch of TinyURL operations (create, update, change, delete, archive or unarchive) for asynchronous processing and returns the batch identifier. |
| Create TinyURL | `createTinyUrl` | Shortens a long URL into a new TinyURL, optionally with a custom alias, tags, description and expiry. |
| Delete TinyURL | `deleteTinyUrl` | Permanently deletes a TinyURL so that the short link no longer resolves. |
| Get Browser, OS and Device Analytics | `getGeneralAnalytics` | Returns the browser, operating system and device breakdown of clicks on the account's TinyURLs. |
| Get Bulk Request Report | `getBulkRequestReport` | Returns the per-item outcome of a processed bulk request, including the resulting TinyURL and any failure comment for each row. |
| Get Bulk Request Status | `getBulkRequestStatus` | Returns the processing status and success/failure counts of a previously submitted bulk request. |
| Get Hourly Popularity Analytics | `getHourlyPopularityAnalytics` | Returns click counts grouped by hour of the day, as a twenty-four element array starting at midnight. |
| Get Location Analytics | `getLocationAnalytics` | Returns click counts by geography. Pass world to break clicks down by country, or a two-letter country code to break that country down by region. |
| Get Raw Analytics Logs | `getRawAnalyticsLogs` | Returns the raw click log for the account's TinyURLs over a time window, one entry per click with referrer, IP, country, browser, operating system, device and language. |
| Get Timeline Analytics | `getTimelineAnalytics` | Returns click totals over time for the account's TinyURLs, bucketed by minute, hour, day, week or month. |
| Get TinyURL | `getTinyUrl` | Returns a single TinyURL's configuration, destination URL, tags, analytics settings and click counts. |
| Get Top Languages | `getTopLanguagesAnalytics` | Returns the visitor languages that produced the most clicks on the account's TinyURLs. |
| Get Top Traffic Sources | `getTopSourcesAnalytics` | Returns the referring domains that sent the most clicks to the account's TinyURLs, along with the direct-traffic count. |
| Get Weekday Popularity Analytics | `getWeekdayPopularityAnalytics` | Returns click counts grouped by day of the week, as a seven-element array starting with Monday. |
| List TinyURLs | `listTinyUrls` | Lists the account's available or archived TinyURLs, optionally filtered by creation date range or by an alias or tag search term. |
| Set Analytics Collection | `setAnalyticsCollection` | Enables or disables collection of click analytics for a single TinyURL. |
| Set Analytics Sharing | `setAnalyticsSharing` | Makes a TinyURL's analytics report publicly viewable, or returns it to private. |
| Update TinyURL | `updateTinyUrl` | Updates an existing TinyURL's alias, domain, tags, description, expiry or analytics collection setting. Tags supplied here overwrite the existing tags. |
