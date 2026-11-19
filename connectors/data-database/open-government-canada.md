---
description: "Connect Open Government Canada to your product with fastn."
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

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Autocomplete Organizations</td><td><code>autocompleteOrganizations</code></td><td>Get organizations whose name matches a partial string. (GET /api/3/action/organization_autocomplete) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Get Action Help</td><td><code>getActionHelp</code></td><td>Get the documentation text of any CKAN API action. (GET /api/3/action/help_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Get Dataset</td><td><code>getDataset</code></td><td>Get one dataset with its resources, tags, organization and metadata by name or id. Unknown ids return 404 'Not found'. (GET /api/3/action/package_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Get one organization; include_datasets=true adds its datasets. (GET /api/3/action/organization_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Get Resource</td><td><code>getResource</code></td><td>Get one resource (file or API) by id: format, download URL and whether the DataStore can query it. (GET /api/3/action/resource_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Get Site Status</td><td><code>getStatus</code></td><td>Get the Canada's Open Government Portal CKAN version, site title, URL and enabled extensions. (GET /api/3/action/status_show) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>List Dataset Activity</td><td><code>listDatasetActivity</code></td><td>Get the change history of one dataset, newest first. (GET /api/3/action/package_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>List Datasets</td><td><code>listDatasets</code></td><td>List the names (slugs) of all public datasets on Canada's Open Government Portal. (GET /api/3/action/package_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>List Licenses</td><td><code>listLicenses</code></td><td>List the licenses datasets can use. (GET /api/3/action/license_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>List Organization Activity</td><td><code>listOrganizationActivity</code></td><td>Get the change history of an organization's datasets. (GET /api/3/action/organization_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Organizations</td><td><code>listOrganizations</code></td><td>List organizations (publishers). Set all_fields=true for details. (GET /api/3/action/organization_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>List Recently Changed Datasets</td><td><code>listRecentlyChangedDatasets</code></td><td>Get the latest dataset changes across Canada's Open Government Portal. (GET /api/3/action/recently_changed_packages_activity_list) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Search Datasets</td><td><code>searchDatasets</code></td><td>Search datasets on Canada's Open Government Portal by keyword and Solr filters, with sorting, paging and facets. (GET /api/3/action/package_search) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Search Resources</td><td><code>searchResources</code></td><td>Search resources by field:term pairs, e.g. name:demand or format:CSV. (GET /api/3/action/resource_search) Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr></tbody></table>

</details>
