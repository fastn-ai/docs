---
description: "Taskade is an AI-native productivity platform for organizing work into workspaces, folders, projects, and tasks, and for building and running AI agents."
hidden: true
---

# Taskade

<img src="../../.gitbook/assets/connectors/lg/taskade.png" alt="Taskade logo">

Taskade is an AI-native productivity platform for organizing work into workspaces, folders, projects, and tasks, and for building and running AI agents. This connector covers the Taskade Public API (v1): workspaces, folders, projects, project members, blocks, share links, tasks and subtasks (create, update, complete, move, dates, notes, assignees, custom fields), AI agents and their knowledge, conversations, public agents, media, and workspace bundles.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [taskade.com](https://taskade.com) |
| **Authentication** | Bearer token |
| **Slug** | `taskade` |

## Use it

Add Taskade from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.taskade.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Media to Agent Knowledge | `agentKnowledgeMediaCreate` | Adds a media item to an AI agent's knowledge base. |
| Add Project to Agent Knowledge | `agentKnowledgeProjectCreate` | Adds a project to an AI agent's knowledge base. |
| Clear Task Date | `taskDeleteDate` | Removes the date from a task. |
| Clear Task Field Value | `taskFieldValueDelete` | Removes a custom field value from a task. |
| Clear Task Note | `taskNoteDelete` | Removes the note from a task. |
| Complete Project | `projectComplete` | Marks a project as complete. |
| Complete Task | `taskComplete` | Marks a task as complete. |
| Copy Project | `projectCopy` | Copies a project into a folder, optionally with a new title. |
| Create Agent in Folder | `folderCreateAgent` | Creates a new AI agent in a folder from configuration data or a predefined template. |
| Create Project | `projectCreate` | Creates a new project from Markdown content in the specified folder. |

<details>

<summary>See 54 more actions</summary>

* **Create Project from Template** `projectFromTemplate`: Creates a new project in a folder from an existing template.
* **Create Project in Workspace** `workspaceCreateProject`: Creates a new project directly in a workspace from Markdown content.
* **Create Tasks** `taskCreate`: Creates one or more tasks in a project (up to 20 per request).
* **Delete Agent** `deleteAgent`: Permanently deletes an AI agent.
* **Delete Media** `mediaDelete`: Permanently deletes a media item.
* **Delete Task** `taskDelete`: Permanently deletes a task from a project.
* **Download All Space Media** `mediaDownloadAll`: Downloads all media items in a space as a single archive.
* **Download Media** `mediaDownload`: Downloads the file content of a media item.
* **Enable Agent Public Access** `agentPublicAccessEnable`: Enables public access for an AI agent and returns its public URL.
* **Enable Project Share Link** `projectShareLinkEnable`: Enables sharing for a project and returns its check, edit, and view share links.
* **Export Space Bundle** `bundleExport`: Exports a space (workspace, folder, or subspace) as a Workspace DNA bundle in JSON form.
* **Export Space Bundle as Archive** `bundleExportZip`: Exports a space as a downloadable .zip or .tsk archive file.
* **Generate Agent in Folder** `folderAgentGenerate`: Generates a new AI agent in a folder from a natural-language description.
* **Get Agent** `agentGet`: Retrieves an AI agent by its ID, including its configuration and metadata.
* **Get Agent Conversation** `agentConvoGet`: Retrieves a single AI agent conversation by its ID.
* **Get Agent Public Settings** `agentPublicGet`: Retrieves the public sharing settings and public URL for an AI agent.
* **Get Media** `mediaGet`: Retrieves a media item's metadata by its ID.
* **Get Project** `projectGet`: Retrieves a project by its ID.
* **Get Project Share Link** `projectShareLinkGet`: Retrieves the share links for a project.
* **Get Public Agent** `publicAgentGet`: Retrieves a publicly shared AI agent by its public ID.
* **Get Task** `taskGet`: Retrieves a single task by its ID.
* **Get Task Date** `taskGetDate`: Retrieves the start and end date of a task.
* **Get Task Field Value** `taskFieldValueGet`: Retrieves a single custom field value on a task.
* **Get Task Note** `taskNoteGet`: Retrieves the note attached to a task.
* **Import Space Bundle** `bundleImport`: Imports a Workspace DNA bundle (JSON) into a target workspace.
* **Import Space Bundle Archive** `bundleImportZip`: Imports a .zip or .tsk bundle archive into a target workspace.
* **List Agent Conversations** `agentConvosGet`: Retrieves the conversations belonging to an AI agent.
* **List Folder Agents** `folderAgentGet`: Retrieves the AI agents contained in a folder.
* **List Folder Media** `mediasGet`: Retrieves the media items contained in a folder.
* **List Folder Project Templates** `folderProjectTemplatesGet`: Retrieves the project templates available in a folder.
* **List Folder Projects** `folderProjectsGet`: Retrieves the projects in a folder, workspace, or space.
* **List My Projects** `meProjectsGet`: Retrieves the authenticated user's projects, ordered by most recently viewed.
* **List Project Blocks** `projectBlocksGet`: Retrieves the content blocks of a project using cursor-based pagination.
* **List Project Fields** `projectFieldsGet`: Retrieves the custom fields defined on a project.
* **List Project Members** `projectMembersGet`: Retrieves the members of a project.
* **List Project Tasks** `projectTasksGet`: Retrieves the tasks of a project using cursor-based pagination.
* **List Task Assignees** `taskAssigneesGet`: Retrieves the users assigned to a task.
* **List Task Field Values** `taskFieldsValueGet`: Retrieves all custom field values on a task.
* **List Workspace Folders** `workspaceFoldersGet`: Retrieves the folders in a workspace.
* **List Workspaces** `listWorkspaces`: Retrieves all workspaces the authenticated user belongs to.
* **Move Task** `taskMove`: Moves a task to a new position relative to another task.
* **Remove Media from Agent Knowledge** `agentKnowledgeMediaRemove`: Removes a media item from an AI agent's knowledge base.
* **Remove Project from Agent Knowledge** `agentKnowledgeProjectRemove`: Removes a project from an AI agent's knowledge base.
* **Remove Task Assignee** `taskDeleteAssignees`: Removes a single assignee from a task by their handle.
* **Restore Project** `projectRestore`: Restores a completed or archived project to active status.
* **Set Task Assignees** `taskPutAssignees`: Sets the assignees of a task by their handles.
* **Set Task Date** `taskPutDate`: Sets the start date (and optional end date) of a task.
* **Set Task Field Value** `taskFieldValuePut`: Sets a custom field value on a task.
* **Set Task Note** `taskNotePut`: Sets the note on a task as plain text or Markdown.
* **Uncomplete Task** `taskUncomplete`: Marks a completed task as incomplete.
* **Update Agent** `agentUpdate`: Updates an AI agent's name and configuration data.
* **Update Agent Public Settings** `agentPublicUpdate`: Updates the public sharing preferences for an AI agent.
* **Update Task Content** `taskPut`: Replaces the content of a task with new Markdown or plain text.
* **Upload Media to Space** `mediaUpload`: Uploads a media file into a space.

</details>
