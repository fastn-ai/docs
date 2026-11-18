---
description: "WeatherAPI.com provides real-time weather, multi-day and hourly forecasts, historical weather back to 2010, long-range future forecasts, astronomy, marine…"
hidden: true
---

# WeatherAPI.com

WeatherAPI.com provides real-time weather, multi-day and hourly forecasts, historical weather back to 2010, long-range future forecasts, astronomy, marine weather, sports schedules, time zone lookup, location search/autocomplete, IP geolocation, air quality, and government weather alerts through a single REST API authenticated by an API key passed as a query parameter.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [weatherapi.com](https://weatherapi.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 13 |
| **Events** | 0 |
| **Slug** | `weatherApiCom` |

## Use it

Add WeatherAPI.com from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.weatherApiCom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check API Connection | `checkApiConnection` | Fetches current weather for London to confirm the configured API key is valid and the connection is working. Used as the connector's connection-verification check. |
| Get Astronomy Data | `getAstronomy` | Retrieves sunrise, sunset, moonrise, moonset, moon phase, and moon illumination for a location on a given date. |
| Get Bulk Current Weather | `getBulkCurrentWeather` | Retrieves current weather for multiple locations in a single request, with each location counted as one API call. Requires a Business-tier plan or higher; on the Free plan this endpoint returns a plan-restriction error. |
| Get Current Weather | `getCurrentWeather` | Retrieves real-time weather conditions for a city, US/UK/Canada postcode, latitude/longitude pair, or IP address, optionally including current air quality data. |
| Get Future Weather | `getFutureWeather` | Retrieves a long-range weather forecast at 3-hour intervals for a date between 14 and 300 days from today, based on historical trend data rather than short-term modeling. |
| Get Historical Weather | `getHistory` | Retrieves past weather observations for a location on a specific date or date range, from 1st January 2010 onwards, optionally including hourly air quality and pollen data. |
| Get Marine Weather | `getMarineWeather` | Retrieves a marine and sailing weather forecast of up to 7 days for a coastal or open-water location, including wave height, swell, and tide information. |
| Get Sports Events | `getSportsEvents` | Lists upcoming football, cricket, and golf events scheduled near a given location. |
| Get Time Zone | `getTimeZone` | Retrieves the IANA time zone identifier and current local time for a location. |
| Get Weather Alerts | `getWeatherAlerts` | Retrieves active government-issued weather alerts and warnings for a location. |
| Get Weather Forecast | `getForecast` | Retrieves a daily and hourly weather forecast of up to 14 days for a location, optionally including air quality, government weather alerts, and pollen data for a specific date. |
| Look Up IP Address | `lookupIpAddress` | Retrieves geolocation, time zone, and network details for a given IP address. |
| Search Locations | `searchLocations` | Searches for matching cities and towns for a partial location name, useful for building autocomplete or location-picker experiences. |
