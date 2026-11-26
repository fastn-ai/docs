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

## Use it

Add Swiss Public Transport (transport.opendata.ch) from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.swissPublicTransport.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Stationboard</td><td><code>getStationboard</code></td><td>Get the next departures (or arrivals) from a Swiss station, with line, destination, platform and delay Give station or id; id wins when both are set. Docs: https://transport.opendata.ch/docs.html</td></tr><tr><td>Search Connections</td><td><code>searchConnections</code></td><td>Find public transport connections (journeys) between two places in Switzerland, with sections, platforms, delays and capacity Docs: https://transport.opendata.ch/docs.html</td></tr><tr><td>Search Locations</td><td><code>searchLocations</code></td><td>Find stations, stops, addresses and points of interest in Switzerland by name or near a coordinate Give query, or x and y. A 'refine' type result means the request must be redone with a clearer name. Docs: https://transport.opendata.ch/docs.html</td></tr></tbody></table>

## Events

Swiss Public Transport (transport.opendata.ch) has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
