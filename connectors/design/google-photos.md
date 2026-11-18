---
description: "Google Photos Library API v1 connector (https://photoslibrary.googleapis.com/v1)."
hidden: true
---

# Google Photos

Google Photos Library API v1 connector (https://photoslibrary.googleapis.com/v1). Manage app-created albums and media items: create/list/get/update albums, add enrichments, batch add/remove media items to albums; list/get/search/update media items, batchGet, batchCreate from upload tokens; raw byte uploads (/v1/uploads). Also includes the (deprecated as of 2025-03-31) sharing and sharedAlbums endpoints for completeness. OAuth 2.0 (Google) authorization-code auth using the shared Google OAuth app. Note: as of 2025-03-31 the API only accesses content the app itself created; the broad photoslibrary/photoslibrary.readonly/photoslibrary.sharing scopes were removed.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [google.com](https://google.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 20 |
| **Events** | 0 |
| **Slug** | `googlePhotos` |

## Use it

Add Google Photos from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googlePhotos.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Album Enrichment | `addEnrichment` | Adds a text enrichment at a specified position in an app-created album. position is one of FIRST_IN_ALBUM, LAST_IN_ALBUM, AFTER_MEDIA_ITEM, AFTER_ENRICHMENT_ITEM. Requires photoslibrary.appendonly scope. |
| Batch Add Media Items To Album | `batchAddMediaItems` | Adds one or more app-created media items to an app-created album. The media items and album must both have been created by this app. Requires photoslibrary.appendonly scope. |
| Batch Create Media Items | `batchCreateMediaItems` | Creates one or more media items in the user's library (optionally added to an app-created album) from previously uploaded upload tokens. Provide newMediaItems as a JSON array of {description, simpleMediaItem:{uploadToken, fileName}}. Requires photoslibrary.appendonly scope. |
| Batch Get Media Items | `batchGetMediaItems` | Returns app-created media items for a list of identifiers. Pass mediaItemIds as a repeated query parameter. Requires photoslibrary.readonly.appcreateddata scope. |
| Batch Remove Media Items From Album | `batchRemoveMediaItems` | Removes one or more app-created media items from an app-created album. Requires photoslibrary.appendonly scope. |
| Create Album | `createAlbum` | Creates an app-created album in the user's Google Photos library. Requires photoslibrary.appendonly scope. |
| Get Album | `getAlbum` | Returns the app-created album for the specified albumId. Requires photoslibrary.readonly.appcreateddata scope. |
| Get Media Item | `getMediaItem` | Returns the app-created media item for the specified mediaItemId. Requires photoslibrary.readonly.appcreateddata scope. |
| Get Shared Album | `getSharedAlbum` | DEPRECATED (removed 2025-03-31): Returns a shared album by its shareToken. Requires the removed photoslibrary.sharing scope and will return 403. Kept for endpoint-inventory completeness. |
| Join Shared Album | `joinSharedAlbum` | DEPRECATED (removed 2025-03-31): Joins a shared album on behalf of the user via shareToken. Requires the removed photoslibrary.sharing scope and will return 403. Kept for endpoint-inventory completeness. |
| Leave Shared Album | `leaveSharedAlbum` | DEPRECATED (removed 2025-03-31): Leaves a previously joined shared album via shareToken. Requires the removed photoslibrary.sharing scope and will return 403. Kept for endpoint-inventory completeness. |
| List Albums | `listAlbums` | Lists all albums created by this app in the user's library. Supports pagination. Requires photoslibrary.readonly.appcreateddata scope. |
| List Media Items | `listMediaItems` | Lists all media items created by this app in the user's library, ordered newest first. Supports pagination. Requires photoslibrary.readonly.appcreateddata scope. |
| List Shared Albums | `listSharedAlbums` | DEPRECATED (removed 2025-03-31): Lists shared albums the user is a member of. Requires the removed photoslibrary.sharing/readonly scope and will return 403. Kept for endpoint-inventory completeness. |
| Search Media Items | `searchMediaItems` | Searches app-created media items within a specific album. Provide albumId and pageSize (albumId cannot be combined with content filters). Requires photoslibrary.readonly.appcreateddata scope. |
| Share Album | `shareAlbum` | DEPRECATED (removed 2025-03-31): Marks an app-created album as shared and returns share info. Requires the removed photoslibrary.sharing scope and will return 403 PERMISSION_DENIED. Kept for endpoint-inventory completeness. |
| Unshare Album | `unshareAlbum` | DEPRECATED (removed 2025-03-31): Stops sharing an app-created album. Requires the removed photoslibrary.sharing scope and will return 403. Kept for endpoint-inventory completeness. |
| Update Album | `updateAlbum` | Updates the title of an app-created album. updateMask controls which fields change (title and/or coverPhotoMediaItemId). Requires photoslibrary.edit.appcreateddata scope. |
| Update Media Item | `updateMediaItem` | Updates the description of an app-created media item. updateMask must be 'description'. Requires photoslibrary.edit.appcreateddata scope. |
| Upload Media Bytes | `uploadMedia` | Uploads raw image/video bytes to Google Photos and returns an upload token (plain-text body). Pass the file bytes as input.file and the file's MIME type as input.mimeType. The returned token is then used in Batch Create Media Items. Requires photoslibrary.appendonly scope. |
