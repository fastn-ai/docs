---
description: "Nominatim is the search engine for OpenStreetMap data."
hidden: true
---

# OpenStreetMap Nominatim

Nominatim is the search engine for OpenStreetMap data. Geocode free-form or structured addresses, reverse geocode coordinates, look up OSM objects by id, get place details, and check server status, held-back deletions and broken polygons. Free public server with no API key, limited to 1 request per second under the OSMF usage policy; results are ODbL-licensed.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [nominatim.openstreetmap.org](https://nominatim.openstreetmap.org) |
| **Authentication** | No authentication |
| **Actions** | 7 |
| **Events** | 0 |
| **Slug** | `nominatim` |

## Use it

Add OpenStreetMap Nominatim from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nominatim.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Place Details | `getDetails` | Show Nominatim's internal details for one object, by place_id or by OSM type + id (GET /details). Meant for debugging; the output format may change. Usage policy: at most 1 request per second, no bulk geocoding. Docs: https://nominatim.org/release-docs/latest/api/Details/ |
| Get Server Status | `getStatus` | Check the Nominatim server and database status and when the data was last updated (GET /status). Usage policy: at most 1 request per second, no bulk geocoding. Docs: https://nominatim.org/release-docs/latest/api/Status/ |
| List Broken Polygons | `listBrokenPolygons` | List broken polygons Nominatim detected in OSM data, with the error found (GET /polygons). Docs: https://nominatim.org/release-docs/latest/api/Overview/ |
| List Deletable Objects | `listDeletable` | List objects that were deleted in OSM but are held back in Nominatim in case the deletion was vandalism (GET /deletable). Docs: https://nominatim.org/release-docs/latest/api/Overview/ |
| Look Up OSM Objects | `lookup` | Get address details for up to 50 OSM objects by their ids (GET /lookup). Usage policy: at most 1 request per second, no bulk geocoding. Docs: https://nominatim.org/release-docs/latest/api/Lookup/ |
| Reverse Geocode | `reverse` | Find the address or place closest to a coordinate (GET /reverse). Usage policy: at most 1 request per second, no bulk geocoding. Docs: https://nominatim.org/release-docs/latest/api/Reverse/ |
| Search Places | `search` | Geocode: find OSM objects by a free-form query (q) or by structured address fields (amenity, street, city, county, state, country, postalcode) - use one style, not both (GET /search). Usage policy: at most 1 request per second, no bulk geocoding. Docs: https://nominatim.org/release-docs/latest/api/Search/ |
