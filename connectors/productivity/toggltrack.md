---
description: "Toggl Track time tracking API."
hidden: true
---

# Toggl Track

<img src="../../.gitbook/assets/connectors/lg/toggltrack.png" alt="Toggl Track logo">

Toggl Track time tracking API. Manage time entries (including the running entry, start/stop and bulk edits), projects, project users and groups, tasks, clients, tags, workspaces, workspace users and memberships, organizations, groups, invitations, goals, alerts, favorites, timesheets and saved reports, and run detailed, summary, weekly and comparative reports through the Reports API v3, plus webhook subscription management.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [toggl.com](https://toggl.com) |
| **Authentication** | Basic auth |
| **Slug** | `toggltrack` |

## Use it

Add Toggl Track from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.toggltrack.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Project Group | `addProjectGroup` | Assigns a group to a project in the workspace. |
| Add Project User | `addProjectUser` | Assigns a user to a project in the workspace. |
| Archive Client | `archiveClient` | Archives the client in the specified workspace. |
| Bulk Archive Clients | `bulkArchiveClients` | Archives multiple clients in a single request. |
| Bulk Delete Clients | `bulkDeleteClients` | Deletes multiple clients in a single request in the specified workspace. |
| Bulk Delete Saved Reports | `bulkDeleteSavedReports` | Deletes multiple saved reports in a single request in the specified workspace. |
| Bulk Delete Tags | `bulkDeleteTags` | Deletes multiple tags in a single request in the specified workspace. |
| Bulk Update Project Users | `bulkUpdateProjectUsers` | Applies changes to multiple project user assignments in a single request. |
| Bulk Update Projects | `bulkUpdateProjects` | Updates multiple projects in a single request in the specified workspace. |
| Bulk Update Tasks | `bulkUpdateTasks` | Updates multiple tasks in a single request in the specified workspace. |

<details>

<summary>See 237 more actions</summary>

* **Bulk Update Time Entries** `bulkUpdateTimeEntries`: Updates multiple time entries in a single request in the specified workspace.
* **Bulk Update Timesheets** `bulkUpdateTimesheets`: Updates a batch of timesheets in a single request.
* **Check Session Logged In** `checkLoggedIn`: Checks whether the current credentials correspond to a valid, logged-in session.
* **Create Alert** `createAlert`: Creates a new alert in the specified workspace.
* **Create Client** `createClient`: Creates a new client in the specified workspace.
* **Create Goal** `createGoal`: Creates a new goal in the specified workspace.
* **Create Invoice** `createInvoice`: Creates a new invoice in the specified workspace.
* **Create My Favorite** `createMyFavorite`: Creates a favorite time entry template for the authenticated user.
* **Create Organization Group** `createOrganizationGroup`: Creates a new organization group in the specified organization.
* **Create Organization Invitation** `createOrganizationInvitation`: Creates a new invitation for the user.
* **Create Ownership Transfer** `createOwnershipTransfer`: Creates new ownership transfer process.
* **Create Project** `createProject`: Creates a new project in the specified workspace.
* **Create Rate** `createRate`: Creates a new rate in the specified workspace.
* **Create Saved Report** `createSavedReport`: Creates a new saved report in the specified workspace.
* **Create Scheduled Report** `createScheduledReport`: Creates a new scheduled report in the specified workspace.
* **Create Tag** `createTag`: Creates a new tag in the specified workspace.
* **Create Task** `createTask`: Creates a new task in the specified workspace.
* **Create Time Entry** `createTimeEntry`: Creates a new time entry in the specified workspace.
* **Create Timesheet Setup** `createTimesheetSetup`: Creates a new timesheet setup in the specified workspace.
* **Create Tracking Reminder** `createTrackReminder`: Creates a new tracking reminder in the specified workspace.
* **Create Webhook Subscription** `createWebhookSubscription`: Creates a new webhook subscription in the specified workspace.
* **Create Workspace** `createWorkspace`: Creates a new workspace inside the specified organization.
* **Create Workspace Favorite** `createWorkspaceFavorite`: Creates a new workspace favorite in the specified workspace.
* **Delete Alert** `deleteAlert`: Deletes the alert in the specified workspace.
* **Delete Calendar Integration** `deleteCalendarIntegration`: Deletes the calendar integration.
* **Delete Client** `deleteClient`: Deletes the client in the specified workspace.
* **Delete Goal** `deleteGoal`: Deletes the goal in the specified workspace.
* **Delete Invoice** `deleteInvoice`: Deletes the invoice in the specified workspace.
* **Delete My Favorite** `deleteMyFavorite`: Deletes one of the authenticated user's favorite time entry templates.
* **Delete Organization Group** `deleteOrganizationGroup`: Deletes the organization group in the specified organization.
* **Delete Project** `deleteProject`: Deletes the project in the specified workspace.
* **Delete Project Group** `deleteProjectGroup`: Deletes the project group in the specified workspace.
* **Delete Project User** `deleteProjectUser`: Removes a user's assignment from a project.
* **Delete Saved Report** `deleteSavedReport`: Deletes the saved report in the specified workspace.
* **Delete Scheduled Report** `deleteScheduledReport`: Deletes the scheduled report in the specified workspace.
* **Delete Tag** `deleteTag`: Deletes the tag in the specified workspace.
* **Delete Task** `deleteTask`: Deletes the task in the specified workspace.
* **Delete Time Entry** `deleteTimeEntry`: Deletes the time entry in the specified workspace.
* **Delete Timesheet Setup** `deleteTimesheetSetup`: Deletes the timesheet setup in the specified workspace.
* **Delete Tracking Reminder** `deleteTrackReminder`: Deletes the tracking reminder in the specified workspace.
* **Delete Webhook Subscription** `deleteWebhookSubscription`: Deletes the webhook subscription in the specified workspace.
* **Delete Workspace Favorite** `deleteWorkspaceFavorite`: Deletes the workspace favorite in the specified workspace.
* **Delete Workspace Logo** `deleteWorkspaceLogo`: Deletes the workspace logo in the specified workspace.
* **Delete Workspace Membership** `deleteWorkspaceMembership`: Removes a user's membership from a workspace.
* **Get API Quota** `getMyQuota`: Retrieves the API request quota and current usage for the authenticated user.
* **Get API Status** `getApiStatus`: Retrieves the availability status of the Toggl Track API.
* **Get Calendar Integration Setup URL** `getCalendarSetupUrl`: Get URL for setting up a calendar integration with given provider.
* **Get Client** `getClient`: Retrieves the client in the specified workspace.
* **Get Client Data Trends** `getClientDataTrends`: Retrieves the client data trends in the specified workspace.
* **Get Current User** `getMe`: Retrieves the profile of the authenticated Toggl Track user, including the default workspace, timezone and account identifiers.
* **Get Current User ID** `getMyUserId`: Retrieves the numeric ID of the authenticated user.
* **Get Current User Location** `getMyLocation`: Retrieves the last known location of the authenticated user, derived from the request IP address.
* **Get Dashboard All Activity** `getDashboardAllActivity`: Get last activity for every workspace user.
* **Get Dashboard Most Active Users** `getDashboardMostActiveUsers`: Retrieves the dashboard most active users in the specified workspace.
* **Get Dashboard Top Activities** `getDashboardTopActivities`: Retrieves the dashboard top activities in the specified workspace.
* **Get Detailed Report Totals** `getDetailedReportTotals`: Retrieves the detailed report totals in the specified workspace.
* **Get Goal** `getGoal`: Retrieves the goal in the specified workspace.
* **Get Insights Project Data Trends** `getInsightsProjectDataTrends`: Retrieves project data trends from the Toggl Track Insights API.
* **Get Invitation** `getInvitation`: Retrieves the details of an organization invitation by its invitation code.
* **Get My Time Entry** `getMyTimeEntry`: Retrieves a single time entry belonging to the authenticated user by its ID.
* **Get Organization** `getOrganization`: Retrieves a single organization by its ID.
* **Get Organization Owner** `getOrganizationOwner`: Get owner of the organization.
* **Get Organization Plan** `getOrganizationPlan`: Retrieves the organization plan in the specified organization.
* **Get Organization Segmentation** `getOrganizationSegmentation`: Retrieves the organization segmentation in the specified organization.
* **Get Organization Subscription** `getOrganizationSubscription`: Retrieves the organization subscription in the specified organization.
* **Get Organization Workspaces Statistics** `getOrganizationWorkspacesStatistics`: Statistics for all workspaces in the organization.
* **Get Ownership Transfer** `getOwnershipTransfer`: Returns single organization transfer in the organization.
* **Get Project** `getProject`: Retrieves the project in the specified workspace.
* **Get Project Data Trends** `getProjectDataTrends`: Retrieves the project data trends in the specified workspace.
* **Get Project Statistics** `getProjectStatistics`: Retrieves the project statistics in the specified workspace.
* **Get Projects Billable Amounts** `getProjectsBillableAmounts`: Retrieves the projects billable amounts in the specified workspace.
* **Get Projects Task Count** `getProjectsTaskCount`: Retrieves the projects task count in the specified workspace.
* **Get Projects User Count** `getProjectsUserCount`: Retrieves the projects user count in the specified workspace.
* **Get Running Time Entry** `getRunningTimeEntry`: Retrieves the time entry currently running for the authenticated user, or null when the timer is stopped.
* **Get Saved Report** `getSavedReport`: Retrieves the saved report in the specified workspace.
* **Get Subscription Invoice Summary** `getSubscriptionInvoiceSummary`: Retrieves the subscription invoice summary in the specified organization.
* **Get Subscription Payment Failure** `getSubscriptionPaymentFailure`: Retrieves the subscription payment failure in the specified organization.
* **Get Task** `getTask`: Retrieves the task in the specified workspace.
* **Get Time Entries Checklist** `getTimeEntriesChecklist`: Retrieves the authenticated user's time tracking checklist.
* **Get Timesheet History** `getTimesheetHistory`: Retrieves the timesheet history in the specified workspace.
* **Get Timesheet Hours** `getTimesheetHours`: Retrieves the timesheet hours in the specified workspace.
* **Get User Data Trends** `getUserDataTrends`: Retrieves the user data trends in the specified workspace.
* **Get User Preferences** `getMyPreferences`: Retrieves the application preferences of the authenticated user.
* **Get User Preferences For Client** `getMyPreferencesForClient`: Retrieves the authenticated user's preferences for a specific Toggl Track client application.
* **Get Web Timer Data** `getWebTimer`: Retrieves the data used by the Toggl Track web timer for the authenticated user.
* **Get Webhook Limits** `getWebhookLimits`: Returns the webhook limits for the specified workspace ID.
* **Get Webhooks Service Status** `getWebhooksStatus`: Retrieves the availability status of the Toggl Track webhooks service.
* **Get Workspace** `getWorkspace`: Retrieves a single workspace by its ID.
* **Get Workspace Logo** `getWorkspaceLogo`: Retrieves the workspace logo image.
* **Get Workspace Preferences** `getWorkspacePreferences`: Retrieves the workspace preferences in the specified workspace.
* **Get Workspace Statistics** `getWorkspaceStatistics`: Retrieves the workspace statistics in the specified workspace.
* **Get Workspace Subscription** `getWorkspaceSubscription`: Retrieves the workspace subscription in the specified workspace.
* **Link SSO Profile** `linkSsoProfile`: Link SSO profile to a workspace.
* **List Alerts** `listAlerts`: Retrieves alerts in the specified workspace.
* **List All Calendars** `listAllCalendars`: Get all calendars for a given user.
* **List Calendar Event Attendees** `listCalendarEventAttendees`: Get all attendees for a given calendar event.
* **List Calendar Events** `listCalendarEvents`: Get all events for the caller user.
* **List Calendar Events By Calendar** `listCalendarEventsByCalendar`: Retrieves the events of a calendar within an integration. Deprecated by Toggl Track in favour of List Calendar Events.
* **List Calendar Integrations** `listCalendarIntegrations`: Get all integrations a user has.
* **List Clients** `listClients`: Retrieves clients in the specified workspace.
* **List Clients By ID** `listClientsById`: Retrieves the clients matching the given client IDs.
* **List Countries** `listCountries`: Retrieves the list of countries known to Toggl Track.
* **List Country Subdivisions** `listCountrySubdivisions`: Retrieves the administrative subdivisions of a country.
* **List Currencies** `listCurrencies`: Retrieves the currencies supported by Toggl Track.
* **List Enabled Features** `listMyFeatures`: Retrieves the feature set enabled for the authenticated user's workspaces.
* **List Expenses** `listExpenses`: Retrieves expenses in the specified workspace.
* **List Goals** `listGoals`: Get a list of goals.
* **List Integration Calendars** `listIntegrationCalendars`: Get all calendars for a given integration.
* **List Invoices** `listInvoices`: Retrieves invoices in the specified workspace.
* **List Linked SSO Profiles** `listLinkedSsoProfiles`: Get linked SSO profiles for a workspace.
* **List My Clients** `listMyClients`: Retrieves all clients visible to the authenticated user across their workspaces.
* **List My Favorites** `listMyFavorites`: Retrieves the authenticated user's favorite time entry templates.
* **List My Organizations** `listMyOrganizations`: Retrieves all organizations the authenticated user is a member of.
* **List My Projects** `listMyProjects`: Retrieves all projects visible to the authenticated user across their workspaces.
* **List My Projects Paginated** `listMyProjectsPaginated`: Retrieves the authenticated user's projects in pages, using a start project ID cursor.
* **List My Tags** `listMyTags`: Retrieves all tags visible to the authenticated user across their workspaces.
* **List My Tasks** `listMyTasks`: Retrieves all tasks visible to the authenticated user across their workspaces.
* **List My Time Entries** `listMyTimeEntries`: Retrieves the authenticated user's time entries within an optional date range.
* **List My Timesheets** `listMyTimesheets`: Retrieves the authenticated user's timesheets.
* **List My Tracking Reminders** `listMyTrackReminders`: Retrieves the tracking reminders configured for the authenticated user.
* **List My Workspaces** `listMyWorkspaces`: Retrieves all workspaces the authenticated user belongs to.
* **List Organization Groups** `listOrganizationGroups`: List of groups in organization with user and workspace assignments.
* **List Organization Payment Records** `listOrganizationPaymentRecords`: Retrieves organization payment records in the specified organization.
* **List Organization Plans** `listOrganizationPlans`: Retrieves organization plans in the specified organization.
* **List Organization Roles** `listOrganizationRoles`: Retrieves organization roles in the specified organization.
* **List Organization Users** `listOrganizationUsers`: List of users in organization.
* **List Organization Users Detailed** `listOrganizationUsersDetailed`: List of users in organization with details.
* **List Organization Workspace Users** `listOrganizationWorkspaceUsers`: List of users who belong to the given workspace.
* **List Ownership Transfers** `listOwnershipTransfers`: Returns list of organization transfers made in the organization.
* **List Project Groups** `listProjectGroups`: Retrieves project groups in the specified workspace.
* **List Project Tasks** `listProjectTasks`: Retrieves project tasks in the specified workspace.
* **List Project Templates** `listProjectTemplates`: Retrieves project templates in the specified workspace.
* **List Project Users** `listProjectUsers`: Retrieves project users in the specified workspace.
* **List Project Users Paginated** `listProjectUsersPaginated`: Retrieves the project user assignments of a workspace in pages.
* **List Projects** `listProjects`: Retrieves projects in the specified workspace.
* **List Public Workspace Plans** `listPublicWorkspacePlans`: Retrieves the publicly available workspace subscription plans.
* **List Rates** `listRates`: Retrieves rates in the specified workspace.
* **List Recurring Project Periods** `listRecurringProjectPeriods`: Retrieves recurring project periods in the specified workspace.
* **List Report Client Filters** `listReportClientFilters`: Retrieves report client filters in the specified workspace.
* **List Report Project Filters** `listReportProjectFilters`: Retrieves report project filters in the specified workspace.
* **List Report Project Group Filters** `listReportProjectGroupFilters`: Retrieves report project group filters in the specified workspace.
* **List Report Project Statuses** `listReportProjectStatuses`: Retrieves report project statuses in the specified workspace.
* **List Report Project User Filters** `listReportProjectUserFilters`: Retrieves report project user filters in the specified workspace.
* **List Report Task Statuses** `listReportTaskStatuses`: Retrieves report task statuses in the specified workspace.
* **List Report Tasks** `listReportTasks`: Retrieves report tasks in the specified workspace.
* **List Report User Filters** `listReportUserFilters`: Retrieves report user filters in the specified workspace.
* **List Saved Reports** `listSavedReports`: Retrieves saved reports in the specified workspace.
* **List Scheduled Reports** `listScheduledReports`: Retrieves scheduled reports in the specified workspace.
* **List Selected Calendars** `listSelectedCalendars`: Get all selected calendars for a given user.
* **List Subscription Plans** `listSubscriptionPlans`: Get all available plans and features.
* **List Tags** `listTags`: Retrieves tags in the specified workspace.
* **List Tasks By Project** `listTasksByProject`: Retrieves the tasks belonging to the given project IDs.
* **List Time Entries Shared With Me** `listTimeEntriesSharedWithMe`: Retrieves the time entries that other users have shared with the authenticated user.
* **List Time Entry Invitations** `listTimeEntryInvitations`: Retrieves time entry invitations in the specified workspace.
* **List Timesheet Setups** `listTimesheetSetups`: Retrieves timesheet setups in the specified workspace.
* **List Timesheet Time Entries** `listTimesheetTimeEntries`: Retrieves timesheet time entries in the specified workspace.
* **List Timesheets** `listTimesheets`: Retrieves timesheets in the specified workspace.
* **List Timezone Offsets** `listTimezoneOffsets`: Retrieves the UTC offsets for the timezones supported by Toggl Track.
* **List Timezones** `listTimezones`: Retrieves the list of timezones supported by Toggl Track.
* **List Tracking Reminders** `listTrackReminders`: Retrieves tracking reminders in the specified workspace.
* **List User Flags** `listMyFlags`: Retrieves the client-side flags stored for the authenticated user.
* **List Webhook Event Filters** `listWebhookEventFilters`: Retrieves the event filters supported by webhook subscriptions, listing every entity and action that can be subscribed to.
* **List Webhook Subscriptions** `listWebhookSubscriptions`: Retrieves existing subscriptions for the requested workspace ID.
* **List Workspace Currencies** `listWorkspaceCurrencies`: Retrieves workspace currencies in the specified workspace.
* **List Workspace Favorites** `listWorkspaceFavorites`: Get a list of favorites.
* **List Workspace Groups** `listWorkspaceGroups`: Retrieves workspace groups in the specified workspace.
* **List Workspace Groups In Organization** `listWorkspaceGroupsInOrganization`: List of groups in a workspace within an organization with user assignments.
* **List Workspace Memberships** `listWorkspaceMemberships`: Retrieves the workspace-user membership records of a workspace, including roles and rates.
* **List Workspace Tasks** `listWorkspaceTasks`: Retrieves all tasks across the projects of a workspace.
* **List Workspace Tasks Basic** `listWorkspaceTasksBasic`: Retrieves a lightweight list of all tasks in a workspace, returning only core fields.
* **List Workspace Users** `listWorkspaceUsers`: Retrieves workspace users in the specified workspace.
* **List Workspace Users Data** `listWorkspaceUsersData`: Retrieves detailed records for the given workspace user IDs.
* **Load Shared Report** `loadSharedReport`: Loads a previously saved report using its public share token.
* **Patch Organization Group** `patchOrganizationGroup`: Applies a partial update to the organization group in the specified organization.
* **Pin Project** `pinProject`: Pins the project in the specified workspace.
* **Ping Webhook Subscription** `pingWebhookSubscription`: Sends a test payload to a webhook subscription's callback URL.
* **Remove Organization Users** `bulkUpdateOrganizationUsers`: Removes one or more users from the organization in a single request. Supply the organization user IDs (not user IDs) to delete.
* **Remove Workspace Users** `changeOrganizationWorkspaceUsers`: Removes one or more users from a workspace within the organization in a single request. Supply the workspace user IDs to delete.
* **Request Feature Upgrade** `requestFeatureUpgrade`: Sends the organization's admins an upgrade request for a premium feature.
* **Resend Organization Invitation** `resendOrganizationInvitation`: Resends a pending organization invitation email to the invited user.
* **Reset Workspace iCal Token** `resetWorkspaceIcalToken`: Regenerates the workspace's iCal feed token, invalidating the previous feed URL.
* **Respond To Time Entry Invitation** `respondToTimeEntryInvitation`: Accepts or rejects a time entry sharing invitation.
* **Restore Client** `restoreClient`: Restores an archived client and its related projects.
* **Run Comparative Report** `runComparativeReport`: Runs comparative report in the specified workspace.
* **Run Detailed Report** `runDetailedReport`: Runs detailed report in the specified workspace.
* **Run Project Profitability Report** `runProjectProfitabilityReport`: Runs project profitability report in the specified workspace.
* **Run Project Summary Report** `runProjectSummaryReport`: Runs project summary report in the specified workspace.
* **Run Projects Summary Report** `runProjectsSummaryReport`: Runs projects summary report in the specified workspace.
* **Run Summary Report** `runSummaryReport`: Runs summary report in the specified workspace.
* **Run Weekly Report** `runWeeklyReport`: Runs weekly report in the specified workspace.
* **Search Report Clients** `searchReportClients`: Searches report clients in the specified workspace.
* **Search Report Projects** `searchReportProjects`: Searches report projects in the specified workspace.
* **Search Report Users** `searchReportUsers`: Searches report users in the specified workspace.
* **Select Calendar** `selectCalendar`: Sets whether a calendar is or not selected by the user.
* **Set User Flag** `setMyFlag`: Sets one flag (a key/value pair) for the authenticated user: adds the flag or overwrites its value. The value is stored as a string. Toggl documents limits of 32 characters per name, 64 per value, 4 flags per request and 128 in total. Toggl returns an empty reply and has no endpoint to delete a flag; use List My Flags to read flags back.
* **Set Webhook Subscription Enabled** `setWebhookSubscriptionEnabled`: Enables or disables an existing webhook subscription.
* **Stop Time Entry** `stopTimeEntry`: Stops the time entry in the specified workspace.
* **Suggest Details For Calendar Event** `suggestDetailsForCalendarEvent`: Get details suggestion for a given event.
* **Suggest Details For Calendar Events** `suggestDetailsForCalendarEvents`: Get details suggestion for given events.
* **Suggest My Favorites** `suggestMyFavorites`: Generates a list of suggested favorite time entry templates for the authenticated user.
* **Suggest Workspace Favorites** `suggestWorkspaceFavorites`: Generates and returns a list of suggested favorites.
* **Sync Calendar Events** `syncCalendarEvents`: Update all events from selected calendars for a user.
* **Sync Integration Calendars** `syncIntegrationCalendars`: Updates calendar data according to provider API.
* **Toggle Workspace iCal Token** `toggleWorkspaceIcalToken`: Enables or disables the workspace's iCal calendar feed.
* **Unlink SSO Profile** `unlinkSsoProfile`: Unlink the workspace from an SSO profile.
* **Update Alert** `updateAlert`: Updates the alert in the specified workspace.
* **Update Calendar Integration** `updateCalendarIntegration`: Updates the calendar integration.
* **Update Client** `updateClient`: Updates the client in the specified workspace.
* **Update Current User** `updateMe`: Updates the authenticated user's profile, such as full name, email, timezone or beginning of week.
* **Update Goal** `updateGoal`: Updates the goal in the specified workspace.
* **Update My Favorites** `updateMyFavorites`: Updates a batch of the authenticated user's favorite time entry templates.
* **Update Organization** `updateOrganization`: Updates an organization's details, such as its name.
* **Update Organization Group** `updateOrganizationGroup`: Updates the organization group in the specified organization.
* **Update Organization Segmentation** `updateOrganizationSegmentation`: Saves the organization segmentation (onboarding survey) answers for an organization. Send at least one survey field: a call with only the organization ID sends no body and Toggl rejects it with 'JSON is not valid'. Send null to clear a field.
* **Update Organization User** `updateOrganizationUser`: Updates the organization user in the specified organization.
* **Update Ownership Transfer** `updateOwnershipTransfer`: Updates transfer process and emails stakeholders.
* **Update Project** `updateProject`: Updates the project in the specified workspace.
* **Update Project User** `updateProjectUser`: Updates a project user assignment, such as its manager flag or hourly rate.
* **Update Saved Report** `updateSavedReport`: Updates the saved report in the specified workspace.
* **Update Saved Reports** `updateSavedReports`: Updates the saved reports in the specified workspace.
* **Update Tag** `updateTag`: Updates the tag in the specified workspace.
* **Update Task** `updateTask`: Updates the task in the specified workspace.
* **Update Time Entry** `updateTimeEntry`: Updates the time entry in the specified workspace.
* **Update Timesheet** `updateTimesheet`: Updates the timesheet in the specified workspace.
* **Update Timesheet Setup** `updateTimesheetSetup`: Updates the timesheet setup in the specified workspace.
* **Update Tracking Reminder** `updateTrackReminder`: Updates the tracking reminder in the specified workspace.
* **Update User Preferences** `updateMyPreferences`: Updates the application preferences of the authenticated user.
* **Update User Preferences For Client** `updateMyPreferencesForClient`: Updates the authenticated user's preferences for a specific Toggl Track client application.
* **Update Webhook Subscription** `updateWebhookSubscription`: Updates the webhook subscription in the specified workspace.
* **Update Workspace** `updateWorkspace`: Updates a workspace's settings, such as its name, default currency or billable defaults.
* **Update Workspace Favorite** `updateWorkspaceFavorites`: Updates a single favorite time entry template in the specified workspace.
* **Update Workspace Membership** `updateWorkspaceMembership`: Updates a workspace-user membership, such as its role or hourly rate.
* **Update Workspace Preferences** `updateWorkspacePreferences`: Updates the workspace preferences in the specified workspace.
* **Update Workspace User** `updateWorkspaceUser`: Updates the workspace user in the specified workspace.
* **Upload Expense** `uploadExpense`: Uploads a work expense record to the workspace.
* **Upload Workspace Logo** `uploadWorkspaceLogo`: Uploads a new logo image for the workspace.
* **Validate Webhook Subscription** `validateWebhookSubscription`: Confirms a webhook subscription by submitting the validation code Toggl Track sent to the callback URL.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Client Created | `client.created` | Maps to {"entity":"client","action":"created"}. |
| Client Deleted | `client.deleted` | Maps to {"entity":"client","action":"deleted"}. |
| Client Updated | `client.updated` | Maps to {"entity":"client","action":"updated"}. |
| Project Created | `project.created` | Maps to {"entity":"project","action":"created"}. |
| Project Deleted | `project.deleted` | Maps to {"entity":"project","action":"deleted"}. |
| Project Group Created | `project_group.created` | Maps to {"entity":"project_group","action":"created"}. |
| Project Group Deleted | `project_group.deleted` | Maps to {"entity":"project_group","action":"deleted"}. |
| Project Group Updated | `project_group.updated` | Maps to {"entity":"project_group","action":"updated"}. |
| Project Updated | `project.updated` | Maps to {"entity":"project","action":"updated"}. |
| Tag Created | `tag.created` | Maps to {"entity":"tag","action":"created"}. |

<details>

<summary>See 12 more events</summary>

* **Tag Deleted** `tag.deleted`: Maps to {"entity":"tag","action":"deleted"}.
* **Tag Updated** `tag.updated`: Maps to {"entity":"tag","action":"updated"}.
* **Task Created** `task.created`: Maps to {"entity":"task","action":"created"}. Note tasks are a paid Toggl feature; the free plan answers 403 "unauthorized to perform this action" on task writes.
* **Task Deleted** `task.deleted`: Maps to {"entity":"task","action":"deleted"}.
* **Task Updated** `task.updated`: Maps to {"entity":"task","action":"updated"}.
* **Time Entry Created** `time_entry.created`: Fires when a time entry is created in the subscribed workspace. Toggl subscriptions carry an event_filters array of {entity, action} pairs, so what a subscription receives is chosen at registration time. This event id maps to {"entity":"time_entry","action":"created"}. Verified live against workspace 21541382: subscription 127661 was created, its validate endpoint answered with the correct provider message for a wrong code, and delete returned the row - real integer subscription ids throughout, so unsubscribe genuinely removes rather than silently no-opping.
* **Time Entry Deleted** `time_entry.deleted`: Fires when a time entry is deleted. Maps to {"entity":"time_entry","action":"deleted"}.
* **Time Entry Updated** `time_entry.updated`: Fires when a time entry is updated. Maps to {"entity":"time_entry","action":"updated"}.
* **Workspace Updated** `workspace.updated`: Maps to {"entity":"workspace","action":"updated"}.
* **Workspace User Created** `workspace_user.created`: Maps to {"entity":"workspace_user","action":"created"}.
* **Workspace User Deleted** `workspace_user.deleted`: Maps to {"entity":"workspace_user","action":"deleted"}.
* **Workspace User Updated** `workspace_user.updated`: Maps to {"entity":"workspace_user","action":"updated"}.

</details>
