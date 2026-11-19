---
description: "Backblaze B2 is cloud object storage. Manage buckets, files, file versions and application keys, and upload, copy and download files."
hidden: true
---

# Backblaze B2

<img src="../../.gitbook/assets/connectors/lg/backblaze-b2.png" alt="Backblaze B2 logo">

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Authentication** | Application key ID and key |
| **Slug** | `backblazeB2` |

## Setup

Your customers enter their application key id and key for Backblaze B2 when they connect. Nothing else needs setting up.

## Use it

Add Backblaze B2 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.backblazeB2.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Authorize Account</td><td><code>authorizeAccount</code></td><td>Authorizes use of the B2 Native API and returns an authorization token plus the storage API URL, download URL, and account details. Run this first; pass the returned authorizationToken to every other action.</td></tr><tr><td>Cancel Large File</td><td><code>cancelLargeFile</code></td><td>Cancels a large file upload and deletes all parts already uploaded.</td></tr><tr><td>Copy File</td><td><code>copyFile</code></td><td>Creates a new file by copying from an existing file, optionally into a different bucket.</td></tr><tr><td>Copy Part</td><td><code>copyPart</code></td><td>Copies from an existing B2 file, storing it as a part of a large file that has already been started.</td></tr><tr><td>Create Application Key</td><td><code>createKey</code></td><td>Creates a new application key with the given capabilities.</td></tr><tr><td>Create Bucket</td><td><code>createBucket</code></td><td>Creates a new bucket owned by the account. Bucket names must be globally unique across all of Backblaze B2.</td></tr><tr><td>Delete Application Key</td><td><code>deleteKey</code></td><td>Deletes the specified application key.</td></tr><tr><td>Delete Bucket</td><td><code>deleteBucket</code></td><td>Deletes the specified bucket. Only buckets that contain no files can be deleted.</td></tr><tr><td>Delete File Version</td><td><code>deleteFileVersion</code></td><td>Deletes one version of a file. If it is the only version, the file is removed entirely.</td></tr><tr><td>Download File By ID</td><td><code>downloadFileById</code></td><td>Downloads one file from B2 by its file id. The response body is the raw file content.</td></tr></tbody></table>

<details>

<summary>View 21 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Download File By Name</td><td><code>downloadFileByName</code></td><td>Downloads one file by providing the bucket name and the file name. The response body is the raw file content.</td></tr><tr><td>Finish Large File</td><td><code>finishLargeFile</code></td><td>Combines the uploaded parts into a single B2 file.</td></tr><tr><td>Get Bucket Notification Rules</td><td><code>getBucketNotificationRules</code></td><td>Returns the event notification rules configured on a bucket.</td></tr><tr><td>Get Download Authorization</td><td><code>getDownloadAuthorization</code></td><td>Generates a token to download files with the given prefix from a private bucket.</td></tr><tr><td>Get File Info</td><td><code>getFileInfo</code></td><td>Gets information about one file stored in Backblaze B2.</td></tr><tr><td>Get Upload Part URL</td><td><code>getUploadPartUrl</code></td><td>Gets a URL and token for uploading parts of a large file.</td></tr><tr><td>Get Upload URL</td><td><code>getUploadUrl</code></td><td>Gets a URL and authorization token to use for uploading files to the given bucket.</td></tr><tr><td>Hide File</td><td><code>hideFile</code></td><td>Hides a file so that downloading by name will not find it, while keeping older versions.</td></tr><tr><td>List Application Keys</td><td><code>listKeys</code></td><td>Lists application keys associated with an account.</td></tr><tr><td>List Buckets</td><td><code>listBuckets</code></td><td>Lists buckets associated with the account, in alphabetical order by bucket name. Optionally filter by bucket id, bucket name, or bucket types.</td></tr><tr><td>List File Names</td><td><code>listFileNames</code></td><td>Lists the names of all files in a bucket, starting at a given name, returning one entry per file.</td></tr><tr><td>List File Versions</td><td><code>listFileVersions</code></td><td>Lists all versions of all files in a bucket, in alphabetical order by file name and reverse-chronological order per version.</td></tr><tr><td>List Parts</td><td><code>listParts</code></td><td>Lists the parts uploaded for a large file that has not been finished.</td></tr><tr><td>List Unfinished Large Files</td><td><code>listUnfinishedLargeFiles</code></td><td>Lists large-file uploads that have been started but not finished or canceled.</td></tr><tr><td>Set Bucket Notification Rules</td><td><code>setBucketNotificationRules</code></td><td>Sets the event notification rules on a bucket. Each rule has name, eventTypes, isEnabled, objectNamePrefix, and targetConfiguration.</td></tr><tr><td>Start Large File</td><td><code>startLargeFile</code></td><td>Prepares to upload the parts of a large file.</td></tr><tr><td>Update Bucket</td><td><code>updateBucket</code></td><td>Updates settings on an existing bucket such as its type, metadata, CORS rules, lifecycle rules, default retention, and encryption.</td></tr><tr><td>Update File Legal Hold</td><td><code>updateFileLegalHold</code></td><td>Turns the legal hold on or off for a file version. The bucket must have Object Lock enabled.</td></tr><tr><td>Update File Retention</td><td><code>updateFileRetention</code></td><td>Modifies Object Lock retention for a file version. fileRetention is e.g. {"mode":"governance","retainUntilTimestamp":&lt;ms&gt;}.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Uploads a file to a bucket using an upload URL and token from Get Upload URL. The upload URL is a per-call dynamic host.</td></tr><tr><td>Upload Part</td><td><code>uploadPart</code></td><td>Uploads one part of a large file using an upload URL from Get Upload Part URL. The upload URL is a per-call dynamic host.</td></tr></tbody></table>

</details>

## Events

Backblaze B2 has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
