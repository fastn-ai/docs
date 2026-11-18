---
description: "Onfleet is a last-mile delivery management platform."
hidden: true
---

# Onfleet

Onfleet is a last-mile delivery management platform. This connector covers the Onfleet v2 REST API: organizations and delegatees, administrators, workers and their schedules, teams and auto-dispatch, hubs, destinations, recipients, tasks (create, batch, clone, complete, auto-assign and metadata search), containers, task custom-field groups, route plans, route optimization and webhooks.

| | |
| --- | --- |
| **Category** | [E-commerce](README.md) |
| **Website** | [onfleet.com](https://onfleet.com) |
| **Authentication** | Basic auth |
| **Actions** | 86 |
| **Events** | 29 |
| **Slug** | `onfleet` |

## Use it

Add Onfleet from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.onfleet.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Abort Route Optimization | `abortRouteOptimization` | Cancels an in-progress route optimization run so its results are discarded. Route optimization requires the Onfleet Scale plan or higher. |
| Apply Route Optimization Results | `applyRouteOptimization` | Commits the routes produced by a completed route optimization run, assigning the tasks to the selected drivers. Route optimization requires the Onfleet Scale plan or higher. |
| Auto Assign Tasks | `autoAssignTasks` | Assigns a list of existing tasks in bulk to available on-duty drivers, optionally restricted to given teams. Returns how many tasks were assigned and the resulting task-to-worker mapping. |
| Auto Dispatch Team | `autoDispatchTeam` | Dispatches the tasks currently held by a team to its on-duty drivers, interleaving them into existing routes. Returns a dispatch id identifying the resulting route optimization. This endpoint requires the Onfleet Scale plan or higher. |
| Cancel Orders | `cancelOrders` | Cancels one or more delivery orders before they start or complete. Orders that have already been completed cannot be cancelled. |
| Clone Order | `cloneOrder` | Creates a copy of an existing delivery order, optionally overriding the pickup or drop-off details on the copy. |
| Clone Task | `cloneTask` | Creates a copy of an existing task, optionally carrying over its metadata, barcodes and dependencies and overriding selected fields. The new task records the original in its sourceTaskId. |
| Complete Task | `completeTask` | Force-completes an active task on the driver's behalf, recording whether the delivery succeeded and any completion notes. Completed tasks can no longer be updated. |
| Create Administrator | `createAdministrator` | Creates a new administrator in the organization. Onfleet emails the address supplied so the administrator can confirm and configure their account. |
| Create Destination | `createDestination` | Creates a destination from a parsed or unparsed street address. Onfleet geocodes the address unless explicit coordinates are supplied. Destinations cannot be deleted through the Onfleet API once created. |
| Create Hub | `createHub` | Creates a hub at the supplied address. Hubs act as the start and end point of team routes and cannot be deleted through the Onfleet API once created. |
| Create Order | `createOrder` | Creates a delivery order as a linked pickup and drop-off task pair and sends it to the courier organization for assignment. Requires an Onfleet Connections relationship between the client and the courier. |
| Create Recipient | `createRecipient` | Creates a recipient who can be attached to tasks and receive delivery notifications. Recipients cannot be deleted through the Onfleet API once created. |
| Create Route Plan | `createRoutePlan` | Creates a route plan grouping tasks into a single scheduled route, optionally assigned to a driver or team and anchored to a start and end hub. |
| Create Task | `createTask` | Creates a delivery or pickup task. The destination and recipients may be given as existing ids or as inline objects, which Onfleet then creates. Optional automatic assignment places the task directly on an on-duty driver's route. |
| Create Task Template | `createTaskTemplate` | Creates a task custom-field template grouping configured custom fields for pickup tasks, drop-off tasks or both. Custom fields themselves must already be configured on the Onfleet dashboard. This endpoint requires a plan that includes custom fields. |
| Create Tasks In Batch | `createTasksInBatch` | Creates up to 100 tasks in a single synchronous request. Returns the tasks that were created together with any per-task errors. |
| Create Tasks In Batch Asynchronously | `createTasksInBatchAsync` | Queues up to 5,000 tasks for background creation and returns a job id immediately. Poll Get Batch Job Status with that id, or subscribe to the taskBatchCreateJobCompleted webhook, to collect the result. |
| Create Team | `createTeam` | Creates a new team in the organization and optionally populates it with workers, managing administrators and a home hub. |
| Create Webhook | `createWebhook` | Registers a webhook so Onfleet posts a chosen event to your HTTPS endpoint. Onfleet validates the URL before saving by issuing a GET with a check query parameter that your server must echo back with HTTP 200. |
| Create Worker | `createWorker` | Creates a new driver (worker) in the organization and assigns them to one or more teams. Onfleet texts the worker a temporary password and links to the driver mobile apps. |
| Delete Administrator | `deleteAdministrator` | Permanently removes an administrator from the organization. The administrator immediately loses access to the Onfleet dashboard and API. |
| Delete Route Plan | `deleteRoutePlan` | Deletes a route plan. The tasks it contained are not deleted; they return to their previous container. |
| Delete Task | `deleteTask` | Permanently removes a task. Completed tasks cannot be deleted and remain in the organization's history. |
| Delete Task Template | `deleteTaskTemplate` | Deletes a task custom-field template. Tasks already created from the template keep their stored custom field values. |
| Delete Team | `deleteTeam` | Permanently removes a team from the organization. Workers on the team are not deleted; they simply lose their membership. |
| Delete Webhook | `deleteWebhook` | Removes a registered webhook so Onfleet stops posting its events to the target URL. |
| Delete Worker | `deleteWorker` | Permanently removes a driver (worker) from the organization. Any tasks still assigned to the worker are returned to the organization's unassigned container. |
| Find Administrators By Metadata | `findAdministratorsByMetadata` | Returns every administrator whose custom metadata contains an entry matching the supplied name, type and value. |
| Find Destinations By Metadata | `findDestinationsByMetadata` | Returns every destination whose custom metadata contains an entry matching the supplied name, type and value. |
| Find Recipient By Name | `findRecipientByName` | Looks up a recipient by their exact name. The comparison is case-insensitive and returns the single matching recipient. |
| Find Recipient By Phone | `findRecipientByPhone` | Looks up a recipient by their phone number and returns the single matching recipient. |
| Find Recipients By Metadata | `findRecipientsByMetadata` | Returns every recipient whose custom metadata contains an entry matching the supplied name, type and value. |
| Find Tasks By Metadata | `findTasksByMetadata` | Returns every task whose custom metadata contains an entry matching the supplied name, type and value. |
| Find Teams By Metadata | `findTeamsByMetadata` | Returns every team whose custom metadata contains an entry matching the supplied name, type and value. |
| Find Workers By Metadata | `findWorkersByMetadata` | Returns every driver (worker) whose custom metadata contains an entry matching the supplied name, type and value. |
| Generate Delivery Manifest | `generateDeliveryManifest` | Generates a delivery manifest for a driver's route from a given hub, listing their assigned stops in sequence with estimated arrival times. Turn-by-turn directions and total distance additionally require a Google Maps Directions key, which this action does not send. |
| Get Batch Job Status | `getBatchJobStatus` | Returns the progress and result of an asynchronous task batch creation job, including the tasks created so far and any per-task errors. |
| Get Delegatee Details | `getDelegatee` | Retrieves the publicly shared details of a connected delegatee organization by its id. The delegatee id must appear in the delegatees array returned by Get Organization Details. |
| Get Destination | `getDestination` | Retrieves a single destination by id, including its normalised address, geocoded coordinates, driver notes and any geocoding warnings. |
| Get Order | `getOrder` | Retrieves a single delivery order by its short id, including the pickup and drop-off tasks, the client and courier organizations and the current state. |
| Get Organization Container | `getOrganizationContainer` | Returns the organization's container, which holds every task that is not yet assigned to a team or a driver, in its current order. |
| Get Organization Details | `getOrganization` | Retrieves the details of the Onfleet organization that owns the API key, including its name, contact email, time zone, country and the ids of any connected delegatee organizations. |
| Get Recipient | `getRecipient` | Retrieves a single recipient by id, including their contact details, driver notes and notification preference. |
| Get Route Optimization Status | `getRouteOptimizationStatus` | Returns the current status and planned routes of a route optimization run. Route optimization requires the Onfleet Scale plan or higher. |
| Get Route Plan | `getRoutePlan` | Retrieves a single route plan by id, including its tasks, assignment, planned window, start and end anchors and progress status. |
| Get Task | `getTask` | Retrieves a single task by id, including its destination, recipients, assigned driver, completion details and tracking URL. |
| Get Task By Short ID | `getTaskByShortId` | Retrieves a single task using its eight-character short id, the identifier shown on tracking pages and in driver notifications. |
| Get Team | `getTeam` | Retrieves a single team by id, including its member workers, managing administrators and assigned hub. |
| Get Team Container | `getTeamContainer` | Returns a team's container, which holds the tasks queued for that team but not yet assigned to a driver, in its current order. |
| Get Team Driver Time Estimate | `getTeamDeliveryEstimate` | Estimates travel time, travel distance, arrival time and completion time for a delivery that has not yet been created, by selecting the best on-duty worker on the given team. The team must have a hub and at least one worker on duty. |
| Get Worker | `getWorker` | Retrieves a single driver (worker) by id, including team membership, duty state, vehicle, assigned tasks and, optionally, delivery analytics. |
| Get Worker Container | `getWorkerContainer` | Returns a driver's container, which is their route: the ordered list of tasks assigned to them plus the task currently in progress. |
| Get Worker Schedule | `getWorkerSchedule` | Retrieves every schedule entry recorded for a driver (worker), each giving the date, time zone and the shifts worked on that date. |
| Get Workers By Location | `getWorkersByLocation` | Returns all on-duty drivers (workers) whose last known position falls within a radius of the supplied coordinates. |
| Initialize Route Optimization | `initializeRouteOptimization` | Starts a scheduled route optimization over a set of unassigned tasks and the drivers on the given teams, returning an optimization id used to poll, apply or abort the run. Route optimization requires the Onfleet Scale plan or higher. |
| List Administrators | `listAdministrators` | Returns every administrator in the organization, covering both super administrators and standard dispatchers, with their contact details, team access and active state. |
| List Hubs | `listHubs` | Returns every hub defined in the organization, with its address, geocoded location and the teams that use it. |
| List Task Templates | `listTaskTemplates` | Returns every task custom-field template in the organization, including the Onfleet default pickup and drop-off templates. |
| List Tasks | `listTasks` | Returns a paginated collection of the organization's tasks within a time range, optionally narrowed by state, worker, container or dependency. Up to 64 tasks are returned per page; continue with the returned Last ID while one is present. |
| List Team Tasks | `listTeamTasks` | Returns a paginated collection of the unassigned tasks currently held by a team, sorted by creation time. Tasks already assigned to a worker are not included. |
| List Teams | `listTeams` | Returns every team in the organization together with its member workers, managers and assigned hub. |
| List Webhooks | `listWebhooks` | Returns every webhook registered on the organization, with its target URL, trigger and any threshold. |
| List Worker Assigned Tasks | `listWorkerTasks` | Returns a paginated collection of the tasks currently assigned to a driver (worker), sorted by creation time. Historical tasks that are no longer assigned are not included. |
| List Workers | `listWorkers` | Returns the drivers (workers) in the organization, optionally restricted to given teams, states or phone numbers, and optionally expanded with their current tasks and analytics. |
| Quote Order | `quoteOrder` | Returns price quotes for an upcoming delivery order across every configured delivery service compatible with the pickup, drop-off, timing and weight supplied. It applies only to clients that have services configured in Onfleet. |
| Reject Order | `rejectOrder` | Rejects an order sent by a client, recording the reason. This action is for courier organizations and requires a courier API key. |
| Search Eligible Custom Fields | `searchEligibleCustomFields` | Returns the custom fields that may be included in a task template matching the given conditions, which is how to discover the valid field keys for a pickup-only or drop-off-only template. |
| Search Route Plans | `searchRoutePlans` | Returns route plans matching the supplied filters on assigned driver, planned start time, creation time and whether the plan holds any tasks. |
| Set Route Plan Tasks | `setRoutePlanTasks` | Replaces the ordered list of tasks on a route plan. Include the tasks already on the plan alongside any new ones, because tasks left out are removed from the plan. |
| Set Worker Schedule | `setWorkerSchedule` | Replaces a driver's (worker's) schedule with the supplied entries. Entries dated before the start of the current week are ignored by Onfleet. |
| Start Route Optimization | `startRouteOptimization` | Begins processing an initialized route optimization run. Route optimization requires the Onfleet Scale plan or higher. |
| Test API Key | `testApiKey` | Verifies that the configured Onfleet API key is valid and correctly formatted. Returns a greeting message naming the authenticated organization and the originating IP address. |
| Update Administrator | `updateAdministrator` | Updates an existing administrator's name, email, phone number or read-only permission. The administrator type cannot be changed after creation; delete and recreate the administrator instead. |
| Update Hub | `updateHub` | Updates an existing hub's name, address, explicit location or the teams that use it. Only the fields supplied are modified. |
| Update Order | `updateOrder` | Updates a delivery order's pickup or drop-off details, price or currency before the courier completes it. |
| Update Organization Container Tasks | `updateOrganizationContainerTasks` | Moves tasks back into the organization's unassigned container at a given position. Put the insertion index as the first element followed by the task ids, using -1 to append to the end. |
| Update Recipient | `updateRecipient` | Updates an existing recipient's name, phone number, notes, notification preference or metadata. Only the fields supplied are modified. |
| Update Route Plan | `updateRoutePlan` | Updates a route plan's name, colour, vehicle, assignment, planned window, time zone or start and end anchors. Only the fields supplied are modified. |
| Update Task | `updateTask` | Updates an existing task's completion window, notes, quantities, requirements, custom fields or metadata. A task that has already been completed cannot be updated. |
| Update Task Template | `updateTaskTemplate` | Updates a task custom-field template's name, applicable task types or included custom fields. |
| Update Team | `updateTeam` | Updates a team's name, worker roster, managing administrators, home hub or self-assignment setting. Supplying workers or managers replaces the existing list. |
| Update Team Container Tasks | `updateTeamContainerTasks` | Moves tasks into a team's container at a given position. Put the insertion index as the first element followed by the task ids, using -1 to append to the end of the queue. |
| Update Webhook | `updateWebhook` | Replaces a registered webhook's configuration. Onfleet treats this as a full replacement, so send every field you want to keep: omitting Name clears it, and Trigger, URL and Scoped API Key ID must always be present. |
| Update Worker | `updateWorker` | Updates an existing driver (worker), changing their name, team membership, vehicle, capacity, display name or metadata. Only the fields supplied are modified. |
| Update Worker Container Tasks | `updateWorkerContainerTasks` | Sets the tasks on a driver's route. Provide the complete ordered list of task ids to replace the route, or put an insertion index as the first element followed by the task ids to insert at that position. Use -1 as the index to append. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Auto Dispatch Job Completed | `autoDispatchJobCompleted` | Fires when a team auto-dispatch job finishes (trigger 18). Payload schema modelled on the captured taskCreated delivery. |
| Predicted Task Delay | `predictedTaskDelay` | Fires when Onfleet predicts a task will be delayed (trigger 30). Payload schema modelled on the captured taskCreated delivery. |
| Route Optimization Job Completed | `routeOptimizationJobCompleted` | Fires when a route optimization job finishes (trigger 20). Payload schema modelled on the captured taskCreated delivery. |
| Route Plan Assigned | `routePlanAssigned` | Fires when a route plan is assigned to a driver (trigger 28). Payload schema modelled on the captured taskCreated delivery. |
| Route Plan Completed | `routePlanCompleted` | Fires when a route plan finishes (trigger 24). Payload schema modelled on the captured taskCreated delivery. |
| Route Plan Created | `routePlanCreated` | Fires when a route plan is created (trigger 22). Payload schema modelled on the captured taskCreated delivery. |
| Route Plan Delayed | `routePlanDelayed` | Fires when a route plan is predicted to run late (trigger 29). Payload schema modelled on the captured taskCreated delivery. |
| Route Plan Started | `routePlanStarted` | Fires when a driver starts a route plan (trigger 23). Payload schema modelled on the captured taskCreated delivery. |
| Route Plan Unassigned | `routePlanUnassigned` | Fires when a route plan is taken away from a driver (trigger 27). Payload schema modelled on the captured taskCreated delivery. |
| Route Plan Updated | `routePlanUpdated` | Fires when a route plan changes (trigger 26). Payload schema modelled on the captured taskCreated delivery. |
| SMS Recipient Opted Out | `SMSRecipientOptOut` | Fires when a recipient opts out of Onfleet delivery texts (trigger 17). Payload schema modelled on the captured taskCreated delivery. |
| SMS Recipient Response Missed | `smsRecipientResponseMissed` | Fires when a recipient replies to a delivery SMS and no one answers (trigger 14). Payload schema modelled on the captured taskCreated delivery. |
| Task Arrival | `taskArrival` | Fires when the driver comes within the distance threshold in metres set on the webhook (trigger 2). Set the Threshold input when subscribing. Payload schema modelled on the captured taskCreated delivery. |
| Task Assigned | `taskAssigned` | Fires when a task is assigned to a driver (trigger 9). Payload schema modelled on the captured taskCreated delivery. |
| Task Batch Create Job Completed | `taskBatchCreateJobCompleted` | Fires when an asynchronous task batch creation job finishes (trigger 19). Payload schema modelled on the captured taskCreated delivery. |
| Task Cloned | `taskCloned` | Fires when a task is cloned (trigger 13). Payload schema modelled on the captured taskCreated delivery. |
| Task Completed | `taskCompleted` | Fires when a task is completed, successfully or not (trigger 3). Payload schema modelled on the captured taskCreated delivery; data.task.completionDetails carries the outcome. |
| Task Created | `taskCreated` | Fires when a task is created in Onfleet (trigger 6). The payload carries the full task object. |
| Task Delayed | `taskDelayed` | Fires when a task is predicted to miss its completion window (trigger 12). Payload schema modelled on the captured taskCreated delivery. |
| Task Deleted | `taskDeleted` | Fires when a task is deleted (trigger 8). Payload schema modelled on the captured taskCreated delivery. |
| Task ETA Threshold Reached | `taskEta` | Fires when the driver's ETA to a task falls to or below the threshold in seconds set on the webhook (trigger 1). Set the Threshold input when subscribing. Payload schema modelled on the captured taskCreated delivery. |
| Task Failed | `taskFailed` | Fires when a task is completed unsuccessfully (trigger 4). Payload schema modelled on the captured taskCreated delivery. |
| Task Started | `taskStarted` | Fires when a driver starts a task (trigger 0). Payload schema modelled on the captured taskCreated delivery; the envelope is identical and data.task carries the task. |
| Task Unassigned | `taskUnassigned` | Fires when a task is removed from a driver (trigger 10). Payload schema modelled on the captured taskCreated delivery. |
| Task Updated | `taskUpdated` | Fires when a task changes, including completion details, attachment ids and recipient feedback (trigger 7). Payload schema modelled on the captured taskCreated delivery. |
| Worker Created | `workerCreated` | Fires when a driver is added to the organization (trigger 15). Payload schema modelled on the captured taskCreated delivery. |
| Worker Deleted | `workerDeleted` | Fires when a driver is removed from the organization (trigger 16). Payload schema modelled on the captured taskCreated delivery. |
| Worker Duty Changed | `workerDuty` | Fires when a driver goes on or off duty (trigger 5). Payload schema modelled on the captured taskCreated delivery. |
| Worker Updated | `workerUpdated` | Fires when a driver record changes (trigger 25). Payload schema modelled on the captured taskCreated delivery. |
