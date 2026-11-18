---
description: "Google Cloud Datastore API v1 (https://datastore.googleapis.com/v1), also used by Firestore in Datastore mode."
---

# Google Cloud Datastore

Google Cloud Datastore API v1 (https://datastore.googleapis.com/v1), also used by Firestore in Datastore mode. Run queries, look up entities by key, allocate IDs, begin transactions, commit entity inserts and deletes, and roll back transactions. OAuth 2.0 (Google) authorization-code auth with the datastore scope.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [datastore.googleapis.com](https://datastore.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 7 |
| **Events** | 0 |
| **Slug** | `googleCloudDatastore` |

## Use it

Add Google Cloud Datastore from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudDatastore.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Allocate IDs | `allocateIds` | Allocates one new numeric ID for an entity of the given kind before it is inserted. Nothing is written to the database. Returns the completed key, whose path[0].id can be passed as keyId to Commit Insert Entity, Lookup Entity and Commit Delete Entity. Requires the https://www.googleapis.com/auth/datastore scope. |
| Begin Transaction | `beginTransaction` | Begins a new read-write Cloud Datastore transaction and returns its opaque transaction identifier. Pass it to Commit Insert Entity or Commit Delete Entity to apply changes atomically, or to Rollback to abandon it. Requires the https://www.googleapis.com/auth/datastore scope. |
| Commit Delete Entity | `commitDeleteEntity` | Commits a delete of one Cloud Datastore entity, identified by kind plus a key name or numeric ID, for example the demo entity made with Commit Insert Entity. Deleting a missing entity is not an error. By default the commit is TRANSACTIONAL and needs the transaction from Begin Transaction; set mode to NON_TRANSACTIONAL to commit without one. Returns the mutation results and commit time. Requires the https://www.googleapis.com/auth/datastore scope. |
| Commit Insert Entity | `commitInsertEntity` | Commits an insert of one new Cloud Datastore entity, identified by kind plus a key name or numeric ID (for example from Allocate IDs), with optional properties. By default the commit is TRANSACTIONAL and needs the transaction from Begin Transaction; set mode to NON_TRANSACTIONAL to commit without one. Fails if the entity already exists. Remove it afterwards with Commit Delete Entity. Returns the mutation results and commit time. Requires the https://www.googleapis.com/auth/datastore scope. |
| Lookup Entity | `lookup` | Looks up one Cloud Datastore entity by key (kind plus either a key name or a numeric ID). Returns it in found, or the key in missing when no such entity exists, which makes it a safe way to confirm an insert or delete. Read-only; requires the https://www.googleapis.com/auth/datastore scope. |
| Rollback | `rollback` | Rolls back (abandons) a Cloud Datastore transaction started with Begin Transaction, discarding it without applying any changes. Returns an empty object on success. Requires the https://www.googleapis.com/auth/datastore scope. |
| Run Query | `runQuery` | Runs a kind query against Cloud Datastore (or Firestore in Datastore mode) and returns up to limit entities of that kind, with their keys and properties. Use a small limit such as 5. Optional databaseId targets a named database and namespaceId a namespace. Read-only; requires the https://www.googleapis.com/auth/datastore scope. |
