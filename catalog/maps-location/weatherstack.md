---
description: "Weatherstack provides weather data. Get current, forecast, historical and marine weather, and search locations."
hidden: true
---

# Weatherstack

<img src="../../.gitbook/assets/connectors/lg/weatherstack.png" alt="Weatherstack logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [weatherstack.com](https://weatherstack.com) |
| **Authentication** | Access key |
| **Slug** | `weatherstack` |

## Setup

Your customers enter their access key for Weatherstack when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Weatherstack from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Weatherstack**.
2. Select **Connect** on the Weatherstack card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Weatherstack's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Current Weather</td><td><code>getCurrentWeather</code></td><td>Returns real-time weather data for one or more locations, including temperature, conditions, wind, pressure, humidity, air quality, and astronomy (sunrise/sunset/moon phase) data embedded in the current block.</td></tr><tr><td>Get Historical Marine Weather</td><td><code>getHistoricalMarineWeather</code></td><td>Returns historical marine (sailing) weather data for a given latitude/longitude coordinate pair over a past date range (max 35 days). Confirmed live: real 403 error (code 105 function_access_restricted) since Marine API Data is a paid-plan-only feature per Weatherstack's pricing page.</td></tr><tr><td>Get Historical Weather</td><td><code>getHistoricalWeather</code></td><td>Returns historical weather data for one or more locations on a single past date, a semicolon-separated list of dates, or a date range, optionally split hourly. Confirmed live on this account: historical queries are blocked with a real 400 error (code 603 historical_queries_not_supported_on_plan) despite Weatherstack's pricing page listing Full Historical Data as a free-plan feature - correctly wired, gated by account entitlement, not a defect.</td></tr><tr><td>Get Marine Weather Forecast</td><td><code>getMarineWeatherForecast</code></td><td>Returns marine (sailing) weather forecast data - including tides, swell, and water temperature - for a given latitude/longitude coordinate pair. Confirmed live: real 403 error (code 105 function_access_restricted) since Marine API Data is a paid-plan-only feature per Weatherstack's pricing page.</td></tr><tr><td>Get Weather Forecast</td><td><code>getWeatherForecast</code></td><td>Returns a day-by-day (and optionally hour-by-hour) weather forecast for one or more locations, including astronomy data per forecast day. Confirmed live: this account's free-plan forecast is limited to a single day and does not honor the forecast_days parameter - passing it returns a real 609 forecast_days_not_supported_on_plan error; omit forecast_days to get a real 200 with one forecast day.</td></tr><tr><td>Search Locations</td><td><code>searchLocations</code></td><td>Looks up one or more locations by name, coordinates, ZIP code, or IP address and returns matching location suggestions. Confirmed live on this account: blocked with a real 403 error (code 105 function_access_restricted) despite Weatherstack's pricing page listing Location Search as a free-plan feature - correctly wired, gated by account entitlement, not a defect.</td></tr></tbody></table>

