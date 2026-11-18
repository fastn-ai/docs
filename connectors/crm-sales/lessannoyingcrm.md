---
description: "Less Annoying CRM (LACRM) v2 API."
hidden: true
---

# Less Annoying CRM

<img src="../../.gitbook/assets/connectors/lessannoyingcrm.png" alt="Less Annoying CRM logo" width="64">

Less Annoying CRM (LACRM) v2 API. Single-endpoint JSON-RPC: POST https://api.lessannoyingcrm.com/v2/ with body {Function, Parameters}. Covers contacts, companies, pipelines, pipeline items/statuses, tasks, events, notes, emails, files, relationships, groups, group memberships, custom fields, calendars, teams, users, search, and webhooks.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [lessannoyingcrm.com](https://lessannoyingcrm.com) |
| **Authentication** | API key |
| **Slug** | `lessannoyingcrm` |

## Use it

Add Less Annoying CRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.lessannoyingcrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Contact | `createContact` | Create a contact (or company when IsCompany=true). Email/Phone/Address/Website are arrays of objects; pass [] if none. |
| Create Custom Field | `createCustomField` | Create a custom field. Type is one of Dropdown, RadioList, Checkbox, Number, Date, Text, TextArea, ContactLink, FileLink, Currency, Section, Signature, SectionHeader, TextBlock. Options is an array of strings (pass [] for non-choice types). |
| Create Email | `createEmail` | Log an email against one or more contacts. From is an object {Address,Name}; To/Cc are arrays of {Address,Name}. Date is a datetime. |
| Create Event | `createEvent` | Create a calendar event. StartDate/EndDate are datetimes (YYYY-MM-DD HH:MM:SS). Attendees is an array of objects; pass []. |
| Create Group | `createGroup` | Create a group. Sharing is Public/Private/Teams; TeamIds required for Teams (pass []). Color is a named color enum or ''. |
| Create Group Membership | `createGroupMembership` | Add a contact to a group. Provide GroupId (pass '' to use GroupName instead). GroupName optional lookup by name. |
| Create Note | `createNote` | Create a note attached to a contact/company. |
| Create Pipeline | `createPipeline` | Create a new pipeline. Permissions is Public or TeamSharing; TeamIds required only for TeamSharing (pass []). |
| Create Pipeline Item | `createPipelineItem` | Add a contact to a pipeline at a status (create a deal). Note is an optional history note (pass ''). |
| Create Pipeline Status | `createPipelineStatus` | Add a status/step to a pipeline. |

<details>

<summary>See 67 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Relationship | `createRelationship` | Create a relationship link between two contacts with a descriptive note. |
| Create Task | `createTask` | Create a task. DueDate YYYY-MM-DD. Attach to a contact via ContactId (pass '' if none). |
| Create Team | `createTeam` | Create a team with an optional list of user Uids (pass []). |
| Create Webhook | `createWebhook` | Register a webhook. EndpointUrl must be HTTPS and complete the X-Hook-Secret handshake. Events values: Contact.Create, Contact.Update, Contact.Delete, Event.Create, Event.Update, Event.Delete, GroupMembership.Create, GroupMembership.Delete, PipelineItemStatus.Create, PipelineItemStatus.Update, PipelineItemStatus.Delete, PublicForm.Submit. WebhookScope is User or Account. |
| Delete Contact | `deleteContact` | Delete a contact or company by Uid. |
| Delete Custom Field | `deleteCustomField` | Delete a custom field. SectionDeletesFields controls whether deleting a section also deletes its fields. |
| Delete Email | `deleteEmail` | Delete a logged email by Uid. |
| Delete Event | `deleteEvent` | Delete an event by Uid. |
| Delete Group | `deleteGroup` | Delete a group by Uid. |
| Delete Group Membership | `deleteGroupMembership` | Remove a contact from a group by ContactId + GroupId. |
| Delete Note | `deleteNote` | Delete a note by Uid. |
| Delete Pipeline | `deletePipeline` | Delete a pipeline by Uid. |
| Delete Pipeline Item | `deletePipelineItem` | Remove a pipeline item by Uid. |
| Delete Pipeline Status | `deletePipelineStatus` | Delete a pipeline status by Uid. |
| Delete Relationship | `deleteRelationship` | Delete a relationship by Uid. |
| Delete Task | `deleteTask` | Delete a task by Uid. |
| Delete Team | `deleteTeam` | Delete a team by Uid. |
| Delete Webhook | `deleteWebhook` | Delete (archive) a webhook by Uid. |
| Edit Contact | `editContact` | Edit an existing contact/company. Arrays replace existing values. |
| Edit Custom Field | `editCustomField` | Edit a custom field's name/required flag/options. |
| Edit Event | `editEvent` | Edit an existing event. |
| Edit Group | `editGroup` | Edit a group's name, sharing, teams, or color. |
| Edit Note | `editNote` | Edit an existing note's content. |
| Edit Pipeline | `editPipeline` | Edit an existing pipeline's name, icon, permissions, or teams. |
| Edit Pipeline Item | `editPipelineItem` | Move a pipeline item to a new status and/or add a history note. |
| Edit Pipeline Status | `editPipelineStatus` | Edit a pipeline status. |
| Edit Relationship | `editRelationship` | Edit a relationship's note. |
| Edit Task | `editTask` | Edit a task, including marking complete via IsComplete. |
| Edit Team | `editTeam` | Edit a team's name or member list. |
| Get Calendars | `getCalendars` | List all calendars. Response is an array of calendar objects. |
| Get Contact | `getContact` | Retrieve a single contact or company by Uid. |
| Get Contacts | `getContacts` | Search or list contacts and companies. Supports full-text SearchTerms, record-type filter, sorting, and pagination. |
| Get Contacts By Id | `getContactsById` | Fetch multiple contacts/companies by their Uids. |
| Get Contacts In Group | `getContactsInGroup` | Get all contacts in a group by GroupId. |
| Get Custom Field | `getCustomField` | Retrieve a single custom field definition by Uid. |
| Get Custom Fields | `getCustomFields` | List custom field definitions. Optionally filter by record type and pipeline. |
| Get Email | `getEmail` | Retrieve a single logged email by Uid. |
| Get Emails | `getEmails` | List logged emails with optional filters and pagination. |
| Get Emails Attached To Contact | `getEmailsAttachedToContact` | Get all logged emails attached to a specific contact. |
| Get Event | `getEvent` | Retrieve a single event by Uid. |
| Get Events | `getEvents` | List calendar events in a date range with filters. StartDate/EndDate are YYYY-MM-DD. |
| Get Events Attached To Contact | `getEventsAttachedToContact` | Get all events attached to a specific contact. |
| Get File | `getFile` | Get file metadata and a temporary download URL (FileUrl valid ~5 minutes) by FileId. |
| Get Files Attached To Contact | `getFilesAttachedToContact` | List files attached to a contact. Set ReturnPreviousVersions to include older versions. |
| Get Group | `getGroup` | Retrieve a single group by Uid. |
| Get Groups | `getGroups` | List groups. Set ReturnNumberOfContacts to include member counts. |
| Get Groups Attached To Contact | `getGroupsAttachedToContact` | Get all groups a contact belongs to. |
| Get Note | `getNote` | Retrieve a single note by Uid. |
| Get Notes | `getNotes` | List notes with optional user/contact filters and pagination. |
| Get Notes Attached To Contact | `getNotesAttachedToContact` | Get all notes attached to a specific contact. |
| Get Pipeline | `getPipeline` | Retrieve a single pipeline by Uid, including its statuses. |
| Get Pipeline Item | `getPipelineItem` | Retrieve a single pipeline item by Uid. |
| Get Pipeline Items | `getPipelineItems` | List pipeline items (deals) in a pipeline with filters and pagination. |
| Get Pipeline Items Attached To Contact | `getPipelineItemsAttachedToContact` | Get all pipeline items attached to a contact, grouped by pipeline. Response is an array. |
| Get Pipeline Statuses | `getPipelineStatuses` | List statuses, optionally filtered to one pipeline. Pass '' for PipelineId to get all. Response is an array. |
| Get Pipelines | `getPipelines` | List all pipelines with statuses and custom fields. Response is an array of pipeline objects. |
| Get Relationship | `getRelationship` | Retrieve a single contact relationship by Uid. |
| Get Relationships Attached To Contact | `getRelationshipsAttachedToContact` | Get all relationships attached to a specific contact. |
| Get Task | `getTask` | Retrieve a single task by Uid. |
| Get Tasks | `getTasks` | List tasks in a date range. StartDate and EndDate are required (YYYY-MM-DD). |
| Get Tasks Attached To Contact | `getTasksAttachedToContact` | Get all tasks attached to a specific contact. |
| Get Team | `getTeam` | Retrieve a single team by Uid. |
| Get Teams | `getTeams` | List all teams. Response is an array of team objects. |
| Get User | `getUser` | Returns the current API user (the account whose API key is used). |
| Get Users | `getUsers` | Return all users you have access to see. Admins see all users. Response is an array of user objects. |
| Get Webhook | `getWebhook` | Retrieve a single webhook by Uid. |
| Get Webhooks | `getWebhooks` | List all webhooks on the account. Set IncludeArchived to include archived. Response is an array. |

</details>
