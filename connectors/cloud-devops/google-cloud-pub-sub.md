---
description: "Google Cloud Pub/Sub REST API v1 connector (https://pubsub.googleapis.com/v1)."
hidden: true
---

# Google Cloud Pub/Sub

<img src="../../.gitbook/assets/connectors/lg/google-cloud-pub-sub.png" alt="Google Cloud Pub/Sub logo">

Google Cloud Pub/Sub REST API v1 connector (https://pubsub.googleapis.com/v1). Manage topics (create, get, list, patch, delete, publish messages, list attached subscriptions and snapshots, IAM policy), subscriptions (create, get, list, patch, delete, pull, acknowledge, modify ack deadline, modify push config, seek, detach, IAM policy), snapshots (create, get, list, patch, delete, IAM policy), and schemas (create, get, list, list revisions, commit, rollback, delete revision, delete, validate, validate message, IAM policy). Resource names are project-scoped (projects/{project}/topics/{topic}, etc.). OAuth 2.0 (Google) authorization-code auth with the single scope https://www.googleapis.com/auth/pubsub.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloud.google.com](https://cloud.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudPubSub` |

## Use it

Add Google Cloud Pub/Sub from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudPubSub.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Acknowledge Messages | `acknowledgeMessages` | Acknowledge one or more messages previously pulled from a subscription, using the ackIds returned by Pull Messages, so they are not redelivered. |
| Commit Schema | `commitSchema` | Commit a new revision of an existing schema. The supplied schema object (with its full resource name, type, and definition) becomes the latest revision. |
| Create Schema | `createSchema` | Create a schema in a project. The schema ID is supplied as a query parameter and the body carries the schema type (Protocol Buffer or Avro) and its definition. |
| Create Snapshot | `createSnapshot` | Create a snapshot from a subscription, capturing the message acknowledgement state of that subscription's topic so a subscription can later be sought back to this point. The snapshot name is taken from the URL path. |
| Create Subscription | `createSubscription` | Create a Pub/Sub subscription on a topic. The subscription name is taken from the URL path; the request body must include the topic and may configure push/BigQuery/Cloud Storage delivery, ack deadline, retention, ordering, filtering, dead-letter and retry policies, and exactly-once delivery. |
| Create Topic | `createTopic` | Create a Pub/Sub topic in the given project. The topic name is taken from the URL path; the request body carries optional configuration such as labels, message storage policy, message retention duration, CMEK key, schema settings, and ingestion data source settings. |
| Delete Schema | `deleteSchema` | Delete a schema and all of its revisions. |
| Delete Schema Revision | `deleteSchemaRevision` | Delete a specific revision of a schema. The most recent revision cannot be deleted while other revisions remain, and a schema's only revision cannot be deleted with this method. |
| Delete Snapshot | `deleteSnapshot` | Delete a Pub/Sub snapshot. Subscriptions can no longer be sought to a deleted snapshot. |
| Delete Subscription | `deleteSubscription` | Delete a Pub/Sub subscription. All messages retained in the subscription are immediately dropped and cannot be delivered. |

<details>

<summary>See 36 more actions</summary>

* **Delete Topic** `deleteTopic`: Delete a Pub/Sub topic. Existing subscriptions are not deleted but their topic field is set to _deleted-topic_.
* **Detach Subscription** `detachSubscription`: Detach a subscription from its topic. All messages retained in the subscription are dropped and the subscription stops receiving new messages; publishers can continue publishing to the topic.
* **Get Schema** `getSchema`: Retrieve a schema by its project and schema ID. Use the view parameter to control whether the definition is included.
* **Get Schema IAM Policy** `getSchemaIamPolicy`: Get the IAM access control policy for a Pub/Sub schema.
* **Get Snapshot** `getSnapshot`: Retrieve the configuration of a single Pub/Sub snapshot by its project and snapshot ID.
* **Get Snapshot IAM Policy** `getSnapshotIamPolicy`: Get the IAM access control policy for a Pub/Sub snapshot.
* **Get Subscription** `getSubscription`: Retrieve the configuration of a single Pub/Sub subscription by its project and subscription ID.
* **Get Subscription IAM Policy** `getSubscriptionIamPolicy`: Get the IAM access control policy for a Pub/Sub subscription.
* **Get Topic** `getTopic`: Retrieve the configuration of a single Pub/Sub topic by its project and topic ID.
* **Get Topic IAM Policy** `getTopicIamPolicy`: Get the IAM access control policy for a Pub/Sub topic.
* **List Schema Revisions** `listSchemaRevisions`: List all revisions of a schema, with optional detail view and pagination.
* **List Schemas** `listSchemas`: List all schemas in a project, with optional detail view and pagination.
* **List Snapshots** `listSnapshots`: List all Pub/Sub snapshots in a project, with optional pagination.
* **List Subscriptions** `listSubscriptions`: List all Pub/Sub subscriptions in a project, with optional pagination.
* **List Topic Snapshots** `listTopicSnapshots`: List the names of snapshots taken from subscriptions attached to a Pub/Sub topic, with optional pagination.
* **List Topic Subscriptions** `listTopicSubscriptions`: List the names of subscriptions attached to a Pub/Sub topic, with optional pagination.
* **List Topics** `listTopics`: List all Pub/Sub topics in a project, with optional pagination.
* **Modify Ack Deadline** `modifyAckDeadline`: Modify the acknowledgement deadline for specific pulled messages. Use to extend processing time or, with a deadline of 0, to immediately make messages available for redelivery (nack).
* **Modify Push Config** `modifyPushConfig`: Modify the push delivery configuration of a subscription. Supply an empty pushConfig to switch the subscription from push to pull delivery.
* **Publish Messages** `publishToTopic`: Publish one or more messages to a Pub/Sub topic. Each message's data must be base64-encoded; attributes and an ordering key are optional. Returns the server-assigned message IDs in publish order.
* **Pull Messages** `pullSubscription`: Pull messages from a Pub/Sub subscription. Returns received messages each with an ackId that must be passed to Acknowledge Messages to confirm processing.
* **Rollback Schema** `rollbackSchema`: Create a new schema revision that is a copy of the given revision ID, effectively rolling the schema back to an earlier definition.
* **Seek Subscription** `seekSubscription`: Seek a subscription to a past point in time or to a snapshot, resetting the acknowledgement state of messages. Provide exactly one of time or snapshot.
* **Set Schema IAM Policy** `setSchemaIamPolicy`: Set (replace) the IAM access control policy for a Pub/Sub schema. The supplied policy overwrites the existing one.
* **Set Snapshot IAM Policy** `setSnapshotIamPolicy`: Set (replace) the IAM access control policy for a Pub/Sub snapshot. The supplied policy overwrites the existing one.
* **Set Subscription IAM Policy** `setSubscriptionIamPolicy`: Set (replace) the IAM access control policy for a Pub/Sub subscription. The supplied policy overwrites the existing one.
* **Set Topic IAM Policy** `setTopicIamPolicy`: Set (replace) the IAM access control policy for a Pub/Sub topic. The supplied policy overwrites the existing one.
* **Test Schema IAM Permissions** `testSchemaIamPermissions`: Return which of the specified IAM permissions the caller holds on a Pub/Sub schema.
* **Test Snapshot IAM Permissions** `testSnapshotIamPermissions`: Return which of the specified IAM permissions the caller holds on a Pub/Sub snapshot.
* **Test Subscription IAM Permissions** `testSubscriptionIamPermissions`: Return which of the specified IAM permissions the caller holds on a Pub/Sub subscription.
* **Test Topic IAM Permissions** `testTopicIamPermissions`: Return which of the specified IAM permissions the caller holds on a Pub/Sub topic.
* **Update Snapshot** `updateSnapshot`: Update an existing Pub/Sub snapshot. Supply the fields to change inside the snapshot object and list their paths in updateMask; only the masked fields (typically labels or expireTime) are modified.
* **Update Subscription** `updateSubscription`: Update an existing Pub/Sub subscription. Supply the fields to change inside the subscription object and list their paths in updateMask; only the masked fields are modified.
* **Update Topic** `updateTopic`: Update an existing Pub/Sub topic. Supply the fields to change inside the topic object and list their paths in updateMask; only the masked fields are modified.
* **Validate Message** `validateMessage`: Validate a message against a schema, either an existing named schema or an inline schema definition, using the given encoding. Returns an empty success response if the message conforms.
* **Validate Schema** `validateSchema`: Validate a schema definition without creating it. Returns an empty success response if the schema type and definition are well-formed, or an error describing the problem.

</details>
