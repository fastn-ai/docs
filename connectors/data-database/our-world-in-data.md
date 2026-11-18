---
description: "Our World in Data publishes free research and data on global problems - health, population, energy, CO2, economy, poverty and more - as thousands of charts."
hidden: true
---

# Our World in Data

Our World in Data publishes free research and data on global problems - health, population, energy, CO2, economy, poverty and more - as thousands of charts. Search charts, articles and topics, then get any chart's data as CSV (all or filtered by country and years), its metadata, README, Grapher config, latest values and search card. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [ourworldindata.org](https://ourworldindata.org) |
| **Authentication** | No authentication |
| **Actions** | 7 |
| **Events** | 0 |
| **Slug** | `ourWorldInData` |

## Use it

Add Our World in Data from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ourWorldInData.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Chart Config | `getChartConfig` | Get the raw Grapher configuration of a chart: chart type, dimensions/variable ids, selected entities, map settings (GET /grapher/{slug}.config.json). Docs: https://docs.owid.io/projects/etl/api/chart-api/ |
| Get Chart Data (CSV) | `getChartDataCsv` | Get the data behind an OWID chart as CSV: Entity, Code (ISO alpha-3 or OWID code), Year or Day, then one column per series (GET /grapher/{slug}.csv). csvType=filtered with country/time returns only the selected entities and period; full (default) returns everything. Docs: https://docs.owid.io/projects/etl/api/chart-api/ |
| Get Chart Metadata | `getChartMetadata` | Get chart metadata: title, subtitle, citation, original chart URL, and per-column units, time span, descriptions, sources and how to cite (GET /grapher/{slug}.metadata.json). Docs: https://docs.owid.io/projects/etl/api/chart-api/ |
| Get Chart README | `getChartReadme` | Get the README (markdown) of a chart's data package describing the CSV structure, sources and citation (GET /grapher/{slug}.readme.md). Docs: https://docs.owid.io/projects/etl/api/chart-api/ |
| Get Chart Search Result | `getChartSearchResult` | Get the search-result card of a chart: title, subtitle, data table rows and value displays for chosen entities (GET /grapher/{slug}.search-result.json). Docs: https://docs.owid.io/projects/etl/api/chart-api/ |
| Get Chart Values | `getChartValues` | Get the latest/selected data values of a chart for an entity, with formatted values and times (GET /grapher/{slug}.values.json). Docs: https://docs.owid.io/projects/etl/api/chart-api/ |
| Search | `search` | Search Our World in Data charts (with country/topic filters), pages (articles) or topic pages (GET https://ourworldindata.org/api/search). Docs: https://docs.owid.io/projects/etl/api/search-api/ |
