---
description: "Pipeline CRM (formerly PipelineDeals) is a sales CRM for small and mid-sized teams."
hidden: true
---

# Pipeline CRM

Pipeline CRM (formerly PipelineDeals) is a sales CRM for small and mid-sized teams. This connector wraps the Pipeline API v3 to manage deals, people, companies, activities, calendar entries, files, projects and milestones, saved searches, account notifications, admin settings such as stages, custom fields, tags, users and teams, and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [pipelinecrm.com](https://pipelinecrm.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 235 |
| **Events** | 9 |
| **Slug** | `pipelineCrm` |

## Use it

Add Pipeline CRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pipelineCrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Project Association | `addProjectAssociation` | Associates a deal, company or person with a Pipeline CRM project. Idempotent: adding an existing association returns it. |
| Archive Project | `archiveProject` | Archives a project in Pipeline CRM (PUT). Archived projects are excluded from default list queries. |
| Archive Project (PATCH) | `archiveProjectPatch` | Archives a project in Pipeline CRM using PATCH. Equivalent to archiveProject (PUT). |
| Autocomplete Project Milestones | `autocompleteProjectMilestones` | Returns project milestones in Pipeline CRM whose name matches the query, as a bare JSON array of {id, autocomplete_result, project_id, project_name}. A blank query returns an empty array. |
| Autocomplete Projects | `autocompleteProjects` | Returns projects in Pipeline CRM whose name matches the query string, as a bare JSON array of {id, autocomplete_result}. A blank query returns an empty array. |
| Bulk Update Project Milestones | `bulkUpdateProjectMilestones` | Performs a bulk action (delete) on multiple project milestones in Pipeline CRM. Large selections may run in the background. |
| Create Account Notification | `createAccountNotification` | Creates an account notification in Pipeline CRM. |
| Create Activity | `createActivity` | Creates an activity (note) in Pipeline CRM attached to a deal, company or person. |
| Create Calendar Entry | `createCalendarEntry` | Creates a calendar entry (CalendarTask or CalendarEvent) in Pipeline CRM. category_id is required by the backend. |
| Create Calendar Entry Priority | `createCalendarEntryPriority` | Creates a calendar event and task priority in Pipeline CRM. |
| Create Calendar Entry Status | `createCalendarEntryStatus` | Creates a custom calendar event/task status in Pipeline CRM. New custom statuses are inserted before the Done system status. |
| Create Comment | `createComment` | Creates a comment on an activity (note) in Pipeline CRM. |
| Create Company | `createCompany` | Creates a company in Pipeline CRM. Optionally applies a todo template and checks for duplicates. |
| Create Company Custom Field Group | `createCompanyCustomFieldGroup` | Creates a company custom field group in Pipeline CRM. |
| Create Company Custom Field Label | `createCompanyCustomFieldLabel` | Creates a company custom field label (custom field definition) in Pipeline CRM. |
| Create Company Tag | `createCompanyTag` | Creates a company tag in Pipeline CRM. |
| Create Custom Field Label Dropdown Entry | `createCustomFieldLabelDropdownEntry` | Creates a dropdown entry (option) for a dropdown or multi-select custom field label in Pipeline CRM. |
| Create Customer | `createCustomer` | Converts a company into a customer record in Pipeline CRM. Note: the vendor ignores health_score and health_score_description on create (verified live); set them afterwards with updateCustomer. |
| Create Deal | `createDeal` | Creates a deal in Pipeline CRM. Optionally applies a todo template. |
| Create Deal Custom Field Group | `createDealCustomFieldGroup` | Creates a deal custom field group in Pipeline CRM. |
| Create Deal Custom Field Label | `createDealCustomFieldLabel` | Creates a deal custom field label (custom field definition) in Pipeline CRM. |
| Create Deal Loss Reason | `createDealLossReason` | Creates a deal loss reason in Pipeline CRM. |
| Create Deal Stage | `createDealStage` | Creates a deal stage in a deal pipeline in Pipeline CRM. percent must be unique within the pipeline (the vendor returns 422 'Percent has already been taken' otherwise). |
| Create Deal Status | `createDealStatus` | Creates a deal status in Pipeline CRM. |
| Create Deal Tag | `createDealTag` | Creates a deal tag in Pipeline CRM. |
| Create Event Category | `createEventCategory` | Creates a calendar event/task category in Pipeline CRM. |
| Create File | `createFile` | Creates a file (document) in Pipeline CRM from a publicly accessible URL. Pipeline downloads the file from the URL asynchronously and reports progress in upload_status. |
| Create File Tag | `createFileTag` | Creates a file (document) tag in Pipeline CRM. |
| Create Lead Source | `createLeadSource` | Creates a lead source in Pipeline CRM. |
| Create Lead Status | `createLeadStatus` | Creates a lead status in Pipeline CRM. |
| Create Note Category | `createNoteCategory` | Creates an activity (note) category in Pipeline CRM. |
| Create Performance Lane | `createPerformanceLane` | Creates a performance lane (product line) in Pipeline CRM. |
| Create Person | `createPerson` | Creates a person (lead or contact) in Pipeline CRM. Optionally applies a todo template. |
| Create Person Custom Field Group | `createPersonCustomFieldGroup` | Creates a person custom field group in Pipeline CRM. |
| Create Person Custom Field Label | `createPersonCustomFieldLabel` | Creates a person custom field label (custom field definition) in Pipeline CRM. |
| Create Predefined Contacts Tag | `createPredefinedContactsTag` | Creates a predefined contacts (person) tag in Pipeline CRM. |
| Create Project | `createProject` | Creates a project in Pipeline CRM, optionally linked to deals, companies and people, from a project template, or with nested milestones. |
| Create Project Custom Field Group | `createProjectCustomFieldGroup` | Creates a project custom field group in Pipeline CRM. |
| Create Project Custom Field Label | `createProjectCustomFieldLabel` | Creates a project custom field label (custom field definition) in Pipeline CRM. |
| Create Project Milestone | `createProjectMilestone` | Creates a project milestone in Pipeline CRM. project_id identifies the project the milestone belongs to. |
| Create Project Milestone For Project | `createProjectMilestoneForProject` | Creates a milestone under a specific Pipeline CRM project, optionally with nested tasks and events. |
| Create Project Milestone Status | `createProjectMilestoneStatus` | Creates a custom project milestone status in Pipeline CRM. name and hex_color are required by the backend. |
| Create Project Template | `createProjectTemplate` | Creates a project template in Pipeline CRM, optionally with nested milestone and collaborator templates. |
| Create Revenue Type | `createRevenueType` | Creates a revenue type in Pipeline CRM. Only one revenue type can be the default at a time. |
| Create Search | `createSearch` | Creates a saved search (list view) in Pipeline CRM. query maps condition identifiers (e.g. person_name) to values; columns lists the result columns. |
| Create Team | `createTeam` | Creates a user team in Pipeline CRM, optionally under a parent team and with visibility permissions. |
| Create Todo Template | `createTodoTemplate` | Creates a todo (task) template in Pipeline CRM for companies, customers, deals or people. |
| Create Todo Template Item | `createTodoTemplateItem` | Creates a todo template item (a task inside a todo template) in Pipeline CRM. |
| Create User | `createUser` | Creates a user in Pipeline CRM (sends the new user an invitation email). Levels: 1 Basic, 2 Manager, 3 Executive. Basic users and Managers must include team_id; Executives cannot belong to a team. Uses POST /users (the documented POST /admin/users path returns a router 404). |
| Create Webhook | `createWebhook` | Subscribes a URL to a Pipeline CRM webhook event: a deal, person or company being created, updated or destroyed. failure_email is required by the backend (without it the vendor returns HTTP 500). |
| Delete Account Notification | `deleteAccountNotification` | Deletes an account notification in Pipeline CRM. |
| Delete Activity | `deleteActivity` | Deletes an activity (note) in Pipeline CRM. |
| Delete Calendar Entry | `deleteCalendarEntry` | Deletes a calendar entry in Pipeline CRM. |
| Delete Calendar Entry Priority | `deleteCalendarEntryPriority` | Deletes a calendar event and task priority in Pipeline CRM. |
| Delete Calendar Entry Status | `deleteCalendarEntryStatus` | Deletes a custom calendar event/task status in Pipeline CRM. System statuses (To-Do, Done) return 403. |
| Delete Comment | `deleteComment` | Deletes a comment on an activity (note) in Pipeline CRM. |
| Delete Company | `deleteCompany` | Deletes a company in Pipeline CRM. |
| Delete Company Custom Field Group | `deleteCompanyCustomFieldGroup` | Deletes a company custom field group in Pipeline CRM. |
| Delete Company Custom Field Label | `deleteCompanyCustomFieldLabel` | Deletes a company custom field label in Pipeline CRM. |
| Delete Company Tag | `deleteCompanyTag` | Deletes a company tag in Pipeline CRM. |
| Delete Custom Field Label Dropdown Entry | `deleteCustomFieldLabelDropdownEntry` | Deletes a custom field label dropdown entry in Pipeline CRM. |
| Delete Customer | `deleteCustomer` | Deletes a customer record in Pipeline CRM (the underlying company remains). |
| Delete Deal | `deleteDeal` | Deletes a deal in Pipeline CRM. |
| Delete Deal Custom Field Group | `deleteDealCustomFieldGroup` | Deletes a deal custom field group in Pipeline CRM. |
| Delete Deal Custom Field Label | `deleteDealCustomFieldLabel` | Deletes a deal custom field label in Pipeline CRM. |
| Delete Deal Loss Reason | `deleteDealLossReason` | Deletes a deal loss reason in Pipeline CRM. |
| Delete Deal Stage | `deleteDealStage` | Deletes a deal stage in Pipeline CRM. |
| Delete Deal Status | `deleteDealStatus` | Deletes a deal status in Pipeline CRM. |
| Delete Deal Tag | `deleteDealTag` | Deletes a deal tag in Pipeline CRM. |
| Delete Event Category | `deleteEventCategory` | Deletes a calendar event/task category in Pipeline CRM. |
| Delete File | `deleteFile` | Deletes a file (document) in Pipeline CRM. Returns 204 with no body on success. |
| Delete File Tag | `deleteFileTag` | Deletes a file (document) tag in Pipeline CRM. |
| Delete Lead Source | `deleteLeadSource` | Deletes a lead source in Pipeline CRM. |
| Delete Lead Status | `deleteLeadStatus` | Deletes a lead status in Pipeline CRM. |
| Delete Note Category | `deleteNoteCategory` | Deletes an activity (note) category in Pipeline CRM. |
| Delete Performance Lane | `deletePerformanceLane` | Deletes a performance lane (product line) in Pipeline CRM. |
| Delete Person | `deletePerson` | Deletes a person in Pipeline CRM. Returns 204 with no body on success. |
| Delete Person Custom Field Group | `deletePersonCustomFieldGroup` | Deletes a person custom field group in Pipeline CRM. |
| Delete Person Custom Field Label | `deletePersonCustomFieldLabel` | Deletes a person custom field label in Pipeline CRM. |
| Delete Predefined Contacts Tag | `deletePredefinedContactsTag` | Deletes a predefined contacts (person) tag in Pipeline CRM. |
| Delete Project | `deleteProject` | Deletes a project in Pipeline CRM. |
| Delete Project Custom Field Group | `deleteProjectCustomFieldGroup` | Deletes a project custom field group in Pipeline CRM. |
| Delete Project Custom Field Label | `deleteProjectCustomFieldLabel` | Deletes a project custom field label in Pipeline CRM. |
| Delete Project Milestone | `deleteProjectMilestone` | Deletes a project milestone in Pipeline CRM. |
| Delete Project Milestone Status | `deleteProjectMilestoneStatus` | Deletes a custom project milestone status in Pipeline CRM. System statuses return 403. If milestones use this status, pass merge_into_project_milestone_status_id to reassign them first. |
| Delete Project Template | `deleteProjectTemplate` | Deletes an account project template in Pipeline CRM. |
| Delete Revenue Type | `deleteRevenueType` | Deletes a revenue type in Pipeline CRM. |
| Delete Team | `deleteTeam` | Deletes a user team in Pipeline CRM. |
| Delete Todo Template | `deleteTodoTemplate` | Deletes a todo (task) template in Pipeline CRM. |
| Delete Todo Template Item | `deleteTodoTemplateItem` | Deletes a todo template item in Pipeline CRM. |
| Delete User | `deleteUser` | Deletes (deactivates) a user of the Pipeline CRM account. Uses DELETE /users/{id} (the documented DELETE /admin/users/{id} path returns a router 404). |
| Delete Webhook | `deleteWebhook` | Unsubscribes and deletes a Pipeline CRM webhook subscription by ID. |
| Dismiss Training Videos Banner | `dismissTrainingVideosBanner` | Persistently dismisses the training videos banner for the current Pipeline CRM user. Note: with API-key authentication the vendor returns HTTP 403 (empty body) on this endpoint; it appears to be usable only from an interactive session. |
| Get Account Notification | `getAccountNotification` | Retrieves an account notification in Pipeline CRM. |
| Get Activity | `getActivity` | Retrieves an activity (note) in Pipeline CRM by ID. |
| Get Calendar Entry | `getCalendarEntry` | Retrieves a calendar entry in Pipeline CRM by ID. Files attached to a calendar entry are listed via listFiles with calendar_entry_id. |
| Get Calendar Entry Priority | `getCalendarEntryPriority` | Retrieves a calendar event and task priority in Pipeline CRM by ID. |
| Get Calendar Entry Status | `getCalendarEntryStatus` | Retrieves a calendar event/task status in Pipeline CRM by ID. |
| Get Comment | `getComment` | Retrieves a comment on an activity (note) in Pipeline CRM. |
| Get Company | `getCompany` | Retrieves a company in Pipeline CRM by ID. |
| Get Company Custom Field Group | `getCompanyCustomFieldGroup` | Retrieves a company custom field group in Pipeline CRM by ID. |
| Get Company Custom Field Label | `getCompanyCustomFieldLabel` | Retrieves a company custom field label in Pipeline CRM by ID. |
| Get Company Tag | `getCompanyTag` | Retrieves a company tag in Pipeline CRM by ID. |
| Get Custom Field Label Dropdown Entry | `getCustomFieldLabelDropdownEntry` | Retrieves a custom field label dropdown entry in Pipeline CRM by ID. |
| Get Deal | `getDeal` | Retrieves a deal in Pipeline CRM by ID. |
| Get Deal Custom Field Group | `getDealCustomFieldGroup` | Retrieves a deal custom field group in Pipeline CRM by ID. |
| Get Deal Custom Field Label | `getDealCustomFieldLabel` | Retrieves a deal custom field label in Pipeline CRM by ID. |
| Get Deal Loss Reason | `getDealLossReason` | Retrieves a deal loss reason in Pipeline CRM by ID. |
| Get Deal Stage | `getDealStage` | Retrieves a deal stage in Pipeline CRM by ID. |
| Get Deal Status | `getDealStatus` | Retrieves a deal status in Pipeline CRM by ID. |
| Get Deal Tag | `getDealTag` | Retrieves a deal tag in Pipeline CRM by ID. |
| Get Event Category | `getEventCategory` | Retrieves a calendar event/task category in Pipeline CRM by ID. |
| Get File | `getFile` | Retrieves a file (document) in Pipeline CRM by ID. |
| Get File Tag | `getFileTag` | Retrieves a file (document) tag in Pipeline CRM by ID. |
| Get Lead Source | `getLeadSource` | Retrieves a lead source in Pipeline CRM by ID. |
| Get Lead Status | `getLeadStatus` | Retrieves a lead status in Pipeline CRM by ID. |
| Get Note Category | `getNoteCategory` | Retrieves an activity (note) category in Pipeline CRM by ID. |
| Get Person | `getPerson` | Retrieves a person in Pipeline CRM by ID. |
| Get Person Custom Field Group | `getPersonCustomFieldGroup` | Retrieves a person custom field group in Pipeline CRM by ID. |
| Get Person Custom Field Label | `getPersonCustomFieldLabel` | Retrieves a person custom field label in Pipeline CRM by ID. |
| Get Predefined Contacts Tag | `getPredefinedContactsTag` | Retrieves a predefined contacts (person) tag in Pipeline CRM by ID. |
| Get Profile | `getProfile` | Retrieves the profile of the Pipeline CRM user that owns the API key, including account and permission details. |
| Get Project | `getProject` | Retrieves a project in Pipeline CRM by ID. |
| Get Project Custom Field Group | `getProjectCustomFieldGroup` | Retrieves a project custom field group in Pipeline CRM by ID. |
| Get Project Custom Field Label | `getProjectCustomFieldLabel` | Retrieves a project custom field label in Pipeline CRM by ID. |
| Get Project Milestone | `getProjectMilestone` | Retrieves a project milestone in Pipeline CRM by ID. |
| Get Project Milestone Status | `getProjectMilestoneStatus` | Retrieves a project milestone status in Pipeline CRM by ID. |
| Get Project Template | `getProjectTemplate` | Retrieves a project template in Pipeline CRM by ID. |
| Get Revenue Type | `getRevenueType` | Retrieves a revenue type in Pipeline CRM by ID. |
| Get Search | `getSearch` | Retrieves a saved search definition in Pipeline CRM by ID. |
| Get Team | `getTeam` | Retrieves a user team in Pipeline CRM by ID. |
| Get Todo Template | `getTodoTemplate` | Retrieves a todo (task) template with its items in Pipeline CRM by ID. |
| Get Todo Template Item | `getTodoTemplateItem` | Retrieves a todo template item in Pipeline CRM by ID. |
| Get Training Video Playback | `getTrainingVideoPlayback` | Returns a redirect (302) to a short-lived presigned S3 URL for an uploaded Pipeline CRM training video. Returns 404 for url-sourced, disabled or other-account videos. |
| Get User | `getUser` | Retrieves a user of the Pipeline CRM account by ID. Note: the record includes the user's personal api_key; handle as sensitive. |
| Invite Project Collaborator | `inviteProjectCollaborator` | Invites a user to collaborate on a Pipeline CRM project. Sends an invitation email to the given address. |
| List Account Notifications | `listAccountNotifications` | Lists account notifications in Pipeline CRM. |
| List Activities | `listActivities` | Lists activities (notes) in Pipeline CRM, filterable by owner, dates, associated company, deal or person, title, content, category and comments. |
| List Calendar Entries | `listCalendarEntries` | Lists calendar entries (tasks and events) in Pipeline CRM, filterable by kind, completion, due window, start/end time and recurrence. |
| List Calendar Entry Priorities | `listCalendarEntryPriorities` | Lists the calendar event and task priorities configured in Pipeline CRM. |
| List Calendar Entry Statuses | `listCalendarEntryStatuses` | Lists calendar event/task statuses for the Pipeline CRM account, ordered by position. System statuses To-Do (first) and Done (last) always exist. |
| List Comments | `listComments` | Lists comments on an activity (note) in Pipeline CRM. |
| List Companies | `listCompanies` | Lists companies in Pipeline CRM, filterable by name, contact details, address, dates, owner, customer status and tags. |
| List Company Custom Field Groups | `listCompanyCustomFieldGroups` | Lists company custom field groups in Pipeline CRM. Admin access required. |
| List Company Custom Field Labels | `listCompanyCustomFieldLabels` | Lists company custom field labels (custom field definitions) in Pipeline CRM, filterable by name, field type and group. |
| List Company Tags | `listCompanyTags` | Lists company tags configured in Pipeline CRM. |
| List Custom Field Label Dropdown Entries | `listCustomFieldLabelDropdownEntries` | Lists dropdown entries (options) of custom field labels in Pipeline CRM, optionally for one custom field label. |
| List Deal Custom Field Groups | `listDealCustomFieldGroups` | Lists deal custom field groups in Pipeline CRM. Admin access required. |
| List Deal Custom Field Labels | `listDealCustomFieldLabels` | Lists deal custom field labels (custom field definitions) in Pipeline CRM, filterable by name, field type and group. |
| List Deal Loss Reasons | `listDealLossReasons` | Lists deal loss reasons configured in Pipeline CRM. |
| List Deal Stages | `listDealStages` | Lists deal stages (with default win probability and pipeline) configured in Pipeline CRM. |
| List Deal Statuses | `listDealStatuses` | Lists deal statuses (colored health indicators) configured in Pipeline CRM. |
| List Deal Tags | `listDealTags` | Lists deal tags configured in Pipeline CRM. |
| List Deals | `listDeals` | Lists deals in Pipeline CRM, filterable by name, source, owner, value range, stage, status, pipeline, dates, company, currency and tags. |
| List Event Categories | `listEventCategories` | Lists calendar event/task categories configured in Pipeline CRM. |
| List File Tags | `listFileTags` | Lists file (document) tags configured in Pipeline CRM. |
| List Files | `listFiles` | Lists files (documents) in Pipeline CRM, filterable by association, name, type, owner, modified date, sharing and tags. |
| List Lead Sources | `listLeadSources` | Lists lead sources (with optional cost per lead and flat fee) configured in Pipeline CRM. |
| List Lead Statuses | `listLeadStatuses` | Lists lead statuses configured in Pipeline CRM. |
| List Note Categories | `listNoteCategories` | Lists activity (note) categories configured in Pipeline CRM. |
| List People | `listPeople` | Lists people (leads and contacts) in Pipeline CRM, filterable by name, email, phone, owner, address, company, lead source/status, type, dates and tags. |
| List Performance Lanes | `listPerformanceLanes` | Lists performance lanes (product lines) configured in Pipeline CRM. The vendor returns only entries (no pagination block). |
| List Person Custom Field Groups | `listPersonCustomFieldGroups` | Lists person custom field groups in Pipeline CRM. Admin access required. |
| List Person Custom Field Labels | `listPersonCustomFieldLabels` | Lists person custom field labels (custom field definitions) in Pipeline CRM, filterable by name, field type and group. |
| List Predefined Contacts Tags | `listPredefinedContactsTags` | Lists predefined contacts (person) tags configured in Pipeline CRM. |
| List Project Associations | `listProjectAssociations` | Lists the deals, companies and people associated with a Pipeline CRM project, optionally filtered by type. |
| List Project Custom Field Groups | `listProjectCustomFieldGroups` | Lists project custom field groups in Pipeline CRM. Admin access required. |
| List Project Custom Field Labels | `listProjectCustomFieldLabels` | Lists project custom field labels (custom field definitions) in Pipeline CRM, filterable by name, field type and group. |
| List Project Milestone Statuses | `listProjectMilestoneStatuses` | Lists project milestone statuses (system and custom) in Pipeline CRM. Admin access required. Note: this vendor endpoint currently returns HTTP 500 for this account (verified live with and without paging); use getProjectMilestoneStatus by ID, or sortProjectMilestoneStatuses which returns the full status list. |
| List Project Milestones | `listProjectMilestones` | Lists all project milestones across projects in Pipeline CRM. Note: the vendor ignores the documented conditions[...] filters here (verified live), so only paging is exposed; use listProjectMilestonesForProject to scope to one project or autocompleteProjectMilestones to match by name. |
| List Project Milestones For Project | `listProjectMilestonesForProject` | Lists the milestones of a single Pipeline CRM project. |
| List Project Templates | `listProjectTemplates` | Lists project templates in Pipeline CRM, including account-specific and system-wide templates (system templates have account_id null). |
| List Projects | `listProjects` | Lists projects in Pipeline CRM, including archived ones. Note: the vendor ignores the documented conditions[...] filters on this endpoint (verified live: name, id, status, archived, date and owner filters all return the full list), so only paging is exposed; use autocompleteProjects to find projects by name. |
| List Revenue Types | `listRevenueTypes` | Lists revenue types configured in Pipeline CRM. |
| List Searches | `listSearches` | Lists saved searches (list views) in Pipeline CRM. |
| List Teams | `listTeams` | Lists user teams (with hierarchy and visibility permissions) in Pipeline CRM. |
| List Todo Template Items | `listTodoTemplateItems` | Lists todo template items (the tasks inside todo templates) in Pipeline CRM. |
| List Todo Templates | `listTodoTemplates` | Lists todo (task) templates with their items in Pipeline CRM. |
| List Training Videos | `listTrainingVideos` | Lists the training videos enabled for the current Pipeline CRM user, filtered by app section. |
| List Users | `listUsers` | Lists users of the Pipeline CRM account, filterable by exact email, admin flag, level and inactive status. Note: user records include each user's personal api_key; handle responses as sensitive. |
| List Webhooks | `listWebhooks` | Lists the webhook subscriptions registered for the Pipeline CRM account. |
| Mark Training Video Watched | `markTrainingVideoWatched` | Marks a training video as watched for the current Pipeline CRM user. |
| Remove Project Association | `removeProjectAssociation` | Removes a single deal, company or person association from a Pipeline CRM project. |
| Restore Training Videos Banner | `restoreTrainingVideosBanner` | Restores the training videos banner for the current Pipeline CRM user by clearing a prior dismissal. |
| Run Saved Search | `runSavedSearch` | Runs a saved Pipeline CRM search by ID and returns matching records as rows of values, with column metadata. |
| Run Saved Search With Overrides | `runSavedSearchWithOverrides` | Runs a saved Pipeline CRM search by ID using the search definition supplied in the body (without saving it) and returns matching records. |
| Run Search | `runSearch` | Runs an ad hoc Pipeline CRM search defined in the body, without saving it, and returns matching records as rows of values with column metadata. |
| Sort Calendar Entry Statuses | `sortCalendarEntryStatuses` | Sets the sort order of calendar event/task statuses in Pipeline CRM. order lists status IDs in the desired order; system To-Do stays first and Done last. |
| Sort Project Custom Field Labels | `sortProjectCustomFieldLabels` | Sets the sort order of project custom field labels within one custom field group in Pipeline CRM. order lists label IDs in the desired order. custom_field_group_id is required by the backend (undocumented; without it the vendor returns an empty 422). Returns the group's labels (bare JSON array) with resulting positions. |
| Sort Project Milestone Statuses | `sortProjectMilestoneStatuses` | Sets the sort order of project milestone statuses in Pipeline CRM. order lists status IDs in the desired order; unknown IDs are ignored. Returns the full status list (bare JSON array) with resulting positions. |
| Unarchive Project | `unarchiveProject` | Restores an archived project in Pipeline CRM back to active status (PUT). |
| Unarchive Project (PATCH) | `unarchiveProjectPatch` | Restores an archived project in Pipeline CRM using PATCH. Equivalent to unarchiveProject (PUT). |
| Unmark Training Video Watched | `unmarkTrainingVideoWatched` | Clears the watched flag of a training video for the current Pipeline CRM user. |
| Update Account Notification | `updateAccountNotification` | Updates an account notification in Pipeline CRM, for example marking it as read. |
| Update Activity | `updateActivity` | Updates an activity (note) in Pipeline CRM. |
| Update Calendar Entry | `updateCalendarEntry` | Updates a calendar entry in Pipeline CRM. |
| Update Calendar Entry Priority | `updateCalendarEntryPriority` | Updates a calendar event and task priority in Pipeline CRM. |
| Update Calendar Entry Status | `updateCalendarEntryStatus` | Updates a calendar event/task status in Pipeline CRM. System statuses (To-Do, Done) cannot be renamed or repositioned. |
| Update Comment | `updateComment` | Updates a comment on an activity (note) in Pipeline CRM. Set edited_by_user_id to record who edited it. |
| Update Company | `updateCompany` | Updates a company in Pipeline CRM. |
| Update Company Custom Field Group | `updateCompanyCustomFieldGroup` | Updates a company custom field group in Pipeline CRM. |
| Update Company Custom Field Label | `updateCompanyCustomFieldLabel` | Updates a company custom field label in Pipeline CRM. |
| Update Company Tag | `updateCompanyTag` | Updates a company tag in Pipeline CRM. |
| Update Custom Field Label Dropdown Entry | `updateCustomFieldLabelDropdownEntry` | Updates a custom field label dropdown entry in Pipeline CRM. |
| Update Customer | `updateCustomer` | Updates a customer record's health score in Pipeline CRM. |
| Update Deal | `updateDeal` | Updates a deal in Pipeline CRM. |
| Update Deal Custom Field Group | `updateDealCustomFieldGroup` | Updates a deal custom field group in Pipeline CRM. |
| Update Deal Custom Field Label | `updateDealCustomFieldLabel` | Updates a deal custom field label in Pipeline CRM. |
| Update Deal Loss Reason | `updateDealLossReason` | Updates a deal loss reason in Pipeline CRM. |
| Update Deal Stage | `updateDealStage` | Updates a deal stage in Pipeline CRM. percent must be unique within the pipeline (the vendor returns 422 'Percent has already been taken' otherwise). |
| Update Deal Status | `updateDealStatus` | Updates a deal status in Pipeline CRM. |
| Update Deal Tag | `updateDealTag` | Updates a deal tag in Pipeline CRM. |
| Update Event Category | `updateEventCategory` | Updates a calendar event/task category in Pipeline CRM. |
| Update File | `updateFile` | Updates a file (document) in Pipeline CRM. Changing the title requires also sending url (the vendor returns 422 'Updating a document's title requires a url'); sending url re-fetches the file. |
| Update File Tag | `updateFileTag` | Updates a file (document) tag in Pipeline CRM. |
| Update Lead Source | `updateLeadSource` | Updates a lead source in Pipeline CRM. |
| Update Lead Status | `updateLeadStatus` | Updates a lead status in Pipeline CRM. |
| Update Note Category | `updateNoteCategory` | Updates an activity (note) category in Pipeline CRM. |
| Update Performance Lane | `updatePerformanceLane` | Updates a performance lane (product line) in Pipeline CRM. |
| Update Person | `updatePerson` | Updates a person (lead or contact) in Pipeline CRM. |
| Update Person Custom Field Group | `updatePersonCustomFieldGroup` | Updates a person custom field group in Pipeline CRM. |
| Update Person Custom Field Label | `updatePersonCustomFieldLabel` | Updates a person custom field label in Pipeline CRM. |
| Update Predefined Contacts Tag | `updatePredefinedContactsTag` | Updates a predefined contacts (person) tag in Pipeline CRM. |
| Update Project | `updateProject` | Updates a project in Pipeline CRM. |
| Update Project Custom Field Group | `updateProjectCustomFieldGroup` | Updates a project custom field group in Pipeline CRM. |
| Update Project Custom Field Label | `updateProjectCustomFieldLabel` | Updates a project custom field label in Pipeline CRM. |
| Update Project Milestone | `updateProjectMilestone` | Updates a project milestone in Pipeline CRM. |
| Update Project Milestone Status | `updateProjectMilestoneStatus` | Updates a project milestone status in Pipeline CRM. |
| Update Project Template | `updateProjectTemplate` | Updates a project template in Pipeline CRM. Nested milestone/collaborator entries need id to update and _destroy true to remove. |
| Update Revenue Type | `updateRevenueType` | Updates a revenue type in Pipeline CRM. |
| Update Search | `updateSearch` | Updates a saved search (list view) in Pipeline CRM. |
| Update Team | `updateTeam` | Updates a user team in Pipeline CRM. |
| Update Todo Template | `updateTodoTemplate` | Updates a todo (task) template in Pipeline CRM. |
| Update Todo Template Item | `updateTodoTemplateItem` | Updates a todo template item in Pipeline CRM. |
| Update User | `updateUser` | Updates a user of the Pipeline CRM account. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Company Created | `company:create` | Fires when a company is created in Pipeline CRM. Registered through POST /admin/webhooks (event_model=company, event_action=create). Payload event_action is 'created'; trigger observed as '&lt;API app name&gt; company:create'. |
| Company Deleted | `company:destroy` | Fires when a company is deleted in Pipeline CRM. Registered through POST /admin/webhooks (event_model=company, event_action=destroy). Payload event_action is 'deleted'; trigger observed as '&lt;API app name&gt; company:destroy'. |
| Company Updated | `company:update` | Fires when a company is updated in Pipeline CRM. Registered through POST /admin/webhooks (event_model=company, event_action=update). Payload event_action is 'updated' with event_changes; trigger observed as '&lt;API app name&gt; company:update'. |
| Deal Created | `deal:create` | Fires when a deal is created in Pipeline CRM. Registered automatically through POST /admin/webhooks (event_model=deal, event_action=create). Payload event_action is 'created'; trigger is the automation name Pipeline assigns, observed as '&lt;API app name&gt; deal:create'. Schema from the vendor's documented Event Payload table. |
| Deal Deleted | `deal:destroy` | Fires when a deal is deleted in Pipeline CRM. Registered through POST /admin/webhooks (event_model=deal, event_action=destroy). Payload event_action is 'deleted'; trigger observed as '&lt;API app name&gt; deal:destroy'. |
| Deal Updated | `deal:update` | Fires when a deal is updated in Pipeline CRM. Registered through POST /admin/webhooks (event_model=deal, event_action=update). Payload event_action is 'updated' and event_changes lists changed values; trigger observed as '&lt;API app name&gt; deal:update'. |
| Person Created | `person:create` | Fires when a person is created in Pipeline CRM. Registered through POST /admin/webhooks (event_model=person, event_action=create). Payload event_action is 'created'; trigger observed as '&lt;API app name&gt; person:create'. |
| Person Deleted | `person:destroy` | Fires when a person is deleted in Pipeline CRM. Registered through POST /admin/webhooks (event_model=person, event_action=destroy). Payload event_action is 'deleted'; trigger observed as '&lt;API app name&gt; person:destroy'. |
| Person Updated | `person:update` | Fires when a person is updated in Pipeline CRM. Registered through POST /admin/webhooks (event_model=person, event_action=update). Payload event_action is 'updated' with event_changes; trigger observed as '&lt;API app name&gt; person:update'. |
