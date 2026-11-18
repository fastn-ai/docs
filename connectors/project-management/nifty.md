---
description: "Nifty project management platform."
hidden: true
---

# Nifty

<img src="../../.gitbook/assets/connectors/lg/nifty.png" alt="Nifty logo">

Nifty project management platform. Manage projects, tasks, task groups (statuses), milestones, documents, files, tags, messages, team members, portfolios, custom fields, time tracking, folders, and webhooks.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `nifty` |

## Use it

Add Nifty from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.nifty.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Document | `attachDocument` | This endpoint adds document to the task. |
| Add File Labels | `addLabels2` | This endpoint adds the labels for the file. |
| Add Folder | `createNewFolder` | This endpoint adds new folder in the project. |
| Add Labels | `addLabels3` | This endpoint adds the labels to the task. |
| Add Project Custom Fields | `addProjectCustomField` | This endpoint creates the custom fields for the project. |
| Add Task Custom Field | `addTaskCustomField` | This endpoint adds the custom field to the task. |
| Archive Milestone | `changeMilestoneStatus` | This endpoint archives the milestone details. |
| Archive Task | `archiveTask` | This endpoint archives the task. |
| Assign Status Members | `assignTask` | This endpoint assignes the list of members to the status. |
| Assign Task | `assignTask2` | This endpoint adds assignee to the task. |
| Clone Task | `cloneTask` | This endpoint creates clone copy of the task. |
| Complete Task | `completeTask` | This endpoint updates the task as completed. |
| Copy File | `copyFile` | This endpoint creates a new copy of the file. |
| Create document | `createDocument` | This endpoint creates a new document. |
| Create Message | `createMessage` | This endpoint creates a new message. |
| Create Milestone | `createMilestone` | This endpoint creates the milestone. |
| Create Personal Document | `createPersonalDocument` | This endpoint creates a new personal document based on given request data. |
| Create Personal Task | `createPersonalTask` | This endpoint creates a personal task for the team member. |
| Create Portfolio | `createSubteam` | This endpoint creates new portfolio |
| Create Project | `createProject` | Creates a project. WARNING - PROVIDER-SIDE FALSE FAILURE, DO NOT RETRY (observed repeatedly 2026-09-02/03): POST https://openapi.niftypm.com/api/v1.0/projects returns upstream 500 {"message":"Looks like something went wrong.","code":999} WHILE ACTUALLY CREATING THE PROJECT - getProejcts immediately afterwards lists it every time. Nothing in the catalog can fix this; the hazard is retry logic, because each retry creates another real project. Callers should treat a 500 from this endpoint as "unknown" and reconcile with getProejcts before retrying. |
| Create Status | `createTaskGroup` | This endpoint creates a new status using the provided details. |
| Create Tag | `createLabel` | This endpoint create a new tag record. |
| Create Task | `createTask` | This endpoint creates the task for the team member. |
| Create task link(s) | `linkTask` | Create task link(s) |
| Create Webhook | `addWebhook` | This endpoint register a new webhook endpoint. |
| Get App | `getApp` | This endpoint fetch the app for team member. |
| Get Apps | `getApps` | This endpoint fetch the apps for team member. |
| Get Chat | `getChat` | This endpoint fetch the details for chat based on given chat id. |
| Get Chats | `getChats` | This endpoint fetch the list of chat id for team member. |
| Get Current User | `getCurrentUser` | Fetch the authenticated user's account and profile details. |
| Get Custom field | `getCustomField` | This endpoint provides details of the custom field in the project. |
| Get Custom fields | `getCustomFields` | This endpoint provides list of all the custom fields in the project. |
| Get Document | `getDocument` | This endpoint fetch a particular document based on document id. |
| Get Documents | `getDocuments` | This endpoint fetch lsit of all the documents based on given query parameters. |
| Get File | `getFile` | This endpoint fetch the details of the file based on unique file identified |
| Get Files | `getFiles` | This endpoint fetch list of files based on the given query parameters. |
| Get Folder | `getFolderbyId` | This endpoint fetch particular folder based on the given query parameter. |
| Get Folder Children | `getChildren` | This endpoint fetch list of sub folders of the folder based on the given query parameters. |
| Get Folder Conntents | `getFolder` | This endpoint fetch folder contents based on the given query parameters. |
| Get Invitee | `getInviteLinks` | This endpoint fetch the list of invitess. |
| Get Member Details | `getMember` | This endpoint fetch the user using user id parameter. |
| Get Members Details | `getMembers` | This endpoint fetch the members details. |
| Get Message | `getMessage` | This endpoint fetch more details about the message. |
| Get Messages | `getMessages` | This endpoint fetch the list of recent messages. |
| Get Milestone | `getMilestone` | This endpoint fetch the milestone information. |
| Get Milestones | `getMilestones` | This endpoint fetch the list of milestones. |
| Get Personal Documents | `getPesonalDocuments` | This endpoint fetch lsit of all the personal documents based on given query parameters. |
| Get Personal Tasks | `getPersonalTasks` | This endpoint fetch the list of personal tasks for the team member. |
| Get Portfolio | `getSubteam` | This endpoint fetch the prortfolio details using unique identifier id. |
| Get Portfolios | `getSubteams` | This endpoint fetch list of portfolios. |
| Get Project | `getProjectById` | This endpoint fetch the project details. |
| Get Project Custom Fields | `getProjectCustomFields` | This endpoint fetch the custom fields for the project. |
| Get Projects | `getProejcts` | This endpoint fetch the list of projects for the team member. |
| Get Status | `getTaskGroup` | This endpoint fetch the status details using unique identifier. |
| Get Statuses | `getTaskGroups` | This endpoint fetch the list of statuses for the team member |
| Get Tag | `getLabel` | This endpoint fetch the tag details using unique label_id. |
| Get Tags | `getLabels` | This endpoint fetch list of all the tag based on given query parameters. |
| Get Task | `getTask` | This endpoint fetch the task details for the team member. |
| Get Task Custom Fields | `getTaskCustomFields` | This endpoint fetch the custom field of the task. |
| Get Tasks | `getTasks` | This endpoint fetch the list of tasks for the team member. |
| Get Templates | `getProjectTemplates` | This endpoint fetch the list of all project templates. |
| Get Tracked Time Duration | `getDuration` | This endpoint fetch the tracked time duration information based on provided criteria. |
| Get Tracked Time Report | `getTimeReport` | This endpoint fetch the tracked time report information based on provided criteria. |
| Get Webhooks | `getWebhooks` | This endpoint fetch list of all webhook registerd by team member. |
| Invite Team Member for project | `invite` | This endpoint sends invitation details to the team member. |
| Leave Portfolio | `leaveSubteam` | This endpoint helps the member to leave from the portfolio. |
| Leave Project | `leaveProject` | This endpoint use to leave the project by team member. |
| Mark Message heard | `hearMessage` | This endpoint marks the message as heard by the member. |
| Mark Message seen | `seeMessage` | This endpoint marks the message as seen by the member. |
| Move Document | `moveDocument` | This endpoint moves a document into another project folder. |
| Move Milestone | `moveToProject` | This endpoint moves the milestone to the project. |
| Move Status Tasks | `moveStatusTasks` | This endpoint transfers list of all the tasks to the given status. |
| Move Tasks | `moveTasks` | This endpoint moves the task. |
| Remove Assignee | `unassignTask2` | This endpoint removes the assignee to the task. |
| Remove Document | `removeDocument` | This endpoint removes a document using unique identifier id. |
| Remove Document Labels | `removeLabels` | This endpoint removes labels from the document. |
| Remove Document Member | `removeMembersFromDocument` | This endpoint removes member from given document. |
| Remove File | `removeFile` | This endpoint removes the file using the unique file idetifier. |
| Remove File Labels | `removeLabels2` | This endpoint remove the labels from the file. |
| Remove Folder | `deleteFolder` | This endpoint removes the folder using the unique folder idetifier. |
| Remove Labels | `removeLabels3` | This endpoint removes the labels from the task. |
| Remove Message | `deleteMessage` | This endpoint removes the message. |
| Remove Milestone | `removeMilestone` | This endpoint removes the milestone. |
| Remove Milestone Task | `untieTasks` | This endpoint removes the list of task from the milestone. |
| Remove Portfolio | `removeSubteam` | This endpoint removes the portfolio using unique identifier id. |
| Remove Portfolio Member | `removeMembers` | This endpoint removes the member from the portfolio. |
| Remove Project | `deleteProject` | This endpoint removes the project details. |
| Remove Status | `removeTaskGroup` | This endpoint removes the status details using unique identifier. |
| Remove Status Member | `unassignTask` | This endpoint removes the list of members to the status. |
| Remove Tag | `removeLabel` | This endpoint removes the tag using unique label_id. |
| Remove Task | `removeTask` | This endpoint removes the task details. |
| Remove Tasks | `removeTasks` | Removes one or more tasks in bulk by their IDs. |
| Remove Webhook | `removeWebhook` | This endpoint remove webhook endpoint. |
| Reorder Task | `reorderTask` | This endpoint moves the order of the task. |
| Start Project | `startProject` | This endpoint marks the project as start state. |
| Tie Task To Milestone | `tieTasks` | This endpoint adds the list of tasks to the milestone. |
| Update Document | `editDocument` | This endpoint updates document using unique document id with given data. |
| Update Document Content | `updateDocumentContent` | Applies content operations to a document. POST https://openapi.niftypm.com/api/v1.0/docs/{document_id}/change. Fixed 2026-09-03: the action sent a "content" array (and an optional "name"), neither of which this endpoint accepts, and Nifty answered 400 Bad Request Exception. The vendor reference (https://developers.niftypm.com/operation/operation-documentsapicontroller_processdocumentchange) defines the body as ChangeDocument: changes (object[], required, "Document content operations to apply, in order") plus an optional changes_id ("Client-generated id used to correlate the change echo over the socket"). Nifty does not publish an item schema for a change operation - its example body is literally {"changes":[{}],"changes_id":"changes_id"} - so callers must supply operations in Nifty's internal collaborative-editing format. |
| Update Document Labels | `addLabels` | This endpoint updates the labels for the document. |
| Update Document Member | `addMembersToDocument` | This endpoint updates document's members list |
| Update File | `editFile` | This endpoint update the file details. |
| Update Folder | `updateFolder` | Update Folder |
| Update Message | `editMessage` | This endpoint update the message. |
| Update Milestone | `editMilestone` | This endpoint updates the milestone details. |
| Update Portfolio | `editSubteam` | This endpoint update the portfolio details using unique identifier id. |
| Update Portfolio Member | `addMembers` | This endpoint update the list of members in the portfolio. |
| Update Project | `updateProject` | This endpoint updates the project details. |
| Update Project Custom Fields | `updateProjectCustomField` | This endpoint update the custom fields details for the project. |
| Update Status | `updateTaskGroup` | This endpoint updates the status details using unique identifier. |
| Update Tag | `editLabel` | This endpoint update the tag details using unique label_id. |
| Update Task | `editTask` | This endpoint update the task details. |
| Update Task Custom Field | `updateTaskCustomField` | This endpoint updates the custom field detail of the task. |
| Update Task Milestone | `updateTaskMilestone` | This endpoint adds milestone details for the task. |
| Update Webhook | `updateWebhook` | This endpoint updates an existing webhook endpoint. |
| Upload Files | `uploadFiles` | This endpoint uploads multiples files. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| PortfolioCreated | `portfolioCreated` | A portfolio was created. (Nifty's docs page lists ~33 total webhook event types behind a client-rendered 'show more' the automated doc fetch could not expand; only these 8 were independently confirmed across multiple sources, so only these are included -- see eventsDetail for the full accounting.) |
| PortfolioRemoved | `portfolioRemoved` | A portfolio was removed. (Nifty's docs page lists ~33 total webhook event types behind a client-rendered 'show more' the automated doc fetch could not expand; only these 8 were independently confirmed across multiple sources, so only these are included -- see eventsDetail for the full accounting.) |
| ProjectCreated | `projectCreated` | A project was created. (Nifty's docs page lists ~33 total webhook event types behind a client-rendered 'show more' the automated doc fetch could not expand; only these 8 were independently confirmed across multiple sources, so only these are included -- see eventsDetail for the full accounting.) |
| ProjectRemoved | `projectRemoved` | A project was removed. (Nifty's docs page lists ~33 total webhook event types behind a client-rendered 'show more' the automated doc fetch could not expand; only these 8 were independently confirmed across multiple sources, so only these are included -- see eventsDetail for the full accounting.) |
| ProjectUpdated | `projectUpdated` | A project was updated. (Nifty's docs page lists ~33 total webhook event types behind a client-rendered 'show more' the automated doc fetch could not expand; only these 8 were independently confirmed across multiple sources, so only these are included -- see eventsDetail for the full accounting.) |
| TaskCreated | `taskCreated` | A task was created. (Nifty's docs page lists ~33 total webhook event types behind a client-rendered 'show more' the automated doc fetch could not expand; only these 8 were independently confirmed across multiple sources, so only these are included -- see eventsDetail for the full accounting.) |
| TaskRemoved | `taskRemoved` | A task was removed. (Nifty's docs page lists ~33 total webhook event types behind a client-rendered 'show more' the automated doc fetch could not expand; only these 8 were independently confirmed across multiple sources, so only these are included -- see eventsDetail for the full accounting.) |
| TaskUpdated | `taskUpdated` | A task was updated. (Nifty's docs page lists ~33 total webhook event types behind a client-rendered 'show more' the automated doc fetch could not expand; only these 8 were independently confirmed across multiple sources, so only these are included -- see eventsDetail for the full accounting.) |
