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

| Action | Slug | What it does |
| --- | --- | --- |
| Get AIRMETs | `getAirmets` | AIRMETs. Decoded domestic AIRMETs (Alaska only). See /api/data/gairmet for similar advisories over the contiguous United States. Docs: https://aviationweather.gov/data/api/ (GET /api/data/airmet) |
| Get Airports | `getAirports` | Airport info. Information about airports. Docs: https://aviationweather.gov/data/api/ (GET /api/data/airport) |
| Get Area Forecast | `getAreaForecast` | US Area Forecasts. Text Area Forecasts for the United States outside the contiguous states (Alaska). Docs: https://aviationweather.gov/data/api/ (GET /api/data/areafcst) |
| Get Center Weather Advisories | `getCwas` | CWSU Center Advisories. Center Weather Advisories issued by NWS Center Weather Service Units (CWSUs). Docs: https://aviationweather.gov/data/api/ (GET /api/data/cwa) |
| Get Features | `getFeatures` | Feature info. Additional geographic features. Docs: https://aviationweather.gov/data/api/ (GET /api/data/feature) |
| Get Fixes | `getFixes` | Navigational fix/waypoint info. Navigational fix data. Docs: https://aviationweather.gov/data/api/ (GET /api/data/fix) |
| Get Forecast Discussion | `getForecastDiscussion` | US Forecast Discussions. Aviation Forecast Discussions issued by NWS Weather Forecast Offices. Returns aviation section or full discussion issued within the past six hours. Docs: https://aviationweather.gov/data/api/ (GET /api/data/fcstdisc) |
| Get G-AIRMETs | `getGAirmets` | US Graphical AIRMETs. Decoded G-AIRMETs for the contiguous United States. See /api/data/airmet for similar advisories over Alaska. Docs: https://aviationweather.gov/data/api/ (GET /api/data/gairmet) |
| Get METARs | `getMetars` | METARs. Decoded aviation weather observations. Station identifiers or a bounding box is required. Docs: https://aviationweather.gov/data/api/ (GET /api/data/metar) |
| Get Obstacles | `getObstacles` | Obstacle info. Aviation obstacle information. Docs: https://aviationweather.gov/data/api/ (GET /api/data/obstacle) |

<details>

<summary>See 6 more actions</summary>

* **Get PIREPs** `getPireps`: Pilot Reports. Pilot reports issued in PIREP or AIREP format. Bounding box, or center point identifier and radial distance, required. Docs: https://aviationweather.gov/data/api/ (GET /api/data/pirep)
* **Get SIGMETs** `getSigmets`: SIGMETs. Decoded SIGMETs. This includes SIGMETs issued by the United States in domestic format (i.e. convective and non-convective domestic) and international SIGMETs. Docs: https://aviationweather.gov/data/api/ (GET /api/data/sigmet)
* **Get Station Info** `getStationInfo`: Station info. Station observation location information. Docs: https://aviationweather.gov/data/api/ (GET /api/data/stationinfo)
* **Get TAFs** `getTafs`: TAFs. Decoded Terminal Aerodrome Forecast products. Station identifiers or a bounding box is required. Docs: https://aviationweather.gov/data/api/ (GET /api/data/taf)
* **Get Winds and Temperatures Aloft** `getWindsTemps`: Wind/Temp Point Data. Wind and temperature information from the legacy FD winds. Docs: https://aviationweather.gov/data/api/ (GET /api/data/windtemp)
* **Query Data Server** `queryDataServer`: Data Server. Compatibility layer with previous Text Data Service. Station identifiers or a bounding box, as well as a time selection, are required. Docs: https://aviationweather.gov/data/api/ (GET /api/data/dataserver)

</details>
