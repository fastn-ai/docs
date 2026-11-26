---
description: "ClickUp is a project management tool. Create spaces, folders, lists, tasks, goals and tags, log time, add comments and set up webhooks."
hidden: true
---

# ClickUp

<img src="../../.gitbook/assets/connectors/lg/clickup.png" alt="ClickUp logo">

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [clickup.com](https://clickup.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `clickup` |

## Setup

Your customers sign in to ClickUp through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Use it

Add ClickUp from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clickup.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Folder</td><td><code>createFolder</code></td><td>Creates a new folder in a space.</td></tr><tr><td>Create Goal</td><td><code>createGoal</code></td><td>Creates a new goal in a team.</td></tr><tr><td>Create List</td><td><code>createList</code></td><td>Creates a new list inside a folder.</td></tr><tr><td>Create Space</td><td><code>createSpace</code></td><td>Creates a new space in a team/workspace.</td></tr><tr><td>Create Space Tag</td><td><code>createSpaceTag</code></td><td>Creates a new tag in a space.</td></tr><tr><td>Create Task</td><td><code>createTask</code></td><td>Creates a new task in a list.</td></tr><tr><td>Create Task Comment</td><td><code>createTaskComment</code></td><td>Creates a comment on a task.</td></tr><tr><td>Create Time Entry</td><td><code>createTimeEntry</code></td><td>Creates a time entry for a task.</td></tr><tr><td>Create Webhook</td><td><code>createWebhook</code></td><td>Creates a webhook to subscribe to ClickUp events.</td></tr><tr><td>Delete Comment</td><td><code>deleteComment</code></td><td>Deletes a comment.</td></tr></tbody></table>

<details>

<summary>View 35 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Folder</td><td><code>deleteFolder</code></td><td>Deletes a folder.</td></tr><tr><td>Delete Goal</td><td><code>deleteGoal</code></td><td>Deletes a goal.</td></tr><tr><td>Delete List</td><td><code>deleteList</code></td><td>Deletes a list.</td></tr><tr><td>Delete Space</td><td><code>deleteSpace</code></td><td>Deletes a space.</td></tr><tr><td>Delete Space Tag</td><td><code>deleteSpaceTag</code></td><td>Deletes a tag from a space.</td></tr><tr><td>Delete Task</td><td><code>deleteTask</code></td><td>Deletes a task.</td></tr><tr><td>Delete Webhook</td><td><code>deleteWebhook</code></td><td>Deletes a webhook subscription.</td></tr><tr><td>Get Folder</td><td><code>getFolder</code></td><td>Returns details of a specific folder.</td></tr><tr><td>Get Goal</td><td><code>getGoal</code></td><td>Returns details of a specific goal.</td></tr><tr><td>Get List</td><td><code>getList</code></td><td>Returns details of a specific list.</td></tr><tr><td>Get List Members</td><td><code>getListMembers</code></td><td>Returns all members assigned to a list.</td></tr><tr><td>Get Space</td><td><code>getSpace</code></td><td>Returns details of a specific space.</td></tr><tr><td>Get Space Tags</td><td><code>getSpaceTags</code></td><td>Returns all tags in a space.</td></tr><tr><td>Get Task</td><td><code>getTask</code></td><td>Returns details of a specific task.</td></tr><tr><td>Get Task Comments</td><td><code>getTaskComments</code></td><td>Returns all comments on a task.</td></tr><tr><td>Get Task Members</td><td><code>getTaskMembers</code></td><td>Returns all members assigned to a task.</td></tr><tr><td>Get Time Entries</td><td><code>getTimeEntries</code></td><td>Returns time entries for a team within an optional date range.</td></tr><tr><td>List Chat Channels</td><td><code>listChatChannels</code></td><td>Retrieve the Chat channels in a Workspace (ClickUp API v3 Filter by channel type, followed channels, closed DMs or recent messages. Use it to find the channel_id needed by Send Chat Message. Supports cursor pagination.</td></tr><tr><td>List Folderless Lists</td><td><code>listFolderlessLists</code></td><td>Returns all folderless lists in a space.</td></tr><tr><td>List Folders</td><td><code>listFolders</code></td><td>Returns all folders in a space.</td></tr><tr><td>List Goals</td><td><code>listGoals</code></td><td>Returns all goals in a team.</td></tr><tr><td>List Lists in Folder</td><td><code>listListsInFolder</code></td><td>Returns all lists inside a folder.</td></tr><tr><td>List Spaces</td><td><code>listSpaces</code></td><td>Returns all spaces in a team/workspace.</td></tr><tr><td>List Tasks</td><td><code>listTasks</code></td><td>Returns all tasks in a list.</td></tr><tr><td>List Teams (Workspaces)</td><td><code>listTeams</code></td><td>Returns all authorized teams (workspaces) for the authenticated user.</td></tr><tr><td>List User Groups</td><td><code>getTeamMembers</code></td><td>Returns all user groups (teams) in a workspace.</td></tr><tr><td>List Webhooks</td><td><code>listWebhooks</code></td><td>Returns all webhooks in a team.</td></tr><tr><td>Send Chat Message</td><td><code>sendChatMessage</code></td><td>Send a top-level message to a ClickUp Chat channel (ClickUp API v3 Content supports markdown (text/md, default) or plain text. Returns the created message (id, content, date, links). Get channel_id from List Chat Channels.</td></tr><tr><td>Update Comment</td><td><code>updateComment</code></td><td>Updates an existing comment.</td></tr><tr><td>Update Folder</td><td><code>updateFolder</code></td><td>Updates an existing folder.</td></tr><tr><td>Update Goal</td><td><code>updateGoal</code></td><td>Updates an existing goal.</td></tr><tr><td>Update List</td><td><code>updateList</code></td><td>Updates an existing list.</td></tr><tr><td>Update Space</td><td><code>updateSpace</code></td><td>Updates an existing space.</td></tr><tr><td>Update Task</td><td><code>updateTask</code></td><td>Updates an existing task.</td></tr><tr><td>Update Webhook</td><td><code>updateWebhook</code></td><td>Updates an existing webhook's endpoint or events.</td></tr></tbody></table>

</details>

## Events

ClickUp has no events, so it can't start a workflow by itself. Use its actions in a workflow that another [trigger](../../build/triggers/README.md) starts, such as a schedule or a webhook.
