---
description: "Reply.io sales engagement platform."
hidden: true
---

# Reply.io

<img src="../../.gitbook/assets/connectors/replyio.png" alt="Reply.io logo" width="64">

Reply.io sales engagement platform. Manage contacts, contact lists, custom fields, multichannel sequences (email/LinkedIn/calls/tasks), sequence steps and contacts, email templates, email/LinkedIn accounts, tasks, schedules, holiday calendars, unified inbox, reporting, blacklist rules, email validation, and webhooks via the Reply v3 REST API (plus legacy v1 campaigns).

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [reply.io](https://reply.io) |
| **Authentication** | API key |
| **Slug** | `replyio` |

## Use it

Add Reply.io from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.replyio.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact Note | `addContactNote` | Append a note to a contact. |
| Add Contacts To List | `addContactsToList` | Add contacts to a contact list. |
| Add Contacts To Sequence | `addContactsToSequence` | Add existing contacts to a sequence (bulk). Optionally set start step, timing, and whether to remove them from other sequences. |
| Archive Sequence | `archiveSequence` | Archive a sequence by id. |
| Batch Complete Tasks | `batchCompleteTasks` | Complete multiple tasks by id. |
| Bulk Delete Contacts | `bulkDeleteContacts` | Delete multiple contacts by id. |
| Change Contacts Owner | `changeContactsOwner` | Reassign the owner of one or more contacts to a user; optionally reassign their tasks. |
| Change Sequence Owner | `updateSequenceOwner` | Change the owner of a sequence. |
| Clone Email Template | `cloneEmailTemplate` | Clone an existing email template. |
| Complete Task | `completeTask` | Mark a single task as completed, optionally recording a call resolution and finishing the contact in its sequence. Reply rejects a body-less request, so finishProspectInSequence must always be supplied. |

<details>

<summary>See 98 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Contact | `createContact` | Create a contact in Reply. Company name, company size and industry live on the linked account, not the contact - pass accountId to link one. Free-text notes are added with the Add Contact Note action, not here. |
| Create Contact List | `createContactList` | Create a new contact list. |
| Create Custom Field | `createCustomField` | Create a custom contact field. 'title' is the field name/label (required). fieldType is text or number. 'metadata' is optional extra config. Set orgWide to make it available org-wide. |
| Create Email Template | `createEmailTemplate` | Create an email template. name, body, and folderType (personal/team) are required. |
| Create Email Template Folder | `createEmailTemplateFolder` | Create an email template folder (personal or team). |
| Create Holiday Calendar | `createHolidayCalendar` | Create a holiday calendar. holidays is an array of {startDate,endDate,name} (dates are YYYY-MM-DD). |
| Create Schedule | `createSchedule` | Create a sending schedule. mainTimings define active weekdays and time ranges (hour/minute). timezoneId is a Windows time zone name such as 'Eastern Standard Time' (see List Schedules), not an IANA id. |
| Create Sequence | `createSequence` | Create a sequence in Reply. At least one step is required at creation time. The sequence is created in the 'new' state and does not send anything until it is started. |
| Create Sequence Step | `createSequenceStep` | Add a step to a sequence. 'type', 'delayInMinutes' are always required. Email/SMS steps also require 'executionMode' and 'variants'/'message'. For email steps pass variants (each with subject/message). |
| Create Sequence Step Variant | `createSequenceStepVariant` | Add a message variant to a sequence step. |
| Create Task | `createTask` | Create a manual task (toDo, call, or meeting). startAt and dueTo are ISO date-times. For LinkedIn tasks set linkedInTaskType. 'template' carries the message subject/body. |
| Create Webhook | `createWebhook` | Create a webhook subscription. eventType must be one of the values from List Webhook Events (e.g. contact_reply_recorded, email_replied, email_opened). url is your receiving endpoint. scope: personal/team/organization. |
| Delete Contact | `deleteContact` | Delete a contact by id. |
| Delete Contact List | `deleteContactList` | Delete a contact list by id. |
| Delete Custom Field | `deleteCustomField` | Delete a custom field by id. |
| Delete Email Template | `deleteEmailTemplate` | Delete an email template by id. KNOWN UPSTREAM DEFECT (verified 2026-09-01): Reply.io returns 204 No Content but does NOT delete the template - Get Email Template still returns 200 with the full resource and List Email Templates still includes it, 30+ seconds later. The endpoint matches Reply.io's documented DELETE /v3/email-templates/{id}; do not treat the 204 as proof of deletion. |
| Delete Email Template Folder | `deleteEmailTemplateFolder` | Delete an email template folder. Templates inside the folder are kept and become unfiled. The folder type must be supplied as well as the folder id - Reply answers 400 'Field is required.' on /folder_type without it. |
| Delete Holiday Calendar | `deleteHolidayCalendar` | Delete a holiday calendar by id. |
| Delete Schedule | `deleteSchedule` | Delete a schedule by id. |
| Delete Sequence | `deleteSequence` | Delete a sequence by id. |
| Delete Sequence Step | `deleteSequenceStep` | Delete a sequence step by id. Verified working on a multi-step sequence (204, step gone from List Sequence Steps). Reply.io refuses to delete the LAST remaining step: a single-step sequence returns 400 'Cannot remove the step. There is only one step in sequence' - delete the sequence itself instead. Optional 'mode' controls handling of contacts sitting on that step. |
| Delete Task | `deleteTask` | Delete a task by id. |
| Delete Webhook | `deleteWebhook` | Delete a webhook subscription by id. |
| Disable Webhook | `disableWebhook` | Disable a webhook subscription. |
| Enable Webhook | `enableWebhook` | Enable a webhook subscription. |
| Filter Contacts | `filterContacts` | Search/filter contacts using structured rules, list, sequence, or a free-text term. |
| Filter Email Accounts | `filterEmailAccounts` | Filter email accounts by connection status, type, email, domains, owners, or tags. |
| Filter Tasks | `filterTasks` | Filter tasks by date range, type, status, sequence, contact, or assignee. |
| Get All Sequences Stats | `getAllSequencesStats` | Get aggregate stats for all sequences within a date range (email + LinkedIn overviews per sequence). |
| Get Calls Report Overview | `getCallsReportOverview` | Get aggregate calls reporting for a date range. |
| Get Contact | `getContact` | Get a single contact by its numeric id. |
| Get Contact Activities | `getContactActivities` | Get the activity/timeline events for a contact. |
| Get Contact List | `getContactList` | Get a contact list by id. |
| Get Contact Lists For Contact | `getContactContactLists` | List the contact lists a given contact belongs to. KNOWN UPSTREAM DEFECT (verified 2026-09-01): Reply.io returns 200 with an empty array even for a contact that IS in a list - Add Contacts To A Contact List succeeded and Filter Contacts by that listId returns the same contact. The endpoint matches Reply.io's documented GET /v3/contacts/{id}/lists. Use Filter Contacts with listId as a reliable substitute. |
| Get Contact Sequences | `getContactSequences` | List the sequences a contact currently belongs to with per-sequence status. |
| Get Contact Statuses | `getContactStatuses` | Get a contact's status flags (opted-out, call status, meeting status) and per-sequence status. |
| Get Current User | `getCurrentUser` | Return the current authenticated Reply user (userId and username). Use to verify credentials and obtain your userId for owner-assignment actions. |
| Get Custom Field | `getCustomField` | Get a custom field by id. |
| Get Email Report Overview | `getEmailReportOverview` | Get aggregate email reporting for a date range. filters requires a date range (from/to) or a dateRangePreset. |
| Get Email Template | `getEmailTemplate` | Get an email template by id. |
| Get Email Template Variables | `getEmailTemplateVariables` | Get available template variables (prospect, team, advanced). |
| Get Holiday Calendar | `getHolidayCalendar` | Get a holiday calendar (with its holidays) by id. |
| Get LinkedIn Report Overview | `getLinkedInReportOverview` | Get aggregate LinkedIn reporting for a date range. |
| Get Schedule | `getSchedule` | Get a schedule by id. |
| Get Sequence | `getSequence` | Get a sequence by id including settings, accounts, and status. |
| Get Sequence Stats | `getSequenceStats` | Get stats for a single sequence within a date range. |
| Get Sequence Step | `getSequenceStep` | Get a single sequence step by id. |
| Get Settings | `getSettings` | Get the account settings (profile, email safety/sending limits, defaults). |
| Get Task | `getTask` | Get a task by id. Optionally include the message content. |
| Get Tasks Report Overview | `getTasksReportOverview` | Get aggregate task reporting for a date range. |
| Get Webhook | `getWebhook` | Get a webhook subscription by id. |
| Get Webhook Logs | `getWebhookLogs` | Get delivery logs for a webhook subscription. |
| Import Contacts | `importContacts` | Bulk import/upsert contacts asynchronously. Returns per-item results plus added/updated/skipped/failed counts (runs as a background job). |
| List Campaigns (v1) | `listCampaignsV1` | Legacy v1 API: list all campaigns (the v1 equivalent of sequences) with basic status counts. The only v1 endpoint in this connector and metered on a separate, much tighter quota than v3 - this account is exhausted and every call returns 400 'Api-requests limit reached'. Prefer List Sequences (GET /v3/sequences) plus Get Sequence Stats, which are on the v3 quota. Candidate for retirement. |
| List Contact Lists | `listContactLists` | List contact lists with pagination and optional name search. |
| List Contacts | `listContacts` | List contacts with pagination. Optionally filter by exact email or LinkedIn URL. |
| List Custom Fields | `listCustomFields` | List all custom contact fields. |
| List Email Account Tags | `listEmailAccountTags` | List all email-account tags. |
| List Email Accounts | `listEmailAccounts` | List connected email sending accounts. |
| List Email Template Folders | `listEmailTemplateFolders` | List email template folders. |
| List Email Templates | `listEmailTemplates` | List email templates with pagination and optional filters. |
| List Holiday Calendars | `listHolidayCalendars` | List all holiday calendars. |
| List LinkedIn Accounts | `listLinkedInAccounts` | List connected LinkedIn accounts. |
| List Schedule Holiday Calendars | `listScheduleHolidayCalendars` | List holiday calendars linked to a schedule. |
| List Schedules | `listSchedules` | List sending schedules. |
| List Sequence Contacts | `listSequenceContacts` | List contacts in a sequence with their in-sequence status. |
| List Sequence Contacts State | `listSequenceContactsState` | List contacts in a sequence with extended per-step state. |
| List Sequence Step Variants | `listSequenceStepVariants` | List message variants of a sequence step. |
| List Sequence Steps | `listSequenceSteps` | List all steps of a sequence. |
| List Sequences | `listSequences` | List sequences with pagination and optional filters (status, owner, folder, archived, name). |
| List Tasks | `listTasks` | List manual tasks with pagination. |
| List Webhook Events | `listWebhookEvents` | List the supported webhook event type strings. |
| List Webhooks | `listWebhooks` | List webhook subscriptions. |
| Mark Contacts Bounced | `markContactsBounced` | Mark contacts as bounced, or clear the bounced flag. Returns HTTP 200 with a per-contact result map - check each entry for an error field before treating the call as successful. Contacts that are not in a sequence are skipped. |
| Mark Contacts Replied | `markContactsReplied` | Mark or unmark contacts as replied across every sequence they are in. PARTIAL SUCCESS API: HTTP 200 does not mean every contact was processed. The response is a map keyed by contactId containing ONLY the contacts that FAILED (e.g. {"760754079":{"error":"invalidInput","errorDetails":"Skipped: NotInSequence"}}); a contactId absent from the map succeeded. An empty object means all succeeded. Callers must inspect the map. |
| Move Contacts To List | `moveContactsToList` | Move contacts into a contact list (removing them from their current list). |
| Pause Sequence | `pauseSequence` | Pause a RUNNING sequence by id. The sequence must have been started at least once; pausing a sequence in status 'new' (never started) returns 403 sequenceAction.forbidden 'You do not have permission to pause sequence' - a misleading message for what is a state precondition, not a permissions problem. |
| Reassign Task | `assignTask` | Reassign a task to another user. |
| Remove Contact From Sequence | `removeContactFromSequence` | Remove a single contact from a sequence. |
| Render Email Template | `renderEmailTemplate` | Render an email template for a specific contact (resolves variables). Returns subject/body and any variable errors. |
| Set Default Schedule | `setDefaultSchedule` | Set a schedule as the account default. |
| Set Sequence Contact Status | `setSequenceContactStatus` | Set the in-sequence status (pause/resume/finish) for contacts in a sequence. |
| Set Sequence Contacts Replied | `setSequenceContactsReplied` | Mark or unmark contacts as replied within a specific sequence. |
| Share Contact List | `shareContactList` | Share a contact list with the team. |
| Start Sequence | `startSequence` | Start/activate a sequence by id. Requires the sequence to have at least one step and a connected sending account. |
| Test Webhook | `testWebhook` | Send a test payload to a webhook subscription's URL. |
| Unshare Contact List | `unshareContactList` | Stop sharing a contact list with the team. |
| Update Contact | `updateContact` | Partially update a contact in Reply. Company name, company size and industry cannot be set here - they come from the linked account, so pass accountId instead. Free-text notes are added with the Add Contact Note action. |
| Update Contact List | `updateContactList` | Rename a contact list. |
| Update Custom Field | `updateCustomField` | Update a custom field's name (title), type, or metadata. |
| Update Email Template | `updateEmailTemplate` | Update an email template's name, subject, or body. |
| Update Email Template Folder | `updateEmailTemplateFolder` | Rename an email template folder. The folder type must be supplied as well as the folder id - Reply answers 400 'Field is required.' on /folder_type without it. |
| Update Holiday Calendar | `updateHolidayCalendar` | Update a holiday calendar and its holidays. |
| Update Schedule | `updateSchedule` | Update a sending schedule. |
| Update Sequence | `updateSequence` | Partially update a sequence (name, schedule, settings, accounts). |
| Update Sequence Step | `updateSequenceStep` | Update a sequence step. Same body shape as create. |
| Update Task | `updateTask` | Replace an OPEN task in full (status 'new'). Reply.io only allows updating open tasks: a completed, failed or otherwise closed task returns 404 'Task not found or insufficient permissions' even though Get Task still returns it with 200. taskType, startAt, dueTo and the template body must be sent every time - omitted fields are cleared, not preserved. |
| Update Webhook | `updateWebhook` | Update a webhook subscription (eventType, url, scope, payloadConfig). |

</details>
