---
description: "Eurostat is the statistical office of the European Union. Read EU datasets, tables, dataflows, codelists and data structure definitions."
hidden: true
---

# Eurostat

<img src="../../.gitbook/assets/connectors/lg/eurostat.png" alt="Eurostat logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [ec.europa.eu](https://ec.europa.eu) |
| **Authentication** | No sign-in needed |
| **Slug** | `eurostat` |

## Setup

Eurostat needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Eurostat from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.eurostat.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Codelist</td><td><code>getCodelist</code></td><td>Get the SDMX codelist (codes and labels, e.g. GEO countries, UNIT units) by id Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Concept Scheme</td><td><code>getConceptScheme</code></td><td>Get the SDMX concept scheme of a dataset by id Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Content Constraint</td><td><code>getContentConstraint</code></td><td>Get the SDMX content constraint (which codes actually have data in a dataset) by id Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Data by Series Key (SDMX)</td><td><code>getDataBySeriesKey</code></td><td>Get data with an SDMX series key - dimension codes in the dataset's order joined by '.', blank to wildcard, '+' for OR - with period range, first/last N observations and output format Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Data Structure Definition</td><td><code>getDataStructure</code></td><td>Get the SDMX data structure definition (dimensions, attributes and their order) by id Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Dataflow</td><td><code>getDataflow</code></td><td>Get the SDMX dataflow (dataset definition and name) by id Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Dataset Data (JSON-stat)</td><td><code>getDatasetData</code></td><td>Get data from a Eurostat dataset as JSON-stat, filtered by the common dimensions geo, unit, freq and time For other dimensions use Get Data by Series Key. Filter at least geo or time - whole datasets can be very large. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Table of Contents</td><td><code>getTableOfContents</code></td><td>Get the full Eurostat table of contents as tab-separated text: every dataset and table with its code, type, last update, data start/end and values count, about 2 MB). Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr></tbody></table>

## Events

Eurostat has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
