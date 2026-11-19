---
description: "Connect Statistics Sweden (SCB) to your product with fastn."
hidden: true
---

# Statistics Sweden (SCB)

<img src="../../.gitbook/assets/connectors/lg/statistics-sweden-scb.png" alt="Statistics Sweden (SCB) logo">

Statistics Sweden (SCB) publishes Sweden's official statistics through the free PxWebApi 2.0 (Statistikdatabasen): search statistical tables on population, economy, labour, prices, environment and more, read table metadata and default selections, get data as JSON-stat, CSV or PX for any selection, read codelists, and create and reuse saved queries. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [scb.se](https://scb.se) |
| **Authentication** | No authentication |
| **Slug** | `statisticsSwedenScb` |

## Use it

Add Statistics Sweden (SCB) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.statisticsSwedenScb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Saved Query</td><td><code>createSavedQuery</code></td><td>Create Saved Query. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (POST /savedqueries)</td></tr><tr><td>Get API Configuration</td><td><code>getApiConfig</code></td><td>Get API Configuration. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (GET /config)</td></tr><tr><td>Get Codelist</td><td><code>getCodelist</code></td><td>Get Codelist. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (GET /codelists/{id})</td></tr><tr><td>Get Saved Query</td><td><code>getSavedQuery</code></td><td>Get Saved Query. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (GET /savedqueries/{id})</td></tr><tr><td>Get Saved Query Data</td><td><code>getSavedQueryData</code></td><td>Get Saved Query Data. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (GET /savedqueries/{id}/data)</td></tr><tr><td>Get Saved Query Selection</td><td><code>getSavedQuerySelection</code></td><td>Get Saved Query Selection. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (GET /savedqueries/{id}/selection)</td></tr><tr><td>Get Table</td><td><code>getTable</code></td><td>Get Table. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (GET /tables/{id})</td></tr><tr><td>Get Table Data (Default Selection)</td><td><code>getTableDataDefault</code></td><td>Get Table Data (Default Selection). Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (GET /tables/{id}/data)</td></tr><tr><td>Get Table Default Selection</td><td><code>getTableDefaultSelection</code></td><td>Get Table Default Selection. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (GET /tables/{id}/defaultselection)</td></tr><tr><td>Get Table Metadata</td><td><code>getTableMetadata</code></td><td>Get Table Metadata. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (GET /tables/{id}/metadata)</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Query Table Data</td><td><code>queryTableData</code></td><td>Get data from a table for an explicit selection of variables and values (POST /tables/{id}/data). Returns JSON-stat 2.0 by default. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Search Tables</td><td><code>searchTables</code></td><td>Search Tables. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/ (GET /tables)</td></tr></tbody></table>

</details>
