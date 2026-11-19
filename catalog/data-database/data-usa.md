---
description: "Data USA publishes US public data on population, economy, education and health. List data cubes and their members, and query data."
hidden: true
---

# Data USA

<img src="../../.gitbook/assets/connectors/lg/data-usa.png" alt="Data USA logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [datausa.io](https://datausa.io) |
| **Authentication** | No sign-in needed |
| **Slug** | `dataUsa` |

## Setup

Data USA needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Data USA from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dataUsa.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Cube</td><td><code>getCube</code></td><td>Get the full schema of one cube: its measures, dimensions, hierarchies and levels Docs: https://datausa.io/about/api/</td></tr><tr><td>List Cubes</td><td><code>listCubes</code></td><td>List every Data USA cube (dataset) with its dimensions, measures and source annotations Docs: https://datausa.io/about/api/</td></tr><tr><td>List Level Members</td><td><code>listMembers</code></td><td>List all members (distinct values with keys) of a level in a cube, useful for include/exclude filters Docs: https://datausa.io/about/api/</td></tr><tr><td>Query Data</td><td><code>queryData</code></td><td>Query a cube for data: choose drilldowns (columns) and measures (aggregated values), filter members with include/exclude, filter measure values, rank, sort, take top-K, select latest/oldest time and paginate. JSON formats return annotations, page, columns and data; csv/tsv return text. Docs: https://datausa.io/about/api/</td></tr></tbody></table>

## Events

Data USA has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
