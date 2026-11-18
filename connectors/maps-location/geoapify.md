---
description: "Geoapify is a location platform built on OpenStreetMap data."
hidden: true
---

# Geoapify

<img src="../../.gitbook/assets/connectors/lg/geoapify.png" alt="Geoapify logo">

Geoapify is a location platform built on OpenStreetMap data. This connector covers the Geoapify REST APIs: forward, reverse and batch geocoding, address autocomplete, places search and place details, postcodes, boundaries, routing, route matrix, route planner optimization, isochrones and isodistances, map matching, elevation, geometry storage and geometry operations, IP geolocation, generic batch jobs, and map rendering (static maps, map tiles, MapLibre styles and marker icons).

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [geoapify.com](https://geoapify.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `geoapify` |

## Use it

Add Geoapify from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.geoapify.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Autocomplete Address | `autocompleteAddress` | Returns address and place suggestions for partial text, for type-ahead address search. Use filter to restrict results and bias to rank them without excluding matches. |
| Calculate Isoline | `calculateIsoline` | Calculates reachability areas from an origin: isochrones by travel time or isodistances by travel distance for a travel mode. Can also retrieve a previously calculated isoline by its id. Returns GeoJSON polygons. |
| Calculate Route | `calculateRoute` | Calculates a route through two or more ordered waypoints for a travel mode, returning geometry, distance, travel time, legs, steps and turn-by-turn instructions. |
| Calculate Route Matrix | `calculateRouteMatrix` | Calculates travel time and distance from every source location to every target location for a travel mode, returning a sources-to-targets matrix. |
| Combine Geometries | `combineGeometries` | Merges (union) or intersects two or more previously generated isolines or stored geometries by their ids and returns the combined GeoJSON, whose new id can be reused in later geometry calls. |
| Geocode Address | `geocodeAddress` | Converts a free-form address (text) or structured address parts (name, housenumber, street, postcode, city, state, country) into geographic coordinates and normalized address components. Do not combine text with the structured parameters. Returns a GeoJSON FeatureCollection by default. |
| Get Batch Geocode Job Result | `getBatchGeocodeJob` | Retrieves the status or results of a batch forward geocoding job by its id. Geoapify answers HTTP 202 with status pending while the job is still processing, and HTTP 200 with the geocoded results once it has finished. |
| Get Batch Job Result | `getBatchJob` | Retrieves the status or results of a generic batch job by its 32-character id. Geoapify answers HTTP 202 with status pending while the job is still processing, and HTTP 200 with one result per input once it has finished. |
| Get Batch Reverse Geocode Job Result | `getBatchReverseGeocodeJob` | Retrieves the status or results of a batch reverse geocoding job by its id. Geoapify answers HTTP 202 with status pending while the job is still processing, and HTTP 200 with the resolved addresses once it has finished. |
| Get Boundaries Containing Place | `getBoundariesPartOf` | Finds the administrative, postal, political and other boundaries that contain a place, identified by a Geoapify place id, coordinates, or an OpenStreetMap id and type. |

<details>

<summary>See 21 more actions</summary>

* **Get Boundaries Within Place** `getBoundariesConsistsOf`: Lists the sub-boundaries contained by a boundary, for example the districts of a city or the municipalities of a region, for a boundary identified by its Geoapify place id.
* **Get Elevations** `getElevations`: Returns the ground elevation for up to 1000 ordered locations, optionally with the distance from the previous location, in metric or imperial units. Results preserve the input order.
* **Get High Resolution Map Tile** `getHighResolutionMapTile`: Downloads a 2x or 3x pixel-density raster PNG map tile for a style at Slippy Map zoom, x and y coordinates, returned as a base64 file reference. The geographic area covered is the same as the standard tile.
* **Get IP Geolocation** `getIpGeolocation`: Returns the approximate location, country, state, city, timezone and currency details for an IPv4 or IPv6 address, or for the calling client when no ip is given.
* **Get Map Marker Icon** `getMapMarkerIcon`: Generates a PNG map marker image with the chosen shape, icon or text, colors and size, returned as a base64 file reference. Useful for building custom map pins.
* **Get Map Style** `getMapStyle`: Returns the MapLibre GL style JSON for a Geoapify map style, including its tile source, sprite and glyph URLs, for use in web and mobile map clients.
* **Get Map Tile** `getMapTile`: Downloads a single raster (PNG) or vector (PBF) map tile for a style at Slippy Map zoom, x and y coordinates, returned as a base64 file reference.
* **Get Place Details** `getPlaceDetails`: Retrieves details, geometry and optional related features (containing building, fixed-radius surroundings, walking or driving reach areas) for a place identified by a Geoapify place id, coordinates, or an OpenStreetMap id and type. Use only one lookup method.
* **Get Static Map** `getStaticMap`: Renders a static map image (JPEG or PNG) for a center and zoom or a bounding box, with optional markers, geometry overlays, GeoJSON and style customization. The image is returned as a base64 file reference.
* **List Postcodes** `listPostcodes`: Lists postcode areas matching free text within an optional spatial filter or bias, with pagination. Useful for postcode pickers and bulk postcode extraction for a region.
* **Match GPS Trace** `matchGpsTrace`: Snaps an ordered GPS trace of up to 1000 timestamped waypoints to the road network for a travel mode and returns the matched route with per-step road details. Input order is preserved; the API does not reorder points.
* **Perform Geometry Operation** `performGeometryOperation`: Analyzes or transforms GeoJSON geometries: buffers, unions, intersections, differences, distances, lengths, areas, centers, clustering, simplification, rotation, scaling, translation and spatial predicates. Supply the geometry inputs the chosen operation expects plus any operation-specific params.
* **Plan Routes** `planRoutes`: Solves a vehicle routing problem: assigns jobs and shipments to agents (vehicles or workers) honouring time windows, capacities and capability requirements, and returns an optimized route per agent. At least one job or shipment is required.
* **Render Static Map** `renderStaticMap`: Renders a static map image from a JSON request body, which supports richer marker, geometry and style-customization objects than the query-parameter form. Provide at least one of area, center, markers, geometries or geojson. The image is returned as a base64 file reference.
* **Reverse Geocode** `reverseGeocode`: Finds the nearest address or place for a latitude and longitude pair. Returns a GeoJSON FeatureCollection by default, or a results array when format is json.
* **Search Places** `searchPlaces`: Finds places and points of interest by category (for example commercial.supermarket or catering.restaurant) within a spatial filter and ranked by an optional bias, with optional attribute conditions, name matching and pagination.
* **Search Postcodes** `searchPostcodes`: Searches postcode areas by postcode text, or by latitude and longitude for a reverse postcode lookup. Use geometry=original to return the source postcode boundary instead of a centroid point.
* **Store Geometry** `storeGeometry`: Stores a GeoJSON geometry, Feature or FeatureCollection on Geoapify and returns its id, which can then be used in Places filters (geometry:id) and in Combine Geometries.
* **Submit Batch Geocode Job** `submitBatchGeocodeJob`: Submits up to 1000 free-form addresses for asynchronous forward geocoding and returns a job id to poll with Get Batch Geocode Job Result. The optional parameters apply to every address in the batch.
* **Submit Batch Job** `submitBatchJob`: Submits a generic batch job that runs any supported Geoapify API (geocoding, places, routing, isolines, boundaries and more) for up to 1000 inputs asynchronously, and returns a job id to poll with Get Batch Job Result.
* **Submit Batch Reverse Geocode Job** `submitBatchReverseGeocodeJob`: Submits up to 1000 coordinate pairs for asynchronous reverse geocoding and returns a job id to poll with Get Batch Reverse Geocode Job Result.

</details>
