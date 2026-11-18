---
description: "Azure Table Storage — NoSQL key-value store for structured, non-relational data."
hidden: true
---

# Azure Table Storage

<img src="../../.gitbook/assets/connectors/lg/azure-table-storage.png" alt="Azure Table Storage logo">

Azure Table Storage — NoSQL key-value store for structured, non-relational data. Create tables, list/query entities with OData filters, and insert new entities via the Azure Tables REST API ({account}.table.core.windows.net).

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [table.core.windows.net](https://table.core.windows.net) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `azureTableStorage` |

## Use it

Add Azure Table Storage from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureTableStorage.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Table | `createTable` | Creates a new table within a storage account. Table names must be alphanumeric, start with a letter, and be 3 to 63 characters long. |
| Delete Entity | `deleteEntity` | Deletes a single entity from a table by its PartitionKey and RowKey. The If-Match header is required: supply the entity's ETag for optimistic concurrency, or * to delete unconditionally. |
| Delete Table | `deleteTable` | Deletes a table and all of the entities it contains from the storage account. The table name is not available for reuse for at least 40 seconds afterwards. |
| Get Entity | `getEntity` | Retrieves a single entity from a table by its PartitionKey and RowKey, optionally projecting a subset of properties with $select. |
| Get Table ACL | `getTableAcl` | Returns the stored access policies specified on a table, which can be used with shared access signatures. Returns an XML SignedIdentifiers document. |
| Get Table Service Properties | `getTableServiceProperties` | Gets the properties of the Table service on a storage account, including logging, hour and minute metrics, and CORS rules. Returns an XML StorageServiceProperties document. |
| Get Table Service Stats | `getTableServiceStats` | Retrieves replication statistics for the Table service. This operation is available only on the secondary location endpoint ({account}-secondary.table.core.windows.net) and only when read-access geo-redundant replication (RA-GRS) is enabled on the storage account. |
| Insert Entity | `insertEntity` | Inserts a new entity into a table. Supply PartitionKey and RowKey plus any additional entity properties; Table Storage entities are schemaless, so extra properties are passed through as-is. Sends Prefer: return-content so the created entity is echoed in the response. |
| Insert Entity Batch Transaction | `insertEntityBatchTransaction` | Performs an entity group transaction against the Table service $batch endpoint, inserting one entity atomically. Engine limitation: the templating layer has no loop construct and cannot build a variable-length multipart/mixed payload, so this action carries exactly one insert operation, whereas the Azure API accepts up to 100 operations sharing a PartitionKey. All operations in a real transaction must target the same table and partition. |
| Insert Or Merge Entity | `insertOrMergeEntity` | Inserts a new entity, or merges the supplied properties into an existing entity with the same PartitionKey and RowKey. Sends no If-Match header, so it always succeeds regardless of the current ETag. Note: the Azure Table REST specification defines this operation on the MERGE verb; the fastn action engine's method enum does not include MERGE, so this action issues PATCH, which Azure Table Storage accepts as the equivalent. |

<details>

<summary>See 7 more actions</summary>

* **Insert Or Replace Entity** `insertOrReplaceEntity`: Inserts a new entity or replaces an existing one with the same PartitionKey and RowKey. Unlike Update Entity this upsert sends no If-Match header, so it always succeeds regardless of the current ETag.
* **Merge Entity** `mergeEntity`: Updates an existing entity by merging the supplied property values into it, leaving properties not named in the request untouched. Set ifMatch to an ETag for optimistic concurrency, or to * to force an unconditional merge. Note: the Azure Table REST specification defines this operation on the MERGE verb; the fastn action engine's method enum does not include MERGE, so this action issues PATCH, which Azure Table Storage accepts as the equivalent.
* **Query Entities** `queryEntities`: Queries entities in a table using OData $filter, $select and $top options. Returns matching entities under the value array.
* **Query Tables** `queryTables`: Enumerates the tables in a storage account. Returns the table names under the given Azure Storage account's Table service endpoint.
* **Set Table ACL** `setTableAcl`: Sets a stored access policy on a table for use with shared access signatures. Engine limitation: the action templating layer has no loop construct, so exactly one stored access policy can be set per call; the Azure API itself accepts up to five and this call replaces all existing policies with the single one supplied.
* **Set Table Service Properties** `setTableServiceProperties`: Sets the properties of the Table service on a storage account, controlling analytics logging and hour metrics. This rewrites account-wide service configuration and affects every table in the account. Engine limitation: the templating layer has no loop construct, so CORS rules cannot be expressed and are omitted from the request, which clears any existing CORS configuration.
* **Update Entity** `updateEntity`: Updates an existing entity by replacing it entirely. Properties omitted from the request are removed. Set ifMatch to an ETag for optimistic concurrency, or to * to force an unconditional update.

</details>
