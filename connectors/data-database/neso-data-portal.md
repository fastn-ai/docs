---
description: "The NESO Data Portal (Great Britain's National Energy System Operator, formerly National Grid ESO) is a free CKAN open data API for GB electricity system…"
hidden: true
---

# NESO Data Portal

<img src="../../.gitbook/assets/connectors/lg/neso-data-portal.png" alt="NESO Data Portal logo">

The NESO Data Portal (Great Britain's National Energy System Operator, formerly National Grid ESO) is a free CKAN open data API for GB electricity system data: demand, generation, balancing, carbon intensity, interconnectors, network charges and more. Search and read datasets, organizations, tags and resources, and query records with DataStore search or SQL. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [neso.energy](https://neso.energy) |
| **Authentication** | No authentication |
| **Slug** | `nesoDataPortal` |

## Use it

Add NESO Data Portal from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nesoDataPortal.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Datasets | `autocompleteDatasets` | Get datasets whose name or title matches a partial string. (GET /api/3/action/package_autocomplete) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Autocomplete Organizations | `autocompleteOrganizations` | Get organizations whose name matches a partial string. (GET /api/3/action/organization_autocomplete) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Autocomplete Resource Formats | `autocompleteFormats` | Get resource formats matching a partial string, e.g. cs -&gt; csv. (GET /api/3/action/format_autocomplete) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Get Action Help | `getActionHelp` | Get the documentation text of any CKAN API action. (GET /api/3/action/help_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Get Dataset | `getDataset` | Get one dataset with its resources, tags, organization and metadata by name or id. Unknown ids return 404 'Not found'. (GET /api/3/action/package_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Get DataStore Info | `getDatastoreInfo` | Get the column names, types and row count of a DataStore resource. (POST /api/3/action/datastore_info) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Get Organization | `getOrganization` | Get one organization; include_datasets=true adds its datasets. (GET /api/3/action/organization_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Get Resource | `getResource` | Get one resource (file or API) by id: format, download URL and whether the DataStore can query it. (GET /api/3/action/resource_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Get Site Status | `getStatus` | Get the the NESO Data Portal CKAN version, site title, URL and enabled extensions. (GET /api/3/action/status_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Get Tag | `getTag` | Get one tag; include_datasets=true adds the datasets using it. (GET /api/3/action/tag_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| List Dataset Activity | `listDatasetActivity` | Get the change history of one dataset, newest first. (GET /api/3/action/package_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| List Datasets | `listDatasets` | List the names (slugs) of all public datasets on the NESO Data Portal. (GET /api/3/action/package_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| List Datasets with Resources | `listDatasetsWithResources` | List datasets (newest first) with their resources in full. (GET /api/3/action/current_package_list_with_resources) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| List Licenses | `listLicenses` | List the licenses datasets can use. (GET /api/3/action/license_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| List Organization Activity | `listOrganizationActivity` | Get the change history of an organization's datasets. (GET /api/3/action/organization_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| List Organizations | `listOrganizations` | List organizations (publishers). Set all_fields=true for details. (GET /api/3/action/organization_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| List Recently Changed Datasets | `listRecentlyChangedDatasets` | Get the latest dataset changes across the NESO Data Portal. (GET /api/3/action/recently_changed_packages_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| List Resource Views | `listResourceViews` | List the preview views (data explorer, charts) of a resource. (GET /api/3/action/resource_view_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| List Tags | `listTags` | List all tags, optionally only those matching a string. (GET /api/3/action/tag_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Query DataStore with SQL | `queryDatastoreSql` | Run a read-only SQL SELECT against DataStore tables (the table name is the resource id in double quotes). Keep a LIMIT in the query. (GET /api/3/action/datastore_search_sql) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Search Datasets | `searchDatasets` | Search datasets on the NESO Data Portal by keyword and Solr filters, with sorting, paging and facets. (GET /api/3/action/package_search) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Search DataStore Records | `searchDatastore` | Read rows from a DataStore-enabled resource with full-text search, filters, field selection, sorting and paging (default 100 rows). (GET /api/3/action/datastore_search) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
| Search Resources | `searchResources` | Search resources by field:term pairs, e.g. name:demand or format:CSV. (GET /api/3/action/resource_search) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) NESO guidance: https://www.neso.energy/data-portal/api-guidance |
