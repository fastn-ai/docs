---
description: "Statistics Finland (Tilastokeskus) publishes Finland's official statistics through its free PxWeb API: browse and search the StatFin and other databases, read…"
hidden: true
---

# Statistics Finland (StatFin)

<img src="../../.gitbook/assets/connectors/statistics-finland.png" alt="Statistics Finland (StatFin) logo" width="64">

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

| Action | Slug | What it does |
| --- | --- | --- |
| Get API Configuration | `getApiConfig` | Get the API limits: max values and cells per query, max calls per time window (GET /PxWeb/api/v1/{lang}/?config). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html) |
| Get Table Metadata | `getTableMetadata` | Get a table's title and variables with their codes, value codes and labels - needed to build a query (GET /PxWeb/api/v1/{lang}/{database}/{folder}/{table}). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html) |
| List Database Contents | `listDatabaseContents` | List the top-level folders (subjects) of a database (GET /PxWeb/api/v1/{lang}/{database}). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html) |
| List Databases | `listDatabases` | List the PxWeb databases of Statistics Finland, e.g. StatFin (GET /PxWeb/api/v1/{lang}/). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html) |
| List Folder Contents | `listFolderContents` | List the tables (and sub-folders) in a subject folder (GET /PxWeb/api/v1/{lang}/{database}/{folder}). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html) |
| Query Table Data | `queryTable` | Get data from a table for a selection of variables (POST /PxWeb/api/v1/{lang}/{database}/{folder}/{table}). Each query item is {code, selection:{filter, values}} with filter item, all ('*' wildcards), top (latest N) or agg:/vs: groupings. Returns JSON-stat 2.0 by default. Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html) |
| Search Tables | `searchTables` | Search the tables of a database by free text, best match first (GET /PxWeb/api/v1/{lang}/{database}?query=). Docs: https://stat.fi/en/services/statistical-data-services/open-data (PxWeb API v1 user guide: https://pxdata.stat.fi/api1.html) |
