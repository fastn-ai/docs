---
description: "Open Government Canada is the Government of Canada's open data portal. Search and read datasets, resources and organizations."
hidden: true
---

# Open Government Canada

<img src="../../.gitbook/assets/connectors/lg/open-government-canada.png" alt="Open Government Canada logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [open.canada.ca](https://open.canada.ca) |
| **Authentication** | No sign-in needed |
| **Slug** | `openGovernmentCanada` |

## Setup

Open Government Canada needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Open Government Canada from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Open Government Canada**.
2. Select **Connect** on the Open Government Canada card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Open Government Canada needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Open Government Canada's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Autocomplete Organizations</td><td><code>autocompleteOrganizations</code></td><td>Get organizations whose name matches a partial string. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Get Action Help</td><td><code>getActionHelp</code></td><td>Get the documentation text of any CKAN API action. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Get Dataset</td><td><code>getDataset</code></td><td>Get one dataset with its resources, tags, organization and metadata by name or id. Unknown ids return 404 'Not found'. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Get Organization</td><td><code>getOrganization</code></td><td>Get one organization; include_datasets=true adds its datasets. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Get Resource</td><td><code>getResource</code></td><td>Get one resource (file or API) by id: format, download URL and whether the DataStore can query it. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Get Site Status</td><td><code>getStatus</code></td><td>Get the Canada's Open Government Portal CKAN version, site title, URL and enabled extensions. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>List Dataset Activity</td><td><code>listDatasetActivity</code></td><td>Get the change history of one dataset, newest first. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>List Datasets</td><td><code>listDatasets</code></td><td>List the names (slugs) of all public datasets on Canada's Open Government Portal. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>List Licenses</td><td><code>listLicenses</code></td><td>List the licenses datasets can use. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>List Organization Activity</td><td><code>listOrganizationActivity</code></td><td>Get the change history of an organization's datasets. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Organizations</td><td><code>listOrganizations</code></td><td>List organizations (publishers). Set all_fields=true for details. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>List Recently Changed Datasets</td><td><code>listRecentlyChangedDatasets</code></td><td>Get the latest dataset changes across Canada's Open Government Portal. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Search Datasets</td><td><code>searchDatasets</code></td><td>Search datasets on Canada's Open Government Portal by keyword and Solr filters, with sorting, paging and facets. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr><tr><td>Search Resources</td><td><code>searchResources</code></td><td>Search resources by field:term pairs, e.g. name:demand or format:CSV. Docs: https://docs.ckan.org/en/latest/api/ (ckan.logic.action.get) Portal guide: https://open.canada.ca/en/access-our-application-programming-interface-api</td></tr></tbody></table>

</details>

