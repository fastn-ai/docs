---
description: "Google Cloud Scheduler is a fully managed enterprise-grade cron job scheduler."
hidden: true
---

# Google Cloud Scheduler

<img src="../../.gitbook/assets/connectors/google-cloud-scheduler.png" alt="Google Cloud Scheduler logo" width="64">

Google Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. Create, list, update, pause, resume, run and delete scheduled jobs that target HTTP endpoints, App Engine services and Pub/Sub topics, and manage locations, CMEK configuration and long-running operations.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloudscheduler.googleapis.com](https://cloudscheduler.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudScheduler` |

## Use it

Add Google Cloud Scheduler from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudScheduler.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Operation | `cancelOperation` | Requests cancellation of a Cloud Scheduler long-running operation. Cancellation is best-effort; poll the operation afterwards to confirm the outcome. |
| Create Job | `createJob` | Creates a Cloud Scheduler job in the given project and location. Supply a schedule plus exactly one target: httpTarget for an arbitrary HTTP endpoint, appEngineHttpTarget for an App Engine service, or pubsubTarget to publish a Pub/Sub message. |
| Delete Job | `deleteJob` | Permanently deletes a Cloud Scheduler job. The job stops running immediately and cannot be recovered. |
| Delete Operation | `deleteOperation` | Deletes a Cloud Scheduler long-running operation record. This removes the client's interest in the operation but does not cancel the underlying work. |
| Get CMEK Config | `getCmekConfig` | Retrieves the customer-managed encryption key (CMEK) configuration for Cloud Scheduler in a given project and location, showing which Cloud KMS key protects job data. |
| Get Job | `getJob` | Retrieves a single Cloud Scheduler job by project, location and job id, including its schedule, target, retry settings, current state and last attempt status. |
| Get Location | `getLocation` | Retrieves metadata about a single Cloud Scheduler location in a project, including its display name and service-specific metadata. |
| Get Operation | `getOperation` | Retrieves the current state of a single Cloud Scheduler long-running operation, including whether it has completed and its result or error. |
| List Jobs | `listJobs` | Lists the Cloud Scheduler jobs in a project and location, including each job's schedule, target configuration, state and last attempt status. |
| List Locations | `listLocations` | Lists the Google Cloud regions in which Cloud Scheduler is available for the given project. Use the returned locationId values when addressing jobs, operations and CMEK configuration. |

<details>

<summary>See 6 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| List Operations | `listOperations` | Lists the long-running operations in a Cloud Scheduler project and location, such as pending CMEK configuration updates. |
| Pause Job | `pauseJob` | Pauses a Cloud Scheduler job so that it stops executing on its schedule. The job must be in the ENABLED state; after pausing its state becomes PAUSED. |
| Resume Job | `resumeJob` | Resumes a paused Cloud Scheduler job so that it executes on its schedule again. The job must be in the PAUSED state; after resuming its state becomes ENABLED. |
| Run Job | `runJob` | Forces a Cloud Scheduler job to run immediately, outside its normal schedule. The job's regular schedule is unaffected and the updated job resource is returned. |
| Update CMEK Config | `updateCmekConfig` | Updates the customer-managed encryption key (CMEK) configuration for Cloud Scheduler in a project and location. Returns a long-running operation. Supply an empty kmsKeyName to disable CMEK for the location. |
| Update Job | `updateJob` | Updates a Cloud Scheduler job. Only the fields named in updateMask are changed, so list exactly the fields you are modifying, for example 'schedule,description'. If the job is paused it remains paused after the update. |

</details>
