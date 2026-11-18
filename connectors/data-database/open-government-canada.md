---
description: "Open Government Canada (open.canada.ca) is the Government of Canada's free open data portal with tens of thousands of federal datasets from Statistics Canada,…"
hidden: true
---

# Open Government Canada

<img src="../../.gitbook/assets/connectors/lg/open-government-canada.png" alt="Open Government Canada logo">

Open Government Canada (open.canada.ca) is the Government of Canada's free open data portal with tens of thousands of federal datasets from Statistics Canada, Environment Canada and other departments. Search and read datasets, resources, organizations, licenses and change activity through its public CKAN API. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [open.canada.ca](https://open.canada.ca) |
| **Authentication** | No authentication |
| **Slug** | `openGovernmentCanada` |

## Use it

Add Open Government Canada from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openGovernmentCanada.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Organizations | `autocompleteOrganizations` | Get organizations whose name matches a partial string. (GET /api/3/action/organization_autocomplete) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| Get Action Help | `getActionHelp` | Get the documentation text of any CKAN API action. (GET /api/3/action/help_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| Get Dataset | `getDataset` | Get one dataset with its resources, tags, organization and metadata by name or id. Unknown ids return 404 'Not found'. (GET /api/3/action/package_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| Get Organization | `getOrganization` | Get one organization; include_datasets=true adds its datasets. (GET /api/3/action/organization_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| Get Resource | `getResource` | Get one resource (file or API) by id: format, download URL and whether the DataStore can query it. (GET /api/3/action/resource_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| Get Site Status | `getStatus` | Get the Canada's Open Government Portal CKAN version, site title, URL and enabled extensions. (GET /api/3/action/status_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| List Dataset Activity | `listDatasetActivity` | Get the change history of one dataset, newest first. (GET /api/3/action/package_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| List Datasets | `listDatasets` | List the names (slugs) of all public datasets on Canada's Open Government Portal. (GET /api/3/action/package_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| List Licenses | `listLicenses` | List the licenses datasets can use. (GET /api/3/action/license_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| List Organization Activity | `listOrganizationActivity` | Get the change history of an organization's datasets. (GET /api/3/action/organization_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| List Organizations | `listOrganizations` | List organizations (publishers). Set all_fields=true for details. (GET /api/3/action/organization_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| List Recently Changed Datasets | `listRecentlyChangedDatasets` | Get the latest dataset changes across Canada's Open Government Portal. (GET /api/3/action/recently_changed_packages_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| Search Datasets | `searchDatasets` | Search datasets on Canada's Open Government Portal by keyword and Solr filters, with sorting, paging and facets. (GET /api/3/action/package_search) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
| Search Resources | `searchResources` | Search resources by field:term pairs, e.g. name:demand or format:CSV. (GET /api/3/action/resource_search) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api |
