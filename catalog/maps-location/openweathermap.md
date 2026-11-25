---
description: "OpenWeatherMap provides weather data. Get current weather, forecasts and air pollution, and geocode places by name or ZIP code."
hidden: true
---

# OpenWeatherMap

<img src="../../.gitbook/assets/connectors/lg/openweathermap.png" alt="OpenWeatherMap logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [openweathermap.org](https://openweathermap.org) |
| **Authentication** | API key |
| **Slug** | `openweathermap` |

## Setup

Your customers enter their API key for OpenWeatherMap when they connect. Nothing else needs setting up.

## Use it

Add OpenWeatherMap from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.openweathermap.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Weather Station</td><td><code>deleteWeatherStation</code></td><td>Permanently deletes a registered personal weather station and all of the measurements uploaded for it.</td></tr><tr><td>Geocode Location by Name</td><td><code>geocodeByName</code></td><td>Converts a place name into one or more sets of geographic coordinates using the OpenWeatherMap geocoding API.</td></tr><tr><td>Geocode Location by ZIP Code</td><td><code>geocodeByZipCode</code></td><td>Converts a postal code and country into geographic coordinates using the OpenWeatherMap geocoding API.</td></tr><tr><td>Get 5-Day Forecast by City ID</td><td><code>getForecastByCityId</code></td><td>Retrieves the five-day weather forecast in three-hour steps for a city identified by its OpenWeatherMap city id.</td></tr><tr><td>Get 5-Day Forecast by City Name</td><td><code>getForecastByCityName</code></td><td>Retrieves the five-day weather forecast in three-hour steps for a city identified by name.</td></tr><tr><td>Get 5-Day Forecast by Coordinates</td><td><code>getForecastByCoordinates</code></td><td>Retrieves the five-day weather forecast in three-hour steps for an exact geographic point.</td></tr><tr><td>Get 5-Day Forecast by ZIP Code</td><td><code>getForecastByZipCode</code></td><td>Retrieves the five-day weather forecast in three-hour steps for a postal code in a given country.</td></tr><tr><td>Get Air Pollution Forecast</td><td><code>getAirPollutionForecast</code></td><td>Retrieves the hourly air quality forecast for the next four days for a geographic point.</td></tr><tr><td>Get Air Pollution History</td><td><code>getAirPollutionHistory</code></td><td>Retrieves historical hourly air quality data for a geographic point over a given time range. History is available from 27 November 2020 onwards.</td></tr><tr><td>Get Current Air Pollution</td><td><code>getCurrentAirPollution</code></td><td>Retrieves the current air quality index and pollutant concentrations for a geographic point.</td></tr></tbody></table>

<details>

<summary>View 13 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Current Weather by City ID</td><td><code>getCurrentWeatherByCityId</code></td><td>Retrieves the current weather observation for a city identified by its OpenWeatherMap city id.</td></tr><tr><td>Get Current Weather by City Name</td><td><code>getCurrentWeatherByCityName</code></td><td>Retrieves the current weather observation for a city identified by name, optionally narrowed by state and country code.</td></tr><tr><td>Get Current Weather by Coordinates</td><td><code>getCurrentWeatherByCoordinates</code></td><td>Retrieves the current weather observation for an exact geographic point given by latitude and longitude.</td></tr><tr><td>Get Current Weather by ZIP Code</td><td><code>getCurrentWeatherByZipCode</code></td><td>Retrieves the current weather observation for a postal code in a given country.</td></tr><tr><td>Get Weather Map Tile</td><td><code>getWeatherMapTile</code></td><td>Retrieves a 256x256 PNG weather map tile for a given layer at the requested zoom level and tile coordinates, for overlaying on a slippy map.</td></tr><tr><td>Get Weather Station</td><td><code>getWeatherStation</code></td><td>Retrieves a single registered personal weather station by its OpenWeatherMap station id.</td></tr><tr><td>List Station Measurements</td><td><code>listStationMeasurements</code></td><td>Retrieves aggregated measurements uploaded for a personal weather station over a time range, grouped into minute, hour or day buckets.</td></tr><tr><td>List Weather Stations</td><td><code>listWeatherStations</code></td><td>Lists every personal weather station registered under the connected OpenWeatherMap account.</td></tr><tr><td>Register Weather Station</td><td><code>registerWeatherStation</code></td><td>Registers a new personal weather station on the connected OpenWeatherMap account so that measurements can be uploaded for it.</td></tr><tr><td>Reverse Geocode Coordinates</td><td><code>reverseGeocode</code></td><td>Converts a latitude and longitude pair into the names of the places at that point using the OpenWeatherMap geocoding API.</td></tr><tr><td>Search Cities by Weather</td><td><code>searchCities</code></td><td>Searches for cities matching a name or surrounding a coordinate and returns the current weather observation for each match.</td></tr><tr><td>Update Weather Station</td><td><code>updateWeatherStation</code></td><td>Updates the name, coordinates or altitude of a registered personal weather station.</td></tr><tr><td>Upload Station Measurements</td><td><code>uploadStationMeasurements</code></td><td>Uploads one or more measurements for a registered personal weather station. The endpoint</td></tr></tbody></table>

</details>

## Events

OpenWeatherMap has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
