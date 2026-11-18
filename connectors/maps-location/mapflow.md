---
description: "Mapflow is an AI mapping platform that extracts buildings, roads, forests and other features from satellite and aerial imagery."
hidden: true
---

# Mapflow

Mapflow is an AI mapping platform that extracts buildings, roads, forests and other features from satellite and aerial imagery. This connector covers the Mapflow Processing API and Data API: projects, processings and their results, cost estimation, processing history, custom imagery mosaics and images, storage usage, the satellite imagery catalog and account status.

| | |
| --- | --- |
| **Category** | [Maps and location](README.md) |
| **Website** | [mapflow.ai](https://mapflow.ai) |
| **Authentication** | Basic auth |
| **Actions** | 30 |
| **Events** | 0 |
| **Slug** | `mapflow` |

## Use it

Add Mapflow from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.mapflow.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Calculate Processing Cost | `calculateProcessingCost` | Estimates what a processing will cost in Mapflow credits before it is run. Supply the workflow definition and either an area of interest geometry or an area in square kilometres. Returns the estimated cost as a number. |
| Create Mosaic | `createMosaic` | Creates an empty imagery mosaic that georeferenced images can then be uploaded or linked into. |
| Create Processing | `createProcessing` | Creates and immediately runs an AI mapping processing over an area of interest. Choose the model with wdName or wdId and the imagery with params.sourceParams. This consumes Mapflow credits; use Calculate Processing Cost first. |
| Create Project | `createProject` | Creates a project, the container that organises Mapflow processings. Returns the new project including the identifier used when creating processings. |
| Delete Image | `deleteImage` | Deletes an uploaded image from Mapflow storage, freeing the space it occupied. |
| Delete Mosaic | `deleteMosaic` | Deletes a mosaic and every image linked to it. This is irreversible and frees the storage the images used. |
| Delete Processing | `deleteProcessing` | Deletes a processing and every child entity it owns, including its areas of interest and results. Credits already spent are not refunded. |
| Delete Project | `deleteProject` | Deletes a project by its identifier. Processings that belong to the project are removed with it, so confirm the project is empty before calling this. |
| Download Processing Results | `downloadProcessingResults` | Downloads a finished processing's results as a GeoJSON file. Optionally filter the output to a single area of interest by passing its identifier. The engine returns the file as a reference whose data is the base64-encoded GeoJSON FeatureCollection. |
| Get Default Project | `getDefaultProject` | Retrieves the account's default project, the container Mapflow uses for processings that are not assigned to a project of their own. |
| Get Image | `getImage` | Retrieves detailed metadata for one uploaded image, including its raster properties, footprint and cloud-optimised GeoTIFF link. |
| Get Image Preview | `getImagePreview` | Retrieves a JPEG thumbnail of an uploaded image, either small (256 x 256) or large (1024 x 1024). The image is returned as a file reference. |
| Get Mosaic | `getMosaic` | Retrieves one imagery mosaic by its identifier, with its tags, combined footprint, stored size, tile layer URLs and a per-status summary of the images it contains. |
| Get Processing | `getProcessing` | Retrieves one processing by its identifier, including its current status, percentage complete, model, imagery source parameters and cost. Poll this to follow a running job. |
| Get Processing History | `getProcessingHistory` | Returns the account's processing history with pagination, sorting and filtering, for usage reporting and billing reconciliation. |
| Get Project | `getProject` | Retrieves a single project by its identifier, including its processing progress summary and area of interest count. |
| Get Storage Usage | `getStorageUsage` | Returns the account's imagery storage usage and limits, including the maximum upload file size and pixel count Mapflow will accept. |
| Get User Status | `getUserStatus` | Retrieves the authenticated Mapflow account's status, including remaining credits and processing area, account limits, the AI models and workflow definitions available to the account, team membership and linked data providers. |
| Link Image To Mosaic | `linkImageToMosaic` | Links an image that already sits in S3 to a mosaic by its URL, without uploading the file through Mapflow. |
| List Mosaic Images | `listMosaicImages` | Lists the images inside a mosaic with their file metadata, footprint and preview links. |
| List Mosaics | `listMosaics` | Lists the imagery mosaics in the account, each one a collection of georeferenced images that can be used as a processing source. |
| List Processings | `listProcessings` | Lists every processing in the account with its status, model, area of interest and cost. |
| List Project Processings | `listProjectProcessings` | Lists the processings that belong to one project, with status, model and cost for each. |
| List Projects | `listProjects` | Lists every project in the Mapflow account, with each project's processing progress summary, area of interest count and creation date. |
| Restart Processing | `restartProcessing` | Restarts a processing, re-running only the partitions that failed. Successful partitions are kept, so no credits are spent on work already completed. |
| Search Imagery Catalog | `searchImageryCatalog` | Searches satellite imagery from the commercial providers linked to the account, filtered by area of interest, acquisition date, resolution, cloud cover and off-nadir angle. Returned image identifiers can be used as a processing source. |
| Update Image Name | `updateImageName` | Renames an uploaded image. The new name is sent as a query parameter, as the Mapflow Data API expects. |
| Update Mosaic | `updateMosaic` | Updates a mosaic's name and tags. A supplied tag list replaces the existing one. |
| Update Processing | `updateProcessing` | Renames a processing, changes its description, or moves it to another project. Only the fields supplied are sent. |
| Update Project | `updateProject` | Updates a project's name and description. Only the fields supplied are sent, so untouched fields keep their current values. |
