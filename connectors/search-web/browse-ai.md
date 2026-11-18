---
description: "Browse AI extracts and monitors data from any website with no-code robots."
hidden: true
---

# Browse AI

<img src="../../.gitbook/assets/connectors/lg/browse-ai.png" alt="Browse AI logo">

Browse AI extracts and monitors data from any website with no-code robots. This connector covers the complete Browse AI REST API v2: infrastructure status, teams, robots (list, get, update cookies), on-demand robot tasks (run, list with filters, get captured data), monitors (create, list, get, update, delete), bulk runs (create, list, get), robot webhooks (create, list, delete) and the robot event webhooks (task finished, task finished successfully or with error, captured data changed, table export finished) as bindable events.

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [browse.ai](https://browse.ai) |
| **Authentication** | Credentials you enter |
| **Slug** | `browseAi` |

## Use it

Add Browse AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.browseAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Bulk Run | `createBulkRun` | Bulk-runs a robot once per entry in the input parameters array (up to 50,000 tasks) under an optional title, returning the bulk run with its task counts. Consumes credits per task; returns 403 credits_limit_reached or exceeded_bulk_run_threshold when limits are hit. |
| Create Robot Monitor | `createRobotMonitor` | Creates a monitor that runs a robot on a recurring schedule with the given input parameters and emails you when captured texts or screenshots change beyond the threshold. Provide the schedule as fixed-interval schedules in minutes; intervals below the plan minimum return 403 schedule_interval_below_minimum. |
| Create Robot Webhook | `createRobotWebhook` | Registers a webhook on a robot so Browse AI POSTs to your URL when the chosen event happens: taskFinished, taskFinishedSuccessfully, taskFinishedWithError, taskCapturedDataChanged or tableExportFinishedSuccessfully. Returns the new webhook with its id. |
| Delete Robot Monitor | `deleteRobotMonitor` | Deletes a monitor from a robot and returns the deleted monitor. |
| Delete Robot Webhook | `deleteRobotWebhook` | Deletes a webhook from a robot so Browse AI stops posting that event to its URL. |
| Get Bulk Run | `getBulkRun` | Retrieves a bulk run with its task counts and a paginated list of the tasks run within it, including each task's captured data. |
| Get Robot | `getRobot` | Retrieves a single robot by id with its name, creation timestamp and input parameter definitions (labels, types, defaults, options). |
| Get Robot Monitor | `getRobotMonitor` | Retrieves one monitor of a robot with its schedule, notification settings, input parameters and status. |
| Get Robot Task | `getRobotTask` | Retrieves a task's details and captured data (texts, lists, screenshots), its status, timing, input parameters and, when available, a temporary URL for the captured data and the run video. |
| Get System Status | `getSystemStatus` | Returns the real-time operational status of the Browse AI infrastructure, including whether the tasks queue is running normally or under maintenance. |

<details>

<summary>See 8 more actions</summary>

* **List Bulk Runs** `listBulkRuns`: Lists a robot's bulk runs with their status and task counts, paginated.
* **List Robot Monitors** `listRobotMonitors`: Lists the monitors configured on a robot with their schedules, notification settings, input parameters and active or paused status.
* **List Robot Tasks** `listRobotTasks`: Lists a robot's tasks with pagination and filters by status, bulk run, creation date range and retried tasks, sorted by the given fields. Each task carries its status, input parameters and captured texts, lists and screenshots.
* **List Robot Webhooks** `listRobotWebhooks`: Lists the webhooks registered on a robot with their target URL and subscribed event type.
* **List Robots** `listRobots`: Lists all robots under your team with their ids, names, creation timestamps and input parameter definitions. Robots are created in the Browse AI dashboard; use the returned ids with the task, monitor, bulk run and webhook actions.
* **Run Robot** `runRobot`: Runs a robot on demand with optional input parameter overrides and optional video recording, creating a task. The response contains the new task; receive the captured data through the robot's webhooks or poll Get Robot Task until the task finishes. Consumes Browse AI credits; returns 403 credits_limit_reached when the team is out of credits.
* **Update Robot Cookies** `updateRobotCookies`: Replaces the cookies a robot uses when it runs, for example to keep it logged in to a site. The request body is an array of cookie objects (name and value required; domain, path, expirationDate, hostOnly, httpOnly and secure optional). Returns the updated cookie list.
* **Update Robot Monitor** `updateRobotMonitor`: Updates a robot monitor: name, input parameters, notification settings, schedule, or status (paused to stop it, active to resume). Only the fields you pass are changed.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Table Export Finished Successfully | `tableExportFinishedSuccessfully` | A table export of the robot's captured data finished (Beta). Registered on the robot given as robotId. Payload per the Browse AI OpenAPI tableExportWebhook schema: exportId, robotId, robotName, exportFile, filesTemporaryUrl[], filesTemporaryUrlExpiresAt, exportCreatedAt, exportFinishedAt; modelled from docs, not captured. |
| Task Captured Data Changed | `taskCapturedDataChanged` | A run of the robot captured data that differs from the previous run (used with monitors). Registered on the robot given as robotId. Payload: { event: 'task.capturedDataChanged', task: RobotTask } per the Browse AI OpenAPI webhook schema; modelled from docs, not captured. |
| Task Finished | `taskFinished` | A run (task) of the robot finished, successfully or with an error. Browse AI registers this webhook on the robot whose id you provide as robotId. Payload: { event: 'task.finishedSuccessfully' \| 'task.finishedWithError', task: RobotTask } per the Browse AI OpenAPI webhook schema (taskWebhook); modelled from the vendor's documented schema, not captured, because this account has no robot yet. |
| Task Finished Successfully | `taskFinishedSuccessfully` | A run (task) of the robot finished successfully. Registered on the robot given as robotId. Payload: { event: 'task.finishedSuccessfully', task: RobotTask } per the Browse AI OpenAPI webhook schema; modelled from docs, not captured. |
| Task Finished With Error | `taskFinishedWithError` | A run (task) of the robot failed. Registered on the robot given as robotId. Payload: { event: 'task.finishedWithError', task: RobotTask with userFriendlyError } per the Browse AI OpenAPI webhook schema; modelled from docs, not captured. |
