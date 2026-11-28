---
description: "The ECB Data Portal publishes the European Central Bank's euro area statistics. Read datasets, codelists, category schemes and other data structures."
hidden: true
---

# ECB Data Portal

<img src="../../.gitbook/assets/connectors/lg/ecb-data-portal.png" alt="ECB Data Portal logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [data.ecb.europa.eu](https://data.ecb.europa.eu) |
| **Authentication** | No sign-in needed |
| **Slug** | `ecbDataPortal` |

## Setup

ECB Data Portal needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect ECB Data Portal from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **ECB Data Portal**.
2. Select **Connect** on the ECB Data Portal card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. ECB Data Portal needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use ECB Data Portal's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Agency Schemes</td><td><code>getAgencySchemes</code></td><td>Get SDMX agency schemes (the maintaining agencies) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get All Structure Artefacts</td><td><code>getAllStructures</code></td><td>Get SDMX all structure artefacts of any type by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Categorisations</td><td><code>getCategorisations</code></td><td>Get SDMX categorisations (links between dataflows and categories) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Category Schemes</td><td><code>getCategorySchemes</code></td><td>Get SDMX category schemes (the topic tree used to browse dataflows) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Codelists</td><td><code>getCodelists</code></td><td>Get SDMX codelists (allowed codes, e.g. CL_FREQ frequencies, CL_CURRENCY currencies) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Concept Schemes</td><td><code>getConceptSchemes</code></td><td>Get SDMX concept schemes (the concepts used by dimensions and attributes) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Content Constraints</td><td><code>getContentConstraints</code></td><td>Get SDMX content constraints (which code combinations actually have data) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Data Schema</td><td><code>getSchema</code></td><td>Get the XML schema (XSD) that describes structure-specific data for a dataflow, data structure or provision agreement Docs: https://data.ecb.europa.eu/help/api/schemas</td></tr><tr><td>Get Data Structure Definitions</td><td><code>getDataStructures</code></td><td>Get SDMX data structure definitions (dimensions and attributes of a dataflow) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Dataflows</td><td><code>listDataflows</code></td><td>Get SDMX dataflows (statistical domains such as EXR exchange rates) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Organisation Schemes</td><td><code>getOrganisationSchemes</code></td><td>Get SDMX organisation schemes by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Statistical Data</td><td><code>getData</code></td><td>Get time series data for a dataflow and series key (dimension codes joined by '.', blank to wildcard, '+' for OR), with date range, updates since a time, detail level, first/last N observations, history and format Docs: https://data.ecb.europa.eu/help/api/data</td></tr><tr><td>Get Structure Sets</td><td><code>getStructureSets</code></td><td>Get SDMX structure sets (mappings between structures) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr></tbody></table>

</details>

