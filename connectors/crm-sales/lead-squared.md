---
description: "LeadSquared sales and marketing CRM."
hidden: true
---

# LeadSquared

LeadSquared sales and marketing CRM. Wraps the LeadSquared v2 REST API (apidocs.leadsquared.com): leads and their custom fields, notes, activities and activity types, tasks and appointments, opportunities, static and dynamic lists, users, sales groups, email campaigns and one-off lead emails, and webhook registration. The API host is region-specific (Singapore, US, India Mumbai/Hyderabad, Middle East, Ireland, Canada), so the host is supplied per connection alongside the access key and secret key; credentials are sent on every request as the x-LSQ-AccessKey and x-LSQ-SecretKey headers.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [leadsquared.com](https://leadsquared.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 58 |
| **Events** | 18 |
| **Slug** | `leadSquared` |

## Use it

Add LeadSquared from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.leadSquared.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Leads to Static List | `addLeadsToStaticList` | Add one or more leads to a static list. Leads already on the list are ignored rather than duplicated. Works only on static lists - dynamic and refreshable lists compute their own membership. |
| Capture Opportunity | `captureOpportunity` | Create an opportunity, creating or matching its lead in the same call. leadDetails identifies the lead (at least one unique attribute plus a SearchBy pair); opportunityEventCode is the opportunity type's code from Get Opportunity Types; opportunityFields carries the opportunity's field values. Returns CreatedOpportunityId and the related lead id. |
| Create Activity on Lead | `createActivity` | Post a custom activity against a lead. ActivityEvent is the numeric event code of the activity type - get the codes from Get Activity Types. Custom activity fields are supplied as an array of SchemaName/Value pairs. Returns the new activity id. |
| Create Custom Lead Field | `createCustomLeadField` | Create a new custom lead field on the account. LeadSquared assigns the mx_ schema name itself and returns the new field's id. Dropdown-style fields take their values through OptionsJson. |
| Create Lead | `createLead` | Create a new lead in LeadSquared. The body is LeadSquared's attribute-value array: a JSON array of {"Attribute": schemaName, "Value": value} objects. At least one unique identifying attribute (EmailAddress or Phone) must be present. Standard schema names include EmailAddress, FirstName, LastName, Phone, Company, ProspectStage, Source, OwnerId; account-specific custom fields use their mx_ schema name. Returns the new ProspectID. |
| Create Leads in Bulk | `createLeadsInBulk` | Create up to 50 leads in a single call. The body is an array of attribute-value arrays, one inner array per lead. Returns a per-row result with the created LeadId and a LeadCreated flag. Counts against the stricter bulk rate limit (5 or 10 calls per 5 seconds depending on plan). |
| Create Note | `createNote` | Add a note to a lead, optionally with a file attached by URL. LeadSquared downloads the URL in AttachmentName and stores it against the note. Returns the new ProspectNoteId. |
| Create or Update Lead | `createOrUpdateLead` | Upsert a lead: create it if no match is found, otherwise update the existing one. Matching is controlled by a SearchBy attribute in the body (for example {"Attribute":"SearchBy","Value":"EmailAddress"}). Returns the lead's ProspectID and the number of rows affected. |
| Create Sales Group | `createSalesGroup` | Create a sales group (user group). Name is mandatory. Returns the new group id. |
| Create Static List | `createStaticList` | Create a new, empty static lead list. Returns the new list id, which Add Leads to Static List and Send Email Campaign to List then take. |
| Create Task | `createTask` | Create a to-do or an appointment. The task type name decides which: appointment task types have Category 0 and to-do types have Category 1 - list them with Get Task Types. RelatedEntity is 0 for a standalone task, 1 to attach it to a lead, and 5 to attach it to an opportunity. Returns the new task id. |
| Create User | `createUser` | Create a LeadSquared user. FirstName, EmailAddress and Role are mandatory. Role must be one of Administrator, Marketing_User, Sales_Manager or Sales_User. Returns the new user's id. |
| Create Webhook | `createWebhook` | Register a webhook that LeadSquared will POST to when the chosen event fires. WebhookEvent is a numeric event code as a string: 1 landing page submission, 2 lead activity create, 3 lead create, 4 lead owner change, 5 lead stage change, 6 lead update, 7 task create, 8 task reminder, 9 lead score change, 15 lead activity update, 16 task complete, 17 task update, 26 lead field update, 31 opportunity create, 32 opportunity update, 33 opportunity field update, 34 opportunity stage update, 35 opportunity delete. Returns the new webhook id. |
| Delete Activity | `deleteActivity` | Delete a single custom activity by its id. LeadSquared exposes this as a GET. The activity type must allow deletion (CanDeleteActivity on the type). |
| Delete Lead | `deleteLead` | Permanently delete a lead and everything attached to it - opportunities, activities, tasks, notes, audit history and files. This cannot be reversed and there is no bulk equivalent. LeadSquared exposes this as a GET, and the endpoint is disabled by default: LeadSquared support must enable it on the account first. |
| Delete Opportunity | `deleteOpportunity` | Delete an opportunity by id. LeadSquared exposes this as a GET. The opportunity type must have been created with Allow Delete enabled, otherwise the call fails. |
| Delete Sales Group | `deleteSalesGroup` | Delete a sales group by id. The group id comes from Get Sales Groups and is sent in the request body, not the query string. |
| Delete Task | `deleteTask` | Delete a task by its id. LeadSquared exposes this as a GET. Returns the number of rows affected. |
| Delete Webhook | `deleteWebhook` | Delete a registered webhook by id, stopping further deliveries. LeadSquared exposes this as a GET. |
| Get Activity Details | `getActivityDetails` | Retrieve one activity by its id, with every custom field resolved to schema name, display name, value and data type, plus the lead it belongs to. |
| Get Activity Types | `getActivityTypes` | List every activity type configured on the account with its numeric ActivityEvent code, custom field definitions and settings. Call this first to find the event code required by Create Activity on Lead and Get Lead Activities. EventType is 0 for email, 1 for web, 2 for custom and 4 for revenue or sales activities. |
| Get All Lists | `getAllLists` | List every lead list on the account, system-generated and user-created, with its id, type and member count. Optionally filter by list type or by a name search. |
| Get Campaign Statistics | `getCampaignStatistics` | Retrieve per-campaign email statistics for a date range: recipients, delivered, opens, clicks, bounces, unsubscribes and spam complaints. Paged with PageIndex and PageSize. |
| Get Lead Activities | `getLeadActivities` | Retrieve the activities posted on a lead, optionally narrowed to one activity type. This endpoint pages with Offset and RowCount rather than PageIndex and PageSize. Each activity carries its event code, type, custom field values and a Data array of extra key-value pairs. |
| Get Lead by Email Address | `getLeadByEmail` | Retrieve a lead by its EmailAddress field. Returns a bare array with the matching lead, or an empty array when no lead has that address. |
| Get Lead by Id | `getLeadById` | Retrieve a single lead by its ProspectID, returning every populated lead field including custom mx_ fields. LeadSquared returns a bare array containing at most one lead; an unknown id yields an empty array. |
| Get Lead by Phone Number | `getLeadByPhone` | Retrieve a lead by its Phone or Mobile field. If several leads share the number, LeadSquared returns the one with the most recent activity. Pass digits only, with or without a country code, and without spaces or hyphens. |
| Get Lead Field Metadata | `getLeadMetadata` | Retrieve the properties of every lead field on the account, standard and custom: schema name, display name, data type, render type, mandatory flag, validation and dropdown option sets. This is the source of truth for the mx_ schema names used by the lead write actions. Set excludeOptionSets to 1 to drop dropdown values and speed the call up. |
| Get Lead Notes | `getLeadNotes` | Retrieve the notes attached to a lead, paged and sorted. Pass a note id in noteId to fetch one specific note, or an empty string to return all of the lead's notes. Each note carries its attachment name and CDN URL when one is present. |
| Get Lead Owner | `getLeadOwner` | Get the user who owns a lead, identified by any lead field rather than only the id. Pass the field name in LeadIdentifier and the value in value. Returns the owner's user record including role, team and time zone. |
| Get Leads by Date Range | `getLeadsByDateRange` | List leads modified between two timestamps. Useful as an incremental sync source. A single call returns at most 5000 leads, so page through with PageIndex. Each lead comes back as a LeadPropertyList of attribute-value pairs rather than a flat object. |
| Get Leads in a List | `getLeadsInList` | Retrieve the leads that belong to a static or dynamic list, selecting which columns come back. Each lead is returned as a LeadPropertyList of attribute-value pairs. |
| Get Lists by Lead Id | `getListsByLeadId` | Return every list a given lead currently belongs to, as id and name pairs. |
| Get Opportunities of a Lead | `getOpportunitiesOfLead` | List the opportunities belonging to one lead, optionally restricted to a single opportunity type, selecting which opportunity columns come back. Paged with PageIndex and PageSize. |
| Get Opportunity by Id | `getOpportunityById` | Retrieve a single opportunity with every field resolved to schema name, display name, value and data type, plus the related lead. Set getFileURL to true to have file-type fields returned as downloadable URLs. |
| Get Opportunity Types | `getOpportunityTypes` | List every opportunity type on the account with its numeric EventCode. The EventCode is required by Capture Opportunity and Search Opportunities. |
| Get Sales Groups | `getSalesGroups` | List the sales groups (user groups) on the account with their ids, descriptions and member counts. Supply a UserId to return only the groups that user belongs to. |
| Get Sent Emails | `getSentEmails` | Retrieve individual email events in a date range - sends, opens, clicks, unsubscribes, resubscribes and view-in-browser clicks - each linked to the lead it concerned. Paged with PageIndex and PageSize. |
| Get Task by Id | `getTaskById` | Retrieve one task by its UserTaskId, including status, owner, reminder and the related lead or opportunity. LeadSquared returns a bare array with at most one task. |
| Get Task Types | `getTaskTypes` | List the task types configured on the account, with their ids, category (0 appointment, 1 to-do) and column configuration. Supply the Name to Create Task and the Id to Search Tasks. Results can be filtered with a ColumnName and ColumnValue pair. |
| Get Tasks by Lead Id | `getTasksByLeadId` | List every task attached to a lead, with owner, due date, status and reminder. Note this endpoint lives under LeadManagement.svc rather than Task.svc. |
| Get User by Email Address | `getUserByEmail` | Retrieve a user by email address, including role, phone numbers, time zone and org id. Returns an empty array if the user is inactive or does not exist. |
| Get User by Id | `getUserById` | Retrieve one user by UserId, including role, manager, designation, department and current check-in and availability status. Returns an empty array if the user is inactive or does not exist. |
| Get Users | `getUsers` | List every user on the LeadSquared account with id, name, email, role and group membership. StatusCode 0 means active and 1 means inactive. This action takes no inputs, so it doubles as a cheap connection check. |
| List Webhooks | `listWebhooks` | List the webhooks registered on the account, paged and filterable. Note the asymmetry: Create Webhook takes a NUMERIC event code while this endpoint filters on the STRING event code (for example Lead_Post_Create) and returns both EventName and EventCode in string form. |
| Mark Task Complete | `markTaskComplete` | Mark a task as complete by its id. LeadSquared exposes this as a GET. Returns the number of rows affected. |
| Quick Search Leads | `quickSearchLeads` | Search leads the same way the LeadSquared web app's Quick Search box does. The key is matched across FirstName, LastName, EmailAddress, Phone, Mobile, Company, City and Country. Returns a bare array of matching leads. |
| Remove Lead from Static List | `removeLeadFromStaticList` | Remove a single lead from a static list. LeadSquared exposes this as a GET and it removes exactly one lead per call - there is no bulk form. Note the parameter casing: ListId and LeadID. |
| Search Leads by Criteria | `searchLeadsByCriteria` | Search leads with an explicit field comparison: a lead field name, a value, and a SQL operator. Choose which columns come back with a CSV list, and page through results. Returns a bare array of lead objects containing only the requested columns. |
| Search Opportunities | `searchOpportunities` | Advanced search across opportunities of one type. The advancedSearch input is LeadSquared's serialised condition JSON, passed as a string. Paged with PageIndex and PageSize. |
| Search Tasks | `searchTasks` | Search tasks by owner, date window, status and task type. Pages with Offset and RowCount. StatusCode 0 is pending and 1 is complete. TypeName takes a task type id from Get Task Types. |
| Send Email Campaign to List | `sendEmailCampaignToList` | Send an email campaign built from a saved template to every lead on a list. Returns the campaign id, the list's member count and how many recipients actually qualified. Campaign reports become available about 20 minutes after sending. |
| Send Email to Lead | `sendEmailToLead` | Send a one-off email to a single lead, either from inline HTML or from a saved email template. Set schedule to a future timestamp to queue it, or leave it empty to send immediately. Returns the email's id and recipient count. |
| Update Activity | `updateActivity` | Update an existing custom activity by its ProspectActivityId. Only the custom fields listed in Fields are written; pass an empty Value to clear one. The activity's own type code must be repeated in ActivityEvent. |
| Update Lead | `updateLead` | Update an existing lead identified by its ProspectID. Only the attributes present in the body are written; every other field on the lead is left untouched. Returns the number of rows affected. |
| Update Opportunity | `updateOpportunity` | Update an existing opportunity by its id. Only the fields listed in fields are written. Use this to move an opportunity's Status, change its value, or set custom fields. Returns the opportunity id. |
| Update Task | `updateTask` | Update an existing task by its UserTaskId - rename it, change its description, due date, reminder, owner, or which lead or opportunity it hangs off. Returns the number of rows affected and the task's auto id. |
| Update Webhook | `updateWebhook` | Update a registered webhook by its WebhookId - change its destination URL, event, content type or custom headers. WebhookId is mandatory. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Landing Page Submitted | `1` | Fires when a LeadSquared landing page form is submitted. Event code 1. Set Is Specific Landing Page on the registration to restrict it to named pages. Schema derived from the published Lead Created sample, which is the entity the submission produces. |
| Lead Activity Created | `2` | Fires when an activity is posted on a lead. Event code 2. Payload schema is LeadSquared's published sample for this event; custom activity fields appear as additional mx_ keys. |
| Lead Activity Updated | `15` | Fires when an existing lead activity is edited. Event code 15. Schema derived from the published Lead Activity Created sample. |
| Lead Created | `3` | Fires when a lead is created. Event code 3 (Lead_Post_Create). Payload schema is LeadSquared's published sample for this event. |
| Lead Field Updated | `26` | Fires when a specific watched lead field changes. Event code 26. Same Before/After envelope as Lead Updated, narrowed to the watched field. Schema derived from the published Lead Updated sample. |
| Lead Owner Changed | `4` | Fires when a lead is reassigned to a different user. Event code 4. Before/After envelope carrying the owner. Schema derived from the published Lead Stage Changed sample, which uses the same envelope. |
| Lead Score Changed | `9` | Fires when a lead's score changes. Event code 9. Before/After envelope carrying the score. Schema derived from the published Lead Stage Changed sample, which uses the same envelope. |
| Lead Stage Changed | `5` | Fires when a lead moves between stages. Event code 5. Payload schema is LeadSquared's published sample for this event. |
| Lead Updated | `6` | Fires when any lead field changes. Event code 6. The body is a Before/After pair of partial lead objects containing only the changed fields. Payload schema is LeadSquared's published sample. |
| Opportunity Created | `31` | Fires when an opportunity is created. Event code 31. Payload schema is LeadSquared's published sample; opportunity custom fields appear as additional mx_ keys and ActivityEvent carries the opportunity type code. |
| Opportunity Deleted | `35` | Fires when an opportunity is deleted. Event code 35. Schema derived from the published Opportunity Created sample. |
| Opportunity Field Updated | `33` | Fires when a specific watched opportunity field changes. Event code 33. Schema derived from the published Opportunity Created sample. |
| Opportunity Stage Updated | `34` | Fires when an opportunity's Status or stage changes. Event code 34. Schema derived from the published Opportunity Created sample. |
| Opportunity Updated | `32` | Fires when an opportunity is edited. Event code 32. Schema derived from the published Opportunity Created sample. |
| Task Completed | `16` | Fires when a task is marked complete. Event code 16. Schema derived from the published Task Created sample. |
| Task Created | `7` | Fires when a task or appointment is created. Event code 7. Payload schema is LeadSquared's published sample for this event. |
| Task Reminder | `8` | Fires at a task's configured reminder time. Event code 8. Schema derived from the published Task Created sample. |
| Task Updated | `17` | Fires when a task is edited. Event code 17. Schema derived from the published Task Created sample. |
