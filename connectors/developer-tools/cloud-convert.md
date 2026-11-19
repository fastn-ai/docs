---
description: "CloudConvert is a file conversion and processing API."
hidden: true
---

# CloudConvert

<img src="../../.gitbook/assets/connectors/lg/cloud-convert.png" alt="CloudConvert logo">

This connector covers the CloudConvert v2 API: jobs, tasks, the import, convert, optimize, merge, archive, thumbnail, watermark, capture-website, metadata and export task types, webhook registration, signed URLs, and the account and format metadata endpoints.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [cloudconvert.com](https://cloudconvert.com) |
| **Authentication** | Bearer token |
| **Slug** | `cloudConvert` |

## Use it

Add CloudConvert from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cloudConvert.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Task</td><td><code>cancelTask</code></td><td>Cancel a task in status waiting or processing (POST /v2/tasks/{id}/cancel). Docs: https://cloudconvert.com/docs/raw/api-reference/tasks.md#cancel-task</td></tr><tr><td>Create Job</td><td><code>createJob</code></td><td>Create a job of one or more tasks (POST /v2/jobs). Asynchronous: returns at once with status processing. Each task uses credits. Docs: https://cloudconvert.com/docs/raw/api-reference/jobs.md#create-job</td></tr><tr><td>Create Job and Wait</td><td><code>createJobAndWait</code></td><td>Create a job and block until it completes (POST https://sync.api.cloudconvert.com/v2/jobs). Not for long-running jobs. Docs: https://cloudconvert.com/docs/raw/api-reference/jobs.md#create-job-and-wait</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Create an account webhook (POST /v2/webhooks). Docs: https://cloudconvert.com/docs/raw/api-reference/webhooks.md#create-webhook</td></tr><tr><td>Delete Job</td><td><code>deleteJob</code></td><td>Delete a job and cancel any of its tasks that have not finished. Files belonging to the job become unavailable. This cannot be undone.</td></tr><tr><td>Delete Task</td><td><code>deleteTask</code></td><td>Delete a task, cancelling it if it has not finished and removing any files it produced. This cannot be undone.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Delete a webhook (DELETE /v2/webhooks/{id}). Returns 204. Docs: https://cloudconvert.com/docs/raw/api-reference/webhooks.md#delete-webhook</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Retrieve the CloudConvert account the API key belongs to, including its remaining conversion credits, whether it is on a paid plan, and whether its email address has been verified.</td></tr><tr><td>Get Job</td><td><code>getJob</code></td><td>Retrieve a single job by its identifier, including its status and, when requested, the tasks it contains.</td></tr><tr><td>Get Task</td><td><code>getTask</code></td><td>Retrieve a single task by its identifier, including its status, the engine that ran it and, once finished, its result files and their download URLs.</td></tr></tbody></table>

<details>

<summary>View 7 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Jobs</td><td><code>listJobs</code></td><td>List the conversion jobs on the account. Filter by status or tag, include the tasks of each job, and page through the results.</td></tr><tr><td>List Supported Operations</td><td><code>listOperations</code></td><td>List every operation CloudConvert supports, as input format plus output format plus engine, with the credit cost of each. Use it to discover which conversions are possible before creating a task.</td></tr><tr><td>List Tasks</td><td><code>listTasks</code></td><td>List the tasks on the account. Filter by job, status, operation or tag, include the job each task belongs to, and page through the results.</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>List the account's webhooks (GET /v2/users/me/webhooks). Docs: https://cloudconvert.com/docs/raw/api-reference/webhooks.md#list-webhooks</td></tr><tr><td>Retry Task</td><td><code>retryTask</code></td><td>Create a new task from the payload of another task (POST /v2/tasks/{id}/retry). Docs: https://cloudconvert.com/docs/raw/api-reference/tasks.md#retry-task</td></tr><tr><td>Wait for Job</td><td><code>waitForJob</code></td><td>Wait until a job completes and return it (GET https://sync.api.cloudconvert.com/v2/jobs/{id}). Docs: https://cloudconvert.com/docs/raw/api-reference/jobs.md#wait-for-job</td></tr><tr><td>Wait for Task</td><td><code>waitForTask</code></td><td>Wait until a task completes and return it (GET https://sync.api.cloudconvert.com/v2/tasks/{id}). Docs: https://cloudconvert.com/docs/raw/api-reference/tasks.md#wait-for-task</td></tr></tbody></table>

</details>
