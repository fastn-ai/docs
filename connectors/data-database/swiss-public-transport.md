---
description: "The Swiss public transport API (transport.opendata.ch) is a free, open API for Swiss trains, trams, buses and boats."
hidden: true
---

# Swiss Public Transport (transport.opendata.ch)

<img src="../../.gitbook/assets/connectors/lg/swiss-public-transport.png" alt="Swiss Public Transport (transport.opendata.ch) logo">

The Swiss public transport API (transport.opendata.ch) is a free, open API for Swiss trains, trams, buses and boats. Search stations and addresses, plan connections between two places with platforms and delays, and get live departure boards. No API key needed.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [transport.opendata.ch](https://transport.opendata.ch) |
| **Authentication** | No authentication |
| **Slug** | `swissPublicTransport` |

## Use it

Add Swiss Public Transport (transport.opendata.ch) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.swissPublicTransport.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Stationboard | `getStationboard` | Get the next departures (or arrivals) from a Swiss station, with line, destination, platform and delay (GET /v1/stationboard). Give station or id; id wins when both are set. Docs: https://transport.opendata.ch/docs.html |
| Search Connections | `searchConnections` | Find public transport connections (journeys) between two places in Switzerland, with sections, platforms, delays and capacity (GET /v1/connections). Docs: https://transport.opendata.ch/docs.html |
| Search Locations | `searchLocations` | Find stations, stops, addresses and points of interest in Switzerland by name or near a coordinate (GET /v1/locations). Give query, or x and y. A 'refine' type result means the request must be redone with a clearer name. Docs: https://transport.opendata.ch/docs.html |
