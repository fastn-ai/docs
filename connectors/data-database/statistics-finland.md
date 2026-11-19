---
description: "Statistics Finland (Tilastokeskus) publishes Finland's official statistics through its free PxWeb API: browse and search the StatFin and other databases, read…"
hidden: true
---

# Statistics Finland (StatFin)

<img src="../../.gitbook/assets/connectors/lg/statistics-finland.png" alt="Statistics Finland (StatFin) logo">

Statistics Finland (Tilastokeskus) publishes Finland's official statistics through its free PxWeb API: browse and search the StatFin and other databases, read table variables and value codes, and query any table for a selection of areas, years and measures as JSON-stat, CSV or PX. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [stat.fi](https://stat.fi) |
| **Authentication** | No authentication |
| **Slug** | `statisticsFinland` |

## Use it

Add Statistics Finland (StatFin) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.statisticsFinland.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get API Configuration</td><td><code>getApiConfig</code></td><td>Get the API limits: max values and cells per query, max calls per time window (GET /PxWeb/api/v1/{lang}/?config). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>Get Table Metadata</td><td><code>getTableMetadata</code></td><td>Get a table's title and variables with their codes, value codes and labels - needed to build a query (GET /PxWeb/api/v1/{lang}/{database}/{folder}/{table}). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>List Database Contents</td><td><code>listDatabaseContents</code></td><td>List the top-level folders (subjects) of a database (GET /PxWeb/api/v1/{lang}/{database}). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>List Databases</td><td><code>listDatabases</code></td><td>List the PxWeb databases of Statistics Finland, e.g. StatFin (GET /PxWeb/api/v1/{lang}/). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>List Folder Contents</td><td><code>listFolderContents</code></td><td>List the tables (and sub-folders) in a subject folder (GET /PxWeb/api/v1/{lang}/{database}/{folder}). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>Query Table Data</td><td><code>queryTable</code></td><td>Get data from a table for a selection of variables (POST /PxWeb/api/v1/{lang}/{database}/{folder}/{table}). Each query item is {code, selection:{filter, values}} with filter item, all ('*' wildcards), top (latest N) or agg:/vs: groupings. Returns JSON-stat 2.0 by default. Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr><tr><td>Search Tables</td><td><code>searchTables</code></td><td>Search the tables of a database by free text, best match first (GET /PxWeb/api/v1/{lang}/{database}?query=). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html)</td></tr></tbody></table>
