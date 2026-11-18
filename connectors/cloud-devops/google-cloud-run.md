---
description: "Deploy and operate serverless containers with the Google Cloud Run Admin API v2: services and revisions, jobs, executions and tasks, worker pools and worker…"
---

# Google Cloud Run

Deploy and operate serverless containers with the Google Cloud Run Admin API v2: services and revisions, jobs, executions and tasks, worker pools and worker pool revisions, instances, builds, source uploads, IAM policies, metadata and image export, and long-running operations.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [run.googleapis.com](https://run.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 63 |
| **Events** | 0 |
| **Slug** | `googleCloudRun` |

## Use it

Add Google Cloud Run from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleCloudRun.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Job Execution | `cancelJobExecution` | Cancels a running execution of a Cloud Run job. Returns a long-running operation to poll for completion. |
| Create Instance | `createInstance` | Creates a Cloud Run instance, a single long-lived container in a project and region. Returns a long-running operation to poll for completion. |
| Create Job | `createJob` | Creates a new Cloud Run job in a project and region. Returns a long-running operation to poll for completion. |
| Create Service | `createService` | Creates a new Cloud Run service in a project and region from the given revision template. Returns a long-running operation to poll for completion. |
| Create Worker Pool | `createWorkerPool` | Creates a new Cloud Run worker pool in a given project and region. Returns a long-running operation to poll for completion. |
| Delete Instance | `deleteInstance` | Deletes a Cloud Run instance. Returns a long-running operation to poll for completion. |
| Delete Job | `deleteJob` | Deletes a Cloud Run job. Returns a long-running operation to poll for completion. |
| Delete Job Execution | `deleteJobExecution` | Deletes an execution of a Cloud Run job. Returns a long-running operation to poll for completion. |
| Delete Operation | `deleteOperation` | Deletes a Cloud Run long-running operation record, indicating the client is no longer interested in its result. This does not cancel the operation. |
| Delete Service | `deleteService` | Deletes a Cloud Run service. The service stops serving traffic and all of its revisions are deleted. Returns a long-running operation. |
| Delete Service Revision | `deleteServiceRevision` | Deletes a revision of a Cloud Run service. Returns a long-running operation to poll for completion. |
| Delete Worker Pool | `deleteWorkerPool` | Deletes a Cloud Run worker pool. Returns a long-running operation to poll for completion. |
| Delete Worker Pool Revision | `deleteWorkerPoolRevision` | Deletes a revision belonging to a Cloud Run worker pool. Returns a long-running operation to poll for completion. |
| Export Image for Job Execution | `exportImageJobExecution` | Exports the container image of a Cloud Run job execution to an Artifact Registry repository. Returns an operation id that tracks the export. |
| Export Image for Service Revision | `exportImageServiceRevision` | Exports the container image of a Cloud Run service revision to an Artifact Registry repository. Returns an operation id that tracks the export. |
| Export Image Metadata for Job Execution | `exportImageMetadataJobExecution` | Exports the Google-generated image metadata for a Cloud Run job execution, returned as a JSON-encoded string. |
| Export Image Metadata for Service Revision | `exportImageMetadataServiceRevision` | Exports the Google-generated image metadata for a Cloud Run service revision, returned as a JSON-encoded string. |
| Export Metadata for Job Execution | `exportMetadataJobExecution` | Exports the Google-generated customer metadata for a Cloud Run job execution, returned as a JSON-encoded string. |
| Export Metadata for Service | `exportMetadataService` | Exports the Google-generated customer metadata for a Cloud Run service, returned as a JSON-encoded string. |
| Export Metadata for Service Revision | `exportMetadataServiceRevision` | Exports the Google-generated customer metadata for a Cloud Run service revision, returned as a JSON-encoded string. |
| Export Project Metadata | `exportProjectMetadata` | Exports the Google-generated customer metadata for a project in a given Cloud Run region, returned as a JSON-encoded string. |
| Export Status for Job Execution | `exportStatusJobExecution` | Reads the status of an image export operation started by Export Image for Job Execution. Supply the operation id returned by that action. |
| Export Status for Service Revision | `exportStatusServiceRevision` | Reads the status of an image export operation started by Export Image for Service Revision. Supply the operation id returned by that action. |
| Get IAM Policy for Instance | `getIamPolicyInstance` | Gets the IAM access control policy currently in effect for a Cloud Run instance. The result does not include inherited policies. |
| Get IAM Policy for Job | `getIamPolicyJob` | Gets the IAM access control policy currently in effect for a Cloud Run job. The result does not include inherited policies. |
| Get IAM Policy for Service | `getIamPolicyService` | Gets the IAM access control policy currently in effect for a Cloud Run service. The result does not include inherited policies. |
| Get IAM Policy for Worker Pool | `getIamPolicyWorkerPool` | Gets the IAM access control policy currently in effect for a Cloud Run worker pool. The result does not include inherited policies. |
| Get Instance | `getInstance` | Gets a Cloud Run instance, including its containers and their resolved image digests, serving URLs, ingress settings and readiness conditions. |
| Get Job | `getJob` | Gets a Cloud Run job, including its execution template, execution count, latest execution reference and readiness conditions. |
| Get Job Execution | `getJobExecution` | Gets an execution of a Cloud Run job, including task counts by phase, start and completion times, log URI and readiness conditions. |
| Get Job Execution Task | `getJobExecutionTask` | Gets a single task from an execution of a Cloud Run job, including its containers, retry count, timings and last attempt result. |
| Get Operation | `getOperation` | Gets the latest state of a Cloud Run long-running operation. Poll this at the interval recommended by the API to learn when a deployment has finished. |
| Get Service | `getService` | Gets a Cloud Run service, including its serving URI, revision template, traffic splits, ingress settings and readiness conditions. |
| Get Service Revision | `getServiceRevision` | Gets a revision of a Cloud Run service, including its containers, volumes, scaling settings, VPC access and readiness conditions. |
| Get Worker Pool | `getWorkerPool` | Gets a Cloud Run worker pool, including its revision template, scaling settings, instance splits, conditions and readiness state. |
| Get Worker Pool Revision | `getWorkerPoolRevision` | Gets a revision of a Cloud Run worker pool, including its containers, volumes, scaling settings, VPC access and readiness conditions. |
| List Instances | `listInstance` | Lists the Cloud Run instances in a project and region, sorted by creation time descending. |
| List Job Execution Tasks | `listJobExecutionTask` | Lists the tasks belonging to an execution of a Cloud Run job. |
| List Job Executions | `listJobExecution` | Lists the executions of a Cloud Run job, sorted by creation time descending. |
| List Jobs | `listJob` | Lists the Cloud Run jobs in a project and region, sorted by creation time descending. |
| List Operations | `listOperation` | Lists the Cloud Run long-running operations in a project and region that match the given filter, for example 'done:true' for completed operations only. |
| List Service Revisions | `listServiceRevision` | Lists the revisions of a Cloud Run service, sorted by creation time descending. |
| List Services | `listService` | Lists the Cloud Run services in a project and region, sorted by creation time descending. |
| List Worker Pool Revisions | `listWorkerPoolRevision` | Lists the revisions of a Cloud Run worker pool, sorted by creation time descending. |
| List Worker Pools | `listWorkerPool` | Lists the Cloud Run worker pools in a project and region, sorted by creation time descending. |
| Run Job | `runJob` | Triggers a new execution of a Cloud Run job, optionally with per-run overrides for task count, timeout and container arguments. Returns a long-running operation. |
| Set IAM Policy for Instance | `setIamPolicyInstance` | Sets the IAM access control policy for a Cloud Run instance, overwriting any existing policy. |
| Set IAM Policy for Job | `setIamPolicyJob` | Sets the IAM access control policy for a Cloud Run job, overwriting any existing policy. |
| Set IAM Policy for Service | `setIamPolicyService` | Sets the IAM access control policy for a Cloud Run service, overwriting any existing policy. Use it to grant or revoke the run.invoker role. |
| Set IAM Policy for Worker Pool | `setIamPolicyWorkerPool` | Sets the IAM access control policy for a Cloud Run worker pool, overwriting any existing policy. |
| Start Instance | `startInstance` | Starts a Cloud Run instance. Returns a long-running operation to poll for completion. |
| Stop Instance | `stopInstance` | Stops a Cloud Run instance. Returns a long-running operation to poll for completion. |
| Submit Build | `submitBuild` | Submits a Cloud Build in a given project and region to build a container image from a Cloud Storage source, using either Buildpacks or a Dockerfile. Returns the Cloud Build operation to poll. |
| Test IAM Permissions for Instance | `testIamPermissionsInstance` | Returns the subset of the supplied permissions that the caller holds on a Cloud Run instance. No permissions are required to make this call. |
| Test IAM Permissions for Job | `testIamPermissionsJob` | Returns the subset of the supplied permissions that the caller holds on a Cloud Run job. No permissions are required to make this call. |
| Test IAM Permissions for Service | `testIamPermissionsService` | Returns the subset of the supplied permissions that the caller holds on a Cloud Run service. No permissions are required to make this call. |
| Test IAM Permissions for Worker Pool | `testIamPermissionsWorkerPool` | Returns the subset of the supplied permissions that the caller holds on a Cloud Run worker pool. No permissions are required to make this call. |
| Update Instance | `updateInstance` | Updates a Cloud Run instance. Returns a long-running operation to poll for completion. |
| Update Job | `updateJob` | Updates a Cloud Run job. Returns a long-running operation to poll for completion. |
| Update Service | `updateService` | Updates a Cloud Run service, typically to deploy a new revision template or change traffic splits. Returns a long-running operation to poll for completion. |
| Update Worker Pool | `updateWorkerPool` | Updates a Cloud Run worker pool. Returns a long-running operation to poll for completion. |
| Upload Source | `uploadSource` | Uploads a source archive to a Google Cloud Storage bucket through Cloud Run and returns the Cloud Storage path to reference in a deployment. You are responsible for the lifecycle of the uploaded object. |
| Wait For Operation | `waitOperation` | Waits until a Cloud Run long-running operation is done or the given timeout elapses, then returns its latest state. If the operation is already done the state is returned immediately. |
