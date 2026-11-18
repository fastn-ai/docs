---
description: "The NOAA/NWS Aviation Weather Center Data API gives free aviation weather: METAR observations, TAF forecasts, PIREPs, SIGMETs, AIRMETs and G-AIRMETs,…"
hidden: true
---

# Aviation Weather Center (aviationweather.gov)

<img src="../../.gitbook/assets/connectors/lg/aviation-weather-center.png" alt="Aviation Weather Center (aviationweather.gov) logo">

The NOAA/NWS Aviation Weather Center Data API gives free aviation weather: METAR observations, TAF forecasts, PIREPs, SIGMETs, AIRMETs and G-AIRMETs, convective forecasts, center weather advisories, winds and temperatures aloft, area forecasts, forecast discussions, plus station, airport, navaid, fix, feature and obstacle data. No API key needed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [aviationweather.gov](https://aviationweather.gov) |
| **Authentication** | No authentication |
| **Slug** | `aviationWeatherCenter` |

## Use it

Add Aviation Weather Center (aviationweather.gov) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.aviationWeatherCenter.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get AIRMETs</td><td><code>getAirmets</code></td><td>AIRMETs. Decoded domestic AIRMETs (Alaska only). See /api/data/gairmet for similar advisories over the contiguous United States. Docs: https://aviationweather.gov/data/api/ (GET /api/data/airmet)</td></tr><tr><td>Get Airports</td><td><code>getAirports</code></td><td>Airport info. Information about airports. Docs: https://aviationweather.gov/data/api/ (GET /api/data/airport)</td></tr><tr><td>Get Area Forecast</td><td><code>getAreaForecast</code></td><td>US Area Forecasts. Text Area Forecasts for the United States outside the contiguous states (Alaska). Docs: https://aviationweather.gov/data/api/ (GET /api/data/areafcst)</td></tr><tr><td>Get Center Weather Advisories</td><td><code>getCwas</code></td><td>CWSU Center Advisories. Center Weather Advisories issued by NWS Center Weather Service Units (CWSUs). Docs: https://aviationweather.gov/data/api/ (GET /api/data/cwa)</td></tr><tr><td>Get Features</td><td><code>getFeatures</code></td><td>Feature info. Additional geographic features. Docs: https://aviationweather.gov/data/api/ (GET /api/data/feature)</td></tr><tr><td>Get Fixes</td><td><code>getFixes</code></td><td>Navigational fix/waypoint info. Navigational fix data. Docs: https://aviationweather.gov/data/api/ (GET /api/data/fix)</td></tr><tr><td>Get Forecast Discussion</td><td><code>getForecastDiscussion</code></td><td>US Forecast Discussions. Aviation Forecast Discussions issued by NWS Weather Forecast Offices. Returns aviation section or full discussion issued within the past six hours. Docs: https://aviationweather.gov/data/api/ (GET /api/data/fcstdisc)</td></tr><tr><td>Get G-AIRMETs</td><td><code>getGAirmets</code></td><td>US Graphical AIRMETs. Decoded G-AIRMETs for the contiguous United States. See /api/data/airmet for similar advisories over Alaska. Docs: https://aviationweather.gov/data/api/ (GET /api/data/gairmet)</td></tr><tr><td>Get METARs</td><td><code>getMetars</code></td><td>METARs. Decoded aviation weather observations. Station identifiers or a bounding box is required. Docs: https://aviationweather.gov/data/api/ (GET /api/data/metar)</td></tr><tr><td>Get Obstacles</td><td><code>getObstacles</code></td><td>Obstacle info. Aviation obstacle information. Docs: https://aviationweather.gov/data/api/ (GET /api/data/obstacle)</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get PIREPs</td><td><code>getPireps</code></td><td>Pilot Reports. Pilot reports issued in PIREP or AIREP format. Bounding box, or center point identifier and radial distance, required. Docs: https://aviationweather.gov/data/api/ (GET /api/data/pirep)</td></tr><tr><td>Get SIGMETs</td><td><code>getSigmets</code></td><td>SIGMETs. Decoded SIGMETs. This includes SIGMETs issued by the United States in domestic format (i.e. convective and non-convective domestic) and international SIGMETs. Docs: https://aviationweather.gov/data/api/ (GET /api/data/sigmet)</td></tr><tr><td>Get Station Info</td><td><code>getStationInfo</code></td><td>Station info. Station observation location information. Docs: https://aviationweather.gov/data/api/ (GET /api/data/stationinfo)</td></tr><tr><td>Get TAFs</td><td><code>getTafs</code></td><td>TAFs. Decoded Terminal Aerodrome Forecast products. Station identifiers or a bounding box is required. Docs: https://aviationweather.gov/data/api/ (GET /api/data/taf)</td></tr><tr><td>Get Winds and Temperatures Aloft</td><td><code>getWindsTemps</code></td><td>Wind/Temp Point Data. Wind and temperature information from the legacy FD winds. Docs: https://aviationweather.gov/data/api/ (GET /api/data/windtemp)</td></tr><tr><td>Query Data Server</td><td><code>queryDataServer</code></td><td>Data Server. Compatibility layer with previous Text Data Service. Station identifiers or a bounding box, as well as a time selection, are required. Docs: https://aviationweather.gov/data/api/ (GET /api/data/dataserver)</td></tr></tbody></table>

</details>
