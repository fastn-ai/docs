---
description: "Where the ISS at?"
hidden: true
---

# Where the ISS at

<img src="../../.gitbook/assets/connectors/where-the-iss-at.png" alt="Where the ISS at logo" width="64">

Where the ISS at? is a free REST API for the International Space Station: its current, past or future position, velocity and visibility, TLE orbital data, and timezone and country info for any coordinates. No API key needed; about 1 request per second.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [wheretheiss.at](https://wheretheiss.at) |
| **Authentication** | No authentication |
| **Slug** | `whereTheIssAt` |

## Use it

Add Where the ISS at from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.whereTheIssAt.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Coordinates Info | `getCoordinatesInfo` | Get the timezone id, current UTC offset, country code and a map link for a latitude/longitude pair (GET /coordinates/{lat},{lon}). Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer |
| Get Satellite Position | `getSatellitePosition` | Get the position, altitude, velocity, visibility and footprint of a satellite now or at a given Unix timestamp (GET /satellites/{id}). Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer |
| Get Satellite Positions | `getSatellitePositions` | Get the satellite's position for up to 10 Unix timestamps in one request (GET /satellites/{id}/positions). Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer |
| Get Satellite TLE | `getSatelliteTles` | Get the latest two-line element (TLE) orbital data for a satellite, as JSON or plain text (GET /satellites/{id}/tles). Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer |
| List Satellites | `listSatellites` | List the satellites the API has data for, with name and NORAD catalog id (GET /satellites). Currently only the ISS (25544). Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer |
