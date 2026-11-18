---
description: "Data USA (by Datawheel and Deloitte) publishes US public data - census, economy, education, health and more - through its Tesseract API."
---

# Data USA

Data USA (by Datawheel and Deloitte) publishes US public data - census, economy, education, health and more - through its Tesseract API. List and inspect data cubes, list level members, and query any cube with drilldowns, measures, member and measure filters, ranking, sorting, top-K and time selection. Free with no API key.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [datausa.io](https://datausa.io) |
| **Authentication** | No authentication |
| **Actions** | 4 |
| **Events** | 0 |
| **Slug** | `dataUsa` |

## Use it

Add Data USA from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dataUsa.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Cube | `getCube` | Get the full schema of one cube: its measures, dimensions, hierarchies and levels (GET /cubes/{name}). Docs: https://datausa.io/about/api/ |
| List Cubes | `listCubes` | List every Data USA cube (dataset) with its dimensions, measures and source annotations (GET /cubes). Docs: https://datausa.io/about/api/ |
| List Level Members | `listMembers` | List all members (distinct values with keys) of a level in a cube, useful for include/exclude filters (GET /members). Docs: https://datausa.io/about/api/ |
| Query Data | `queryData` | Query a cube for data (GET /data.{format}): choose drilldowns (columns) and measures (aggregated values), filter members with include/exclude, filter measure values, rank, sort, take top-K, select latest/oldest time and paginate. JSON formats return annotations, page, columns and data; csv/tsv return text. Docs: https://datausa.io/about/api/ |
