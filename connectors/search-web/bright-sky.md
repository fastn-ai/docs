---
description: "Bright Sky is a free JSON API for open weather data from the German Weather Service (DWD)."
---

# Bright Sky

Bright Sky is a free JSON API for open weather data from the German Weather Service (DWD). Get hourly historical weather, MOSMIX forecasts and current conditions for any location, raw SYNOP observations, rain radar, DWD weather alerts and the list of weather stations. No API key needed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [brightsky.dev](https://brightsky.dev) |
| **Authentication** | No authentication |
| **Actions** | 6 |
| **Events** | 0 |
| **Slug** | `brightSky` |

## Use it

Add Bright Sky from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.brightSky.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Current Weather | `getCurrentWeather` | Current weather. Returns current weather for a given location. To set the location for which to retrieve weather, you must supply both `lat` and `lon` _or_ one of `dwd_station_id`, `wmo_station_id`, or `source_id`. This endpoint is different from the other weather endpoints in that it does not directly correspond to any of the data available from the DWD Open Data server. Instead, it is a best-effort solution to reflect current weather conditions by compiling [SYNOP observations](/operations/getSynop) from the past one and a half hours. Docs: https://brightsky.dev/docs/ (GET /current_weather) |
| Get Hourly Weather | `getWeather` | Hourly weather (including forecasts). Returns a list of hourly weather records (and/or forecasts) for the time range given by `date` and `last_date`. To set the location for which to retrieve records (and/or forecasts), you must supply both `lat` and `lon` _or_ one of `dwd_station_id`, `wmo_station_id`, or `source_id`. Docs: https://brightsky.dev/docs/ (GET /weather) |
| Get Rain Radar | `getRadar` | Get rain radar data (1 km grid, 5-minute steps, past 6 hours plus a 2-hour forecast) from the DWD 1200 x 1100 km radar grid. Narrow it with lat/lon + distance or a pixel bbox - the full grid is large. format: compressed (default, base64 zlib), bytes or plain (2-D integer grid; plain/bytes need a gzip/br/zstd-accepting client). Docs: https://brightsky.dev/docs/ (GET /radar) |
| Get SYNOP Observations | `getSynopObservations` | Get raw ten-minutely SYNOP observations for one station between date and last_date (only the past 30 hours are stored). Supply one of dwd_station_id, wmo_station_id or source_id - lat/lon is not supported (use Get Weather Sources to find a station). Parameters such as sunshine_60 are only reported at certain timestamps. Docs: https://brightsky.dev/docs/ (GET /synop) |
| Get Weather Alerts | `getAlerts` | Get DWD weather alerts for a location (lat+lon or a municipality warn_cell_id), or all current alerts in Germany when no location is given. With a location, the location field describes the warn cell. Alerts carry English and German headline, description and instruction, severity, urgency, certainty, onset and expiry. Docs: https://brightsky.dev/docs/ (GET /alerts) |
| Get Weather Sources | `getSources` | Weather sources (stations). Return a list of all Bright Sky sources matching the given location criteria, ordered by distance. You must supply both `lat` and `lon` _or_ one of `dwd_station_id`, `wmo_station_id`, or `source_id`. Docs: https://brightsky.dev/docs/ (GET /sources) |
