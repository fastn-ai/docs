---
description: "The USGS Earthquake Catalog records earthquakes worldwide. Search and count earthquake events and read real-time feeds."
hidden: true
---

# USGS Earthquake Catalog

<img src="../../.gitbook/assets/connectors/lg/usgs-earthquake-catalog.png" alt="USGS Earthquake Catalog logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [earthquake.usgs.gov](https://earthquake.usgs.gov) |
| **Authentication** | No sign-in needed |
| **Slug** | `usgsEarthquakeCatalog` |

## Setup

USGS Earthquake Catalog needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add USGS Earthquake Catalog from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.usgsEarthquakeCatalog.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Count Earthquake Events</td><td><code>countEvents</code></td><td>Count the events that match the same filters as Search Earthquake Events geojson returns {count, maxAllowed}; text (default) returns the number; xml returns XML. Docs: https://earthquake.usgs.gov/fdsnws/event/1/</td></tr><tr><td>Get Enumerated Parameter Values</td><td><code>getEnumeratedValues</code></td><td>Get the known values for enumerated parameters: catalogs, contributors, product types, event types and magnitude types Docs: https://earthquake.usgs.gov/fdsnws/event/1/</td></tr><tr><td>Get Real-Time Earthquake Feed</td><td><code>getRealtimeFeed</code></td><td>Get a USGS real-time GeoJSON summary feed of recent earthquakes, updated every minute USGS recommends these feeds over the query method for showing recent events. Docs: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php</td></tr><tr><td>Get Service Version</td><td><code>getVersion</code></td><td>Get the full version number of the event web service, as plain text, e.g. 2.8.1. Docs: https://earthquake.usgs.gov/fdsnws/event/1/</td></tr><tr><td>Get Service WADL</td><td><code>getWadl</code></td><td>Get the WADL (Web Application Description Language) description of the event web service, as XML text. Docs: https://earthquake.usgs.gov/fdsnws/event/1/</td></tr><tr><td>List Catalogs</td><td><code>listCatalogs</code></td><td>List the catalog ids that can be used in the catalog filter Returned as XML text. Docs: https://earthquake.usgs.gov/fdsnws/event/1/</td></tr><tr><td>List Contributors</td><td><code>listContributors</code></td><td>List the contributor ids that can be used in the contributor filter Returned as XML text. Docs: https://earthquake.usgs.gov/fdsnws/event/1/</td></tr><tr><td>Search Earthquake Events</td><td><code>searchEvents</code></td><td>Search the USGS ComCat earthquake catalog by time, area (rectangle or circle), magnitude, depth, alert level, intensity and more Use format geojson for JSON; quakeml (xml) is the default, csv/text/kml are also available. Max 20,000 events per request. Docs: https://earthquake.usgs.gov/fdsnws/event/1/</td></tr></tbody></table>

## Events

USGS Earthquake Catalog has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
