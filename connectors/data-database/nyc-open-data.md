---
description: "NYC Open Data publishes thousands of free datasets from New York City agencies (311 requests, taxi trips, restaurant inspections, crime, housing and more) on…"
hidden: true
---

# NYC Open Data

NYC Open Data publishes thousands of free datasets from New York City agencies (311 requests, taxi trips, restaurant inspections, crime, housing and more) on the Socrata platform. Query any dataset with SoQL filters and aggregates as JSON or CSV, read dataset metadata and columns, and search the catalog by text, category and tag. No API key needed (anonymous requests are throttled).

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [opendata.cityofnewyork.us](https://opendata.cityofnewyork.us) |
| **Authentication** | No authentication |
| **Actions** | 8 |
| **Events** | 0 |
| **Slug** | `nycOpenData` |

## Use it

Add NYC Open Data from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nycOpenData.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Dataset Titles | `autocompleteDatasets` | Suggest dataset titles that match partial text (GET /api/catalog/v1/autocomplete). Docs: https://dev.socrata.com/docs/other/discovery |
| Get Dataset Columns and View Info | `getDatasetSchema` | Get the full view definition of a dataset including every column (field name, data type, description) and row/update info (GET /api/views/{id}.json). Docs: https://dev.socrata.com/docs/endpoints.html and https://opendata.cityofnewyork.us/ |
| Get Dataset Metadata | `getDatasetMetadata` | Get a dataset's metadata: name, description, category, tags, license, update dates and custom fields (GET /api/views/metadata/v1/{id}). Docs: https://dev.socrata.com/docs/endpoints.html and https://opendata.cityofnewyork.us/ |
| List Catalog Categories | `listCategories` | List NYC Open Data categories with asset counts (GET /api/catalog/v1/domain_categories). Docs: https://dev.socrata.com/docs/other/discovery |
| List Catalog Tags | `listTags` | List NYC Open Data tags with asset counts (GET /api/catalog/v1/domain_tags). Docs: https://dev.socrata.com/docs/other/discovery |
| Query Dataset | `queryDataset` | Query rows of any NYC Open Data dataset with SoQL: select columns, filter, sort, group, aggregate, full-text search and page (GET /resource/{id}.json). Rows come back as JSON objects keyed by column field name. Docs: https://dev.socrata.com/docs/endpoints.html and https://opendata.cityofnewyork.us/ |
| Query Dataset (CSV) | `queryDatasetCsv` | Same SoQL query as Query Dataset but returns CSV text (GET /resource/{id}.csv). Docs: https://dev.socrata.com/docs/endpoints.html and https://opendata.cityofnewyork.us/ |
| Search Datasets | `searchDatasets` | Search the NYC Open Data catalog (Socrata Discovery API) by text, category, tag, type and agency, with paging (GET /api/catalog/v1?domains=data.cityofnewyork.us). Docs: https://dev.socrata.com/docs/other/discovery |
