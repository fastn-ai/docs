---
description: "ClickUp project management REST API connector for managing workspaces, spaces, folders, lists, tasks, subtasks, comments, members, goals, tags, time tracking,…"
hidden: true
---

# ClickUp

<img src="../../.gitbook/assets/connectors/lg/clickup.png" alt="ClickUp logo">

ClickUp project management REST API connector for managing workspaces, spaces, folders, lists, tasks, subtasks, comments, members, goals, tags, time tracking, and webhooks.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [clickup.com](https://clickup.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `clickup` |

## Use it

Add ClickUp from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clickup.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Folder | `createFolder` | Creates a new folder in a space. |
| Create Goal | `createGoal` | Creates a new goal in a team. |
| Create List | `createList` | Creates a new list inside a folder. |
| Create Space | `createSpace` | Creates a new space in a team/workspace. |
| Create Space Tag | `createSpaceTag` | Creates a new tag in a space. |
| Create Task | `createTask` | Creates a new task in a list. |
| Create Task Comment | `createTaskComment` | Creates a comment on a task. |
| Create Time Entry | `createTimeEntry` | Creates a time entry for a task. |
| Create Webhook | `createWebhook` | Creates a webhook to subscribe to ClickUp events. |
| Delete Comment | `deleteComment` | Deletes a comment. |
| Delete Folder | `deleteFolder` | Deletes a folder. |
| Delete Goal | `deleteGoal` | Deletes a goal. |
| Delete List | `deleteList` | Deletes a list. |
| Delete Space | `deleteSpace` | Deletes a space. |
| Delete Space Tag | `deleteSpaceTag` | Deletes a tag from a space. |
| Delete Task | `deleteTask` | Deletes a task. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook subscription. |
| Get Folder | `getFolder` | Returns details of a specific folder. |
| Get Goal | `getGoal` | Returns details of a specific goal. |
| Get List | `getList` | Returns details of a specific list. |
| Get List Members | `getListMembers` | Returns all members assigned to a list. |
| Get Space | `getSpace` | Returns details of a specific space. |
| Get Space Tags | `getSpaceTags` | Returns all tags in a space. |
| Get Task | `getTask` | Returns details of a specific task. |
| Get Task Comments | `getTaskComments` | Returns all comments on a task. |
| Get Task Members | `getTaskMembers` | Returns all members assigned to a task. |
| Get Time Entries | `getTimeEntries` | Returns time entries for a team within an optional date range. |
| List Chat Channels | `listChatChannels` | Retrieve the Chat channels in a Workspace (ClickUp API v3 GET /api/v3/workspaces/{workspace_id}/chat/channels). Filter by channel type, followed channels, closed DMs or recent messages. Use it to find the channel_id needed by Send Chat Message. Supports cursor pagination. |
| List Folderless Lists | `listFolderlessLists` | Returns all folderless lists in a space. |
| List Folders | `listFolders` | Returns all folders in a space. |
| List Goals | `listGoals` | Returns all goals in a team. |
| List Lists in Folder | `listListsInFolder` | Returns all lists inside a folder. |
| List Spaces | `listSpaces` | Returns all spaces in a team/workspace. |
| List Tasks | `listTasks` | Returns all tasks in a list. |
| List Teams (Workspaces) | `listTeams` | Returns all authorized teams (workspaces) for the authenticated user. |
| List User Groups | `getTeamMembers` | Returns all user groups (teams) in a workspace. |
| List Webhooks | `listWebhooks` | Returns all webhooks in a team. |
| Send Chat Message | `sendChatMessage` | Send a top-level message to a ClickUp Chat channel (ClickUp API v3 POST /api/v3/workspaces/{workspace_id}/chat/channels/{channel_id}/messages). Content supports markdown (text/md, default) or plain text. Returns the created message (id, content, date, links). Get channel_id from List Chat Channels. |
| Update Comment | `updateComment` | Updates an existing comment. |
| Update Folder | `updateFolder` | Updates an existing folder. |
| Update Goal | `updateGoal` | Updates an existing goal. |
| Update List | `updateList` | Updates an existing list. |
| Update Space | `updateSpace` | Updates an existing space. |
| Update Task | `updateTask` | Updates an existing task. |
| Update Webhook | `updateWebhook` | Updates an existing webhook's endpoint or events. |
