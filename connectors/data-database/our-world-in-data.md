---
description: "Our World in Data publishes research and data on global problems. Search charts and read their data, values and metadata."
hidden: true
---

# Our World in Data

<img src="../../.gitbook/assets/connectors/lg/our-world-in-data.png" alt="Our World in Data logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [ourworldindata.org](https://ourworldindata.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `ourWorldInData` |

## Setup

Our World in Data needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Our World in Data from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ourWorldInData.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Chart Config</td><td><code>getChartConfig</code></td><td>Get the raw Grapher configuration of a chart: chart type, dimensions/variable ids, selected entities, map settings Docs: https://docs.owid.io/projects/etl/api/chart-api/</td></tr><tr><td>Get Chart Data (CSV)</td><td><code>getChartDataCsv</code></td><td>Get the data behind an OWID chart as CSV: Entity, Code (ISO alpha-3 or OWID code), Year or Day, then one column per series csvType=filtered with country/time returns only the selected entities and period; full (default) returns everything. Docs: https://docs.owid.io/projects/etl/api/chart-api/</td></tr><tr><td>Get Chart Metadata</td><td><code>getChartMetadata</code></td><td>Get chart metadata: title, subtitle, citation, original chart URL, and per-column units, time span, descriptions, sources and how to cite Docs: https://docs.owid.io/projects/etl/api/chart-api/</td></tr><tr><td>Get Chart README</td><td><code>getChartReadme</code></td><td>Get the README (markdown) of a chart's data package describing the CSV structure, sources and citation Docs: https://docs.owid.io/projects/etl/api/chart-api/</td></tr><tr><td>Get Chart Search Result</td><td><code>getChartSearchResult</code></td><td>Get the search-result card of a chart: title, subtitle, data table rows and value displays for chosen entities Docs: https://docs.owid.io/projects/etl/api/chart-api/</td></tr><tr><td>Get Chart Values</td><td><code>getChartValues</code></td><td>Get the latest/selected data values of a chart for an entity, with formatted values and times Docs: https://docs.owid.io/projects/etl/api/chart-api/</td></tr><tr><td>Search</td><td><code>search</code></td><td>Search Our World in Data charts (with country/topic filters), pages (articles) or topic pages (GET https://ourworldindata.org/api/search). Docs: https://docs.owid.io/projects/etl/api/search-api/</td></tr></tbody></table>

## Events

Our World in Data has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
