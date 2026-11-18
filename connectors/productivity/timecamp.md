---
description: "TimeCamp time tracking and project management API."
hidden: true
---

# TimeCamp

<img src="../../.gitbook/assets/connectors/timecamp.png" alt="TimeCamp logo" width="64">

TimeCamp time tracking and project management API. Track time entries and timers, manage tasks and projects, users, groups and roles, computer activities, attendance and approvals, tags and tag lists, billing rates, expenses, custom fields, clients, invoices and data exports.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [timecamp.com](https://timecamp.com) |
| **Authentication** | Bearer token |
| **Slug** | `timecamp` |

## Use it

Add TimeCamp from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.timecamp.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Allowed Group to Tag | `addAllowedGroupToTag` | Grants a group permission to use a tag. |
| Add Favorite Task | `addFavoriteTask` | Adds a task to the user's list of favorite tasks. (TimeCamp API v3.) |
| Add Tags to Task | `addTagsToTask` | Assigns one or more tags to a task. |
| Add Tags to Time Entry | `addTagsToTimeEntry` | Assigns one or more tags to a time entry. |
| Archive Expense Category | `archiveExpenseCategory` | Archives an expense category so it can no longer be selected. (TimeCamp API v3.) |
| Archive Tasks | `archiveTasks` | Archives a batch of tasks. (TimeCamp API v3.) |
| Assign Custom Field Value | `assignCustomFieldValue` | Assigns a value for a custom field on a resource such as a task. (TimeCamp API v3.) |
| Assign Invoice to Expense | `assignInvoiceToExpense` | Links an invoice to one or more expenses. (TimeCamp API v3.) |
| Assign Tag List to Task | `assignTagListToTask` | Assigns a tag list to a task or updates an existing assignment. (TimeCamp API v3.) |
| Assign Users to Project | `assignUsersToProject` | Assigns one or more users to a project task. (TimeCamp API v3.) |

<details>

<summary>See 144 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Change Approval Status | `bulkChangeApprovalStatus` | Changes the status of multiple approvals at once. (TimeCamp API v3.) |
| Change Approval Status | `changeApprovalStatus` | Changes the status of a single approval, such as approving or rejecting it. (TimeCamp API v3.) |
| Change Task Parent | `changeTaskParent` | Moves a task under a different parent task. (TimeCamp API v3.) |
| Check Pending Attendance Requests | `hasPendingAttendanceRequests` | Checks whether the user has attendance requests awaiting a decision. |
| Control Timer | `controlTimer` | Starts, stops or checks the status of the user's timer. |
| Create Approval Message | `createApprovalMessage` | Adds a message to an approval. (TimeCamp API v3.) |
| Create Attendance Request | `createAttendanceRequest` | Creates a request for time off or an attendance correction. |
| Create Custom Field Template | `createCustomFieldTemplate` | Creates a new custom field template. (TimeCamp API v3.) |
| Create Expense | `createExpense` | Creates a new expense against a task. (TimeCamp API v3.) |
| Create Expense Category | `createExpenseCategory` | Creates a new expense category. (TimeCamp API v3.) |
| Create Export Request | `createExportRequest` | Requests a new data export for a dataset and date range. (TimeCamp API v3.) |
| Create Group | `createGroup` | Creates a new group under a parent group. |
| Create Predefined Days | `createPredefinedDays` | Creates predefined attendance days, such as public holidays, for a group. (TimeCamp API v3.) |
| Create Tag | `createTag` | Creates a new tag within a tag list. |
| Create Tag List | `createTagList` | Creates a new tag list. |
| Create Task | `createTask` | Creates a new task or project in the task tree. |
| Create Time Entry | `createTimeEntry` | Creates a time entry for a task on a given date. |
| Create Time Entry (v3) | `createTimeEntryV3` | Creates a time entry. (TimeCamp API v3.) |
| Create Time Entry Restriction | `createTimeEntryRestriction` | Creates a rule that restricts when time entries may be edited. (TimeCamp API v3.) |
| Create Time Tracking Role | `createTimeTrackingRole` | Creates a custom time tracking role with a permission set. |
| Delete Custom Field Template | `deleteCustomFieldTemplate` | Deletes a custom field template. (TimeCamp API v3.) |
| Delete Expense | `deleteExpense` | Deletes an expense by its ID. (TimeCamp API v3.) |
| Delete Expense Attachment | `deleteExpenseAttachment` | Deletes a file attached to an expense. (TimeCamp API v3.) |
| Delete Group | `deleteGroup` | Permanently deletes a group from the account. |
| Delete Group Scheduler | `deleteGroupScheduler` | Deletes the scheduled report configuration for a group. |
| Delete Group Setting | `deleteGroupSetting` | Deletes a named setting from a group. |
| Delete Task | `deleteTask` | Deletes a task by its ID. |
| Delete Time Entry | `deleteTimeEntry` | Deletes a single time entry by its ID. |
| Delete Time Entry (v3) | `deleteTimeEntryV3` | Deletes a time entry by its ID. (TimeCamp API v3.) |
| Delete Time Entry Restriction | `deleteTimeEntryRestriction` | Deletes a time entry restriction rule. (TimeCamp API v3.) |
| Delete Time Tracking Role | `deleteTimeTrackingRole` | Deletes a custom time tracking role. Returns an object keyed by ID, where each value is the corresponding record. |
| Delete Timer | `deleteTimer` | Deletes the currently running timer and discards its tracked time. |
| Delete User Setting | `deleteUserSetting` | Deletes a named setting from a user. |
| Detach Tag List from Task | `detachTagListFromTask` | Detaches a tag list from a task. (TimeCamp API v3.) |
| Download Storage File | `downloadStorageFile` | Downloads a file stored in TimeCamp by its ID. (TimeCamp API v3.) |
| Duplicate Task | `duplicateTask` | Duplicates a single task. (TimeCamp API v3.) |
| Duplicate Tasks | `duplicateTasks` | Duplicates a batch of tasks. (TimeCamp API v3.) |
| Get Approval | `getApproval` | Retrieves a single approval by its resource ID. (TimeCamp API v3.) |
| Get Current User | `getCurrentUser` | Retrieves the profile and permissions of the user who owns the API token. |
| Get Current User Settings | `getCurrentUserSettings` | Retrieves the full settings profile of the user who owns the API token, including time zone, language and tracking preferences. |
| Get Custom Field Value | `getCustomFieldValue` | Retrieves the value of a single custom field on a resource. (TimeCamp API v3.) |
| Get Data Export | `getDataExport` | Retrieves a single data export by its ID. (TimeCamp API v3.) |
| Get Group Billing Rate | `getGroupBillingRate` | Retrieves the billing rate configured for a group. Returns an object keyed by ID, where each value is the corresponding record. |
| Get Group Logo | `getGroupLogo` | Retrieves the company logo configured for a group. |
| Get Group Scheduler | `getGroupScheduler` | Retrieves the scheduled report configuration for a group. |
| Get Group Setting | `getGroupSetting` | Retrieves the value of a named setting for a group. |
| Get Logged Time in Week | `getLoggedTimeInWeek` | Retrieves the total time logged per day for a week. Returns an object keyed by ID, where each value is the corresponding record. |
| Get Running Timer | `getRunningTimer` | Retrieves information about the timer currently running for the user. |
| Get Tag | `getTag` | Retrieves a single tag by its ID. |
| Get Tag List | `getTagList` | Retrieves a tag list together with the tags it contains. |
| Get Task Billing Rate | `getTaskBillingRate` | Retrieves the billing rate configured for a task. Returns an object keyed by ID, where each value is the corresponding record. |
| Get Task User Billing Rate | `getTaskUserBillingRate` | Retrieves the billing rate for a specific user on a specific task. Returns an object keyed by ID, where each value is the corresponding record. |
| Get User Attendance | `getUserAttendance` | Retrieves attendance records for a single user within a date range. |
| Get User Billing Rate | `getUserBillingRate` | Retrieves the billing rate configured for a user. Returns an object keyed by ID, where each value is the corresponding record. |
| Get User by ID | `getUserById` | Retrieves a single user's profile by their user ID. |
| Get User Setting | `getUserSetting` | Retrieves the value of a named setting for a user. |
| Invite User to Group | `inviteUserToGroup` | Invites a user to join a group by email address. |
| List Approval Activities | `listApprovalActivities` | Lists the activity history recorded against an approval. (TimeCamp API v3.) |
| List Approval Users | `listApprovalUsers` | Lists the users whose timesheets the current user can approve. |
| List Approvals | `listApprovals` | Lists timesheet approvals for a date range. |
| List Attendance | `listAttendance` | Lists attendance records (clock in and out) within a date range. |
| List Available Attendance Day Types | `listAvailableDayTypes` | Lists all day types that can be assigned to attendance records. |
| List Away Time | `listAwayTime` | Lists periods of computer inactivity recorded for users within a date range. |
| List Clients | `listClients` | Lists the clients defined in the account. Clients are created in the TimeCamp web app. |
| List Computer Activities | `listComputerActivities` | Lists tracked computer application and website activity for a given date. |
| List Currencies | `listCurrencies` | Lists the currencies supported by TimeCamp for billing rates and invoicing. |
| List Custom Field Templates | `listCustomFieldTemplates` | Lists the custom field templates defined in the account. (TimeCamp API v3.) |
| List Custom Field Values | `listCustomFieldValues` | Lists the values of all custom fields on a resource. (TimeCamp API v3.) |
| List Data Exports | `listDataExports` | Lists the data exports requested for the account. (TimeCamp API v3.) |
| List Dataset Availability | `listDatasetAvailability` | Lists which datasets are available for export. (TimeCamp API v3.) |
| List Declared Attendance Day Types | `listAttendanceDayTypes` | Lists the day types, such as holiday or sick leave, declared by users within a timeframe. Returns an object keyed by ID, where each value is the corresponding record. |
| List Effective Predefined Days | `listEffectivePredefinedDays` | Lists the predefined attendance days that are effective for a group, including inherited ones. (TimeCamp API v3.) |
| List Expense Attachments | `listExpenseAttachments` | Lists the files attached to an expense. (TimeCamp API v3.) |
| List Expense Categories | `listExpenseCategories` | Lists the expense categories defined in the account. (TimeCamp API v3.) |
| List Expenses | `listExpenses` | Lists expenses, optionally filtered by task, category or date. (TimeCamp API v3.) |
| List Favorite Tasks | `listFavoriteTasks` | Lists the tasks the user marked as favorites. (TimeCamp API v3.) |
| List Group Users | `listGroupUsers` | Lists all users belonging to a group. |
| List Groups | `listGroups` | Lists all groups in the account, including their structure and settings. |
| List Invoices | `listInvoices` | Lists the invoices in the account. Invoicing is a paid TimeCamp feature and invoices are created in the TimeCamp web app. |
| List Open Data Exports | `listOpenDataExports` | Lists data exports that are still being generated. (TimeCamp API v3.) |
| List Predefined Days | `listPredefinedDays` | Lists the predefined attendance days, such as public holidays, assigned to a group. (TimeCamp API v3.) |
| List Project Assigned Users | `listProjectAssignedUsers` | Lists the users assigned to a project task. (TimeCamp API v3.) |
| List Projects | `listProjects` | Lists the project and task tree visible to the user. (TimeCamp API v3.) |
| List Rate Types | `listRateTypes` | Lists the billing rate types defined in the account, such as Cost and Income. Use the returned rateTypeId when saving billing rates. |
| List Storage Files | `listStorageFiles` | Lists the files stored in the user's main group. (TimeCamp API v3.) |
| List Tag Allowed Groups | `listTagAllowedGroups` | Lists the groups that are allowed to use a tag. Returns an object keyed by ID, where each value is the corresponding record. |
| List Tag Lists | `listTagLists` | Lists all tag lists defined in the account. Returns an object keyed by ID, where each value is the corresponding record. |
| List Tags in Tag List | `listTagsInTagList` | Lists only the tags belonging to a tag list. Returns an object keyed by ID, where each value is the corresponding record. |
| List Task Details | `listTaskDetails` | Lists extended detail fields for tasks, such as budgets and estimates. |
| List Tasks | `listTasks` | Lists tasks and projects in the account's task tree. Returns an object keyed by ID, where each value is the corresponding record. |
| List Taxes | `listTaxes` | Lists the tax rates defined in the account for invoicing. |
| List Time Entries | `listTimeEntries` | Lists time entries within a date range, optionally filtered by user or task. |
| List Time Entries (v3) | `listTimeEntriesV3` | Lists time entries visible to the user, with filtering and pagination. (TimeCamp API v3.) |
| List Time Entry Changes | `listTimeEntryChanges` | Lists time entries that were added or modified within a date range. |
| List Time Entry Deletions | `listTimeEntryDeletions` | Lists time entries that were deleted within a date range. |
| List Time Entry Restrictions | `listTimeEntryRestrictions` | Lists the rules that restrict when time entries may be edited. (TimeCamp API v3.) |
| List Time Entry Tags | `listTimeEntryTags` | Lists the tags assigned to a time entry. |
| List Time Tracking Roles | `listTimeTrackingRoles` | Lists the time tracking roles and their permission sets. Returns an object keyed by ID, where each value is the corresponding record. |
| List Tracked Applications | `listTrackedApplications` | Lists the applications recorded by the TimeCamp desktop tracker. |
| List Tracked Sites and Apps | `listSitesAndApps` | Lists the websites and applications recorded in the activity log. (TimeCamp API v3.) |
| List Users | `listUsers` | Lists all users in the account with their group membership and profile data. |
| Merge Time Entries | `mergeTimeEntries` | Merges two time entries into a single entry. |
| Move Task Worklogs | `moveTaskWorklogs` | Moves the time entries logged against a task to another task. (TimeCamp API v3.) |
| Remove Allowed Group from Tag | `removeAllowedGroupFromTag` | Revokes a group's permission to use a tag. |
| Remove Favorite Task | `removeFavoriteTask` | Removes a task from the user's list of favorite tasks. (TimeCamp API v3.) |
| Remove Predefined Day | `removePredefinedDay` | Removes a predefined attendance day from a group. (TimeCamp API v3.) |
| Remove Tags from Task | `removeTagsFromTask` | Removes one or more tags from a task. |
| Remove Tags from Time Entry | `removeTagsFromTimeEntry` | Removes one or more tags from a time entry. |
| Remove Tasks | `removeTasks` | Removes one or more tasks. (TimeCamp API v3.) |
| Remove User from Group | `removeUserFromGroup` | Removes a user from a group. |
| Restore Archived Tasks | `restoreArchivedTasks` | Restores a batch of archived tasks along with their parent tasks. (TimeCamp API v3.) |
| Save Approval | `saveApproval` | Creates or updates a timesheet approval for a user and period. |
| Save Group Billing Rate | `saveGroupBillingRate` | Creates or updates the billing rate for a group. |
| Save Group Scheduler | `saveGroupScheduler` | Creates or updates the scheduled report configuration for a group. |
| Save Task Billing Rate | `saveTaskBillingRate` | Creates or updates the billing rate for a task. |
| Save Task User Billing Rate | `saveTaskUserBillingRate` | Creates or updates the billing rate for a specific user on a specific task. |
| Save User Attendance | `saveUserAttendance` | Creates or updates attendance records for a user. |
| Save User Billing Rate | `saveUserBillingRate` | Creates or updates the billing rate for a user. |
| Search Approvals | `searchApprovals` | Searches timesheet approvals using a filter payload. (TimeCamp API v3.) |
| Search Attendance Calendar | `searchAttendanceCalendar` | Searches the attendance calendar for users over a date range. (TimeCamp API v3.) |
| Search Expenses | `searchExpenses` | Searches expenses using a filter payload. (TimeCamp API v3.) |
| Search Projects | `searchProjects` | Searches the project and task tree by name. (TimeCamp API v3.) |
| Search Time Entries | `searchTimeEntries` | Searches time entries visible to the user, with filtering and pagination. (TimeCamp API v3.) |
| Send Approval Reminder | `sendApprovalReminder` | Sends a reminder to users to submit their timesheet for approval. (TimeCamp API v3.) |
| Set Task Color | `setTaskColor` | Sets or changes the display color of a task. |
| Unassign Custom Field Value | `unassignCustomFieldValue` | Removes a custom field value from a resource. (TimeCamp API v3.) |
| Unassign Invoice from Expense | `unassignInvoiceFromExpense` | Removes the link between an invoice and an expense. (TimeCamp API v3.) |
| Unassign Users from Project | `unassignUsersFromProject` | Removes one or more users from a project task. (TimeCamp API v3.) |
| Update Custom Field Template | `updateCustomFieldTemplate` | Updates an existing custom field template. (TimeCamp API v3.) |
| Update Expense | `updateExpense` | Updates an existing expense. (TimeCamp API v3.) |
| Update Expense Category | `updateExpenseCategory` | Updates an expense category. (TimeCamp API v3.) |
| Update Group | `updateGroup` | Updates the name or parent of an existing group. |
| Update Group Setting | `updateGroupSetting` | Creates or updates a named setting for a group. |
| Update Group User | `updateGroupUser` | Updates a user's details or status within a group. |
| Update Tag | `updateTag` | Updates the name or properties of an existing tag. |
| Update Tag List | `updateTagList` | Updates the name or properties of an existing tag list. |
| Update Task | `updateTask` | Updates the name, parent, budget or other properties of a task. |
| Update Task Tag Assignment | `updateTaskTagAssignment` | Changes how tags are assigned to a task, such as making a tag list required. |
| Update Time Entry | `updateTimeEntry` | Updates an existing time entry. |
| Update Time Entry (v3) | `updateTimeEntryV3` | Updates an existing time entry by its ID. (TimeCamp API v3.) |
| Update Time Tracking Role | `updateTimeTrackingRole` | Updates the name or permissions of a time tracking role. Returns an object keyed by ID, where each value is the corresponding record. |
| Update User | `updateUser` | Updates the profile of a user in the account. |
| Update User Setting | `updateUserSetting` | Creates or updates a named setting for a user. |
| Upload Expense Attachment | `uploadExpenseAttachment` | Uploads a receipt or document file and attaches it to an expense. (TimeCamp API v3.) |

</details>
