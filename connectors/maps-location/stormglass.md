---
description: "Stormglass provides global marine and land weather data."
hidden: true
---

# Stormglass

<img src="../../.gitbook/assets/connectors/lg/stormglass.png" alt="Stormglass logo">

This connector covers the Stormglass v2 API: hourly weather forecasts, historical weather since 2014, ocean bio and soil data, tide extremes and hourly sea levels, tide station lists and area searches, sun and moon astronomy data, solar radiation and UV data, and elevation or bathymetry for any coordinate.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [stormglass.io](https://stormglass.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `stormglass` |

## Use it

Add Stormglass from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.stormglass.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Astronomy Data</td><td><code>getAstronomyPoint</code></td><td>Retrieves daily astronomy data for a coordinate: sunrise and sunset, moonrise and moonset, moon illumination and phase, and astronomical, nautical and civil dawn and dusk times. Up to 10 days can be requested.</td></tr><tr><td>Get Bio Data</td><td><code>getBioPoint</code></td><td>Retrieves hourly biological and soil data for a single coordinate, such as ocean chlorophyll, nitrate, oxygen, pH and salinity at sea or soil moisture and temperature on land, per data source.</td></tr><tr><td>Get Elevation</td><td><code>getElevationPoint</code></td><td>Retrieves the elevation in meters relative to sea level for a single coordinate: topography on land or bathymetry (negative values) at sea.</td></tr><tr><td>Get Historical Weather</td><td><code>getHistoricalWeatherPoint</code></td><td>Retrieves hourly historical weather data for a single coordinate from 2014 onwards, based on the ECMWF ERA5 reanalysis. Each response covers up to 10 days; at least one of start or end must be supplied. Data for the most recent 7 days may be unavailable.</td></tr><tr><td>Get Solar Data</td><td><code>getSolarPoint</code></td><td>Retrieves hourly solar data for a single coordinate, including UV index and solar downward radiation flux, per data source.</td></tr><tr><td>Get Tide Extremes</td><td><code>getTideExtremesPoint</code></td><td>Retrieves high and low tide times and their relative sea levels in meters for a coordinate, using the nearest tide station. Heights are relative to the chosen datum, Mean Sea Level by default, and never represent actual water depth.</td></tr><tr><td>Get Tide Sea Level</td><td><code>getTideSeaLevelPoint</code></td><td>Retrieves the hourly relative sea level in meters for a coordinate, using the nearest tide station. Values are relative to the chosen datum, Mean Sea Level by default.</td></tr><tr><td>Get Weather Forecast</td><td><code>getWeatherPoint</code></td><td>Retrieves hourly weather forecast data for a single coordinate, including marine parameters such as wave and swell height when the point is at sea. Each requested parameter is returned per data source. Forecast data is available for a 14-day look-back period; use Get Historical Weather for older data.</td></tr><tr><td>List Tide Stations</td><td><code>listTideStations</code></td><td>Lists every tide station available in Stormglass with its name, coordinates and owning source. The full list is large; use List Tide Stations In Area to narrow it to a region.</td></tr><tr><td>List Tide Stations In Area</td><td><code>listTideStationsInArea</code></td><td>Lists the tide stations inside a rectangular geographic area defined by its top-right and bottom-left corners.</td></tr></tbody></table>
