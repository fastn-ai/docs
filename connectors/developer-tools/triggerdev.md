---
description: "Trigger.dev v3 REST/Management API connector."
hidden: true
---

# Trigger.dev

Trigger.dev v3 REST/Management API connector. Trigger and manage background task runs, batch triggers, schedules (CRUD + activate/deactivate), environment variables (CRUD + import), and queues (list/retrieve/concurrency override/reset/pause/resume). Base: https://api.trigger.dev. Auth: project-specific Secret API key (tr_...) as Bearer token.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [trigger.dev](https://trigger.dev) |
| **Authentication** | Bearer token |
| **Actions** | 29 |
| **Events** | 0 |
| **Slug** | `triggerdev` |

## Use it

Add Trigger.dev from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.triggerdev.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate schedule | `activateSchedule` | Activate an IMPERATIVE schedule by its ID. |
| Add tags to a run | `addRunTags` | Adds one or more tags to a run. Runs can have a maximum of 10 tags. Duplicate tags are ignored. |
| Batch trigger tasks | `batchTrigger` | Batch trigger tasks with up to 1,000 payloads. Each item specifies the task and its payload/options. Returns the batchId and the IDs of all triggered runs. |
| Cancel a run | `cancelRun` | Cancels an in-progress run. If the run is already completed, this has no effect. |
| Create env var | `createEnvVar` | Create a new environment variable for a specific project and environment. |
| Create schedule | `createSchedule` | Create a new IMPERATIVE schedule for a task based on a CRON expression. |
| Deactivate schedule | `deactivateSchedule` | Deactivate an IMPERATIVE schedule by its ID. |
| Delete env var | `deleteEnvVar` | Delete a specific environment variable for a project and environment. |
| Delete schedule | `deleteSchedule` | Delete an IMPERATIVE schedule by its ID. |
| Get timezones | `getTimezones` | Get all supported IANA timezones that scheduled tasks support. |
| Import env vars | `importEnvVars` | Upload multiple environment variables for a project and environment in one call. |
| List env vars | `listEnvVars` | List all environment variables for a specific project and environment. Returns a JSON array of {name, value} objects. |
| List queues | `listQueues` | List all queues in your environment with pagination support. |
| List runs | `listRuns` | List runs in the environment. Supports cursor pagination via page[size]/page[after]/page[before] and filtering via filter[status], filter[taskIdentifier], filter[version], filter[createdAt][period], filter[createdAt][from], filter[createdAt][to], filter[bulkAction], filter[schedule], filter[isTest] and filter[tag]. |
| List schedules | `listSchedules` | List all schedules with pagination. |
| Override queue concurrency limit | `overrideQueueConcurrency` | Override the concurrency limit of a queue. Useful for temporarily scaling up or down based on demand. |
| Pause or resume queue | `pauseQueue` | Pause a queue to prevent new runs from starting, or resume a paused queue. Currently executing runs continue to completion. |
| Replay a run | `replayRun` | Creates a new run with the same payload and options as the original run. |
| Reschedule a run | `rescheduleRun` | Updates a delayed run with a new delay. Only valid when the run is in the DELAYED state. |
| Reset queue concurrency limit | `resetQueueConcurrency` | Reset the concurrency limit of a queue back to its base value defined in code. |
| Retrieve a run | `retrieveRun` | Retrieve information about a run, including its status, payload, output, and attempts. |
| Retrieve env var | `retrieveEnvVar` | Retrieve a specific environment variable for a project and environment. |
| Retrieve queue | `retrieveQueue` | Get a queue by its ID, or by type and name. |
| Retrieve run result | `retrieveRunResult` | Returns the execution result of a completed run. Returns 404 if the run doesn't exist or hasn't finished yet. |
| Retrieve schedule | `retrieveSchedule` | Get a schedule by its ID. |
| Trigger a task | `triggerTask` | Trigger a task by its identifier. Returns the ID of the run that was created. |
| Update env var | `updateEnvVar` | Update the value of a specific environment variable for a project and environment. |
| Update run metadata | `updateRunMetadata` | Update the metadata of a run. |
| Update schedule | `updateSchedule` | Update an IMPERATIVE schedule by its ID. |
