---
description: "Peaka is a zero-ETL data integration platform that lets you connect APIs, databases and SaaS tools and query them together with SQL."
hidden: true
---

# Peaka

<img src="../../.gitbook/assets/connectors/peaka.png" alt="Peaka logo" width="64">

Peaka is a zero-ETL data integration platform that lets you connect APIs, databases and SaaS tools and query them together with SQL. This connector covers the complete Peaka Partner API: organizations, workspaces and projects, project API keys, connections and connection types, catalogs, schemas, tables and search, Peaka internal and BI tables and columns, saved and materialized queries, query folders, query execution and SQL transpilation, table and query exports, data caches, parametric and semantic catalogs, AI metadata and golden SQL, metadata refresh callbacks, the AI agent, embedded sessions and supported drivers.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [peaka.com](https://peaka.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `peaka` |

## Use it

Add Peaka from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.peaka.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add BI Columns | `addBiColumn` | Adds one or more columns to a Peaka BI Table. Each column definition includes its name, data type, display name, optional default value and nullability and uniqueness constraints. |
| Add Columns | `addColumn` | Adds one or more columns to a Peaka internal table. Each column definition includes its name, data type, display name, optional default value and nullability and uniqueness constraints. Supported data types are VARCHAR, BIGINT, BOOLEAN, DECIMAL, TIMESTAMP, TIME, DATE and UUID. |
| Add Or Remove Queries In Folder | `addOrRemoveQueriesInFolder` | Moves queries into or out of a folder. Queries in queryIdsAdded move to the folder's path; queries in queryIdsRemoved move to the root (/). |
| Add Relation To Metadata | `addRelation` | Adds a relation from a column of one table to a column of another table in the project's AI metadata, so the AI agent understands how tables join. |
| Cancel Export | `cancelExport` | Cancels a PENDING or RUNNING export, killing the running query and cleaning up partial artifacts. A no-op on an already finished job; idempotent. |
| Cancel Full Refresh Cache Update | `cancelFullRefreshCache` | Cancels a running full refresh of a cache (best effort). Previously cached data stays intact and the status becomes CANCELLED. Does not affect incremental syncs. |
| Cancel Incremental Cache Update | `cancelIncrementalCache` | Cancels a running incremental sync of a cache (best effort). Previously cached data stays intact and the status becomes CANCELLED. Does not affect full refreshes. |
| Cancel Materialized Query Refresh | `cancelMaterializedQuery` | Cancels the in-progress refresh of a materialized query, if any. |
| Chat With AI Agent | `chatWithAgent` | Sends a message to the Peaka AI agent for a project and returns the conversation, including the generated SQL, reasoning and summary. Pass threadId to continue a conversation or omit it to start a new thread; set noExecute to true to generate SQL without running it. |
| Chat With AI Agent (Stream) | `chatWithAgentStream` | Sends a message to the Peaka AI agent and streams the agent's intermediate and final responses as server-sent events. streamModes selects which event kinds are streamed. |

<details>

<summary>See 127 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Check If Table Is Cached | `isTableCached` | Checks whether a table has an active cache in Peaka, and whether and with which schedule types (FULL_REFRESH, INCREMENTAL) a cache can be created for it. |
| Complete OAuth2 Connection | `completeOAuth2Connection` | Completes an OAuth2-based connection after the user is redirected back from the third-party platform. Pass every query parameter received on the redirect as one string. See https://docs.peaka.com/how-to-guides/how-to-create-oauth2-based-connections-via-peaka. |
| Create API Key | `createApiKey` | Creates a project API key used to authenticate project-scoped requests to the Peaka API. The full key value is returned only once, at creation time, and cannot be retrieved later. |
| Create Batch Cache | `createBatchCache` | Creates multiple caches in one request. Each item follows the Create Cache schema; caches are created independently, and the response has one result per item with success, the created cache or an error. |
| Create BI Table | `createBiTable` | Creates a new, empty Peaka BI Table with the given name. BI Tables use column-oriented storage optimised for large datasets and bulk inserts; JSON data types are not supported. Add columns afterwards with Add BI Columns. |
| Create Cache | `createCache` | Creates a cache for a table in a catalog, copying data from the external source into Peaka's internal store for faster queries. Check isCacheable and supportedCacheTypes first. With no schedules the data is cached once; incrementalCacheSchedule syncs changes periodically; adding fullRefreshCacheSchedule also rebuilds the whole table periodically. Schedules use type BASIC with an ISO-8601 duration expression (for example PT6H), or type NONE. |
| Create Catalog | `createCatalog` | Creates a new catalog in the specified project from an existing connection. A catalog exposes a connected data source's schemas and tables for querying within Peaka. Some connectors accept extraParameters, for example Google Sheets requires the sheets to include. |
| Create Connection | `createConnection` | Creates a new connection to an external data source in a Peaka project. The credential object's structure depends on the connection type; call Get Connection Config first to learn the required fields. OAuth2 connection types return a URL to authorize, after which Complete OAuth2 Connection finishes the flow. |
| Create Golden SQL | `addGoldenSql` | Adds a golden SQL example to a Peaka project, pairing a natural-language prompt with a verified SQL query that the AI agent uses as guidance. |
| Create Parametric Table | `createParametricTable` | Creates a parametric table under a REST catalog, binding fixed query parameter values (such as _q_account) to a source table and exposing the result as a new named table. Date and timestamp values accept relative macros re-evaluated on each query: anchors @today, @yesterday, @now, @sow/@eow, @som/@eom, @soq/@eoq, @soy/@eoy with optional offsets such as @today-7d or @som-1M. |
| Create Project | `createProject` | Creates a new project within a Peaka workspace. A project is the unit of work where connections, catalogs, queries, tables and semantic catalogs are managed. |
| Create Project (Legacy) | `createProjectLegacy` | Deprecated by Peaka in favour of Create Project. Creates a new project in the organization's default workspace. |
| Create Query | `createQuery` | Creates a saved query in the project. PLAIN queries store SQL; MATERIALIZED queries are materialized immediately (queryable as peaka.mtquery.&lt;name&gt;) and can be kept fresh with a schedule. To materialize an existing query, send inputQueryRefId instead of inputQuery. An optional path places the query in a folder, creating intermediate folders. |
| Create Query Folder | `createQueryFolder` | Creates a query folder at the root level; folderName Reports becomes path /Reports. Intermediate parent folders are created automatically for a nested name. |
| Create Query Folder Under Parent | `createQueryFolderUnderParent` | Creates a query folder as a child of the specified parent folder, at {parentPath}/{folderName}. |
| Create Semantic Catalog | `createSemanticCatalog` | Creates a semantic catalog in the project. A semantic catalog is a virtual catalog grouping semantic tables, which are backed by saved queries. |
| Create Semantic Table | `createSemanticTable` | Creates a semantic table in a semantic catalog, mapping a saved query to a table so it can be queried with SQL like any other table. |
| Create Table | `createTable` | Creates a new, empty Peaka Table with the given name in the project. Add columns afterwards with Add Columns. |
| Create Workspace | `createWorkspace` | Creates a new workspace within a Peaka organization. A workspace groups projects to organize team collaboration and data operations. |
| Delete AI Agent Thread | `deleteAgentThread` | Permanently deletes an AI agent chat thread from a Peaka project. |
| Delete API Key | `deleteApiKey` | Deletes a project API key. Requests authenticated with the key are rejected afterwards. |
| Delete BI Column | `deleteBiColumn` | Permanently removes a column and its data from a Peaka BI Table. This action is irreversible. |
| Delete BI Table | `deleteBiTable` | Permanently deletes a Peaka BI Table and all its rows and columns. This action is irreversible. |
| Delete Cache | `deleteCache` | Permanently deletes a cache: cancels running and scheduled syncs, drops the cached table and removes its settings, history and status. Irreversible. |
| Delete Catalog | `deleteCatalog` | Permanently removes the specified catalog from the project, making all its schemas and tables unavailable for querying. This action is irreversible. |
| Delete Categorical Column Values | `deleteCategoricalColumnValues` | Deletes the categorical values stored in a column's AI metadata and removes the scheduled job that regenerates them. |
| Delete Column | `deleteColumn` | Permanently removes a column and its data from a Peaka Table. This action is irreversible. |
| Delete Connection | `deleteConnection` | Deletes a connection from a Peaka project. Any catalogs using this connection lose access to their data source. |
| Delete Golden SQL | `deleteGoldenSql` | Deletes a golden SQL example from a Peaka project. |
| Delete Parametric Table | `deleteParametricTable` | Deletes a parametric table identified by its target schema and table name. The source table is not affected. |
| Delete Project | `deleteProject` | Deletes a project within a Peaka workspace, together with its connections, catalogs, queries and tables. |
| Delete Project (Legacy) | `deleteProjectLegacy` | Deprecated by Peaka in favour of Delete Project. Deletes a project by its ID. |
| Delete Query | `deleteQuery` | Permanently deletes a saved query from a Peaka project by its ID. |
| Delete Query Folder | `deleteQueryFolder` | Deletes a query folder. By default only empty folders can be deleted; set force to true to recursively delete the folder with all sub-folders and contained queries. |
| Delete Relation From Metadata | `deleteRelation` | Deletes a relation from a table's AI metadata. |
| Delete Semantic Table | `deleteSemanticTable` | Deletes a semantic table from a semantic catalog. The underlying saved query is not affected. |
| Delete Table | `deleteTable` | Permanently deletes a Peaka Table and all its rows and columns. This action is irreversible. |
| Delete Workspace | `deleteWorkspace` | Deletes a workspace within a Peaka organization. |
| Execute Query | `executeQuery` | Executes a query and returns its columns and rows. Provide exactly one form: a raw SQL statement (with optional bindings), a saved query id, a qualifiedName such as peaka.query.samplequery, or a query builder object (from, with optional columns, filters, orderBy, limit and offset). format controls the row shape: CELL_TYPED (default, typed cell objects), SIMPLE (flat objects keyed by column) or COMPACT (arrays of values). |
| Export Query | `exportQuery` | Submits an asynchronous export of a saved query's results as CSV or JSONL. Returns a job id immediately; poll Get Export for the download URLs. |
| Export Table | `exportTable` | Submits an asynchronous export of a table as CSV or JSONL. Returns a job id immediately; poll Get Export for the download URLs. |
| Generate Categorical Column Values | `generateCategoricalColumnValues` | Generates the categorical values of a column from its data and stores them in the column's AI metadata, optionally regenerating them on a recurring frequency. |
| Generate Sample AI Questions | `generateSampleQuestions` | Uses the Peaka AI agent to generate sample natural-language questions a user could ask about the project's data for a given topic. |
| Generate Table Semantics | `generateTableSemantics` | Uses the Peaka AI agent to generate semantic descriptions for a table and its columns and stores them in the project's AI metadata. |
| Get AI Agent Thread | `getAgentThread` | Retrieves a single AI agent chat thread in a Peaka project, including its conversation state. |
| Get AI Agent Workflow Image | `getAgentWorkflowImage` | Returns a PNG diagram of the current Peaka AI agent workflow, showing the steps the agent follows to answer data questions. |
| Get Cache Execution History | `getCacheExecutionHistory` | Returns past sync executions of a cache, most recent first, with status, progress counters, errors and timestamps. Page with limit (default 10) and offset (default 0). Records are retained for 14 days. |
| Get Cache Settings | `getCacheSettings` | Retrieves a cache's configuration: target catalog, schema and table and the incremental and full refresh schedules. Use Get Cache Status for runtime status. |
| Get Cache Status | `getCacheStatus` | Returns the current status of a cache (NOT_INITIALIZED, RUNNING, COMPLETED, FAILED, CANCELLED or DELETED) with details of the last incremental sync and last full refresh, and the cache action logs unless excludeLogs is true. |
| Get Catalog | `getCatalog` | Retrieves the details of a single catalog by its ID: its name, display name, catalog type and associated connection ID. |
| Get Catalog Cache Statuses | `getCatalogCacheStatuses` | Returns the status of every cache belonging to one catalog of the project, each with the same information as Get Cache Status. |
| Get Catalog Metadata Relations | `getCatalogMetadataRelations` | Returns the table and column relations stored in the project's AI metadata for a catalog. |
| Get Connection | `getConnection` | Returns the name, type and URL of a connection in a Peaka project. |
| Get Connection Config | `getConnectionConfig` | Returns the configuration schema for a specific connection type, including required credential fields and their types. Use this to understand what parameters are needed when creating a connection of this type. |
| Get Connection Detail | `getConnectionDetail` | Returns the non-sensitive details of a connection in a Peaka project. The fields returned depend on the connection type. |
| Get Export | `getExport` | Returns the status of a single export job. For a SUCCEEDED job owned by the caller, files carries freshly presigned download URLs; other callers get downloadable false. |
| Get JDBC Driver | `getJdbcDriver` | Returns the JDBC connection details for connecting JDBC-compatible tools to Peaka's query engine. Access depends on the account's entitlement to supported drivers. |
| Get Materialized Query Status | `getMaterializedQueryStatus` | Returns refresh status and schedule information for a single materialized query. |
| Get Metadata Refresh Callback | `getMetadataRefreshCallback` | Returns the callback URL and token registered to be called when metadata refresh jobs finish for a Peaka project. |
| Get Metadata Refresh Job Status | `getMetadataRefreshJobStatus` | Returns the status of the most recent metadata refresh job for a catalog, including timings, attempts, progress and any failure reason. |
| Get Organization | `getOrganization` | Returns the specified Peaka organization, the highest-level resource that contains workspaces. |
| Get Project | `getProject` | Returns details of a project within a Peaka workspace, including its domain and webhook base URL. |
| Get Project (Legacy) | `getProjectLegacy` | Deprecated by Peaka in favour of Get Project. Returns details of a project by its ID without requiring the organization and workspace IDs. |
| Get Project Cache Statuses | `getProjectCacheStatuses` | Returns the status of every cache in the project, each with the same information as Get Cache Status. |
| Get Project Metadata | `getProjectMetadata` | Returns the AI metadata of a Peaka project (tables, columns, descriptions and categorical values), optionally filtered by catalog and schema. |
| Get Query | `getQuery` | Returns a single saved query by its ID, including its SQL, type, schedule and folder placement. |
| Get Query Folder | `getQueryFolder` | Returns a single query folder by its ID, including its direct child folders and the queries it contains. |
| Get Query Folder Tree | `getQueryFolderTree` | Returns the query folder hierarchy as a tree, optionally with the queries in each folder. Use rootFolderId to return only the subtree under one folder. |
| Get Sample CSV | `getSampleCsv` | Returns a sample CSV (text/csv) for a Peaka Table: a header row of column names followed by a few rows of example values. Use it as a template for files uploaded with Import CSV. |
| Get Schema Cache Statuses | `getSchemaCacheStatuses` | Returns the status of every cache within one schema of a catalog, each with the same information as Get Cache Status. |
| Get SQL Alchemy Driver | `getSqlAlchemyDriver` | Returns the SQL Alchemy connection string for Peaka's query engine for one catalog. |
| Get Table Statistics | `getTableStatistics` | Returns statistics for a table used by Peaka's query optimizer, including each column's distinctFraction (estimated share of distinct values relative to row count). Not supported for the internal catalog. |
| Get Workspace | `getWorkspace` | Returns details of a workspace within a Peaka organization. |
| Import CSV | `importCsv` | Imports rows from a CSV file into a Peaka Table using a multipart/form-data request. The request part is a JSON string with mappings (each with the target column name and either csvColumnName or csvColumnIndex) and containsHeader. Returns an import job with its status and progress. |
| Init Embedded Session | `initSession` | Initializes an Embedded Peaka session and returns a one-time session URL to load inside an iframe, embedding Peaka's connections, catalogs, caching and query UI in your application. Direct iframe embedding requires enabling Embedded UI in Developer Settings and registering your HTTPS domain. sessionMode selects the connector modal only or the full studio; theme, themeOverride and featureFlags customise the UI. |
| Init Embedded Session (Legacy) | `initSessionLegacy` | Deprecated by Peaka in favour of Init Embedded Session. Initializes an Embedded Peaka session for a project and returns a session URL to embed the Peaka UI in an iframe. |
| List AI Agent Threads | `listAgentThreads` | Lists the AI agent chat threads in a Peaka project, with each thread's ID, display name, source and timestamps. |
| List API Keys | `listApiKeys` | Lists the project API keys of a Peaka project. Key values are not returned; only their identifiers and metadata. |
| List BI Columns | `listBiColumns` | Lists all columns defined in a Peaka BI Table, with name, data type, display name, default value, nullability and uniqueness. |
| List BI Tables | `listBiTables` | Lists all Peaka BI Tables in the project. BI Tables use column-oriented storage optimised for large datasets, event data and bulk inserts, and do not support JSON data types. |
| List Catalog Table Columns | `listCatalogTableColumns` | Lists all columns for a specific table within a catalog, with name, data type, display name, default value and constraints. Some connectors expose virtual columns prefixed with _q_ for passing query-time parameters to the data source. |
| List Catalog Tables | `listCatalogTables` | Lists all tables under the specified schema of a catalog, with caching metadata (isCacheable, isDynamicTable, isCached, supportedCacheTypes). supportedCacheTypes lists FULL_REFRESH and/or INCREMENTAL; it is empty when the table is not cacheable. For the internal catalog this includes Peaka Tables and BI Tables. |
| List Catalogs | `listCatalogs` | Returns all catalogs registered in the specified project. Each catalog represents a data source connected to Peaka, such as Airtable, Stripe, or internal Peaka storage. Built-in catalogs for internal tables (Peaka Tables and BI Tables) and Peaka Queries are always present. |
| List Connection Config | `listConnectionConfig` | Lists every connection type Peaka supports, with its authorization type, category and the credential fields required to create a connection of that type. |
| List Connections | `listConnections` | Retrieves all connections for the specified project. A connection represents an authenticated link to an external data source such as Stripe, Airtable or PostgreSQL. |
| List Exports | `listExports` | Returns the project's export jobs, newest first, optionally filtered by status. Download URLs are omitted from the list; call Get Export for them. Page with limit and createdBefore (the previous page's last createdAt). |
| List Golden SQLs | `listGoldenSqls` | Lists the golden SQL examples stored for a Peaka project. Golden SQLs pair a natural-language prompt with a verified SQL query and are used to guide the AI agent. |
| List Materialized Query Statuses | `listMaterializedQueryStatuses` | Returns refresh status and schedule information for all materialized queries in the project. |
| List Organizations | `listOrganizations` | Retrieves all the organizations accessible with the Partner API key. An organization is the highest-level resource in Peaka and can contain multiple workspaces. |
| List Parametric Tables | `listParametricTables` | Lists the parametric tables defined under a catalog. A parametric table is a view of a REST-based table with fixed query parameter values (such as _q_account), so it can be queried without passing those parameters. |
| List Projects | `listProjects` | Lists all projects within a Peaka workspace. A project is the unit of work where connections, catalogs, queries, tables and semantic catalogs are managed. |
| List Projects (Legacy) | `listProjectsLegacy` | Deprecated by Peaka in favour of List Projects. Retrieves all projects accessible with the API key, across workspaces. |
| List Queries | `listQueries` | Returns all saved queries in the project, including each query's SQL, type, schedule and folder placement. |
| List Query Folders | `listQueryFolders` | Returns all query folders in the project as a flat list. |
| List Schemas | `listSchemas` | Returns all schemas available under the specified catalog. Schemas are logical groupings of tables; for external connectors they typically correspond to databases or namespaces exposed by the data source. |
| List Supported Drivers | `listSupportedDrivers` | Returns connection strings for all supported drivers (JDBC and SQL Alchemy) for connecting external tools to Peaka's query engine. |
| List Table Columns | `listTableColumns` | Lists all columns defined in a Peaka Table, with name, data type, display name, default value, nullability and uniqueness. |
| List Tables | `listInternalTables` | Lists all Peaka Tables in the project. A Peaka Table is an internal relational table that supports full CRUD, JSON data types and frequent edits; it is best suited for smaller datasets. |
| List Workspaces | `listWorkspaces` | Returns all workspaces under a Peaka organization. A workspace is a collaborative environment that groups projects; the hierarchy is organization, then workspace, then project. |
| Move Query Folder | `moveQueryFolder` | Moves a query folder to a new path in the hierarchy; child folders and their paths are updated accordingly. |
| Refresh Materialized Query | `refreshMaterializedQuery` | Triggers an immediate refresh of a materialized query. If the query has a schedule, the scheduled workflow is invoked; otherwise a one-time refresh starts. |
| Refresh Project Metadata | `refreshProjectMetadata` | Starts a job that refreshes the AI metadata of a Peaka project, optionally for one catalog, and optionally calls callbackURL (with callbackToken) when the job finishes. |
| Register Metadata Refresh Callback | `registerMetadataRefreshCallback` | Registers the callback URL, and optional token, that Peaka calls whenever a metadata refresh job finishes for the project. Replaces any previously registered callback. |
| Rename Query Folder | `renameQueryFolder` | Renames a query folder; its path segments are updated to reflect the new name. |
| Search Catalog | `searchCatalog` | Searches catalogs, schemas and tables across the project with a case-insensitive contains match, optionally restricted to a catalog or schema, with limit and offset paging. |
| Search Golden SQLs | `searchGoldenSqls` | Performs a semantic search over a Peaka project's golden SQL examples and returns the question and SQL pairs most similar to the supplied text. |
| Search Metadata | `searchMetadata` | Performs a semantic search over the project's AI metadata and returns the table metadata entries most relevant to the supplied text. |
| Share Catalog | `shareCatalog` | Shares a catalog from the current project with another Peaka project, giving the target project read access to the catalog's schemas and tables. |
| Share Semantic Catalog | `shareSemanticCatalog` | Shares a semantic catalog with another project, giving the target project read access to its schemas and tables. |
| Transpile SQL | `transpileSql` | Transpiles a SQL query from Peaka's Trino dialect into a target dialect such as mysql, postgres or bigquery, for reuse in other database systems. |
| Trigger Full Refresh Cache Update | `triggerFullRefreshCache` | Manually triggers a one-time full refresh of a cache, dropping the cached data and re-reading the entire source table. Monitor progress with Get Cache Status. |
| Trigger Incremental Cache Update | `triggerIncrementalCache` | Manually triggers a one-time incremental sync of a cache, applying inserts, updates and deletes since the last sync. Monitor progress with Get Cache Status. |
| Unregister Metadata Refresh Callback | `unregisterMetadataRefreshCallback` | Removes the metadata refresh job callback registered for a Peaka project, so Peaka stops calling the callback URL when metadata refresh jobs finish. |
| Update AI Agent Thread | `updateAgentThread` | Renames an AI agent chat thread in a Peaka project. |
| Update BI Column | `updateBiColumn` | Replaces the definition of an existing column in a Peaka BI Table. dataType and displayName are required; this is a full replacement, so omitted fields are reset. |
| Update Cache Settings | `updateCacheSettings` | Updates the sync schedules of an existing cache; the target table cannot change. A changed schedule replaces the running scheduled workflow for that mode. Set a schedule's type to NONE to disable that mode; BASIC expressions are ISO-8601 durations such as PT6H. |
| Update Catalog Metadata AI Usage | `updateCatalogMetadataAiUsage` | Enables or disables use of a catalog's metadata by the Peaka AI agent. |
| Update Column | `updateColumn` | Replaces the definition of an existing column in a Peaka Table. dataType and displayName are required; this is a full replacement, so omitted fields are reset (an omitted name is derived from displayName, an omitted defaultValue is cleared). |
| Update Connection | `updateConnection` | Updates a connection's name, credentials or other parameters. The body follows the same structure as Create Connection. |
| Update Project | `updateProject` | Updates the name and description of a project within a Peaka workspace. |
| Update Project (Legacy) | `updateProjectLegacy` | Deprecated by Peaka in favour of Update Project. Updates the name and description of a project by its ID. |
| Update Query | `updateQuery` | Updates the display name, SQL or schedule of a saved query; omitted fields keep their values. Sending queryType MATERIALIZED converts a plain query; sending inputQueryRefId re-syncs the SQL snapshot from the source query. Use Update Query Path to move a query between folders. |
| Update Query Path | `updateQueryPath` | Moves a saved query to the specified folder path, for example /analytics/dashboards. |
| Update Relation From Metadata | `updateRelation` | Updates the type of a relation stored in a table's AI metadata. |
| Update Schema Metadata AI Usage | `updateSchemaMetadataAiUsage` | Enables or disables use of a schema's metadata by the Peaka AI agent. |
| Update Table Metadata | `updateTableMetadata` | Updates the AI metadata of a table: its description, column descriptions and attributes (categorical values, keys, lineage) and whether the AI agent uses the table. |
| Update Workspace | `updateWorkspace` | Updates the name and description of a workspace within a Peaka organization. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Metadata Refresh Completed | `metadataRefreshCompleted` | Fires when a metadata refresh job finishes for the project (started by Refresh Project Metadata or by Peaka itself). On subscribe, fastn registers the trigger URL as the project's metadata refresh callback (POST /metadata/{projectId}/refresh/callback) with a generated callbackToken, then verifies the registration with Get Metadata Refresh Callback; on unsubscribe it removes the callback and verifies it is gone. Peaka keeps one callback per project, so subscribing replaces any callback registered outside fastn. Peaka does not publish the delivery payload; the schema below is modelled on the refresh job status object (Get Metadata Refresh Job Status) and is not captured from a real delivery. The callbackToken is stored as the trigger's secret; Peaka does not document how the token is presented on delivery, so verification is not configured. |
