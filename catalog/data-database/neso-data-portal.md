---
description: "The NESO Data Portal publishes Great Britain's national energy system data. Search and read datasets, resources and organizations."
hidden: true
---

# NESO Data Portal

<img src="../../.gitbook/assets/connectors/lg/neso-data-portal.png" alt="NESO Data Portal logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [neso.energy](https://neso.energy) |
| **Authentication** | No sign-in needed |
| **Slug** | `nesoDataPortal` |

## Setup

NESO Data Portal needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect NESO Data Portal from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **NESO Data Portal**.
2. Select **Connect** on the NESO Data Portal card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. NESO Data Portal needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use NESO Data Portal's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Autocomplete Datasets</td><td><code>autocompleteDatasets</code></td><td>Get datasets whose name or title matches a partial string. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Autocomplete Organizations</td><td><code>autocompleteOrganizations</code></td><td>Get organizations whose name matches a partial string. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Autocomplete Resource Formats</td><td><code>autocompleteFormats</code></td><td>Get resource formats matching a partial string, e.g. cs -&gt; csv. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Get Action Help</td><td><code>getActionHelp</code></td><td>Get the documentation text of any CKAN API action. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Get Dataset</td><td><code>getDataset</code></td><td>Get one dataset with its resources, tags, organization and metadata by name or id. Unknown ids return 404 'Not found'. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Get DataStore Info</td><td><code>getDatastoreInfo</code></td><td>Get the column names, types and row count of a DataStore resource. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Get one organization; include_datasets=true adds its datasets. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Get Resource</td><td><code>getResource</code></td><td>Get one resource (file or API) by id: format, download URL and whether the DataStore can query it. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Get Site Status</td><td><code>getStatus</code></td><td>Get the the NESO Data Portal CKAN version, site title, URL and enabled extensions. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Get Tag</td><td><code>getTag</code></td><td>Get one tag; include_datasets=true adds the datasets using it. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr></tbody></table>

<details>

<summary>View 13 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Dataset Activity</td><td><code>listDatasetActivity</code></td><td>Get the change history of one dataset, newest first. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>List Datasets</td><td><code>listDatasets</code></td><td>List the names (slugs) of all public datasets on the NESO Data Portal. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>List Datasets with Resources</td><td><code>listDatasetsWithResources</code></td><td>List datasets (newest first) with their resources in full. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>List Licenses</td><td><code>listLicenses</code></td><td>List the licenses datasets can use. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>List Organization Activity</td><td><code>listOrganizationActivity</code></td><td>Get the change history of an organization's datasets. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>List Organizations</td><td><code>listOrganizations</code></td><td>List organizations (publishers). Set all_fields=true for details. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>List Recently Changed Datasets</td><td><code>listRecentlyChangedDatasets</code></td><td>Get the latest dataset changes across the NESO Data Portal. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>List Resource Views</td><td><code>listResourceViews</code></td><td>List the preview views (data explorer, charts) of a resource. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>List Tags</td><td><code>listTags</code></td><td>List all tags, optionally only those matching a string. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Query DataStore with SQL</td><td><code>queryDatastoreSql</code></td><td>Run a read-only SQL SELECT against DataStore tables (the table name is the resource id in double quotes). Keep a LIMIT in the query. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Search Datasets</td><td><code>searchDatasets</code></td><td>Search datasets on the NESO Data Portal by keyword and Solr filters, with sorting, paging and facets. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Search DataStore Records</td><td><code>searchDatastore</code></td><td>Read rows from a DataStore-enabled resource with full-text search, filters, field selection, sorting and paging (default 100 rows). Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr><tr><td>Search Resources</td><td><code>searchResources</code></td><td>Search resources by field:term pairs, e.g. name:demand or format:CSV. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance</td></tr></tbody></table>

</details>

