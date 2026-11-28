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

## Connect in Fastn

Your customers connect Data USA from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Data USA**.
2. Select **Connect** on the Data USA card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Data USA needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Data USA's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Cube</td><td><code>getCube</code></td><td>Get the full schema of one cube: its measures, dimensions, hierarchies and levels Docs: https://datausa.io/about/api/</td></tr><tr><td>List Cubes</td><td><code>listCubes</code></td><td>List every Data USA cube (dataset) with its dimensions, measures and source annotations Docs: https://datausa.io/about/api/</td></tr><tr><td>List Level Members</td><td><code>listMembers</code></td><td>List all members (distinct values with keys) of a level in a cube, useful for include/exclude filters Docs: https://datausa.io/about/api/</td></tr><tr><td>Query Data</td><td><code>queryData</code></td><td>Query a cube for data: choose drilldowns (columns) and measures (aggregated values), filter members with include/exclude, filter measure values, rank, sort, take top-K, select latest/oldest time and paginate. JSON formats return annotations, page, columns and data; csv/tsv return text. Docs: https://datausa.io/about/api/</td></tr></tbody></table>

