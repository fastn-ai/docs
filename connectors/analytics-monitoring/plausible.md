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

| Action | Slug | What it does |
| --- | --- | --- |
| Create Goal | `createGoal` | Creates a conversion goal on a site, or returns the existing goal when an identical one already exists. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401. |
| Create Shared Link | `createSharedLink` | Creates a shared dashboard link for a site, or returns the existing link when one with the same name already exists. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401. |
| Create Site | `createSite` | Creates a new site in the Plausible account. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401. |
| Delete Goal | `deleteGoal` | Deletes a conversion goal from a site by its goal id. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401. |
| Delete Site | `deleteSite` | Permanently deletes a site and all of its recorded statistics. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401. |
| Get Aggregate Stats | `getAggregateStats` | Returns aggregate totals for the site configured on the connection over a reporting period, using the Stats API v1 aggregate endpoint. |
| Get Realtime Visitors | `getRealtimeVisitors` | Returns the number of visitors currently on the site configured on the connection, counted over the last five minutes. The endpoint responds with a bare integer rather than a JSON object. |
| Get Site | `getSite` | Retrieves a single site by its domain, including its reporting timezone, tracker script configuration and custom properties. |
| Get Stats Breakdown | `getStatsBreakdown` | Breaks the site's statistics down by a single property such as source, page, country or device, using the Stats API v1 breakdown endpoint. |
| Get Timeseries Stats | `getTimeseriesStats` | Returns a time series of metrics for the site configured on the connection, one data point per day or month, using the Stats API v1 timeseries endpoint. |
| List Sites | `listSites` | Lists every site the API key has access to, with cursor-based paging. |
| Run Aggregate Stats Query | `runAggregateQuery` | Runs an aggregate Stats API v2 query against the site configured on the connection, returning a single row of totals for the requested metrics over a relative date range. |
| Run Breakdown Stats Query | `runBreakdownQuery` | Runs a Stats API v2 query broken down by one or more dimensions against the site configured on the connection, returning one paginated row per dimension combination ordered by the first metric descending. |
| Run Custom Date Range Stats Query | `runCustomDateRangeQuery` | Runs an aggregate Stats API v2 query over an absolute start and end date against the site configured on the connection. Use this instead of the relative date ranges offered by the other v2 query actions. |
| Run Timeseries Stats Query | `runTimeseriesQuery` | Runs a Stats API v2 query bucketed over time against the site configured on the connection, returning one row per hour, day, week or month in the requested date range. |
| Update Site | `updateSite` | Changes the domain of an existing site, which also changes its site id. Requires an API key with the sites:provision:* scope; a Stats API key is rejected with HTTP 401. |
