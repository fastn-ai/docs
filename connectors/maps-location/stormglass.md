---
description: "Stormglass provides global marine and land weather data."
hidden: true
---

# Stormglass

<img src="../../.gitbook/assets/connectors/stormglass.png" alt="Stormglass logo" width="64">

Stormglass provides global marine and land weather data. This connector covers the Stormglass v2 API: hourly weather forecasts, historical weather since 2014, ocean bio and soil data, tide extremes and hourly sea levels, tide station lists and area searches, sun and moon astronomy data, solar radiation and UV data, and elevation or bathymetry for any coordinate.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [stormglass.io](https://stormglass.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `stormglass` |

## Use it

Add Stormglass from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.stormglass.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Astronomy Data | `getAstronomyPoint` | Retrieves daily astronomy data for a coordinate: sunrise and sunset, moonrise and moonset, moon illumination and phase, and astronomical, nautical and civil dawn and dusk times. Up to 10 days can be requested. |
| Get Bio Data | `getBioPoint` | Retrieves hourly biological and soil data for a single coordinate, such as ocean chlorophyll, nitrate, oxygen, pH and salinity at sea or soil moisture and temperature on land, per data source. |
| Get Elevation | `getElevationPoint` | Retrieves the elevation in meters relative to sea level for a single coordinate: topography on land or bathymetry (negative values) at sea. |
| Get Historical Weather | `getHistoricalWeatherPoint` | Retrieves hourly historical weather data for a single coordinate from 2014 onwards, based on the ECMWF ERA5 reanalysis. Each response covers up to 10 days; at least one of start or end must be supplied. Data for the most recent 7 days may be unavailable. |
| Get Solar Data | `getSolarPoint` | Retrieves hourly solar data for a single coordinate, including UV index and solar downward radiation flux, per data source. |
| Get Tide Extremes | `getTideExtremesPoint` | Retrieves high and low tide times and their relative sea levels in meters for a coordinate, using the nearest tide station. Heights are relative to the chosen datum, Mean Sea Level by default, and never represent actual water depth. |
| Get Tide Sea Level | `getTideSeaLevelPoint` | Retrieves the hourly relative sea level in meters for a coordinate, using the nearest tide station. Values are relative to the chosen datum, Mean Sea Level by default. |
| Get Weather Forecast | `getWeatherPoint` | Retrieves hourly weather forecast data for a single coordinate, including marine parameters such as wave and swell height when the point is at sea. Each requested parameter is returned per data source. Forecast data is available for a 14-day look-back period; use Get Historical Weather for older data. |
| List Tide Stations | `listTideStations` | Lists every tide station available in Stormglass with its name, coordinates and owning source. The full list is large; use List Tide Stations In Area to narrow it to a region. |
| List Tide Stations In Area | `listTideStationsInArea` | Lists the tide stations inside a rectangular geographic area defined by its top-right and bottom-left corners. |
