---
description: "OSRM (Open Source Routing Machine) computes routes on OpenStreetMap data: fastest routes, nearest road snapping, distance/duration tables, GPS map matching,…"
hidden: true
---

# OSRM

<img src="../../.gitbook/assets/connectors/osrm.png" alt="OSRM logo" width="64">

OSRM (Open Source Routing Machine) computes routes on OpenStreetMap data: fastest routes, nearest road snapping, distance/duration tables, GPS map matching, travelling-salesman trips and vector tiles. Point it at your own OSRM server, or at the public demo server router.project-osrm.org for light, non-commercial testing (no API key; best effort, ODbL attribution required).

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [project-osrm.org](https://project-osrm.org) |
| **Authentication** | Credentials you enter |
| **Slug** | `osrm` |

## Use it

Add OSRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.osrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Distance Table | `getTable` | Compute travel durations and/or distances between all pairs of coordinates (GET /table/v1/{profile}/{coordinates}). Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md |
| Get Nearest Road | `getNearest` | Snap one or more coordinates to the street network and return the nearest matches (GET /nearest/v1/{profile}/{coordinates}). Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md |
| Get Route | `getRoute` | Find the fastest route through the coordinates in order, with optional alternatives, steps and geometry (GET /route/v1/{profile}/{coordinates}). Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md |
| Get Vector Tile | `getVectorTile` | Get a Mapbox Vector Tile (protobuf) with the routing graph's road geometries and speeds for a slippy-map tile (GET /tile/v1/{profile}/tile({x},{y},{zoom}).mvt). Zoom must be 12 or higher. Returned as a file. Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md |
| Match GPS Trace | `matchTrace` | Map-match a GPS trace to the road network (GET /match/v1/{profile}/{coordinates}). Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md |
| Solve Trip | `solveTrip` | Solve a travelling-salesman trip that visits all coordinates, as a round trip or between a fixed start and end (GET /trip/v1/{profile}/{coordinates}). Docs: https://project-osrm.org/docs/v5.24.0/api/ and https://github.com/Project-OSRM/osrm-backend/blob/master/docs/http.md |
