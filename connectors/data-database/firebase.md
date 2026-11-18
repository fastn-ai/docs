---
description: "Google Firebase app development platform."
hidden: true
---

# Firebase

<img src="../../.gitbook/assets/connectors/lg/firebase.png" alt="Firebase logo">

Google Firebase app development platform. Covers Cloud Firestore (document CRUD, collections, structured queries, batch writes, transactions), Firebase Realtime Database (JSON REST read/write/patch/delete), Firebase Authentication Admin (list/get/create/update/delete users via Identity Toolkit), Firebase Cloud Messaging v1 (send push notifications), Remote Config (get/publish template), and Cloud Storage for Firebase (objects and buckets via the GCS JSON API). Auth is a Google service-account JWT-bearer flow: a per-project OAuth Bearer access token is minted by RS256-signing a JWT with the service account key and exchanging it at Google's token endpoint, then sent as Authorization: Bearer on every call alongside the project ID. Custom auth tokens are a local Admin SDK signing operation, not a REST endpoint, so are out of scope.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [firebase.google.com](https://firebase.google.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `firebase` |

## Use it

Add Firebase from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.firebase.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Get Firestore Documents | `batchGetFirestoreDocuments` | Retrieves multiple Firestore documents by their full resource names in a single call, optionally within a transaction. |
| Batch Write Firestore Documents | `batchWriteFirestoreDocuments` | Applies a batch of write operations (update, delete, or transform) to multiple Firestore documents in one call. Writes are applied atomically per-document but are not an all-or-nothing transaction across documents. |
| Begin Firestore Transaction | `beginFirestoreTransaction` | Starts a new Firestore transaction and returns its ID, to be used with Batch Get, Commit, or Rollback. |
| Commit Firestore Transaction | `commitFirestoreTransaction` | Commits a set of writes to Firestore, optionally as part of a transaction started with Begin Firestore Transaction. |
| Copy Storage Object | `copyStorageObject` | Copies an object from a source bucket/path to a destination bucket/path within Cloud Storage, optionally across buckets. |
| Create Firebase Auth User | `createFirebaseAuthUser` | Creates a new Firebase Authentication user account with the given email/password, phone number, or profile fields. |
| Create Firestore Document | `createFirestoreDocument` | Creates a new document in the given Firestore collection, either with a specified document ID or an auto-generated one. |
| Delete Firebase Auth User | `deleteFirebaseAuthUser` | Permanently deletes a Firebase Authentication user account by its user ID. |
| Delete Firestore Document | `deleteFirestoreDocument` | Permanently deletes a single Firestore document by its full path. |
| Delete Realtime Database Data | `deleteRealtimeDatabaseData` | Deletes all data at the given path in the Realtime Database. |

<details>

<summary>See 25 more actions</summary>

* **Delete Storage Object** `deleteStorageObject`: Permanently deletes a single object from a Cloud Storage bucket.
* **Download Storage Object** `downloadStorageObject`: Downloads the raw content of an object stored in a Cloud Storage bucket.
* **Get Firebase Auth User** `getFirebaseAuthUser`: Looks up one or more Firebase Authentication user accounts by user ID, email address, or phone number.
* **Get Firestore Document** `getFirestoreDocument`: Retrieves a single Firestore document by its full path within the (default) database, e.g. 'users/alice'.
* **Get Remote Config Template** `getRemoteConfigTemplate`: Retrieves the current published Remote Config template for the project, including its parameters, parameter groups, conditions, and version metadata.
* **Get Storage Bucket** `getStorageBucket`: Retrieves metadata for a single Cloud Storage bucket by name, such as its location, storage class, and creation time.
* **Get Storage Object Metadata** `getStorageObjectMetadata`: Retrieves the metadata (size, content type, hashes, timestamps) of a single object in a Cloud Storage bucket without downloading its content.
* **List Firebase Auth Users** `listFirebaseAuthUsers`: Lists (queries) the Firebase Authentication user accounts in this project, with pagination.
* **List Firestore Collection IDs** `listFirestoreCollectionIds`: Lists the IDs of the top-level collections in the (default) Firestore database.
* **List Firestore Documents** `listFirestoreDocuments`: Lists the documents in a Firestore collection, with optional pagination, ordering, and field masking.
* **List Storage Buckets** `listStorageBuckets`: Lists the Cloud Storage buckets owned by this Firebase project, including the default Firebase Storage bucket once it has been provisioned.
* **List Storage Objects** `listStorageObjects`: Lists the objects (files) stored in a Cloud Storage bucket, optionally filtered to a folder-style prefix.
* **Publish Remote Config Template** `publishRemoteConfigTemplate`: Publishes a new Remote Config template for the project, replacing the currently active template. Requires the ETag of the template this update is based on (from Get Remote Config Template) to prevent overwriting a concurrent change; pass '*' to force-publish regardless of the current version.
* **Push Realtime Database Data** `pushRealtimeDatabaseData`: Adds a new child under the given path with a unique, chronologically-ordered key generated by the Realtime Database, and writes the given value there.
* **Read Realtime Database Data** `readRealtimeDatabaseData`: Reads the JSON data at a path in the project's default Firebase Realtime Database, with optional shallow, ordering, and range filters.
* **Rollback Firestore Transaction** `rollbackFirestoreTransaction`: Rolls back a Firestore transaction started with Begin Firestore Transaction, discarding any pending writes.
* **Run Firestore Aggregation Query** `runFirestoreAggregationQuery`: Runs an aggregation query (count, sum, or average) against a top-level Firestore collection without reading the individual matching documents.
* **Run Firestore Query** `runFirestoreQuery`: Runs a structured query against a top-level Firestore collection (filters, ordering, limit, offset) and returns the matching documents.
* **Send Firebase Auth Email Action Link** `sendFirebaseAuthEmailActionLink`: Sends (or generates) an out-of-band email action, such as a password reset, email verification, or email sign-in link, for a Firebase Authentication user.
* **Send Message** `sendMessage`: Sends a push notification and/or data payload through Firebase Cloud Messaging to a single device registration token, a topic, or a condition expression combining topics.
* **Update Firebase Auth User** `updateFirebaseAuthUser`: Updates an existing Firebase Authentication user's profile, credentials, custom claims, or disabled state.
* **Update Firestore Document** `updateFirestoreDocument`: Updates (patches) an existing Firestore document's fields, or creates it if it does not exist. Only the fields listed in updateFieldPaths are changed; other existing fields are left untouched. Supports a single comma-separated updateFieldPaths value (multiple repeated updateMask.fieldPaths query entries are not expressible through this connector - for multi-field partial updates, call this action once per field or replace the whole document's fields).
* **Update Realtime Database Data** `updateRealtimeDatabaseData`: Updates specific children under a path in the Realtime Database without overwriting the entire subtree - only the keys present in the update object are changed.
* **Upload Storage Object** `uploadStorageObject`: Uploads text content as a new object (or overwrites an existing one) in a Cloud Storage bucket using a simple media upload. Reliable for text content; binary content may be corrupted by UTF-8 re-encoding.
* **Write Realtime Database Data** `writeRealtimeDatabaseData`: Overwrites the JSON data at a path in the Realtime Database with the given value, replacing anything already there.

</details>
