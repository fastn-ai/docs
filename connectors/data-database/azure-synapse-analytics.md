---
description: "Connect to Azure Synapse Analytics data-plane APIs — pipelines, datasets, linked services, data flows, triggers, notebooks, Spark jobs (Livy), SQL pools, role…"
hidden: true
---

# Azure Synapse Analytics

<img src="../../.gitbook/assets/connectors/lg/azure-synapse-analytics.png" alt="Azure Synapse Analytics logo">

Connect to Azure Synapse Analytics data-plane APIs — pipelines, datasets, linked services, data flows, triggers, notebooks, Spark jobs (Livy), SQL pools, role assignments, managed private endpoints, link connections, KQL scripts, and more.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [azure.microsoft.com](https://azure.microsoft.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `azureSynapseAnalytics` |

## Use it

Add Azure Synapse Analytics from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.azureSynapseAnalytics.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Data Flow To Debug Session | `addDataFlowToDebugSession` | Adds a data flow into an existing debug session, returning the job version. |
| Append Library Chunk | `appendLibraryChunk` | BLOCKED: Appends a binary chunk to a library file being uploaded (PUT /libraries/{libraryName}?comp=appendblock). Requires application/octet-stream body with binary content up to 4 MiB per call. Blocked — fastn does not support binary/octet-stream request bodies. |
| Cancel Pipeline Run | `cancelPipelineRun` | Cancels a pipeline run by its run ID. Optionally cancels child pipelines recursively. |
| Cancel Spark Batch Job | `cancelSparkBatchJob` | Cancels a running Spark batch job by its batch ID. |
| Cancel Spark Statement | `cancelSparkStatement` | Kill (cancel) a statement within a Spark session. |
| Cancel Trigger Instance | `cancelTriggerInstance` | Cancels a single trigger instance identified by triggerName and runId. |
| Check Access Synapse RBAC | `checkAccessSynapseRbac` | Check if the given principalId has access to perform a list of actions at a given scope. Returns an access decision per action. |
| Create Data Flow Debug Session | `createDataFlowDebugSession` | Creates a data flow debug session. Returns sessionId on completion (long-running operation). |
| Create Library | `createLibrary` | Creates a library with the given library name in the Synapse workspace. This is a long-running operation. |
| Create Managed Private Endpoint | `createManagedPrivateEndpoint` | Create or update a managed private endpoint in a managed virtual network. Requires the privateLinkResourceId and groupId of the target Azure resource. |
| Create or Update Credential | `createOrUpdateCredential` | Creates or updates a managed identity credential in the Synapse workspace. |
| Create Or Update Dataflow | `createOrUpdateDataflow` | Creates or updates a data flow in the workspace. |
| Create or Update Dataset | `createOrUpdateDataset` | Creates or updates a dataset in the Azure Synapse workspace. For update, provide ifMatch with the dataset ETag or '*' for unconditional update. |
| Create Or Update KQL Script | `createOrUpdateKqlScript` | Creates or updates a KQL Script in the workspace. This is a long-running operation. |
| Create Or Update Link Connection | `createOrUpdateLinkConnection` | Creates or updates a link connection in the workspace. Provide all required properties including source database, target database, landing zone, and compute configuration. |
| Create or Update Linked Service | `createOrUpdateLinkedService` | Creates or updates a linked service in the Azure Synapse Analytics workspace. Supports all linked service types (AzureStorage, AzureSqlDatabase, AzureBlobStorage, etc.). This is a long-running operation. |
| Create Or Update Notebook | `createOrUpdateNotebook` | Creates or updates a Notebook in the Azure Synapse workspace. This is a long-running operation — poll getNotebookOperationResult with the returned operation ID to check completion. |
| Create Or Update Pipeline | `createOrUpdatePipeline` | Creates or updates a pipeline in the Azure Synapse workspace. |
| Create Or Update Spark Configuration | `createOrUpdateSparkConfiguration` | Creates or updates a Spark configuration in the workspace. Optionally accepts an If-Match ETag header for conditional updates. This is a long-running operation. |
| Create Or Update Spark Job Definition | `createOrUpdateSparkJobDefinition` | Creates or updates a Spark Job Definition in the workspace. This is a long-running operation. |
| Create Or Update SQL Script | `createOrUpdateSqlScript` | Creates or updates a SQL Script in the Azure Synapse Analytics workspace. |
| Create Or Update Trigger | `createOrUpdateTrigger` | Creates or updates a trigger in the Synapse workspace. Supports ScheduleTrigger, BlobEventsTrigger, CustomEventsTrigger, RerunTumblingWindowTrigger, and TumblingWindowTrigger types. |
| Create Pipeline Run | `createPipelineRun` | Creates a run of a pipeline in the Azure Synapse workspace. Returns the run ID. |
| Create Role Assignment | `createRoleAssignment` | Create a Synapse RBAC role assignment by specifying a roleAssignmentId (UUID), roleId, principalId, and scope. |
| Create Spark Batch Job | `createSparkBatchJob` | Create a new Spark batch job under the specified Spark pool. Requires a job name and the path to the main file to execute. |
| Create Spark Session | `createSparkSession` | Create a new interactive Spark session under the specified Spark pool. Requires a session name. |
| Create Spark Statement | `createSparkStatement` | Create and execute a statement within a Spark session. Supports Spark (Scala), PySpark, .NET Spark, and SQL. |
| Debug Spark Job Definition | `debugSparkJobDefinition` | Debugs a Spark Job Definition by running it in debug mode. This is a long-running operation that returns a SparkBatchJob tracked via the Location header. |
| Delete Credential | `deleteCredential` | Deletes a credential by name from the Synapse workspace. This is a long-running operation. |
| Delete Data Flow Debug Session | `deleteDataFlowDebugSession` | Deletes a data flow debug session. |
| Delete Dataflow | `deleteDataflow` | Deletes a data flow from the workspace. |
| Delete Dataset | `deleteDataset` | Deletes a dataset from the Azure Synapse workspace. Returns 200, 202 (accepted for async), or 204 (no content). |
| Delete KQL Script | `deleteKqlScript` | Delete a KQL script by name. Returns 200, 202, or 204 on success. This is a long-running operation. |
| Delete Library | `deleteLibrary` | Deletes a library resource by name from the Synapse workspace. This is a long-running operation. |
| Delete Link Connection | `deleteLinkConnection` | Delete a link connection by name. Returns 200 OK or 204 No Content on success. |
| Delete Linked Service | `deleteLinkedService` | Deletes a linked service by name from the Azure Synapse Analytics workspace. This is a long-running operation. |
| Delete Managed Private Endpoint | `deleteManagedPrivateEndpoint` | Delete a managed private endpoint from a managed virtual network. Returns 202 Accepted (async deletion) or 204 if already deleted. |
| Delete Notebook | `deleteNotebook` | Deletes a Notebook from the Azure Synapse workspace. This is a long-running operation — poll getNotebookOperationResult to confirm completion. |
| Delete Pipeline | `deletePipeline` | Deletes a pipeline from the Azure Synapse workspace. |
| Delete Role Assignment | `deleteRoleAssignment` | Delete a Synapse RBAC role assignment by its role assignment ID. Optionally filter by scope. |
| Delete Spark Configuration | `deleteSparkConfiguration` | Deletes a Spark configuration by name. Returns 200, 202, or 204 on success. This is a long-running operation. |
| Delete Spark Job Definition | `deleteSparkJobDefinition` | Deletes a Spark Job Definition from the workspace. This is a long-running operation. |
| Delete Spark Session | `deleteSparkSession` | Cancels (deletes) a running Spark session by its session ID. |
| Delete SQL Script | `deleteSqlScript` | Deletes a SQL Script from the Azure Synapse Analytics workspace. |
| Delete Trigger | `deleteTrigger` | Deletes a trigger from the Synapse workspace. |
| Edit Link Connection Tables | `editLinkConnectionTables` | Edit (add, update, or remove) link tables for a link connection. Provide an array of link table definitions with operationType (add/update/remove). |
| Execute Data Flow Debug Command | `executeDataFlowDebugCommand` | Executes a data flow debug command (preview, statistics, or expression query) against an active debug session. |
| Execute Spark Job Definition | `executeSparkJobDefinition` | Executes (runs) a Spark Job Definition on a Spark pool. This is a long-running operation that returns a SparkBatchJob. The operation is tracked via the Location header. |
| Flush Library | `flushLibrary` | Flushes a library resource by name from the Synapse workspace. This is a long-running operation. |
| Get Big Data Pool | `getBigDataPool` | Gets a specific Apache Spark Big Data Pool by name from the Azure Synapse Analytics workspace. |
| Get Credential | `getCredential` | Gets a credential by name from the Synapse workspace. |
| Get Dataflow | `getDataflow` | Gets a data flow by name from the workspace. |
| Get Dataset | `getDataset` | Gets a dataset by name from the Azure Synapse workspace. |
| Get GitHub Access Token | `getGitHubAccessToken` | Exchange a GitHub OAuth access code for a GitHub access token for Git integration with the Synapse workspace. |
| Get Integration Runtime | `getIntegrationRuntime` | Gets a specific Integration Runtime by name from the Azure Synapse Analytics workspace. |
| Get KQL Script | `getKqlScript` | Get a KQL script by name from the workspace. |
| Get Library | `getLibrary` | Gets a library resource by name from the Synapse workspace. |
| Get Library Operation Result | `getLibraryOperationResult` | Get the operation result for a library operation (create, delete, flush) by operation ID. |
| Get Link Connection | `getLinkConnection` | Get a specific link connection by name. Returns the full link connection resource including properties. |
| Get Link Connection Detailed Status | `getLinkConnectionDetailedStatus` | Get the detailed status of a link connection, including running state, error info, continuous run id, refresh status, and landing zone credential expiry. |
| Get Linked Service | `getLinkedService` | Gets a linked service by name from the Azure Synapse Analytics workspace. |
| Get Managed Private Endpoint | `getManagedPrivateEndpoint` | Get a specific managed private endpoint by name from a managed virtual network. |
| Get Notebook | `getNotebook` | Gets a specific Notebook by name from the Azure Synapse workspace. |
| Get Notebook Operation Result | `getNotebookOperationResult` | Polls the result of a long-running notebook operation (create, update, delete, rename). Returns 200 when complete, 202 while still in progress, 201 on creation success, 204 when no content on deletion. |
| Get Operation Result | `getOperationResult` | Get the result of a generic operation by operation ID in the Synapse workspace. |
| Get Operation Status | `getOperationStatus` | Get the status of a generic operation by operation ID in the Synapse workspace. |
| Get Pipeline | `getPipeline` | Gets a pipeline by name from the Azure Synapse workspace. |
| Get Pipeline Run | `getPipelineRun` | Gets a pipeline run by its run ID. |
| Get Role Assignment | `getRoleAssignment` | Get a Synapse RBAC role assignment by its role assignment ID. |
| Get Role Definition | `getRoleDefinition` | Get a Synapse RBAC role definition by its role definition ID. |
| Get Spark Batch Job | `getSparkBatchJob` | Gets a single Spark batch job by its batch ID. |
| Get Spark Configuration | `getSparkConfiguration` | Gets a Spark configuration by name from the workspace. |
| Get Spark Job Definition | `getSparkJobDefinition` | Gets a specific Spark Job Definition by name from the workspace. |
| Get Spark Session | `getSparkSession` | Gets a single Spark session by its session ID. |
| Get Spark Statement | `getSparkStatement` | Gets a single statement within a Spark session. |
| Get SQL Pool | `getSqlPool` | Gets a specific SQL Pool by name from the Azure Synapse Analytics workspace. |
| Get SQL Script | `getSqlScript` | Gets a specific SQL Script by name from the Azure Synapse Analytics workspace. |
| Get Trigger | `getTrigger` | Gets a trigger by name from the Synapse workspace. |
| Get Trigger Event Subscription Status | `getTriggerEventSubscriptionStatus` | Gets the event subscription status of a trigger. |
| Get Workspace | `getWorkspace` | Gets workspace information for the Azure Synapse Analytics workspace. |
| List Big Data Pools | `listBigDataPools` | Lists all Apache Spark Big Data Pools in the Azure Synapse Analytics workspace. |
| List Credentials | `listCredentials` | Lists all credentials in the Synapse workspace. |
| List Dataflows | `listDataflows` | Lists all data flows in the workspace. |
| List Datasets | `listDatasets` | Lists all datasets in the Azure Synapse workspace. Returns a paginated list of DatasetResource objects. |
| List Integration Runtimes | `listIntegrationRuntimes` | Lists all Integration Runtimes in the Azure Synapse Analytics workspace. |
| List KQL Scripts | `listKqlScripts` | Get all KQL scripts in the workspace. Returns a paginated list of KqlScriptResource objects. |
| List Libraries | `listLibraries` | Lists all library resources in the Synapse workspace. |
| List Link Connection Link Tables | `listLinkConnectionLinkTables` | List the link tables configured for a specific link connection. |
| List Link Connections | `listLinkConnections` | List all link connections in the workspace. Returns a paginated list of link connection resources. |
| List Linked Services | `listLinkedServices` | Lists all linked services in the Azure Synapse Analytics workspace. |
| List Managed Private Endpoints | `listManagedPrivateEndpoints` | List all managed private endpoints in a managed virtual network for the Synapse workspace. |
| List Notebooks | `listNotebooks` | Lists all Notebooks in the Azure Synapse workspace. Returns paginated results with a nextLink for subsequent pages. |
| List Notebooks Summary | `listNotebooksSummary` | Lists a summary of Notebooks in the Azure Synapse workspace. Returns lightweight notebook representations with a nextLink for pagination. |
| List Pipelines | `listPipelines` | Lists all pipelines in the Azure Synapse workspace. |
| List RBAC Scopes | `listRbacScopes` | List all available Synapse RBAC scopes (e.g. workspace, Spark pools, SQL pools). |
| List Role Assignments | `listRoleAssignments` | List all Synapse RBAC role assignments. Optionally filter by roleId, principalId, or scope. Supports pagination via the x-ms-continuation header. |
| List Role Definitions | `listRoleDefinitions` | List all Synapse RBAC role definitions. Optionally filter by isBuiltIn flag or scope. |
| List Spark Applications | `listSparkApplications` | Get the list of Spark applications running in the Synapse workspace for monitoring purposes. |
| List Spark Batch Jobs | `listSparkBatchJobs` | List all Spark batch jobs running under a particular Spark pool. Returns a paginated collection of SparkBatchJob objects. |
| List Spark Configurations | `listSparkConfigurations` | Lists all Spark configurations in the workspace. Returns a paginated list of SparkConfigurationResource objects. |
| List Spark Job Definitions | `listSparkJobDefinitions` | Lists all Spark Job Definitions in the workspace. Returns a paginated list with nextLink for continuation. |
| List Spark Sessions | `listSparkSessions` | List all Spark sessions running under a particular Spark pool. Returns a paginated collection of SparkSession objects. |
| List Spark Statements | `listSparkStatements` | Gets a list of statements within a Spark session. |
| List SQL Pools | `listSqlPools` | Lists all SQL Pools in the Azure Synapse Analytics workspace. |
| List SQL Query Activity | `listSqlQueryActivity` | Get active SQL on-demand and dedicated SQL pool query strings for monitoring in the Synapse workspace. |
| List SQL Scripts | `listSqlScripts` | Lists all SQL Scripts in the Azure Synapse Analytics workspace. |
| List Triggers | `listTriggers` | Lists all triggers in the Synapse workspace. |
| Pause Link Connection | `pauseLinkConnection` | Pause a link connection. It may take a few minutes from Pausing to Paused — monitor status with Get Link Connection Detailed Status. |
| Query Activity Runs | `queryActivityRuns` | Queries activity runs for a specific pipeline run based on input filter conditions. |
| Query Data Flow Debug Sessions | `queryDataFlowDebugSessions` | Queries all active data flow debug sessions in the workspace. |
| Query Link Connection Table Status | `queryLinkConnectionTableStatus` | Query the status of link tables in a link connection. Supports pagination via continuation token and limits max segment count. |
| Query Pipeline Runs | `queryPipelineRuns` | Queries pipeline runs in the workspace based on input filter conditions. Supports filtering by time range, pipeline name, run status, and more. |
| Query Trigger Runs | `queryTriggerRuns` | Queries trigger runs in the Synapse workspace with filter parameters including date range, filters, and ordering. |
| Rename Dataflow | `renameDataflow` | Renames a data flow in the workspace. |
| Rename Dataset | `renameDataset` | Renames a dataset in the Azure Synapse workspace. This is a long-running operation. |
| Rename KQL Script | `renameKqlScript` | Rename a KQL script. This is a long-running operation. |
| Rename Linked Service | `renameLinkedService` | Renames a linked service in the Azure Synapse Analytics workspace. This is a long-running operation. |
| Rename Notebook | `renameNotebook` | Renames a notebook in the Azure Synapse workspace. This is a long-running operation — poll getNotebookOperationResult to confirm completion. |
| Rename Pipeline | `renamePipeline` | Renames a pipeline in the Azure Synapse workspace. |
| Rename Spark Configuration | `renameSparkConfiguration` | Renames a Spark configuration. This is a long-running operation. |
| Rename Spark Job Definition | `renameSparkJobDefinition` | Renames a Spark Job Definition. This is a long-running operation. |
| Rename SQL Script | `renameSqlScript` | Renames a SQL Script in the Azure Synapse Analytics workspace. |
| Rerun Trigger Instance | `rerunTriggerInstance` | Reruns a single trigger instance identified by triggerName and runId. |
| Reset Spark Session Timeout | `resetSparkSessionTimeout` | Sends a keep-alive call to a Spark session to reset its timeout. Prevents idle sessions from being terminated. |
| Resume Link Connection | `resumeLinkConnection` | Resume a paused link connection. It may take a few minutes from Resuming to Running — monitor status with Get Link Connection Detailed Status. |
| Start Link Connection | `startLinkConnection` | Start a link connection. It may take a few minutes from Starting to Running — monitor status with Get Link Connection Detailed Status. |
| Start Trigger | `startTrigger` | Starts a trigger in the Synapse workspace, setting its runtime state to Started. |
| Stop Link Connection | `stopLinkConnection` | Stop a link connection. It may take a few minutes from Stopping to Stopped — monitor status with Get Link Connection Detailed Status. |
| Stop Trigger | `stopTrigger` | Stops a trigger in the Synapse workspace, setting its runtime state to Stopped. |
| Subscribe Trigger To Events | `subscribeTriggerToEvents` | Subscribes an event trigger to events (e.g. BlobEventsTrigger or CustomEventsTrigger). Returns the subscription operation status. |
| Unsubscribe Trigger From Events | `unsubscribeTriggerFromEvents` | Unsubscribes an event trigger from events. |
| Update Link Connection Landing Zone Credential | `updateLinkConnectionLandingZoneCredential` | Update the landing zone SAS token credential for a link connection. Use this to refresh expiring landing zone credentials. |
