---
description: "The Humanitarian Data Exchange (HDX), run by UN OCHA, is a free open platform with over 20,000 humanitarian datasets (population, displacement, food security,…"
hidden: true
---

# Humanitarian Data Exchange (HDX)

<img src="../../.gitbook/assets/connectors/humanitarian-data-exchange.png" alt="Humanitarian Data Exchange (HDX) logo" width="64">

The Humanitarian Data Exchange (HDX), run by UN OCHA, is a free open platform with over 20,000 humanitarian datasets (population, displacement, food security, health, conflict and more) from hundreds of organizations. Search and read datasets, resources, organizations, tags and activity through its public CKAN API. No API key needed for reads.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [data.humdata.org](https://data.humdata.org) |
| **Authentication** | No authentication |
| **Slug** | `humanitarianDataExchange` |

## Use it

Add Humanitarian Data Exchange (HDX) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.humanitarianDataExchange.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Datasets | `autocompleteDatasets` | Get datasets whose name or title matches a partial string. (GET /api/3/action/package_autocomplete) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| Autocomplete Organizations | `autocompleteOrganizations` | Get organizations whose name matches a partial string. (GET /api/3/action/organization_autocomplete) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| Autocomplete Resource Formats | `autocompleteFormats` | Get resource formats matching a partial string, e.g. cs -&gt; csv. (GET /api/3/action/format_autocomplete) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| Get Action Help | `getActionHelp` | Get the documentation text of any CKAN API action. (GET /api/3/action/help_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| Get Dataset | `getDataset` | Get one dataset with its resources, tags, organization and metadata by name or id. Unknown ids return 404 'Not found'. (GET /api/3/action/package_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| Get Organization | `getOrganization` | Get one organization; include_datasets=true adds its datasets. (GET /api/3/action/organization_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| Get Resource | `getResource` | Get one resource (file or API) by id: format, download URL and whether the DataStore can query it. (GET /api/3/action/resource_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| Get Site Status | `getStatus` | Get the the Humanitarian Data Exchange CKAN version, site title, URL and enabled extensions. (GET /api/3/action/status_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| Get Tag | `getTag` | Get one tag; include_datasets=true adds the datasets using it. (GET /api/3/action/tag_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| List Dataset Activity | `listDatasetActivity` | Get the change history of one dataset, newest first. (GET /api/3/action/package_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |

<details>

<summary>See 8 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Datasets | `listDatasets` | List the names (slugs) of all public datasets on the Humanitarian Data Exchange. (GET /api/3/action/package_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| List Datasets with Resources | `listDatasetsWithResources` | List datasets (newest first) with their resources in full. (GET /api/3/action/current_package_list_with_resources) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| List Licenses | `listLicenses` | List the licenses datasets can use. (GET /api/3/action/license_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| List Organizations | `listOrganizations` | List organizations (publishers). Set all_fields=true for details. (GET /api/3/action/organization_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| List Recently Changed Datasets | `listRecentlyChangedDatasets` | Get the latest dataset changes across the Humanitarian Data Exchange. (GET /api/3/action/recently_changed_packages_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| List Tags | `listTags` | List all tags, optionally only those matching a string. (GET /api/3/action/tag_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| Search Datasets | `searchDatasets` | Search datasets on the Humanitarian Data Exchange by keyword and Solr filters, with sorting, paging and facets. (GET /api/3/action/package_search) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |
| Search Resources | `searchResources` | Search resources by field:term pairs, e.g. name:demand or format:CSV. (GET /api/3/action/resource_search) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) HDX guide: https://data.humdata.org/faqs/devs |

</details>
