---
description: "Wrike work management and project collaboration platform."
hidden: true
---

# Wrike

<img src="../../.gitbook/assets/connectors/wrike.png" alt="Wrike logo" width="64">

Wrike work management and project collaboration platform. Manage tasks, folders, projects, timelogs, comments, and account resources via the Wrike API v4.

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [wrike.com](https://wrike.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `wrike` |

## Use it

Add Wrike from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wrike.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Copy Folder | `copyFolder` | Copies a folder or project (and optionally its subtree) into a target parent folder. |
| Create Custom Field | `createCustomField` | Creates a new custom field in the account. |
| Create Dependency | `createDependency` | Creates a dependency between the given task and a predecessor or successor task. |
| Create Folder | `createFolder` | Creates a new folder or project inside a parent folder. |
| Create Folder Comment | `createFolderComment` | Adds a comment to a folder or project. |
| Create Group | `createGroup` | Creates a new user group in the account. |
| Create Invitation | `createInvitation` | Invites a new user to the account by email. |
| Create Space | `createSpace` | Creates a new space in the account. |
| Create Task | `createTask` | Creates a new task inside a folder or project. |
| Create Task Approval | `createTaskApproval` | Creates an approval on a task, assigning approvers and an optional due date. |

<details>

<summary>See 72 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Task Comment | `createTaskComment` | Adds a comment to a task. |
| Create Timelog | `createTimelog` | Logs time against a task. |
| Create Webhook | `createWebhook` | Registers an account-level webhook that delivers event notifications to a URL. |
| Create Workflow | `createWorkflow` | Creates a new workflow in the account. |
| Delete Approval | `deleteApproval` | Deletes an approval by its ID. |
| Delete Attachment | `deleteAttachment` | Deletes an attachment by its ID. |
| Delete Comment | `deleteComment` | Deletes a comment by its ID. |
| Delete Custom Field | `deleteCustomField` | Deletes a custom field by its ID. |
| Delete Dependency | `deleteDependency` | Deletes a task dependency by its ID. |
| Delete Folder | `deleteFolder` | Moves a folder or project to the recycle bin. |
| Delete Group | `deleteGroup` | Deletes a user group by its ID. |
| Delete Invitation | `deleteInvitation` | Cancels and deletes a pending invitation. |
| Delete Space | `deleteSpace` | Deletes a space by its ID. |
| Delete Task | `deleteTask` | Moves a task to the recycle bin. |
| Delete Timelog | `deleteTimelog` | Deletes a time-log record by its ID. |
| Delete Webhook | `deleteWebhook` | Deletes a webhook by its ID. |
| Get Account | `getAccount` | Retrieves information about the current Wrike account, including its name, date format, subscription, and enabled features. |
| Get Approval | `getApproval` | Retrieves one or more approvals by ID (comma-separated). |
| Get Attachment | `getAttachment` | Retrieves metadata for one or more attachments by ID (comma-separated). |
| Get Attachment Download URL | `getAttachmentDownloadUrl` | Returns a temporary download URL for an attachment. |
| Get Comment | `getComment` | Retrieves one or more comments by ID (comma-separated). |
| Get Contacts By ID | `getContactsById` | Retrieves one or more specific contacts by their IDs. Accepts a comma-separated list of up to 100 contact IDs. |
| Get Current User | `getCurrentUser` | Retrieves the profile of the currently authenticated Wrike user, including name, profiles, and account membership. |
| Get Custom Field | `getCustomField` | Retrieves one or more custom fields by ID (comma-separated). |
| Get Dependency | `getDependency` | Retrieves one or more dependencies by ID (comma-separated). |
| Get Folder | `getFolder` | Retrieves one or more folders/projects by ID (comma-separated, max 100). |
| Get Group | `getGroup` | Retrieves a single user group by its ID. |
| Get Space | `getSpace` | Retrieves a single space by its ID. |
| Get Task | `getTask` | Retrieves one or more tasks by ID (comma-separated, max 100). |
| Get Timelog | `getTimelog` | Retrieves one or more time-log records by ID (comma-separated). |
| Get User | `getUser` | Retrieves detailed information about a single user by their user ID, including profile and account membership. |
| Get Webhook | `getWebhook` | Retrieves one or more webhooks by ID (comma-separated). |
| List Approvals | `listApprovals` | Lists approvals in the account, optionally filtered by status. |
| List Attachments | `listAttachments` | Lists attachments in the account created within a date range (default last 7 days). |
| List Comments | `listComments` | Lists all comments in the account created within the last 7 days. |
| List Contact Timelogs | `listContactTimelogs` | Lists time-log records logged by a specific contact. |
| List Contacts | `listContacts` | Lists all contacts (users and user groups) in the current Wrike account. |
| List Custom Fields | `listCustomFields` | Lists all custom fields defined in the account. |
| List Folder Attachments | `listFolderAttachments` | Lists attachments on a specific folder or project. |
| List Folder Comments | `listFolderComments` | Lists all comments on a specific folder or project. |
| List Folder Subtree | `listFolderSubtree` | Lists the folders/projects contained within a given folder (its subtree). |
| List Folder Tasks | `listFolderTasks` | Lists tasks within a specific folder or project. |
| List Folder Timelogs | `listFolderTimelogs` | Lists time-log records within a specific folder or project. |
| List Folders | `listFolders` | Lists all folders and projects in the account tree. |
| List Groups | `listGroups` | Lists all user groups in the account. |
| List Invitations | `listInvitations` | Lists all pending user invitations in the account. |
| List Space Folders | `listSpaceFolders` | Lists the folders/projects within a space. |
| List Space Tasks | `listSpaceTasks` | Lists tasks within a specific space. |
| List Spaces | `listSpaces` | Lists all spaces the current user can access. |
| List Task Approvals | `listTaskApprovals` | Lists approvals on a specific task. |
| List Task Attachments | `listTaskAttachments` | Lists attachments on a specific task. |
| List Task Comments | `listTaskComments` | Lists all comments on a specific task. |
| List Task Dependencies | `listTaskDependencies` | Lists all dependencies of a task. |
| List Task Timelogs | `listTaskTimelogs` | Lists time-log records on a specific task. |
| List Tasks | `listTasks` | Lists tasks across the account with optional filters. |
| List Timelog Categories | `listTimelogCategories` | Lists all time-log categories defined in the account. |
| List Timelogs | `listTimelogs` | Lists all time-log records in the account. |
| List Webhooks | `listWebhooks` | Lists all webhooks registered for the account. |
| List Workflows | `listWorkflows` | Lists all workflows and their custom statuses for the account. |
| Modify Approval | `modifyApproval` | Updates an approval: change its due date, or add and remove approvers. Note that the Wrike API does not accept status changes on this endpoint; use Delete Approval to remove an approval. |
| Modify Comment | `modifyComment` | Updates the text of an existing comment (author only, within 5 minutes). |
| Modify Contact | `modifyContact` | Updates a contact. Only the current user's own contact can be modified unless the caller is an account admin. |
| Modify Custom Field | `modifyCustomField` | Updates a custom field's title, type, scope, or settings. |
| Modify Dependency | `modifyDependency` | Updates a dependency's relation type or lag time. |
| Modify Folder | `modifyFolder` | Updates a folder or project: title, description, sharing, custom fields, or project settings. |
| Modify Group | `modifyGroup` | Updates a user group's title, members, parents, or metadata. |
| Modify Invitation | `modifyInvitation` | Resends an invitation or updates its role. |
| Modify Space | `modifySpace` | Updates a space's title, description, access type, members, or archived state. |
| Modify Task | `modifyTask` | Updates a task's fields such as title, description, status, dates, or responsibles. |
| Modify Timelog | `modifyTimelog` | Updates a time-log record's hours, date, comment, or category. |
| Modify Webhook | `modifyWebhook` | Suspends or resumes a webhook by changing its status. |
| Modify Workflow | `modifyWorkflow` | Updates a workflow's name, hidden state, or a custom status. |

</details>
