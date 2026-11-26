---
description: "Google Photos stores photos and videos. Create albums, upload media and add or remove media items in albums."
hidden: true
---

# Google Photos

<img src="../../.gitbook/assets/connectors/lg/google-photos.png" alt="Google Photos logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [google.com](https://google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googlePhotos` |

## Setup

Your customers sign in to Google Photos through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Photos from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googlePhotos.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Add Album Enrichment</td><td><code>addEnrichment</code></td><td>Adds a text enrichment at a specified position in an app-created album. position is one of FIRST_IN_ALBUM, LAST_IN_ALBUM, AFTER_MEDIA_ITEM, AFTER_ENRICHMENT_ITEM. Requires photoslibrary.appendonly scope.</td></tr><tr><td>Batch Add Media Items To Album</td><td><code>batchAddMediaItems</code></td><td>Adds one or more app-created media items to an app-created album. The media items and album must both have been created by this app. Requires photoslibrary.appendonly scope.</td></tr><tr><td>Batch Create Media Items</td><td><code>batchCreateMediaItems</code></td><td>Creates one or more media items in the user's library (optionally added to an app-created album) from previously uploaded upload tokens. Provide newMediaItems as a JSON array of {description, simpleMediaItem:{uploadToken, fileName}}. Requires photoslibrary.appendonly scope.</td></tr><tr><td>Batch Get Media Items</td><td><code>batchGetMediaItems</code></td><td>Returns app-created media items for a list of identifiers. Pass mediaItemIds as a repeated query parameter. Requires photoslibrary.readonly.appcreateddata scope.</td></tr><tr><td>Batch Remove Media Items From Album</td><td><code>batchRemoveMediaItems</code></td><td>Removes one or more app-created media items from an app-created album. Requires photoslibrary.appendonly scope.</td></tr><tr><td>Create Album</td><td><code>createAlbum</code></td><td>Creates an app-created album in the user's Google Photos library. Requires photoslibrary.appendonly scope.</td></tr><tr><td>Get Album</td><td><code>getAlbum</code></td><td>Returns the app-created album for the specified albumId. Requires photoslibrary.readonly.appcreateddata scope.</td></tr><tr><td>Get Media Item</td><td><code>getMediaItem</code></td><td>Returns the app-created media item for the specified mediaItemId. Requires photoslibrary.readonly.appcreateddata scope.</td></tr><tr><td>Get Shared Album</td><td><code>getSharedAlbum</code></td><td>DEPRECATED (removed 2025-03-31): Returns a shared album by its shareToken. Requires the removed photoslibrary.sharing scope and will return 403. Kept for endpoint-inventory completeness.</td></tr><tr><td>Join Shared Album</td><td><code>joinSharedAlbum</code></td><td>DEPRECATED (removed 2025-03-31): Joins a shared album on behalf of the user via shareToken. Requires the removed photoslibrary.sharing scope and will return 403. Kept for endpoint-inventory completeness.</td></tr></tbody></table>

<details>

<summary>View 10 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Leave Shared Album</td><td><code>leaveSharedAlbum</code></td><td>DEPRECATED (removed 2025-03-31): Leaves a previously joined shared album via shareToken. Requires the removed photoslibrary.sharing scope and will return 403. Kept for endpoint-inventory completeness.</td></tr><tr><td>List Albums</td><td><code>listAlbums</code></td><td>Lists all albums created by this app in the user's library. Supports pagination. Requires photoslibrary.readonly.appcreateddata scope.</td></tr><tr><td>List Media Items</td><td><code>listMediaItems</code></td><td>Lists all media items created by this app in the user's library, ordered newest first. Supports pagination. Requires photoslibrary.readonly.appcreateddata scope.</td></tr><tr><td>List Shared Albums</td><td><code>listSharedAlbums</code></td><td>DEPRECATED (removed 2025-03-31): Lists shared albums the user is a member of. Requires the removed photoslibrary.sharing/readonly scope and will return 403. Kept for endpoint-inventory completeness.</td></tr><tr><td>Search Media Items</td><td><code>searchMediaItems</code></td><td>Searches app-created media items within a specific album. Provide albumId and pageSize (albumId cannot be combined with content filters). Requires photoslibrary.readonly.appcreateddata scope.</td></tr><tr><td>Share Album</td><td><code>shareAlbum</code></td><td>DEPRECATED (removed 2025-03-31): Marks an app-created album as shared and returns share info. Requires the removed photoslibrary.sharing scope and will return 403 PERMISSION_DENIED. Kept for endpoint-inventory completeness.</td></tr><tr><td>Unshare Album</td><td><code>unshareAlbum</code></td><td>DEPRECATED (removed 2025-03-31): Stops sharing an app-created album. Requires the removed photoslibrary.sharing scope and will return 403. Kept for endpoint-inventory completeness.</td></tr><tr><td>Update Album</td><td><code>updateAlbum</code></td><td>Updates the title of an app-created album. updateMask controls which fields change (title and/or coverPhotoMediaItemId). Requires photoslibrary.edit.appcreateddata scope.</td></tr><tr><td>Update Media Item</td><td><code>updateMediaItem</code></td><td>Updates the description of an app-created media item. updateMask must be 'description'. Requires photoslibrary.edit.appcreateddata scope.</td></tr><tr><td>Upload Media Bytes</td><td><code>uploadMedia</code></td><td>Uploads raw image/video bytes to Google Photos and returns an upload token (plain-text body). Pass the file bytes as input.file and the file's MIME type as input.mimeType. The returned token is then used in Batch Create Media Items. Requires photoslibrary.appendonly scope.</td></tr></tbody></table>

</details>

## Events

Google Photos has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
