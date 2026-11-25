---
description: "Open-Meteo is a free weather service. Get weather forecasts, air quality, flood and climate data, and elevation for any location."
hidden: true
---

# Open-Meteo

<img src="../../.gitbook/assets/connectors/lg/open-meteo.png" alt="Open-Meteo logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [open-meteo.com](https://open-meteo.com) |
| **Authentication** | No sign-in needed |
| **Slug** | `openMeteo` |

## Setup

Open-Meteo needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Open-Meteo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openMeteo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Air Quality</td><td><code>getAirQuality</code></td><td>Returns air quality and pollen forecasts (PM10, PM2.5, ozone, NO2, European and US AQI) from CAMS. Docs: https://open-meteo.com/en/docs/air-quality-api</td></tr><tr><td>Get Climate Change Projection</td><td><code>getClimateProjection</code></td><td>Returns daily downscaled CMIP6 climate model projections from 1950 to 2050. Docs: https://open-meteo.com/en/docs/climate-api</td></tr><tr><td>Get DWD ICON Forecast</td><td><code>getDwdIconForecast</code></td><td>Returns forecast data from the DWD ICON model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/dwd-api</td></tr><tr><td>Get ECMWF Forecast</td><td><code>getEcmwfForecast</code></td><td>Returns forecast data from the ECMWF model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/ecmwf-api</td></tr><tr><td>Get Elevation</td><td><code>getElevation</code></td><td>Returns terrain elevation in metres (Copernicus DEM GLO-90) for up to 100 coordinates. Docs: https://open-meteo.com/en/docs/elevation-api</td></tr><tr><td>Get Ensemble Forecast</td><td><code>getEnsembleForecast</code></td><td>Returns every member of ensemble weather models (e.g. icon_seamless, gfs_seamless, ecmwf_ifs025) to estimate forecast uncertainty, up to 35 days. Docs: https://open-meteo.com/en/docs/ensemble-api</td></tr><tr><td>Get Flood Forecast</td><td><code>getFloodForecast</code></td><td>Returns daily river discharge forecasts and history from GloFAS, optionally with all ensemble members. Docs: https://open-meteo.com/en/docs/flood-api</td></tr><tr><td>Get GEM Forecast</td><td><code>getGemForecast</code></td><td>Returns forecast data from the GEM model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/gem-api</td></tr><tr><td>Get GFS and HRRR Forecast</td><td><code>getGfsForecast</code></td><td>Returns forecast data from the GFS and HRRR model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/gfs-api</td></tr><tr><td>Get Historical Forecast</td><td><code>getHistoricalForecast</code></td><td>Returns archived high-resolution forecasts (from 2022 onwards) for a date range, built from the first hours of each model run. Docs: https://open-meteo.com/en/docs/historical-forecast-api</td></tr></tbody></table>

<details>

<summary>View 12 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Historical Weather</td><td><code>getHistoricalWeather</code></td><td>Returns historical weather (reanalysis) data from 1940 to a few days ago for a date range and coordinates. Docs: https://open-meteo.com/en/docs/historical-weather-api</td></tr><tr><td>Get JMA Forecast</td><td><code>getJmaForecast</code></td><td>Returns forecast data from the JMA model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/jma-api</td></tr><tr><td>Get Location</td><td><code>getLocation</code></td><td>Returns one geocoding location by its id (as returned by Search Locations). Docs: https://open-meteo.com/en/docs/geocoding-api</td></tr><tr><td>Get Marine Forecast</td><td><code>getMarineForecast</code></td><td>Returns marine weather (wave height, swell, wave period, sea surface temperature, ocean currents) for coordinates at sea. Docs: https://open-meteo.com/en/docs/marine-weather-api</td></tr><tr><td>Get MET Norway Forecast</td><td><code>getMetNoForecast</code></td><td>Returns forecast data from the MET Norway model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/metno-api</td></tr><tr><td>Get Meteo-France Forecast</td><td><code>getMeteoFranceForecast</code></td><td>Returns forecast data from the Meteo-France model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/meteofrance-api</td></tr><tr><td>Get Previous Model Runs</td><td><code>getPreviousModelRuns</code></td><td>Returns forecasts from previous model runs (variables with suffix _previous_day1 to _previous_day7) to compare forecast accuracy by lead time. Docs: https://open-meteo.com/en/docs/previous-runs-api</td></tr><tr><td>Get Satellite Radiation</td><td><code>getSatelliteRadiation</code></td><td>Returns solar radiation from geostationary satellites (shortwave, direct, diffuse, tilted irradiance) at native or hourly resolution. Docs: https://open-meteo.com/en/docs/satellite-radiation-api</td></tr><tr><td>Get Seasonal Forecast</td><td><code>getSeasonalForecast</code></td><td>Returns long-range seasonal forecasts (ECMWF EC46/SEAS5, up to 7 months) as 6-hourly, daily or monthly values. Docs: https://open-meteo.com/en/docs/seasonal-forecast-api</td></tr><tr><td>Get Single Model Run Forecast</td><td><code>getSingleRunForecast</code></td><td>Returns the forecast of one specific model run (run time in UTC). Docs: https://open-meteo.com/en/docs/single-runs-api</td></tr><tr><td>Get Weather Forecast</td><td><code>getForecast</code></td><td>Returns hourly, daily, 15-minutely and current weather forecast data for one or more coordinates, combining the best national weather models (up to 16 days). Docs: https://open-meteo.com/en/docs</td></tr><tr><td>Search Locations</td><td><code>searchLocations</code></td><td>Searches places by name or postal code and returns coordinates, time zone, country, population and admin areas (geocoding). Docs: https://open-meteo.com/en/docs/geocoding-api</td></tr></tbody></table>

</details>

## Events

Open-Meteo has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
