---
description: "Statistics Sweden publishes Sweden's official statistics. Search tables, read table data and codelists, and work with saved queries."
hidden: true
---

# Statistics Sweden (SCB)

<img src="../../.gitbook/assets/connectors/lg/statistics-sweden-scb.png" alt="Statistics Sweden (SCB) logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [scb.se](https://scb.se) |
| **Authentication** | No sign-in needed |
| **Slug** | `statisticsSwedenScb` |

## Setup

Statistics Sweden (SCB) needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Statistics Sweden (SCB) from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Statistics Sweden (SCB)**.
2. Select **Connect** on the Statistics Sweden (SCB) card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Statistics Sweden (SCB) needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Statistics Sweden (SCB)'s actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Saved Query</td><td><code>createSavedQuery</code></td><td>Create Saved Query. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Get API Configuration</td><td><code>getApiConfig</code></td><td>Get API Configuration. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Get Codelist</td><td><code>getCodelist</code></td><td>Get Codelist. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Get Saved Query</td><td><code>getSavedQuery</code></td><td>Get Saved Query. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Get Saved Query Data</td><td><code>getSavedQueryData</code></td><td>Get Saved Query Data. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Get Saved Query Selection</td><td><code>getSavedQuerySelection</code></td><td>Get Saved Query Selection. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Get Table</td><td><code>getTable</code></td><td>Get Table. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Get Table Data (Default Selection)</td><td><code>getTableDataDefault</code></td><td>Get Table Data (Default Selection). Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Get Table Default Selection</td><td><code>getTableDefaultSelection</code></td><td>Get Table Default Selection. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Get Table Metadata</td><td><code>getTableMetadata</code></td><td>Get Table Metadata. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Query Table Data</td><td><code>queryTableData</code></td><td>Get data from a table for an explicit selection of variables and values Returns JSON-stat 2.0 by default. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr><tr><td>Search Tables</td><td><code>searchTables</code></td><td>Search Tables. Docs: https://www.scb.se/en/services/open-data-api/pxwebapi/</td></tr></tbody></table>

</details>

