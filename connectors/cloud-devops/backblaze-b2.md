---
description: "Backblaze B2 Cloud Storage connector using the B2 Native API v3."
hidden: true
---

# Backblaze B2

<img src="../../.gitbook/assets/connectors/lg/backblaze-b2.png" alt="Backblaze B2 logo">

Backblaze B2 Cloud Storage connector using the B2 Native API v3. Manage buckets, files and file versions, application keys, large-file uploads, download authorizations, and bucket event-notification rules.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Authentication** | Credentials you enter |
| **Slug** | `backblazeB2` |

## Use it

Add Backblaze B2 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.backblazeB2.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Authorize Account | `authorizeAccount` | Authorizes use of the B2 Native API and returns an authorization token plus the storage API URL, download URL, and account details. Run this first; pass the returned authorizationToken to every other action. |
| Cancel Large File | `cancelLargeFile` | Cancels a large file upload and deletes all parts already uploaded. |
| Copy File | `copyFile` | Creates a new file by copying from an existing file, optionally into a different bucket. |
| Copy Part | `copyPart` | Copies from an existing B2 file, storing it as a part of a large file that has already been started. |
| Create Application Key | `createKey` | Creates a new application key with the given capabilities. |
| Create Bucket | `createBucket` | Creates a new bucket owned by the account. Bucket names must be globally unique across all of Backblaze B2. |
| Delete Application Key | `deleteKey` | Deletes the specified application key. |
| Delete Bucket | `deleteBucket` | Deletes the specified bucket. Only buckets that contain no files can be deleted. |
| Delete File Version | `deleteFileVersion` | Deletes one version of a file. If it is the only version, the file is removed entirely. |
| Download File By ID | `downloadFileById` | Downloads one file from B2 by its file id. The response body is the raw file content. |

<details>

<summary>See 21 more actions</summary>

* **Download File By Name** `downloadFileByName`: Downloads one file by providing the bucket name and the file name. The response body is the raw file content.
* **Finish Large File** `finishLargeFile`: Combines the uploaded parts into a single B2 file.
* **Get Bucket Notification Rules** `getBucketNotificationRules`: Returns the event notification rules configured on a bucket.
* **Get Download Authorization** `getDownloadAuthorization`: Generates a token to download files with the given prefix from a private bucket.
* **Get File Info** `getFileInfo`: Gets information about one file stored in Backblaze B2.
* **Get Upload Part URL** `getUploadPartUrl`: Gets a URL and token for uploading parts of a large file.
* **Get Upload URL** `getUploadUrl`: Gets a URL and authorization token to use for uploading files to the given bucket.
* **Hide File** `hideFile`: Hides a file so that downloading by name will not find it, while keeping older versions.
* **List Application Keys** `listKeys`: Lists application keys associated with an account.
* **List Buckets** `listBuckets`: Lists buckets associated with the account, in alphabetical order by bucket name. Optionally filter by bucket id, bucket name, or bucket types.
* **List File Names** `listFileNames`: Lists the names of all files in a bucket, starting at a given name, returning one entry per file.
* **List File Versions** `listFileVersions`: Lists all versions of all files in a bucket, in alphabetical order by file name and reverse-chronological order per version.
* **List Parts** `listParts`: Lists the parts uploaded for a large file that has not been finished.
* **List Unfinished Large Files** `listUnfinishedLargeFiles`: Lists large-file uploads that have been started but not finished or canceled.
* **Set Bucket Notification Rules** `setBucketNotificationRules`: Sets the event notification rules on a bucket. Each rule has name, eventTypes, isEnabled, objectNamePrefix, and targetConfiguration.
* **Start Large File** `startLargeFile`: Prepares to upload the parts of a large file.
* **Update Bucket** `updateBucket`: Updates settings on an existing bucket such as its type, metadata, CORS rules, lifecycle rules, default retention, and encryption.
* **Update File Legal Hold** `updateFileLegalHold`: Turns the legal hold on or off for a file version. The bucket must have Object Lock enabled.
* **Update File Retention** `updateFileRetention`: Modifies Object Lock retention for a file version. fileRetention is e.g. {"mode":"governance","retainUntilTimestamp":&lt;ms&gt;}.
* **Upload File** `uploadFile`: Uploads a file to a bucket using an upload URL and token from Get Upload URL. The upload URL is a per-call dynamic host.
* **Upload Part** `uploadPart`: Uploads one part of a large file using an upload URL from Get Upload Part URL. The upload URL is a per-call dynamic host.

</details>
