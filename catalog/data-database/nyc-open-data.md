---
description: "NYC Open Data publishes free datasets from New York City agencies. Search the catalog, read dataset details and query dataset rows."
hidden: true
---

# NYC Open Data

<img src="../../.gitbook/assets/connectors/lg/nyc-open-data.png" alt="NYC Open Data logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [opendata.cityofnewyork.us](https://opendata.cityofnewyork.us) |
| **Authentication** | No sign-in needed |
| **Slug** | `nycOpenData` |

## Setup

NYC Open Data needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add NYC Open Data from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nycOpenData.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Autocomplete Dataset Titles</td><td><code>autocompleteDatasets</code></td><td>Suggest dataset titles that match partial text Docs: https://dev.socrata.com/docs/other/discovery</td></tr><tr><td>Get Dataset Columns and View Info</td><td><code>getDatasetSchema</code></td><td>Get the full view definition of a dataset including every column (field name, data type, description) and row/update info Docs: https://dev.socrata.com/docs/endpoints.html and https://opendata.cityofnewyork.us/</td></tr><tr><td>Get Dataset Metadata</td><td><code>getDatasetMetadata</code></td><td>Get a dataset's metadata: name, description, category, tags, license, update dates and custom fields Docs: https://dev.socrata.com/docs/endpoints.html and https://opendata.cityofnewyork.us/</td></tr><tr><td>List Catalog Categories</td><td><code>listCategories</code></td><td>List NYC Open Data categories with asset counts Docs: https://dev.socrata.com/docs/other/discovery</td></tr><tr><td>List Catalog Tags</td><td><code>listTags</code></td><td>List NYC Open Data tags with asset counts Docs: https://dev.socrata.com/docs/other/discovery</td></tr><tr><td>Query Dataset</td><td><code>queryDataset</code></td><td>Query rows of any NYC Open Data dataset with SoQL: select columns, filter, sort, group, aggregate, full-text search and page Rows come back as JSON objects keyed by column field name. Docs: https://dev.socrata.com/docs/endpoints.html and https://opendata.cityofnewyork.us/</td></tr><tr><td>Query Dataset (CSV)</td><td><code>queryDatasetCsv</code></td><td>Same SoQL query as Query Dataset but returns CSV text Docs: https://dev.socrata.com/docs/endpoints.html and https://opendata.cityofnewyork.us/</td></tr><tr><td>Search Datasets</td><td><code>searchDatasets</code></td><td>Search the NYC Open Data catalog (Socrata Discovery API) by text, category, tag, type and agency, with paging Docs: https://dev.socrata.com/docs/other/discovery</td></tr></tbody></table>

## Events

NYC Open Data has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
