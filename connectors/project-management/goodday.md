---
description: "GoodDay work management platform — projects, tasks, users, time reports, events, custom fields, CRM, expenses, attendance, dependencies and documents via the…"
hidden: true
---

# GoodDay

GoodDay work management platform — projects, tasks, users, time reports, events, custom fields, CRM, expenses, attendance, dependencies and documents via the GoodDay API v2.0 (https://api.goodday.work/2.0).

| | |
| --- | --- |
| **Category** | [Project management](README.md) |
| **Website** | [goodday.work](https://goodday.work) |
| **Authentication** | API key |
| **Actions** | 73 |
| **Events** | 0 |
| **Slug** | `goodday` |

## Use it

Add GoodDay from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.goodday.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Task Comment | `addTaskComment` | Add a comment/message to a task. |
| Add Task Tag | `addTaskTag` | Add a tag to a task. |
| Add User To Project | `addProjectUser` | Give a company member access to a project at a chosen access level. For a project inside a workspace the member must already belong to that workspace. |
| Clock In | `clockIn` | Record a clock-in attendance event for a user. |
| Clock Out | `clockOut` | Record a clock-out attendance event for a user. |
| Create Attachment Upload URLs | `createAttachmentUploadUrls` | Reserve temporary upload URLs for up to 20 files and return the file identifiers used in the attachments array of a task, comment or reply. Upload each file with a PUT to its returned URL within one hour before referencing it. |
| Create Attendance Record | `createAttendanceRecord` | Create a complete attendance record with clock-in and clock-out timestamps for a user. |
| Create CRM Account | `createCrmAccount` | Create a CRM account. |
| Create CRM Contact | `createCrmContact` | Create a CRM contact. |
| Create Dependency | `createDependency` | Create a dependency between tasks, events or projects. Provide predecessor and successor IDs of the relevant type. |
| Create Event | `createEvent` | Create a calendar event (personal or project event). |
| Create Expense | `createExpense` | Create a project expense, optionally linked to a task. |
| Create Folder | `createFolder` | Create a new folder (folder-type project) under an optional parent project. |
| Create Project | `createProject` | Create a new project from a project template under an optional parent project. |
| Create Task | `createTask` | Create a new task in a project, optionally assigned to a user with a message, dates and a to-do list. |
| Create Time Report | `createTimeReport` | Log a time report (timelog) against a task for a user. |
| Delete Attendance Event | `deleteAttendanceEvent` | Delete an attendance event by ID. |
| Delete CRM Account | `deleteCrmAccount` | Delete a CRM account by ID. |
| Delete CRM Contact | `deleteCrmContact` | Delete a CRM contact by ID. |
| Delete Dependency | `deleteDependency` | Delete a dependency by ID. |
| Delete Event | `deleteEvent` | Delete an event by ID. |
| Delete Task | `deleteTask` | Delete a task and all of its related data. |
| Delete Time Report | `deleteTimeReport` | Delete a time report by ID. |
| Get CRM Account | `getCrmAccount` | Get a single CRM account by ID, including its contacts. |
| Get CRM Contact | `getCrmContact` | Get a single CRM contact by ID, including its related tasks. |
| Get Document | `getDocument` | Get a single document by ID, including plain and rich-text content. |
| Get Event | `getEvent` | Get a single event by ID. |
| Get Expense | `getExpense` | Get a single expense by ID. |
| Get Project | `getProject` | Get a single project by ID, including its settings (work items, task custom fields, custom workflow, task types). |
| Get Project History | `getProjectHistory` | Get the activity/history events for a project. |
| Get Project Snapshot | `getProjectSnapshot` | Get a single project snapshot by its identifier, including the captured snapshot data. |
| Get Task | `getTask` | Get full details of a single task including subtasks, custom fields and form submissions. |
| Get User | `getUser` | Get a single organization user by ID. |
| Get User Hourly Rate History | `getUserHourlyRateHistory` | Get the historical labor and service rates for a user. |
| List All Time Reports | `listAllTimeReports` | List all time reports across the organization within a required date range, optionally filtered by projects and users. |
| List Attendance Events | `listAttendanceEvents` | List attendance events within a required date range, optionally filtered by user(s). |
| List CRM Accounts | `listCrmAccounts` | List all CRM accounts. |
| List CRM Contacts | `listCrmContacts` | List all CRM contacts. |
| List Custom Fields | `listCustomFields` | List all custom field definitions in the organization. |
| List Event Dependencies | `listEventDependencies` | List predecessor and successor dependencies for an event. |
| List Events | `listEvents` | List calendar events within a required date range, optionally filtered by event types. |
| List Expense Categories | `listExpenseCategories` | List all expense categories defined in the organization. |
| List Offices | `listOffices` | List all offices defined in the organization. |
| List Project Dependencies | `listProjectDependencies` | List predecessor and successor dependencies for a project. |
| List Project Documents | `listProjectDocuments` | List documents in a project, optionally including subfolders. |
| List Project Expenses | `listProjectExpenses` | List expenses for a project. |
| List Project Snapshots | `listProjectSnapshots` | List the Gantt snapshots captured for a project, optionally including each snapshot's full data payload. |
| List Project Tasks | `listProjectTasks` | List tasks in a project. Optionally include closed tasks and tasks from subfolders. |
| List Project Time Reports | `listProjectTimeReports` | List time reports for a project, optionally including subfolders and filtered by date range. |
| List Project Users | `listProjectUsers` | List users who have access to a project. |
| List Projects | `listProjects` | List all projects in the organization. Optionally include archived projects and restrict to root-level projects. |
| List Skills | `listSkills` | List all skills defined in the organization. |
| List Statuses | `listStatuses` | List all task/project statuses defined in the organization. |
| List Tag Tasks | `listTagTasks` | List every task carrying a given tag, optionally including closed tasks. |
| List Task Dependencies | `listTaskDependencies` | List predecessor and successor dependencies for a task. |
| List Task Messages | `listTaskMessages` | List comments/messages on a task. |
| List Task Time Reports | `listTaskTimeReports` | List time reports for a task, optionally including subtasks and filtered by date range. |
| List Task Types | `listTaskTypes` | List all task types defined in the organization. |
| List User Action Required Tasks | `listUserActionRequiredTasks` | List tasks that require action from a specific user. |
| List User Assigned Tasks | `listUserAssignedTasks` | List tasks assigned to a specific user. Optionally include closed tasks. |
| List User Time Reports | `listUserTimeReports` | List time reports submitted by a user within an optional date range. |
| List Users | `listUsers` | List all users in the organization. Optionally include deleted users. |
| Remove Task Tag | `removeTaskTag` | Remove a tag from a task. |
| Remove User From Project | `removeProjectUser` | Remove a member from a project and reassign the work they own to the project owner. The project owner cannot be removed, nor can members of public projects or members inherited from a parent project or team. |
| Reply To Task | `replyToTask` | Reply to a task and change the action-required user, optionally with a message. |
| Update CRM Account | `updateCrmAccount` | Update a CRM account. |
| Update CRM Contact | `updateCrmContact` | Update a CRM contact. |
| Update Project | `updateProject` | Update an existing project's attributes such as name, dates, owner, status and progress. |
| Update Project Custom Fields | `updateProjectCustomFields` | Set custom field values on a project. Pass an array of {id, value} objects; use null value to reset a field. |
| Update Project User Access | `updateProjectUserAccess` | Change a member's access level on a project. Moving a member to a read-only level unassigns or reassigns the work they own in that project. |
| Update Task | `updateTask` | Update a task's attributes such as title, project, dates, priority, progress and assignee. Also used to link CRM contacts/account. |
| Update Task Custom Fields | `updateTaskCustomFields` | Set custom field values on a task. Pass an array of {id, value} objects; use null value to reset a field. |
| Update Task Status | `updateTaskStatus` | Change a task's status, optionally with a message. |
