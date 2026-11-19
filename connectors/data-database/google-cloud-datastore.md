---
description: "Google Cloud Datastore is a NoSQL document database. Look up, insert and delete entities, run queries and manage transactions."
hidden: true
---

# Google Cloud Datastore

<img src="../../.gitbook/assets/connectors/lg/google-cloud-datastore.png" alt="Google Cloud Datastore logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [datastore.googleapis.com](https://datastore.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudDatastore` |

## Setup

Your customers sign in to Google Cloud Datastore through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Cloud Datastore from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudDatastore.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Allocate IDs</td><td><code>allocateIds</code></td><td>Allocates one new numeric ID for an entity of the given kind before it is inserted. Nothing is written to the database. Returns the completed key, whose path[0].id can be passed as keyId to Commit Insert Entity, Lookup Entity and Commit Delete Entity. Requires the https://www.googleapis.com/auth/datastore scope.</td></tr><tr><td>Begin Transaction</td><td><code>beginTransaction</code></td><td>Begins a new read-write Cloud Datastore transaction and returns its opaque transaction identifier. Pass it to Commit Insert Entity or Commit Delete Entity to apply changes atomically, or to Rollback to abandon it. Requires the https://www.googleapis.com/auth/datastore scope.</td></tr><tr><td>Commit Delete Entity</td><td><code>commitDeleteEntity</code></td><td>Commits a delete of one Cloud Datastore entity, identified by kind plus a key name or numeric ID, for example the demo entity made with Commit Insert Entity. Deleting a missing entity is not an error. By default the commit is TRANSACTIONAL and needs the transaction from Begin Transaction; set mode to NON_TRANSACTIONAL to commit without one. Returns the mutation results and commit time. Requires the https://www.googleapis.com/auth/datastore scope.</td></tr><tr><td>Commit Insert Entity</td><td><code>commitInsertEntity</code></td><td>Commits an insert of one new Cloud Datastore entity, identified by kind plus a key name or numeric ID (for example from Allocate IDs), with optional properties. By default the commit is TRANSACTIONAL and needs the transaction from Begin Transaction; set mode to NON_TRANSACTIONAL to commit without one. Fails if the entity already exists. Remove it afterwards with Commit Delete Entity. Returns the mutation results and commit time. Requires the https://www.googleapis.com/auth/datastore scope.</td></tr><tr><td>Lookup Entity</td><td><code>lookup</code></td><td>Looks up one Cloud Datastore entity by key (kind plus either a key name or a numeric ID). Returns it in found, or the key in missing when no such entity exists, which makes it a safe way to confirm an insert or delete. Read-only; requires the https://www.googleapis.com/auth/datastore scope.</td></tr><tr><td>Rollback</td><td><code>rollback</code></td><td>Rolls back (abandons) a Cloud Datastore transaction started with Begin Transaction, discarding it without applying any changes. Returns an empty object on success. Requires the https://www.googleapis.com/auth/datastore scope.</td></tr><tr><td>Run Query</td><td><code>runQuery</code></td><td>Runs a kind query against Cloud Datastore (or Firestore in Datastore mode) and returns up to limit entities of that kind, with their keys and properties. Use a small limit such as 5. Optional databaseId targets a named database and namespaceId a namespace. Read-only; requires the https://www.googleapis.com/auth/datastore scope.</td></tr></tbody></table>

## Events

Google Cloud Datastore has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
