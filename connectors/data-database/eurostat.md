---
description: "Eurostat is the statistical office of the European Union."
hidden: true
---

# Eurostat

Eurostat is the statistical office of the European Union. Its free dissemination API gives EU statistics on economy, population, labour, prices, trade, energy, environment and more: get dataset data as JSON-stat, query SDMX series keys as JSON-stat, CSV or XML, read dataflows, data structures, codelists, concept schemes and content constraints, and list every dataset in the table of contents. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [ec.europa.eu](https://ec.europa.eu) |
| **Authentication** | No authentication |
| **Actions** | 8 |
| **Events** | 0 |
| **Slug** | `eurostat` |

## Use it

Add Eurostat from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.eurostat.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Codelist | `getCodelist` | Get the SDMX codelist (codes and labels, e.g. GEO countries, UNIT units) by id (GET /sdmx/2.1/codelist/ESTAT/{id}/latest). Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines |
| Get Concept Scheme | `getConceptScheme` | Get the SDMX concept scheme of a dataset by id (GET /sdmx/2.1/conceptscheme/ESTAT/{id}/latest). Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines |
| Get Content Constraint | `getContentConstraint` | Get the SDMX content constraint (which codes actually have data in a dataset) by id (GET /sdmx/2.1/contentconstraint/ESTAT/{id}/latest). Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines |
| Get Data by Series Key (SDMX) | `getDataBySeriesKey` | Get data with an SDMX series key - dimension codes in the dataset's order joined by '.', blank to wildcard, '+' for OR - with period range, first/last N observations and output format (GET /sdmx/2.1/data/{flow}/{key}). Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines |
| Get Data Structure Definition | `getDataStructure` | Get the SDMX data structure definition (dimensions, attributes and their order) by id (GET /sdmx/2.1/datastructure/ESTAT/{id}/latest). Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines |
| Get Dataflow | `getDataflow` | Get the SDMX dataflow (dataset definition and name) by id (GET /sdmx/2.1/dataflow/ESTAT/{id}/latest). Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines |
| Get Dataset Data (JSON-stat) | `getDatasetData` | Get data from a Eurostat dataset as JSON-stat, filtered by the common dimensions geo, unit, freq and time (GET /statistics/1.0/data/{datasetCode}). For other dimensions use Get Data by Series Key. Filter at least geo or time - whole datasets can be very large. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines |
| Get Table of Contents | `getTableOfContents` | Get the full Eurostat table of contents as tab-separated text: every dataset and table with its code, type, last update, data start/end and values count (GET /catalogue/toc/txt, about 2 MB). Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines |
