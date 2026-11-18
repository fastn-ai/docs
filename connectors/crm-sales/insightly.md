---
description: "Insightly CRM REST API v3.1 — contacts, organisations, leads, opportunities, projects, tasks, events, notes, emails, comments, pipelines, custom…"
hidden: true
---

# Insightly

Insightly CRM REST API v3.1 — contacts, organisations, leads, opportunities, projects, tasks, events, notes, emails, comments, pipelines, custom objects/fields, users, teams, files, milestones, tags and more.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [insightly.com](https://insightly.com) |
| **Authentication** | Basic auth |
| **Actions** | 147 |
| **Events** | 0 |
| **Slug** | `insightly` |

## Use it

Add Insightly from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.insightly.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact Link | `addContactLink` | Link a contact to another record. Path id=CONTACT_ID; body LINK_OBJECT_NAME (e.g. Organisation) and LINK_OBJECT_ID. |
| Add Contact Tag | `addContactTag` | Add a tag to a contact. Path id=CONTACT_ID; body TAG_NAME. |
| Add Lead Tag | `addLeadTag` | Add a tag to a lead. Path id=LEAD_ID; body TAG_NAME. |
| Add Note Comment | `addNoteComment` | Add a comment to a note. Path id=NOTE_ID; body BODY (comment text). |
| Add Opportunity Link | `addOpportunityLink` | Link an opportunity to another record. Path id=OPPORTUNITY_ID; body LINK_OBJECT_NAME + LINK_OBJECT_ID. |
| Add Organisation Link | `addOrganisationLink` | Link an organisation to another record. Path id=ORGANISATION_ID; body LINK_OBJECT_NAME + LINK_OBJECT_ID. |
| Add Organisation Tag | `addOrganisationTag` | Add a tag to an organisation. Path id=ORGANISATION_ID; body TAG_NAME. |
| Add Project Link | `addProjectLink` | Link a project to another record. Path id=PROJECT_ID; body LINK_OBJECT_NAME + LINK_OBJECT_ID. |
| Add Task Comment | `addTaskComment` | Add a comment to a task. Path id=TASK_ID; body BODY (comment text). |
| Add Team Member | `addTeamMember` | Add a member to a team. Path id = TEAM_ID; body MEMBER_USER_ID. |
| Change Opportunity State | `changeOpportunityState` | Change an opportunity state. Path id=OPPORTUNITY_ID; body FOR_OPPORTUNITY_STATE (Open/Won/Lost/Abandoned/Suspended) and optional STATE_REASON_ID. |
| Create Contact | `createContact` | Create a contact. Common fields: FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, PHONE, TITLE, ORGANISATION_ID, BACKGROUND. |
| Create Contact Note | `createContactNote` | Add a note to a contact. Path id=CONTACT_ID; body TITLE (required) and BODY. |
| Create Event | `createEvent` | Create a calendar event. Required: TITLE, START_DATE_UTC, END_DATE_UTC (format 'YYYY-MM-DD HH:MM:SS'). Optional: ALL_DAY, LOCATION, DETAILS, REMINDER_DATE_UTC. |
| Create File Category | `createFileCategory` | Create a file category. Body: CATEGORY_NAME (required), ACTIVE, BACKGROUND_COLOR. |
| Create Lead | `createLead` | Create a lead. Required: LAST_NAME. Common: FIRST_NAME, EMAIL_ADDRESS, ORGANISATION_NAME, TITLE, PHONE_NUMBER, LEAD_SOURCE_ID, LEAD_STATUS_ID, LEAD_DESCRIPTION, LEAD_RATING. |
| Create Lead Note | `createLeadNote` | Add a note to a lead. Path id=LEAD_ID; body TITLE (required), BODY. |
| Create Lead Source | `createLeadSource` | Create a lead source. Body: LEAD_SOURCE (required), DEFAULT_VALUE, FIELD_ORDER. |
| Create Lead Status | `createLeadStatus` | Create a lead status. Body: LEAD_STATUS (required), DEFAULT_STATUS, STATUS_TYPE, FIELD_ORDER. |
| Create Opportunity | `createOpportunity` | Create an opportunity. Required: OPPORTUNITY_NAME. Optional: OPPORTUNITY_STATE (Open/Won/Lost/Abandoned/Suspended), OPPORTUNITY_DETAILS, BID_AMOUNT, BID_CURRENCY, PROBABILITY, FORECAST_CLOSE_DATE, CATEGORY_ID, RESPONSIBLE_USER_ID. Pipeline and stage cannot be set here (Insightly ignores PIPELINE_ID/STAGE_ID on this call); Insightly sets them on an existing opportunity with PUT /Opportunities/{id}/Pipeline and /PipelineStage. |
| Create Opportunity Category | `createOpportunityCategory` | Create an opportunity category. Body: CATEGORY_NAME (required), ACTIVE, BACKGROUND_COLOR. |
| Create Opportunity Note | `createOpportunityNote` | Add a note to an opportunity. Path id=OPPORTUNITY_ID; body TITLE (required), BODY. |
| Create Organisation | `createOrganisation` | Create an organisation. Required: ORGANISATION_NAME. Optional: PHONE, WEBSITE, BACKGROUND, address fields. |
| Create Organisation Note | `createOrganisationNote` | Add a note to an organisation. Path id=ORGANISATION_ID; body TITLE (required), BODY. |
| Create Project | `createProject` | Create a project. Required: PROJECT_NAME and STATUS (Not Started/In Progress/Completed/Deferred/Cancelled). Optional: PROJECT_DETAILS, OPPORTUNITY_ID, CATEGORY_ID, OWNER_USER_ID, RESPONSIBLE_USER_ID. Pipeline and stage cannot be set here (Insightly ignores PIPELINE_ID/STAGE_ID on this call); Insightly sets them on an existing project with PUT /Projects/{id}/Pipeline and /PipelineStage. |
| Create Project Category | `createProjectCategory` | Create a project category. Body: CATEGORY_NAME (required), ACTIVE, BACKGROUND_COLOR. |
| Create Project Milestone | `createProjectMilestone` | Add a milestone to a project. The path id is the PROJECT_ID. MILESTONE_ID must be sent as 0 when creating, DUE_DATE is mandatory, and TITLE names the milestone. |
| Create Project Note | `createProjectNote` | Add a note to a project. Path id=PROJECT_ID; body TITLE (required), BODY. |
| Create Task | `createTask` | Create a task. Required: TITLE. Optional: STATUS (Not Started/In Progress/Waiting/Completed/Deferred), DUE_DATE, PRIORITY, COMPLETED, DETAILS, CATEGORY_ID, RESPONSIBLE_USER_ID, PROJECT_ID, OPPORTUNITY_ID, MILESTONE_ID, PERCENT_COMPLETE. |
| Create Task Category | `createTaskCategory` | Create a task category. Body: CATEGORY_NAME (required), ACTIVE, BACKGROUND_COLOR. |
| Create Team | `createTeam` | Create a team. Body: TEAM_NAME (required). Optionally include TEAMMEMBERS. |
| Create Webhook | `createWebhook` | Create a webhook subscription. Body: OBJECT_NAME (e.g. Contact), TARGET_URL (HTTPS endpoint), FIELD_NAME (field to watch). |
| Delete Comment | `deleteComment` | Delete a comment by COMMENT_ID. |
| Delete Contact | `deleteContact` | Delete a contact by CONTACT_ID. |
| Delete Event | `deleteEvent` | Delete a calendar event by EVENT_ID. |
| Delete File Category | `deleteFileCategory` | Delete a file category by CATEGORY_ID. |
| Delete Lead | `deleteLead` | Delete a lead by LEAD_ID. |
| Delete Lead Source | `deleteLeadSource` | Delete a lead source by id (query param). |
| Delete Lead Status | `deleteLeadStatus` | Delete a lead status by id (query param). |
| Delete Note | `deleteNote` | Delete a note by NOTE_ID. |
| Delete Opportunity | `deleteOpportunity` | Delete an opportunity by OPPORTUNITY_ID. |
| Delete Opportunity Category | `deleteOpportunityCategory` | Delete an opportunity category by CATEGORY_ID. |
| Delete Organisation | `deleteOrganisation` | Delete an organisation by ORGANISATION_ID. |
| Delete Project | `deleteProject` | Delete a project by PROJECT_ID. |
| Delete Project Category | `deleteProjectCategory` | Delete a project category by CATEGORY_ID. |
| Delete Task | `deleteTask` | Delete a task by TASK_ID. |
| Delete Task Category | `deleteTaskCategory` | Delete a task category by CATEGORY_ID. |
| Delete Team | `deleteTeam` | Delete a team by TEAM_ID. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription by SUBSCRIPTION_ID. |
| Follow Contact | `followContact` | Start following a contact (adds to the current user's follows). Path id=CONTACT_ID. |
| Get Activity Set | `getActivitySet` | Get a single activity set by ACTIVITYSET_ID. |
| Get Contact | `getContact` | Get a single contact by CONTACT_ID. |
| Get Current User | `getCurrentUser` | Get the user that owns the API key (GET /Users/Me). Use to validate the connection. |
| Get Email | `getEmail` | Get an email by EMAIL_ID. |
| Get Event | `getEvent` | Get a calendar event by EVENT_ID. |
| Get File Category | `getFileCategory` | Get a file category by CATEGORY_ID. |
| Get Instance | `getInstance` | Get metadata about the current Insightly instance (plan, version, limits). |
| Get Lead | `getLead` | Get a lead by LEAD_ID. |
| Get Milestone | `getMilestone` | Get a milestone by MILESTONE_ID. |
| Get Note | `getNote` | Get a note by NOTE_ID. |
| Get Opportunity | `getOpportunity` | Get an opportunity by OPPORTUNITY_ID. |
| Get Opportunity Category | `getOpportunityCategory` | Get an opportunity category by CATEGORY_ID. |
| Get Opportunity State History | `getOpportunityStateHistory` | List the state-change history for an opportunity. |
| Get Organisation | `getOrganisation` | Get an organisation by ORGANISATION_ID. |
| Get Pipeline | `getPipeline` | Get a single pipeline by its PIPELINE_ID. |
| Get Pipeline Stage | `getPipelineStage` | Get a single pipeline stage by STAGE_ID. |
| Get Project | `getProject` | Get a project by PROJECT_ID. |
| Get Task | `getTask` | Get a task by TASK_ID. |
| Get Team | `getTeam` | Get a team by TEAM_ID. |
| Get User | `getUser` | Get a single user by USER_ID. |
| Get Webhook | `getWebhook` | Get a webhook subscription by SUBSCRIPTION_ID. |
| List Activity Sets | `listActivitySets` | List activity set templates. |
| List Contact Emails | `listContactEmails` | List emails linked to a contact. |
| List Contact Events | `listContactEvents` | List calendar events linked to a contact. |
| List Contact Links | `listContactLinks` | List links (to other records) on a contact. |
| List Contact Notes | `listContactNotes` | List notes attached to a contact. |
| List Contact Tags | `listContactTags` | List tags on a contact. |
| List Contact Tasks | `listContactTasks` | List tasks associated with a contact. |
| List Contacts | `listContacts` | List contacts. Supports paging (top/skip), brief and count_total. GET /Contacts has no date filter; to get records updated after a date use Search Contacts (updated_after_utc). |
| List Countries | `listCountries` | List the reference set of countries recognised by Insightly. |
| List Currencies | `listCurrencies` | List the reference set of currencies. |
| List Custom Fields | `listCustomFields` | List custom field definitions for an object (e.g. Contact, Organisation, Lead, Opportunity, Project, Task, Event). |
| List Custom Objects | `listCustomObjects` | List custom object definitions configured in this instance. |
| List Document Templates | `listDocumentTemplates` | List merge/document templates. |
| List Email Comments | `listEmailComments` | List comments on an email. |
| List Emails | `listEmails` | List emails. Supports top/skip/brief/count_total. |
| List Events | `listEvents` | List calendar events. Supports paging (top/skip), brief and count_total. GET /Events has no date filter; to get records updated after a date use Search Events (updated_after_utc). |
| List File Categories | `listFileCategories` | List file categories. |
| List Follows | `listFollows` | List records the current user is following. |
| List Lead Notes | `listLeadNotes` | List notes on a lead. |
| List Lead Sources | `listLeadSources` | List lead sources. |
| List Lead Statuses | `listLeadStatuses` | List lead statuses. |
| List Leads | `listLeads` | List leads. Supports top/skip/brief/count_total/updated_after_utc. |
| List Milestones | `listMilestones` | List all project milestones. |
| List Note Comments | `listNoteComments` | List comments on a note. |
| List Opportunities | `listOpportunities` | List opportunities. Supports paging (top/skip), brief and count_total. GET /Opportunities has no date filter; to get records updated after a date use Search Opportunities (updated_after_utc). |
| List Opportunity Categories | `listOpportunityCategories` | List opportunity categories. |
| List Opportunity Links | `listOpportunityLinks` | List links on an opportunity. |
| List Opportunity Notes | `listOpportunityNotes` | List notes on an opportunity. |
| List Opportunity State Reasons | `listOpportunityStateReasons` | List reasons used when changing an opportunity state (won/lost/etc). |
| List Organisation Links | `listOrganisationLinks` | List links on an organisation. |
| List Organisation Notes | `listOrganisationNotes` | List notes attached to an organisation. |
| List Organisations | `listOrganisations` | List organisations. Supports paging (top/skip), brief and count_total. GET /Organisations has no date filter; to get records updated after a date use Search Organisations (updated_after_utc). |
| List Permissions | `listPermissions` | List the caller's object/record permissions. |
| List Pipeline Stages | `listPipelineStages` | List all pipeline stages across pipelines. |
| List Pipelines | `listPipelines` | List all pipelines (for opportunities and projects). |
| List Project Categories | `listProjectCategories` | List project categories. |
| List Project Links | `listProjectLinks` | List links on a project. |
| List Project Milestones | `listProjectMilestones` | List milestones on a project. |
| List Project Notes | `listProjectNotes` | List notes on a project. |
| List Projects | `listProjects` | List projects. Supports paging (top/skip), brief and count_total. GET /Projects has no date filter; to get records updated after a date use Search Projects (updated_after_utc). |
| List Relationships | `listRelationships` | List relationship definitions (e.g. Colleague, Customer) used to link records. |
| List Task Categories | `listTaskCategories` | List task categories. |
| List Task Comments | `listTaskComments` | List comments on a task. |
| List Tasks | `listTasks` | List tasks. Supports paging (top/skip), brief and count_total. GET /Tasks has no date filter; to get records updated after a date use Search Tasks (updated_after_utc). |
| List Team Members | `listTeamMembers` | List all team members across every team in the Insightly instance. This endpoint accepts no filter parameters — to get the members of one specific team, use Get Team, whose TEAMMEMBERS array is scoped to that team. |
| List Teams | `listTeams` | List all teams. |
| List Users | `listUsers` | List all users in the instance. |
| List Webhooks | `listWebhooks` | List webhook subscriptions. |
| Search Contacts | `searchContacts` | Search contacts by field name/value (e.g. field_name=EMAIL_ADDRESS, field_value=jane@x.com). |
| Search Contacts By Tag | `searchContactsByTag` | List contacts having a given tag (tag_name query param). |
| Search Emails | `searchEmails` | Search emails by field name/value. |
| Search Events | `searchEvents` | Search events by field name/value. |
| Search Leads | `searchLeads` | Search leads by field name/value. |
| Search Notes | `searchNotes` | Search notes by field name/value. |
| Search Opportunities | `searchOpportunities` | Search opportunities by field name/value. |
| Search Organisations | `searchOrganisations` | Search organisations by field name/value. |
| Search Projects | `searchProjects` | Search projects by field name/value. |
| Search Tasks | `searchTasks` | Search tasks by field name/value. |
| Search Users | `searchUsers` | Search users by a field name/value (OData-style). |
| Update Comment | `updateComment` | Update a comment. Body must include COMMENT_ID plus BODY. |
| Update Contact | `updateContact` | Update a contact. Body must include CONTACT_ID plus any fields to change. |
| Update Event | `updateEvent` | Update a calendar event. Body must include EVENT_ID plus fields to change. |
| Update File Category | `updateFileCategory` | Update a file category. Body must include CATEGORY_ID plus fields to change. |
| Update Lead | `updateLead` | Update a lead. Body must include LEAD_ID plus fields to change. |
| Update Lead Source | `updateLeadSource` | Update a lead source. Body must include LEAD_SOURCE_ID plus fields to change. |
| Update Lead Status | `updateLeadStatus` | Update a lead status. Body must include LEAD_STATUS_ID plus fields to change. |
| Update Note | `updateNote` | Update a note. Body must include NOTE_ID plus TITLE/BODY. |
| Update Opportunity | `updateOpportunity` | Update an opportunity. Body must include OPPORTUNITY_ID plus fields to change. Pipeline and stage cannot be set here (Insightly ignores PIPELINE_ID/STAGE_ID on this call); Insightly sets them on an existing opportunity with PUT /Opportunities/{id}/Pipeline and /PipelineStage. |
| Update Opportunity Category | `updateOpportunityCategory` | Update an opportunity category. Body must include CATEGORY_ID plus fields to change. |
| Update Organisation | `updateOrganisation` | Update an organisation. Body must include ORGANISATION_ID plus fields to change. |
| Update Project | `updateProject` | Update a project. Body must include PROJECT_ID plus fields to change. Pipeline and stage cannot be set here (Insightly ignores PIPELINE_ID/STAGE_ID on this call); Insightly sets them on an existing project with PUT /Projects/{id}/Pipeline and /PipelineStage. |
| Update Project Category | `updateProjectCategory` | Update a project category. Body must include CATEGORY_ID plus fields to change. |
| Update Task | `updateTask` | Update a task. Body must include TASK_ID plus fields to change. |
| Update Task Category | `updateTaskCategory` | Update a task category. Body must include CATEGORY_ID plus fields to change. |
| Update Team | `updateTeam` | Update a team. Body must include TEAM_ID plus fields to change (e.g. TEAM_NAME). |
| Update Webhook | `updateWebhook` | Update a webhook subscription. Body must include SUBSCRIPTION_ID plus fields to change. |
