---
description: "AccuWeather provides global weather data."
hidden: true
---

# AccuWeather

<img src="../../.gitbook/assets/connectors/accu-weather.png" alt="AccuWeather logo" width="64">

AccuWeather provides global weather data. This connector covers the AccuWeather APIs on dataservice.accuweather.com: location lookup by text, postal code, coordinates, IP address and point of interest, current conditions and past-24-hour observations, daily and hourly forecasts, MinuteCast precipitation, lifestyle indices, severe weather alerts and alarms, government tropical storm tracking, and phrase translations.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [accuweather.com](https://accuweather.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `accuWeather` |

## Use it

Add AccuWeather from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.accuWeather.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Cities | `autocompleteCities` | Returns up to ten AccuWeather city suggestions for a partial name, intended for type-ahead location pickers. |
| Autocomplete Cities In Country | `autocompleteCitiesInCountry` | Returns city matches for a partial name within a specific country, suitable for type-ahead search. |
| Autocomplete Locations | `autocompleteLocations` | Returns basic location matches for a partial name, covering cities and points of interest, suitable for type-ahead search. |
| Autocomplete Locations In Country | `autocompleteLocationsInCountry` | Returns basic location matches for a partial name within a specific country, for cities and points of interest, suitable for type-ahead search. |
| Autocomplete Points Of Interest | `autocompletePointsOfInterest` | Returns point-of-interest matches for a partial name, suitable for type-ahead search. |
| Autocomplete Points Of Interest In Country | `autocompletePointsOfInterestInCountry` | Returns point-of-interest matches for a partial name within a specific country, suitable for type-ahead search. |
| Get 1 Day Daily Forecast | `getDailyForecast1Day` | Returns today's AccuWeather daily forecast for a location, with the headline, high and low temperatures, and separate day and night summaries. |
| Get 1 Day Indices | `getDailyIndices1Day` | Returns today's AccuWeather lifestyle indices for a location, such as the UV index, flight delay risk, running and gardening conditions, each with a rating and a plain-language category. |
| Get 1 Hour Hourly Forecast | `getHourlyForecast1Hour` | Returns the AccuWeather forecast for the next single hour at a location, with temperature, conditions and precipitation probability. |
| Get 10 Day Daily Forecast | `getDailyForecast10Day` | Returns the AccuWeather ten-day daily forecast for a location, with a headline and a day and night summary for each of the ten days. |

<details>

<summary>See 75 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get 10 Day Indices | `getDailyIndices10Day` | Returns AccuWeather lifestyle indices for a location over the next ten days, one entry per index per day. |
| Get 12 Hour Hourly Forecast | `getHourlyForecast12Hour` | Returns the AccuWeather hour-by-hour forecast for the next twelve hours at a location. |
| Get 120 Hour Hourly Forecast | `getHourlyForecast120Hour` | Returns the AccuWeather hour-by-hour forecast for the next one hundred and twenty hours at a location, the longest hourly outlook available. |
| Get 15 Day Daily Forecast | `getDailyForecast15Day` | Returns the AccuWeather fifteen-day daily forecast for a location, the longest daily outlook available, with a day and night summary for each day. |
| Get 15 Day Indices | `getDailyIndices15Day` | Returns AccuWeather lifestyle indices for a location over the next fifteen days, one entry per index per day. |
| Get 24 Hour Hourly Forecast | `getHourlyForecast24Hour` | Returns the AccuWeather hour-by-hour forecast for the next twenty-four hours at a location. |
| Get 5 Day Daily Forecast | `getDailyForecast5Day` | Returns the AccuWeather five-day daily forecast for a location, with a headline and a day and night summary for each of the five days. |
| Get 5 Day Indices | `getDailyIndices5Day` | Returns AccuWeather lifestyle indices for a location over the next five days, one entry per index per day. |
| Get 7 Day Daily Forecast | `getDailyForecast7Day` | Returns AccuWeather's daily forecast for the next 7 days for a location, with a headline and day and night summaries for each day. |
| Get 72 Hour Hourly Forecast | `getHourlyForecast72Hour` | Returns the AccuWeather hour-by-hour forecast for the next seventy-two hours at a location. |
| Get Active Tropical Storm | `getActiveTropicalStorm` | Returns one currently active government-issued tropical cyclone by basin and government storm ID. Returns null when that storm is not active. |
| Get Administrative Area | `getAdminArea` | Returns a single administrative area by its country code and administrative area code. |
| Get Alerts | `getAlerts` | Returns government-issued severe weather alerts currently in effect for a location. |
| Get City By Coordinates | `getCityByGeoposition` | Returns the AccuWeather city nearest to a latitude and longitude, which is how you turn GPS coordinates into the location key the weather actions need. |
| Get City By IP Address | `getCityByIpAddress` | Returns the AccuWeather city that an IP address geolocates to, which is a quick way to pick a default location for a visitor. |
| Get Country | `getCountry` | Returns a single country by its region code and country code. |
| Get Current Conditions | `getCurrentConditions` | Returns the latest observed weather for a location: temperature, what it feels like, humidity, wind, visibility, pressure, UV index and a plain-language description. |
| Get Daily Indices By Group | `getDailyIndicesByGroup` | Returns the daily lifestyle indices belonging to one index group for a location over a 1, 5, 10 or 15 day range. |
| Get Historical Conditions Past 24 Hours | `getHistoricalConditions24Hour` | Returns the hourly weather observations recorded for a location over the past twenty-four hours. |
| Get Historical Conditions Past 6 Hours | `getHistoricalConditions6Hour` | Returns the hourly weather observations recorded for a location over the past six hours. |
| Get Index By ID | `getDailyIndexById` | Returns a single named AccuWeather lifestyle index for a location over the chosen number of days, for example just the UV index or just the flight delay risk. |
| Get Index Group Metadata | `getIndexGroupMetadata` | Returns metadata for every lifestyle index within one index group. |
| Get Index Metadata | `getIndexMetadata` | Returns metadata for a single lifestyle index by its index ID. |
| Get Language Code By ID | `getLanguageById` | Returns the language code for a numeric AccuWeather language ID. The API responds with a bare string, for example "en" for ID 1. |
| Get Language ID By Code | `getLanguageByCode` | Returns the numeric AccuWeather language ID for a language code. The API responds with a bare integer, for example 1 for en-us. |
| Get Lightning Forecast | `getLightningForecast` | Returns the short-range lightning probability forecast in 10-minute steps for a latitude and longitude. |
| Get Location By Geoposition | `getLocationByGeoposition` | Returns the location (of any type) closest to a latitude and longitude, including its location key. |
| Get Location By Key | `getLocationByKey` | Returns the full location record for an AccuWeather location key, including its name, country, administrative area, time zone and coordinates. |
| Get MinuteCast Precipitation Forecast | `getMinuteCast` | Returns AccuWeather MinuteCast, a minute-by-minute precipitation forecast for the next two hours at an exact latitude and longitude, with a plain-language summary of when rain or snow will start and stop. |
| Get Point Of Interest By Geoposition | `getPointOfInterestByGeoposition` | Returns the point of interest closest to a latitude and longitude, including its location key. Returns null when no point of interest is near the coordinates. |
| Get Radar And Satellite Images | `getRadarSatelliteImages` | Returns links to radar and satellite images centred on a location, in 480x480, 640x480 or 1024x1024 pixel sizes. |
| Get Region | `getRegion` | Returns a single AccuWeather region by its region code. |
| Get Top Cities Conditions | `getTopCitiesConditions` | Returns the current weather for each of the world's top-ranked cities in one call, useful for building a global weather board. |
| Get Translations By Group | `getTranslationsByGroup` | Returns the translated phrases of one translation group (for example US warning types or day names) in the requested language. |
| Get Tropical Storm | `getTropicalStorm` | Returns one government-issued tropical cyclone by season year, basin and government storm ID. |
| Get Tropical Storm Current Position | `getTropicalStormCurrentPosition` | Returns the current position, wind speed, pressure and movement of a government-issued tropical cyclone. |
| Get Weather Alarms | `getWeatherAlarms` | Returns threshold-based weather alarms (temperature extremes, heavy rain, high wind and similar) derived from the daily forecast for a location over a 1, 5, 10 or 15 day range. |
| List Active Tropical Storms | `listActiveTropicalStorms` | Returns all currently active government-issued tropical cyclones across every basin. |
| List Active Tropical Storms In Basin | `listActiveTropicalStormsInBasin` | Returns the currently active government-issued tropical cyclones in one basin. |
| List Administrative Areas | `listAdminAreas` | Lists the administrative areas within a country, such as states, provinces or counties. Use an area code to narrow a city search to one part of a country. |
| List All Administrative Areas | `listAllAdminAreas` | Returns administrative areas across all countries, optionally filtered by country code or administrative area code, in pages of 25. |
| List Countries | `listCountries` | Lists every country AccuWeather has location data for, with its two-letter country code. |
| List Countries In Region | `listCountriesInRegion` | Lists the countries that belong to one AccuWeather world region, such as all European countries. |
| List Historical Lightning Strikes | `listHistoricalLightningStrikes` | Returns daily historical lightning strikes within a radius of a latitude and longitude starting from a given date. Available only on AccuWeather Enterprise plans with the Lightning API enabled. |
| List Index Groups | `listIndexGroups` | Returns the list of lifestyle index groups (for example Health, Outdoor Activities) with their IDs. |
| List Index Metadata | `listIndexMetadata` | Returns metadata (ID, name, description, ascending flag) for every available lifestyle index. |
| List Lightning Strikes In Bounding Box | `listLightningStrikesInBoundingBox` | Returns recent lightning strikes within a bounding box over the last 5 to 120 minutes as a GeoJSON feature collection. Available only on AccuWeather Enterprise plans with the Lightning API enabled. |
| List Lightning Strikes In Radius | `listLightningStrikesInRadius` | Returns recent lightning strikes within a radius of a latitude and longitude over the last 5 to 120 minutes as a GeoJSON feature collection. |
| List MinuteCast Colors | `listMinuteCastColors` | Returns the full MinuteCast color code table used to render precipitation intensity and type. |
| List MinuteCast Simple Colors | `listMinuteCastSimpleColors` | Returns the simplified MinuteCast color code table used to render precipitation intensity and type. |
| List Neighboring Locations | `listNeighboringLocations` | Returns the locations that neighbor a given location key, with their own location keys and geoposition. |
| List Regions | `listRegions` | Lists the world regions AccuWeather groups countries into, such as Europe, Africa and Asia. Use a region code with List Countries In Region to narrow a country lookup. |
| List Supported Languages | `listSupportedLanguages` | Returns every language AccuWeather can return content in, with language IDs and codes. |
| List Top Cities | `listTopCities` | Lists the world's most significant cities ranked by AccuWeather, in groups of 50, 100 or 150, each with the location key other actions need. |
| List Top Cities In Region | `listTopCitiesInRegion` | Returns the list of top cities for an AccuWeather region, with location keys for each city. |
| List Translation Groups | `listTranslationGroups` | Returns the list of translation groups (phrase categories) with their IDs. |
| List Tropical Storm Forecasts | `listTropicalStormForecasts` | Returns the forecast positions and intensities of a government-issued tropical cyclone. |
| List Tropical Storm Positions | `listTropicalStormPositions` | Returns the historical track positions of a government-issued tropical cyclone. |
| List Tropical Storm Statuses | `listTropicalStormStatuses` | Returns the status classifications (for example Tropical Storm, Hurricane - Category 1) and their sustained wind thresholds used for government-issued tropical cyclones across all basins. |
| List Tropical Storm Statuses In Basin | `listTropicalStormStatusesInBasin` | Returns the status classifications and their sustained wind thresholds used for government-issued tropical cyclones in one basin. |
| List Tropical Storms By Year | `listTropicalStormsByYear` | Returns every government-issued tropical cyclone recorded in a season year across all basins. |
| List Tropical Storms By Year And Basin | `listTropicalStormsByYearAndBasin` | Returns the government-issued tropical cyclones recorded in one basin for a season year. |
| Search Administrative Areas | `searchAdminAreas` | Searches administrative areas by name across all countries, returning matches with their codes. |
| Search Administrative Areas In Country | `searchAdminAreasInCountry` | Searches administrative areas by name within a specific country, returning matches with their codes. |
| Search Cities | `searchCities` | Searches AccuWeather cities worldwide by name and returns the matches with their location keys, countries and coordinates. |
| Search Cities In Administrative Area | `searchCitiesInAdminArea` | Searches for cities by name within a specific country and administrative area, returning matching locations with their location keys. |
| Search Cities In Country | `searchCitiesInCountry` | Searches AccuWeather cities by name within a single country, which removes same-name matches from elsewhere in the world. |
| Search Locations | `searchLocations` | Searches every AccuWeather location type at once by free text, returning cities, postal codes and points of interest that match, each with the location key the weather actions need. |
| Search Locations In Administrative Area | `searchLocationsInAdminArea` | Searches for locations of any type by name within a specific country and administrative area, returning matches with their location keys. |
| Search Locations In Country | `searchLocationsInCountry` | Searches for locations of any type by name within a specific country, returning matches with their location keys. |
| Search Points Of Interest | `searchPointsOfInterest` | Searches AccuWeather points of interest such as airports, parks and stadiums by name, returning each with the location key needed to fetch its weather. |
| Search Points Of Interest In Administrative Area | `searchPointsOfInterestInAdminArea` | Searches for points of interest by name within a specific country and administrative area, returning matches with their location keys. |
| Search Points Of Interest In Country | `searchPointsOfInterestInCountry` | Searches for points of interest by name within a specific country, returning matches with their location keys. |
| Search Postal Codes | `searchPostalCodes` | Searches AccuWeather locations by postal code and returns the matches with their location keys. Postal code coverage varies by country. |
| Search Postal Codes In Country | `searchPostalCodesInCountry` | Searches for a postal code within a specific country and returns the matching locations with their location keys. |

</details>
