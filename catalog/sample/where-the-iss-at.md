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

## Connect in Fastn

Your customers connect Where the ISS at from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Where the ISS at**.
2. Select **Connect** on the Where the ISS at card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Where the ISS at needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Where the ISS at's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Coordinates Info</td><td><code>getCoordinatesInfo</code></td><td>Get the timezone id, current UTC offset, country code and a map link for a latitude/longitude pair,{lon}). Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer</td></tr><tr><td>Get Satellite Position</td><td><code>getSatellitePosition</code></td><td>Get the position, altitude, velocity, visibility and footprint of a satellite now or at a given Unix timestamp Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer</td></tr><tr><td>Get Satellite Positions</td><td><code>getSatellitePositions</code></td><td>Get the satellite's position for up to 10 Unix timestamps in one request Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer</td></tr><tr><td>Get Satellite TLE</td><td><code>getSatelliteTles</code></td><td>Get the latest two-line element (TLE) orbital data for a satellite, as JSON or plain text Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer</td></tr><tr><td>List Satellites</td><td><code>listSatellites</code></td><td>List the satellites the API has data for, with name and NORAD catalog id Currently only the ISS (25544). Rate limit about 1 request per second. Docs: https://wheretheiss.at/w/developer</td></tr></tbody></table>

