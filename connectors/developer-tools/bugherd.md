---
description: "BugHerd is a visual bug tracker and website feedback tool that pins client feedback directly onto a web page."
hidden: true
---

# BugHerd

BugHerd is a visual bug tracker and website feedback tool that pins client feedback directly onto a web page. This connector covers the BugHerd API v2: the organization, users, members and guests, projects, project membership, kanban columns, tasks with filtering and moving between projects, task comments, task attachments, and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [bugherd.com](https://bugherd.com) |
| **Authentication** | Basic auth |
| **Actions** | 43 |
| **Events** | 5 |
| **Slug** | `bugherd` |

## Use it

Add BugHerd from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.bugherd.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Guest To Project | `addGuestToProject` | Adds a guest collaborator to a BugHerd project, either by the id of an existing guest or by email address. Supplying a new email address invites that person to the project. |
| Add Member To Project | `addMemberToProject` | Grants an existing organization team member access to a BugHerd project. |
| Create Attachment From URL | `createAttachmentFromUrl` | Attaches a file to a BugHerd task by giving BugHerd a publicly reachable URL to fetch it from. Use this instead of Upload Attachment when the file is already hosted somewhere. |
| Create Column | `createColumn` | Adds a custom kanban column to a BugHerd project's taskboard. |
| Create Project | `createProject` | Creates a new BugHerd project for a website. The response includes the project API key needed by the BugHerd sidebar snippet. |
| Create Task | `createTask` | Creates a task in a BugHerd project. The first line of the description becomes the task title on the board. To assign the task, the target user must already be a member of the project - add them with Add Member To Project first, otherwise the assignment fields are accepted and silently ignored. |
| Create Task Comment | `createTaskComment` | Posts a comment on a BugHerd task. Private comments are visible to team members but hidden from guests. |
| Create Webhook | `createWebhook` | Registers a webhook so BugHerd posts to a target URL whenever the chosen event happens. Leave Project ID empty to receive the event for every project in the organization. |
| Delete Column | `deleteColumn` | Removes a custom kanban column from a BugHerd project's taskboard. |
| Delete Project | `deleteProject` | Permanently deletes a BugHerd project together with all of its tasks, comments and attachments. This cannot be undone. |
| Delete Task | `deleteTask` | Deletes a task from a BugHerd project, along with its comments and attachments. |
| Delete Task Attachment | `deleteTaskAttachment` | Removes one attachment from a BugHerd task. |
| Delete Task Comment | `deleteTaskComment` | Deletes one comment from a BugHerd task. The comment id goes in the URL path; the published API reference shows it as a body field, which the API does not accept. |
| Delete Webhook | `deleteWebhook` | Removes a webhook registration so BugHerd stops posting that event to its target URL. |
| List Active Projects | `listActiveProjects` | Returns only the active projects in the BugHerd organization. |
| List Archived Tasks | `listArchivedTasks` | Returns the archived tasks of a BugHerd project, which are tasks removed from the board but not deleted. |
| List Columns | `listColumns` | Returns the kanban columns of a BugHerd project in board order, with the number of tasks in each. |
| List Feedback Tasks | `listFeedbackTasks` | Returns the tasks sitting in a project's Feedback inbox, the queue of new items that have not yet been triaged onto the kanban board. |
| List Guests | `listGuests` | Returns all guest users across the BugHerd organization. Guests are external collaborators invited to specific projects. |
| List Members | `listMembers` | Returns only the team members of the BugHerd organization, excluding guest collaborators. |
| List Project Comments | `listProjectComments` | Returns every comment across all tasks in a BugHerd project. This endpoint is not listed in the published API reference but is served by the API. |
| List Projects | `listProjects` | Returns every project in the BugHerd organization, active and inactive. |
| List Task Attachments | `listTaskAttachments` | Returns the files attached to one BugHerd task, with their download URLs. |
| List Task Comments | `listTaskComments` | Returns the comments on one BugHerd task, in the order they were posted. |
| List Taskboard Tasks | `listTaskboardTasks` | Returns the tasks currently placed on a project's kanban taskboard, excluding the untriaged feedback queue and the archive. |
| List Tasks | `listTasks` | Returns the tasks in a BugHerd project, with optional filtering by column status, priority, tag, assignee, external id and update or creation date. |
| List User Projects | `listUserProjects` | Returns every BugHerd project one user belongs to, optionally limited to active or inactive projects or to projects created after a given date. |
| List User Tasks | `listUserTasks` | Returns the tasks assigned to one BugHerd user, grouped by project, with optional filtering by creation or update date, priority, tag and assignee. Each group carries the project's id and name plus that project's matching tasks. |
| List Users | `listUsers` | Returns all users in the BugHerd organization, both team members and guests. |
| List Webhooks | `listWebhooks` | Returns every webhook registered on the BugHerd organization, with its target URL, event, scope and delivery success and error counts. |
| Move Tasks | `moveTasks` | Moves tasks from one BugHerd project into another. Identify the tasks by their project-scoped local task numbers, not by their global task ids - the API rejects global ids with 'Task ID N not found in project M'. The tasks are renumbered in the destination project. |
| Show Column | `showColumn` | Returns one kanban column of a BugHerd project, with its board position and task count. |
| Show Organization | `showOrganization` | Returns top-level details about the connected BugHerd organization, including its id and name. |
| Show Project | `showProject` | Returns one BugHerd project in full, including its settings, project API key, kanban columns, members and guests. |
| Show Task | `showTask` | Returns one task in a BugHerd project, including its status, priority, tags, assignee and the page it was logged on. |
| Show Task Attachment | `showTaskAttachment` | Returns one attachment on a BugHerd task, including its download URL. |
| Show Task By Global ID | `showTaskGlobal` | Returns one task by its organization-wide task id, without needing to know which project it belongs to. |
| Show Task By Local ID | `showTaskByLocalId` | Returns one task by the project-scoped task number shown in the BugHerd interface, rather than by its global id. |
| Show Task Comment | `showTaskComment` | Returns one comment on a BugHerd task. This endpoint is not listed in the published API reference but is served by the API. |
| Update Column | `updateColumn` | Renames a kanban column on a BugHerd project's taskboard. |
| Update Project | `updateProject` | Updates the settings of an existing BugHerd project. Only the attributes supplied are changed. |
| Update Task | `updateTask` | Updates a task in a BugHerd project: its description, kanban column, priority, assignee, tags, external id or the page it points at. Only the attributes supplied are changed. To assign the task, the target user must already be a member of the project - add them with Add Member To Project first, otherwise the assignment fields are accepted and silently ignored. |
| Update Webhook | `updateWebhook` | Changes the target URL, event or project scope of an existing BugHerd webhook. This endpoint is not listed in the published API reference but is served by the API. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Comment Posted | `comment` | Fires when a comment is posted on a BugHerd task. The payload carries the comment, its author and the full task it belongs to. Set the optional projectId input to restrict the trigger to one project. Payload schema captured from a real delivery. BugHerd does not sign webhook deliveries. |
| Project Created | `project_create` | Fires when a project is created in the BugHerd organization. This event is organization-wide, so leave the projectId input empty. Payload schema captured from a real delivery. BugHerd does not sign webhook deliveries. |
| Task Created | `task_create` | Fires when a task is created in BugHerd. Set the optional projectId input to restrict the trigger to one project; leave it empty to receive the event for every project in the organization. Payload schema captured from a real delivery. BugHerd does not sign webhook deliveries. |
| Task Deleted | `task_destroy` | Fires when a task is deleted from BugHerd. The payload carries the deleted task in the same envelope as Task Created. Set the optional projectId input to restrict the trigger to one project. BugHerd does not sign webhook deliveries. |
| Task Updated | `task_update` | Fires when a task is changed in BugHerd, including moves between kanban columns and priority, tag or assignee changes. Set the optional projectId input to restrict the trigger to one project. Payload schema captured from a real delivery. BugHerd does not sign webhook deliveries. |
