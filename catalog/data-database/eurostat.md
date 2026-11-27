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

## Connect in Fastn

Your customers connect Eurostat from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Eurostat**.
2. Select **Connect** on the Eurostat card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Eurostat needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Eurostat's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Codelist</td><td><code>getCodelist</code></td><td>Get the SDMX codelist (codes and labels, e.g. GEO countries, UNIT units) by id Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Concept Scheme</td><td><code>getConceptScheme</code></td><td>Get the SDMX concept scheme of a dataset by id Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Content Constraint</td><td><code>getContentConstraint</code></td><td>Get the SDMX content constraint (which codes actually have data in a dataset) by id Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Data by Series Key (SDMX)</td><td><code>getDataBySeriesKey</code></td><td>Get data with an SDMX series key - dimension codes in the dataset's order joined by '.', blank to wildcard, '+' for OR - with period range, first/last N observations and output format Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Data Structure Definition</td><td><code>getDataStructure</code></td><td>Get the SDMX data structure definition (dimensions, attributes and their order) by id Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Dataflow</td><td><code>getDataflow</code></td><td>Get the SDMX dataflow (dataset definition and name) by id Returns SDMX-ML XML. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Dataset Data (JSON-stat)</td><td><code>getDatasetData</code></td><td>Get data from a Eurostat dataset as JSON-stat, filtered by the common dimensions geo, unit, freq and time For other dimensions use Get Data by Series Key. Filter at least geo or time - whole datasets can be very large. Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr><tr><td>Get Table of Contents</td><td><code>getTableOfContents</code></td><td>Get the full Eurostat table of contents as tab-separated text: every dataset and table with its code, type, last update, data start/end and values count, about 2 MB). Docs: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines</td></tr></tbody></table>

