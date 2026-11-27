---
description: "Statistics Finland publishes Finland's official statistics. Browse and search tables, read their metadata and query table data."
hidden: true
---

# Statistics Finland (StatFin)

<img src="../../.gitbook/assets/connectors/lg/statistics-finland.png" alt="Statistics Finland (StatFin) logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [stat.fi](https://stat.fi) |
| **Authentication** | No sign-in needed |
| **Slug** | `statisticsFinland` |

## Setup

Statistics Finland (StatFin) needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Statistics Finland (StatFin) from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Statistics Finland (StatFin)**.
2. Select **Connect** on the Statistics Finland (StatFin) card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Statistics Finland (StatFin) needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Statistics Finland (StatFin)'s actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Configuration</td><td><code>getApiConfig</code></td><td>Get the API limits: max values and cells per query, max calls per time window Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>Get Table Metadata</td><td><code>getTableMetadata</code></td><td>Get a table's title and variables with their codes, value codes and labels - needed to build a query Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>List Database Contents</td><td><code>listDatabaseContents</code></td><td>List the top-level folders (subjects) of a database Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>List Databases</td><td><code>listDatabases</code></td><td>List the PxWeb databases of Statistics Finland, e.g. StatFin Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>List Folder Contents</td><td><code>listFolderContents</code></td><td>List the tables (and sub-folders) in a subject folder Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>Query Table Data</td><td><code>queryTable</code></td><td>Get data from a table for a selection of variables Each query item is {code, selection:{filter, values}} with filter item, all ('*' wildcards), top (latest N) or agg:/vs: groupings. Returns JSON-stat 2.0 by default. Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>Search Tables</td><td><code>searchTables</code></td><td>Search the tables of a database by free text, best match first Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr></tbody></table>

