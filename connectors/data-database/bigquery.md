---
description: "Google BigQuery REST API v2 connector."
hidden: true
---

# Google BigQuery

Google BigQuery REST API v2 connector. Manage datasets, tables, jobs, queries, table data, routines, and models in Google Cloud BigQuery.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [cloud.google.com](https://cloud.google.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 30 |
| **Events** | 0 |
| **Slug** | `bigquery` |

## Use it

Add Google BigQuery from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bigquery.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Job | `cancelJob` | Requests that a job be cancelled. POST /projects/{projectId}/jobs/{jobId}/cancel. |
| Delete Dataset | `deleteDataset` | Deletes the dataset specified by the datasetId value. DELETE /projects/{projectId}/datasets/{datasetId}. Set deleteContents to true to delete a dataset and its non-empty contents. |
| Delete Model | `deleteModel` | Deletes the model specified by modelId from the dataset. DELETE /projects/{projectId}/datasets/{datasetId}/models/{modelId}. |
| Delete Routine | `deleteRoutine` | Deletes the routine specified by routineId from the dataset. DELETE /projects/{projectId}/datasets/{datasetId}/routines/{routineId}. |
| Delete Table | `deleteTable` | Deletes the table specified by tableId from the dataset. DELETE /projects/{projectId}/datasets/{datasetId}/tables/{tableId}. |
| Get Dataset | `getDataset` | Returns the dataset specified by datasetID. GET /projects/{projectId}/datasets/{datasetId}. |
| Get Job | `getJob` | Returns information about a specific job. GET /projects/{projectId}/jobs/{jobId}. |
| Get Model | `getModel` | Gets the specified model resource by model ID. GET /projects/{projectId}/datasets/{datasetId}/models/{modelId}. |
| Get Query Results | `getQueryResults` | Retrieves the results of a query job. GET /projects/{projectId}/queries/{jobId}. Useful to poll a previously started query/job. |
| Get Routine | `getRoutine` | Gets the specified routine resource by routine ID. GET /projects/{projectId}/datasets/{datasetId}/routines/{routineId}. |
| Get Table | `getTable` | Gets the specified table resource by table ID, with full schema. GET /projects/{projectId}/datasets/{datasetId}/tables/{tableId}. |
| Insert All Table Data | `insertAllTableData` | Streams data into BigQuery one record at a time without running a load job. POST /projects/{projectId}/datasets/{datasetId}/tables/{tableId}/insertAll. |
| Insert Dataset | `insertDataset` | Creates a new empty dataset. POST /projects/{projectId}/datasets. |
| Insert Job | `insertJob` | Starts a new asynchronous job (query, load, extract, or copy). POST /projects/{projectId}/jobs. Provide the configuration object describing the job. |
| Insert Routine | `insertRoutine` | Creates a new routine in the dataset. POST /projects/{projectId}/datasets/{datasetId}/routines. |
| Insert Table | `insertTable` | Creates a new, empty table in the dataset. POST /projects/{projectId}/datasets/{datasetId}/tables. |
| List Datasets | `listDatasets` | Lists all datasets in the specified project to which the user has been granted access. GET /projects/{projectId}/datasets. |
| List Jobs | `listJobs` | Lists all jobs that you started in the specified project. GET /projects/{projectId}/jobs. |
| List Models | `listModels` | Lists all models in the specified dataset. GET /projects/{projectId}/datasets/{datasetId}/models. |
| List Projects | `listProjects` | Lists all projects to which the authenticated user has been granted any project role. GET /projects. |
| List Routines | `listRoutines` | Lists all routines in the specified dataset. GET /projects/{projectId}/datasets/{datasetId}/routines. |
| List Table Data | `listTableData` | Lists the content of a table in rows. GET /projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data. |
| List Tables | `listTables` | Lists all tables in the specified dataset. GET /projects/{projectId}/datasets/{datasetId}/tables. |
| Patch Dataset | `patchDataset` | Updates information in an existing dataset using patch semantics (only supplied fields change). PATCH /projects/{projectId}/datasets/{datasetId}. |
| Patch Model | `patchModel` | Patches specific fields in an existing model. PATCH /projects/{projectId}/datasets/{datasetId}/models/{modelId}. |
| Patch Table | `patchTable` | Updates information in an existing table using patch semantics. PATCH /projects/{projectId}/datasets/{datasetId}/tables/{tableId}. |
| Query | `query` | Runs a BigQuery SQL query synchronously and returns results if it completes within the timeout. POST /projects/{projectId}/queries. The request body is built from the inputs (query, useLegacySql, dryRun, timeoutMs, maxResults, location, defaultDataset), so dryRun=true validates the query and returns totalBytesProcessed without running it. Google scope: bigquery (or cloud-platform). |
| Update Dataset | `updateDataset` | Updates information in an existing dataset (full replacement of supplied resource). PUT /projects/{projectId}/datasets/{datasetId}. |
| Update Routine | `updateRoutine` | Updates information in an existing routine (full replacement). PUT /projects/{projectId}/datasets/{datasetId}/routines/{routineId}. |
| Update Table | `updateTable` | Updates information in an existing table (full replacement of supplied resource). PUT /projects/{projectId}/datasets/{datasetId}/tables/{tableId}. |
