---
description: "OSRM calculates routes on OpenStreetMap data. Get routes, distance tables and trips, snap points to roads and match GPS traces."
hidden: true
---

# OSRM

<img src="../../.gitbook/assets/connectors/lg/osrm.png" alt="OSRM logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [project-osrm.org](https://project-osrm.org) |
| **Authentication** | Server URL |
| **Slug** | `osrm` |

## Setup

Your customers enter their server url for OSRM when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect OSRM from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **OSRM**.
2. Select **Connect** on the OSRM card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use OSRM's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Distance Table</td><td><code>getTable</code></td><td>Compute travel durations and/or distances between all pairs of coordinates Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md</td></tr><tr><td>Get Nearest Road</td><td><code>getNearest</code></td><td>Snap one or more coordinates to the street network and return the nearest matches Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md</td></tr><tr><td>Get Route</td><td><code>getRoute</code></td><td>Find the fastest route through the coordinates in order, with optional alternatives, steps and geometry Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md</td></tr><tr><td>Get Vector Tile</td><td><code>getVectorTile</code></td><td>Get a Mapbox Vector Tile (protobuf) with the routing graph's road geometries and speeds for a slippy-map tile,{y},{zoom}).mvt). Zoom must be 12 or higher. Returned as a file. Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md</td></tr><tr><td>Match GPS Trace</td><td><code>matchTrace</code></td><td>Map-match a GPS trace to the road network Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md</td></tr><tr><td>Solve Trip</td><td><code>solveTrip</code></td><td>Solve a travelling-salesman trip that visits all coordinates, as a round trip or between a fixed start and end Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md</td></tr></tbody></table>

