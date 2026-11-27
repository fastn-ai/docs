---
description: "The Swiss public transport service covers trains, trams and buses in Switzerland. Search stations and connections and read departure boards."
hidden: true
---

# Swiss Public Transport (transport.opendata.ch)

<img src="../../.gitbook/assets/connectors/lg/swiss-public-transport.png" alt="Swiss Public Transport (transport.opendata.ch) logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [transport.opendata.ch](https://transport.opendata.ch) |
| **Authentication** | No sign-in needed |
| **Slug** | `swissPublicTransport` |

## Setup

Swiss Public Transport (transport.opendata.ch) needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Connect in Fastn

Your customers connect Swiss Public Transport (transport.opendata.ch) from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Swiss Public Transport (transport.opendata.ch)**.
2. Select **Connect** on the Swiss Public Transport (transport.opendata.ch) card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Swiss Public Transport (transport.opendata.ch) needs no credentials. Select **Connect** in the dialog that opens.

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Swiss Public Transport (transport.opendata.ch)'s actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Stationboard</td><td><code>getStationboard</code></td><td>Get the next departures (or arrivals) from a Swiss station, with line, destination, platform and delay Give station or id; id wins when both are set. Docs: https://transport.opendata.ch/docs.html</td></tr><tr><td>Search Connections</td><td><code>searchConnections</code></td><td>Find public transport connections (journeys) between two places in Switzerland, with sections, platforms, delays and capacity Docs: https://transport.opendata.ch/docs.html</td></tr><tr><td>Search Locations</td><td><code>searchLocations</code></td><td>Find stations, stops, addresses and points of interest in Switzerland by name or near a coordinate Give query, or x and y. A 'refine' type result means the request must be redone with a clearer name. Docs: https://transport.opendata.ch/docs.html</td></tr></tbody></table>

