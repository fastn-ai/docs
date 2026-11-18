---
description: "Felt is a collaborative web mapping platform."
hidden: true
---

# Felt

<img src="../../.gitbook/assets/connectors/felt.png" alt="Felt logo" width="64">

Felt is a collaborative web mapping platform. This connector covers the Felt REST API v2: maps (create, read, update, move, duplicate, delete, image export, embed tokens), map layers (upload, add from source, style, publish, refresh, export, duplicate, delete), layer components, layer groups, elements and element groups, comments, projects, data sources and source credentials, the layer library, and the current user.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [felt.com](https://felt.com) |
| **Authentication** | Bearer token |
| **Slug** | `felt` |

## Use it

Add Felt from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.felt.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Layer From Source | `addMapLayerFromSource` | Creates a layer on a map from an existing connected data source: a catalogued dataset, a SQL query against a database source, or a STAC asset. |
| Check Custom Export Status | `pollMapLayerCustomExport` | Returns the processing status of a custom layer export and, once completed, the download URL for the exported file. |
| Create Custom Layer Export | `createMapLayerCustomExport` | Starts an asynchronous export of a layer in a chosen format, optionally restricted by Felt Style Language filters. Poll the returned export_request_id with Check Custom Export Status. |
| Create Layer Component | `createLayerComponent` | Adds a component to a layer - a statistic, histogram, line chart, bar chart, time series or filter that appears in the map legend. |
| Create Layer Export Link | `createMapLayerExportLink` | Returns a direct download link for a layer's data - a GeoPackage for vector layers or a GeoTIFF for raster layers. |
| Create Map | `createMap` | Creates a new Felt map, optionally with a title, description, basemap, initial viewport, sharing level and raster tile layers imported from URLs. |
| Create Map Embed Token | `createMapEmbedToken` | Creates a 12-hour token that lets a named end user view a private embedded map without logging in to Felt. The email must belong to a workspace member. |
| Create Or Update Map Element Groups | `upsertMapElementGroups` | Creates or updates element groups on a map. Felt expects a raw JSON array as the request body, so element_groups is passed as a JSON-array string and emitted verbatim. An element without an id creates a new group. |
| Create Or Update Map Elements | `upsertMapElements` | Creates or updates annotation elements on a map from a GeoJSON FeatureCollection. A feature whose properties carry felt:id updates that element; a feature without one creates a new element. felt:parentId places the element in an element group. Note: Felt's own OpenAPI document places felt:id inside geometry, but the live API returns and accepts it under properties. |
| Create Project | `createProject` | Creates a project in the workspace with the given name and visibility. |

<details>

<summary>See 47 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Source | `createSource` | Connects a new data source to the workspace. Connecting and cataloguing the datasets happens asynchronously after the response - poll Get Source for sync_status. |
| Create Source Credential | `createSourceCredential` | Adds an authentication credential to an existing data source, for example an S3 key pair or a STAC API token. Secret fields are returned as felt:redacted. |
| Delete Layer Component | `deleteLayerComponent` | Permanently removes a component from a layer. |
| Delete Map | `deleteMap` | Permanently deletes a map and all of its layers, elements and comments. This cannot be undone. |
| Delete Map Comment | `deleteMapComment` | Permanently deletes a comment or reply from a map. This cannot be undone. |
| Delete Map Element | `deleteMapElement` | Permanently deletes a single annotation element from a map. |
| Delete Map Layer | `deleteMapLayer` | Permanently removes a layer and all of its data from a map. This cannot be undone. |
| Delete Map Layer Group | `deleteMapLayerGroup` | Permanently deletes a layer group from a map. |
| Delete Project | `deleteProject` | Permanently deletes a project together with every folder and map inside it. This cannot be undone. |
| Delete Source | `deleteSource` | Permanently deletes a data source connection. Layers already created from it remain on their maps but stop refreshing. |
| Delete Source Credential | `deleteSourceCredential` | Removes an authentication credential from a data source. |
| Duplicate Map | `duplicateMap` | Creates a copy of a map including all of its layers, elements and configuration, optionally under a new title and in a different project or folder. |
| Duplicate Map Layers | `duplicateMapLayers` | Copies layers or layer groups onto other maps, keeping their styling and configuration. Also the way to add a library layer to a map. Felt expects a raw JSON array as the request body, so duplications is passed as a JSON-array string and emitted verbatim. |
| Export Map As Image | `createMapImageExport` | Renders the map to a PNG, JPG or PDF at a chosen size and view, the same output as the app's Export as image. The call blocks for up to 55 seconds and returns a completed export with a download_url valid until expires_at. |
| Export Map Comments | `exportMapComments` | Exports every comment thread and reply on a map as JSON (default), CSV or GeoJSON. |
| Get Current User | `showCurrentUser` | Returns the profile of the Felt user that owns the API token: id, name and email. |
| Get Layer Component | `showLayerComponent` | Returns a single component attached to a layer. |
| Get Map | `showMap` | Returns a map with its basemap, viewport-independent metadata, sharing settings, layers, layer groups, elements and element groups. |
| Get Map Element Group | `showMapElementGroup` | Returns the elements inside a single element group as a GeoJSON FeatureCollection. Each feature carries felt:id - and felt:parentId - inside its properties object (Felt's own OpenAPI document places them under geometry, but the live API returns them under properties). |
| Get Map Layer | `showMapLayer` | Returns a single layer on a map with its attributes, metadata, refresh schedule and Felt Style Language style. |
| Get Map Layer Group | `showMapLayerGroup` | Returns a single layer group on a map with the layers it contains. |
| Get Project | `showProject` | Returns a single project with its metadata, permission settings and references to every map inside it. |
| Get Source | `showSource` | Returns a connected data source with its connection settings, permissions, sync status and catalogued datasets. |
| List Layer Components | `listLayerComponents` | Lists the components attached to a layer - statistics, histograms, line charts, bar charts, time series and filters shown in the map legend. |
| List Library Layers | `listLibraryLayers` | Lists the layers and layer groups in the workspace library, the Felt public data library, or both. Layer ids returned here can be copied onto a map with Duplicate Map Layers. |
| List Map Element Groups | `listMapElementGroups` | Lists the element groups on a map with their colour, symbol and the elements inside each one. |
| List Map Elements | `listMapElements` | Returns all annotation elements drawn on a map as a GeoJSON FeatureCollection. Each feature carries felt:id - and felt:parentId when grouped - inside its properties object (Felt's own OpenAPI document places them under geometry, but the live API returns them under properties). |
| List Map Layer Groups | `listMapLayerGroups` | Lists the layer groups on a map together with the layers inside each one. |
| List Map Layers | `listMapLayers` | Lists every layer on a map, whether uploaded, imported from a URL or backed by a connected data source. |
| List Projects | `listProjects` | Lists every project in the workspace that the authenticated user can access. |
| List Sources | `listSources` | Lists the connected data sources in the workspace - databases, warehouses, object stores and OGC/STAC services - with their sync status. |
| Move Map | `moveMap` | Moves a map into a different project or folder in the same workspace. Supply exactly one of project_id or folder_id. |
| Publish Map Layer | `publishMapLayer` | Publishes a layer into the workspace library so team members can reuse it on other maps. |
| Publish Map Layer Group | `publishMapLayerGroup` | Publishes a layer group and its layers into the workspace library for reuse on other maps. |
| Refresh Map Layer | `refreshMapLayer` | Triggers a data refresh for a layer from its original source. For URL-backed layers this single call is enough; for file-backed layers the response returns a presigned Amazon S3 url and presigned_attributes for uploading the replacement file. |
| Resolve Map Comment | `resolveMapComment` | Marks a comment thread on a map as resolved. |
| Sync Source | `syncSource` | Triggers a full re-sync of a data source so its catalogued datasets and connected layers pick up the latest data. The sync runs asynchronously - poll Get Source for sync_status. |
| Update Layer Component | `updateLayerComponent` | Updates a layer component's title, computation or configuration. Keys supplied in config are merged; data is replaced as a unit. |
| Update Layer Style | `updateMapLayerStyle` | Replaces a layer's visual style with a new Felt Style Language document, controlling colours, symbols and rendering. |
| Update Map | `updateMap` | Updates a map's title, legend description, basemap, public access level, data-table settings and viewer permissions. |
| Update Map Layer Group | `updateMapLayerGroup` | Updates a single layer group's name, caption, legend behaviour and ordering. |
| Update Map Layer Groups | `updateMapLayerGroups` | Creates or updates several layer groups on a map in one call. Felt expects a raw JSON array as the request body, so layer_groups is passed as a JSON-array string and emitted verbatim. An element without an id creates a new group. |
| Update Map Layers | `updateMapLayer` | Updates one or more layers on a map - name, caption, metadata, legend behaviour, ordering, layer group membership and refresh period. Felt expects a raw JSON array as the request body, so layers is passed as a JSON-array string and emitted verbatim. |
| Update Project | `updateProject` | Updates a project's name, visibility or inherited-permission level. |
| Update Source | `updateSource` | Updates a source's name, connection settings or permissions. Reconnecting and re-cataloguing happen asynchronously after the response. |
| Update Source Credential | `updateSourceCredential` | Updates an existing source credential's name, use case or secret material. Secret fields are returned as felt:redacted. |
| Upload Map Layer | `uploadMapLayer` | Starts creating a new layer on a map, either by importing a public URL (import_url - one call is enough) or by uploading a file. For file uploads the response returns a presigned Amazon S3 url plus presigned_attributes that must be POSTed as multipart form data to finish the upload. |

</details>
