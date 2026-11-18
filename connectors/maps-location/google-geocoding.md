---
description: "Google Maps Platform Geocoding API connector."
hidden: true
---

# Google Geocoding

Google Maps Platform Geocoding API connector. Forward geocode addresses into coordinates/Place IDs and reverse geocode coordinates/Place IDs into addresses, plus Time Zone and Elevation lookups. Authenticates with a Google Maps Platform API key supplied as the 'key' query parameter.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [maps.google.com](https://maps.google.com) |
| **Authentication** | API key |
| **Actions** | 5 |
| **Events** | 0 |
| **Slug** | `googleGeocoding` |

## Use it

Add Google Geocoding from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleGeocoding.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Forward Geocode (by address) | `forwardGeocode` | Forward geocoding: convert an address, Plus Code, or structured components into latitude/longitude coordinates and a Place ID using the Geocoding API. Supply either 'address' or 'components' (or both). Optional bounds, region, language, and result filters refine the results. |
| Get Elevation (locations) | `getElevation` | Elevation API: return elevation data (meters above sea level) for one or more discrete locations on the earth. Provide 'locations' as pipe-separated 'lat,lng' pairs. |
| Get Elevation Along Path | `getElevationAlongPath` | Elevation API (path mode): return elevation data for a number of samples taken along a path on the earth's surface. Provide 'path' as pipe-separated 'lat,lng' pairs (or an encoded polyline) and the number of 'samples'. |
| Get Time Zone | `getTimeZone` | Time Zone API: return the time zone, UTC offset, and daylight-savings offset for a given location and timestamp. Provide the location as 'lat,lng' and a Unix timestamp (seconds since midnight Jan 1 1970 UTC). |
| Reverse Geocode (by latlng or place_id) | `reverseGeocode` | Reverse geocoding: convert latitude/longitude coordinates ('latlng') or a Place ID ('place_id') into a human-readable address and address components using the Geocoding API. Optional result_type and location_type filters restrict the returned results. |
