---
description: "Azure Table Storage is a key-value store for structured data. Create tables and insert, query, update and delete entities."
hidden: true
---

# Azure Table Storage

<img src="../../.gitbook/assets/connectors/lg/azure-table-storage.png" alt="Azure Table Storage logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [table.core.windows.net](https://table.core.windows.net) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `azureTableStorage` |

## Setup

Your customers sign in to Azure Table Storage through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Azure Table Storage from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Azure Table Storage**.
2. Select **Connect** on the Azure Table Storage card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Azure Table Storage and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Azure Table Storage's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Table</td><td><code>createTable</code></td><td>Creates a new table within a storage account. Table names must be alphanumeric, start with a letter, and be 3 to 63 characters long.</td></tr><tr><td>Delete Entity</td><td><code>deleteEntity</code></td><td>Deletes a single entity from a table by its PartitionKey and RowKey. The If-Match header is required: supply the entity's ETag for optimistic concurrency, or * to delete unconditionally.</td></tr><tr><td>Delete Table</td><td><code>deleteTable</code></td><td>Deletes a table and all of the entities it contains from the storage account. The table name is not available for reuse for at least 40 seconds afterwards.</td></tr><tr><td>Get Entity</td><td><code>getEntity</code></td><td>Retrieves a single entity from a table by its PartitionKey and RowKey, optionally projecting a subset of properties with $select.</td></tr><tr><td>Get Table ACL</td><td><code>getTableAcl</code></td><td>Returns the stored access policies specified on a table, which can be used with shared access signatures. Returns an XML SignedIdentifiers document.</td></tr><tr><td>Get Table Service Properties</td><td><code>getTableServiceProperties</code></td><td>Gets the properties of the Table service on a storage account, including logging, hour and minute metrics, and CORS rules. Returns an XML StorageServiceProperties document.</td></tr><tr><td>Get Table Service Stats</td><td><code>getTableServiceStats</code></td><td>Retrieves replication statistics for the Table service. This operation is available only on the secondary location endpoint ({account}-secondary.table.core.windows.net) and only when read-access geo-redundant replication (RA-GRS) is enabled on the storage account.</td></tr><tr><td>Insert Entity</td><td><code>insertEntity</code></td><td>Inserts a new entity into a table. Supply PartitionKey and RowKey plus any additional entity properties; Table Storage entities are schemaless, so extra properties are passed through as-is. Sends Prefer: return-content so the created entity is echoed in the response.</td></tr><tr><td>Insert Entity Batch Transaction</td><td><code>insertEntityBatchTransaction</code></td><td>Performs an entity group transaction against the Table service $batch endpoint, inserting one entity atomically. Engine limitation: the templating layer has no loop construct and cannot build a variable-length multipart/mixed payload, so this action carries exactly one insert operation, whereas the Azure API accepts up to 100 operations sharing a PartitionKey. All operations in a real transaction must target the same table and partition.</td></tr><tr><td>Insert Or Merge Entity</td><td><code>insertOrMergeEntity</code></td><td>Inserts a new entity, or merges the supplied properties into an existing entity with the same PartitionKey and RowKey. Sends no If-Match header, so it always succeeds regardless of the current ETag. Note: the Azure Table REST specification defines this operation on the MERGE verb; the Fastn action engine's method enum does not include MERGE, so this action issues PATCH, which Azure Table Storage accepts as the equivalent.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Insert Or Replace Entity</td><td><code>insertOrReplaceEntity</code></td><td>Inserts a new entity or replaces an existing one with the same PartitionKey and RowKey. Unlike Update Entity this upsert sends no If-Match header, so it always succeeds regardless of the current ETag.</td></tr><tr><td>Merge Entity</td><td><code>mergeEntity</code></td><td>Updates an existing entity by merging the supplied property values into it, leaving properties not named in the request untouched. Set ifMatch to an ETag for optimistic concurrency, or to * to force an unconditional merge. Note: the Azure Table REST specification defines this operation on the MERGE verb; the Fastn action engine's method enum does not include MERGE, so this action issues PATCH, which Azure Table Storage accepts as the equivalent.</td></tr><tr><td>Query Entities</td><td><code>queryEntities</code></td><td>Queries entities in a table using OData $filter, $select and $top options. Returns matching entities under the value array.</td></tr><tr><td>Query Tables</td><td><code>queryTables</code></td><td>Enumerates the tables in a storage account. Returns the table names under the given Azure Storage account's Table service endpoint.</td></tr><tr><td>Set Table ACL</td><td><code>setTableAcl</code></td><td>Sets a stored access policy on a table for use with shared access signatures. Engine limitation: the action templating layer has no loop construct, so exactly one stored access policy can be set per call; the Azure API itself accepts up to five and this call replaces all existing policies with the single one supplied.</td></tr><tr><td>Set Table Service Properties</td><td><code>setTableServiceProperties</code></td><td>Sets the properties of the Table service on a storage account, controlling analytics logging and hour metrics. This rewrites account-wide service configuration and affects every table in the account. Engine limitation: the templating layer has no loop construct, so CORS rules cannot be expressed and are omitted from the request, which clears any existing CORS configuration.</td></tr><tr><td>Update Entity</td><td><code>updateEntity</code></td><td>Updates an existing entity by replacing it entirely. Properties omitted from the request are removed. Set ifMatch to an ETag for optimistic concurrency, or to * to force an unconditional update.</td></tr></tbody></table>

</details>

