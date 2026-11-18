---
description: "Mapulus is a location-intelligence platform for Australian geographies."
hidden: true
---

# Mapulus

<img src="../../.gitbook/assets/connectors/lg/mapulus.png" alt="Mapulus logo">

Mapulus is a location-intelligence platform for Australian geographies. This connector covers the Mapulus Studio API - maps, layers and the locations (pins, addresses, custom attributes and travel contours) that sit on them - together with the public service-health endpoints of the Mapulus Data API.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [mapulus.com](https://mapulus.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `mapulus` |

## Use it

Add Mapulus from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mapulus.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Lookup Boundaries | `searchBoundaries` | Resolves up to 100 locations to their containing statistical boundaries in one request. Each location is resolved independently and returned with the client-supplied identifier. Requires an API key with access to the Mapulus Data API. |
| Create Location | `createLocation` | Creates a location on a layer. Layer ID is required, and the location must carry either an address or a latitude and longitude. Set Create Or Update Custom Attributes to true when supplying custom attributes that do not yet exist on the layer, otherwise the request is rejected. |
| Create Targeting Job | `createTargetingJob` | Creates a background job that generates Meta Ads targeting circles for up to 20 boundaries regardless of their size. Returns the job to poll with Get Targeting Job, or the completed result immediately when it is already cached. Requires an API key with access to the Mapulus Data API. |
| Delete Location | `deleteLocation` | Permanently deletes a location from its layer. This cannot be undone. |
| Enrich Locations | `enrichLocations` | Batch-enriches up to 100 locations by resolving their containing boundaries and attaching datapack data (demographics or fundraising) for each one. Requires an API key with access to the Mapulus Data API. |
| Export Boundaries As GeoJSON | `exportBoundariesGeoJson` | Exports up to 500 specific boundaries by identifier as a GeoJSON FeatureCollection with geometry, bounding box, centroid and properties for each boundary. Requires an API key with access to the Mapulus Data API. |
| Export Boundary Type As GeoJSON | `exportBoundaryTypeGeoJson` | Downloads all boundaries of one type as a streamed GeoJSON FeatureCollection, optionally filtered by state, parent boundary, name or code prefix and simplified for mapping. Large types such as SA1 contain tens of thousands of features. Requires an API key with access to the Mapulus Data API. |
| Generate Meta Ads Targeting | `generateMetaTargeting` | Decomposes up to 20 statistical boundaries into inclusion and exclusion circles (or postcode targets) that approximate their shape for Meta Ads Manager location targeting. Results are cached by boundary hash; boundaries over 100 km2 are computed asynchronously and return a job to poll with Get Targeting Job. Requires an API key with access to the Mapulus Data API. |
| Get Account | `getAccount` | Returns the Mapulus account the API key belongs to. Useful as a connection check and to confirm which workspace the key addresses. |
| Get Boundary | `getBoundary` | Returns metadata for a single boundary by type and code. Requires an API key with access to the Mapulus Data API. |

<details>

<summary>See 24 more actions</summary>

* **Get Boundary GeoJSON** `getBoundaryGeoJson`: Downloads a single boundary as a GeoJSON Feature with full geometry. Simplification defaults to full (none) for single boundaries. Requires an API key with access to the Mapulus Data API.
* **Get Boundary Vector Tile** `getBoundaryVectorTile`: Returns a Mapbox Vector Tile (protobuf) of the boundary polygons of one layer that intersect the requested z/x/y tile, with boundary_id, name and state properties (plus flood_risk and flood_type for the flood layer). Empty tiles return 204 No Content. The tile is returned as a binary file. Requires an API key with access to the Mapulus Data API.
* **Get Data Service Health** `getDataServiceHealth`: Returns the current health and version of the Mapulus Data API, including database and cache latency and the state of the background sync daemon.
* **Get Demographic Field** `getDemographicField`: Returns detailed metadata for a single demographic field by its API path, including its unit, whether it is derived, and related fields. Requires an API key with access to the Mapulus Data API.
* **Get Incident** `getIncident`: Returns full detail for a single incident, including geometry, raw source data, structured location fields and the full description with impact details. Requires an API key with access to the Mapulus Data API.
* **Get Incident Summary** `getIncidentSummary`: Returns aggregated incident counts grouped by incident type, event type and event subtype for the same filters as List Incidents, plus an unfiltered catalogue of every known type combination for building filter menus. Requires an API key with access to the Mapulus Data API.
* **Get Location** `getLocation`: Retrieves a single location by its identifier, including its coordinates, address, contact details and custom attributes.
* **Get Map** `getMap`: Retrieves a single map by its identifier. Set Expand to 'layer' to include the map's layers, their location counts and their custom attributes.
* **Get Sync Source Health** `getSyncSourceHealth`: Returns the health of the Mapulus data-sync daemon. Supply Source to check a single upstream feed, such as 'qld_traffic'; omit it to get every source with a top-level aggregate status.
* **Get Targeting Job** `getTargetingJob`: Polls the status of a Meta Ads targeting job and returns the targeting circles once it has completed. Jobs are account-scoped. Requires an API key with access to the Mapulus Data API.
* **List Boundaries** `listBoundaries`: Lists all boundaries of one type, paginated. Use Contained By for spatial questions such as which SA1s fall inside postcode 2000, Search to match boundary names, or Code Prefix to match codes. Requires an API key with access to the Mapulus Data API.
* **List Boundary Types** `listBoundaryTypes`: Lists every supported boundary type grouped by country (20 Australian and 20 US geographies), with type codes, human-readable labels and country codes. Requires an API key with access to the Mapulus Data API.
* **List Demographic Topics** `listDemographicTopics`: Lists the available demographic topics, such as summary, age, income, housing and employment, plus the Indigenous Profile topics available at ILOC, IARE and IREG geographies. Topic IDs are used with the Topics parameter of Query Demographics. Requires an API key with access to the Mapulus Data API.
* **List Derived Fields** `listDerivedFields`: Lists the derived percentage fields computed at query time from raw census data (population shares, age brackets, motor vehicles, dwelling structure and more). Use them with the Fields parameter of Query Demographics, for example derived.pct_indigenous. Requires an API key with access to the Mapulus Data API.
* **List Incident Sources** `listIncidentSources`: Lists the government and utility data feeds that incidents are synced from, such as QLD Traffic, QFD Fire, Energex/Ergon outages and BOM Weather, with their sync status. Requires an API key with access to the Mapulus Data API.
* **List Incidents** `listIncidents`: Lists real-time traffic, fire, power-outage and weather incidents with hierarchical type filters, status, state, severity, source, boundary intersection, radius search and time range. Radius searches sort closest-first and include the distance to each incident. Requires an API key with access to the Mapulus Data API.
* **List Locations** `listLocations`: Lists locations in the Mapulus account, paginated. Filter by map, layer or external identifier, or use the nearest-search parameters to return up to the 24 closest locations to a point or address, ranked by travel time or distance for a driving, cycling or walking profile.
* **List Maps** `listMaps`: Lists every map in the Mapulus account, paginated. Set Expand to 'layer' to include each map's layers, their location counts and their custom attributes.
* **Lookup Boundaries By Point** `lookupBoundaries`: Resolves a latitude and longitude to every statistical boundary that contains it (SA1-SA4, LGA, postcode, suburb and more), plus H3 grid indices at resolutions 3-9 and any matching planning regions. Requires an API key with access to the Mapulus Data API.
* **Query Demographics** `queryDemographics`: Queries ABS Census demographics for a point (latitude and longitude), one or more boundary identifiers, or a whole boundary type in browse mode. Choose data with Topics or Fields, aggregate across boundaries, filter and sort in browse mode, or add a sex and age segment. Requires an API key with access to the Mapulus Data API.
* **Query Demographics By Polygon** `queryDemographicsByPolygon`: Queries ABS Census demographics for the boundaries that intersect a GeoJSON Polygon or MultiPolygon, returning either each boundary with its overlap fraction or area-weighted aggregated statistics. Sex and age segment filters are not supported for polygon queries. Requires an API key with access to the Mapulus Data API.
* **Search Demographic Fields** `searchDemographicFields`: Browses and searches the catalogue of 13,498 census fields across 25 topics. Filter by topic or search field names and labels, paginated. Requires an API key with access to the Mapulus Data API.
* **Search Incidents By Polygon** `searchIncidents`: Searches for incidents intersecting a GeoJSON Polygon or MultiPolygon, with optional type, status, severity, source, state and time-range filters. Results default to closest-first from the polygon centroid and include the distance to each incident. Requires an API key with access to the Mapulus Data API.
* **Update Location** `updateLocation`: Updates an existing location. Only the fields you supply are sent, so omitted fields keep their current values. The location must retain either an address or a latitude and longitude. Supplying a different Layer ID moves the location to that layer.

</details>
