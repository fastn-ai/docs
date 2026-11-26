---
description: "Google Cloud Scheduler runs scheduled jobs on Google Cloud. Create, list, update, pause, resume, run and delete scheduled jobs."
hidden: true
---

# Google Cloud Scheduler

<img src="../../.gitbook/assets/connectors/lg/google-cloud-scheduler.png" alt="Google Cloud Scheduler logo">

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [cloudscheduler.googleapis.com](https://cloudscheduler.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleCloudScheduler` |

## Setup

Your customers sign in to Google Cloud Scheduler through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Cloud Scheduler from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudScheduler.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Cancel Operation</td><td><code>cancelOperation</code></td><td>Requests cancellation of a Cloud Scheduler long-running operation. Cancellation is best-effort; poll the operation afterwards to confirm the outcome.</td></tr><tr><td>Create Job</td><td><code>createJob</code></td><td>Creates a Cloud Scheduler job in the given project and location. Supply a schedule plus exactly one target: httpTarget for an arbitrary HTTP endpoint, appEngineHttpTarget for an App Engine service, or pubsubTarget to publish a Pub/Sub message.</td></tr><tr><td>Delete Job</td><td><code>deleteJob</code></td><td>Permanently deletes a Cloud Scheduler job. The job stops running immediately and cannot be recovered.</td></tr><tr><td>Delete Operation</td><td><code>deleteOperation</code></td><td>Deletes a Cloud Scheduler long-running operation record. This removes the client's interest in the operation but does not cancel the underlying work.</td></tr><tr><td>Get CMEK Config</td><td><code>getCmekConfig</code></td><td>Retrieves the customer-managed encryption key (CMEK) configuration for Cloud Scheduler in a given project and location, showing which Cloud KMS key protects job data.</td></tr><tr><td>Get Job</td><td><code>getJob</code></td><td>Retrieves a single Cloud Scheduler job by project, location and job id, including its schedule, target, retry settings, current state and last attempt status.</td></tr><tr><td>Get Location</td><td><code>getLocation</code></td><td>Retrieves metadata about a single Cloud Scheduler location in a project, including its display name and service-specific metadata.</td></tr><tr><td>Get Operation</td><td><code>getOperation</code></td><td>Retrieves the current state of a single Cloud Scheduler long-running operation, including whether it has completed and its result or error.</td></tr><tr><td>List Jobs</td><td><code>listJobs</code></td><td>Lists the Cloud Scheduler jobs in a project and location, including each job's schedule, target configuration, state and last attempt status.</td></tr><tr><td>List Locations</td><td><code>listLocations</code></td><td>Lists the Google Cloud regions in which Cloud Scheduler is available for the given project. Use the returned locationId values when addressing jobs, operations and CMEK configuration.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Operations</td><td><code>listOperations</code></td><td>Lists the long-running operations in a Cloud Scheduler project and location, such as pending CMEK configuration updates.</td></tr><tr><td>Pause Job</td><td><code>pauseJob</code></td><td>Pauses a Cloud Scheduler job so that it stops executing on its schedule. The job must be in the ENABLED state; after pausing its state becomes PAUSED.</td></tr><tr><td>Resume Job</td><td><code>resumeJob</code></td><td>Resumes a paused Cloud Scheduler job so that it executes on its schedule again. The job must be in the PAUSED state; after resuming its state becomes ENABLED.</td></tr><tr><td>Run Job</td><td><code>runJob</code></td><td>Forces a Cloud Scheduler job to run immediately, outside its normal schedule. The job's regular schedule is unaffected and the updated job resource is returned.</td></tr><tr><td>Update CMEK Config</td><td><code>updateCmekConfig</code></td><td>Updates the customer-managed encryption key (CMEK) configuration for Cloud Scheduler in a project and location. Returns a long-running operation. Supply an empty kmsKeyName to disable CMEK for the location.</td></tr><tr><td>Update Job</td><td><code>updateJob</code></td><td>Updates a Cloud Scheduler job. Only the fields named in updateMask are changed, so list exactly the fields you are modifying, for example 'schedule,description'. If the job is paused it remains paused after the update.</td></tr></tbody></table>

</details>

## Events

Google Cloud Scheduler has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
