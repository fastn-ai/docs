---
description: "Statistics Norway (SSB) publishes Norway's official statistics through the free PxWebApi 2.0: search thousands of statistical tables (population, prices,…"
hidden: true
---

# Statistics Norway (SSB)

<img src="../../.gitbook/assets/connectors/lg/statistics-norway-ssb.png" alt="Statistics Norway (SSB) logo">

Statistics Norway (SSB) publishes Norway's official statistics through the free PxWebApi 2.0: search thousands of statistical tables (population, prices, labour, trade, energy, more), read table metadata and default selections, get data as JSON-stat, CSV or PX for any selection of variables, read codelists, and create and reuse saved queries. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [ssb.no](https://ssb.no) |
| **Authentication** | No authentication |
| **Slug** | `statisticsNorwaySsb` |

## Use it

Add Statistics Norway (SSB) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.statisticsNorwaySsb.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Saved Query | `createSavedQuery` | Create Saved Query. Docs: https://www.ssb.no/en/api/pxwebapi (POST /savedqueries) |
| Get API Configuration | `getApiConfig` | Get API Configuration. Docs: https://www.ssb.no/en/api/pxwebapi (GET /config) |
| Get Codelist | `getCodelist` | Get Codelist. Docs: https://www.ssb.no/en/api/pxwebapi (GET /codelists/{id}) |
| Get Saved Query | `getSavedQuery` | Get Saved Query. Docs: https://www.ssb.no/en/api/pxwebapi (GET /savedqueries/{id}) |
| Get Saved Query Data | `getSavedQueryData` | Get Saved Query Data. Docs: https://www.ssb.no/en/api/pxwebapi (GET /savedqueries/{id}/data) |
| Get Saved Query Selection | `getSavedQuerySelection` | Get Saved Query Selection. Docs: https://www.ssb.no/en/api/pxwebapi (GET /savedqueries/{id}/selection) |
| Get Table | `getTable` | Get Table. Docs: https://www.ssb.no/en/api/pxwebapi (GET /tables/{id}) |
| Get Table Data (Default Selection) | `getTableDataDefault` | Get Table Data (Default Selection). Docs: https://www.ssb.no/en/api/pxwebapi (GET /tables/{id}/data) |
| Get Table Default Selection | `getTableDefaultSelection` | Get Table Default Selection. Docs: https://www.ssb.no/en/api/pxwebapi (GET /tables/{id}/defaultselection) |
| Get Table Metadata | `getTableMetadata` | Get Table Metadata. Docs: https://www.ssb.no/en/api/pxwebapi (GET /tables/{id}/metadata) |
| Query Table Data | `queryTableData` | Get data from a table for an explicit selection of variables and values (POST /tables/{id}/data). Returns JSON-stat 2.0 by default. Docs: https://www.ssb.no/en/api/pxwebapi |
| Search Tables | `searchTables` | Search Tables. Docs: https://www.ssb.no/en/api/pxwebapi (GET /tables) |
