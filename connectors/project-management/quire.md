---
description: "Quire is a collaborative task-management and project-planning tool."
hidden: true
---

# Quire

Quire is a collaborative task-management and project-planning tool. Manage organizations, projects, tasks, sublists, comments, tags, statuses, documents, and notifications.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 92 |
| **Events** | 0 |
| **Slug** | `quire` |

## Use it

Add Quire from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.quire.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Chat Comment | `addChatComment` | Adds a comment (message) to a chatroom. |
| Add Project Field | `addProjectField` | Adds a custom field to a project. (Requires a paid Quire plan.) |
| Add Task Comment | `addTaskComment` | Adds a comment to a task. |
| Add Task Timelog | `addTaskTimelog` | Adds a time-tracking log entry to a task. |
| Approve Task | `approveTask` | Approves a task in an approval workflow. |
| Bulk Approve Tasks | `bulkApproveTasks` | Approves multiple tasks at once within a project. |
| Bulk Create Tasks | `bulkCreateTasks` | Creates multiple tasks at once under a project or parent task. Provide 'tasks' as a JSON array string of task objects. |
| Bulk Move Tasks | `bulkMoveTasks` | Moves multiple tasks at once within a project. Provide 'tasks' as a JSON array string of move instructions. |
| Bulk Remove Tasks | `bulkRemoveTasks` | Deletes multiple tasks at once within a project. Provide 'tasks' as a JSON array string of task OIDs. |
| Bulk Transfer Tasks | `bulkTransferTasks` | Transfers multiple tasks from a source project to a destination project. |
| Bulk Update Tasks | `bulkUpdateTasks` | Updates multiple tasks at once within a project. Provide 'tasks' as a JSON array string; each object must include the task oid or id. |
| Create Chat | `createChat` | Creates a chatroom under an owner object (project or organization). |
| Create Document | `createDocument` | Creates a document under an owner object (project or organization). |
| Create Insight | `createInsight` | Creates an insight (saved report/filter) under an owner object (project or organization). |
| Create Status | `createStatus` | Creates a status (board column) in a project. |
| Create Sublist | `createSublist` | Creates a sublist under an owner object (typically a task). |
| Create Tag | `createTag` | Creates a tag in a project. |
| Create Task | `createTask` | Creates a task under a project (root task) or under a parent task (subtask), identified by object ID (oid). |
| Delete Chat | `deleteChat` | Deletes a chatroom by its object ID (oid). |
| Delete Comment | `deleteComment` | Deletes a comment by its object ID (oid). |
| Delete Document | `deleteDocument` | Deletes a document by its object ID (oid). |
| Delete Insight | `deleteInsight` | Deletes an insight by its object ID (oid). |
| Delete Status | `deleteStatus` | Deletes a status by its numeric value within a project. |
| Delete Storage | `deleteStorage` | Deletes a key-value storage entry by name. |
| Delete Sublist | `deleteSublist` | Deletes a sublist by its object ID (oid). |
| Delete Tag | `deleteTag` | Deletes a tag by its object ID (oid). |
| Delete Task | `deleteTask` | Deletes a task by its object ID (oid). The task can be restored with Undo Remove Task. |
| Export Project as CSV | `exportProjectCsv` | Exports a project's tasks as CSV text. |
| Export Project as JSON | `exportProjectJson` | Exports a project's full task tree as JSON. |
| Get Chat | `getChat` | Retrieves a single chatroom by its object ID (oid). |
| Get Comment | `getComment` | Retrieves a single comment by its object ID (oid). |
| Get Current User | `getCurrentUser` | Retrieves the profile of the currently authenticated Quire user. |
| Get Document | `getDocument` | Retrieves a single document by its object ID (oid). |
| Get Insight | `getInsight` | Retrieves a single insight by its object ID (oid). |
| Get Organization | `getOrganization` | Retrieves a single organization by its object ID (oid). |
| Get Partner | `getPartner` | Retrieves a single partner by its object ID (oid). |
| Get Project | `getProject` | Retrieves a single project by its object ID (oid). |
| Get Rate Limit | `getRateLimit` | Retrieves the current API rate-limit status for an object (e.g. an organization or project oid). |
| Get Status | `getStatus` | Retrieves a single status by its numeric value within a project. |
| Get Storage | `getStorage` | Retrieves a single key-value storage entry by name. |
| Get Sublist | `getSublist` | Retrieves a single sublist by its object ID (oid). |
| Get Tag | `getTag` | Retrieves a single tag by its object ID (oid). |
| Get Task | `getTask` | Retrieves a single task by its object ID (oid). |
| Get User | `getUser` | Retrieves a single user by their object ID (oid). |
| List Chat Comments | `listChatComments` | Lists the comments (messages) in a chatroom. |
| List Chats | `listChats` | Lists the chatrooms belonging to an owner object (project or organization). |
| List Documents | `listDocuments` | Lists the documents belonging to an owner object (project or organization). |
| List Insights | `listInsights` | Lists the insights (saved reports/filters) of an owner object (project or organization). |
| List Organizations | `listOrganizations` | Lists all organizations the authenticated user belongs to. |
| List Partners | `listPartners` | Lists the external partners (guest collaborators) of a project. |
| List Project Users | `listProjectUsers` | Lists all users who are members of the given project. |
| List Projects | `listProjects` | Lists all projects the authenticated user can access across all organizations. |
| List Projects by Organization | `listProjectsByOrganization` | Lists all projects within a specific organization. |
| List Statuses | `listStatuses` | Lists all statuses (board columns) defined in a project. |
| List Storage | `listStorage` | Lists all key-value storage entries saved by this app for the authenticated user. |
| List Storage by Prefix | `listStorageByPrefix` | Lists key-value storage entries whose name starts with the given prefix. |
| List Sublists | `listSublists` | Lists the sublists of an owner object (typically a task). |
| List Tags | `listTags` | Lists all tags defined in a project. |
| List Task Comments | `listTaskComments` | Lists the comments on a task. |
| List Tasks | `listTasks` | Lists the direct child tasks of a project (root tasks) or a task (subtasks), identified by object ID (oid). |
| List Users | `listUsers` | Lists all users the authenticated user shares an organization or project with. |
| Move Project Field | `moveProjectField` | Reorders a project custom field. |
| Move Task | `moveTask` | Moves a task to a new parent and/or position within the same project. |
| Remove Project Field | `removeProjectField` | Removes a custom field from a project. |
| Remove Task Timelog | `removeTaskTimelog` | Removes a time-tracking log entry from a task. |
| Rename Project Field | `renameProjectField` | Renames a project custom field. |
| Revoke Task Approval | `revokeTaskApproval` | Revokes a previously granted approval on a task. |
| Run Insight | `runInsight` | Runs an insight and returns its computed result rows. |
| Search Tasks in Folder | `searchTasksInFolder` | Searches tasks within a folder (smart folder / saved view). |
| Search Tasks in Organization | `searchTasksInOrganization` | Searches tasks across all projects in an organization. |
| Search Tasks in Project | `searchTasksInProject` | Searches tasks within a project. Supports a text query and other filter parameters. |
| Send Notification | `sendNotification` | Sends a notification to one or more Quire users. |
| Set Storage | `setStorage` | Creates or updates a key-value storage entry. Provide 'value' as a JSON string to store. |
| Transfer Task | `transferTask` | Transfers a task (and its subtasks) to a different project. |
| Undo Remove Chat | `undoRemoveChat` | Restores a previously deleted chatroom. |
| Undo Remove Comment | `undoRemoveComment` | Restores a previously deleted comment. |
| Undo Remove Document | `undoRemoveDocument` | Restores a previously deleted document. |
| Undo Remove Insight | `undoRemoveInsight` | Restores a previously deleted insight. |
| Undo Remove Sublist | `undoRemoveSublist` | Restores a previously deleted sublist. |
| Undo Remove Task | `undoRemoveTask` | Restores a task that was previously deleted. |
| Update Chat | `updateChat` | Updates a chatroom. Only the fields you provide are changed. |
| Update Comment | `updateComment` | Updates a comment's body. Only the fields you provide are changed. |
| Update Document | `updateDocument` | Updates a document. Only the fields you provide are changed. |
| Update Insight | `updateInsight` | Updates an insight. Only the fields you provide are changed. |
| Update Organization | `updateOrganization` | Updates an organization's editable fields. Only the fields you provide are changed. |
| Update Project | `updateProject` | Updates a project's editable fields. Only the fields you provide are changed. |
| Update Project Field | `updateProjectField` | Updates a project custom field's configuration. |
| Update Status | `updateStatus` | Updates a status by its numeric value within a project. |
| Update Sublist | `updateSublist` | Updates a sublist. Only the fields you provide are changed. |
| Update Tag | `updateTag` | Updates a tag. Only the fields you provide are changed. |
| Update Task | `updateTask` | Updates a task's editable fields. Only the fields you provide are changed. |
| Update Task Timelog | `updateTaskTimelog` | Updates an existing time-tracking log entry on a task. |
