---
description: "Todoist unified API v1 (base https://api.todoist.com/api/v1)."
hidden: true
---

# Todoist

<img src="../../.gitbook/assets/connectors/lg/todoist.png" alt="Todoist logo">

Manage projects, sections, tasks (create/get/update/close/reopen/delete), comments, labels (personal + shared), and collaborators. List endpoints are cursor-paginated ({results, next_cursor}). Auth: Bearer API token (Settings &gt; Integrations &gt; Developer) or OAuth 2.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [todoist.com](https://todoist.com) |
| **Authentication** | Bearer token |
| **Slug** | `todoist` |

## Use it

Add Todoist from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.todoist.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Close Task</td><td><code>closeTask</code></td><td>Complete a task (POST /tasks/{id}/close). Returns 204.</td></tr><tr><td>Create Comment</td><td><code>createComment</code></td><td>Add a comment to a task or project (POST /comments).</td></tr><tr><td>Create Label</td><td><code>createLabel</code></td><td>Create a personal label (POST /labels).</td></tr><tr><td>Create Project</td><td><code>createProject</code></td><td>Create a new project (POST /projects).</td></tr><tr><td>Create Section</td><td><code>createSection</code></td><td>Create a section in a project (POST /sections).</td></tr><tr><td>Create Task</td><td><code>createTask</code></td><td>Create a new task (POST /tasks).</td></tr><tr><td>Delete Comment</td><td><code>deleteComment</code></td><td>Delete a comment (DELETE /comments/{id}). Returns 204.</td></tr><tr><td>Delete Label</td><td><code>deleteLabel</code></td><td>Delete a personal label (DELETE /labels/{id}). Returns 204.</td></tr><tr><td>Delete Project</td><td><code>deleteProject</code></td><td>Delete a project (DELETE /projects/{id}). Returns 204.</td></tr><tr><td>Delete Section</td><td><code>deleteSection</code></td><td>Delete a section and its tasks (DELETE /sections/{id}). Returns 204.</td></tr></tbody></table>

<details>

<summary>View 21 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Task</td><td><code>deleteTask</code></td><td>Delete a task (DELETE /tasks/{id}). Returns 204.</td></tr><tr><td>Get Comment</td><td><code>getComment</code></td><td>Get a comment by ID (GET /comments/{id}).</td></tr><tr><td>Get Label</td><td><code>getLabel</code></td><td>Get a personal label by ID (GET /labels/{id}).</td></tr><tr><td>Get Project</td><td><code>getProject</code></td><td>Get a project by ID (GET /projects/{id}).</td></tr><tr><td>Get Project Collaborators</td><td><code>getProjectCollaborators</code></td><td>List collaborators of a shared project (GET /projects/{id}/collaborators).</td></tr><tr><td>Get Section</td><td><code>getSection</code></td><td>Get a section by ID (GET /sections/{id}).</td></tr><tr><td>Get Task</td><td><code>getTask</code></td><td>Get an active task by ID (GET /tasks/{id}).</td></tr><tr><td>List Comments</td><td><code>listComments</code></td><td>List comments for a task or project (GET /comments).</td></tr><tr><td>List Labels</td><td><code>listLabels</code></td><td>Get all personal labels (GET /labels).</td></tr><tr><td>List Projects</td><td><code>listProjects</code></td><td>Get all projects (GET /projects).</td></tr><tr><td>List Sections</td><td><code>listSections</code></td><td>List sections, optionally filtered by project (GET /sections).</td></tr><tr><td>List Shared Labels</td><td><code>listSharedLabels</code></td><td>List all shared label names (GET /labels/shared).</td></tr><tr><td>List Tasks</td><td><code>listTasks</code></td><td>List active tasks (GET /api/v1/tasks). All given filters narrow the list: project, section, parent task, label or a list of task ids. The list is paginated: pass limit (max 200) and the returned next_cursor as cursor to read the next page. Todoist filter queries (e.g. 'today | overdue') are served by the separate /tasks/filter endpoint, not here.</td></tr><tr><td>Remove Shared Label</td><td><code>removeSharedLabel</code></td><td>Remove a shared label from all tasks (POST /labels/shared/remove). Returns 204.</td></tr><tr><td>Rename Shared Label</td><td><code>renameSharedLabel</code></td><td>Rename a shared label across all tasks (POST /labels/shared/rename). Returns 204.</td></tr><tr><td>Reopen Task</td><td><code>reopenTask</code></td><td>Reopen a completed task (POST /tasks/{id}/reopen). Returns 204.</td></tr><tr><td>Update Comment</td><td><code>updateComment</code></td><td>Update a comment (POST /comments/{id}).</td></tr><tr><td>Update Label</td><td><code>updateLabel</code></td><td>Update a personal label (POST /labels/{id}).</td></tr><tr><td>Update Project</td><td><code>updateProject</code></td><td>Update a project (POST /projects/{id}).</td></tr><tr><td>Update Section</td><td><code>updateSection</code></td><td>Rename a section (POST /sections/{id}).</td></tr><tr><td>Update Task</td><td><code>updateTask</code></td><td>Update a task (POST /tasks/{id}).</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Comment Added</td><td><code>note:added</code></td><td>A comment was added.</td></tr><tr><td>Comment Deleted</td><td><code>note:deleted</code></td><td>A comment was deleted.</td></tr><tr><td>Comment Updated</td><td><code>note:updated</code></td><td>A comment was updated.</td></tr><tr><td>Label Added</td><td><code>label:added</code></td><td>A label was created.</td></tr><tr><td>Label Deleted</td><td><code>label:deleted</code></td><td>A label was deleted.</td></tr><tr><td>Label Updated</td><td><code>label:updated</code></td><td>A label was updated.</td></tr><tr><td>Project Added</td><td><code>project:added</code></td><td>A project was created.</td></tr><tr><td>Project Archived</td><td><code>project:archived</code></td><td>A project was archived.</td></tr><tr><td>Project Deleted</td><td><code>project:deleted</code></td><td>A project was deleted.</td></tr><tr><td>Project Updated</td><td><code>project:updated</code></td><td>A project was updated.</td></tr></tbody></table>

<details>

<summary>View 9 more events</summary>

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Reminder Fired</td><td><code>reminder:fired</code></td><td>A reminder fired.</td></tr><tr><td>Section Added</td><td><code>section:added</code></td><td>A section was created.</td></tr><tr><td>Section Deleted</td><td><code>section:deleted</code></td><td>A section was deleted.</td></tr><tr><td>Section Updated</td><td><code>section:updated</code></td><td>A section was updated.</td></tr><tr><td>Task Added</td><td><code>item:added</code></td><td>A task was created.</td></tr><tr><td>Task Completed</td><td><code>item:completed</code></td><td>A task was completed.</td></tr><tr><td>Task Deleted</td><td><code>item:deleted</code></td><td>A task was deleted.</td></tr><tr><td>Task Uncompleted</td><td><code>item:uncompleted</code></td><td>A completed task was reopened.</td></tr><tr><td>Task Updated</td><td><code>item:updated</code></td><td>A task was updated.</td></tr></tbody></table>

</details>
