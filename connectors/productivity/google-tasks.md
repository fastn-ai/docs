---
description: "Google Tasks API - manage Google Workspace task lists and tasks (create, read, update, delete, move, and clear completed tasks)."
hidden: true
---

# Google Tasks

<img src="../../.gitbook/assets/connectors/lg/google-tasks.png" alt="Google Tasks logo">

Google Tasks API - manage Google Workspace task lists and tasks (create, read, update, delete, move, and clear completed tasks).

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [tasks.googleapis.com](https://tasks.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleTasks` |

## Use it

Add Google Tasks from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleTasks.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Clear Completed Tasks | `clearTasks` | Clears all completed tasks from the specified task list (POST /lists/{tasklist}/clear). The affected tasks are marked hidden; they are not deleted. |
| Create Task | `createTask` | Creates a new task on the specified task list (POST /lists/{tasklist}/tasks). Optionally place it as a subtask (parent) or after a sibling (previous). |
| Create Task List | `createTaskList` | Creates a new task list and adds it to the authenticated user's task lists (POST /users/@me/lists). |
| Delete Task | `deleteTask` | Deletes the specified task from the task list (DELETE /lists/{tasklist}/tasks/{task}). |
| Delete Task List | `deleteTaskList` | Deletes the specified task list (DELETE /users/@me/lists/{tasklist}). This also deletes all tasks in it. The default task list cannot be deleted. |
| Get Task | `getTask` | Returns the specified task (GET /lists/{tasklist}/tasks/{task}). |
| Get Task List | `getTaskList` | Returns the specified task list (GET /users/@me/lists/{tasklist}). |
| List Task Lists | `listTaskLists` | Returns all the authenticated user's task lists (GET /users/@me/lists). Supports pagination via maxResults/pageToken. |
| List Tasks | `listTasks` | Returns all tasks in the specified task list (GET /lists/{tasklist}/tasks). Supports filtering by due/completed/updated date ranges and pagination. |
| Move Task | `moveTask` | Moves the specified task to another position in the destination task list (POST /lists/{tasklist}/tasks/{task}/move). Reposition among siblings, re-parent as a subtask, or move to a different task list. |
| Patch Task | `patchTask` | Partially updates the specified task; only the fields provided are changed (PATCH /lists/{tasklist}/tasks/{task}). Typical use: mark a task completed by setting status. |
| Patch Task List | `patchTaskList` | Partially updates the specified task list; only the fields provided are changed (PATCH /users/@me/lists/{tasklist}). |
| Update Task | `updateTask` | Updates the specified task, replacing it with the supplied resource (PUT /lists/{tasklist}/tasks/{task}). |
| Update Task List | `updateTaskList` | Updates the specified task list, replacing it with the supplied resource (PUT /users/@me/lists/{tasklist}). |
