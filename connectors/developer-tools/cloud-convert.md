---
description: "CloudConvert is a file conversion and processing API."
hidden: true
---

# CloudConvert

<img src="../../.gitbook/assets/connectors/lg/cloud-convert.png" alt="CloudConvert logo">

CloudConvert is a file conversion and processing API. This connector covers the CloudConvert v2 API: jobs, tasks, the import, convert, optimize, merge, archive, thumbnail, watermark, capture-website, metadata and export task types, webhook registration, signed URLs, and the account and format metadata endpoints.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [cloudconvert.com](https://cloudconvert.com) |
| **Authentication** | Bearer token |
| **Slug** | `cloudConvert` |

## Use it

Add CloudConvert from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.cloudConvert.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Task | `cancelTask` | Cancel a task in status waiting or processing (POST /v2/tasks/{id}/cancel). Docs: https://cloudconvert.com/docs/raw/api-reference/tasks.md#cancel-task |
| Create Job | `createJob` | Create a job of one or more tasks (POST /v2/jobs). Asynchronous: returns at once with status processing. Each task uses credits. Docs: https://cloudconvert.com/docs/raw/api-reference/jobs.md#create-job |
| Create Job and Wait | `createJobAndWait` | Create a job and block until it completes (POST https://sync.api.cloudconvert.com/v2/jobs). Not for long-running jobs. Docs: https://cloudconvert.com/docs/raw/api-reference/jobs.md#create-job-and-wait |
| Create Webhook | `createWebhook` | Create an account webhook (POST /v2/webhooks). Docs: https://cloudconvert.com/docs/raw/api-reference/webhooks.md#create-webhook |
| Delete Job | `deleteJob` | Delete a job and cancel any of its tasks that have not finished. Files belonging to the job become unavailable. This cannot be undone. |
| Delete Task | `deleteTask` | Delete a task, cancelling it if it has not finished and removing any files it produced. This cannot be undone. |
| Delete Webhook | `deleteWebhook` | Delete a webhook (DELETE /v2/webhooks/{id}). Returns 204. Docs: https://cloudconvert.com/docs/raw/api-reference/webhooks.md#delete-webhook |
| Get Current User | `getCurrentUser` | Retrieve the CloudConvert account the API key belongs to, including its remaining conversion credits, whether it is on a paid plan, and whether its email address has been verified. |
| Get Job | `getJob` | Retrieve a single job by its identifier, including its status and, when requested, the tasks it contains. |
| Get Task | `getTask` | Retrieve a single task by its identifier, including its status, the engine that ran it and, once finished, its result files and their download URLs. |

<details>

<summary>See 7 more actions</summary>

* **List Jobs** `listJobs`: List the conversion jobs on the account. Filter by status or tag, include the tasks of each job, and page through the results.
* **List Supported Operations** `listOperations`: List every operation CloudConvert supports, as input format plus output format plus engine, with the credit cost of each. Use it to discover which conversions are possible before creating a task.
* **List Tasks** `listTasks`: List the tasks on the account. Filter by job, status, operation or tag, include the job each task belongs to, and page through the results.
* **List Webhooks** `listWebhooks`: List the account's webhooks (GET /v2/users/me/webhooks). Docs: https://cloudconvert.com/docs/raw/api-reference/webhooks.md#list-webhooks
* **Retry Task** `retryTask`: Create a new task from the payload of another task (POST /v2/tasks/{id}/retry). Docs: https://cloudconvert.com/docs/raw/api-reference/tasks.md#retry-task
* **Wait for Job** `waitForJob`: Wait until a job completes and return it (GET https://sync.api.cloudconvert.com/v2/jobs/{id}). Docs: https://cloudconvert.com/docs/raw/api-reference/jobs.md#wait-for-job
* **Wait for Task** `waitForTask`: Wait until a task completes and return it (GET https://sync.api.cloudconvert.com/v2/tasks/{id}). Docs: https://cloudconvert.com/docs/raw/api-reference/tasks.md#wait-for-task

</details>
