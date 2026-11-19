---
description: "Nominatim is the search engine for OpenStreetMap. Search places and addresses, reverse geocode coordinates and get place details."
hidden: true
---

# OpenStreetMap Nominatim

<img src="../../.gitbook/assets/connectors/lg/nominatim.png" alt="OpenStreetMap Nominatim logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [nominatim.openstreetmap.org](https://nominatim.openstreetmap.org) |
| **Authentication** | No sign-in needed |
| **Slug** | `nominatim` |

## Setup

OpenStreetMap Nominatim needs no sign-in, so there is nothing to set up. Add it and use its actions.

## Use it

Add OpenStreetMap Nominatim from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nominatim.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Place Details</td><td><code>getDetails</code></td><td>Show Nominatim's internal details for one object, by place_id or by OSM type + id Meant for debugging; the output format may change. Usage policy: at most 1 request per second, no bulk geocoding. Docs: https://nominatim.org/release-docs/latest/api/Details/</td></tr><tr><td>Get Server Status</td><td><code>getStatus</code></td><td>Check the Nominatim server and database status and when the data was last updated Usage policy: at most 1 request per second, no bulk geocoding. Docs: https://nominatim.org/release-docs/latest/api/Status/</td></tr><tr><td>List Broken Polygons</td><td><code>listBrokenPolygons</code></td><td>List broken polygons Nominatim detected in OSM data, with the error found Docs: https://nominatim.org/release-docs/latest/api/Overview/</td></tr><tr><td>List Deletable Objects</td><td><code>listDeletable</code></td><td>List objects that were deleted in OSM but are held back in Nominatim in case the deletion was vandalism Docs: https://nominatim.org/release-docs/latest/api/Overview/</td></tr><tr><td>Look Up OSM Objects</td><td><code>lookup</code></td><td>Get address details for up to 50 OSM objects by their ids Usage policy: at most 1 request per second, no bulk geocoding. Docs: https://nominatim.org/release-docs/latest/api/Lookup/</td></tr><tr><td>Reverse Geocode</td><td><code>reverse</code></td><td>Find the address or place closest to a coordinate Usage policy: at most 1 request per second, no bulk geocoding. Docs: https://nominatim.org/release-docs/latest/api/Reverse/</td></tr><tr><td>Search Places</td><td><code>search</code></td><td>Geocode: find OSM objects by a free-form query (q) or by structured address fields (amenity, street, city, county, state, country, postalcode) - use one style, not both Usage policy: at most 1 request per second, no bulk geocoding. Docs: https://nominatim.org/release-docs/latest/api/Search/</td></tr></tbody></table>

## Events

OpenStreetMap Nominatim has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
