---
description: "The ECB Data Portal API is the European Central Bank's free SDMX 2.1 RESTful web service for euro-area statistics: exchange rates, interest rates, inflation,…"
hidden: true
---

# ECB Data Portal

<img src="../../.gitbook/assets/connectors/ecb-data-portal.png" alt="ECB Data Portal logo" width="64">

The ECB Data Portal API is the European Central Bank's free SDMX 2.1 RESTful web service for euro-area statistics: exchange rates, interest rates, inflation, money, banking, payments and more. Get time series data as SDMX-JSON or CSV, and discover dataflows, data structures, codelists, concept schemes, constraints, categories and schemas. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [data.ecb.europa.eu](https://data.ecb.europa.eu) |
| **Authentication** | No authentication |
| **Slug** | `ecbDataPortal` |

## Use it

Add ECB Data Portal from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ecbDataPortal.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Agency Schemes | `getAgencySchemes` | Get SDMX agency schemes (the maintaining agencies) by agency, id and version; use all/latest as wildcards (GET /service/agencyscheme/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |
| Get All Structure Artefacts | `getAllStructures` | Get SDMX all structure artefacts of any type by agency, id and version; use all/latest as wildcards (GET /service/structure/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |
| Get Categorisations | `getCategorisations` | Get SDMX categorisations (links between dataflows and categories) by agency, id and version; use all/latest as wildcards (GET /service/categorisation/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |
| Get Category Schemes | `getCategorySchemes` | Get SDMX category schemes (the topic tree used to browse dataflows) by agency, id and version; use all/latest as wildcards (GET /service/categoryscheme/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |
| Get Codelists | `getCodelists` | Get SDMX codelists (allowed codes, e.g. CL_FREQ frequencies, CL_CURRENCY currencies) by agency, id and version; use all/latest as wildcards (GET /service/codelist/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |
| Get Concept Schemes | `getConceptSchemes` | Get SDMX concept schemes (the concepts used by dimensions and attributes) by agency, id and version; use all/latest as wildcards (GET /service/conceptscheme/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |
| Get Content Constraints | `getContentConstraints` | Get SDMX content constraints (which code combinations actually have data) by agency, id and version; use all/latest as wildcards (GET /service/contentconstraint/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |
| Get Data Schema | `getSchema` | Get the XML schema (XSD) that describes structure-specific data for a dataflow, data structure or provision agreement (GET /service/schema/{context}/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/schemas |
| Get Data Structure Definitions | `getDataStructures` | Get SDMX data structure definitions (dimensions and attributes of a dataflow) by agency, id and version; use all/latest as wildcards (GET /service/datastructure/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |
| Get Dataflows | `listDataflows` | Get SDMX dataflows (statistical domains such as EXR exchange rates) by agency, id and version; use all/latest as wildcards (GET /service/dataflow/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |

<details>

<summary>See 3 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Organisation Schemes | `getOrganisationSchemes` | Get SDMX organisation schemes by agency, id and version; use all/latest as wildcards (GET /service/organisationscheme/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |
| Get Statistical Data | `getData` | Get time series data for a dataflow and series key (dimension codes joined by '.', blank to wildcard, '+' for OR), with date range, updates since a time, detail level, first/last N observations, history and format (GET /service/data/{flowRef}/{key}). Docs: https://data.ecb.europa.eu/help/api/data |
| Get Structure Sets | `getStructureSets` | Get SDMX structure sets (mappings between structures) by agency, id and version; use all/latest as wildcards (GET /service/structureset/{agencyID}/{resourceID}/{version}). Docs: https://data.ecb.europa.eu/help/api/metadata |

</details>
