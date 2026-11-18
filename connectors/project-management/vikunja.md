---
description: "Vikunja is an open-source, self-hostable to-do and task-management app."
hidden: true
---

# Vikunja

<img src="../../.gitbook/assets/connectors/lg/vikunja.png" alt="Vikunja logo">

Vikunja is an open-source, self-hostable to-do and task-management app. This connector covers projects, tasks, labels, teams, task relations/comments/attachments metadata, kanban views/buckets, project sharing (link shares, per-project users/teams), saved filters, project webhooks, and notifications via the REST API, authenticated with a Vikunja Personal Access Token.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [vikunja.io](https://vikunja.io) |
| **Authentication** | Credentials you enter |
| **Slug** | `vikunja` |

## Use it

Add Vikunja from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.vikunja.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Label To Task | `addLabelToTask` | Attaches an existing label to a task. |
| Add Task Assignee | `addTaskAssignee` | Assigns a user to a task. |
| Add Team Member | `addTeamMember` | Adds a user to a team by username. |
| Add Team To Project | `addTeamToProject` | Shares a project with a team, granting its members the given permission level. |
| Add User To Project | `addUserToProject` | Shares a project directly with a user, granting them the given permission level. |
| Bulk Add Task Assignees | `bulkAddTaskAssignees` | Assigns multiple users to a task in a single call. |
| Bulk Update Task Labels | `bulkUpdateTaskLabels` | Replaces every label on a task with the given set of labels in one call. |
| Bulk Update Tasks | `bulkUpdateTasks` | Applies the same field change to multiple tasks at once, e.g. marking several tasks as done. |
| Create Filter | `createFilter` | Creates a saved filter, which appears alongside projects as a pseudo-project showing tasks matching a Vikunja filter query. |
| Create Kanban Bucket | `createKanbanBucket` | Creates a new kanban bucket (column) on a project's kanban view. |

<details>

<summary>See 74 more actions</summary>

* **Create Label** `createLabel`: Creates a new label that can be attached to tasks.
* **Create Project** `createProject`: Creates a new project. Projects organize tasks and can be nested under a parent project.
* **Create Project Share** `createProjectShare`: Creates a public link share for a project, optionally password-protected, so it can be viewed without an account.
* **Create Project View** `createProjectView`: Creates a custom view on a project with a chosen layout (list, gantt, table, or kanban) and optional filter.
* **Create Project Webhook** `createProjectWebhook`: Registers a webhook target on a project so Vikunja calls the given URL when any of the selected events occur.
* **Create Task** `createTask`: Creates a new task in a project.
* **Create Task Comment** `createTaskComment`: Adds a new comment to a task.
* **Create Task Relation** `createTaskRelation`: Creates a relation (e.g. subtask, blocked by, related) between two tasks.
* **Create Team** `createTeam`: Creates a new team that projects and tasks can be shared with.
* **Delete Filter** `deleteFilter`: Permanently deletes a saved filter.
* **Delete Kanban Bucket** `deleteKanbanBucket`: Deletes a kanban bucket from a project's kanban view. Tasks in the bucket are not deleted.
* **Delete Label** `deleteLabel`: Permanently deletes a label, removing it from every task it was attached to.
* **Delete Project** `deleteProject`: Permanently deletes a project and all of its tasks. This cannot be undone.
* **Delete Project Share** `deleteProjectShare`: Removes a public link share from a project, revoking access for anyone using that link.
* **Delete Project View** `deleteProjectView`: Deletes a custom view from a project. Built-in default views cannot be deleted.
* **Delete Project Webhook** `deleteProjectWebhook`: Removes a webhook target from a project.
* **Delete Task** `deleteTask`: Permanently deletes a task. This cannot be undone.
* **Delete Task Attachment** `deleteTaskAttachment`: Removes a file attachment from a task.
* **Delete Task Comment** `deleteTaskComment`: Removes a comment from a task.
* **Delete Task Relation** `deleteTaskRelation`: Removes a relation between two tasks.
* **Delete Team** `deleteTeam`: Permanently deletes a team and revokes any access it had been granted.
* **Duplicate Project** `duplicateProject`: Creates a copy of an existing project, including its tasks, by its numeric id.
* **Duplicate Task** `duplicateTask`: Creates a copy of an existing task in the given project.
* **Get Filter** `getFilter`: Retrieves a single saved filter by its id.
* **Get Instance Info** `getInstanceInfo`: Retrieves public information about the connected Vikunja instance, including its version and enabled features. This endpoint requires no authentication.
* **Get Label** `getLabel`: Retrieves a single label by its numeric id.
* **Get Project** `getProject`: Retrieves a single project by its numeric id, including its description, color, archive state, and configured views.
* **Get Project Share** `getProjectShare`: Retrieves a single link share for a project by its id.
* **Get Project View** `getProjectView`: Retrieves a single project view by its id.
* **Get Task** `getTask`: Retrieves a single task by its numeric id, including its assignees, labels, and related tasks.
* **Get Task Attachment** `getTaskAttachment`: Retrieves metadata for a single file attachment on a task by its id.
* **Get Task By Project Index** `getTaskByProjectIndex`: Retrieves a task using its per-project index number (e.g. the 5 in PRJ-5) instead of its global numeric id.
* **Get Task Comment** `getTaskComment`: Retrieves a single comment on a task by its id.
* **Get Team** `getTeam`: Retrieves a single team by its numeric id, including its members.
* **List Available Webhook Events** `listWebhookEvents`: Lists every event name Vikunja can deliver to a project webhook target.
* **List Kanban Buckets** `listKanbanBuckets`: Lists the kanban buckets (columns) of a project's kanban view.
* **List Labels** `listLabels`: Lists the labels the current user has access to.
* **List Notifications** `listNotifications`: Lists the in-app notifications for the current user.
* **List Project Members** `listProjectMembers`: Lists the users who have access to a project, either directly or via a team.
* **List Project Shares** `listProjectShares`: Lists the public link shares created for a project.
* **List Project Teams** `listProjectTeams`: Lists the teams that have been given access to a project.
* **List Project Users** `listProjectUsers`: Lists the individual users a project has been directly shared with.
* **List Project Views** `listProjectViews`: Lists the views (List, Gantt, Table, Kanban, or custom) configured for a project.
* **List Project Webhooks** `listProjectWebhooks`: Lists the webhook targets configured on a project.
* **List Projects** `listProjects`: Lists all projects the authenticated user has access to.
* **List Task Assignees** `listTaskAssignees`: Lists the users assigned to a task.
* **List Task Attachments** `listTaskAttachments`: Lists the file attachments on a task.
* **List Task Comments** `listTaskComments`: Lists the comments left on a task.
* **List Task Labels** `listTaskLabels`: Lists the labels attached to a task.
* **List Tasks** `listTasks`: Lists tasks across all projects the user has access to. Supports pagination, text search, sorting, and Vikunja filter query syntax.
* **List Tasks In View** `listTasksInView`: Lists the tasks visible in a specific project view, respecting that view's filter and sort configuration.
* **List Teams** `listTeams`: Lists the teams the current user belongs to or manages.
* **Mark All Notifications Read** `markAllNotificationsRead`: Marks every notification for the current user as read.
* **Mark Notification Read** `markNotificationRead`: Marks a single notification as read or unread.
* **Mark Task As Read** `markTaskAsRead`: Marks a task as read, clearing its unread/notification indicator for the current user.
* **Move Task To Bucket** `moveTaskToBucket`: Moves a task into a specific kanban bucket on a project's kanban view.
* **Remove Label From Task** `removeLabelFromTask`: Detaches a label from a task.
* **Remove Task Assignee** `removeTaskAssignee`: Unassigns a user from a task.
* **Remove Team From Project** `removeTeamFromProject`: Revokes a team's access to a project.
* **Remove Team Member** `removeTeamMember`: Removes a user from a team by username.
* **Remove User From Project** `removeUserFromProject`: Revokes a user's direct access to a project.
* **Toggle Team Member Admin** `toggleTeamMemberAdmin`: Toggles whether a team member has admin rights over the team.
* **Update Filter** `updateFilter`: Updates an existing saved filter's title, description, or filter query.
* **Update Kanban Bucket** `updateKanbanBucket`: Updates a kanban bucket's title, position, limit, or its role as the default/done bucket.
* **Update Label** `updateLabel`: Updates an existing label's title, description, or color. Vikunja replaces the whole label on this endpoint rather than merging, so fields left out of the call are reset to empty - always resend every field you want to keep.
* **Update Project** `updateProject`: Updates an existing project's title, description, color, archive state, or parent. Only the fields provided are changed.
* **Update Project Team** `updateProjectTeam`: Updates the permission level a team has on a project.
* **Update Project User** `updateProjectUser`: Updates the permission level a user has on a project.
* **Update Project View** `updateProjectView`: Updates the title, kanban bucket configuration, or filter of a project view.
* **Update Project Webhook** `updateProjectWebhook`: Changes the subscribed events of an existing project webhook target.
* **Update Task** `updateTask`: Updates an existing task's title, description, due date, priority, completion state, or other fields. Vikunja treats this as a broad replace for some fields (e.g. priority resets to 0 if omitted) while preserving others (e.g. title) - always resend every field you want to keep unchanged.
* **Update Task Comment** `updateTaskComment`: Edits the text of an existing task comment.
* **Update Task Position** `updateTaskPosition`: Updates a task's sort position within its current view.
* **Update Team** `updateTeam`: Updates an existing team's name, description, or public visibility.

</details>
