---
description: "Queue (app.usequeue.com) is a client-portal and project-management platform for agencies and productized-service businesses."
hidden: true
---

# Queue

<img src="../../.gitbook/assets/connectors/lg/queue.png" alt="Queue logo">

Queue (app.usequeue.com) is a client-portal and project-management platform for agencies and productized-service businesses. This connector covers the Queue REST API v1: projects, taskboard columns and tasks, task comments and replies, clients, invoices, timesheets, task credits, services, service checkouts (subscriptions) with pause/unpause/cancel, and files with their comments and replies.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [usequeue.com](https://usequeue.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `queue` |

## Use it

Add Queue from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.queue.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Service Checkout | `cancelServiceCheckout` | Cancel a client's recurring service subscription. This ends the paying subscription and cannot be undone from the API. Returns {success: true}. |
| Create Client | `createClient` | Add a client-portal user to a project. WARNING: Queue may email the address you supply an invitation to the client portal, so only pass real addresses of people who expect it. Responds 201 with the created client. |
| Create Column | `createColumn` | Add a taskboard column to a project. Returns the created column including its id. Responds 201. Note: Queue accepts but silently ignores the finished and start_timer flags on this endpoint - they always come back null and must be set in the Queue web app. The column's WIP limit is read-only over the API. |
| Create File Comment | `createFileComment` | Leave a review comment on a file or screen recording. WARNING: the Queue API has no endpoint to delete a file comment, so anything created here is permanent and can only be removed in the Queue web app. A non-private comment is visible to the project's clients. |
| Create Invoice | `createInvoice` | Raise a new invoice on a project. The invoice is created as a draft with amount 0 and no line items; line items are added in the Queue web app. Responds 201 with the created invoice. |
| Create Project | `createProject` | Create a new project (client workspace) in Queue. Queue automatically seeds the new project with three default taskboard columns. Returns the created project including its id. Responds 201. WARNING: do NOT pass private=true. A project created with private=true is returned by this call but is then invisible to the API key forever - it is omitted from List Projects and Get Project, Update Project and Delete Project all answer 422 'Project not found', so the project can only be reached in the Queue web app. Create the project without private and set it private in the web app instead. |
| Create Task | `createTask` | Create a task inside a taskboard column. Returns the created task including its id, its author and its column. Responds 201. Note: Queue accepts but silently ignores position and cover_url on this endpoint - both always come back null. |
| Create Task Comment | `createTaskComment` | Post a comment on a task. A non-private comment is visible to the project's clients in the Queue client portal and may notify them, so set private to true for internal notes. Responds 201 with the created comment. |
| Create Task Comment By Task ID | `createTaskCommentByTaskId` | Post a task comment through the top-level endpoint, passing the task id in the body instead of the URL. Undocumented but live (POST /api/v1/task_comments). Functionally the same as Create Task Comment. Responds 201. |
| Create Task Credit | `createTaskCredit` | Record a task credit against a task. Despite the documentation marking it optional, the API rejects the request with 'service_id is required' unless a valid service_id is supplied, so the workspace must already have at least one service (services are created in the Queue web app). Responds 201. |

<details>

<summary>See 50 more actions</summary>

* **Delete Client** `deleteClient`: Remove a client-portal user from the workspace, revoking their portal access. This cannot be undone. Returns {success: true}.
* **Delete Column** `deleteColumn`: Delete a taskboard column and the tasks it holds. This cannot be undone. Returns {success: true}.
* **Delete Invoice** `deleteInvoice`: Delete an invoice. This cannot be undone. Returns {success: true}.
* **Delete Project** `deleteProject`: Permanently delete a Queue project and everything inside it - columns, tasks, comments, invoices, clients and files. This cannot be undone. Returns {success: true}.
* **Delete Service Checkout** `deleteServiceCheckout`: Delete a service checkout record. This removes a paying client's subscription record from Queue and cannot be undone. Returns {success: true}.
* **Delete Task** `deleteTask`: Delete a task and its comments. This cannot be undone. Returns {success: true}.
* **Delete Task Comment** `deleteTaskComment`: Delete a task comment. This cannot be undone. Returns {success: true}.
* **Delete Task Credit** `deleteTaskCredit`: Delete a recorded task credit. This cannot be undone. Returns {success: true}.
* **Delete Timesheet** `deleteTimesheet`: Delete a tracked time entry. This cannot be undone. Returns {success: true}.
* **Get Client** `getClient`: Retrieve a single client-portal user by id.
* **Get Column** `getColumn`: Retrieve a single taskboard column by its id.
* **Get File** `getFile`: Retrieve a single file by its token, with its owner, project, folder and comment count. Pass the file's 'token' value, not its numeric 'id'. SECURITY: the returned file_link is a publicly reachable, unauthenticated URL.
* **Get File Comment** `getFileComment`: Retrieve a single file review comment by its numeric id, with its threaded replies.
* **Get Project** `getProject`: Retrieve a single Queue project by its id. Returns the project's title, avatar, private and archive flags and timestamps.
* **Get Service** `getService`: Retrieve a single productized service by id, with its pricing tiers and checkout link.
* **Get Service Checkout** `getServiceCheckout`: Retrieve a single service checkout by id, with its Stripe or PayPal subscription data, pause and cancel state.
* **Get Task** `getTask`: Retrieve a single task by its id, with its description, priority, deadline, status, custom fields, author and the column it sits in.
* **Get Task Comment** `getTaskComment`: Retrieve a single task comment by its id, with its author.
* **Get Task Credit** `getTaskCredit`: Retrieve a single task credit by id, with its task, user, service and credit amount.
* **Get Timesheet** `getTimesheet`: Retrieve a single tracked time entry by id, with its task, project, user, duration and billing fields.
* **List All Files** `listAllFiles`: List every file and screen recording in the Queue workspace across all projects. Undocumented but live endpoint (GET /api/v1/files). SECURITY: file_link is a publicly reachable, unauthenticated URL to the file content.
* **List All Invoices** `listAllInvoices`: List every invoice in the Queue workspace across all projects. Undocumented but live endpoint (GET /api/v1/invoices); returns a top-level array.
* **List All Service Checkouts** `listAllServiceCheckouts`: List every service checkout in the Queue workspace across all projects. Undocumented but live endpoint (GET /api/v1/service_checkouts).
* **List All Task Comments** `listAllTaskComments`: List task comments across the whole Queue workspace. Undocumented but live endpoint (GET /api/v1/task_comments); returns {task_comments: [...]}. Use List Task Comments for one task.
* **List All Tasks** `listAllTasks`: List tasks across the whole Queue workspace, paginated. Undocumented but live endpoint (GET /api/v1/tasks); returns {tasks: [...], meta: {...}}. It has no project filter - a project_id query parameter is silently ignored and every project's tasks are returned - so use List Column Tasks when you need one project or board column.
* **List All Timesheets** `listAllTimesheets`: List tracked time entries across the whole Queue workspace, paginated. Undocumented but live endpoint (GET /api/v1/timesheets); the response carries a meta block with page, per_page, total and total_pages.
* **List Column Tasks** `listColumnTasks`: List the tasks sitting in one taskboard column. The project_id query parameter is required by the API.
* **List File Comment Replies** `listFileCommentReplies`: List the threaded replies posted under one file review comment.
* **List File Comments** `listFileComments`: List the review comments left on a file or screen recording, each with its threaded replies. Pass the file's string token.
* **List Project Clients** `listProjectClients`: List the client-portal users attached to a project, with their username, email and role.
* **List Project Columns** `listProjectColumns`: List the taskboard columns of a project, in board order. Returns an array of columns with id, title, position, stage, finished, start_timer and limit.
* **List Project Files** `listProjectFiles`: List the files and screen recordings uploaded to a project. SECURITY: each item carries file_link, a publicly reachable URL that serves the file with no authentication - treat it as a secret. Files are uploaded through the Queue web app; there is no API endpoint to upload one.
* **List Project Invoices** `listProjectInvoices`: List the invoices raised on one project, with their line items, amount, tax and payment terms. Returns an array.
* **List Project Service Checkouts** `listProjectServiceCheckouts`: List the service checkouts (client subscriptions and one-off purchases) on a project, with their pause, cancel and billing state.
* **List Project Task Credits** `listProjectTaskCredits`: List the task credits consumed or granted on a project, with the task, user, service and credit amount.
* **List Project Timesheets** `listProjectTimesheets`: List the tracked time entries on a project, with their task, user, duration, billable rate and formatted duration.
* **List Projects** `listProjects`: List every project in the Queue workspace. Returns an array of projects with their id, title, avatar, private and archive flags and timestamps.
* **List Services** `listServices`: List the productized services offered in the Queue workspace, with their pricing tiers, checkout link and subscription rules. Services are created in the Queue web app; there is no API endpoint to create one.
* **List Task Comments** `listTaskComments`: List the comments on one task, newest first, each with its author. Returns an array.
* **Pause Service Checkout** `pauseServiceCheckout`: Pause a client's recurring service subscription. Billing stops until it is unpaused. Returns {success: true}.
* **Reply To File Comment** `replyToFileComment`: Post a threaded reply under a file review comment. WARNING: the Queue API has no endpoint to delete a file comment reply, so anything created here is permanent and can only be removed in the Queue web app.
* **Reply To Task Comment** `replyToTaskComment`: Post a threaded reply under an existing task comment. A non-private reply is visible to the project's clients, so set private to true for internal notes. Responds 201 with the created reply.
* **Unpause Service Checkout** `unpauseServiceCheckout`: Resume a paused client service subscription so that billing restarts. Returns {success: true}.
* **Update Column** `updateColumn`: Update a taskboard column - rename it, move it, or change its workflow stage. Send only the fields you want to change. Note: Queue accepts but silently ignores the finished and start_timer flags on this endpoint - they always come back null and must be set in the Queue web app. The column's WIP limit is read-only over the API.
* **Update File Comment** `updateFileComment`: Edit a file review comment or flip its private flag. Returns the updated comment.
* **Update Project** `updateProject`: Update an existing Queue project. Send only the fields you want to change. Returns the updated project.
* **Update Task** `updateTask`: Update a task - retitle it, edit the description, change priority, deadline or custom sections. Send only the fields you want to change. Returns the updated task with its author and column. Note: Queue accepts but silently ignores position and cover_url on this endpoint.
* **Update Task Comment** `updateTaskComment`: Edit an existing task comment or flip its private flag. Returns the updated comment.
* **Update Task Credit** `updateTaskCredit`: Update a recorded task credit - change the credit amount, the task or user it is attributed to, or its comment.
* **Update Timesheet** `updateTimesheet`: Update a tracked time entry - reassign it to another task, change the logged duration or edit its notes. Returns the updated timesheet.

</details>
