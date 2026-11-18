---
description: "TomTom location services."
hidden: true
---

# TomTom

<img src="../../.gitbook/assets/connectors/lg/tomtom.png" alt="TomTom logo">

TomTom location services. This connector covers the TomTom Maps REST APIs on api.tomtom.com: fuzzy, POI, category, geometry, nearby, along-route and routed search, autocomplete, place by ID, POI categories and additional data, geocoding and reverse geocoding, batch search, route and reachable-range calculation, batch and matrix routing, traffic incident details, viewport and flow data with traffic tiles, plus the Geofencing (projects, fences, objects, transitions, reports, alert rules, archives), Location History and Notifications (contact groups, history) services.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [tomtom.com](https://tomtom.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `tomtom` |

## Use it

Add TomTom from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.tomtom.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Along Route Search | `alongRouteSearch` | Searches for points of interest along a route given as a list of points, limited by the maximum detour time, and returns detour time, distance and offset for each result. |
| Archive Geofencing Structure | `archiveGeofencingStructure` | Requests an archive of the Geofencing configuration, projects, fences and objects and returns a token for Download Geofencing Archive. Requires the Admin Key. |
| Archive Geofencing Transitions | `archiveGeofencingTransitions` | Requests an archive of all stored fence transitions and returns a token for Download Geofencing Archive. Requires the Admin Key. |
| Archive Position History | `archivePositionHistory` | Requests an archive of all stored object positions and returns a token for Download Location History Archive. Requires the Admin Key. |
| Autocomplete | `autocomplete` | Recognizes entities such as brands, categories and plain text inside a partial query and returns them as segments that can be used to build a more precise search. |
| Batch Routing | `batchRoutingSync` | Runs up to 100 Calculate Route or Calculate Reachable Range requests synchronously in one call and returns each item's status code and response. Times out with 408 if processing exceeds 60 seconds. |
| Batch Search | `batchSearchSync` | Runs up to 100 Search API requests (fuzzy, POI, category, geocode, reverse geocode, nearby, geometry and along-route search) synchronously in one call and returns each item's status code and response. |
| Calculate Matrix | `calculateMatrix` | Synchronously calculates route summaries (distance, travel time, traffic delay) for every origin and destination pair, for matrices of up to 100 cells (200 with historical traffic settings). |
| Calculate Reachable Range | `calculateReachableRange` | Calculates the polygon of locations reachable from an origin within a time, distance, fuel or energy budget, using the given travel mode, vehicle and consumption model. |
| Calculate Reachable Range With Constraints | `calculateReachableRangePost` | Calculates the area reachable from an origin within a time, distance, fuel or energy budget, with request-body constraints such as areas to avoid and vignette restrictions. |
| Calculate Route | `calculateRoute` | Calculates a route between an origin and destination through optional waypoints, returning distance, travel time, traffic delay, route geometry, guidance instructions and alternatives. Supports car, truck, bicycle and pedestrian modes plus vehicle dimensions and consumption models. |
| Calculate Route With Constraints | `calculateRoutePost` | Calculates a route using request-body options that the GET form cannot carry: supporting points to reconstruct a known route, rectangular areas to avoid, and vignette country restrictions. |
| Category Search | `categorySearch` | Searches points of interest by category name, such as parking or petrol station, with optional position bias, area restriction and POI filters. |
| Change Geofencing Secret | `changeGeofencingSecret` | Replaces the registered Geofencing secret with a new one, authenticated by the old secret. |
| Change Location History Secret | `changeLocationHistorySecret` | Replaces the registered Location History secret with a new one, authenticated by the old secret. |
| Clear Alert History | `clearAlertHistory` | Deletes stored Geofencing alert history for one alert type or all types. The deletion runs asynchronously. Requires the Admin Key. |
| Clear Notifications History | `clearNotificationsHistory` | Deletes the history of sent notifications. The deletion runs asynchronously; the response reports the cut-off timestamp and processing status. |
| Clear Position History | `clearPositionHistory` | Deletes all stored object position history. The deletion runs asynchronously and the response reports the cut-off and status. Requires the Admin Key. |
| Clear Transitions History | `clearTransitionsHistory` | Deletes all stored fence transition history. The deletion runs asynchronously and the response reports the cut-off and status. Requires the Admin Key. |
| Create Alert Rule | `createAlertRule` | Creates a Geofencing alert rule that sends a notification to a contact group when an object enters or exits a fence (TRANSITION), dwells too long (DWELL), a fence holds too many objects (OBJECT_COUNT) or an object comes within a distance of a fence (PROXIMITY). Use * for any project, fence or object. Requires the Admin Key. |
| Create Contact Group | `createContactGroup` | Creates a Notifications API contact group of webhook URLs and email addresses that receive geofencing alerts. Use the returned group ID as the notification group of alert rules. |
| Create Fence | `createFence` | Creates a geofence and assigns it to one or more projects at once. Requires the Admin Key. |
| Create Fence In Project | `createFenceInProject` | Creates a geofence and links it to a single project. The geometry is a GeoJSON geometry or a custom shape (Circle, Rectangle, Polygon, Corridor) with shapeType. Requires the Admin Key. |
| Create Geofencing Object | `createGeofencingObject` | Creates a Geofencing object (a tracked vehicle, device or asset) with an optional default project and free-form properties. Requires the Admin Key. |
| Create Geofencing Project | `createGeofencingProject` | Creates a Geofencing project, the container that fences and objects are assigned to. Requires the Admin Key. |
| Create Location History Object | `createLocationHistoryObject` | Creates a Location History object (a tracked vehicle, device or asset) with free-form properties. Requires the Admin Key. |
| Cross Street Lookup | `crossStreetLookup` | Finds the nearest cross streets (intersections) to a set of coordinates. |
| Delete Alert Rule | `deleteAlertRule` | Deletes a Geofencing alert rule and returns its last definition. Requires the Admin Key. |
| Delete Contact Group | `deleteContactGroup` | Deletes a Notifications API contact group by ID and returns the deleted group. |
| Delete Fence | `deleteFence` | Deletes a geofence from all projects and reports the affected projects. Use dry run to preview. Requires the Admin Key. |
| Delete Geofencing Object | `deleteGeofencingObject` | Deletes a Geofencing object. Requires the Admin Key. |
| Delete Geofencing Project | `deleteGeofencingProject` | Deletes a Geofencing project. Fences that exist only in this project are deleted too; fences shared with other projects and objects using it as default project are unlinked. Use dry run to preview the cascade. Requires the Admin Key. |
| Delete Location History Object | `deleteLocationHistoryObject` | Deletes a Location History object. Requires the Admin Key. |
| Download Batch Routing Results | `batchRoutingAsyncDownload` | Downloads the results of an asynchronous batch routing job. Long-polls up to the wait time and returns 202 while processing, then 200 with each item's status code and response. |
| Download Batch Search Results | `batchSearchAsyncDownload` | Downloads the results of an asynchronous batch search job. Long-polls up to the wait time and returns 202 while processing, then 200 with each item's status code and response. |
| Download Geofencing Archive | `downloadGeofencingArchive` | Downloads a prepared Geofencing archive by token as a compressed file. Requires the Admin Key. |
| Download Location History Archive | `downloadLocationHistoryArchive` | Downloads a prepared Location History archive by token as a compressed file. Requires the Admin Key. |
| Fuzzy Search | `fuzzySearch` | Searches addresses, streets, geographies and points of interest with a single free-text query, tolerating typos and partial input. Supports position bias, area restriction and POI filters. |
| Geocode Address | `geocode` | Converts a free-text address or place name into coordinates and a structured address, with optional country, position and area restrictions. |
| Geometry Filter | `geometryFilter` | Filters a list of points of interest, supplied as JSON query parameters, down to those located inside the given circles or polygons. |
| Geometry Filter With Body | `geometryFilterPost` | Filters a list of points of interest sent in the request body down to those located inside the given circles or polygons. |
| Geometry Search | `geometrySearch` | Searches for places matching a query inside one or more circles or polygons supplied as a JSON string query parameter. Use Geometry Search With Body for large geometries. |
| Geometry Search With Body | `geometrySearchPost` | Searches for places matching a query inside one or more circles or polygons sent in the request body, suitable for large or complex geometries. |
| Get Additional Data | `getAdditionalData` | Retrieves GeoJSON geometry outlines for geographies such as countries, cities or postal areas, using geometry IDs returned in the dataSources of search results. |
| Get Alert Rule | `getAlertRule` | Retrieves a Geofencing alert rule with its scope, type, constraints, notification group and enabled state. |
| Get Contact Group | `getContactGroup` | Retrieves a Notifications API contact group with its webhook URLs and email addresses. |
| Get Fence | `getFence` | Retrieves a geofence with its geometry and properties. |
| Get Fence Transitions | `getFenceTransitions` | Lists the enter and leave transitions of all objects for one fence in a time window of at most 24 hours. |
| Get Geofencing Object | `getGeofencingObject` | Retrieves a Geofencing object with its default project and properties. |
| Get Geofencing Project | `getGeofencingProject` | Retrieves a Geofencing project with its fences and, optionally, the objects that use it as their default project. |
| Get Geofencing Report | `getGeofencingReport` | Reports which fences of a project a position is inside of and which nearby fences it is outside of, sorted by distance. If no project is given, the object's default project is used. Does not record the position. |
| Get Geofencing Settings | `getGeofencingSettings` | Retrieves the Geofencing account limits (maximum objects, projects, fences and vertices) and privacy settings such as consent for storing position and transition history. Requires the Admin Key. |
| Get Last Position | `getLastPosition` | Retrieves the most recent recorded position of a Location History object with estimated speed and direction. |
| Get Location History Object | `getLocationHistoryObject` | Retrieves a Location History object with its properties. |
| Get Location History Settings | `getLocationHistorySettings` | Retrieves the Location History account limit and privacy settings, including consent for storing positions. Requires the Admin Key. |
| Get Matrix Job Result | `getMatrixJobResult` | Downloads the route summaries of a completed asynchronous matrix job. Returns 404 while the job is not yet Completed. |
| Get Matrix Job Status | `getMatrixJobStatus` | Retrieves the state of an asynchronous matrix job (Submitted, Validated, Completed or Failed) with success and failure statistics or validation errors. |
| Get Notifications Settings | `getNotificationsSettings` | Retrieves the Notifications API privacy settings, including the status of any pending history deletion. |
| Get Object Transitions | `getObjectTransitions` | Lists the fence enter and leave transitions of one object in a time window of at most 24 hours, optionally limited to given projects. |
| Get Place By ID | `getPlaceById` | Retrieves full details of a POI, street, geography, point address, address range or cross street by its entity ID, including address, position, opening hours and related POIs. |
| Get Position History | `getPositionHistory` | Lists the recorded positions of a Location History object in a time window of at most 24 hours, with estimated speed and direction for each. |
| Get Project Transitions | `getProjectTransitions` | Lists the enter and leave transitions for all fences of a project in a time window of at most 24 hours. |
| Get Traffic Flow Raster Tile | `getTrafficFlowRasterTile` | Returns a transparent PNG map tile coloring roads by absolute or relative traffic speed for a zoom level and tile grid position. The response is a binary image file. |
| Get Traffic Flow Segment Data | `getTrafficFlowSegmentData` | Returns current speed, free-flow speed, travel times, confidence and closure status for the road segment closest to a coordinate, with the segment geometry. |
| Get Traffic Flow Vector Tile | `getTrafficFlowVectorTile` | Returns a Mapbox Vector Tile (protobuf) with traffic flow geometries and tags such as traffic level and road type for a zoom level and tile grid position. The response is a binary file. |
| Get Traffic Incident Details | `getTrafficIncidentDetails` | Lists current or future traffic incidents such as jams, accidents, closures and roadworks inside a bounding box or for given incident IDs, with geometry, delay, magnitude, road numbers and event descriptions. |
| Get Traffic Incident Details By IDs | `getTrafficIncidentDetailsByIds` | Retrieves details of many traffic incidents at once by sending their IDs in the request body, avoiding URL length limits. |
| Get Traffic Incident Raster Tile | `getTrafficIncidentRasterTile` | Returns a transparent PNG or GIF map tile rendering traffic incidents for a zoom level and tile grid position, for overlay on a base map. The response is a binary image file. |
| Get Traffic Incident Vector Tile | `getTrafficIncidentVectorTile` | Returns a Mapbox Vector Tile (protobuf) with traffic incident geometries and tags for a zoom level and tile grid position. The response is a binary file. |
| Get Traffic Incident Viewport | `getTrafficIncidentViewport` | Returns the current Traffic Model ID, traffic data age and copyright information for a map viewport and overview map given in EPSG:900913 coordinates. |
| List Alert History | `listAlertHistory` | Lists Geofencing alerts triggered in a time window, optionally filtered by alert type. |
| List Alert Rules | `listAlertRules` | Lists Geofencing alert rules, optionally filtered by project, fence, object, alert type, enabled state or notification group. |
| List Contact Groups | `listContactGroups` | Lists the Notifications API contact groups of the account with their IDs and names, paginated. |
| List Geofencing Objects | `listGeofencingObjects` | Lists all Geofencing objects of the configuration with their IDs and names. |
| List Geofencing Projects | `listGeofencingProjects` | Lists all Geofencing projects of the configuration with their IDs and names. |
| List Location History Objects | `listLocationHistoryObjects` | Lists all Location History objects with their IDs and names. |
| List Notifications History | `listNotificationsHistory` | Lists notifications sent to contact groups in a time window of at most 24 hours (history is kept for 7 days), newest first, with the contact, delivery status, send date and source of each. |
| List Objects In Fence | `listObjectsInFence` | Lists the objects currently inside a geofence, optionally filtered by an object property, with the total count. |
| List POI Categories | `listPoiCategories` | Lists all point of interest categories with their IDs, names, synonyms and child categories, for use in the categorySet filter of search actions. |
| List Project Fences | `listProjectFences` | Lists the fences of a Geofencing project with their IDs and names. |
| Nearby Search | `nearbySearch` | Lists points of interest around a position without a text query, optionally filtered by category, brand, fuel type or EV connector. |
| Patch Contact Group | `patchContactGroup` | Partially updates a Notifications API contact group, changing only the name, webhook URLs or email addresses that are supplied. |
| Premium Geocode | `premiumGeocode` | Geocodes a free-text address with premium address data, including unit-level details where available. Requires an API key entitled to Premium Geocoding. |
| Record Position And Get Report | `recordGeofencingReport` | Records an object's position, detects and stores fence transitions (which trigger alert rules) and returns the same inside/outside fence report as Get Geofencing Report. Requires consent for storing positions and transitions. |
| Regenerate Geofencing Admin Key | `regenerateGeofencingAdminKey` | Generates a new Geofencing Admin Key using the registered secret and revokes the previous key. Update the connection's Admin Key afterwards. |
| Regenerate Location History Admin Key | `regenerateLocationHistoryAdminKey` | Generates a new Location History Admin Key using the registered secret and revokes the previous key. Update the connection's Admin Key afterwards. |
| Register Geofencing Admin Key | `registerGeofencingAdminKey` | Registers the API key's Geofencing and Location History configuration with a secret (10 to 30 characters) and returns the Admin Key needed for all write operations. Each API key can register only once; a second call returns 403. Note: TomTom will decommission the Geofencing API on 31 January 2027. |
| Register Location History Admin Key | `registerLocationHistoryAdminKey` | Registers the API key's Location History configuration with a secret and returns the Admin Key. The configuration is shared with Geofencing, so a key already registered there returns 403. |
| Remove Fence From Project | `removeFenceFromProject` | Unlinks a geofence from one project. If that was the fence's only project, the fence is deleted permanently. Use dry run to preview. Requires the Admin Key. |
| Reverse Geocode | `reverseGeocode` | Converts coordinates into the nearest human-readable street address, optionally including speed limit, road class, road use and match type. |
| Search Points Of Interest | `poiSearch` | Searches points of interest by name or brand, such as restaurants, shops or attractions, with optional position bias, area restriction and POI filters. |
| Send Position | `sendPosition` | Records a GeoJSON Point position for a Location History object. Requires consent for storing positions; each timestamp must be later than the object's last recorded position. Returns 201 with an empty body. |
| Structured Geocode | `structuredGeocode` | Converts an address supplied as separate components, such as street, number, city and postal code, into coordinates and a structured address. |
| Submit Batch Routing Job | `batchRoutingAsyncSubmit` | Submits up to 700 routing requests for asynchronous processing. With redirect mode manual the service answers 202 Accepted and the batch ID is in the Location response header; use Download Batch Routing Results with that ID. |
| Submit Batch Search Job | `batchSearchAsyncSubmit` | Submits up to 10,000 Search API requests for asynchronous processing. With redirect mode manual the service answers 202 Accepted and the batch ID is in the Location response header; use Download Batch Search Results with that ID. |
| Submit Matrix Job | `submitMatrixJob` | Submits a large origin-destination matrix (up to 2500 cells) for asynchronous calculation and returns a job ID to check with Get Matrix Job Status and download with Get Matrix Job Result. |
| Update Alert Rule | `updateAlertRule` | Enables or disables a Geofencing alert rule. Requires the Admin Key. |
| Update Contact Group | `updateContactGroup` | Replaces the name, webhook URLs and email addresses of a Notifications API contact group. |
| Update Fence | `updateFence` | Updates a geofence. Only supplied fields change; projects replaces the full project list, geometry must be sent as a whole block, and properties replaces all existing properties. Requires the Admin Key. |
| Update Geofencing Object | `updateGeofencingObject` | Updates a Geofencing object's name, default project or properties; only supplied fields change. Requires the Admin Key. |
| Update Geofencing Project | `updateGeofencingProject` | Renames a Geofencing project. Requires the Admin Key. |
| Update Geofencing Settings | `updateGeofencingSettings` | Sets the Geofencing privacy consents for storing object position history and transition history. Both consents are required before positions and transitions are recorded. Requires the Admin Key. |
| Update Location History Object | `updateLocationHistoryObject` | Updates a Location History object's name or properties; only supplied fields change. Requires the Admin Key. |
| Update Location History Settings | `updateLocationHistorySettings` | Sets consent for storing object position history, which is required before Send Position works. Requires the Admin Key. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Dwell Alert | `DWELL` | An object stayed inside a fence longer than the rule's maxDwellTime and a DWELL alert rule fired. Same subscription flow as TRANSITION; create the alert rule with alertType DWELL and the returned contact group. Payload modelled from the documented Notifications alert format and the captured TRANSITION delivery (title, body, contextData with eventType DWELL); dwell-specific contextData fields are as documented by TomTom. |
| Fence Transition Alert | `TRANSITION` | A tracked object entered or exited a geofence and a TRANSITION alert rule fired. Subscribing creates a TomTom Notifications contact group whose webhook URL is this trigger; then create an alert rule (Create Alert Rule, alertType TRANSITION) that names the returned contact group as notificationGroup. TomTom POSTs unsigned JSON with title, body and contextData; contextData.eventType carries the alert type. Payload schema captured from real deliveries on 2026-09-15. |
| Object Count Alert | `OBJECT_COUNT` | The number of objects inside a fence exceeded the rule's maxObjectCount and an OBJECT_COUNT alert rule fired. Same subscription flow; create the alert rule with alertType OBJECT_COUNT. Payload modelled from docs and the captured alert format. |
| Proximity Alert | `PROXIMITY` | An object came within the rule's proximityDistance of a fence (inside or outside) and a PROXIMITY alert rule fired. Same subscription flow; create the alert rule with alertType PROXIMITY. Payload modelled from docs and the captured alert format. |
