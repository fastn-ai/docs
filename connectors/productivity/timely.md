---
description: "Timely automatic time tracking API."
hidden: true
---

# Timely

<img src="../../.gitbook/assets/connectors/lg/timely.png" alt="Timely logo">

Timely automatic time tracking API. Log and manage time entries and timers, plan and forecast tasks, organize projects, clients, teams and users, manage tags, capacities, roles, states and permissions, generate reports, run bulk imports, and subscribe to webhooks.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [timelyapp.com](https://timelyapp.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `timely` |

## Use it

Add Timely from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.timely.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Import Events | `bulkImportEvents` | Creates, updates or deletes up to 100 events in a single request. Requests with more than 20 records are processed asynchronously and return a job identifier. Supply at least one of create, update or delete. |
| Bulk Import Time Entries | `bulkImportTimeEntries` | Creates, updates or deletes up to 100 time entries in a single request. Requests with more than 20 records are processed asynchronously and return a job identifier. Supply at least one of create, update or delete. |
| Create Client | `createClient` | Creates a new client in the Timely account. |
| Create Day Properties | `createDayProperties` | Creates or updates day properties, such as marking days as holiday or time off. |
| Create Project | `createProject` | Creates a new project in the Timely account, optionally assigning it to a client and setting rates and budget. |
| Create State | `createState` | Creates a new custom state for the account. |
| Create State Permissions | `createStatePermissions` | Creates or updates the role permissions attached to a state. |
| Create Tag | `createTag` | Creates a new tag in the Timely account, optionally nested under a parent tag. |
| Create Task | `createTask` | Creates a new planned task (forecast) for a user and project over a date range. |
| Create Team | `createTeam` | Creates a new team in the Timely account with the given name and members. |

<details>

<summary>See 66 more actions</summary>

* **Create Time Entry** `createTimeEntry`: Creates a new time entry in the Timely account for a given project, user and day.
* **Create Time Entry State** `createTimeEntryState`: Creates a new custom time entry state for the account.
* **Create Webhook** `createWebhook`: Registers a new webhook that delivers Timely events to the given HTTPS endpoint.
* **Delete Project** `deleteProject`: Deletes a project from the Timely account.
* **Delete State** `deleteState`: Deletes a custom state from the account. The state is soft-deleted: it still appears in List States with the deleted flag set.
* **Delete State Permissions** `deleteStatePermissions`: Deletes a role permission from a state.
* **Delete Tag** `deleteTag`: Deletes a tag from the Timely account.
* **Delete Task** `deleteTask`: Deletes a planned task from the Timely account.
* **Delete Team** `deleteTeam`: Deletes a team from the Timely account.
* **Delete Time Entry** `deleteTimeEntry`: Permanently deletes a time entry from the Timely account.
* **Delete Time Entry State** `deleteTimeEntryState`: Deletes a custom time entry state from the account. The state is soft-deleted: it still appears in List Time Entry States with the deleted flag set.
* **Delete User** `deleteUser`: Removes a user from the Timely account.
* **Delete Webhook** `deleteWebhook`: Deletes a webhook from the Timely account so it stops receiving events.
* **Filter Reports** `filterReports`: Returns a filtered report breakdown for the account over a date range.
* **Get Client** `getClient`: Retrieves a single client by its unique identifier.
* **Get Current User** `getCurrentUser`: Retrieves the profile of the Timely user that the connection is authenticated as, including name, email, time zone and account role.
* **Get Current User Permissions** `getCurrentUserPermissions`: Lists the resource permissions granted to the user that the connection is authenticated as.
* **Get Identity** `getIdentity`: Retrieves the identity of the authenticated user, independent of any Timely account.
* **Get Project** `getProject`: Retrieves a single project by its unique identifier, including budget and rate details.
* **Get Report Totals** `getReportTotals`: Returns aggregated report totals for the account over a date range, optionally filtered by user, project or client.
* **Get Tag** `getTag`: Retrieves a single tag by its unique identifier.
* **Get Task** `getTask`: Retrieves a single planned task by its unique identifier.
* **Get Team** `getTeam`: Retrieves a single team by its unique identifier, including its members.
* **Get Time Entry** `getTimeEntry`: Retrieves a single time entry by its unique identifier.
* **Get Token Info** `getTokenInfo`: Returns information about the access token in use, including its scopes, application and resource owner.
* **Get User** `getUser`: Retrieves a single account user by their unique identifier.
* **Get User Capacities** `getUserCapacities`: Lists a specific user's working capacities, such as weekly and daily hours and work days.
* **Get User Day Properties** `getUserDayProperties`: Lists a specific user's day properties, such as holidays and time off.
* **Get User Permissions** `getUserPermissions`: Lists the resource permissions granted to a specific account user.
* **Get Webhook** `getWebhook`: Retrieves a single webhook by its unique identifier.
* **Introspect Access Token** `introspectAccessToken`: Introspects an OAuth access token and reports whether it is active, together with its scope and expiry.
* **Invite User** `inviteUser`: Invites a new user to the Timely account and sends them an invitation email. Supply either role_id or user_level: the account rejects the request when both are blank. If the email already exists, the user is re-invited with the updated settings.
* **List Accounts** `listAccounts`: Lists the Timely accounts (workspaces) that the authenticated user belongs to, including currency and logo details.
* **List Apps** `listApps`: Lists the third-party applications, such as calendars and project tools, that can be connected to the Timely account.
* **List Clients** `listClients`: Lists the clients of the Timely account, with optional paging and filtering by archived state.
* **List Day Properties** `listDayProperties`: Lists day properties such as holidays or time off for the account over a date range.
* **List Pinned Reports** `listPinnedReports`: Lists the reports that have been pinned in the Timely account.
* **List Projects** `listProjects`: Lists the projects in the Timely account, with optional filtering by state, relation and update time.
* **List Resource Permissions** `listResourcePermissions`: Lists the permissions defined for a given resource type in the account.
* **List Roles** `listRoles`: Lists the roles available in the Timely account, together with the scopes each role grants.
* **List States** `listStates`: Lists the states configured for the account, such as Billed, Approved or custom states. Deleted states are returned as well and are marked with the deleted flag.
* **List Tags** `listTags`: Lists the tags (labels) defined in the Timely account, including their nested child tags.
* **List Tasks** `listTasks`: Lists planned tasks (forecasts) in the Timely account, with optional filtering by date range, user and project.
* **List Teams** `listTeams`: Lists the teams defined in the Timely account.
* **List Time Entries** `listTimeEntries`: Lists time entries (hours) logged in the Timely account. Without a date range this returns only the current day; pass since and upto to query a wider period. Supports filtering by project, user and sorting.
* **List Time Entry States** `listTimeEntryStates`: Lists the time entry states configured for the account, such as Billed or Approved. Deleted states are returned as well and are marked with the deleted flag.
* **List Timesheet Proposals** `listTimesheetProposals`: Lists AutoSheet timesheet proposals generated for the Timely account.
* **List Users** `listUsers`: Lists the users who are members of the Timely account, including their roles and rates.
* **List Users Capacities** `listUsersCapacities`: Lists the working capacities of all users in the account, such as weekly and daily hours.
* **List Webhooks** `listWebhooks`: Lists the webhooks registered on the Timely account.
* **Patch Team** `patchTeam`: Partially updates an existing team, changing only the attributes supplied.
* **Search Teams** `searchTeams`: Searches the teams of the Timely account by name.
* **Search Users** `searchUsers`: Searches the users of the Timely account by name or email.
* **Start Timer** `startTimer`: Starts the running timer on an existing time entry.
* **Stop Timer** `stopTimer`: Stops the running timer on a time entry and records the elapsed duration.
* **Update Client** `updateClient`: Updates an existing client. Only the attributes supplied in the company object are changed.
* **Update Day Properties** `updateDayProperties`: Updates existing day properties for the account.
* **Update Project** `updateProject`: Updates an existing project. Only the attributes supplied in the project object are changed.
* **Update State** `updateState`: Updates an existing state.
* **Update Tag** `updateTag`: Updates an existing tag. Only the attributes supplied in the label object are changed.
* **Update Task** `updateTask`: Updates an existing planned task. Only the attributes supplied in the forecast object are changed.
* **Update Team** `updateTeam`: Replaces an existing team with the supplied attributes. Attributes that are omitted are cleared, including team members; use Patch Team for a partial update.
* **Update Time Entry** `updateTimeEntry`: Updates an existing time entry. Only the attributes supplied in the event object are changed.
* **Update Time Entry State** `updateTimeEntryState`: Updates an existing time entry state.
* **Update User** `updateUser`: Updates an existing account user, such as their name, role, rate or teams. Supply either role_id or user_level. This replaces the user record, so send the attributes you want to keep.
* **Update Webhook** `updateWebhook`: Updates an existing webhook, such as its target URL, subscriptions or active state.

</details>
