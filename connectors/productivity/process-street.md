---
description: "Process Street is a workflow and process management platform for recurring checklists, approvals and standard operating procedures."
hidden: true
---

# Process Street

Process Street is a workflow and process management platform for recurring checklists, approvals and standard operating procedures. This connector covers the Process Street Public API v1.1: workflows and their revisions, tasks, widgets, form fields and conditional logic; workflow runs with assignees, approvals and form field values; pages and page revisions; data sets and their records; folders, permissions, scheduled workflows, one-off tasks, My Work, attachments, comments, users and webhooks.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [process.st](https://process.st) |
| **Authentication** | API key |
| **Actions** | 150 |
| **Events** | 6 |
| **Slug** | `processStreet` |

## Use it

Add Process Street from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.processStreet.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Approve Or Reject Task | `upsertApproval` | Records an Approved or Rejected decision on an approval task in a workflow run. Approval Task ID is the approval task itself; Subject Task ID is the task being approved. Returns 204 with no body on success. |
| Assign User To Task | `assignTask` | Assigns a user, by email, to one task in a workflow run. Returns 204 with no body on success. |
| Assign User To Workflow Run | `assignWorkflowRun` | Assigns a user, by email, to a whole workflow run. Returns 204 with no body on success. |
| Batch Update Form Field Values | `batchUpdateFormFieldValues` | Writes several form field values in one call. Each entry needs the form field id plus value (or values for multi-select, dataSetRowId for a data set lookup). |
| Complete One-Off Task | `completeOneOffTask` | Marks a standalone task complete. |
| Create Comment | `createComment` | Posts a comment on a task inside a workflow run. |
| Create Conditional Logic Rule | `createWorkflowRevisionLogicRule` | Adds a Show or Hide conditional logic rule to a draft workflow revision. Condition must be nested as { or: [ { and: [ { widgetId, operator, value } ] } ] }; Targets names the taskIds and widgetIds the rule acts on. |
| Create Data Set | `createDataSet` | Creates a data set with an optional list of column definitions. Each field needs a name and a fieldType such as Text, Number, Date, Url or Email. |
| Create Data Set Incoming Webhook | `createDataSetIncomingWebhook` | Creates an inbound webhook URL that writes rows into a data set. Config.columns is an object whose KEYS are the 22-character data set column IDs and whose values are the incoming payload keys. |
| Create Data Set Record | `createDataSetRecord` | Adds a row to a data set. Cells is a list of { fieldId, value } pairs using the data set's column IDs. |
| Create File Upload | `createFileUpload` | Reserves a file slot and returns a File Upload ID plus a pre-signed S3 uploadUrl. PUT the file bytes to that uploadUrl, then pass the File Upload ID to Upload Attachment, Upload Form Field Value or a widget upload action. |
| Create Folder | `createFolder` | Creates a folder in your organization. Omit Parent Folder ID to create it directly under the organization's Home folder. |
| Create One-Off Task | `createOneOffTask` | Creates a standalone task that is not part of a workflow run. Subtasks and Assignee Emails must both be present, even as empty lists. |
| Create Page | `createPage` | Creates a page in a folder. Leave Share Level at None unless a publicly viewable page was explicitly requested. |
| Create Page Revision | `createPageRevision` | Opens a new draft revision of a page so its widgets can be edited. Publish it afterwards with Publish Page Revision. |
| Create Page Widget | `createPageRevisionWidget` | Adds a content widget to a draft page revision. Type is one of FormField, Text, Image, File, Video, Embed or CrossLink; supply the matching payload field (content for Text, url for Image/File/Video/Embed, linkedTemplateId for CrossLink). |
| Create Scheduled Workflow | `createScheduledWorkflow` | Schedules a workflow to start runs on a recurrence. Rules must contain at least one rule such as { interval: 1, frequency: 'Daily' }; Weekly rules add weekDay and Monthly rules add by. |
| Create Task Widget | `createWorkflowRevisionTaskWidget` | Adds a widget to a task in a draft workflow revision. Type is FormField, Text, Image, File, Video, Embed or CrossLink. Text takes content; Image, File, Video and Embed take url; CrossLink takes linkedTemplateId; FormField takes fieldType, label and key. |
| Create Webhook | `createWebhook` | Creates a webhook subscription that posts Process Street events to your URL. Scope it to the whole organization, to a single workflow, or to a single task by supplying Workflow ID and Task ID. |
| Create Workflow | `createWorkflow` | Creates a workflow in a folder. Leave Share Level at None and Run Link Share Level at Organization unless the customer has explicitly asked for a shareable or public link, because those settings expose the workflow outside the organization. |
| Create Workflow Incoming Webhook | `createWorkflowIncomingWebhook` | Creates an inbound webhook URL that starts a run of this workflow when it receives a POST. Automation App names the integration sending it, for example Zapier. |
| Create Workflow Revision | `createWorkflowRevision` | Opens a new draft revision of a workflow, copying the published content, so its tasks and widgets can be edited. Publish it afterwards with Publish Workflow Revision. |
| Create Workflow Revision Task | `createWorkflowRevisionTask` | Adds a task to a draft workflow revision. Task Type is Standard, Approval, AI or Code. Stop marks it as a stop task; Due Offset is an ISO-8601 duration. |
| Create Workflow Run | `createWorkflowRun` | Starts a new run of a workflow. Optionally give it a name, a due date and whether it is shared. |
| Delete All Files From Form Field | `deleteFormFieldAllFiles` | Clears every uploaded file from a File or Image form field in a workflow run. Returns 204 with no body on success. |
| Delete Attachment | `deleteAttachment` | Permanently deletes a file attachment by its ID. |
| Delete Comment | `deleteComment` | Deletes a comment by its ID. Returns 204 with no body on success. |
| Delete Conditional Logic Rule | `deleteWorkflowRevisionLogicRule` | Removes a conditional logic rule from a draft workflow revision. Returns 204 with no body on success. |
| Delete Data Set | `deleteDataSet` | Deletes a data set and all of its records. Returns 204 with no body on success. |
| Delete Data Set Incoming Webhook | `deleteDataSetIncomingWebhook` | Deletes an inbound data set webhook by its ID. Returns 204 with no body on success. |
| Delete Data Set Record | `deleteDataSetRecord` | Deletes a single row from a data set. |
| Delete File From Form Field | `deleteFormFieldFileById` | Removes one specific uploaded file from a form field in a workflow run. Returns 204 with no body on success. |
| Delete Folder | `deleteFolder` | Deletes a folder. The folder must already be empty - it cannot contain subfolders, workflows or pages. |
| Delete One-Off Task | `deleteOneOffTask` | Deletes a standalone task. Returns 204 with no body on success. |
| Delete Page | `deletePage` | Deletes a page by its ID. Returns 204 with no body on success. |
| Delete Page Revision | `deletePageRevision` | Discards a draft page revision. Returns 204 with no body on success. |
| Delete Page Widget | `deletePageRevisionWidget` | Removes a widget from a draft page revision. Returns 204 with no body on success. |
| Delete Scheduled Workflow | `deleteScheduledWorkflow` | Deletes a workflow schedule so it stops starting runs. Returns 204 with no body on success. |
| Delete Task Widget | `deleteWorkflowRevisionTaskWidget` | Removes a widget from a task in a draft workflow revision. Returns 204 with no body on success. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook subscription by its ID, stopping all further event deliveries to its URL. |
| Delete Workflow | `deleteWorkflow` | Soft-deletes a workflow by its ID. Its runs are no longer listed and the workflow disappears from the active workflow list. |
| Delete Workflow Incoming Webhook | `deleteWorkflowIncomingWebhook` | Deletes an inbound workflow webhook by its ID. Returns 204 with no body on success. |
| Delete Workflow Revision | `deleteWorkflowRevision` | Discards a draft workflow revision. Returns 204 with no body on success. |
| Delete Workflow Revision Task | `deleteWorkflowRevisionTask` | Removes a task from a draft workflow revision. Returns 204 with no body on success. |
| Delete Workflow Run | `deleteWorkflowRun` | Deletes a workflow run by its ID. The deletion is soft, so the run can be restored with Undelete Workflow Run. |
| Duplicate Page | `duplicatePage` | Copies a page, optionally from a specific revision, into a chosen folder under a new name. |
| Duplicate Workflow | `duplicateWorkflow` | Copies a workflow, optionally from a specific revision, into a chosen folder under a new name. |
| Export Page As Markdown | `getPageMarkdown` | Returns the page's published content rendered as Markdown. |
| Export Page Revision As Markdown | `getPageRevisionMarkdown` | Returns one page revision's content rendered as Markdown. |
| Get Comment | `getComment` | Retrieves a single comment by its ID. |
| Get Conditional Logic Rule | `getWorkflowRevisionLogicRule` | Retrieves one conditional logic rule by its ID. |
| Get Data Set | `getDataSet` | Retrieves a data set by its ID, including its column definitions. |
| Get Data Set Incoming Webhook | `getDataSetIncomingWebhook` | Retrieves one inbound data set webhook by its ID. |
| Get Data Set Record | `getDataSetRecord` | Retrieves a single data set row by its ID. |
| Get Folder Permissions | `getFolderPermissions` | Lists who can access a folder and at what level. |
| Get My Work Stats | `getMyWorkStats` | Returns counts of overdue, due-today and upcoming My Work items for a person. |
| Get One-Off Task | `getOneOffTask` | Retrieves a standalone task by its ID, with its subtasks and assignees. |
| Get Page | `getPage` | Retrieves a page by its ID. |
| Get Page Permissions | `getPagePermissions` | Lists who can access a page and at what level. |
| Get Page Revision | `getPageRevision` | Retrieves a single page revision by its ID. |
| Get Page Widget | `getPageRevisionWidget` | Retrieves a single page widget by its ID. |
| Get Scheduled Workflow | `getScheduledWorkflow` | Retrieves one workflow schedule, including its next and previous run dates. |
| Get Task Assignment Rules | `getWorkflowRevisionTaskAssignmentRules` | Returns the rules that decide who a task is assigned to when a run starts. |
| Get Task Due Date Rule | `getTaskDueDateRule` | Returns the rule that sets a task's due date inside a run. |
| Get Task In Workflow Run | `getTask` | Retrieves one task of a workflow run, with its status, due date and assignees. |
| Get Task Permission Rules | `getWorkflowRevisionTaskPermissionRules` | Returns the per-task read and update permission rules of a workflow revision task. |
| Get Task Widget | `getWorkflowRevisionTaskWidget` | Retrieves one widget of a workflow revision task. |
| Get Webhook | `getWebhook` | Retrieves a single webhook subscription by its ID, including its target URL, triggers, status and any workflow or task scoping. |
| Get Workflow | `getWorkflow` | Retrieves a single workflow by its ID, with its name, description and audit trail. |
| Get Workflow Incoming Webhook | `getWorkflowIncomingWebhook` | Retrieves one inbound workflow webhook by its ID. |
| Get Workflow Permissions | `getWorkflowPermissions` | Lists who can access a workflow and at what level. |
| Get Workflow Revision | `getWorkflowRevision` | Retrieves one workflow revision by its ID, with its version and status. |
| Get Workflow Revision Task | `getWorkflowRevisionTask` | Retrieves one task definition of a workflow revision. |
| Get Workflow Run | `getWorkflowRun` | Retrieves a workflow run by its ID, with its status, name, due date, sharing flag and audit trail. |
| Get Workflow Run Due Date Rule | `getChecklistDueDateRule` | Returns the rule that sets the due date of runs started from this workflow revision. |
| Get Workflow Task Configuration | `getWorkflowRevisionTaskConfig` | Returns the type-specific configuration of an Approval, AI or Code task. |
| Import Data Set Records | `importDataSetRecords` | Bulk-loads rows into a data set from CSV text using the Upsert or Sync strategy. Key is the COLUMN NAME (the CSV header, not the column ID) that rows are matched on. CSV Content is the full file text including its header row. Append is not available here because Process Street rejects a request that carries a key, and this action always sends one. |
| List Approvals In Workflow Run | `listApprovals` | Lists the approval decisions recorded on a workflow run. |
| List Attachments | `listAttachments` | Lists file attachments, optionally narrowed to a workflow, a workflow run, a task or a creator. |
| List Comments | `listComments` | Lists comments. Process Street requires at least one scope: pass Workflow ID, or Workflow Run ID (optionally with Task ID). Page with the cursor from the response link named 'next'. |
| List Conditional Logic Rules | `listWorkflowRevisionLogicRules` | Lists the conditional logic rules of a workflow revision. |
| List Data Set Incoming Webhooks | `listDataSetIncomingWebhooks` | Lists the inbound webhooks that push rows into a data set. |
| List Data Set Records | `listDataSetRecords` | Lists the rows of a data set. Pass Columns as a comma-separated list of column IDs to narrow the returned cells. |
| List Data Sets | `listDataSets` | Lists the data sets in your organization. Page with the cursor from the response link named 'next'. |
| List Folders | `listFolders` | Lists the folders in your organization that you have permission to read, as a paginated page. The system Home and Private folders are excluded. |
| List Form Field Options | `listFormFieldOptions` | Lists the selectable options of a dropdown, multi-choice or multi-select form field. |
| List Form Field Values | `listFormFieldValues` | Lists every form field in a workflow run with its current value. |
| List Form Field Values In Task | `listFormFieldValuesByTask` | Lists the form fields belonging to one task of a workflow run with their current values. |
| List Form Fields In Workflow | `listFormFields` | Lists the form fields defined on a workflow's published revision, with their keys, labels and field types. |
| List My Work Items | `listMyWorkItems` | Lists My Work items (assigned workflow tasks and one-off tasks) for a person, with optional due-date window, type, workflow, snooze status and completed filters. |
| List Page Revisions | `listPageRevisions` | Lists a page's revisions, optionally filtered by status such as Draft or Finished. |
| List Page Widgets | `listPageRevisionWidgets` | Lists the content widgets of a page revision, optionally filtered by widget type. |
| List Pages | `listPages` | Lists the pages in your organization, optionally filtered by a partial name match or a folder. |
| List Scheduled Workflows | `listScheduledWorkflows` | Lists recurring workflow schedules, optionally narrowed to one workflow or a search term. |
| List Task Assignees | `listTaskAssignees` | Lists the people assigned to one task in a workflow run. |
| List Task Widgets | `listWorkflowRevisionTaskWidgets` | Lists the widgets of a workflow revision task, optionally filtered by widget type. |
| List Tasks By Assignee | `listTasks` | Lists every workflow run task assigned to one person. Assignee Email is required; narrow further with Workflow ID. |
| List Tasks In Workflow | `listWorkflowTasks` | Lists every run task across all runs of a workflow. |
| List Tasks In Workflow Run | `listTasksByWorkflowRun` | Lists the tasks in a workflow run, 20 at a time and in task order. To page, follow the href of the link named 'next'. |
| List Users | `listUsers` | Lists the users in your Process Street organization, 20 at a time and sorted by name. To page, follow the href of the link named 'next' in the response rather than constructing a cursor yourself. |
| List Webhooks | `listWebhooks` | Lists the webhook subscriptions registered for your Process Street organization, as a paginated page. |
| List Workflow Incoming Webhooks | `listWorkflowIncomingWebhooks` | Lists the inbound webhooks that start runs of a workflow. |
| List Workflow Revision Tasks | `listWorkflowRevisionTasks` | Lists the task definitions of a workflow revision, optionally filtered by task type. |
| List Workflow Revision Variables | `listWorkflowRevisionVariables` | Lists the merge-tag variables available in a workflow revision. Type is required, for example FormField. |
| List Workflow Revisions | `listWorkflowRevisions` | Lists a workflow's revisions, optionally filtered by status such as Draft or Finished. |
| List Workflow Run Assignees | `listWorkflowRunAssignees` | Lists the people assigned to a workflow run. |
| List Workflow Runs | `listWorkflowRuns` | Lists workflow runs as a paginated page, optionally filtered by workflow and status. |
| List Workflows | `listWorkflows` | Lists the active workflows in your organization, 20 at a time and sorted by name, optionally narrowed by a partial name match. To page, follow the href of the link named 'next'. |
| Publish Page Revision | `publishPageRevision` | Publishes a draft page revision, making its content the live version of the page. |
| Publish Workflow Revision | `publishWorkflowRevision` | Publishes a draft workflow revision so new runs use it. |
| Search My Work Items | `searchMyWorkItems` | Searches My Work items across several assignees, types and workflows at once, with sorting. |
| Search Workflow Runs | `searchWorkflowRuns` | Searches workflow runs by workflow, name and status. Pass Fields as a comma-separated list of form field keys to include their values in each result. |
| Set Folder Permissions | `updateFolderPermissions` | Grants one user an access level on a folder. Process Street replaces the whole permission list on every call, so this action sets exactly one { email, accessLevel } entry and anyone else loses their explicit grant. |
| Set Page Permissions | `updatePagePermissions` | Grants one user an access level on a page. Process Street replaces the whole permission list on every call, so this action sets exactly one { email, accessLevel } entry. |
| Set Task Due Date Rule | `setTaskDueDateRule` | Sets the rule that computes a task's due date. Rule needs sourceType, offsetDirection, dueOffset as an ISO-8601 duration such as P2D, and businessDaysHandlingMode. |
| Set Workflow Permissions | `updateWorkflowPermissions` | Grants one user an access level on a workflow. Process Street replaces the whole permission list on every call, so this action sets exactly one { email, accessLevel } entry. |
| Set Workflow Run Due Date Rule | `setChecklistDueDateRule` | Sets or clears the due date rule for runs of this workflow revision. Rule needs sourceType (ChecklistStartDate or FormFieldValue), offsetDirection, dueOffset as an ISO-8601 duration such as P1D, and businessDaysHandlingMode. Omit Rule to clear it. |
| Snooze My Work Item | `snoozeMyWorkItem` | Hides a My Work item from the active list until the given date and time. |
| Test Authentication | `testAuth` | Confirms the API key is valid and returns the label it was given in Process Street. The cheapest call for checking a connection. |
| Unassign User From Task | `unassignTask` | Removes a user, by email, from one task in a workflow run. Returns 204 with no body on success. |
| Unassign User From Workflow Run | `unassignWorkflowRun` | Removes a user, by email, from a workflow run. Returns 204 with no body on success. |
| Uncomplete One-Off Task | `uncompleteOneOffTask` | Reopens a completed standalone task. |
| Undelete Workflow Run | `undeleteWorkflowRun` | Restores a soft-deleted workflow run. |
| Unsnooze My Work Item | `unsnoozeMyWorkItem` | Returns a snoozed My Work item to the active list. Returns 204 with no body on success. |
| Update Comment | `updateComment` | Replaces the text of an existing comment. Returns 204 with no body on success. |
| Update Conditional Logic Rule | `updateWorkflowRevisionLogicRule` | Replaces a conditional logic rule's condition, action and targets. Condition must be nested as { or: [ { and: [ { widgetId, operator, value } ] } ] }. |
| Update Data Set | `updateDataSet` | Replaces a data set's name and column definitions. PUT semantics: send every column you want to keep, each with its existing id, or it is removed. |
| Update Data Set Incoming Webhook | `updateDataSetIncomingWebhook` | Replaces an inbound data set webhook's name, automation app, status and column mapping. PUT semantics - send every field you want to keep. |
| Update Data Set Record | `updateDataSetRecord` | Replaces the cells of a data set row. Send every cell you want to keep. |
| Update Folder | `updateFolder` | Renames an existing folder. The name is the only folder property this endpoint changes. |
| Update One-Off Task | `updateOneOffTask` | Replaces a standalone task. PUT semantics - send name, required, assigneeEmails and the full subtasks list every time. Every subtask needs both a name and a status (NotCompleted or Completed); include its id to keep an existing subtask. |
| Update Page | `updatePage` | Replaces a page's name, description, folder and share level. PUT semantics - send every field you want to keep. |
| Update Page Revision | `updatePageRevision` | Sets the change type (Material or NonMaterial) and change explanation on a draft page revision. |
| Update Page Widget | `updatePageRevisionWidget` | Replaces a page widget's payload. Send the widget type plus the matching content field. |
| Update Scheduled Workflow | `updateScheduledWorkflow` | Replaces a workflow schedule. PUT semantics - send workflowId, startDate, timeZone and the full rules list every time. |
| Update Task Assignment Rules | `updateWorkflowRevisionTaskAssignmentRules` | Sets the task's assignment rules to a single fixed-user rule. Process Street replaces the whole rule list on every call, so this action sends exactly one { type, email } entry. |
| Update Task In Workflow Run | `updateTask` | Checks or unchecks a task in a workflow run and optionally sets its due date. Returns 204 with no body on success. |
| Update Task Permission Rules | `updateWorkflowRevisionTaskPermissionRules` | Sets the task's permission rules to a single fixed-user rule. Process Street replaces the whole rule list on every call, so this action sends exactly one { type, email, taskRead, taskUpdate } entry. |
| Update Task Widget | `updateWorkflowRevisionTaskWidget` | Replaces a task widget's payload. Send the widget type plus the matching content field. |
| Update Webhook | `updateWebhook` | Replaces a webhook subscription's configuration. This endpoint has PUT semantics, so send every field you want to keep - anything you leave out is cleared. |
| Update Workflow | `updateWorkflow` | Replaces a workflow's properties. This endpoint has PUT semantics, so send every field you want to keep - read the workflow first if you are changing only one of them. Leave Share Level at None and Run Link Share Level at Organization unless a shareable or public link was explicitly requested. |
| Update Workflow Incoming Webhook | `updateWorkflowIncomingWebhook` | Replaces an inbound workflow webhook's name, automation app, status and config. PUT semantics. |
| Update Workflow Revision | `updateWorkflowRevision` | Sets the change type, change explanation and default run name on a draft workflow revision. |
| Update Workflow Revision Task | `updateWorkflowRevisionTask` | Replaces a task definition in a draft workflow revision. Stop and Hidden By Default are both required, so send their current values if you are only renaming the task. |
| Update Workflow Run | `updateWorkflowRun` | Replaces a workflow run's name, status, sharing flag and due date. This endpoint has PUT semantics, so send every field you want to keep; omitting Due Date, or sending it as null, clears the due date. Setting Status to Completed completes the run and Archived archives it. |
| Update Workflow Task Configuration | `updateWorkflowRevisionTaskConfig` | Sets the type-specific configuration of a task. Send Type Approval with Subject Task IDs, Type AI with Prompt (and optionally System Prompt and Output Mapping), or Type Code with Code (and optionally Input Mapping and Output Mapping). Only the fields you pass are sent. |
| Upload Attachment | `uploadAttachment` | Attaches an already-uploaded file to a task in a workflow run. First call Create File Upload, PUT the bytes to the returned uploadUrl, then pass the returned File Upload ID here. |
| Upload File To Page Widget | `uploadPageRevisionWidgetFile` | Attaches an already-uploaded file to an Image, File or Video page widget. Call Create File Upload first, PUT the bytes to the returned uploadUrl, then pass the File Upload ID here. |
| Upload File To Task Widget | `uploadWorkflowRevisionTaskWidgetFile` | Attaches an already-uploaded file to an Image, File or Video task widget. Call Create File Upload first, PUT the bytes to the returned uploadUrl, then pass the File Upload ID here. |
| Upload Form Field Value | `uploadFormFieldValue` | Sets a File or Image form field's value from an already-uploaded file. Call Create File Upload first, PUT the bytes to the returned uploadUrl, then pass the File Upload ID here. Returns 204 with no body on success. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Task Checked | `TaskChecked` | Fires when a task in a workflow run is marked complete. Payload schema modelled from Process Street's documented task sample, not captured from a live delivery. |
| Task Checked Or Unchecked | `TaskCheckedUnchecked` | Fires on either completion or un-completion of a task, so one subscription covers both transitions. Read the payload's type field to tell them apart. Payload schema modelled from Process Street's documented task sample, not captured from a live delivery. |
| Task Ready | `TaskReady` | Fires when a task becomes available to work on, for example when a stop task ahead of it is cleared. Payload schema modelled from Process Street's documented task sample, not captured from a live delivery. |
| Task Unchecked | `TaskUnchecked` | Fires when a completed task in a workflow run is marked incomplete again. Payload schema modelled from Process Street's documented task sample, not captured from a live delivery. |
| Workflow Run Completed | `WorkflowRunCompleted` | Fires when every task in a workflow run has been completed and the run finishes. Payload schema modelled from Process Street's documented workflow-run sample, not captured from a live delivery. |
| Workflow Run Created | `WorkflowRunCreated` | Fires when a workflow run is started. Note that the delivered payload's own discriminator is `type: "ChecklistCreated"` - Process Street's subscription trigger names and its payload type names differ. Payload schema modelled from Process Street's documented sample at https://www.process.st/help/docs/webhooks/, not captured from a live delivery. |
