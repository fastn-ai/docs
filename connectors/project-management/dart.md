---
description: "Dart (dartai.com) is an AI-native project and task management tool."
hidden: true
---

# Dart

<img src="../../.gitbook/assets/connectors/lg/dart.png" alt="Dart logo">

Dart (dartai.com) is an AI-native project and task management tool. This connector wraps the Dart Public API v0: tasks, docs, comments, dartboards, folders, views, agents, skills, webhooks and workspace configuration.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [dartai.com](https://dartai.com) |
| **Authentication** | Bearer token |
| **Slug** | `dart` |

## Use it

Add Dart from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.dart.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Task Attachment From URL | `addTaskAttachmentFromUrl` | Attaches a file to a Dart task by giving Dart a publicly reachable URL to download. Dart fetches the URL, stores the file and returns its stored name, CDN url and MIME kind. The source URL must actually serve the file: an unreachable URL still returns 200 but nothing is attached, so confirm with Get Task. |
| Add Task Comment | `addTaskComment` | Posts a comment on a Dart task, optionally as a reply to an existing comment. Comments notify the task's subscribers in Dart, so do not use this to reach people who are not expecting it. Dart's public API has no delete-comment route, so a posted comment can only be removed with its task. |
| Add Task Time Tracking | `addTaskTimeTracking` | Records a time-tracking entry on a Dart task with a start and finish timestamp. Timestamps must be full ISO-8601 datetimes; date-only values are rejected. The entry is stored against the task, but the public Get Task response only surfaces timeTracking when the workspace has a custom time-tracking property configured. |
| Create Agent | `createAgent` | Creates a new AI agent in the Dart workspace. Only the name is required. Choose an execution mode: Instructions runs a Dart-hosted model against your markdown prompt, Forwarding posts the trigger to a URL you supply, Local hands the work to a local coding agent, and None leaves the agent inert. Instructions-mode agents consume Dart AI usage when triggered. |
| Create Doc | `createDoc` | Creates a new doc in Dart. Only the title is required; folder must be a full folder title from Get Workspace Configuration, and text is the doc body in markdown. |
| Create Skill | `createSkill` | Creates a new skill in Dart: a titled, reusable markdown instruction that every member of the workspace can apply to a task. Both the title and the prompt markdown are required. |
| Create Task | `createTask` | Creates a new task in Dart. Only the title is required; dartboard, type, status, priority, tags and sizes must match the values returned by Get Workspace Configuration. Assigning a task or naming reviewers notifies those people in Dart, so leave them empty unless you intend that. |
| Create Webhook | `createWebhook` | Registers an outgoing webhook so Dart posts the selected workspace events to your URL. The destination URL and at least one event kind are required. Dart will start delivering immediately, so point it at an endpoint you control. |
| Delete Agent | `deleteAgent` | Retires a Dart AI agent by its 12-character id. VERIFIED BEHAVIOUR: despite the name, Dart does not remove the agent - the call returns 200 with the agent body and sets enabled to false, but the agent stays readable through Get Agent and stays in List Agents indefinitely, and repeating the call changes nothing further. Treat this as "disable", not "delete". Tasks previously assigned to the agent are unaffected. |
| Delete Doc | `deleteDoc` | Moves a Dart doc to the trash by its 12-character id and returns the doc as it was before deletion. |
| Delete Skill | `deleteSkill` | Deletes a Dart skill by its 12-character id and returns the skill as it was before deletion. |
| Delete Task | `deleteTask` | Moves a Dart task to the trash by its 12-character id and returns the trashed task. Any comments and attachments on the task go with it. |
| Delete Webhook | `deleteWebhook` | Removes a registered Dart webhook by its 12-character id so it stops receiving events, and returns the webhook as it was before deletion. |
| Exchange Login Token For API Token | `tokenLogin` | Exchanges a standard Dart login token for that user's long-lived public API authentication token. SECURITY: the response body is itself a credential, so treat the result as a secret, never log it, and prefer configuring the API token directly on the connection instead of calling this. |
| Get Agent | `getAgent` | Retrieves a single Dart AI agent by its 12-character id, including its name, whether it is enabled, its execution mode and the configuration for that mode. |
| Get Current User | `getCurrentUser` | Returns the Dart user that the API token authenticates as, including their id, name and email, plus whether the token is currently logged in. Useful as a connection health check. |
| Get Dartboard | `getDartboard` | Retrieves a Dart dartboard (a project or list of tasks) by its 12-character id, returning its full title, description and web URL. Dartboard ids appear in the app URL as /d/&lt;id&gt;-&lt;slug&gt;; Get Workspace Configuration lists dartboard titles. |
| Get Doc | `getDoc` | Retrieves a single Dart doc by its 12-character id, including its folder and its full text. |
| Get Folder | `getFolder` | Retrieves a Dart folder (a container for docs) by its 12-character id, returning its full title, description and web URL. Folder ids appear in the app URL as /f/&lt;id&gt;-&lt;slug&gt;; Get Workspace Configuration lists folder titles. |
| Get Skill | `getSkill` | Retrieves a single Dart skill by its 12-character id, returning its title, prompt markdown and any attachments linked to it. |
| Get Task | `getTask` | Retrieves a single Dart task by its 12-character id, including its description, assignee, reviewer, tags, priority, dates, size, attachments, custom properties and relationships. |
| Get View | `getView` | Retrieves a Dart view (a saved filter over tasks, such as 'My tasks', 'Search' or 'Trash') by its 12-character id, returning its title, description and web URL. View ids appear in the app URL as /v/&lt;id&gt;-&lt;slug&gt; and can be passed to List Tasks as view_id. |
| Get Webhook | `getWebhook` | Retrieves a single registered Dart webhook by its 12-character id, returning its title, destination URL, subscribed event kinds and whether it is enabled. |
| Get Workspace Configuration | `getWorkspaceConfiguration` | Returns the configuration of the authenticated user's Dart workspace: today's date, the user, and the full lists of dartboards, folders, task types, statuses, assignees, tags, priorities, sizes, skills and custom properties. Call this first to discover the valid values for Create Task and Update Task. |
| List Agents | `listAgents` | Lists the AI agents configured in the Dart workspace. Agents can be assigned tasks and carry their own instructions, model and execution mode. Supports limit and offset pagination. |
| List Comments | `listComments` | Lists the comments on a Dart task. task_id is required; the other parameters narrow the result by author, text, parent comment or published date and control ordering and pagination. |
| List Docs | `listDocs` | Lists docs in the Dart workspace with optional filtering by folder, editor, title, body text or id, plus ordering and pagination. An unknown filter value returns an empty page rather than an error. |
| List Skills | `listSkills` | Lists the skills defined in the Dart workspace. A skill is a reusable, user-defined markdown instruction for a type of task. Supports limit and offset pagination. |
| List Tasks | `listTasks` | Lists tasks in the Dart workspace with optional filtering, ordering and pagination. All filters are exact-match on the titles shown in Get Workspace Configuration; an unknown filter value returns an empty page rather than an error. |
| List Webhooks | `listWebhooks` | Lists the outgoing webhooks registered in the Dart workspace, with the URL and event kinds each one subscribes to. Supports limit and offset pagination. |
| Move Task | `moveTask` | Reorders a Dart task relative to another task, placing it immediately before or after the given sibling. Supply exactly one of beforeTaskId or afterTaskId; both are ignored when omitted and the task keeps its position. |
| Retrieve Skill By Title | `retrieveSkillByTitle` | Looks up a Dart skill by its exact title instead of its id. Returns 404 with 'Skill not found' when no skill carries that title, so it doubles as an existence check. |
| Search Help Center Articles | `listHelpCenterArticles` | Searches Dart's public help-center articles and returns matching article titles, descriptions and URLs. Useful for answering how-to questions about Dart itself. |
| Update Agent | `updateAgent` | Updates an existing Dart AI agent. item.id identifies the agent and must match the path id; omitted top-level fields keep their current values. |
| Update Doc | `updateDoc` | Updates an existing Dart doc's title, folder or full text. item.id identifies the doc and is required; supplying text replaces the whole body, so use Update Doc Text for targeted edits. |
| Update Doc Text | `updateDocText` | Applies targeted text edits to a Dart doc's body without resending the whole document. Each update replaces, deletes, or inserts text before or after an anchor string. |
| Update Skill | `updateSkill` | Updates an existing Dart skill's title and/or prompt markdown. item.id identifies the skill and must match the path id; only the fields you supply are changed. |
| Update Task | `updateTask` | Updates an existing Dart task. Only the fields you supply are changed; item.id identifies the task and is required. Changing the assignee notifies that person in Dart. |
| Update Task Description | `updateTaskDescription` | Applies targeted text edits to a Dart task's description without resending the whole body. Each update replaces, deletes, or inserts text before or after an anchor string. Use this to patch a long description safely. |
| Update Webhook | `updateWebhook` | Updates a registered Dart webhook's title, destination URL, event kinds or enabled flag. item.id identifies the webhook and must match the path id; only the fields you supply are changed. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Comment Created | `comment.created` | Fires when a comment is posted on a task. data.model is the comment, including the id of the task it belongs to. Payload shape modelled from Dart's own SDK handler and a real Dart API comment body. |
| Doc Created | `doc.created` | Fires when a doc is created. data.model is the new doc. Payload shape modelled from Dart's own SDK handler and real Dart API doc bodies. |
| Doc Deleted | `doc.deleted` | Fires when a doc is moved to the trash. data.model is the doc as it was before deletion. Payload shape modelled from Dart's own SDK handler. |
| Doc Updated | `doc.updated` | Fires when a doc's title, folder or text changes. data.oldModel is the doc before the change and data.model after it. Payload shape modelled from Dart's own SDK handler. |
| Task Assignees Updated | `task.assignees_updated` | Fires when a task's assignees change. data.oldAssignees and data.newAssignees are the assignee lists and data.model is the task after the change. Payload shape modelled from Dart's own SDK handler. |
| Task Created | `task.created` | Fires when a task is created in the Dart workspace. data.model is the new task. Payload shape modelled from Dart's own SDK handler (its-dart/dart-tools-py dart/server.py) and real Dart API task bodies. |
| Task Deleted | `task.deleted` | Fires when a task is moved to the trash. data.model is the task as it was before deletion. Payload shape modelled from Dart's own SDK handler. |
| Task Status Updated | `task.status_updated` | Fires when a task moves between statuses. data.oldStatus and data.newStatus name the statuses and data.model is the task after the move. Payload shape modelled from Dart's own SDK handler. |
| Task Updated | `task.updated` | Fires when any field of a task changes. data.oldModel is the task before the change and data.model after it. Payload shape modelled from Dart's own SDK handler and real Dart API task bodies. |
