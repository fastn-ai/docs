---
description: "Google Geocoding converts between addresses and coordinates. Geocode and reverse geocode places, and get elevation and time zones."
hidden: true
---

# Google Geocoding

<img src="../../.gitbook/assets/connectors/lg/google-geocoding.png" alt="Google Geocoding logo">

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [maps.google.com](https://maps.google.com) |
| **Authentication** | API key |
| **Slug** | `googleGeocoding` |

## Setup

Your customers enter their API key for Google Geocoding when they connect. Nothing else needs setting up.

## Use it

Add Google Geocoding from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleGeocoding.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Forward Geocode (by address)</td><td><code>forwardGeocode</code></td><td>Forward geocoding: convert an address, Plus Code, or structured components into latitude/longitude coordinates and a Place ID using the Geocoding API. Supply either 'address' or 'components' (or both). Optional bounds, region, language, and result filters refine the results.</td></tr><tr><td>Get Elevation (locations)</td><td><code>getElevation</code></td><td>Elevation API: return elevation data (meters above sea level) for one or more discrete locations on the earth. Provide 'locations' as pipe-separated 'lat,lng' pairs.</td></tr><tr><td>Get Elevation Along Path</td><td><code>getElevationAlongPath</code></td><td>Elevation API (path mode): return elevation data for a number of samples taken along a path on the earth's surface. Provide 'path' as pipe-separated 'lat,lng' pairs (or an encoded polyline) and the number of 'samples'.</td></tr><tr><td>Get Time Zone</td><td><code>getTimeZone</code></td><td>Time Zone API: return the time zone, UTC offset, and daylight-savings offset for a given location and timestamp. Provide the location as 'lat,lng' and a Unix timestamp (seconds since midnight Jan 1 1970 UTC).</td></tr><tr><td>Reverse Geocode (by latlng or place_id)</td><td><code>reverseGeocode</code></td><td>Reverse geocoding: convert latitude/longitude coordinates ('latlng') or a Place ID ('place_id') into a human-readable address and address components using the Geocoding API. Optional result_type and location_type filters restrict the returned results.</td></tr></tbody></table>

## Events

Google Geocoding has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
