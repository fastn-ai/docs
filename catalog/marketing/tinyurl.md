---
description: "TinyURL shortens and tracks links. Create, update, archive and delete short links, run bulk requests and read click analytics."
hidden: true
---

# TinyURL

<img src="../../.gitbook/assets/connectors/lg/tinyurl.png" alt="TinyURL logo">

| | |
| --- | --- |
| **Category** | [Marketing](README.md) |
| **Authentication** | API token |
| **Slug** | `tinyurl` |

## Setup

Your customers enter their API token for TinyURL when they connect. Nothing else needs setting up.

## Use it

Add TinyURL from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tinyurl.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Archive TinyURL</td><td><code>archiveTinyUrl</code></td><td>Toggles a TinyURL between archived and available. Archiving hides the link from the active list while keeping it resolvable.</td></tr><tr><td>Change Long URL</td><td><code>changeTinyUrlDestination</code></td><td>Points an existing TinyURL at a different destination long URL, keeping the same short link.</td></tr><tr><td>Count TinyURLs</td><td><code>countTinyUrls</code></td><td>Returns the number of available or archived TinyURLs on the account, honouring the same date-range and search filters as the list action.</td></tr><tr><td>Create Bulk Request</td><td><code>createBulkRequest</code></td><td>Submits a batch of TinyURL operations (create, update, change, delete, archive or unarchive) for asynchronous processing and returns the batch identifier.</td></tr><tr><td>Create TinyURL</td><td><code>createTinyUrl</code></td><td>Shortens a long URL into a new TinyURL, optionally with a custom alias, tags, description and expiry.</td></tr><tr><td>Delete TinyURL</td><td><code>deleteTinyUrl</code></td><td>Permanently deletes a TinyURL so that the short link no longer resolves.</td></tr><tr><td>Get Browser, OS and Device Analytics</td><td><code>getGeneralAnalytics</code></td><td>Returns the browser, operating system and device breakdown of clicks on the account's TinyURLs.</td></tr><tr><td>Get Bulk Request Report</td><td><code>getBulkRequestReport</code></td><td>Returns the per-item outcome of a processed bulk request, including the resulting TinyURL and any failure comment for each row.</td></tr><tr><td>Get Bulk Request Status</td><td><code>getBulkRequestStatus</code></td><td>Returns the processing status and success/failure counts of a previously submitted bulk request.</td></tr><tr><td>Get Hourly Popularity Analytics</td><td><code>getHourlyPopularityAnalytics</code></td><td>Returns click counts grouped by hour of the day, as a twenty-four element array starting at midnight.</td></tr></tbody></table>

<details>

<summary>View 11 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Location Analytics</td><td><code>getLocationAnalytics</code></td><td>Returns click counts by geography. Pass world to break clicks down by country, or a two-letter country code to break that country down by region.</td></tr><tr><td>Get Raw Analytics Logs</td><td><code>getRawAnalyticsLogs</code></td><td>Returns the raw click log for the account's TinyURLs over a time window, one entry per click with referrer, IP, country, browser, operating system, device and language.</td></tr><tr><td>Get Timeline Analytics</td><td><code>getTimelineAnalytics</code></td><td>Returns click totals over time for the account's TinyURLs, bucketed by minute, hour, day, week or month.</td></tr><tr><td>Get TinyURL</td><td><code>getTinyUrl</code></td><td>Returns a single TinyURL's configuration, destination URL, tags, analytics settings and click counts.</td></tr><tr><td>Get Top Languages</td><td><code>getTopLanguagesAnalytics</code></td><td>Returns the visitor languages that produced the most clicks on the account's TinyURLs.</td></tr><tr><td>Get Top Traffic Sources</td><td><code>getTopSourcesAnalytics</code></td><td>Returns the referring domains that sent the most clicks to the account's TinyURLs, along with the direct-traffic count.</td></tr><tr><td>Get Weekday Popularity Analytics</td><td><code>getWeekdayPopularityAnalytics</code></td><td>Returns click counts grouped by day of the week, as a seven-element array starting with Monday.</td></tr><tr><td>List TinyURLs</td><td><code>listTinyUrls</code></td><td>Lists the account's available or archived TinyURLs, optionally filtered by creation date range or by an alias or tag search term.</td></tr><tr><td>Set Analytics Collection</td><td><code>setAnalyticsCollection</code></td><td>Enables or disables collection of click analytics for a single TinyURL.</td></tr><tr><td>Set Analytics Sharing</td><td><code>setAnalyticsSharing</code></td><td>Makes a TinyURL's analytics report publicly viewable, or returns it to private.</td></tr><tr><td>Update TinyURL</td><td><code>updateTinyUrl</code></td><td>Updates an existing TinyURL's alias, domain, tags, description, expiry or analytics collection setting. Tags supplied here overwrite the existing tags.</td></tr></tbody></table>

</details>

## Events

TinyURL has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
