---
description: "Uploadcare file uploading, storage, CDN delivery, and processing platform."
hidden: true
---

# Uploadcare

<img src="../../.gitbook/assets/connectors/uploadcare.png" alt="Uploadcare logo" width="64">

Uploadcare file uploading, storage, CDN delivery, and processing platform. Manage files, groups, file metadata, webhooks, document and video conversion, and AI add-ons (AWS Rekognition, virus scanning, background removal) via the Uploadcare REST API v0.7, plus uploading via the Upload API.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [uploadcare.com](https://uploadcare.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `uploadcare` |

## Use it

Add Uploadcare from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.uploadcare.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Convert Document | `convertDocument` | Convert one or more documents to another format (e.g. PDF to PNG, DOCX to PDF). Each path uses the form uuid/document/-/format/target/. Returns a conversion token to poll for status. |
| Convert Video | `convertVideo` | Convert or transcode one or more videos (format, quality, size, cut, thumbnails). Each path uses the form uuid/video/-/format/target/... . Returns a conversion token to poll for status. |
| Copy File To Local Storage | `copyFileToLocalStorage` | Create a copy of a file in the project's local Uploadcare storage. Accepts a file UUID or CDN URL as the source. |
| Copy File To Remote Storage | `copyFileToRemoteStorage` | Copy a file to a custom (remote) storage backend configured for the project, such as an S3 bucket. Requires a custom storage target to be set up in the project settings. |
| Create Group | `createGroup` | Create a group from a set of previously uploaded files via the Upload API. Provide file UUIDs in the indexed files[0], files[1], ... fields. At least one file is required. |
| Create Webhook | `createWebhook` | Subscribe a target URL to a project event so Uploadcare sends a webhook notification when that event occurs. |
| Delete File | `deleteFile` | Remove a single file from the project by its UUID. The file becomes inaccessible and is scheduled for permanent deletion. |
| Delete File Metadata Key | `deleteFileMetadataKey` | Remove a single custom metadata key from a file. |
| Delete Files Batch | `deleteFilesBatch` | Remove multiple files in one request. Provide a JSON array of file UUIDs (up to 100). |
| Delete Group | `deleteGroup` | Delete a file group by its ID. The files that belonged to the group are not deleted. |

<details>

<summary>See 26 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Execute AWS Rekognition Labels | `executeAwsRekognitionLabels` | Run the AWS Rekognition object/label detection add-on on an image file. Returns a request ID to poll for results. |
| Execute AWS Rekognition Moderation | `executeAwsRekognitionModeration` | Run the AWS Rekognition unsafe-content moderation add-on on an image file. Returns a request ID to poll for results. |
| Execute Remove Background | `executeRemoveBg` | Run the remove.bg background-removal add-on on an image file. Returns a request ID to poll for the resulting file. |
| Execute Virus Scan | `executeVirusScan` | Run the ClamAV virus scan add-on on a file. Optionally purge the file automatically if it is infected. Returns a request ID to poll for results. |
| Get AWS Rekognition Labels Status | `getAwsRekognitionLabelsStatus` | Check the status and retrieve results of an AWS Rekognition label detection add-on execution by its request ID. |
| Get AWS Rekognition Moderation Status | `getAwsRekognitionModerationStatus` | Check the status and retrieve results of an AWS Rekognition moderation add-on execution by its request ID. |
| Get Document Conversion Status | `getDocumentConversionStatus` | Check the status of a document conversion job using the token returned by Convert Document. |
| Get File | `getFile` | Retrieve detailed information about a single file by its UUID, optionally including add-on application data. |
| Get File Metadata | `getFileMetadata` | Retrieve all custom metadata key-value pairs attached to a file. |
| Get File Metadata Key | `getFileMetadataKey` | Retrieve the value of a single custom metadata key for a file. |
| Get Group | `getGroup` | Retrieve information about a single file group by its ID (in the form uuid~filesCount). |
| Get Project | `getProject` | Retrieve information about the current project, including its name, public key, collaborators, and auto-store setting. |
| Get Remove Background Status | `getRemoveBgStatus` | Check the status and retrieve the result of a remove.bg background-removal add-on execution by its request ID. When done, the result includes the UUID of the processed file. |
| Get Upload File Info | `uploadFileInfo` | Retrieve information about an uploaded file directly from the Upload API by its file ID (UUID). |
| Get Upload From URL Status | `getUploadFromUrlStatus` | Check the status of an asynchronous upload-from-URL job using its token. When complete, returns the uploaded file's UUID and metadata. |
| Get Video Conversion Status | `getVideoConversionStatus` | Check the status of a video conversion job using the token returned by Convert Video. |
| Get Virus Scan Status | `getVirusScanStatus` | Check the status and retrieve results of a ClamAV virus scan add-on execution by its request ID. |
| List Files | `listFiles` | List files in the Uploadcare project with optional filtering by stored/removed status, ordering, and pagination. |
| List Groups | `listGroups` | List file groups in the project, with optional ordering and pagination. |
| List Webhooks | `listWebhooks` | List all webhook subscriptions configured for the project. |
| Store File | `storeFile` | Store a single file permanently by its UUID so it is not deleted after the temporary storage period. |
| Store Files Batch | `storeFilesBatch` | Store multiple files permanently in one request. Provide a JSON array of file UUIDs (up to 100). |
| Unsubscribe Webhook | `unsubscribeWebhook` | Remove a webhook subscription identified by its target URL and event. |
| Update File Metadata Key | `updateFileMetadataKey` | Set or update the value of a single custom metadata key on a file. Key up to 64 characters; value up to 512 characters. |
| Update Webhook | `updateWebhook` | Update an existing webhook subscription by its ID. Only the provided fields are changed. |
| Upload File From URL | `uploadFromUrl` | Upload a file to Uploadcare from a publicly accessible source URL via the Upload API. Returns an async token; poll Get Upload From URL Status with the token to obtain the resulting file. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| File Deleted | `file.deleted` | A file was removed from the project. |
| File Infected | `file.infected` | Malware was detected during an automatic or explicit scan (Uploadcare is deprecating this in favor of file.info_updated). |
| File Info Updated | `file.info_updated` | metadata or appdata changed, typically after an add-on ran (object recognition, unsafe content detection, malware protection). |
| File Stored | `file.stored` | A file transitioned to stored status. |
| File Uploaded | `file.uploaded` | A new file was uploaded, a local copy created, or a file generated from a processing operation. |
