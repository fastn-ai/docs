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

## Use it

Add ECB Data Portal from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ecbDataPortal.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Agency Schemes</td><td><code>getAgencySchemes</code></td><td>Get SDMX agency schemes (the maintaining agencies) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get All Structure Artefacts</td><td><code>getAllStructures</code></td><td>Get SDMX all structure artefacts of any type by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Categorisations</td><td><code>getCategorisations</code></td><td>Get SDMX categorisations (links between dataflows and categories) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Category Schemes</td><td><code>getCategorySchemes</code></td><td>Get SDMX category schemes (the topic tree used to browse dataflows) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Codelists</td><td><code>getCodelists</code></td><td>Get SDMX codelists (allowed codes, e.g. CL_FREQ frequencies, CL_CURRENCY currencies) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Concept Schemes</td><td><code>getConceptSchemes</code></td><td>Get SDMX concept schemes (the concepts used by dimensions and attributes) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Content Constraints</td><td><code>getContentConstraints</code></td><td>Get SDMX content constraints (which code combinations actually have data) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Data Schema</td><td><code>getSchema</code></td><td>Get the XML schema (XSD) that describes structure-specific data for a dataflow, data structure or provision agreement Docs: https://data.ecb.europa.eu/help/api/schemas</td></tr><tr><td>Get Data Structure Definitions</td><td><code>getDataStructures</code></td><td>Get SDMX data structure definitions (dimensions and attributes of a dataflow) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Dataflows</td><td><code>listDataflows</code></td><td>Get SDMX dataflows (statistical domains such as EXR exchange rates) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr></tbody></table>

<details>

<summary>View 3 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Organisation Schemes</td><td><code>getOrganisationSchemes</code></td><td>Get SDMX organisation schemes by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr><tr><td>Get Statistical Data</td><td><code>getData</code></td><td>Get time series data for a dataflow and series key (dimension codes joined by '.', blank to wildcard, '+' for OR), with date range, updates since a time, detail level, first/last N observations, history and format Docs: https://data.ecb.europa.eu/help/api/data</td></tr><tr><td>Get Structure Sets</td><td><code>getStructureSets</code></td><td>Get SDMX structure sets (mappings between structures) by agency, id and version; use all/latest as wildcards Docs: https://data.ecb.europa.eu/help/api/metadata</td></tr></tbody></table>

</details>

## Events

ECB Data Portal has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
