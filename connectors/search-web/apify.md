---
description: "Apify is a cloud platform for web scraping, browser automation and data extraction."
hidden: true
---

# Apify

<img src="../../.gitbook/assets/connectors/apify.png" alt="Apify logo" width="64">

Apify is a cloud platform for web scraping, browser automation and data extraction. This connector covers the full Apify API v2: Actors and their versions, environment variables, builds and runs; Actor tasks; standalone runs and builds; key-value stores, datasets and request queues; schedules; webhooks and webhook dispatches; logs; Apify Store; user account, usage and limits; and the signing utilities.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [apify.com](https://apify.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `apify` |

## Use it

Add Apify from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.apify.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abort Actor Build | `abortActorBuild` | Aborts a build of an Actor that is still running and returns the updated build record. |
| Abort Actor Run | `abortActorRun` | Stops a running Actor run. A graceful abort gives the Actor a chance to clean up before it is terminated. This is the Actor-scoped form of the endpoint (deprecated by Apify in favour of the actor-runs namespace) and requires the owning Actor id as well as the run id. |
| Abort Actor Task's Last Run | `abortActorTaskLastRun` | Stops a running Actor run. A graceful abort gives the Actor a chance to clean up before it is terminated. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Abort Actor's Last Run | `abortActorLastRun` | Stops a running Actor run. A graceful abort gives the Actor a chance to clean up before it is terminated. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Abort Build | `abortBuild` | Stops an Actor build that is still in progress and returns the updated build record. |
| Abort Run | `abortRun` | Stops a running Actor run. A graceful abort gives the Actor a chance to clean up before it is terminated. |
| Add Request To Actor Task's Last Run Request Queue | `addRequestToActorTaskLastRunRequestQueue` | Adds a single request to the default request queue of an Actor run. A request with an existing unique key is not added twice. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Add Request To Actor's Last Run Request Queue | `addRequestToActorLastRunRequestQueue` | Adds a single request to the default request queue of an Actor run. A request with an existing unique key is not added twice. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Add Request To Request Queue | `addRequestToRequestQueue` | Adds a single request to a request queue. A request with an existing unique key is not added twice. |
| Add Request To Run Request Queue | `addRequestToRunRequestQueue` | Adds a single request to the default request queue of an Actor run. A request with an existing unique key is not added twice. |

<details>

<summary>See 210 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Batch Add Requests To Actor Task's Last Run Request Queue | `batchAddRequestsToActorTaskLastRunRequestQueue` | Adds up to 25 requests at once to the default request queue of an Actor run and reports which were processed and which failed. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Batch Add Requests To Actor's Last Run Request Queue | `batchAddRequestsToActorLastRunRequestQueue` | Adds up to 25 requests at once to the default request queue of an Actor run and reports which were processed and which failed. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Batch Add Requests To Request Queue | `batchAddRequestsToRequestQueue` | Adds up to 25 requests at once to a request queue and reports which were processed and which failed. |
| Batch Add Requests To Run Request Queue | `batchAddRequestsToRunRequestQueue` | Adds up to 25 requests at once to the default request queue of an Actor run and reports which were processed and which failed. |
| Batch Delete Requests From Actor Task's Last Run Request Queue | `batchDeleteRequestsFromActorTaskLastRunRequestQueue` | Deletes a batch of requests from the default request queue of an Actor run, identified by their unique keys. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Batch Delete Requests From Actor's Last Run Request Queue | `batchDeleteRequestsFromActorLastRunRequestQueue` | Deletes a batch of requests from the default request queue of an Actor run, identified by their unique keys. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Batch Delete Requests From Request Queue | `batchDeleteRequestsFromRequestQueue` | Deletes a batch of requests from a request queue, identified by their unique keys. |
| Batch Delete Requests From Run Request Queue | `batchDeleteRequestsFromRunRequestQueue` | Deletes a batch of requests from the default request queue of an Actor run, identified by their unique keys. |
| Build Actor | `buildActor` | Starts a build of a specific Actor version and returns the build record. Set Wait For Finish to block until the build completes or the wait elapses. |
| Charge Run Events | `chargeRunEvents` | Charges a pay-per-event Actor run for a number of occurrences of a named event. Only the Actor's own run may charge itself, and the idempotency key prevents double billing on retries. |
| Create Actor | `createActor` | Creates a new Actor in the account. At least one version with its source files or a source URL must be supplied so the Actor can be built. |
| Create Actor Task | `createActorTask` | Creates an Actor task, which stores a named input and run configuration for an Actor so it can be re-run on demand or on a schedule. |
| Create Actor Version | `createActorVersion` | Creates a new version of an Actor. Supply the source that matches the chosen source type: sourceFiles, gitRepoUrl, tarballUrl or gitHubGistUrl. |
| Create Actor Version Environment Variable | `createActorVersionEnvVar` | Adds an environment variable to a specific version of an Actor. Variables marked as secret are encrypted at rest and never returned in read calls. |
| Create Dataset | `createDataset` | Creates a named dataset, or returns the existing dataset if one with that name already exists. |
| Create Key-Value Store | `createKeyValueStore` | Creates a named key-value store, or returns the existing store if one with that name already exists. |
| Create Request Queue | `createRequestQueue` | Creates a named request queue, or returns the existing queue if one with that name already exists. |
| Create Schedule | `createSchedule` | Creates a schedule that starts the listed Actors or Actor tasks whenever its cron expression fires. |
| Create Webhook | `createWebhook` | Creates a webhook that posts to a URL whenever the chosen run events occur on the Actor or task named in the condition. |
| Decode And Verify Object | `decodeAndVerifyObject` | Verifies the signature of a token produced by Encode And Sign Object and returns the original JSON object. |
| Delete Actor | `deleteActor` | Permanently deletes an Actor together with all of its versions, builds and runs. This cannot be undone. |
| Delete Actor Last Run Dataset | `deleteActorLastRunDataset` | Permanently deletes the default dataset of an Actor's most recent run together with all of its items. |
| Delete Actor Task | `deleteActorTask` | Permanently deletes an Actor task. Runs already started by the task are not affected. |
| Delete Actor Task's Last Run Dataset | `deleteActorTaskLastRunDataset` | Permanently deletes the default dataset of an Actor run together with all of its items. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Actor Task's Last Run Key-Value Store | `deleteActorTaskLastRunKeyValueStore` | Permanently deletes the default key-value store of an Actor run together with all of its records. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Actor Task's Last Run Key-Value Store Record | `deleteActorTaskLastRunKeyValueStoreRecord` | Deletes a single record from the default key-value store of an Actor run. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Actor Task's Last Run Request Queue | `deleteActorTaskLastRunRequestQueue` | Permanently deletes the default request queue of an Actor run together with all of its requests. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Actor Task's Last Run Request Queue Request | `deleteActorTaskLastRunRequestQueueRequest` | Removes a single request from the default request queue of an Actor run. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Actor Task's Last Run Request Queue Request Lock | `deleteActorTaskLastRunRequestQueueRequestLock` | Releases the lock this client holds on a single request in the default request queue of an Actor run. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Actor Version | `deleteActorVersion` | Permanently deletes a single version of an Actor. |
| Delete Actor Version Environment Variable | `deleteActorVersionEnvVar` | Removes an environment variable from a specific version of an Actor. |
| Delete Actor's Last Run Key-Value Store | `deleteActorLastRunKeyValueStore` | Permanently deletes the default key-value store of an Actor run together with all of its records. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Actor's Last Run Key-Value Store Record | `deleteActorLastRunKeyValueStoreRecord` | Deletes a single record from the default key-value store of an Actor run. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Actor's Last Run Request Queue | `deleteActorLastRunRequestQueue` | Permanently deletes the default request queue of an Actor run together with all of its requests. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Actor's Last Run Request Queue Request | `deleteActorLastRunRequestQueueRequest` | Removes a single request from the default request queue of an Actor run. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Actor's Last Run Request Queue Request Lock | `deleteActorLastRunRequestQueueRequestLock` | Releases the lock this client holds on a single request in the default request queue of an Actor run. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Delete Build | `deleteBuild` | Permanently deletes an Actor build. A build that is still tagged as the Actor's default cannot be deleted. |
| Delete Dataset | `deleteDataset` | Permanently deletes a dataset together with all of its items. |
| Delete Key-Value Store | `deleteKeyValueStore` | Permanently deletes a key-value store together with all of its records. |
| Delete Key-Value Store Record | `deleteKeyValueStoreRecord` | Deletes a single record from a key-value store. |
| Delete Request Queue | `deleteRequestQueue` | Permanently deletes a request queue together with all of its requests. |
| Delete Request Queue Request | `deleteRequestQueueRequest` | Removes a single request from a request queue. |
| Delete Request Queue Request Lock | `deleteRequestQueueRequestLock` | Releases the lock this client holds on a single request in a request queue. |
| Delete Run | `deleteRun` | Permanently deletes a finished Actor run. A run that is still in progress must be aborted first. |
| Delete Run Dataset | `deleteRunDataset` | Permanently deletes the default dataset of an Actor run together with all of its items. |
| Delete Run Key-Value Store | `deleteRunKeyValueStore` | Permanently deletes the default key-value store of an Actor run together with all of its records. |
| Delete Run Key-Value Store Record | `deleteRunKeyValueStoreRecord` | Deletes a single record from the default key-value store of an Actor run. |
| Delete Run Request Queue | `deleteRunRequestQueue` | Permanently deletes the default request queue of an Actor run together with all of its requests. |
| Delete Run Request Queue Request | `deleteRunRequestQueueRequest` | Removes a single request from the default request queue of an Actor run. |
| Delete Run Request Queue Request Lock | `deleteRunRequestQueueRequestLock` | Releases the lock this client holds on a single request in the default request queue of an Actor run. |
| Delete Schedule | `deleteSchedule` | Permanently deletes a schedule so it stops starting Actors or tasks. |
| Delete Webhook | `deleteWebhook` | Permanently deletes a webhook so it stops receiving events. |
| Download Actor Task's Last Run Key-Value Store Records | `downloadActorTaskLastRunKeyValueStoreRecords` | Downloads the records of an Actor run's default key-value store as a single ZIP archive. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Download Actor's Last Run Key-Value Store Records | `downloadActorLastRunKeyValueStoreRecords` | Downloads the records of an Actor run's default key-value store as a single ZIP archive. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Download Key-Value Store Records | `downloadKeyValueStoreRecords` | Downloads the records of a key-value store as a single ZIP archive. |
| Download Run Key-Value Store Records | `downloadRunKeyValueStoreRecords` | Downloads the records of an Actor run's default key-value store as a single ZIP archive. |
| Encode And Sign Object | `encodeAndSignObject` | Encodes a JSON object into a signed, tamper-proof token that can safely be passed through a third party and decoded later. |
| Get Account Limits | `getAccountLimits` | Retrieves the account's plan limits and the spending caps currently configured on it. |
| Get Actor | `getActor` | Retrieves a single Actor by its id or by the username~actor-name shorthand, including its versions, default run options and usage statistics. |
| Get Actor Build | `getActorBuild` | Retrieves a single build of an Actor, including its status, usage and the resulting Docker image details. |
| Get Actor Build OpenAPI Definition | `getActorBuildOpenApiDefinition` | Retrieves the OpenAPI definition generated from a build's input schema, describing how that Actor can be called. |
| Get Actor Default Build | `getActorDefaultBuild` | Retrieves the build that an Actor's runs use by default, which is the build behind the Actor's default build tag. |
| Get Actor Last Run | `getActorLastRun` | Retrieves the most recent run of an Actor, optionally restricted to runs with a given status or origin. |
| Get Actor Last Run Dataset | `getActorLastRunDataset` | Retrieves the default dataset of an Actor's most recent run, including its item count and access settings. |
| Get Actor Last Run Dataset Statistics | `getActorLastRunDatasetStatistics` | Retrieves field-level statistics for the default dataset of an Actor's most recent run. |
| Get Actor Run | `getActorRun` | Retrieves a single Actor run by id, including its status, timings, usage and the ids of its default storages. This is the Actor-scoped form of the endpoint (deprecated by Apify in favour of the actor-runs namespace) and requires the owning Actor id as well as the run id. |
| Get Actor Task | `getActorTask` | Retrieves a single Actor task by its id or by the username~task-name shorthand. |
| Get Actor Task Input | `getActorTaskInput` | Retrieves only the saved input of an Actor task, as it will be passed to the Actor when the task runs. |
| Get Actor Task Last Run | `getActorTaskLastRun` | Retrieves the most recent run started from an Actor task, optionally restricted to runs with a given status or origin. |
| Get Actor Task's Last Run Dataset | `getActorTaskLastRunDataset` | Retrieves the default dataset of an Actor run, including its item count and access settings. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor Task's Last Run Dataset Items | `getActorTaskLastRunDatasetItems` | Retrieves the items a run wrote to its default dataset, with paging, field selection and format options. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor Task's Last Run Dataset Statistics | `getActorTaskLastRunDatasetStatistics` | Retrieves field-level statistics for the default dataset of an Actor run, such as how often each field is populated. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor Task's Last Run Key-Value Store | `getActorTaskLastRunKeyValueStore` | Retrieves the default key-value store of an Actor run, including its name and access settings. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor Task's Last Run Key-Value Store Record | `getActorTaskLastRunKeyValueStoreRecord` | Retrieves a single record from the default key-value store of an Actor run. The run's result is normally stored under the key OUTPUT. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor Task's Last Run Log | `getActorTaskLastRunLog` | Retrieves the console log produced by an Actor run as plain text. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor Task's Last Run Request Queue | `getActorTaskLastRunRequestQueue` | Retrieves the default request queue of an Actor run, including how many requests are pending and handled. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor Task's Last Run Request Queue Head | `getActorTaskLastRunRequestQueueHead` | Returns the next unhandled requests waiting at the head of the default request queue of an Actor run, without locking them. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor Task's Last Run Request Queue Request | `getActorTaskLastRunRequestQueueRequest` | Retrieves a single request from the default request queue of an Actor run by its request id. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor Version | `getActorVersion` | Retrieves a single version of an Actor by its version number. |
| Get Actor Version Environment Variable | `getActorVersionEnvVar` | Retrieves a single environment variable of an Actor version by name. The value of a secret variable is not returned. |
| Get Actor's Last Run Dataset Items | `getActorLastRunDatasetItems` | Retrieves the items a run wrote to its default dataset, with paging, field selection and format options. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor's Last Run Key-Value Store | `getActorLastRunKeyValueStore` | Retrieves the default key-value store of an Actor run, including its name and access settings. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor's Last Run Key-Value Store Record | `getActorLastRunKeyValueStoreRecord` | Retrieves a single record from the default key-value store of an Actor run. The run's result is normally stored under the key OUTPUT. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor's Last Run Log | `getActorLastRunLog` | Retrieves the console log produced by an Actor run as plain text. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor's Last Run Request Queue | `getActorLastRunRequestQueue` | Retrieves the default request queue of an Actor run, including how many requests are pending and handled. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor's Last Run Request Queue Head | `getActorLastRunRequestQueueHead` | Returns the next unhandled requests waiting at the head of the default request queue of an Actor run, without locking them. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get Actor's Last Run Request Queue Request | `getActorLastRunRequestQueueRequest` | Retrieves a single request from the default request queue of an Actor run by its request id. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get And Lock Actor Task's Last Run Request Queue Head | `getAndLockActorTaskLastRunRequestQueueHead` | Returns the next unhandled requests from the default request queue of an Actor run and locks them for this client so no other consumer picks them up. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get And Lock Actor's Last Run Request Queue Head | `getAndLockActorLastRunRequestQueueHead` | Returns the next unhandled requests from the default request queue of an Actor run and locks them for this client so no other consumer picks them up. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Get And Lock Request Queue Head | `getAndLockRequestQueueHead` | Returns the next unhandled requests from a request queue and locks them for this client so no other consumer picks them up. |
| Get And Lock Run Request Queue Head | `getAndLockRunRequestQueueHead` | Returns the next unhandled requests from the default request queue of an Actor run and locks them for this client so no other consumer picks them up. |
| Get Browser Info | `getBrowserInfo` | Returns the client IP address and the HTTP headers Apify received, which is useful for checking how a proxy or scraper appears to a target site. |
| Get Build | `getBuild` | Retrieves a single Actor build by id, including its status, usage and the input schema it exposes. |
| Get Build Log | `getBuildLog` | Retrieves the Docker build log of an Actor build as plain text. |
| Get Build OpenAPI Definition | `getBuildOpenApiDefinition` | Retrieves the OpenAPI definition generated from an Actor build's input schema, describing how that Actor can be called. |
| Get Current User | `getCurrentUser` | Retrieves the private profile of the account that owns the API token, including username, email, plan, proxy settings and effective platform feature flags. |
| Get Dataset | `getDataset` | Retrieves a single dataset by id, including its item count, field list and access settings. |
| Get Dataset Items | `getDatasetItems` | Retrieves the items stored in a dataset, with paging, field selection and a choice of output formats including JSON, CSV, XML and RSS. |
| Get Dataset Statistics | `getDatasetStatistics` | Retrieves field-level statistics for a dataset, such as how often each field is populated across its items. |
| Get Key-Value Store | `getKeyValueStore` | Retrieves a single key-value store by id, including its name, size statistics and access settings. |
| Get Key-Value Store Record | `getKeyValueStoreRecord` | Retrieves the value stored under a given key in a key-value store, in whatever content type it was saved with. |
| Get Log | `getLog` | Retrieves the log of either an Actor run or an Actor build by its id, as plain text. |
| Get Monthly Usage | `getMonthlyUsage` | Retrieves the account's usage and charges for a billing month, broken down by chargeable service. |
| Get Public User | `getPublicUser` | Retrieves the public profile of any Apify user by id or username, which is the information shown on their Store page. |
| Get Request Queue | `getRequestQueue` | Retrieves a single request queue by id, including how many requests are pending and how many have been handled. |
| Get Request Queue Head | `getRequestQueueHead` | Returns the next unhandled requests waiting at the head of a request queue, without locking them. |
| Get Request Queue Request | `getRequestQueueRequest` | Retrieves a single request from a request queue by its request id. |
| Get Run | `getRun` | Retrieves a single Actor run by id, including its status, timings, usage and the ids of its default storages. |
| Get Run Dataset | `getRunDataset` | Retrieves the default dataset of an Actor run, including its item count and access settings. |
| Get Run Dataset Items | `getRunDatasetItems` | Retrieves the items a run wrote to its default dataset, with paging, field selection and format options. |
| Get Run Dataset Statistics | `getRunDatasetStatistics` | Retrieves field-level statistics for the default dataset of an Actor run, such as how often each field is populated. |
| Get Run Key-Value Store | `getRunKeyValueStore` | Retrieves the default key-value store of an Actor run, including its name and access settings. |
| Get Run Key-Value Store Record | `getRunKeyValueStoreRecord` | Retrieves a single record from the default key-value store of an Actor run. The run's result is normally stored under the key OUTPUT. |
| Get Run Log | `getRunLog` | Retrieves the console log produced by an Actor run as plain text. |
| Get Run Request Queue | `getRunRequestQueue` | Retrieves the default request queue of an Actor run, including how many requests are pending and handled. |
| Get Run Request Queue Head | `getRunRequestQueueHead` | Returns the next unhandled requests waiting at the head of the default request queue of an Actor run, without locking them. |
| Get Run Request Queue Request | `getRunRequestQueueRequest` | Retrieves a single request from the default request queue of an Actor run by its request id. |
| Get Schedule | `getSchedule` | Retrieves a single schedule by id, including its cron expression, timezone and the actions it starts. |
| Get Schedule Log | `getScheduleLog` | Retrieves the invocation history of a schedule, showing each time it fired and what it started. |
| Get Webhook | `getWebhook` | Retrieves a single webhook by id, including its condition, event types and delivery statistics. |
| Get Webhook Dispatch | `getWebhookDispatch` | Retrieves a single webhook delivery attempt, including the event type, the target URL and the response received. |
| List Actor Builds | `listActorBuilds` | Lists the builds of a given Actor, newest or oldest first, with paging. |
| List Actor Runs | `listActorRuns` | Lists the runs of a given Actor, optionally filtered by status and by the time the run started. |
| List Actor Task Runs | `listActorTaskRuns` | Lists the runs started from a given Actor task, optionally filtered by status. |
| List Actor Task Webhooks | `listActorTaskWebhooks` | Lists the webhooks whose trigger condition is scoped to a given Actor task. |
| List Actor Task's Last Run Key-Value Store Keys | `listActorTaskLastRunKeyValueStoreKeys` | Lists the record keys stored in the default key-value store of an Actor run, with cursor paging and an optional key prefix filter. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| List Actor Task's Last Run Request Queue Requests | `listActorTaskLastRunRequestQueueRequests` | Lists the requests held in the default request queue of an Actor run, in the order they were added. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| List Actor Tasks | `listActorTasks` | Lists the Actor tasks in the account. A task is a saved Actor configuration that can be run without supplying input each time. |
| List Actor Version Environment Variables | `listActorVersionEnvVars` | Lists the environment variables defined on a specific version of an Actor. Values of variables marked secret are not returned. |
| List Actor Versions | `listActorVersions` | Lists every version defined on an Actor, including its source type, build tag and environment variables. |
| List Actor Webhooks | `listActorWebhooks` | Lists the webhooks whose trigger condition is scoped to a given Actor. |
| List Actor's Last Run Key-Value Store Keys | `listActorLastRunKeyValueStoreKeys` | Lists the record keys stored in the default key-value store of an Actor run, with cursor paging and an optional key prefix filter. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| List Actor's Last Run Request Queue Requests | `listActorLastRunRequestQueueRequests` | Lists the requests held in the default request queue of an Actor run, in the order they were added. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| List Actors | `listActors` | Lists the Actors the account owns or has access to, sorted by creation date or last run time, with paging. |
| List Builds | `listBuilds` | Lists every Actor build in the account across all Actors, newest or oldest first. |
| List Datasets | `listDatasets` | Lists the datasets the account owns or has access to, optionally including the unnamed datasets created automatically by runs. |
| List Key-Value Store Keys | `listKeyValueStoreKeys` | Lists the record keys held in a key-value store, with cursor paging and an optional key prefix filter. |
| List Key-Value Stores | `listKeyValueStores` | Lists the key-value stores the account owns or has access to, optionally restricted to named stores or to a given ownership. |
| List Request Queue Requests | `listRequestQueueRequests` | Lists the requests held in a request queue, in the order they were added. |
| List Request Queues | `listRequestQueues` | Lists the request queues the account owns or has access to, optionally including the unnamed queues created automatically by runs. |
| List Run Key-Value Store Keys | `listRunKeyValueStoreKeys` | Lists the record keys stored in the default key-value store of an Actor run, with cursor paging and an optional key prefix filter. |
| List Run Request Queue Requests | `listRunRequestQueueRequests` | Lists the requests held in the default request queue of an Actor run, in the order they were added. |
| List Runs | `listRuns` | Lists every Actor run in the account across all Actors, optionally filtered by status and start time. |
| List Schedules | `listSchedules` | Lists the schedules in the account, each of which starts Actors or tasks on a cron expression. |
| List Webhook Dispatches | `listWebhookDispatches` | Lists every webhook delivery attempt made across the account, newest or oldest first. |
| List Webhook Dispatches For Webhook | `listWebhookDispatchesForWebhook` | Lists the delivery attempts made by a single webhook, including the HTTP status each attempt received. |
| List Webhooks | `listWebhooks` | Lists the webhooks configured in the account, including the events each one listens for and the URL it posts to. |
| Metamorph Actor Run | `metamorphActorRun` | Transforms a running Actor run into a run of a different Actor, keeping the same run id and storages. The new Actor's input is supplied as raw JSON text. This is the Actor-scoped form of the endpoint (deprecated by Apify in favour of the actor-runs namespace) and requires the owning Actor id as well as the run id. |
| Metamorph Actor Task's Last Run | `metamorphActorTaskLastRun` | Transforms a running Actor run into a run of a different Actor, keeping the same run id and storages. The new Actor's input is supplied as raw JSON text. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Metamorph Actor's Last Run | `metamorphActorLastRun` | Transforms a running Actor run into a run of a different Actor, keeping the same run id and storages. The new Actor's input is supplied as raw JSON text. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Metamorph Run | `metamorphRun` | Transforms a running Actor run into a run of a different Actor, keeping the same run id and storages. The new Actor's input is supplied as raw JSON text. |
| Prolong Actor Task's Last Run Request Queue Request Lock | `prolongActorTaskLastRunRequestQueueRequestLock` | Extends the lock this client holds on a request in the default request queue of an Actor run, keeping it reserved for longer. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Prolong Actor's Last Run Request Queue Request Lock | `prolongActorLastRunRequestQueueRequestLock` | Extends the lock this client holds on a request in the default request queue of an Actor run, keeping it reserved for longer. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Prolong Request Queue Request Lock | `prolongRequestQueueRequestLock` | Extends the lock this client holds on a request in a request queue, keeping it reserved for longer. |
| Prolong Run Request Queue Request Lock | `prolongRunRequestQueueRequestLock` | Extends the lock this client holds on a request in the default request queue of an Actor run, keeping it reserved for longer. |
| Reboot Actor Task's Last Run | `rebootActorTaskLastRun` | Restarts a running Actor run from the beginning while keeping the same run id and storages. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Reboot Actor's Last Run | `rebootActorLastRun` | Restarts a running Actor run from the beginning while keeping the same run id and storages. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Reboot Run | `rebootRun` | Restarts a running Actor run from the beginning while keeping the same run id and storages. |
| Resurrect Actor Run | `resurrectActorRun` | Restarts a finished, failed, timed-out or aborted run of an Actor, reusing the same storages so the run continues where it stopped. |
| Resurrect Run | `resurrectRun` | Restarts a finished, failed, timed-out or aborted run, reusing the same storages so the run continues where it stopped. |
| Run Actor | `runActor` | Starts an Actor run and returns immediately with the run record. The run input is the JSON object defined by that Actor's own input schema, so it is passed through as raw JSON text. |
| Run Actor Synchronously | `runActorSynchronously` | Runs an Actor, waits for it to finish and returns the record stored under the chosen key in the run's default key-value store, which is OUTPUT unless another key is given. |
| Run Actor Synchronously And Get Dataset Items | `runActorSyncGetDatasetItems` | Runs an Actor, waits for it to finish and returns the items its run wrote to the default dataset, in the requested format. |
| Run Actor Synchronously Without Input | `runActorSynchronouslyWithoutInput` | GET variant of the synchronous Actor run: starts the run without a request body (the Actor's default input is used), waits for it to finish and returns the OUTPUT record from the default key-value store. Apify documents this as a legacy form of the POST endpoint; the run consumes compute units. |
| Run Actor Synchronously Without Input And Get Dataset Items | `runActorSyncGetDatasetItemsWithoutInput` | GET variant of the synchronous Actor run: starts the run without a request body (the Actor's default input is used), waits for it to finish and returns the items of the default dataset. Apify documents this as a legacy form of the POST endpoint; the run consumes compute units. |
| Run Actor Task | `runActorTask` | Starts a run of an Actor task and returns immediately with the run record. The task's saved input is used unless an override input is supplied. |
| Run Actor Task Synchronously | `runActorTaskSynchronously` | Runs an Actor task, waits for it to finish and returns the record stored under the chosen key in the run's default key-value store, which is OUTPUT unless another key is given. |
| Run Actor Task Synchronously And Get Dataset Items | `runActorTaskSyncGetDatasetItems` | Runs an Actor task, waits for it to finish and returns the items its run wrote to the default dataset, in the requested format. |
| Run Actor Task Synchronously Without Input | `runActorTaskSynchronouslyWithoutInput` | GET variant of the synchronous Actor task run: starts the run without a request body (the task's saved input is used), waits for it to finish and returns the OUTPUT record from the default key-value store. Apify documents this as a legacy form of the POST endpoint; the run consumes compute units. |
| Run Actor Task Synchronously Without Input And Get Dataset Items | `runActorTaskSyncGetDatasetItemsWithoutInput` | GET variant of the synchronous Actor task run: starts the run without a request body (the task's saved input is used), waits for it to finish and returns the items of the default dataset. Apify documents this as a legacy form of the POST endpoint; the run consumes compute units. |
| Search Apify Store | `searchApifyStore` | Searches the public Apify Store for Actors, with filters for category, author, pricing model and free-text search. |
| Store Actor Task's Last Run Dataset Items | `storeActorTaskLastRunDatasetItems` | Appends one or more items to the default dataset of an Actor run. Items are supplied as a JSON array or a single JSON object serialized to text. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Store Actor Task's Last Run Key-Value Store Record | `storeActorTaskLastRunKeyValueStoreRecord` | Creates or replaces a record in the default key-value store of an Actor run. The value is supplied as raw JSON text. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Store Actor's Last Run Dataset Items | `storeActorLastRunDatasetItems` | Appends one or more items to the default dataset of an Actor run. Items are supplied as a JSON array or a single JSON object serialized to text. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Store Actor's Last Run Key-Value Store Record | `storeActorLastRunKeyValueStoreRecord` | Creates or replaces a record in the default key-value store of an Actor run. The value is supplied as raw JSON text. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Store Dataset Items | `storeDatasetItems` | Appends one or more items to a dataset. Items are supplied as a JSON array or a single JSON object serialized to text. |
| Store Key-Value Store Record | `storeKeyValueStoreRecord` | Creates or replaces the record stored under a given key in a key-value store. The value is supplied as raw JSON text. |
| Store Run Dataset Items | `storeRunDatasetItems` | Appends one or more items to the default dataset of an Actor run. Items are supplied as a JSON array or a single JSON object serialized to text. |
| Store Run Key-Value Store Record | `storeRunKeyValueStoreRecord` | Creates or replaces a record in the default key-value store of an Actor run. The value is supplied as raw JSON text. |
| Test Webhook | `testWebhook` | Sends a dummy event to a webhook's target URL so the receiving endpoint can be verified, and returns the resulting dispatch record. |
| Unlock Actor Task's Last Run Request Queue Requests | `unlockActorTaskLastRunRequestQueueRequests` | Releases every lock this client holds on requests in the default request queue of an Actor run, making them available to other consumers. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Unlock Actor's Last Run Request Queue Requests | `unlockActorLastRunRequestQueueRequests` | Releases every lock this client holds on requests in the default request queue of an Actor run, making them available to other consumers. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Unlock Request Queue Requests | `unlockRequestQueueRequests` | Releases every lock this client holds on requests in a request queue, making them available to other consumers. |
| Unlock Run Request Queue Requests | `unlockRunRequestQueueRequests` | Releases every lock this client holds on requests in the default request queue of an Actor run, making them available to other consumers. |
| Update Account Limits | `updateAccountLimits` | Updates the account's monthly spending cap and how long run data is retained. |
| Update Actor | `updateActor` | Updates an existing Actor. Only the fields supplied are changed; everything else on the Actor is preserved. |
| Update Actor Last Run Dataset | `updateActorLastRunDataset` | Renames the default dataset of an Actor's most recent run or changes who may access it. |
| Update Actor Task | `updateActorTask` | Updates an Actor task. Only the fields supplied are changed; everything else on the task is preserved. |
| Update Actor Task Input | `updateActorTaskInput` | Replaces the saved input of an Actor task. The shape of the input is defined by the Actor's own input schema, so it is passed through as raw JSON text. |
| Update Actor Task's Last Run Dataset | `updateActorTaskLastRunDataset` | Renames the default dataset of an Actor task's most recent run or changes who may access it. This shortcut resolves the task's last run instead of taking a run id; the run status and origin filters are not available on this update because Apify validates the request body strictly. |
| Update Actor Task's Last Run Key-Value Store | `updateActorTaskLastRunKeyValueStore` | Renames the default key-value store of an Actor task's most recent run or changes who may access it. This shortcut resolves the task's last run instead of taking a run id; the run status and origin filters are not available on this update because Apify validates the request body strictly. |
| Update Actor Task's Last Run Request Queue | `updateActorTaskLastRunRequestQueue` | Renames the default request queue of an Actor task's most recent run or changes who may access it. This shortcut resolves the task's last run instead of taking a run id; the run status and origin filters are not available on this update because Apify validates the request body strictly. |
| Update Actor Task's Last Run Request Queue Request | `updateActorTaskLastRunRequestQueueRequest` | Updates a request in the default request queue of an Actor run, for example to change its URL or move it to the front. This shortcut resolves the Actor task's last run (optionally filtered by status or origin) instead of taking a run id. |
| Update Actor Version | `updateActorVersion` | Updates an existing version of an Actor, for example to replace its source files or change its build tag. |
| Update Actor Version Environment Variable | `updateActorVersionEnvVar` | Updates an environment variable on an Actor version, replacing its name, value and secret flag. |
| Update Actor's Last Run Key-Value Store | `updateActorLastRunKeyValueStore` | Renames the default key-value store of an Actor's most recent run or changes who may access it. This shortcut resolves the Actor's last run instead of taking a run id; the run status and origin filters are not available on this update because Apify validates the request body strictly. |
| Update Actor's Last Run Request Queue | `updateActorLastRunRequestQueue` | Renames the default request queue of an Actor's most recent run or changes who may access it. This shortcut resolves the Actor's last run instead of taking a run id; the run status and origin filters are not available on this update because Apify validates the request body strictly. |
| Update Actor's Last Run Request Queue Request | `updateActorLastRunRequestQueueRequest` | Updates a request in the default request queue of an Actor run, for example to change its URL or move it to the front. This shortcut resolves the Actor's last run (optionally filtered by status or origin) instead of taking a run id. |
| Update Dataset | `updateDataset` | Renames a dataset or changes who may access it. |
| Update Key-Value Store | `updateKeyValueStore` | Renames a key-value store or changes who may access it. |
| Update Request Queue | `updateRequestQueue` | Renames a request queue or changes who may access it. |
| Update Request Queue Request | `updateRequestQueueRequest` | Updates a request in a request queue, for example to change its URL or move it to the front of the queue. |
| Update Run | `updateRun` | Updates a run's status message or changes who may access it. Only the fields supplied are changed. |
| Update Run Dataset | `updateRunDataset` | Renames the default dataset of an Actor run or changes who may access it. |
| Update Run Key-Value Store | `updateRunKeyValueStore` | Renames the default key-value store of an Actor run or changes who may access it. |
| Update Run Request Queue | `updateRunRequestQueue` | Renames the default request queue of an Actor run or changes who may access it. |
| Update Run Request Queue Request | `updateRunRequestQueueRequest` | Updates a request in the default request queue of an Actor run, for example to mark it handled. |
| Update Schedule | `updateSchedule` | Updates a schedule, for example to change its cron expression or to enable or disable it. |
| Update Webhook | `updateWebhook` | Updates an existing webhook. Only the fields supplied are changed; everything else on the webhook is preserved. |
| Validate Actor Input | `validateActorInput` | Checks a proposed run input against an Actor build's input schema and reports any validation errors without starting a run. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Actor Build Aborted | `ACTOR.BUILD.ABORTED` | Fires when a build of the watched Actor is aborted. |
| Actor Build Created | `ACTOR.BUILD.CREATED` | Fires as soon as a build of the watched Actor is created, before it starts building. |
| Actor Build Failed | `ACTOR.BUILD.FAILED` | Fires when a build of the watched Actor fails. |
| Actor Build Succeeded | `ACTOR.BUILD.SUCCEEDED` | Fires when a build of the watched Actor completes successfully. |
| Actor Build Timed Out | `ACTOR.BUILD.TIMED_OUT` | Fires when a build of the watched Actor is killed because it exceeded its timeout. |
| Actor Run Aborted | `ACTOR.RUN.ABORTED` | Fires when a run of the watched Actor or Actor task is aborted by a user or by the API. |
| Actor Run Created | `ACTOR.RUN.CREATED` | Fires as soon as a run of the watched Actor or Actor task is created, before it starts executing. |
| Actor Run Failed | `ACTOR.RUN.FAILED` | Fires when a run of the watched Actor or Actor task ends with a non-zero exit code. |
| Actor Run Resurrected | `ACTOR.RUN.RESURRECTED` | Fires when a finished run of the watched Actor or Actor task is resurrected and starts again. |
| Actor Run Succeeded | `ACTOR.RUN.SUCCEEDED` | Fires when a run of the watched Actor or Actor task finishes successfully. |

<details>

<summary>See 1 more event</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Actor Run Timed Out | `ACTOR.RUN.TIMED_OUT` | Fires when a run of the watched Actor or Actor task is killed because it exceeded its timeout. |

</details>
