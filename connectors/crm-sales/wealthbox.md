---
description: "Wealthbox CRM — the CRM built for financial advisors and RIA firms."
hidden: true
---

# Wealthbox

<img src="../../.gitbook/assets/connectors/wealthbox.png" alt="Wealthbox logo" width="64">

Wealthbox CRM — the CRM built for financial advisors and RIA firms. Wraps the Wealthbox v1 REST API at https://api.crmworkspace.com/v1 and covers contacts (people, households, organizations and trusts), household membership, tasks and subtasks, calendar events, opportunities with amounts and stages, projects, notes, comments, workflows, workflow templates and workflow steps, tags, custom fields, contact roles and every customizable category pick-list, plus users, teams and user groups and the firm-wide activity stream. Supports both a personal API access token (ACCESS_TOKEN header) and OAuth 2.0 authorization-code with refresh. Change detection is by polling: every list endpoint accepts updated_since/updated_before, contacts expose deleted/deleted_since tombstones, and the activity stream is a cursor-paginated change feed.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [wealthbox.com](https://wealthbox.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Slug** | `wealthbox` |

## Use it

Add Wealthbox from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.wealthbox.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Household Member | `addHouseholdMember` | Add an existing contact to a household and give them a household title. The household is itself a contact record of type Household — use List Contacts with type=household to find its id. |
| Complete Workflow Step | `completeWorkflowStep` | Mark a step of a running Wealthbox workflow complete. Pass workflow_outcome_id to record which outcome was chosen; if that outcome restarts the step, due_date_set and due_date control the restarted step's due date. |
| Create Contact | `createContact` | Create a contact in Wealthbox. Only first_name and last_name are required; everything else is optional and omitted fields are not sent. Set type to Household, Organization or Trust to create those record kinds instead of a person. Pass household to place the contact in a household, and the collection fields to attach addresses, emails, phones, websites, tags, custom fields and contact roles in the same call. |
| Create Event | `createEvent` | Create a Wealthbox calendar event. Requires title, starts_at and ends_at. Link the event to contacts with linked_to, invite users and contacts with invitees, and set email_invitees true to send the invitations. |
| Create Note | `createNote` | Create a Wealthbox note. content is required; attach the note to a contact with linked_to (Contact is the only supported linked type) and classify it with tags. |
| Create Opportunity | `createOpportunity` | Create a Wealthbox opportunity. Requires name, target_close, probability, stage and amounts. stage is an opportunity-stage id (see List Category Members with type=opportunity_stages). amounts is an array of {amount, currency, kind} where kind is Fee, Commission, AUM or Other. Only the first contact in linked_to is used. |
| Create Project | `createProject` | Create a Wealthbox project. Both name and description are required by the API. organizer is the id of the user responsible for the project. |
| Create Task For Team | `createTaskForTeam` | Create a Wealthbox task assigned to a team rather than an individual. Requires name and due_date; assigned_to_team takes a team id (see List Teams). Otherwise identical to Create Task For User. |
| Create Task For User | `createTaskForUser` | Create a Wealthbox task assigned to an individual user. Requires name and due_date; assigned_to takes a user id (see List Users). Link the task to contacts, projects or opportunities with linked_to, and attach subtasks and custom fields in the same call. To assign to a team instead, use Create Task For Team. |
| Create Workflow | `createWorkflow` | Start a Wealthbox workflow from a workflow template. workflow_template is the template id (see List Workflow Templates). Link the workflow to a contact or other record with linked_to, schedule it with starts_at, and supply workflow_milestones for every milestone the template defines. |

<details>

<summary>See 41 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Delete Contact | `deleteContact` | Delete a Wealthbox contact by id. Deleted contacts remain retrievable as tombstones through List Contacts with deleted=true, which returns id and deleted_at. |
| Delete Event | `deleteEvent` | Delete a Wealthbox calendar event by id. |
| Delete Opportunity | `deleteOpportunity` | Delete a Wealthbox opportunity by id. |
| Delete Project | `deleteProject` | Delete a Wealthbox project by id. |
| Delete Task | `deleteTask` | Delete a Wealthbox task by id. |
| Delete Workflow | `deleteWorkflow` | Delete a Wealthbox workflow instance by id. This removes the running workflow and its steps; the underlying template is untouched. |
| Get Contact | `getContact` | Retrieve a single Wealthbox contact by id, with its household, tags, addresses, email addresses, phone numbers, websites, custom fields and contact roles. |
| Get Current User | `getMe` | Retrieve the login profile of the authenticated Wealthbox user: name, email, plan, the current_user (the account/workspace all API calls run in), every account the login can access, and the users in the current account. Takes no input, so it is the cheapest call to verify a credential. |
| Get Event | `getEvent` | Retrieve a single Wealthbox calendar event by id, including its invitees, linked contacts and custom fields. |
| Get Note | `getNote` | Retrieve a single Wealthbox note by id, including its content, linked contacts and tags. |
| Get Opportunity | `getOpportunity` | Retrieve a single Wealthbox opportunity by id, including its amounts, stage, linked contact and custom fields. |
| Get Project | `getProject` | Retrieve a single Wealthbox project by id, including its organizer, visibility and custom fields. |
| Get Task | `getTask` | Retrieve a single Wealthbox task by id, including its subtasks, linked records and custom fields. |
| Get Workflow | `getWorkflow` | Retrieve a single Wealthbox workflow by id, including its steps (with their completion state and outcomes) and milestones. |
| Get Workflow Template | `getWorkflowTemplate` | Retrieve a single Wealthbox workflow template by id, including the steps and milestones it defines. |
| List Activity Stream | `listActivityStream` | Retrieve the Wealthbox activity stream for the authenticated user — the firm-wide feed of everything that happened, each item linked to the document it concerns. This is the change feed to poll for near-real-time sync: filter with updated_since/updated_before and page with cursor (page-based pagination is deprecated here). |
| List Category Members | `listCategoryMembers` | List the members of any customizable Wealthbox category — the workspace pick-lists. This is how you resolve the numeric ids that create and update calls need: opportunity_stages for an opportunity's stage, task_categories for a task's category, event_categories for an event's category, plus contact_types, contact_sources, opportunity_pipelines, file_categories, investment_objectives, financial_account_types, email_types, phone_types, address_types, website_types, tags, custom_fields and contact_roles. |
| List Comments | `listComments` | Retrieve Wealthbox comments — the replies left on notes, tasks, events and other records — optionally scoped to one record. resource_id is ignored unless resource_type is also given. Comments are read-only in the v1 API. |
| List Contact Roles | `listContactRoles` | List the contact roles defined in the Wealthbox workspace (Planning Advisor, Attorney, CPA and any custom roles). Use the returned ids as contact_roles[].id when creating or updating a contact. |
| List Contacts | `listContacts` | Retrieve contacts from Wealthbox, optionally filtered. A Wealthbox contact covers people, households, organizations and trusts — set type=household to list households. Supports incremental sync via updated_since/updated_before and tombstones via deleted/deleted_since. Page with per_page (default 25) and page (default 1). |
| List Custom Fields | `listCustomFields` | List the custom fields defined in the Wealthbox workspace, optionally narrowed to one document type. Use the returned ids as custom_fields[].id when creating or updating contacts, tasks, events, opportunities and projects. |
| List Events | `listEvents` | Retrieve Wealthbox calendar events, optionally filtered by the record they are linked to or by a start-date window. Supports incremental sync via updated_since/updated_before and paging via per_page/page. |
| List Notes | `listNotes` | Retrieve Wealthbox notes, optionally scoped to the record they are attached to. order accepts asc (ascending by created date, the default), created (descending by created date) or updated (descending by updated date). |
| List Opportunities | `listOpportunities` | Retrieve Wealthbox opportunities. Won and lost opportunities are excluded unless include_closed is true. Filter by the linked record with resource_id/resource_type, and sync incrementally with updated_since/updated_before. |
| List Projects | `listProjects` | Retrieve Wealthbox projects. Supports incremental sync via updated_since/updated_before and paging via per_page/page. |
| List Tags | `listTags` | List the tags defined in the Wealthbox workspace, optionally narrowed to the document type they apply to. Tags are referenced by name when creating or updating contacts and notes. |
| List Tasks | `listTasks` | Retrieve Wealthbox tasks, optionally filtered by the record they are linked to, assignee, creator, completion state or task type. Completed tasks are excluded unless completed=true. Supports incremental sync via updated_since/updated_before and paging via per_page/page. |
| List Teams | `listTeams` | List the teams in the Wealthbox account. Use the returned ids for assigned_to_team when creating or updating tasks. |
| List User Groups | `listUserGroups` | List the user groups in the Wealthbox account. A user group id is what the visible_to field on contacts, notes, tasks, events, opportunities and projects takes when the record should be visible to a group rather than Everyone or Private. |
| List Users | `listUsers` | List the users in the Wealthbox account. Defaults to active users only; pass status to include invited, inactive, legacy or all. Use the returned ids for assigned_to, organizer, manager and invitee fields. |
| List Workflow Templates | `listWorkflowTemplates` | List the workflow templates defined in the Wealthbox workspace. Use a template id with Create Workflow to start a workflow, and read its milestones to know what workflow_milestones the create call needs. |
| List Workflows | `listWorkflows` | Retrieve Wealthbox workflows — running instances of a workflow template — optionally filtered by the record they are linked to or by status (active, completed, scheduled). Each workflow includes its steps and milestones. |
| Remove Household Member | `removeHouseholdMember` | Remove a contact from a household. This unlinks the contact from the household; it does not delete the contact record. |
| Revert Workflow Step | `revertWorkflowStep` | Revert a completed step of a running Wealthbox workflow back to incomplete. |
| Update Contact | `updateContact` | Update an existing Wealthbox contact. This is a partial update: every field except id is optional and any field you omit is left untouched. Collection fields (addresses, emails, phones, websites) replace-or-append by the id inside each item; pass destroy true inside an item to remove it. Returns the full updated contact. |
| Update Event | `updateEvent` | Update a Wealthbox calendar event. The API requires title, starts_at and ends_at on every update, so send them even when unchanged. Use state to confirm, complete or cancel the event. |
| Update Note | `updateNote` | Update a Wealthbox note. content is required on every update. Note: the Wealthbox v1 API exposes no delete endpoint for notes. |
| Update Opportunity | `updateOpportunity` | Update a Wealthbox opportunity — move it to a new stage, revise the probability, target close date, next step or amounts. Fields you omit are not sent. |
| Update Project | `updateProject` | Update a Wealthbox project. The API requires name and description on every update, so send them even when unchanged. |
| Update Task For Team | `updateTaskForTeam` | Update a Wealthbox task and assign it to a team. Set complete true to mark the task done. Fields you omit are not sent. |
| Update Task For User | `updateTaskForUser` | Update a Wealthbox task and assign it to an individual user. Set complete true to mark the task done. Fields you omit are not sent. To assign to a team instead, use Update Task For Team. |

</details>
