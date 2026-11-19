---
description: "Google Tasks is a to-do list service. Create, update, move and delete tasks and task lists, and clear completed tasks."
hidden: true
---

# Google Tasks

<img src="../../.gitbook/assets/connectors/lg/google-tasks.png" alt="Google Tasks logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [tasks.googleapis.com](https://tasks.googleapis.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleTasks` |

## Setup

Your customers sign in to Google Tasks through fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add Google Tasks from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleTasks.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Clear Completed Tasks</td><td><code>clearTasks</code></td><td>Clears all completed tasks from the specified task list The affected tasks are marked hidden; they are not deleted.</td></tr><tr><td>Create Task</td><td><code>createTask</code></td><td>Creates a new task on the specified task list Optionally place it as a subtask (parent) or after a sibling (previous).</td></tr><tr><td>Create Task List</td><td><code>createTaskList</code></td><td>Creates a new task list and adds it to the authenticated user's task lists</td></tr><tr><td>Delete Task</td><td><code>deleteTask</code></td><td>Deletes the specified task from the task list</td></tr><tr><td>Delete Task List</td><td><code>deleteTaskList</code></td><td>Deletes the specified task list This also deletes all tasks in it. The default task list cannot be deleted.</td></tr><tr><td>Get Task</td><td><code>getTask</code></td><td>Returns the specified task</td></tr><tr><td>Get Task List</td><td><code>getTaskList</code></td><td>Returns the specified task list</td></tr><tr><td>List Task Lists</td><td><code>listTaskLists</code></td><td>Returns all the authenticated user's task lists Supports pagination via maxResults/pageToken.</td></tr><tr><td>List Tasks</td><td><code>listTasks</code></td><td>Returns all tasks in the specified task list Supports filtering by due/completed/updated date ranges and pagination.</td></tr><tr><td>Move Task</td><td><code>moveTask</code></td><td>Moves the specified task to another position in the destination task list Reposition among siblings, re-parent as a subtask, or move to a different task list.</td></tr></tbody></table>

<details>

<summary>View 4 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Patch Task</td><td><code>patchTask</code></td><td>Partially updates the specified task; only the fields provided are changed Typical use: mark a task completed by setting status.</td></tr><tr><td>Patch Task List</td><td><code>patchTaskList</code></td><td>Partially updates the specified task list; only the fields provided are changed</td></tr><tr><td>Update Task</td><td><code>updateTask</code></td><td>Updates the specified task, replacing it with the supplied resource</td></tr><tr><td>Update Task List</td><td><code>updateTaskList</code></td><td>Updates the specified task list, replacing it with the supplied resource</td></tr></tbody></table>

</details>

## Events

Google Tasks has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
