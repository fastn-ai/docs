---
description: "Clockify time-tracking integration."
hidden: true
---

# Clockify

<img src="../../.gitbook/assets/connectors/clockify.png" alt="Clockify logo" width="64">

Clockify time-tracking integration. Manage workspaces, users, user groups, projects, tasks, clients, tags, and time entries; run detailed, summary, and weekly reports; and manage webhooks for real-time event notifications.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [clockify.me](https://clockify.me) |
| **Authentication** | API key |
| **Slug** | `clockify` |

## Use it

Add Clockify from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clockify.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Time Entry For User | `addTimeEntryForUser` | Create a time entry on behalf of another user on the workspace. |
| Add User To User Group | `addUserToUserGroup` | Add a user to a user group. |
| Add User To Workspace | `addWorkspaceUser` | Invite a user to the workspace by email address. |
| Create Client | `createClient` | Create a new client on the workspace. |
| Create Expense Category | `createExpenseCategory` | Create a new expense category on the workspace. Requires a paid plan. |
| Create Holiday | `createHoliday` | Create a holiday on the workspace. Requires a paid plan. |
| Create Project | `createProject` | Create a new project on the workspace. |
| Create Tag | `createTag` | Create a new tag on the workspace. |
| Create Task | `createTask` | Create a new task on a project. |
| Create Time Entry | `createTimeEntry` | Create a new time entry on the workspace for the authenticated user. Provide only start to begin a running timer, or both start and end for a completed entry. |

<details>

<summary>See 64 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create User Group | `createUserGroup` | Create a new user group on the workspace. |
| Create Webhook | `createWebhook` | Create a webhook that sends real-time notifications to a URL when a subscribed event occurs. |
| Delete Client | `deleteClient` | Delete a client from the workspace. |
| Delete Project | `deleteProject` | Delete a project from the workspace. The project must be archived first. |
| Delete Shared Report | `deleteSharedReport` | Delete a shared report from a workspace. Uses the Clockify Reports API. |
| Delete Tag | `deleteTag` | Delete a tag from the workspace. |
| Delete Task | `deleteTask` | Delete a task from a project. |
| Delete Time Entry | `deleteTimeEntry` | Delete a time entry from the workspace. |
| Delete User Group | `deleteUserGroup` | Delete a user group from the workspace. |
| Delete Webhook | `deleteWebhook` | Delete a webhook from the workspace. |
| Generate Detailed Report | `detailedReport` | Generate a detailed report of individual time entries for a date range. Uses the Clockify Reports API. |
| Generate Summary Report | `summaryReport` | Generate a summary report grouped by project, client, user, or other dimensions. Uses the Clockify Reports API. |
| Generate Webhook Token | `generateWebhookToken` | Regenerate the signing token for a webhook. |
| Generate Weekly Report | `weeklyReport` | Generate a weekly report of tracked time. Uses the Clockify Reports API. |
| Get Client | `getClient` | Retrieve a single client by its id. |
| Get Current User | `getCurrentUser` | Retrieve the profile of the user whose API key is used, including id, email, name, and active workspace. |
| Get Member Profile | `getMemberProfile` | Retrieve the member profile of a user on a workspace. |
| Get Project | `getProject` | Retrieve a single project by its id. |
| Get Tag | `getTag` | Retrieve a single tag by its id. |
| Get Task | `getTask` | Retrieve a single task by its id. |
| Get Time Entry | `getTimeEntry` | Retrieve a single time entry by its id. |
| Get Time Off Policies | `getTimeOffPolicies` | Retrieve time off policies on a workspace. Requires a paid plan with the time off add-on. |
| Get Webhook | `getWebhook` | Retrieve a single webhook by its id. |
| Get Workspace | `getWorkspace` | Retrieve a single workspace by its id. |
| List Approval Requests | `listApprovals` | Retrieve timesheet approval requests on a workspace. Requires a paid plan. |
| List Clients | `listClients` | Retrieve all clients on a workspace. |
| List Expense Categories | `listExpenseCategories` | Retrieve expense categories on a workspace. Requires a paid plan. |
| List Expenses | `listExpenses` | Retrieve expenses on a workspace. Requires a paid plan. |
| List Holidays | `listHolidays` | Retrieve holidays configured on a workspace. Requires a paid plan. |
| List Invoices | `listInvoices` | Retrieve invoices on a workspace. Requires a paid plan. |
| List Project Custom Fields | `listProjectCustomFields` | Retrieve custom fields configured for a specific project. Requires a paid plan. |
| List Projects | `listProjects` | Retrieve all projects on a workspace, with optional name, archived, and billable filters. |
| List Shared Reports | `listSharedReports` | Retrieve shared reports on a workspace. Uses the Clockify Reports API. |
| List Tags | `listTags` | Retrieve all tags on a workspace. |
| List Tasks | `listTasks` | Retrieve all tasks for a project. |
| List Time Entries For User | `listTimeEntriesForUser` | Retrieve time entries for a specific user on a workspace, with optional date range and pagination filters. |
| List Time Off Requests | `getAllTimeOffRequests` | Retrieve time off requests on a workspace, optionally filtered by date range and status. Requires the time off add-on. |
| List User Groups | `listUserGroups` | Retrieve all user groups on a workspace. |
| List Webhooks | `listWebhooks` | Retrieve all webhooks created on a workspace by the authenticated user. |
| List Workspace Custom Fields | `listWorkspaceCustomFields` | Retrieve all custom fields defined on a workspace. Requires a paid plan. |
| List Workspace Users | `listWorkspaceUsers` | Retrieve all users on a workspace, with optional filters for email, status, and pagination. |
| List Workspaces | `listWorkspaces` | Retrieve all workspaces the authenticated user belongs to. |
| Mark Time Entries Invoiced | `markTimeEntriesInvoiced` | Mark a set of time entries as invoiced or not invoiced. |
| Remove Project Custom Field | `removeProjectCustomField` | Remove a custom field from a project. Requires a paid plan. |
| Remove User From User Group | `removeUserFromUserGroup` | Remove a user from a user group. |
| Remove User From Workspace | `removeWorkspaceUser` | Remove a user from the workspace. |
| Set User Custom Field Value | `setUserCustomFieldValue` | Set the value of a custom field for a user. Requires a paid plan. |
| Stop Running Timer | `stopTimer` | Stop the currently running timer for a user by setting its end time. |
| Submit Approval Request | `submitApprovalRequest` | Submit a timesheet approval request for the authenticated user for a given week. Requires a paid plan. |
| Update Approval Request | `updateApprovalRequest` | Approve, reject, or withdraw an approval request. Requires a paid plan. |
| Update Client | `updateClient` | Update an existing client. |
| Update Member Profile | `updateMemberProfile` | Update a member profile on a workspace (for example working hours or default project). |
| Update Project | `updateProject` | Update an existing project. |
| Update Project Custom Field | `updateProjectCustomField` | Update a custom field configuration on a project. Requires a paid plan. |
| Update Project Estimate | `updateProjectEstimate` | Update the time or budget estimate for a project. |
| Update Project Memberships | `updateProjectMemberships` | Update the member assignments on a project. |
| Update Tag | `updateTag` | Update an existing tag. |
| Update Task | `updateTask` | Update an existing task on a project. |
| Update Time Entry | `updateTimeEntry` | Update an existing time entry. Start is required by the API even for partial updates. |
| Update User Cost Rate | `updateUserCostRate` | Set the internal cost rate for a user on a workspace. Requires a paid plan. |
| Update User Group | `updateUserGroup` | Rename an existing user group. |
| Update User Hourly Rate | `updateUserHourlyRate` | Set the billable hourly rate for a user on a workspace. Requires a paid plan. |
| Update Webhook | `updateWebhook` | Update an existing webhook's name, URL, or subscribed event. |
| Update Workspace User Status | `updateWorkspaceUserStatus` | Activate or deactivate a user on the workspace. |

</details>
