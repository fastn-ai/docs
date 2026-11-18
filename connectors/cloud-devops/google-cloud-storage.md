---
description: "Google Cloud Storage JSON API connector."
hidden: true
---

# Google Cloud Storage

<img src="../../.gitbook/assets/connectors/lg/google-cloud-storage.png" alt="Google Cloud Storage logo">

Google Cloud Storage JSON API connector. Manage buckets, objects (including media upload, compose, copy, rewrite), bucket/object/default object ACLs, IAM policies, HMAC keys, and Pub/Sub notification configs. Base URL https://storage.googleapis.com/storage/v1 (uploads at https://storage.googleapis.com/upload/storage/v1). OAuth 2.0 (Google) auth.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloud.google.com](https://cloud.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudStorage` |

## Use it

Add Google Cloud Storage from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudStorage.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Compose Objects | `composeObjects` | Concatenates a list of existing objects into a new object in the same bucket. |
| Copy Object | `copyObject` | Copies a source object to a destination object. Optionally overrides metadata. |
| Create HMAC Key | `createHmacKey` | Creates a new HMAC key for the specified service account. The secret is returned only once, in this response. |
| Delete Bucket | `deleteBucket` | Permanently deletes an empty bucket. |
| Delete Bucket ACL | `deleteBucketAcl` | Permanently deletes the ACL entry for the specified entity on the specified bucket. |
| Delete Default Object ACL | `deleteDefaultObjectAcl` | Permanently deletes the default object ACL entry for the specified entity on the specified bucket. |
| Delete HMAC Key | `deleteHmacKey` | Deletes an HMAC key. The key must be in the INACTIVE state before it can be deleted. |
| Delete Notification | `deleteNotification` | Permanently deletes a Pub/Sub notification configuration from the given bucket. |
| Delete Object | `deleteObject` | Deletes an object and its metadata. Deletions are permanent if versioning is not enabled. |
| Delete Object ACL | `deleteObjectAcl` | Permanently deletes the ACL entry for the specified entity on the specified object. |
| Get Bucket | `getBucket` | Returns metadata for the specified bucket. |
| Get Bucket ACL | `getBucketAcl` | Returns the ACL entry for the specified entity on the specified bucket. |
| Get Bucket IAM Policy | `getBucketIamPolicy` | Returns the IAM policy for the specified bucket. |
| Get Default Object ACL | `getDefaultObjectAcl` | Returns the default object ACL entry for the specified entity on the specified bucket. |
| Get HMAC Key | `getHmacKey` | Retrieves an HMAC key's metadata by access ID. |
| Get Notification | `getNotification` | Returns a single Pub/Sub notification configuration on the given bucket. |
| Get Object ACL | `getObjectAcl` | Returns the ACL entry for the specified entity on the specified object. |
| Get Object IAM Policy | `getObjectIamPolicy` | Returns the IAM policy for the specified object. |
| Get Object Metadata | `getObject` | Retrieves an object's metadata. To download the object's content, use the media download (alt=media) parameter. |
| Insert Bucket | `insertBucket` | Creates a new bucket in the given project. Requires the project query parameter and a bucket name in the body. |
| Insert Bucket ACL | `insertBucketAcl` | Creates a new ACL entry on the specified bucket. |
| Insert Default Object ACL | `insertDefaultObjectAcl` | Creates a new default object ACL entry on the specified bucket. |
| Insert Notification | `insertNotification` | Creates a Pub/Sub notification configuration for the given bucket. Requires a fully-qualified Pub/Sub topic (//pubsub.googleapis.com/projects/{project}/topics/{topic}) that the GCS service account can publish to. |
| Insert Object ACL | `insertObjectAcl` | Creates a new ACL entry on the specified object. |
| List Bucket ACLs | `listBucketAcls` | Retrieves ACL entries on the specified bucket. |
| List Buckets | `listBuckets` | Retrieves a list of buckets for a given project. Requires the project query parameter. |
| List Default Object ACLs | `listDefaultObjectAcls` | Retrieves default object ACL entries on the specified bucket. |
| List HMAC Keys | `listHmacKeys` | Retrieves a list of HMAC keys matching the criteria in the given project. |
| List Notifications | `listNotifications` | Retrieves a list of Pub/Sub notification configurations for the given bucket. |
| List Object ACLs | `listObjectAcls` | Retrieves ACL entries on the specified object. |
| List Objects | `listObjects` | Retrieves a list of objects matching the criteria in the given bucket. |
| Patch Bucket | `patchBucket` | Updates a bucket. Changes are applied to only the fields provided (partial update). |
| Patch Bucket ACL | `patchBucketAcl` | Patches an ACL entry on the specified bucket (partial update). |
| Patch Default Object ACL | `patchDefaultObjectAcl` | Patches a default object ACL entry on the specified bucket (partial update). |
| Patch Object | `patchObject` | Patches an object's metadata (partial update). |
| Patch Object ACL | `patchObjectAcl` | Patches an ACL entry on the specified object (partial update). |
| Rewrite Object | `rewriteObject` | Rewrites a source object to a destination object. Supports cross-location and cross-storage-class copies, and resumes via rewriteToken. |
| Set Bucket IAM Policy | `setBucketIamPolicy` | Updates (replaces) the IAM policy for the specified bucket. |
| Update Bucket | `updateBucket` | Updates a bucket. This method performs a full update; unspecified writable fields are reset to default values. |
| Update Bucket ACL | `updateBucketAcl` | Updates an ACL entry on the specified bucket (full update). |
| Update Default Object ACL | `updateDefaultObjectAcl` | Updates a default object ACL entry on the specified bucket (full update). |
| Update HMAC Key | `updateHmacKey` | Updates the state of an HMAC key. Only the state field is mutable (ACTIVE or INACTIVE). |
| Update Object | `updateObject` | Updates an object's metadata (full update). |
| Update Object ACL | `updateObjectAcl` | Updates an ACL entry on the specified object (full update). |
| Upload Object (Media) | `insertObject` | Stores a new object using a simple media upload. Uses the upload base URL with uploadType=media. The object name is set via the 'name' query param and the file content is passed as the request body. |
