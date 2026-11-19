---
description: "Trigger.dev v3 REST/Management API connector."
hidden: true
---

# Trigger.dev

<img src="../../.gitbook/assets/connectors/lg/triggerdev.png" alt="Trigger.dev logo">

Trigger and manage background task runs, batch triggers, schedules (CRUD + activate/deactivate), environment variables (CRUD + import), and queues (list/retrieve/concurrency override/reset/pause/resume). Base: https://api.trigger.dev. Auth: project-specific Secret API key (tr_...) as Bearer token.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [trigger.dev](https://trigger.dev) |
| **Authentication** | Bearer token |
| **Slug** | `triggerdev` |

## Use it

Add Trigger.dev from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.triggerdev.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Activate schedule</td><td><code>activateSchedule</code></td><td>Activate an IMPERATIVE schedule by its ID.</td></tr><tr><td>Add tags to a run</td><td><code>addRunTags</code></td><td>Adds one or more tags to a run. Runs can have a maximum of 10 tags. Duplicate tags are ignored.</td></tr><tr><td>Batch trigger tasks</td><td><code>batchTrigger</code></td><td>Batch trigger tasks with up to 1,000 payloads. Each item specifies the task and its payload/options. Returns the batchId and the IDs of all triggered runs.</td></tr><tr><td>Cancel a run</td><td><code>cancelRun</code></td><td>Cancels an in-progress run. If the run is already completed, this has no effect.</td></tr><tr><td>Create env var</td><td><code>createEnvVar</code></td><td>Create a new environment variable for a specific project and environment.</td></tr><tr><td>Create schedule</td><td><code>createSchedule</code></td><td>Create a new IMPERATIVE schedule for a task based on a CRON expression.</td></tr><tr><td>Deactivate schedule</td><td><code>deactivateSchedule</code></td><td>Deactivate an IMPERATIVE schedule by its ID.</td></tr><tr><td>Delete env var</td><td><code>deleteEnvVar</code></td><td>Delete a specific environment variable for a project and environment.</td></tr><tr><td>Delete schedule</td><td><code>deleteSchedule</code></td><td>Delete an IMPERATIVE schedule by its ID.</td></tr><tr><td>Get timezones</td><td><code>getTimezones</code></td><td>Get all supported IANA timezones that scheduled tasks support.</td></tr></tbody></table>

<details>

<summary>View 19 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Import env vars</td><td><code>importEnvVars</code></td><td>Upload multiple environment variables for a project and environment in one call.</td></tr><tr><td>List env vars</td><td><code>listEnvVars</code></td><td>List all environment variables for a specific project and environment. Returns a JSON array of {name, value} objects.</td></tr><tr><td>List queues</td><td><code>listQueues</code></td><td>List all queues in your environment with pagination support.</td></tr><tr><td>List runs</td><td><code>listRuns</code></td><td>List runs in the environment. Supports cursor pagination via page[size]/page[after]/page[before] and filtering via filter[status], filter[taskIdentifier], filter[version], filter[createdAt][period], filter[createdAt][from], filter[createdAt][to], filter[bulkAction], filter[schedule], filter[isTest] and filter[tag].</td></tr><tr><td>List schedules</td><td><code>listSchedules</code></td><td>List all schedules with pagination.</td></tr><tr><td>Override queue concurrency limit</td><td><code>overrideQueueConcurrency</code></td><td>Override the concurrency limit of a queue. Useful for temporarily scaling up or down based on demand.</td></tr><tr><td>Pause or resume queue</td><td><code>pauseQueue</code></td><td>Pause a queue to prevent new runs from starting, or resume a paused queue. Currently executing runs continue to completion.</td></tr><tr><td>Replay a run</td><td><code>replayRun</code></td><td>Creates a new run with the same payload and options as the original run.</td></tr><tr><td>Reschedule a run</td><td><code>rescheduleRun</code></td><td>Updates a delayed run with a new delay. Only valid when the run is in the DELAYED state.</td></tr><tr><td>Reset queue concurrency limit</td><td><code>resetQueueConcurrency</code></td><td>Reset the concurrency limit of a queue back to its base value defined in code.</td></tr><tr><td>Retrieve a run</td><td><code>retrieveRun</code></td><td>Retrieve information about a run, including its status, payload, output, and attempts.</td></tr><tr><td>Retrieve env var</td><td><code>retrieveEnvVar</code></td><td>Retrieve a specific environment variable for a project and environment.</td></tr><tr><td>Retrieve queue</td><td><code>retrieveQueue</code></td><td>Get a queue by its ID, or by type and name.</td></tr><tr><td>Retrieve run result</td><td><code>retrieveRunResult</code></td><td>Returns the execution result of a completed run. Returns 404 if the run doesn't exist or hasn't finished yet.</td></tr><tr><td>Retrieve schedule</td><td><code>retrieveSchedule</code></td><td>Get a schedule by its ID.</td></tr><tr><td>Trigger a task</td><td><code>triggerTask</code></td><td>Trigger a task by its identifier. Returns the ID of the run that was created.</td></tr><tr><td>Update env var</td><td><code>updateEnvVar</code></td><td>Update the value of a specific environment variable for a project and environment.</td></tr><tr><td>Update run metadata</td><td><code>updateRunMetadata</code></td><td>Update the metadata of a run.</td></tr><tr><td>Update schedule</td><td><code>updateSchedule</code></td><td>Update an IMPERATIVE schedule by its ID.</td></tr></tbody></table>

</details>
