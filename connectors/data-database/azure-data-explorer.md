---
description: "Azure Data Explorer (Kusto) — run KQL management and query commands against a cluster for real-time analytics on large datasets."
---

# Azure Data Explorer

Azure Data Explorer (Kusto) — run KQL management and query commands against a cluster for real-time analytics on large datasets. REST API v1 at {clusterUrl}/v1/rest/mgmt.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [kusto.windows.net](https://kusto.windows.net) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 55 |
| **Events** | 0 |
| **Slug** | `azureDataExplorer` |

## Use it

Add Azure Data Explorer from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureDataExplorer.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Query | `cancelQuery` | Requests cancellation of a currently running query, identified by the client request id returned from Show Running Queries. |
| Clear Table Data | `clearTableData` | Removes all rows from a table while keeping its schema intact. Requires Database Admin or Table Admin permission. |
| Create Merge Table | `createMergeTable` | Creates a table, or merges the supplied columns into an existing table of the same name rather than failing. Requires Database User permission. |
| Create Or Alter Function | `createOrAlterFunction` | Creates a stored function, or replaces the definition of an existing function of the same name, in the database metadata. |
| Create Table | `createTable` | Creates a new empty table in the database. If a table of the same name already exists the command succeeds without altering it. Requires Database User permission. |
| Drop Function | `dropFunction` | Removes a stored function from the database. Requires Database Admin or Function Admin permission. |
| Drop Materialized View | `dropMaterializedView` | Removes a materialized view and its materialized data from the database. Requires Database Admin or Materialized View Admin permission. |
| Drop Table | `dropTable` | Permanently removes a table and all of its data from the database. Requires Database Admin or Table Admin permission and cannot be undone once the retention period elapses. |
| Ingest Inline Into Table | `ingestInlineIntoTable` | Ingests a small batch of comma-separated rows supplied inline into an existing table. Intended for testing and small volumes rather than production data loading. |
| Rename Table | `renameTable` | Renames an existing table within the database. Requires Database Admin or Table Admin permission. |
| Run Management Command | `runManagementCommand` | Runs any Kusto management command against a database. Use this escape hatch for control commands that do not have a dedicated action; the command text must begin with a dot. |
| Run Query | `runQuery` | Runs a KQL query against a database on an Azure Data Explorer cluster and returns the result tables. Use the cluster's engine host, for example mycluster.westus.kusto.windows.net. |
| Run Query V2 | `runQueryV2` | Runs a KQL query using the v2 query endpoint, which returns a streaming frame-based response with richer result metadata than v1. |
| Set Or Append Table From Query | `setOrAppendTableFromQuery` | Appends the results of a KQL query into a table, creating the table from the query's result schema if it does not already exist. |
| Set Or Replace Table From Query | `setOrReplaceTableFromQuery` | Replaces the entire contents of a table with the results of a KQL query, creating the table if it does not already exist. |
| Show Cluster | `showCluster` | Returns the list of nodes composing the Azure Data Explorer cluster, including each node's machine name, state and role. |
| Show Cluster Principal Roles | `showClusterPrincipalRoles` | Returns the cluster-level security roles held by the connected identity, such as AllDatabasesAdmin or AllDatabasesViewer. |
| Show Cluster Principals | `showClusterPrincipals` | Returns every principal assigned a cluster-level security role, together with the role granted and the principal's display name and type. |
| Show Commands | `showCommands` | Returns the management commands recently executed on the cluster, including their text, state, duration and resource utilisation. |
| Show Commands And Queries | `showCommandsAndQueries` | Returns a combined view of the management commands and queries recently executed on the cluster, useful for auditing and workload analysis. |
| Show Continuous Exports | `showContinuousExports` | Returns the continuous export jobs defined in the database, which periodically export query results to an external table. |
| Show Database | `showDatabase` | Returns the properties of a single database, including its name, persistent storage location, version and access mode. |
| Show Database Caching Policy | `showDatabaseCachingPolicy` | Returns the caching policy of a database, which controls how much recent data is kept in the cluster's hot cache. |
| Show Database Extents | `showDatabaseExtents` | Returns the extents (data shards) across all tables in the database, with each extent's id, row count and size. |
| Show Database Principal Roles | `showDatabasePrincipalRoles` | Returns the security roles the connected identity holds on the specified database. |
| Show Database Principals | `showDatabasePrincipals` | Returns every principal assigned a security role on the database, such as admins, users, viewers and ingestors. |
| Show Database Retention Policy | `showDatabaseRetentionPolicy` | Returns the retention policy of a database, which controls how long ingested data is kept before it is automatically removed. |
| Show Database Schema | `showDatabaseSchema` | Returns a flat list of the database structure, with one row per column across all tables in the database. |
| Show Database Schema As JSON | `showDatabaseSchemaAsJson` | Returns the complete structure of a database as a single JSON document describing every table, column and data type. |
| Show Database Schema Violations | `showDatabaseSchemaViolations` | Returns any schema validation issues detected within the database, such as update policies or functions referencing missing entities. |
| Show Databases | `showDatabases` | Returns one record per database on the cluster that the connected identity has access to, including database name, persistent storage and pretty name. |
| Show Databases Entities | `showDatabasesEntities` | Returns the entities contained in the cluster's databases, such as tables, materialized views and functions, in a single flat list. |
| Show External Table Schema | `showExternalTableSchema` | Returns the schema of a single external table as a JSON document describing its columns and data types. |
| Show External Tables | `showExternalTables` | Returns all external tables defined in the database, which expose data held outside the cluster such as in blob storage or a data lake. |
| Show Function | `showFunction` | Returns the definition of a single stored function, including its parameter list and body. |
| Show Functions | `showFunctions` | Returns all stored functions in the database, with their name, parameters, body, folder and documentation string. |
| Show Ingestion Failures | `showIngestionFailures` | Returns recent ingestion failures for the database, including the failing operation, error reason and originating data source. |
| Show Journal | `showJournal` | Returns the metadata operation journal for the database in context, recording schema and policy changes and the principal that made each one. |
| Show Materialized View | `showMaterializedView` | Returns the definition and current state of a single materialized view, including its source table and last materialization time. |
| Show Materialized Views | `showMaterializedViews` | Returns all materialized views in the database, including their source table, aggregation query and current health state. |
| Show Operations | `showOperations` | Returns the set of admin operations recorded on the cluster, including each operation's id, state, start time and duration. |
| Show Queries | `showQueries` | Returns the recently completed queries the connected identity is permitted to see, with their text, duration, state and resource consumption. |
| Show Running Queries | `showRunningQueries` | Returns the queries currently executing on the cluster, including the client request id needed to cancel a running query. |
| Show Table | `showTable` | Returns the definition of a single table, including its column names and data types. |
| Show Table Caching Policy | `showTableCachingPolicy` | Returns the caching policy applied to a single table, controlling how much of its data is held in hot cache. |
| Show Table Details | `showTableDetails` | Returns detailed statistics for a single table, including row count, extent count, original and compressed data size and hot cache size. |
| Show Table Extents | `showTableExtents` | Returns the extents (data shards) belonging to a table, with each extent's id, row count, size and creation time. |
| Show Table Ingestion Mappings | `showTableIngestionMappings` | Returns the ingestion mappings defined on a table, which describe how incoming source fields map onto the table's columns. |
| Show Table Principals | `showTablePrincipals` | Returns every principal assigned a security role on the specified table, such as admins and ingestors. |
| Show Table Retention Policy | `showTableRetentionPolicy` | Returns the retention policy applied to a single table, including its soft-delete period and recoverability setting. |
| Show Table Schema As JSON | `showTableSchemaAsJson` | Returns a table's schema as a JSON document, the same shape returned when the table is created. |
| Show Table Update Policy | `showTableUpdatePolicy` | Returns the update policy of a table, which defines transformations automatically applied when data is ingested into a source table. |
| Show Tables | `showTables` | Returns every table in the database, with its name, owning database, folder and documentation string. |
| Show Tables Details | `showTablesDetails` | Returns detailed statistics for every table in the database, including row count, extent count, total data size and hot cache size. |
| Show Version | `showVersion` | Returns the build and service version information for an Azure Data Explorer cluster. This is a cluster-scoped management command and needs no database context. |
