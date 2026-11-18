---
description: "Microsoft Power BI REST API connector."
hidden: true
---

# Microsoft Power BI

<img src="../../.gitbook/assets/connectors/lg/powerbi.png" alt="Microsoft Power BI logo">

Microsoft Power BI REST API connector. Manage workspaces (groups), datasets, reports, dashboards, tiles, dataflows, imports, gateways, apps, capacities, and admin resources. Auth via Azure AD OAuth 2.0.

| | |
| --- | --- |
| **Category** | [Analytics and monitoring](README.md) |
| **Website** | [powerbi.com](https://powerbi.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `powerbi` |

## Use it

Add Microsoft Power BI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.powerbi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Group User | `addGroupUser` | Grants the specified user the specified permissions to the workspace (group). |
| Admin: Get Activity Events | `adminGetActivityEvents` | Admin: Returns a list of audit activity events for the organization, scoped by start and end date-time (same day) or by continuationToken. |
| Admin: Get Datasets In Group | `adminGetDatasetsInGroup` | Admin: Returns a list of datasets from the specified workspace. |
| Admin: Get Group | `adminGetGroup` | Admin: Returns a workspace for the organization. |
| Admin: Get Group Users | `adminGetGroupUsers` | Admin: Returns a list of users that have access to the specified workspace. |
| Admin: List Capacities | `adminListCapacities` | Admin: Returns a list of capacities for the organization. |
| Admin: List Dashboards | `adminListDashboards` | Admin: Returns a list of dashboards for the organization. |
| Admin: List Dataflows | `adminListDataflows` | Admin: Returns a list of dataflows for the organization. |
| Admin: List Datasets | `adminListDatasets` | Admin: Returns a list of datasets for the organization. |
| Admin: List Groups | `adminListGroups` | Admin: Returns a list of workspaces for the organization. |
| Admin: List Imports | `adminListImports` | Admin: Returns a list of imports for the organization. |
| Admin: List Reports | `adminListReports` | Admin: Returns a list of reports for the organization. |
| Bind Dataset To Gateway In Group | `bindToGatewayInGroup` | Binds the specified dataset from the specified workspace to the specified gateway, optionally with a given set of datasource IDs. |
| Clone Report In Group | `cloneReportInGroup` | Clones the specified report from the specified workspace. |
| Clone Tile In Group | `cloneTileInGroup` | Clones the specified tile from the specified dashboard to a target dashboard. |
| Create Dashboard In Group | `createDashboardInGroup` | Creates a new empty dashboard in the specified workspace. |
| Create Dataset (My Workspace) | `createDataset` | Creates a new push dataset in the signed-in user's My Workspace, defining its tables and columns. Use defaultMode Push to enable the real-time rows API. |
| Create Dataset In Group | `createDatasetInGroup` | Creates a new push dataset in the specified Power BI workspace, defining its tables and columns. Use defaultMode Push to enable the real-time rows API. |
| Create Gateway Datasource | `createGatewayDatasource` | Creates a new datasource on the specified gateway. |
| Create Group (Workspace) | `createGroup` | Creates a new workspace (group). |
| Create Import In Group | `createImportInGroup` | Creates new content in the specified workspace from a .pbix file, OneDrive, or an imported file path. Sends the displayName as a query parameter; the file content/connection details are supplied in the request body. |
| Delete Dataflow | `deleteDataflow` | Deletes the specified dataflow from the specified workspace. |
| Delete Dataset (My Workspace) | `deleteDataset` | Deletes the specified dataset from My workspace. |
| Delete Dataset In Group | `deleteDatasetInGroup` | Deletes the specified dataset from the specified workspace. |
| Delete Gateway Datasource | `deleteGatewayDatasource` | Deletes the specified datasource from the specified gateway. |
| Delete Group (Workspace) | `deleteGroup` | Deletes the specified workspace (group). |
| Delete Group User | `deleteGroupUser` | Removes the specified user permissions from the workspace (group). |
| Delete Report (My Workspace) | `deleteReport` | Deletes the specified report from My workspace. |
| Delete Report In Group | `deleteReportInGroup` | Deletes the specified report from the specified workspace. |
| Delete Rows (My Workspace) | `deleteRows` | Deletes all rows from the specified table within the specified push dataset in My workspace. |
| Delete Rows In Group | `deleteRowsInGroup` | Deletes all rows from the specified table within the specified push dataset in the specified workspace. |
| Discover Gateways In Group | `discoverGatewaysInGroup` | Returns the list of on-premises data gateways that the specified semantic model in the given workspace can be bound to. |
| Execute DAX Queries (My Workspace) | `executeQueries` | Executes a Data Analysis Expressions (DAX) query against a semantic model in My Workspace and returns the result rows. Only one query is supported per request. |
| Execute DAX Queries In Group | `executeQueriesInGroup` | Executes Data Analysis Expressions (DAX) queries against a semantic model in the specified workspace and returns the result rows. Only one query is supported per request and the result is capped at 100,000 rows or 1,000,000 values. |
| Export Report In Group | `exportReportInGroup` | Exports the specified report from the specified workspace to a .pbix file. |
| Export Report To File In Group | `exportReportToFileInGroup` | Initiates an asynchronous export job (e.g. PDF, PNG, PPTX) for the specified report in the specified workspace. |
| Get App | `getApp` | Returns the specified installed app. |
| Get Available Features | `getAvailableFeatures` | Returns a list of available features for the user. |
| Get Capacity Workloads | `getCapacityWorkloads` | Returns the current state of the specified capacity workloads. |
| Get Dashboard In Group | `getDashboardInGroup` | Returns the specified dashboard from the specified workspace. |
| Get Dataflow | `getDataflow` | Exports the specified dataflow definition (model.json) from the specified workspace. |
| Get Dataflow Datasources | `getDataflowDatasources` | Returns a list of datasources for the specified dataflow. |
| Get Dataset (My Workspace) | `getDataset` | Returns the specified dataset from My workspace. |
| Get Dataset Datasources In Group | `getDatasourcesInGroup` | Returns a list of datasources for the specified dataset in the specified workspace. |
| Get Dataset In Group | `getDatasetInGroup` | Returns the specified dataset from the specified workspace. |
| Get Dataset Parameters In Group | `getParametersInGroup` | Returns a list of parameters for the specified dataset in the specified workspace. |
| Get Dataset Tables (My Workspace) | `getDatasetTables` | Returns a list of tables within the specified push dataset in My workspace. |
| Get Dataset Tables In Group | `getDatasetTablesInGroup` | Returns a list of tables within the specified push dataset in the specified workspace. |
| Get Dataset Users In Group | `getDatasetUsersInGroup` | Returns the list of principals that have access to the specified semantic model in the given workspace, with the access right granted to each. |
| Get Export To File Status In Group | `getExportToFileStatusInGroup` | Returns the status of an export-to-file job for the specified report in the specified workspace. |
| Get Gateway | `getGateway` | Returns the specified gateway. |
| Get Gateway Datasource | `getGatewayDatasource` | Returns the specified datasource from the specified gateway. |
| Get Import (My Workspace) | `getImport` | Returns the specified import from My workspace. |
| Get Import In Group | `getImportInGroup` | Returns the specified import from the specified workspace. |
| Get Refresh History (My Workspace) | `getRefreshHistory` | Returns the refresh history for the specified dataset in My workspace. |
| Get Refresh History In Group | `getRefreshHistoryInGroup` | Returns the refresh history for the specified dataset in the specified workspace. |
| Get Refresh Schedule In Group | `getRefreshScheduleInGroup` | Returns the scheduled refresh configuration for the specified semantic model in the given workspace, including the days, times, time zone and notification setting. |
| Get Report (My Workspace) | `getReport` | Returns the specified report from My workspace. |
| Get Report Datasources In Group | `getReportDatasourcesInGroup` | Returns a list of datasources for the specified RDL report from the specified workspace. |
| Get Report In Group | `getReportInGroup` | Returns the specified report from the specified workspace. |
| Get Report Pages In Group | `getReportPagesInGroup` | Returns a list of pages within the specified report from the specified workspace. |
| Get Tile In Group | `getTileInGroup` | Returns the specified tile within the specified dashboard from the specified workspace. |
| List App Dashboards | `listAppDashboards` | Returns a list of dashboards from the specified app. |
| List App Reports | `listAppReports` | Returns a list of reports from the specified app. |
| List Apps | `listApps` | Returns a list of installed apps for the current user. |
| List Capacities | `listCapacities` | Returns a list of capacities the user has access to. |
| List Dashboards (My Workspace) | `listDashboards` | Returns a list of dashboards from My workspace. |
| List Dashboards In Group | `listDashboardsInGroup` | Returns a list of dashboards from the specified workspace. |
| List Dataflows In Group | `listDataflowsInGroup` | Returns a list of all dataflows from the specified workspace. |
| List Datasets (My Workspace) | `listDatasets` | Returns a list of datasets from My workspace. |
| List Datasets In Group | `listDatasetsInGroup` | Returns a list of datasets from the specified workspace. |
| List Gateway Datasources | `listGatewayDatasources` | Returns a list of datasources from the specified gateway. |
| List Gateways | `listGateways` | Returns a list of gateways for which the user is an admin. |
| List Group Users | `listGroupUsers` | Returns a list of users that have access to the specified workspace (group). |
| List Groups (Workspaces) | `listGroups` | Returns a list of workspaces (groups) the user has access to. |
| List Imports (My Workspace) | `listImports` | Returns a list of imports from My workspace. |
| List Imports In Group | `listImportsInGroup` | Returns a list of imports from the specified workspace. |
| List Reports (My Workspace) | `listReports` | Returns a list of reports from My workspace. |
| List Reports In Group | `listReportsInGroup` | Returns a list of reports from the specified workspace. |
| List Tiles In Group | `listTilesInGroup` | Returns a list of tiles within the specified dashboard from the specified workspace. |
| Post Rows (My Workspace) | `postRows` | Adds new data rows to the specified table within the specified push dataset in My workspace. |
| Post Rows In Group | `postRowsInGroup` | Adds new data rows to the specified table within the specified push dataset in the specified workspace. |
| Rebind Report In Group | `rebindReportInGroup` | Rebinds the specified report from the specified workspace to the requested dataset. |
| Refresh Dataflow | `refreshDataflow` | Triggers a refresh for the specified dataflow in the specified workspace. |
| Refresh Dataset (My Workspace) | `refreshDataset` | Triggers a refresh for the specified dataset in My workspace. |
| Refresh Dataset In Group | `refreshDatasetInGroup` | Triggers a refresh for the specified dataset in the specified workspace. |
| Take Over Dataset In Group | `takeOverDatasetInGroup` | Transfers ownership over the specified dataset to the current authorized user. |
| Update Dataset Datasources In Group | `updateDatasourcesInGroup` | Updates the datasources of the specified dataset in the specified workspace. |
| Update Dataset In Group | `updateDatasetInGroup` | Updates the properties of the specified semantic model in the given workspace, such as its target storage mode or query scale-out settings. |
| Update Dataset Parameters In Group | `updateParametersInGroup` | Updates the parameters values for the specified dataset in the specified workspace. |
| Update Dataset Table Schema In Group | `putTableInGroup` | Replaces the schema of the specified table in a push semantic model in the given workspace. Existing rows in the table are removed when the schema changes. |
| Update Group (Workspace) | `updateGroup` | Updates the properties of the specified workspace (group), such as its name. |
| Update Group User | `updateGroupUser` | Updates the specified user permissions to the workspace (group). |
| Update Refresh Schedule In Group | `updateRefreshScheduleInGroup` | Updates the scheduled refresh configuration of the specified semantic model in the given workspace. Only the supplied properties are changed; at least one property must be provided. |
| Update Report Content In Group | `updateReportContentInGroup` | Updates the content of the specified report from the specified workspace with the content of a specified source report. |
