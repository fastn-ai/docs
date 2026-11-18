---
description: "Plausible Analytics is a privacy-friendly, cookie-free web analytics platform."
hidden: true
---

# Plausible Analytics

<img src="../../.gitbook/assets/connectors/lg/plausible.png" alt="Plausible Analytics logo">

Plausible Analytics is a privacy-friendly, cookie-free web analytics platform. This connector covers the Stats API v2 query endpoint for aggregate, timeseries, breakdown and absolute date-range reporting, the Stats API v1 realtime, aggregate, timeseries and breakdown endpoints, and the Sites API for managing sites, shared dashboard links and conversion goals. Requests authenticate with a Plausible API key sent as a bearer token.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [plausible.io](https://plausible.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `plausible` |

## Use it

Add Plausible Analytics from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.plausible.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Goal</td><td><code>createGoal</code></td><td>Creates a conversion goal on a site, or returns the existing goal when an identical one already exists. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401.</td></tr><tr><td>Create Shared Link</td><td><code>createSharedLink</code></td><td>Creates a shared dashboard link for a site, or returns the existing link when one with the same name already exists. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401.</td></tr><tr><td>Create Site</td><td><code>createSite</code></td><td>Creates a new site in the Plausible account. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401.</td></tr><tr><td>Delete Goal</td><td><code>deleteGoal</code></td><td>Deletes a conversion goal from a site by its goal id. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401.</td></tr><tr><td>Delete Site</td><td><code>deleteSite</code></td><td>Permanently deletes a site and all of its recorded statistics. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401.</td></tr><tr><td>Get Aggregate Stats</td><td><code>getAggregateStats</code></td><td>Returns aggregate totals for the site configured on the connection over a reporting period, using the Stats API v1 aggregate endpoint.</td></tr><tr><td>Get Realtime Visitors</td><td><code>getRealtimeVisitors</code></td><td>Returns the number of visitors currently on the site configured on the connection, counted over the last five minutes. The endpoint responds with a bare integer rather than a JSON object.</td></tr><tr><td>Get Site</td><td><code>getSite</code></td><td>Retrieves a single site by its domain, including its reporting timezone, tracker script configuration and custom properties.</td></tr><tr><td>Get Stats Breakdown</td><td><code>getStatsBreakdown</code></td><td>Breaks the site's statistics down by a single property such as source, page, country or device, using the Stats API v1 breakdown endpoint.</td></tr><tr><td>Get Timeseries Stats</td><td><code>getTimeseriesStats</code></td><td>Returns a time series of metrics for the site configured on the connection, one data point per day or month, using the Stats API v1 timeseries endpoint.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Sites</td><td><code>listSites</code></td><td>Lists every site the API key has access to, with cursor-based paging.</td></tr><tr><td>Run Aggregate Stats Query</td><td><code>runAggregateQuery</code></td><td>Runs an aggregate Stats API v2 query against the site configured on the connection, returning a single row of totals for the requested metrics over a relative date range.</td></tr><tr><td>Run Breakdown Stats Query</td><td><code>runBreakdownQuery</code></td><td>Runs a Stats API v2 query broken down by one or more dimensions against the site configured on the connection, returning one paginated row per dimension combination ordered by the first metric descending.</td></tr><tr><td>Run Custom Date Range Stats Query</td><td><code>runCustomDateRangeQuery</code></td><td>Runs an aggregate Stats API v2 query over an absolute start and end date against the site configured on the connection. Use this instead of the relative date ranges offered by the other v2 query actions.</td></tr><tr><td>Run Timeseries Stats Query</td><td><code>runTimeseriesQuery</code></td><td>Runs a Stats API v2 query bucketed over time against the site configured on the connection, returning one row per hour, day, week or month in the requested date range.</td></tr><tr><td>Update Site</td><td><code>updateSite</code></td><td>Changes the domain of an existing site, which also changes its site id. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401.</td></tr></tbody></table>

</details>
