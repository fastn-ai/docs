---
description: "Open Topo Data is an open-source elevation API with a free public server (api.opentopodata.org) serving open datasets such as SRTM, ASTER, EU-DEM, NED,…"
hidden: true
---

# Open Topo Data

<img src="../../.gitbook/assets/connectors/open-topo-data.png" alt="Open Topo Data logo" width="64">

Open Topo Data is an open-source elevation API with a free public server (api.opentopodata.org) serving open datasets such as SRTM, ASTER, EU-DEM, NED, ETOPO1, GEBCO bathymetry and Mapzen. Get elevations for points or sampled paths as JSON or GeoJSON. No API key needed; the public server allows 100 points per request, 1 call per second and 1000 calls per day.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [opentopodata.org](https://opentopodata.org) |
| **Authentication** | No authentication |
| **Slug** | `openTopoData` |

## Use it

Add Open Topo Data from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openTopoData.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Elevation | `getElevation` | Get the elevation of one or more points (or sampled points along a path) from an open elevation dataset; JSON or GeoJSON (GET /v1/{dataset}). Docs: https://www.opentopodata.org/api/ |
| Get Elevation (POST) | `postElevation` | Same as Get Elevation but with the arguments in a JSON body, for long point lists that do not fit in a URL (POST /v1/{dataset}). Docs: https://www.opentopodata.org/api/ |
| Get Health | `getHealth` | Check that the elevation server is healthy (GET /health); status OK with HTTP 200 when healthy, 500 otherwise. Docs: https://www.opentopodata.org/api/ |
| List Datasets | `listDatasets` | List the elevation datasets configured on the server, with any child datasets of multi-datasets (GET /datasets). Docs: https://www.opentopodata.org/api/ |
