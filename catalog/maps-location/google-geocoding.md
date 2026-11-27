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

## Connect in Fastn

Your customers connect Google Geocoding from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Geocoding**.
2. Select **Connect** on the Google Geocoding card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Geocoding's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Forward Geocode (by address)</td><td><code>forwardGeocode</code></td><td>Forward geocoding: convert an address, Plus Code, or structured components into latitude/longitude coordinates and a Place ID using the Geocoding API. Supply either 'address' or 'components' (or both). Optional bounds, region, language, and result filters refine the results.</td></tr><tr><td>Get Elevation (locations)</td><td><code>getElevation</code></td><td>Elevation API: return elevation data (meters above sea level) for one or more discrete locations on the earth. Provide 'locations' as pipe-separated 'lat,lng' pairs.</td></tr><tr><td>Get Elevation Along Path</td><td><code>getElevationAlongPath</code></td><td>Elevation API (path mode): return elevation data for a number of samples taken along a path on the earth's surface. Provide 'path' as pipe-separated 'lat,lng' pairs (or an encoded polyline) and the number of 'samples'.</td></tr><tr><td>Get Time Zone</td><td><code>getTimeZone</code></td><td>Time Zone API: return the time zone, UTC offset, and daylight-savings offset for a given location and timestamp. Provide the location as 'lat,lng' and a Unix timestamp (seconds since midnight Jan 1 1970 UTC).</td></tr><tr><td>Reverse Geocode (by latlng or place_id)</td><td><code>reverseGeocode</code></td><td>Reverse geocoding: convert latitude/longitude coordinates ('latlng') or a Place ID ('place_id') into a human-readable address and address components using the Geocoding API. Optional result_type and location_type filters restrict the returned results.</td></tr></tbody></table>

