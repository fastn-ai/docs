---
description: "Open-Meteo is a free, keyless weather API: forecasts from national weather models, historical weather back to 1940, marine, air quality, flood, climate,…"
---

# Open-Meteo

Open-Meteo is a free, keyless weather API: forecasts from national weather models, historical weather back to 1940, marine, air quality, flood, climate, ensemble and seasonal data, plus geocoding and elevation. Free for non-commercial use (under 10,000 calls per day); commercial use needs an Open-Meteo API subscription.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [open-meteo.com](https://open-meteo.com) |
| **Authentication** | No authentication |
| **Actions** | 22 |
| **Events** | 0 |
| **Slug** | `openMeteo` |

## Use it

Add Open-Meteo from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openMeteo.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Air Quality | `getAirQuality` | Returns air quality and pollen forecasts (PM10, PM2.5, ozone, NO2, European and US AQI) from CAMS. Docs: https://open-meteo.com/en/docs/air-quality-api |
| Get Climate Change Projection | `getClimateProjection` | Returns daily downscaled CMIP6 climate model projections from 1950 to 2050. Docs: https://open-meteo.com/en/docs/climate-api |
| Get DWD ICON Forecast | `getDwdIconForecast` | Returns forecast data from the DWD ICON model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/dwd-api |
| Get ECMWF Forecast | `getEcmwfForecast` | Returns forecast data from the ECMWF model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/ecmwf-api |
| Get Elevation | `getElevation` | Returns terrain elevation in metres (Copernicus DEM GLO-90) for up to 100 coordinates. Docs: https://open-meteo.com/en/docs/elevation-api |
| Get Ensemble Forecast | `getEnsembleForecast` | Returns every member of ensemble weather models (e.g. icon_seamless, gfs_seamless, ecmwf_ifs025) to estimate forecast uncertainty, up to 35 days. Docs: https://open-meteo.com/en/docs/ensemble-api |
| Get Flood Forecast | `getFloodForecast` | Returns daily river discharge forecasts and history from GloFAS, optionally with all ensemble members. Docs: https://open-meteo.com/en/docs/flood-api |
| Get GEM Forecast | `getGemForecast` | Returns forecast data from the GEM model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/gem-api |
| Get GFS and HRRR Forecast | `getGfsForecast` | Returns forecast data from the GFS and HRRR model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/gfs-api |
| Get Historical Forecast | `getHistoricalForecast` | Returns archived high-resolution forecasts (from 2022 onwards) for a date range, built from the first hours of each model run. Docs: https://open-meteo.com/en/docs/historical-forecast-api |
| Get Historical Weather | `getHistoricalWeather` | Returns historical weather (reanalysis) data from 1940 to a few days ago for a date range and coordinates. Docs: https://open-meteo.com/en/docs/historical-weather-api |
| Get JMA Forecast | `getJmaForecast` | Returns forecast data from the JMA model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/jma-api |
| Get Location | `getLocation` | Returns one geocoding location by its id (as returned by Search Locations). Docs: https://open-meteo.com/en/docs/geocoding-api |
| Get Marine Forecast | `getMarineForecast` | Returns marine weather (wave height, swell, wave period, sea surface temperature, ocean currents) for coordinates at sea. Docs: https://open-meteo.com/en/docs/marine-weather-api |
| Get MET Norway Forecast | `getMetNoForecast` | Returns forecast data from the MET Norway model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/metno-api |
| Get Meteo-France Forecast | `getMeteoFranceForecast` | Returns forecast data from the Meteo-France model family only (same parameters as Get Weather Forecast; models narrows to a specific model of this family). Docs: https://open-meteo.com/en/docs/meteofrance-api |
| Get Previous Model Runs | `getPreviousModelRuns` | Returns forecasts from previous model runs (variables with suffix _previous_day1 to _previous_day7) to compare forecast accuracy by lead time. Docs: https://open-meteo.com/en/docs/previous-runs-api |
| Get Satellite Radiation | `getSatelliteRadiation` | Returns solar radiation from geostationary satellites (shortwave, direct, diffuse, tilted irradiance) at native or hourly resolution. Docs: https://open-meteo.com/en/docs/satellite-radiation-api |
| Get Seasonal Forecast | `getSeasonalForecast` | Returns long-range seasonal forecasts (ECMWF EC46/SEAS5, up to 7 months) as 6-hourly, daily or monthly values. Docs: https://open-meteo.com/en/docs/seasonal-forecast-api |
| Get Single Model Run Forecast | `getSingleRunForecast` | Returns the forecast of one specific model run (run time in UTC). Docs: https://open-meteo.com/en/docs/single-runs-api |
| Get Weather Forecast | `getForecast` | Returns hourly, daily, 15-minutely and current weather forecast data for one or more coordinates, combining the best national weather models (up to 16 days). Docs: https://open-meteo.com/en/docs |
| Search Locations | `searchLocations` | Searches places by name or postal code and returns coordinates, time zone, country, population and admin areas (geocoding). Docs: https://open-meteo.com/en/docs/geocoding-api |
