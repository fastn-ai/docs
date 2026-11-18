---
description: "The UK Environment Agency real-time flood-monitoring API gives near real time flood warnings and alerts for England, flood areas with boundaries, and water…"
hidden: true
---

# Environment Agency Flood Monitoring

<img src="../../.gitbook/assets/connectors/lg/ea-flood-monitoring.png" alt="Environment Agency Flood Monitoring logo">

The UK Environment Agency real-time flood-monitoring API gives near real time flood warnings and alerts for England, flood areas with boundaries, and water level, flow, rainfall and tidal readings from thousands of monitoring stations. No API key needed (Open Government Licence).

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [environment.data.gov.uk](https://environment.data.gov.uk) |
| **Authentication** | No authentication |
| **Slug** | `eaFloodMonitoring` |

## Use it

Add Environment Agency Flood Monitoring from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.eaFloodMonitoring.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Flood Area</td><td><code>getFloodArea</code></td><td>Get one flood alert or warning area by its code, with county, river or sea and polygon link (GET /id/floodAreas/{code}). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>Get Flood Area Polygon</td><td><code>getFloodAreaPolygon</code></td><td>Get the boundary of a flood area as a GeoJSON feature in WGS84 (GET /id/floodAreas/{code}/polygon). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>Get Measure</td><td><code>getMeasure</code></td><td>Get one measure with its unit, period and latest reading (GET /id/measures/{id}). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>Get Station</td><td><code>getStation</code></td><td>Get one monitoring station with its measures, location and scale information (GET /id/stations/{id}). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Flood Areas</td><td><code>listFloodAreas</code></td><td>List flood alert and flood warning areas, optionally within a distance of a point (GET /id/floodAreas). Default limit 500. Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Flood Warnings</td><td><code>listFloodWarnings</code></td><td>List current flood warnings and alerts for England, updated every 15 minutes, filtered by minimum severity, county or distance from a point (GET /id/floods). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Measure Readings</td><td><code>listMeasureReadings</code></td><td>List readings of one measure: latest, today, a day, a date range or since a time (GET /id/measures/{id}/readings). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Measures</td><td><code>listMeasures</code></td><td>List measures across all stations, filtered by parameter, qualifier or station (GET /id/measures). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Readings</td><td><code>listReadings</code></td><td>List readings across all measures and stations: latest, today, a day or a date range, filtered by parameter or station (GET /data/readings). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Station Measures</td><td><code>listStationMeasures</code></td><td>List the measures (level, flow and so on) available from one station (GET /id/stations/{id}/measures). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Station Readings</td><td><code>listStationReadings</code></td><td>List readings of all measures at one station: latest, today, a day, a date range or since a time (GET /id/stations/{id}/readings). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Stations</td><td><code>listStations</code></td><td>List water level, flow, rainfall and other monitoring stations, filtered by parameter, river, catchment, town, type, status, label search or distance (GET /id/stations). Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr></tbody></table>

</details>
