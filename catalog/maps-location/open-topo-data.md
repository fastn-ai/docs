---
description: "Open Topo Data is an open elevation service. Get the ground elevation for any set of locations and list the available datasets."
hidden: true
---

# Open Topo Data

<img src="../../.gitbook/assets/connectors/lg/open-topo-data.png" alt="Open Topo Data logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [opentopodata.org](https://opentopodata.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `openTopoData` |

## Setup

Open Topo Data needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Open Topo Data from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Open Topo Data**.
2. Select **Connect** on the Open Topo Data card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Open Topo Data needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Open Topo Data's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Elevation</td><td><code>getElevation</code></td><td>Get the elevation of one or more points (or sampled points along a path) from an open elevation dataset; JSON or GeoJSON Docs: https://www.opentopodata.org/api/</td></tr><tr><td>Get Elevation (POST)</td><td><code>postElevation</code></td><td>Same as Get Elevation but with the arguments in a JSON body, for long point lists that do not fit in a URL Docs: https://www.opentopodata.org/api/</td></tr><tr><td>Get Health</td><td><code>getHealth</code></td><td>Check that the elevation server is healthy; status OK with HTTP 200 when healthy, 500 otherwise. Docs: https://www.opentopodata.org/api/</td></tr><tr><td>List Datasets</td><td><code>listDatasets</code></td><td>List the elevation datasets configured on the server, with any child datasets of multi-datasets Docs: https://www.opentopodata.org/api/</td></tr></tbody></table>

