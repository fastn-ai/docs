---
description: "Inngest is a durable execution platform for background jobs, step functions, scheduled workflows and AI agent orchestration."
hidden: true
---

# Inngest

Inngest is a durable execution platform for background jobs, step functions, scheduled workflows and AI agent orchestration. Send events to trigger functions, inspect and control function runs, manage apps, functions, environments, webhooks, experiments and sessions, and query run analytics with Insights.

| | |
| --- | --- |
| **Category** | [Cloud and DevOps](README.md) |
| **Website** | [inngest.com](https://inngest.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 66 |
| **Events** | 0 |
| **Slug** | `inngest` |

## Use it

Add Inngest from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.inngest.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Function Run | `cancelFunctionRun` | Cancels a running function immediately. No further steps run after a function is cancelled. |
| Cancel Run | `cancelRun` | Cancels an in-progress function run through the v2 API and returns the cancelled run ID. |
| Create Cancellation | `createCancellation` | Creates a bulk cancellation that cancels every run of a function started within the given time range, optionally narrowed by a CEL expression. |
| Create Environment | `createEnvironment` | Creates a custom environment in the connected Inngest account. |
| Create Environment Webhook | `createEnvironmentWebhook` | Creates a webhook in the connected environment through the v2 API, with an optional event filter and an optional GET responder used for provider verification challenges. |
| Create Partner Account | `createPartnerAccount` | Creates a sub-account under the connected account and returns its API key. Requires Inngest partner access on the account. |
| Create Run Scores | `createRunScores` | Records one or more named scores against a function run, or against specific steps when step IDs are supplied. Scores are stored as run metadata and aggregated for experiments. |
| Create Sandbox | `createSandbox` | Creates a sandbox with the given name, CPU and memory allocation, and environment variables. |
| Create Webhook | `createWebhook` | Creates a webhook endpoint that converts inbound HTTP requests into Inngest events using a JavaScript transform function. |
| Delete Cancellation | `deleteCancellation` | Deletes a bulk cancellation so that it stops cancelling further function runs. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook endpoint. Requests to its URL stop producing Inngest events. |
| Destroy Sandbox | `destroySandbox` | Destroys a sandbox and releases its compute resources. Running processes inside the sandbox are terminated. |
| Execute Sandbox Command | `executeSandboxCommand` | Runs a command inside a sandbox and waits for it to finish, returning the exit code and the base64-encoded standard output and error. |
| Generate Insights Query | `generateInsightsQuery` | Translates a natural-language prompt into an Insights SQL query and returns the generated SQL with a plain-language summary of what it does. |
| Get Account | `getAccount` | Retrieves the Inngest account that the connected signing key belongs to. |
| Get App | `getApp` | Retrieves a single app by its user-defined app ID, including its latest sync metadata and function count. |
| Get Event | `getEvent` | Retrieves a single event from the connected Inngest environment by its internal event ID. |
| Get Experiment | `getExperiment` | Retrieves variant run counts and score aggregates for one experiment on one function. |
| Get Function | `getFunction` | Retrieves a single function's configuration and status within an app. |
| Get Function Run | `getFunctionRun` | Retrieves a single function run by its run ID, including its status and the data returned by the function handler. |
| Get Run Summary | `getRunSummary` | Retrieves the canonical summary for a single function run, including timings, trigger and status. |
| Get Run Trace | `getRunTrace` | Retrieves the full trace tree for a single function run, showing every step, its status and timing. |
| Get Sandbox | `getSandbox` | Retrieves a single sandbox by ID, including its status and allocated resources. |
| Get Sandbox Logs | `getSandboxLogs` | Retrieves the log output produced by a sandbox. Leave Follow unset to return the logs currently available rather than holding the connection open. |
| Get Sandbox Process | `getSandboxProcess` | Retrieves the current state of a single process inside a sandbox. |
| Get Sandbox Process Output | `getSandboxProcessOutput` | Retrieves the buffered standard output and error chunks produced by a sandbox process. |
| Get Webhook | `getWebhook` | Retrieves a single webhook endpoint's configuration, including its inbound URL and transform function. |
| Invoke Function | `invokeFunction` | Invokes a function directly with the supplied input data and returns the resulting run ID. Supply an idempotency key to make repeated invocations safe. |
| List Apps | `listApps` | Lists the apps synced to the connected Inngest environment. Set Archived to true to list archived apps instead of active ones. |
| List Cancellations | `listCancellations` | Lists every bulk cancellation configured in the connected Inngest environment. |
| List Environment Webhooks | `listEnvironmentWebhooks` | Lists the webhooks in the connected environment through the v2 API, including each webhook's event allow or deny filter. |
| List Environments | `listEnvironments` | Lists the environments in the connected Inngest account, including production and branch environments. |
| List Event Function Runs | `listEventFunctionRuns` | Lists the function runs that were triggered by a specific event, including each run's status and output. |
| List Event Keys | `listEventKeys` | Lists the event keys for the connected account. Event keys are used to send events to Inngest. Without an environment override this returns the production environment's keys. |
| List Event Runs | `listEventRuns` | Lists the function runs triggered by a specific event through the v2 API, with pagination and optional output. |
| List Events | `listEvents` | Lists events received by the connected Inngest environment, optionally filtered by event name and received-at time range. |
| List Experiments | `listExperiments` | Lists every experiment observed in the connected Inngest environment, optionally scoped to one app or function. |
| List Function Experiments | `listFunctionExperiments` | Lists the experiments observed for a single function, with variant counts and run totals. |
| List Function Run Jobs | `listFunctionRunJobs` | Lists a subset of the jobs queued for a function run, in order from earliest to latest, showing each job's position in the function queue. Results are cached for five seconds. |
| List Function Runs | `listFunctionRuns` | Lists runs for a single function, filtered by time range and status. |
| List Functions | `listFunctions` | Lists the functions belonging to an app, with their triggers and flow-control configuration. |
| List Insights Event Schemas | `listInsightsEventSchemas` | Lists the observed event type schemas, each describing the JSON shape of one event's data. |
| List Insights Tables | `listInsightsTables` | Lists the tables available to the Insights query endpoint, with the columns and types of each. |
| List Partner Accounts | `listPartnerAccounts` | Lists the sub-accounts under the connected account. Requires Inngest partner access on the account. |
| List Runs | `listRuns` | Lists function runs across the connected Inngest environment, filtered by time range, status, app and function. |
| List Sandbox Processes | `listSandboxProcesses` | Lists the processes started inside a sandbox, with their state and exit codes. |
| List Sandboxes | `listSandboxes` | Lists the sandboxes in the connected Inngest environment. Sandboxes are isolated compute environments used to run untrusted or agent-generated code. |
| List Session Keys | `listSessionKeys` | Lists the session keys observed in the connected Inngest environment. A session key groups related runs, such as all runs for one end user. |
| List Session Runs | `listSessionRuns` | Lists the function runs associated with a single session ID. |
| List Sessions | `listSessions` | Lists the individual sessions recorded under one session key, with run counts and failure rates. |
| List Signing Keys | `listSigningKeys` | Lists the signing keys for the connected account. Signing keys authenticate the REST API and requests from Inngest to your app. Without an environment override this returns the production environment's keys. |
| List Webhooks | `listWebhooks` | Lists every webhook endpoint configured in the connected Inngest environment. A webhook endpoint gives an external service a URL whose requests are transformed into Inngest events. |
| Query Insights | `queryInsights` | Runs an Insights query against your Inngest event and run data using modified ClickHouse SQL, returning typed columns and rows. |
| Read Sandbox File | `readSandboxFile` | Reads a file from a sandbox's filesystem and returns its contents. |
| Rerun Function Run | `rerunFunctionRun` | Creates a new run from an existing run's triggering event data, optionally restarting from a specific step with replacement input. |
| Resume Signal | `resumeSignal` | Resumes a function run that is waiting on a signal, delivering the supplied data to the waiting step. |
| Send Event | `sendEvent` | Sends a single event to Inngest, triggering every function subscribed to that event name. Uses the Inngest Event API with the connection's event key. |
| Send Events | `sendEvents` | Sends a batch of events to Inngest in a single request. Provide the events as a JSON array string; each element is a full event payload with a name and data. |
| Signal Sandbox Process | `signalSandboxProcess` | Sends an operating-system signal to a process inside a sandbox, for example 15 for SIGTERM or 9 for SIGKILL. |
| Start Sandbox Process | `startSandboxProcess` | Starts a long-running process inside a sandbox and returns immediately with the process ID. |
| Stream Sandbox Process Output | `streamSandboxProcessOutput` | Opens the streaming output feed for a sandbox process, returning output chunks as they are produced. |
| Sync App | `syncApp` | Triggers a sync of an app at the given Inngest serve endpoint URL, registering the app's current function configuration with Inngest. |
| Update Environment | `updateEnvironment` | Archives or unarchives an environment. Only the supplied fields are modified. |
| Update Webhook | `updateWebhook` | Updates a webhook endpoint's name or transform function. The inbound URL is unchanged. |
| Wait For Sandbox Process | `waitForSandboxProcess` | Waits for a sandbox process to exit and returns its final state and exit code. |
| Write Sandbox File | `writeSandboxFile` | Writes a file into a sandbox's filesystem. The file contents are supplied base64-encoded. |
