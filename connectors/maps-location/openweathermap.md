---
description: "OpenWeatherMap provides current weather, 5-day/3-hour forecasts, city search, air pollution data (current, forecast and history), direct/reverse/ZIP…"
hidden: true
---

# OpenWeatherMap

OpenWeatherMap provides current weather, 5-day/3-hour forecasts, city search, air pollution data (current, forecast and history), direct/reverse/ZIP geocoding, personal weather-station management with measurement upload, and weather map tiles. All requests authenticate with an API key passed as the appid query parameter.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [openweathermap.org](https://openweathermap.org) |
| **Authentication** | Credentials you enter |
| **Actions** | 23 |
| **Events** | 0 |
| **Slug** | `openweathermap` |

## Use it

Add OpenWeatherMap from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openweathermap.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Weather Station | `deleteWeatherStation` | Permanently deletes a registered personal weather station and all of the measurements uploaded for it. |
| Geocode Location by Name | `geocodeByName` | Converts a place name into one or more sets of geographic coordinates using the OpenWeatherMap geocoding API. |
| Geocode Location by ZIP Code | `geocodeByZipCode` | Converts a postal code and country into geographic coordinates using the OpenWeatherMap geocoding API. |
| Get 5-Day Forecast by City ID | `getForecastByCityId` | Retrieves the five-day weather forecast in three-hour steps for a city identified by its OpenWeatherMap city id. |
| Get 5-Day Forecast by City Name | `getForecastByCityName` | Retrieves the five-day weather forecast in three-hour steps for a city identified by name. |
| Get 5-Day Forecast by Coordinates | `getForecastByCoordinates` | Retrieves the five-day weather forecast in three-hour steps for an exact geographic point. |
| Get 5-Day Forecast by ZIP Code | `getForecastByZipCode` | Retrieves the five-day weather forecast in three-hour steps for a postal code in a given country. |
| Get Air Pollution Forecast | `getAirPollutionForecast` | Retrieves the hourly air quality forecast for the next four days for a geographic point. |
| Get Air Pollution History | `getAirPollutionHistory` | Retrieves historical hourly air quality data for a geographic point over a given time range. History is available from 27 November 2020 onwards. |
| Get Current Air Pollution | `getCurrentAirPollution` | Retrieves the current air quality index and pollutant concentrations for a geographic point. |
| Get Current Weather by City ID | `getCurrentWeatherByCityId` | Retrieves the current weather observation for a city identified by its OpenWeatherMap city id. |
| Get Current Weather by City Name | `getCurrentWeatherByCityName` | Retrieves the current weather observation for a city identified by name, optionally narrowed by state and country code. |
| Get Current Weather by Coordinates | `getCurrentWeatherByCoordinates` | Retrieves the current weather observation for an exact geographic point given by latitude and longitude. |
| Get Current Weather by ZIP Code | `getCurrentWeatherByZipCode` | Retrieves the current weather observation for a postal code in a given country. |
| Get Weather Map Tile | `getWeatherMapTile` | Retrieves a 256x256 PNG weather map tile for a given layer at the requested zoom level and tile coordinates, for overlaying on a slippy map. |
| Get Weather Station | `getWeatherStation` | Retrieves a single registered personal weather station by its OpenWeatherMap station id. |
| List Station Measurements | `listStationMeasurements` | Retrieves aggregated measurements uploaded for a personal weather station over a time range, grouped into minute, hour or day buckets. |
| List Weather Stations | `listWeatherStations` | Lists every personal weather station registered under the connected OpenWeatherMap account. |
| Register Weather Station | `registerWeatherStation` | Registers a new personal weather station on the connected OpenWeatherMap account so that measurements can be uploaded for it. |
| Reverse Geocode Coordinates | `reverseGeocode` | Converts a latitude and longitude pair into the names of the places at that point using the OpenWeatherMap geocoding API. |
| Search Cities by Weather | `searchCities` | Searches for cities matching a name or surrounding a coordinate and returns the current weather observation for each match. |
| Update Weather Station | `updateWeatherStation` | Updates the name, coordinates or altitude of a registered personal weather station. |
| Upload Station Measurements | `uploadStationMeasurements` | Uploads one or more measurements for a registered personal weather station. The endpoint returns HTTP 204 with an empty body on success. |
