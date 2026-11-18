---
description: "Cloudinary media management — Admin API and Upload API."
hidden: true
---

# Cloudinary

<img src="../../.gitbook/assets/connectors/lg/cloudinary.png" alt="Cloudinary logo">

Cloudinary media management — Admin API and Upload API. Manage assets (resources), folders, transformations, upload presets, usage reporting, and upload/transform media. Auth via HTTP Basic (API key:API secret) scoped to a cloud name.

| | |
| --- | --- |
| **Category** | [Design](README.md) |
| **Website** | [cloudinary.com](https://cloudinary.com) |
| **Authentication** | Basic auth |
| **Slug** | `cloudinary` |

## Use it

Add Cloudinary from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cloudinary.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Context To Assets | `addContext` | Upload API: add contextual key/value metadata to one or more assets by public_id. |
| Add Related Assets | `addRelatedAssets` | Relate an asset (by asset ID) to up to 10 other assets (by asset IDs). Bidirectional. Admin API POST /resources/related_assets/:asset_id. |
| Add Tag | `addTag` | Add a single tag to one or more assets. Upload API POST /{resource_type}/tags with command=add. |
| Create Folder | `createFolder` | Create a new (empty) folder at the given path. Admin API POST /folders/{folder}. |
| Create Metadata Field | `createMetadataField` | Admin API: create a new structured metadata field (string, integer, date, enum, set). |
| Create Multi Animated Asset | `createMulti` | Upload API: create a single animated GIF/WebP/PDF from all assets sharing a tag (multi method). |
| Create Named Transformation | `createTransformation` | Create a new named transformation. Admin API POST /transformations/{name} with the transformation string. |
| Create Notification Trigger | `createTrigger` | Register a webhook notification URL trigger. Admin API POST /triggers. Each trigger links one event_type to one notification URI. |
| Create Streaming Profile | `createStreamingProfile` | Create a custom adaptive streaming profile. Admin API POST /streaming_profiles. representations is an array of {transformation:[{width,height,bit_rate,video_codec,...}]} objects. |
| Create Upload Mapping | `createUploadMapping` | Create an upload mapping that maps a Cloudinary folder to a remote URL prefix (auto-upload / lazy migration). Admin API POST /upload_mappings. |
| Create Upload Preset | `createUploadPreset` | Create a new upload preset with default upload parameters (folder, tags, transformation, unsigned, etc.). Admin API POST /upload_presets. |
| Delete Derived Resources | `deleteDerivedResources` | Delete derived assets by their derived resource IDs (up to 100). Derived IDs come from Get Resource details. Admin API DELETE /derived_resources. |
| Delete Folder | `deleteFolder` | Delete an empty folder. The folder must contain no assets. Admin API DELETE /folders/{folder}. |
| Delete Metadata Field | `deleteMetadataField` | Admin API: delete a structured metadata field definition by external_id. |
| Delete Metadata Field Datasource Entries | `deleteMetadataFieldDatasourceEntries` | Soft-delete (block, set inactive) datasource entries of a metadata field. Restorable via Restore Metadata Field Datasource Entries. Admin API DELETE /metadata_fields/:external_id/datasource. |
| Delete Notification Trigger | `deleteTrigger` | Delete a global webhook notification trigger by id. Used by the webhook unsubscription flow. Admin API DELETE /triggers/{id}. |
| Delete Or Revert Streaming Profile | `deleteStreamingProfile` | Delete a custom streaming profile, or revert a modified built-in profile to its original settings. Admin API DELETE /streaming_profiles/:name. |
| Delete Related Assets | `deleteRelatedAssets` | Unrelate an asset (by asset ID) from other assets (by asset IDs). Bidirectional. Admin API DELETE /resources/related_assets/:asset_id. |
| Delete Resources | `deleteResources` | Delete assets by public_ids (or by prefix/all). Optionally invalidate CDN cache and keep original. Admin API DELETE /resources/{resource_type}/{type}. |
| Delete Resources By Asset IDs | `deleteResourcesByAssetIds` | Delete assets by their immutable asset IDs (up to 100). Optionally only derived assets (keep_original) or specific transformations. Admin API DELETE /resources. |
| Delete Transformation | `deleteTransformation` | Delete a named transformation (or clear a used transformation's derived assets). Admin API DELETE /transformations/{transformation}. |
| Delete Upload Mapping | `deleteUploadMapping` | Delete the upload mapping for a folder. Admin API DELETE /upload_mappings?folder=:folder. |
| Delete Upload Preset | `deleteUploadPreset` | Delete an upload preset by name. Admin API DELETE /upload_presets/{name}. |
| Destroy Asset | `destroyAsset` | Immediately delete a single asset by public_id and remove it from the CDN. Upload API POST /{resource_type}/destroy. |
| Explicit (Apply Operations) | `explicitAsset` | Apply operations to an already-uploaded asset (e.g. generate eager transformations, set tags/context, trigger background removal/moderation) without re-uploading. Upload API POST /{resource_type}/explicit. |
| Explode Asset | `explodeAsset` | Upload API: explode a multi-page PDF (or animated asset) into individual per-page derived assets. |
| Generate Archive | `generateArchive` | Upload API: generate a ZIP archive of assets selected by public_ids, tags, or prefixes. |
| Generate Sprite | `generateSprite` | Upload API: generate a single sprite image (and CSS) from all assets sharing a tag. |
| Get Metadata Field | `getMetadataField` | Admin API: get a single structured metadata field definition by its external_id. |
| Get Resource By Asset ID | `getResourceByAssetId` | Admin API: get full details for a single asset by its asset_id. |
| Get Resource By Public ID | `getResource` | Get details of a single asset by public_id, including derived assets, colors, faces, exif and metadata when requested. Admin API GET /resources/{resource_type}/{type}/{public_id}. |
| Get Streaming Profile | `getStreamingProfile` | Get details of a single streaming profile (built-in or custom) by name, including its representations. Admin API GET /streaming_profiles/:name. |
| Get Transformation | `getTransformation` | Get details of a single transformation by its name/string, including derived assets. Admin API GET /transformations/{transformation}. |
| Get Upload Mapping | `getUploadMapping` | Get the upload mapping for a single folder. Admin API GET /upload_mappings?folder=:folder. Returns the folder and its mapped URL template. |
| Get Upload Preset | `getUploadPreset` | Get the details and settings of a single upload preset by name. Admin API GET /upload_presets/{name}. |
| Get Usage | `getUsage` | Get a report on account usage details — storage, transformations, bandwidth, requests, and plan limits. Admin API GET /usage (optionally for a specific date). |
| Get Usage By Date | `getUsageByDate` | Admin API: get account usage details for a specific date. Returns the same structure as getUsage but for the given day. |
| List Metadata Fields | `listMetadataFields` | Admin API: list all structured metadata field definitions in the product environment. |
| List Notification Triggers | `listTriggers` | List all global webhook notification trigger URLs configured for the product environment. Admin API GET /triggers. |
| List Resources | `listResources` | List assets (resources) of a given type and delivery type (e.g. image/upload). Supports pagination, prefix filtering, tags/context/metadata inclusion. Admin API GET /resources/{resource_type}/{type}. |
| List Resources By Asset Folder | `listResourcesByAssetFolder` | List assets located in a given asset folder (dynamic folder mode). Admin API GET /resources/by_asset_folder. |
| List Resources By Asset IDs | `listResourcesByAssetIds` | Admin API: fetch details for multiple assets in one call by their asset_ids. |
| List Resources By Context | `listResourcesByContext` | Admin API: list assets that have a contextual metadata key (and optional value). |
| List Resources By Moderation | `listResourcesByModeration` | Admin API: list assets in a given moderation status (pending, approved, rejected) for a moderation kind. |
| List Resources By Public IDs | `listResourcesByPublicIds` | Get details of multiple assets (up to 100) of a resource type and delivery type by their public IDs. Admin API GET /resources/:resource_type/:type with public_ids[]. |
| List Resources By Tag | `listResourcesByTag` | Admin API: list assets of a given resource_type that have the specified tag. |
| List Root Folders | `listFolders` | List all root folders in the product environment. Admin API GET /folders. |
| List Streaming Profiles | `listStreamingProfiles` | List all built-in and custom adaptive streaming profiles. Admin API GET /streaming_profiles. |
| List Subfolders | `listSubfolders` | List immediate subfolders of a given parent folder. Admin API GET /folders/{folder}. |
| List Tags | `listTags` | List all tags currently assigned to assets of a given resource type. Admin API GET /tags/{resource_type}. |
| List Transformations | `listTransformations` | List all defined transformations (named and used). Admin API GET /transformations. |
| List Upload Mappings | `listUploadMappings` | List all upload mappings (folder -&gt; remote URL prefix) in the product environment. Admin API GET /upload_mappings. Supports max_results/next_cursor paging. |
| List Upload Presets | `listUploadPresets` | List all upload presets defined in the product environment. Admin API GET /upload_presets. |
| Ping | `ping` | Test connectivity and credentials. Returns {status: 'ok'}. Admin API GET /ping. |
| Remove All Tags | `removeAllTags` | Remove all tags from the given assets. Upload API POST /{resource_type}/tags with command=remove_all. |
| Remove Tag | `removeTag` | Remove a single tag from one or more assets. Upload API POST /{resource_type}/tags with command=remove. |
| Rename Asset | `renameAsset` | Rename / move an asset to a new public_id, optionally overwriting and invalidating the CDN. Upload API POST /{resource_type}/rename. |
| Rename Folder | `renameFolder` | Admin API: rename/move a folder from one path to another. |
| Replace Tags | `replaceTags` | Replace all tags on the given assets with the supplied tag(s). Upload API POST /{resource_type}/tags with command=replace. |
| Restore Metadata Field Datasource Entries | `restoreMetadataFieldDatasourceEntries` | Restore (unblock) previously deleted datasource entries of a metadata field. Admin API POST /metadata_fields/:external_id/datasource_restore. |
| Restore Resources | `restoreResources` | Restore previously deleted assets (from backup) by public_ids, optionally restoring specific versions. Admin API POST /resources/{resource_type}/{type}/restore. |
| Restore Resources By Asset IDs | `restoreResourcesByAssetIds` | Restore backed-up (deleted or existing) assets by their asset IDs (up to 100), optionally a specific version per asset. Requires backup enabled. Admin API POST /resources/restore. |
| Search Folders | `searchFolders` | Search asset folders with a Lucene-like expression (e.g. name:prod* AND path:marketing/*). With no expression returns the 50 most recently created folders. Admin API GET /folders/search. |
| Search Resources | `searchResources` | Advanced asset search using the Cloudinary search Lucene-like expression syntax, with sorting, aggregation, field selection and pagination. Admin API POST /resources/search. |
| Update Access Mode By Tag | `updateAccessModeByTag` | Admin API: bulk-update the access_mode (public/authenticated) of uploaded assets selected by tag. |
| Update Assets Metadata | `updateAssetsMetadata` | Upload API: set structured metadata field values on one or more assets by public_id. |
| Update Metadata Field | `updateMetadataField` | Admin API: update an existing structured metadata field definition by external_id. |
| Update Metadata Field Datasource | `updateMetadataFieldDatasource` | Add or update datasource entries of an enum/set structured metadata field. Entries with an existing external_id are updated, others are added. Admin API PUT /metadata_fields/:external_id/datasource. |
| Update Notification Trigger | `updateTrigger` | Update an existing webhook notification trigger. Admin API PUT /triggers/{id}. |
| Update Resource | `updateResource` | Update an existing asset's details — tags, context, metadata, moderation status, display name. Admin API POST /resources/{resource_type}/{type}/{public_id}. |
| Update Resource By Asset ID | `updateResourceByAssetId` | Update attributes of an asset identified by its immutable asset ID (display name, asset folder, tags, context, metadata, moderation status, coordinates). Admin API PUT /resources/:asset_id. |
| Update Streaming Profile | `updateStreamingProfile` | Update an existing streaming profile (custom, or override a built-in one) by name. Admin API PUT /streaming_profiles/:name. Replaces the representations list. |
| Update Transformation | `updateTransformation` | Update an existing named transformation — change its definition or its allowed_for_strict flag. Admin API PUT /transformations/{transformation}. |
| Update Upload Mapping | `updateUploadMapping` | Update an existing upload mapping folder with a new URL template. Admin API PUT /upload_mappings. |
| Update Upload Preset | `updateUploadPreset` | Update an existing upload preset's settings. Admin API PUT /upload_presets/{name}. |
| Upload Asset | `uploadAsset` | Upload a new asset (image/video/raw) from a remote URL, base64 data URI, or S3/GCS reference. Supports public_id, folder, tags, context, transformations, eager, overwrite, and more. Upload API POST /{resource_type}/upload. Note: server-side calls authenticate via Basic auth (api_key/api_secret). |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Asset Deleted | `delete` | Sent when assets are deleted via the API or console. |
| Asset Renamed | `rename` | Sent when an asset is renamed/moved. |
| Create Folder | `create_folder` | Sent when a folder is created. |
| Delete | `delete` | Sent when assets are deleted. |
| Eager Transformation | `eager` | Sent when asynchronous eager transformations requested via upload/explicit complete. |
| Eager Transformation Done | `eager` | Sent when asynchronous eager transformations requested at upload time have finished generating. |
| Folder Created | `create_folder` | Sent when a new folder is created. |
| Moderation | `moderation` | Sent when manual or automatic moderation (e.g. WebPurify, AWS Rekognition, manual) completes for an asset. |
| Moderation Result | `moderation` | Sent when a moderation (manual, aws_rek, webpurify, etc.) result is available for an asset. |
| Multi (Animated) Generated | `multi` | Sent when an asynchronous multi (animated GIF/video) generation request completes. |
| Rename | `rename` | Sent when an asset is renamed. |
| Resource Metadata Changed | `resource_metadata_changed` | Sent when structured metadata of an asset changes. |
| Sprite Generated | `sprite` | Sent when an asynchronous sprite generation request completes. |
| Tags Changed | `tags_changed` | Sent when tags on an asset are added, removed, or replaced. |
| Update | `update` | Sent when an asset's metadata, tags, or context are updated. |
| Upload | `upload` | Sent when an asset finishes uploading (including asynchronous/eager processing of the originally uploaded asset). |
| Upload Complete | `upload` | Sent when an asset upload finishes processing. Carries the full upload response (public_id, version, format, bytes, url, etc.). |
