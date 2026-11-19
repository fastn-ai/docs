---
description: "Where the ISS at tracks the International Space Station. Get satellite positions, orbit data and coordinate details."
hidden: true
---

# Where the ISS at

<img src="../../.gitbook/assets/connectors/lg/where-the-iss-at.png" alt="Where the ISS at logo">

| | |
| --- | --- |
| **Category** | [Sample and novelty APIs](README.md) |
| **Website** | [wheretheiss.at](https://wheretheiss.at) |
| **Authentication** | No sign-in needed |
| **Slug** | `whereTheIssAt` |

## Setup

Where the ISS at needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add Where the ISS at from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.whereTheIssAt.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Coordinates Info</td><td><code>getCoordinatesInfo</code></td><td>Get the timezone id, current UTC offset, country code and a map link for a latitude/longitude pair,{lon}). Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer</td></tr><tr><td>Get Satellite Position</td><td><code>getSatellitePosition</code></td><td>Get the position, altitude, velocity, visibility and footprint of a satellite now or at a given Unix timestamp Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer</td></tr><tr><td>Get Satellite Positions</td><td><code>getSatellitePositions</code></td><td>Get the satellite's position for up to 10 Unix timestamps in one request Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer</td></tr><tr><td>Get Satellite TLE</td><td><code>getSatelliteTles</code></td><td>Get the latest two-line element (TLE) orbital data for a satellite, as JSON or plain text Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer</td></tr><tr><td>List Satellites</td><td><code>listSatellites</code></td><td>List the satellites the API has data for, with name and NORAD catalog id Currently only the ISS (25544). Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer</td></tr></tbody></table>

## Events

Where the ISS at has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
