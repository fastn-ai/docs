---
description: "Google BigQuery is a cloud data warehouse. Run queries and manage datasets, tables, jobs, routines and models."
hidden: true
---

# Google BigQuery

<img src="../../.gitbook/assets/connectors/lg/bigquery.png" alt="Google BigQuery logo">

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [cloud.google.com](https://cloud.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `bigquery` |

## Setup

Your customers sign in to Google BigQuery through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google BigQuery from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bigquery.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Job</td><td><code>cancelJob</code></td><td>Requests that a job be cancelled.</td></tr><tr><td>Delete Dataset</td><td><code>deleteDataset</code></td><td>Deletes the dataset specified by the datasetId value. Set deleteContents to true to delete a dataset and its non-empty contents.</td></tr><tr><td>Delete Model</td><td><code>deleteModel</code></td><td>Deletes the model specified by modelId from the dataset.</td></tr><tr><td>Delete Routine</td><td><code>deleteRoutine</code></td><td>Deletes the routine specified by routineId from the dataset.</td></tr><tr><td>Delete Table</td><td><code>deleteTable</code></td><td>Deletes the table specified by tableId from the dataset.</td></tr><tr><td>Get Dataset</td><td><code>getDataset</code></td><td>Returns the dataset specified by datasetID.</td></tr><tr><td>Get Job</td><td><code>getJob</code></td><td>Returns information about a specific job.</td></tr><tr><td>Get Model</td><td><code>getModel</code></td><td>Gets the specified model resource by model ID.</td></tr><tr><td>Get Query Results</td><td><code>getQueryResults</code></td><td>Retrieves the results of a query job. Useful to poll a previously started query/job.</td></tr><tr><td>Get Routine</td><td><code>getRoutine</code></td><td>Gets the specified routine resource by routine ID.</td></tr></tbody></table>

<details>

<summary>View 20 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Table</td><td><code>getTable</code></td><td>Gets the specified table resource by table ID, with full schema.</td></tr><tr><td>Insert All Table Data</td><td><code>insertAllTableData</code></td><td>Streams data into BigQuery one record at a time without running a load job.</td></tr><tr><td>Insert Dataset</td><td><code>insertDataset</code></td><td>Creates a new empty dataset.</td></tr><tr><td>Insert Job</td><td><code>insertJob</code></td><td>Starts a new asynchronous job (query, load, extract, or copy). Provide the configuration object describing the job.</td></tr><tr><td>Insert Routine</td><td><code>insertRoutine</code></td><td>Creates a new routine in the dataset.</td></tr><tr><td>Insert Table</td><td><code>insertTable</code></td><td>Creates a new, empty table in the dataset.</td></tr><tr><td>List Datasets</td><td><code>listDatasets</code></td><td>Lists all datasets in the specified project to which the user has been granted access.</td></tr><tr><td>List Jobs</td><td><code>listJobs</code></td><td>Lists all jobs that you started in the specified project.</td></tr><tr><td>List Models</td><td><code>listModels</code></td><td>Lists all models in the specified dataset.</td></tr><tr><td>List Projects</td><td><code>listProjects</code></td><td>Lists all projects to which the authenticated user has been granted any project role.</td></tr><tr><td>List Routines</td><td><code>listRoutines</code></td><td>Lists all routines in the specified dataset.</td></tr><tr><td>List Table Data</td><td><code>listTableData</code></td><td>Lists the content of a table in rows.</td></tr><tr><td>List Tables</td><td><code>listTables</code></td><td>Lists all tables in the specified dataset.</td></tr><tr><td>Patch Dataset</td><td><code>patchDataset</code></td><td>Updates information in an existing dataset using patch semantics (only supplied fields change).</td></tr><tr><td>Patch Model</td><td><code>patchModel</code></td><td>Patches specific fields in an existing model.</td></tr><tr><td>Patch Table</td><td><code>patchTable</code></td><td>Updates information in an existing table using patch semantics.</td></tr><tr><td>Query</td><td><code>query</code></td><td>Runs a BigQuery SQL query synchronously and returns results if it completes within the timeout. The request body is built from the inputs (query, useLegacySql, dryRun, timeoutMs, maxResults, location, defaultDataset), so dryRun=true validates the query and returns totalBytesProcessed without running it. Google scope: bigquery (or cloud-platform).</td></tr><tr><td>Update Dataset</td><td><code>updateDataset</code></td><td>Updates information in an existing dataset (full replacement of supplied resource).</td></tr><tr><td>Update Routine</td><td><code>updateRoutine</code></td><td>Updates information in an existing routine (full replacement).</td></tr><tr><td>Update Table</td><td><code>updateTable</code></td><td>Updates information in an existing table (full replacement of supplied resource).</td></tr></tbody></table>

</details>

## Events

Google BigQuery has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
