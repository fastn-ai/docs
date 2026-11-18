---
description: "The Norwegian Meteorological Institute's free Weather API (api.met.no, the data behind Yr): global location forecasts, Nordic nowcasts, ocean and subseasonal…"
hidden: true
---

# MET Norway Weather API

The Norwegian Meteorological Institute's free Weather API (api.met.no, the data behind Yr): global location forecasts, Nordic nowcasts, ocean and subseasonal forecasts, sunrise/sunset and moon times, MetAlerts weather warnings, air quality forecasts, text forecasts and tidal water. No API key needed (identify with a User-Agent).

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [met.no](https://met.no) |
| **Authentication** | No authentication |
| **Actions** | 29 |
| **Events** | 0 |
| **Slug** | `metNorwayWeather` |

## Use it

Add MET Norway Weather API from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.metNorwayWeather.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Air Quality Forecast | `getAirQualityForecast` | Something goes here. Docs: https://api.met.no/weatherapi/airqualityforecast/0.1/documentation (GET /) |
| Get Air Quality Index Description | `getAqiDescription` | Something goes here. Docs: https://api.met.no/weatherapi/airqualityforecast/0.1/documentation (GET /aqi_description) |
| Get Air Quality Meteorology Description | `getAirQualityMetDescription` | Something goes here. Docs: https://api.met.no/weatherapi/airqualityforecast/0.1/documentation (GET /met_description) |
| Get Air Quality Meteorology Forecast | `getAirQualityMetForecast` | Something goes here. Docs: https://api.met.no/weatherapi/airqualityforecast/0.1/documentation (GET /met) |
| Get All Weather Alerts | `getAllAlerts` | Weather alerts from the Norwegian Meteorological Institute. Docs: https://api.met.no/weatherapi/metalerts/2.0/documentation (GET /all.{format}) |
| Get Archived Weather Alerts | `getArchivedAlerts` | Weather alerts from the Norwegian Meteorological Institute. Docs: https://api.met.no/weatherapi/metalerts/2.0/documentation (GET /archive.{format}) |
| Get Current Weather Alerts | `getCurrentAlerts` | Weather alerts from the Norwegian Meteorological Institute. Docs: https://api.met.no/weatherapi/metalerts/2.0/documentation (GET /current.{format}) |
| Get Location Forecast (Classic XML) | `getLocationForecastClassic` | Weather forecasts for any location on earth. Docs: https://api.met.no/weatherapi/locationforecast/2.0/documentation (GET /classic) |
| Get Location Forecast (Compact) | `getLocationForecastCompact` | Weather forecasts for any location on earth. Docs: https://api.met.no/weatherapi/locationforecast/2.0/documentation (GET /compact) |
| Get Location Forecast (Complete) | `getLocationForecastComplete` | Weather forecasts for any location on earth. Docs: https://api.met.no/weatherapi/locationforecast/2.0/documentation (GET /complete) |
| Get Location Forecast Status | `getLocationForecastStatus` | Weather forecasts for any location on earth. Docs: https://api.met.no/weatherapi/locationforecast/2.0/documentation (GET /status) |
| Get Moonrise and Moonset | `getMoonEvents` | Calculate sun or moon events, as seen from a specific location on Earth. Docs: https://api.met.no/weatherapi/sunrise/3.0/documentation (GET /moon) |
| Get Nowcast | `getNowcast` | Immediate weather forecast for specified locations in the Nordic area. Docs: https://api.met.no/weatherapi/nowcast/2.0/documentation (GET /complete) |
| Get Nowcast (Classic XML) | `getNowcastClassic` | Immediate weather forecast for specified locations in the Nordic area. Docs: https://api.met.no/weatherapi/nowcast/2.0/documentation (GET /classic) |
| Get Nowcast Status | `getNowcastStatus` | Immediate weather forecast for specified locations in the Nordic area. Docs: https://api.met.no/weatherapi/nowcast/2.0/documentation (GET /status) |
| Get Ocean Forecast | `getOceanForecast` | Ocean forecasts for points at sea in Northwestern Europe. Docs: https://api.met.no/weatherapi/oceanforecast/2.0/documentation (GET /complete) |
| Get Ocean Forecast (MOX XML) | `getOceanForecastMox` | Ocean forecasts for points at sea in Northwestern Europe. Docs: https://api.met.no/weatherapi/oceanforecast/2.0/documentation (GET /mox) |
| Get Ocean Forecast Status | `getOceanForecastStatus` | Ocean forecasts for points at sea in Northwestern Europe. Docs: https://api.met.no/weatherapi/oceanforecast/2.0/documentation (GET /status) |
| Get Subseasonal Forecast | `getSubseasonalForecast` | Long term weather forecast for specified locations in the Nordic area. Docs: https://api.met.no/weatherapi/subseasonal/1.0/documentation (GET /complete) |
| Get Subseasonal Forecast Status | `getSubseasonalStatus` | Long term weather forecast for specified locations in the Nordic area. Docs: https://api.met.no/weatherapi/subseasonal/1.0/documentation (GET /status) |
| Get Sunrise and Sunset | `getSunEvents` | Calculate sun or moon events, as seen from a specific location on Earth. Docs: https://api.met.no/weatherapi/sunrise/3.0/documentation (GET /sun) |
| Get Text Forecast | `getTextForecast` | Textual weather forecast for Norwegian land and sea areas. Docs: https://api.met.no/weatherapi/textforecast/3.0/documentation (GET /) |
| Get Tidal Water Forecast | `getTidalWater` | Tidal water information. Docs: https://api.met.no/weatherapi/tidalwater/1.1/documentation (GET /) |
| List Air Quality Area Classes | `listAirQualityAreaClasses` | Something goes here. Docs: https://api.met.no/weatherapi/airqualityforecast/0.1/documentation (GET /areaclasses) |
| List Air Quality Areas | `listAirQualityAreas` | Something goes here. Docs: https://api.met.no/weatherapi/airqualityforecast/0.1/documentation (GET /areas) |
| List Air Quality Model Run Times | `listAirQualityReftimes` | Something goes here. Docs: https://api.met.no/weatherapi/airqualityforecast/0.1/documentation (GET /reftimes) |
| List Air Quality Stations | `listAirQualityStations` | Something goes here. Docs: https://api.met.no/weatherapi/airqualityforecast/0.1/documentation (GET /stations) |
| List Available Text Forecasts | `listTextForecasts` | List available resources as XML, RSS or JSON. Docs: https://api.met.no/weatherapi/textforecast/3.0/documentation (GET /available.{format}) |
| List Tidal Water Forecasts | `listTidalWaterHarbors` | List available resources as XML, RSS or JSON. Docs: https://api.met.no/weatherapi/tidalwater/1.1/documentation (GET /available.{format}) |
