---
description: "Todoist unified API v1 (base https://api.todoist.com/api/v1)."
hidden: true
---

# Todoist

<img src="../../.gitbook/assets/connectors/lg/todoist.png" alt="Todoist logo">

Todoist unified API v1 (base https://api.todoist.com/api/v1). Manage projects, sections, tasks (create/get/update/close/reopen/delete), comments, labels (personal + shared), and collaborators. List endpoints are cursor-paginated ({results, next_cursor}). Auth: Bearer API token (Settings &gt; Integrations &gt; Developer) or OAuth 2.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [todoist.com](https://todoist.com) |
| **Authentication** | Bearer token |
| **Slug** | `todoist` |

## Use it

Add Todoist from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.todoist.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Close Task | `closeTask` | Complete a task (POST /tasks/{id}/close). Returns 204. |
| Create Comment | `createComment` | Add a comment to a task or project (POST /comments). |
| Create Label | `createLabel` | Create a personal label (POST /labels). |
| Create Project | `createProject` | Create a new project (POST /projects). |
| Create Section | `createSection` | Create a section in a project (POST /sections). |
| Create Task | `createTask` | Create a new task (POST /tasks). |
| Delete Comment | `deleteComment` | Delete a comment (DELETE /comments/{id}). Returns 204. |
| Delete Label | `deleteLabel` | Delete a personal label (DELETE /labels/{id}). Returns 204. |
| Delete Project | `deleteProject` | Delete a project (DELETE /projects/{id}). Returns 204. |
| Delete Section | `deleteSection` | Delete a section and its tasks (DELETE /sections/{id}). Returns 204. |
| Delete Task | `deleteTask` | Delete a task (DELETE /tasks/{id}). Returns 204. |
| Get Comment | `getComment` | Get a comment by ID (GET /comments/{id}). |
| Get Label | `getLabel` | Get a personal label by ID (GET /labels/{id}). |
| Get Project | `getProject` | Get a project by ID (GET /projects/{id}). |
| Get Project Collaborators | `getProjectCollaborators` | List collaborators of a shared project (GET /projects/{id}/collaborators). |
| Get Section | `getSection` | Get a section by ID (GET /sections/{id}). |
| Get Task | `getTask` | Get an active task by ID (GET /tasks/{id}). |
| List Comments | `listComments` | List comments for a task or project (GET /comments). |
| List Labels | `listLabels` | Get all personal labels (GET /labels). |
| List Projects | `listProjects` | Get all projects (GET /projects). |
| List Sections | `listSections` | List sections, optionally filtered by project (GET /sections). |
| List Shared Labels | `listSharedLabels` | List all shared label names (GET /labels/shared). |
| List Tasks | `listTasks` | List active tasks (GET /api/v1/tasks). All given filters narrow the list: project, section, parent task, label or a list of task ids. The list is paginated: pass limit (max 200) and the returned next_cursor as cursor to read the next page. Todoist filter queries (e.g. 'today \| overdue') are served by the separate /tasks/filter endpoint, not here. |
| Remove Shared Label | `removeSharedLabel` | Remove a shared label from all tasks (POST /labels/shared/remove). Returns 204. |
| Rename Shared Label | `renameSharedLabel` | Rename a shared label across all tasks (POST /labels/shared/rename). Returns 204. |
| Reopen Task | `reopenTask` | Reopen a completed task (POST /tasks/{id}/reopen). Returns 204. |
| Update Comment | `updateComment` | Update a comment (POST /comments/{id}). |
| Update Label | `updateLabel` | Update a personal label (POST /labels/{id}). |
| Update Project | `updateProject` | Update a project (POST /projects/{id}). |
| Update Section | `updateSection` | Rename a section (POST /sections/{id}). |
| Update Task | `updateTask` | Update a task (POST /tasks/{id}). |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Comment Added | `note:added` | A comment was added. |
| Comment Deleted | `note:deleted` | A comment was deleted. |
| Comment Updated | `note:updated` | A comment was updated. |
| Label Added | `label:added` | A label was created. |
| Label Deleted | `label:deleted` | A label was deleted. |
| Label Updated | `label:updated` | A label was updated. |
| Project Added | `project:added` | A project was created. |
| Project Archived | `project:archived` | A project was archived. |
| Project Deleted | `project:deleted` | A project was deleted. |
| Project Updated | `project:updated` | A project was updated. |
| Reminder Fired | `reminder:fired` | A reminder fired. |
| Section Added | `section:added` | A section was created. |
| Section Deleted | `section:deleted` | A section was deleted. |
| Section Updated | `section:updated` | A section was updated. |
| Task Added | `item:added` | A task was created. |
| Task Completed | `item:completed` | A task was completed. |
| Task Deleted | `item:deleted` | A task was deleted. |
| Task Uncompleted | `item:uncompleted` | A completed task was reopened. |
| Task Updated | `item:updated` | A task was updated. |
