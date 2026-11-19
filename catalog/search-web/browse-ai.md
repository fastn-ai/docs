---
description: "Browse AI runs no-code robots that extract and monitor website data. Run robot tasks and bulk runs, and manage monitors and webhooks."
hidden: true
---

# Browse AI

<img src="../../.gitbook/assets/connectors/lg/browse-ai.png" alt="Browse AI logo">

| | |
| --- | --- |
| **Category** | [Search and web](README.md) |
| **Website** | [browse.ai](https://browse.ai) |
| **Authentication** | API key |
| **Slug** | `browseAi` |

## Setup

Your customers enter their API key for Browse AI when they connect. Nothing else needs setting up.

## Use it

Add Browse AI from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.browseAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Bulk Run</td><td><code>createBulkRun</code></td><td>Bulk-runs a robot once per entry in the input parameters array (up to 50,000 tasks) under an optional title, returning the bulk run with its task counts. Consumes credits per task</td></tr><tr><td>Create Robot Monitor</td><td><code>createRobotMonitor</code></td><td>Creates a monitor that runs a robot on a recurring schedule with the given input parameters and emails you when captured texts or screenshots change beyond the threshold. Provide the schedule as fixed-interval schedules in minutes; intervals below the plan minimum return 403 schedule_interval_below_minimum.</td></tr><tr><td>Create Robot Webhook</td><td><code>createRobotWebhook</code></td><td>Registers a webhook on a robot so Browse AI POSTs to your URL when the chosen event happens: taskFinished, taskFinishedSuccessfully, taskFinishedWithError, taskCapturedDataChanged or tableExportFinishedSuccessfully. Returns the new webhook with its id.</td></tr><tr><td>Delete Robot Monitor</td><td><code>deleteRobotMonitor</code></td><td>Deletes a monitor from a robot and returns the deleted monitor.</td></tr><tr><td>Delete Robot Webhook</td><td><code>deleteRobotWebhook</code></td><td>Deletes a webhook from a robot so Browse AI stops posting that event to its URL.</td></tr><tr><td>Get Bulk Run</td><td><code>getBulkRun</code></td><td>Retrieves a bulk run with its task counts and a paginated list of the tasks run within it, including each task's captured data.</td></tr><tr><td>Get Robot</td><td><code>getRobot</code></td><td>Retrieves a single robot by id with its name, creation timestamp and input parameter definitions (labels, types, defaults, options).</td></tr><tr><td>Get Robot Monitor</td><td><code>getRobotMonitor</code></td><td>Retrieves one monitor of a robot with its schedule, notification settings, input parameters and status.</td></tr><tr><td>Get Robot Task</td><td><code>getRobotTask</code></td><td>Retrieves a task's details and captured data (texts, lists, screenshots), its status, timing, input parameters and, when available, a temporary URL for the captured data and the run video.</td></tr><tr><td>Get System Status</td><td><code>getSystemStatus</code></td><td>Returns the real-time operational status of the Browse AI infrastructure, including whether the tasks queue is running normally or under maintenance.</td></tr></tbody></table>

<details>

<summary>View 8 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>List Bulk Runs</td><td><code>listBulkRuns</code></td><td>Lists a robot's bulk runs with their status and task counts, paginated.</td></tr><tr><td>List Robot Monitors</td><td><code>listRobotMonitors</code></td><td>Lists the monitors configured on a robot with their schedules, notification settings, input parameters and active or paused status.</td></tr><tr><td>List Robot Tasks</td><td><code>listRobotTasks</code></td><td>Lists a robot's tasks with pagination and filters by status, bulk run, creation date range and retried tasks, sorted by the given fields. Each task carries its status, input parameters and captured texts, lists and screenshots.</td></tr><tr><td>List Robot Webhooks</td><td><code>listRobotWebhooks</code></td><td>Lists the webhooks registered on a robot with their target URL and subscribed event type.</td></tr><tr><td>List Robots</td><td><code>listRobots</code></td><td>Lists all robots under your team with their ids, names, creation timestamps and input parameter definitions. Robots are created in the Browse AI dashboard; use the returned ids with the task, monitor, bulk run and webhook actions.</td></tr><tr><td>Run Robot</td><td><code>runRobot</code></td><td>Runs a robot on demand with optional input parameter overrides and optional video recording, creating a task. The response contains the new task; receive the captured data through the robot's webhooks or poll Get Robot Task until the task finishes. Consumes Browse AI credits</td></tr><tr><td>Update Robot Cookies</td><td><code>updateRobotCookies</code></td><td>Replaces the cookies a robot uses when it runs, for example to keep it logged in to a site. The request body is an array of cookie objects (name and value required; domain, path, expirationDate, hostOnly, httpOnly and secure optional). Returns the updated cookie list.</td></tr><tr><td>Update Robot Monitor</td><td><code>updateRobotMonitor</code></td><td>Updates a robot monitor: name, input parameters, notification settings, schedule, or status (paused to stop it, active to resume). Only the fields you pass are changed.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Table Export Finished Successfully</td><td><code>tableExportFinishedSuccessfully</code></td><td>A table export of the robot's captured data finished (Beta). Registered on the robot given as robotId.</td></tr><tr><td>Task Captured Data Changed</td><td><code>taskCapturedDataChanged</code></td><td>A run of the robot captured data that differs from the previous run (used with monitors). Registered on the robot given as robotId.</td></tr><tr><td>Task Finished</td><td><code>taskFinished</code></td><td>A run (task) of the robot finished, successfully or with an error. Browse AI registers this webhook on the robot whose id you provide as robotId.</td></tr><tr><td>Task Finished Successfully</td><td><code>taskFinishedSuccessfully</code></td><td>A run (task) of the robot finished successfully. Registered on the robot given as robotId.</td></tr><tr><td>Task Finished With Error</td><td><code>taskFinishedWithError</code></td><td>A run (task) of the robot failed. Registered on the robot given as robotId.</td></tr></tbody></table>
