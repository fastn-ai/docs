---
description: "The UK Environment Agency flood monitoring service gives near real-time flood data. List flood warnings and areas, and read stations and measure readings."
hidden: true
---

# Environment Agency Flood Monitoring

<img src="../../.gitbook/assets/connectors/lg/ea-flood-monitoring.png" alt="Environment Agency Flood Monitoring logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [environment.data.gov.uk](https://environment.data.gov.uk) |
| **Authentication** | No sign-in needed |
| **Slug** | `eaFloodMonitoring` |

## Setup

Environment Agency Flood Monitoring needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Environment Agency Flood Monitoring from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Environment Agency Flood Monitoring**.
2. Select **Connect** on the Environment Agency Flood Monitoring card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Environment Agency Flood Monitoring needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Environment Agency Flood Monitoring's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Flood Area</td><td><code>getFloodArea</code></td><td>Get one flood alert or warning area by its code, with county, river or sea and polygon link Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>Get Flood Area Polygon</td><td><code>getFloodAreaPolygon</code></td><td>Get the boundary of a flood area as a GeoJSON feature in WGS84 Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>Get Measure</td><td><code>getMeasure</code></td><td>Get one measure with its unit, period and latest reading Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>Get Station</td><td><code>getStation</code></td><td>Get one monitoring station with its measures, location and scale information Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Flood Areas</td><td><code>listFloodAreas</code></td><td>List flood alert and flood warning areas, optionally within a distance of a point Default limit 500. Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Flood Warnings</td><td><code>listFloodWarnings</code></td><td>List current flood warnings and alerts for England, updated every 15 minutes, filtered by minimum severity, county or distance from a point Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Measure Readings</td><td><code>listMeasureReadings</code></td><td>List readings of one measure: latest, today, a day, a date range or since a time Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Measures</td><td><code>listMeasures</code></td><td>List measures across all stations, filtered by parameter, qualifier or station Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Readings</td><td><code>listReadings</code></td><td>List readings across all measures and stations: latest, today, a day or a date range, filtered by parameter or station Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Station Measures</td><td><code>listStationMeasures</code></td><td>List the measures (level, flow and so on) available from one station Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr></tbody></table>

<details>

<summary>View 2 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Station Readings</td><td><code>listStationReadings</code></td><td>List readings of all measures at one station: latest, today, a day, a date range or since a time Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr><tr><td>List Stations</td><td><code>listStations</code></td><td>List water level, flow, rainfall and other monitoring stations, filtered by parameter, river, catchment, town, type, status, label search or distance Docs: https://environment.data.gov.uk/flood-monitoring/doc/reference</td></tr></tbody></table>

</details>

