---
description: "CentralStationCRM is a German customer relationship management platform for small and mid-sized teams."
---

# CentralStationCRM

CentralStationCRM is a German customer relationship management platform for small and mid-sized teams. This connector covers the full CentralStationCRM REST API: people, companies, deals, projects, tasks, protocols, comments, tags, addresses, contact details, custom fields, calendar events, attachments, avatars, external emails, filter groups, users and webhooks.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [centralstationcrm.net](https://centralstationcrm.net) |
| **Authentication** | Credentials you enter |
| **Actions** | 201 |
| **Events** | 15 |
| **Slug** | `centralStationCrm` |

## Use it

Add CentralStationCRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.centralStationCrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check API Connection | `checkApiConnection` | Verifies that the configured CentralStationCRM API key and account name are valid and that the API is reachable. Returns an empty object on success. |
| Count Activities | `countActivities` | Returns the total number of activities in CentralStationCRM for the given record, user or account scope. |
| Count Attachments | `countAttachments` | Returns the total number of attachments in the CentralStationCRM account and their combined file size. |
| Count Avatars | `countAvatars` | Returns the total number of avatar images in the CentralStationCRM account and their combined file size. |
| Count Companies | `countCompanies` | Returns the total number of companies in the CentralStationCRM account, optionally narrowed by tag or by field filters. This endpoint accepts the same filter[field][operator] query parameters as List Companies; the most commonly used field filters are modelled here. |
| Count Company External Emails | `countCompanyExternalEmails` | Returns the number of external emails filed against the given company in CentralStationCRM. |
| Count Deal External Emails | `countDealExternalEmails` | Returns the number of external emails filed against the given deal in CentralStationCRM. |
| Count Deals | `countDeals` | Returns the total number of deals in the CentralStationCRM account, optionally narrowed by tag or by field filters. This endpoint accepts the same filter[field][operator] query parameters as List Deals; the most commonly used field filters are modelled here. |
| Count External Emails | `countExternalEmails` | Returns the total number of external emails filed in the CentralStationCRM account. |
| Count Filter Group Records | `countFilterGroupRecords` | Returns the number of records matching the given CentralStationCRM filter group. |
| Count People | `countPeople` | Returns the total number of people in the CentralStationCRM account, optionally narrowed by tag or by field filters. This endpoint accepts the same filter[field][operator] query parameters as List People; the most commonly used field filters are modelled here. |
| Count Person External Emails | `countPersonExternalEmails` | Returns the number of external emails filed against the given person in CentralStationCRM. |
| Count Project External Emails | `countProjectExternalEmails` | Returns the number of external emails filed against the given project in CentralStationCRM. |
| Count Projects | `countProjects` | Returns the total number of projects in the CentralStationCRM account, optionally narrowed by tag or by field filters. This endpoint accepts the same filter[field][operator] query parameters as List Projects; the most commonly used field filters are modelled here. |
| Count Protocols | `countProtocols` | Returns the total number of protocols (notes, call logs and email records) in the CentralStationCRM account. |
| Create Attachment | `createAttachment` | Uploads a new attachment to CentralStationCRM and links it to a protocol, comment or external email. The file content is supplied Base64-encoded. |
| Create Calendar Event | `createCalendarEvent` | Creates a new calendar event in CentralStationCRM. Leave email invitations disabled to avoid sending invitation emails to attendees. |
| Create Calendar Event Attendee | `createCalendarEventAttendee` | Adds an attendee to the given calendar event in CentralStationCRM. Use the status no_invite to add an attendee without sending an email invitation. |
| Create Comment | `createComment` | Creates a new comment in CentralStationCRM on an attachment, calendar event, protocol, external email or task. |
| Create Company | `createCompany` | Creates a new company in CentralStationCRM. |
| Create Company Address | `createCompanyAddress` | Creates a new address on the given company in CentralStationCRM. |
| Create Company Avatar | `createCompanyAvatar` | Uploads a new avatar image for the given company in CentralStationCRM. The image content is supplied Base64-encoded. |
| Create Company Contact Detail | `createCompanyContactDetail` | Adds a contact detail to the given company in CentralStationCRM. The body key selects the kind of contact detail: tel, email, homepage or im. |
| Create Company Protocol Attachment | `createCompanyProtocolAttachment` | Uploads an attachment to the given protocol under the given company in CentralStationCRM. The file content is supplied Base64-encoded. |
| Create Custom Field Type | `createCustomFieldType` | Creates a new custom field type in CentralStationCRM, defining an extra field that can be filled in on people, companies, deals or projects. |
| Create Deal | `createDeal` | Creates a new deal in CentralStationCRM within the given pipeline. The API requires a name, pipeline, value and target date. |
| Create Deal Protocol Attachment | `createDealProtocolAttachment` | Uploads an attachment to the given protocol under the given deal in CentralStationCRM. The file content is supplied Base64-encoded. |
| Create External Email Attachment | `createExternalEmailAttachment` | Uploads an attachment to the given external email in CentralStationCRM. The file content is supplied Base64-encoded. |
| Create Group Calendar | `createGroupCalendar` | Creates a new shared group calendar in CentralStationCRM that calendar events can be placed in. |
| Create Person | `createPerson` | Creates a new person (contact) in CentralStationCRM. |
| Create Person Address | `createPersonAddress` | Creates a new address on the given person in CentralStationCRM. |
| Create Person Assistant | `createPersonAssistant` | Records an assistant for the given person in CentralStationCRM. |
| Create Person Avatar | `createPersonAvatar` | Uploads a new avatar image for the given person in CentralStationCRM. The image content is supplied Base64-encoded. |
| Create Person Contact Detail | `createPersonContactDetail` | Adds a contact detail to the given person in CentralStationCRM. The body key selects the kind of contact detail: tel, email, homepage or im. |
| Create Person Custom Field | `createPersonCustomField` | Stores a custom field value on the given person in CentralStationCRM. The custom field type must already exist; use List Custom Field Types to look up its ID. |
| Create Person Historic Event | `createPersonHistoricEvent` | Records a historic event such as a birthday, anniversary or first-met date for the given person in CentralStationCRM. |
| Create Person Position | `createPersonPosition` | Creates a position for the given person in CentralStationCRM, linking them to a company with a job title and department. |
| Create Person Protocol Attachment | `createPersonProtocolAttachment` | Uploads an attachment to the given protocol under the given person in CentralStationCRM. The file content is supplied Base64-encoded. |
| Create Person Tag | `createPersonTag` | Adds a tag to the given person in CentralStationCRM. The attachable type and ID are set automatically from the route. |
| Create Project | `createProject` | Creates a new project in CentralStationCRM, optionally linked to a company and to the deal it originated from. |
| Create Project Protocol Attachment | `createProjectProtocolAttachment` | Uploads an attachment to the given protocol under the given project in CentralStationCRM. The file content is supplied Base64-encoded. |
| Create Protocol | `createProtocol` | Creates a new protocol (note, call log or email record) in CentralStationCRM and assigns it to the given people, companies, deals or projects. An attachment can be uploaded with the protocol in the same call. |
| Create Protocol Attachment | `createProtocolAttachment` | Uploads an attachment to the given protocol in CentralStationCRM. The file content is supplied Base64-encoded. |
| Create Tag | `createTag` | Creates a tag on any person, company, deal or project in CentralStationCRM. The target record is identified by the attachable type and ID. |
| Create Task | `createTask` | Creates a new task in CentralStationCRM, optionally attached to a person, company, deal or project. |
| Create Webhook | `createWebhook` | Registers a new webhook subscription in CentralStationCRM so that create, update or destroy events on people, companies, deals, projects or protocols are delivered to the given target URL. New webhooks are always created active. |
| Delete Attachment | `deleteAttachment` | Permanently deletes an attachment from CentralStationCRM by its ID. This cannot be undone. |
| Delete Avatar | `deleteAvatar` | Permanently deletes an avatar image from CentralStationCRM by its ID. This cannot be undone. |
| Delete Calendar Event | `deleteCalendarEvent` | Permanently deletes a calendar event from CentralStationCRM by its ID. This cannot be undone. |
| Delete Calendar Event Attendee | `deleteCalendarEventAttendee` | Removes an attendee from the given calendar event in CentralStationCRM. This cannot be undone. |
| Delete Comment | `deleteComment` | Permanently deletes a comment from CentralStationCRM by its ID. This cannot be undone. |
| Delete Company | `deleteCompany` | Permanently deletes a company from CentralStationCRM by its ID. This cannot be undone. |
| Delete Company Address | `deleteCompanyAddress` | Permanently deletes an address of the given company in CentralStationCRM by its ID. This cannot be undone. |
| Delete Company Avatar | `deleteCompanyAvatar` | Permanently deletes an avatar image of the given company in CentralStationCRM by its ID. This cannot be undone. |
| Delete Company Contact Detail | `deleteCompanyContactDetail` | Permanently deletes a contact detail of the given company in CentralStationCRM by its ID. This cannot be undone. |
| Delete Company Protocol Attachment | `deleteCompanyProtocolAttachment` | Permanently deletes an attachment of the given protocol under the given company in CentralStationCRM by its ID. This cannot be undone. |
| Delete Custom Field Type | `deleteCustomFieldType` | Permanently deletes a custom field type from CentralStationCRM by its ID, together with the values stored against it. This cannot be undone. |
| Delete Deal | `deleteDeal` | Permanently deletes a deal from CentralStationCRM by its ID. This cannot be undone. |
| Delete Deal Protocol Attachment | `deleteDealProtocolAttachment` | Permanently deletes an attachment of the given protocol under the given deal in CentralStationCRM by its ID. This cannot be undone. |
| Delete External Email Attachment | `deleteExternalEmailAttachment` | Permanently deletes an attachment of the given external email in CentralStationCRM by its ID. This cannot be undone. |
| Delete Group Calendar | `deleteGroupCalendar` | Permanently deletes a group calendar from CentralStationCRM by its ID. Read-only calendars created with the account cannot be removed. This cannot be undone. |
| Delete Person | `deletePerson` | Permanently deletes a person (contact) from CentralStationCRM by their ID. This cannot be undone. |
| Delete Person Address | `deletePersonAddress` | Permanently deletes an address of the given person in CentralStationCRM by its ID. This cannot be undone. |
| Delete Person Assistant | `deletePersonAssistant` | Permanently deletes an assistant of the given person in CentralStationCRM by its ID. This cannot be undone. |
| Delete Person Avatar | `deletePersonAvatar` | Permanently deletes an avatar image of the given person in CentralStationCRM by its ID. This cannot be undone. |
| Delete Person Contact Detail | `deletePersonContactDetail` | Permanently deletes a contact detail of the given person in CentralStationCRM by its ID. This cannot be undone. |
| Delete Person Custom Field | `deletePersonCustomField` | Permanently deletes a custom field value from the given person in CentralStationCRM by its ID. The custom field type itself is not affected. This cannot be undone. |
| Delete Person Historic Event | `deletePersonHistoricEvent` | Permanently deletes a historic event of the given person in CentralStationCRM by its ID. This cannot be undone. |
| Delete Person Position | `deletePersonPosition` | Permanently deletes a position of the given person in CentralStationCRM by its ID, removing the link between the person and that company. This cannot be undone. |
| Delete Person Protocol Attachment | `deletePersonProtocolAttachment` | Permanently deletes an attachment of the given protocol under the given person in CentralStationCRM by its ID. This cannot be undone. |
| Delete Person Tag | `deletePersonTag` | Removes a tag from the given person in CentralStationCRM by its ID. This cannot be undone. |
| Delete Project | `deleteProject` | Permanently deletes a project from CentralStationCRM by its ID. This cannot be undone. |
| Delete Project Protocol Attachment | `deleteProjectProtocolAttachment` | Permanently deletes an attachment of the given protocol under the given project in CentralStationCRM by its ID. This cannot be undone. |
| Delete Protocol | `deleteProtocol` | Permanently deletes a protocol from CentralStationCRM by its ID. This cannot be undone. |
| Delete Protocol Attachment | `deleteProtocolAttachment` | Permanently deletes an attachment of the given protocol in CentralStationCRM by its ID. This cannot be undone. |
| Delete Tag | `deleteTag` | Removes a tag from CentralStationCRM by its ID, regardless of the record type it is attached to. Use this to remove tags on companies, deals or projects, which have no record-scoped tag delete endpoint. This endpoint is live but not listed in the vendor's OpenAPI document. |
| Delete Task | `deleteTask` | Permanently deletes a task from CentralStationCRM by its ID. This cannot be undone. |
| Delete Webhook | `deleteWebhook` | Removes a webhook subscription from CentralStationCRM by its ID so that no further events are delivered to its target URL. |
| Get Activity | `getActivity` | Retrieves a single activity from CentralStationCRM by its ID. |
| Get Attachment | `getAttachment` | Retrieves a single attachment from CentralStationCRM by its ID, optionally including the Base64 encoded file content. |
| Get Avatar | `getAvatar` | Retrieves a single avatar image from CentralStationCRM by its ID, including the Base64 encoded file content. |
| Get Calendar Event | `getCalendarEvent` | Retrieves a single calendar event from CentralStationCRM by its ID. |
| Get Calendar Event Attendee | `getCalendarEventAttendee` | Retrieves a single attendee of the given calendar event in CentralStationCRM by its ID. |
| Get Comment | `getComment` | Retrieves a single comment from CentralStationCRM by its ID. |
| Get Companies Statistics | `getCompaniesStatistics` | Returns key statistics about the companies in the CentralStationCRM account, optionally narrowed by tag or by field filters. This endpoint accepts the same filter[field][operator] query parameters as List Companies; the most commonly used field filters are modelled here. |
| Get Company | `getCompany` | Retrieves a single company from CentralStationCRM by its ID. |
| Get Company Address | `getCompanyAddress` | Retrieves a single address of the given company in CentralStationCRM by its ID. |
| Get Company Avatar | `getCompanyAvatar` | Retrieves a single avatar image of the given company in CentralStationCRM by its ID. |
| Get Company Contact Detail | `getCompanyContactDetail` | Retrieves a single contact detail of the given company in CentralStationCRM by its ID. |
| Get Company Protocol Attachment | `getCompanyProtocolAttachment` | Retrieves a single attachment of the given protocol under the given company in CentralStationCRM by its ID. |
| Get Current User | `getCurrentUser` | Retrieves the details of the CentralStationCRM user that the API key belongs to, including the accounts the user can access and the preferred salutations. |
| Get Current User Maildrop Addresses | `getCurrentUserMaildropAddresses` | Retrieves the maildrop email address of the current CentralStationCRM user, used to file emails against people and companies by forwarding them. |
| Get Custom Field Type | `getCustomFieldType` | Retrieves a single custom field type definition from CentralStationCRM by its ID. |
| Get Deal | `getDeal` | Retrieves a single deal from CentralStationCRM by its ID. |
| Get Deal Maildrop Address | `getDealMaildropAddress` | Retrieves the maildrop email address of the given deal in CentralStationCRM. Emails forwarded to this address are filed against the deal. |
| Get Deal Protocol Attachment | `getDealProtocolAttachment` | Retrieves a single attachment of the given protocol under the given deal in CentralStationCRM by its ID. |
| Get Deal Type | `getDealType` | Retrieves a single deal type (sales pipeline) from CentralStationCRM by its ID, including its stages. |
| Get Deals Statistics | `getDealsStatistics` | Returns key statistics about the deals in the CentralStationCRM account, including the summed pipeline value and the account currency. This endpoint accepts the same filter[field][operator] query parameters as List Deals; the most commonly used field filters are modelled here. |
| Get External Email | `getExternalEmail` | Retrieves a single external email from CentralStationCRM by its ID. |
| Get External Email Attachment | `getExternalEmailAttachment` | Retrieves a single attachment of the given external email in CentralStationCRM by its ID. |
| Get Filter Group Records | `getFilterGroup` | Retrieves the records matching the given CentralStationCRM filter group. The row shape follows the filter group's model type (person, company, deal or project). |
| Get Group Calendar | `getGroupCalendar` | Retrieves a single group calendar from CentralStationCRM by its ID. |
| Get People Statistics | `getPeopleStatistics` | Returns key statistics about the people in the CentralStationCRM account, optionally narrowed by tag or by field filters. This endpoint accepts the same filter[field][operator] query parameters as List People; the most commonly used field filters are modelled here. |
| Get Person | `getPerson` | Retrieves a single person (contact) from CentralStationCRM by their ID. |
| Get Person Address | `getPersonAddress` | Retrieves a single address of the given person in CentralStationCRM by its ID. |
| Get Person Assistant | `getPersonAssistant` | Retrieves a single assistant of the given person in CentralStationCRM by its ID. |
| Get Person Avatar | `getPersonAvatar` | Retrieves a single avatar image of the given person in CentralStationCRM by its ID. |
| Get Person Contact Detail | `getPersonContactDetail` | Retrieves a single contact detail of the given person in CentralStationCRM by its ID. |
| Get Person Custom Field | `getPersonCustomField` | Retrieves a single custom field value of the given person in CentralStationCRM by its ID. |
| Get Person Historic Event | `getPersonHistoricEvent` | Retrieves a single historic event of the given person in CentralStationCRM by its ID. |
| Get Person Position | `getPersonPosition` | Retrieves a single position of the given person in CentralStationCRM by its ID. |
| Get Person Protocol Attachment | `getPersonProtocolAttachment` | Retrieves a single attachment of the given protocol under the given person in CentralStationCRM by its ID. |
| Get Person Tag | `getPersonTag` | Retrieves a single tag on the given person in CentralStationCRM by its ID. |
| Get Project | `getProject` | Retrieves a single project from CentralStationCRM by its ID. |
| Get Project Maildrop Address | `getProjectMaildropAddress` | Retrieves the maildrop email address of the given project in CentralStationCRM. Emails forwarded to this address are filed against the project. |
| Get Project Protocol Attachment | `getProjectProtocolAttachment` | Retrieves a single attachment of the given protocol under the given project in CentralStationCRM by its ID. |
| Get Projects Statistics | `getProjectsStatistics` | Returns key statistics about the projects in the CentralStationCRM account, optionally narrowed by tag or by field filters. This endpoint accepts the same filter[field][operator] query parameters as List Projects; the most commonly used field filters are modelled here. |
| Get Protocol | `getProtocol` | Retrieves a single protocol (note, call log or email record) from CentralStationCRM by its ID. |
| Get Protocol Attachment | `getProtocolAttachment` | Retrieves a single attachment of the given protocol in CentralStationCRM by its ID. |
| Get Tag | `getTag` | Retrieves a single tag from CentralStationCRM by its ID, regardless of whether it is attached to a person, company, deal or project. This endpoint is live but not listed in the vendor's OpenAPI document. |
| Get Task | `getTask` | Retrieves a single task from CentralStationCRM by its ID. |
| Get User | `getUser` | Retrieves a single CentralStationCRM user by their ID. |
| Get Webhook | `getWebhook` | Retrieves a single webhook subscription from CentralStationCRM by its ID. |
| List Activities | `listActivities` | Retrieves all activities in CentralStationCRM. An object scope is required - supply one of person_id, company_id, deal_id, project_id, user_id or account_id. |
| List Attachments | `listAttachments` | Retrieves all attachments stored in the CentralStationCRM account. |
| List Avatars | `listAvatars` | Retrieves all avatar images stored in the CentralStationCRM account. |
| List Calendar Event Attendees | `listCalendarEventAttendees` | Retrieves all attendees of the given calendar event in CentralStationCRM. This endpoint is not paginated: it always returns every record. |
| List Calendar Events | `listCalendarEvents` | Retrieves all calendar events in the CentralStationCRM account, with optional date range, state and field filters. |
| List Comments | `listComments` | Retrieves all comments in the CentralStationCRM account. Comments can be attached to attachments, calendar events, protocols, external emails and tasks. |
| List Companies | `listCompanies` | Retrieves all companies in the CentralStationCRM account, with optional tag, activity-stream and field filters. |
| List Company Addresses | `listCompanyAddresses` | Retrieves all addresses stored on the given company in CentralStationCRM. This endpoint is not paginated: it always returns every record. |
| List Company Avatars | `listCompanyAvatars` | Retrieves all avatar images attached to the given company in CentralStationCRM. This endpoint is not paginated: it always returns every record. |
| List Company Contact Details | `listCompanyContactDetails` | Retrieves all contact details of the given company in CentralStationCRM, covering phone numbers, email addresses, homepages, instant messaging handles and SMS numbers. This endpoint is not paginated: it always returns every record. |
| List Company External Emails | `listCompanyExternalEmails` | Retrieves all external emails filed against the given company in CentralStationCRM. |
| List Company Protocol Attachments | `listCompanyProtocolAttachments` | Retrieves all attachments of the given protocol under the given company in CentralStationCRM. |
| List Custom Field Types | `listCustomFieldTypes` | Retrieves all custom field types defined in the CentralStationCRM account. Custom field types are the definitions that custom field values on people, companies, deals and projects refer to. This endpoint is not paginated: it always returns every record. |
| List Deal External Emails | `listDealExternalEmails` | Retrieves all external emails filed against the given deal in CentralStationCRM. |
| List Deal Protocol Attachments | `listDealProtocolAttachments` | Retrieves all attachments of the given protocol under the given deal in CentralStationCRM. |
| List Deal Types | `listDealTypes` | Retrieves all deal types (sales pipelines) configured in the CentralStationCRM account, including their stages. |
| List Deals | `listDeals` | Retrieves all deals in the CentralStationCRM account, optionally narrowed by tag, activity stream date or field filters. |
| List External Email Attachments | `listExternalEmailAttachments` | Retrieves all attachments of the given external email in CentralStationCRM. |
| List External Emails | `listExternalEmails` | Retrieves all external emails filed in the CentralStationCRM account. External emails are messages forwarded to a maildrop address and attached to a record. |
| List Filter Group Record IDs | `listFilterGroupRecordIds` | Retrieves just the IDs of the records matching the given CentralStationCRM filter group, which is faster than fetching the full records. |
| List Filter Groups | `listFilterGroups` | Retrieves all filter groups (saved segments) defined in the CentralStationCRM account, across people, companies, deals and projects. |
| List Group Calendars | `listGroupCalendars` | Retrieves all group calendars in the CentralStationCRM account. Group calendars are the shared calendars that calendar events are placed in. This endpoint is not paginated: it always returns every record. |
| List Historic Events | `listHistoricEvents` | Retrieves historic events (birthdays, anniversaries and similar dates) across all people in CentralStationCRM. CentralStationCRM does not apply filters, sorting, date ranges or paging on this endpoint, so it always returns every historic event; use List Person Historic Events for the events of one person. |
| List People | `listPeople` | Retrieves all people (contacts) in the CentralStationCRM account, with optional tag, activity-stream and field filters. |
| List Person Addresses | `listPersonAddresses` | Retrieves all addresses stored on the given person in CentralStationCRM. This endpoint is not paginated: it always returns every record. |
| List Person Assistants | `listPersonAssistants` | Retrieves all assistants recorded for the given person in CentralStationCRM. This endpoint is not paginated: it always returns every record. |
| List Person Avatars | `listPersonAvatars` | Retrieves all avatar images attached to the given person in CentralStationCRM. This endpoint is not paginated: it always returns every record. |
| List Person Contact Details | `listPersonContactDetails` | Retrieves all contact details of the given person in CentralStationCRM, covering phone numbers, email addresses, homepages, instant messaging handles and SMS numbers. This endpoint is not paginated: it always returns every record. |
| List Person Custom Fields | `listPersonCustomFields` | Retrieves all custom field values stored on the given person in CentralStationCRM. This endpoint is not paginated: it always returns every record. |
| List Person External Emails | `listPersonExternalEmails` | Retrieves all external emails filed against the given person in CentralStationCRM. |
| List Person Historic Events | `listPersonHistoricEvents` | Retrieves all historic events of the given person in CentralStationCRM, such as their birthday, anniversary or first-met date. This endpoint is not paginated: it always returns every record. |
| List Person Positions | `listPersonPositions` | Retrieves all positions of the given person in CentralStationCRM. A position links a person to a company with a job title and department. This endpoint is not paginated: it always returns every record. |
| List Person Protocol Attachments | `listPersonProtocolAttachments` | Retrieves all attachments of the given protocol under the given person in CentralStationCRM. |
| List Person Tags | `listPersonTags` | Retrieves all tags on the given person in CentralStationCRM. |
| List Project External Emails | `listProjectExternalEmails` | Retrieves all external emails filed against the given project in CentralStationCRM. |
| List Project Protocol Attachments | `listProjectProtocolAttachments` | Retrieves all attachments of the given protocol under the given project in CentralStationCRM. |
| List Projects | `listProjects` | Retrieves all projects in the CentralStationCRM account, optionally narrowed by tag, activity stream date or field filters. |
| List Protocol Attachments | `listProtocolAttachments` | Retrieves all attachments of the given protocol in CentralStationCRM. |
| List Protocols | `listProtocols` | Retrieves all protocols (notes, call logs and email records) in the CentralStationCRM account, optionally narrowed to a single person, company, deal or project. |
| List Tag Names | `listTagNames` | Retrieves the distinct tag names used across the CentralStationCRM account as a plain list of strings. |
| List Tags | `listTags` | Retrieves all tags in the CentralStationCRM account, optionally narrowed to the tags on a single person, company, deal or project. |
| List Tasks | `listTasks` | Retrieves all tasks in the CentralStationCRM account, optionally narrowed to open or closed tasks, a date range or a single user. |
| List Users | `listUsers` | Retrieves all users of the CentralStationCRM account. This endpoint is not paginated: it always returns every record. |
| List Webhooks | `listWebhooks` | Retrieves all webhook subscriptions (hooks) registered in the CentralStationCRM account. This endpoint is not paginated: it always returns every record. |
| Merge Companies | `mergeCompanies` | Merges one or more other companies into the given company in CentralStationCRM. The merged companies are removed and their data is moved to the surviving company. This cannot be undone. |
| Merge People | `mergePeople` | Merges one or more other people into the given person in CentralStationCRM. The merged people are removed and their data is moved to the surviving person. This cannot be undone. |
| Search All Records | `searchAllRecords` | Runs a global search across CentralStationCRM and returns the records matching the given search term. A search term is mandatory. |
| Search Attachments | `searchAttachments` | Searches attachments in CentralStationCRM by file name and returns the matching records. |
| Search Companies | `searchCompanies` | Searches companies in CentralStationCRM by name and returns the matching records. |
| Search Company Protocol Attachments | `searchCompanyProtocolAttachments` | Searches the attachments of the given protocol under the given company in CentralStationCRM by file name. |
| Search Contact Details | `searchContactDetails` | Searches the contact details (phone numbers, email addresses, homepages and similar) of people or companies in CentralStationCRM and returns the matching records. |
| Search Deal Protocol Attachments | `searchDealProtocolAttachments` | Searches the attachments of the given protocol under the given deal in CentralStationCRM by file name. |
| Search Deals | `searchDeals` | Searches deals in CentralStationCRM by name and returns the matching records. |
| Search People | `searchPeople` | Searches people in CentralStationCRM by last name, first name, email address or phone number and returns the matching records. Email and phone are mutually exclusive. |
| Search Person Protocol Attachments | `searchPersonProtocolAttachments` | Searches the attachments of the given protocol under the given person in CentralStationCRM by file name. |
| Search Project Protocol Attachments | `searchProjectProtocolAttachments` | Searches the attachments of the given protocol under the given project in CentralStationCRM by file name. |
| Search Projects | `searchProjects` | Searches projects in CentralStationCRM by name and returns the matching records. |
| Search Users | `searchUsers` | Searches CentralStationCRM users by first or last name and returns the matching records. |
| Update Calendar Event | `updateCalendarEvent` | Updates an existing calendar event in CentralStationCRM. Only the fields you supply are changed. |
| Update Calendar Event Attendee | `updateCalendarEventAttendee` | Updates an existing attendee of the given calendar event in CentralStationCRM, for example the attendee's email address or linked person. Only the fields you supply are changed. Note: the API accepts the status field but does not change the stored attendance status. |
| Update Comment | `updateComment` | Updates an existing comment in CentralStationCRM. Only the fields you supply are changed. |
| Update Company | `updateCompany` | Updates an existing company in CentralStationCRM. Only the fields you supply are changed. The API returns an empty body on success. |
| Update Company Address | `updateCompanyAddress` | Updates an existing address of the given company in CentralStationCRM. Only the fields you supply are changed. |
| Update Company Contact Detail | `updateCompanyContactDetail` | Updates an existing contact detail (phone number, email address, homepage, instant messaging handle or SMS number) of the given company in CentralStationCRM. Only the fields you supply are changed. |
| Update Custom Field Type | `updateCustomFieldType` | Updates an existing custom field type in CentralStationCRM. Only the fields you supply are changed. |
| Update Deal | `updateDeal` | Updates an existing deal in CentralStationCRM and returns the updated deal record. Only the fields you supply are changed. |
| Update Group Calendar | `updateGroupCalendar` | Updates an existing group calendar in CentralStationCRM. Only the fields you supply are changed. Read-only calendars created with the account cannot be renamed. |
| Update Person | `updatePerson` | Updates an existing person (contact) in CentralStationCRM. Only the fields you supply are changed. The API returns an empty body on success. |
| Update Person Address | `updatePersonAddress` | Updates an existing address of the given person in CentralStationCRM. Only the fields you supply are changed. |
| Update Person Assistant | `updatePersonAssistant` | Updates an existing assistant of the given person in CentralStationCRM. Only the fields you supply are changed. |
| Update Person Contact Detail | `updatePersonContactDetail` | Updates an existing contact detail (phone number, email address, homepage, instant messaging handle or SMS number) of the given person in CentralStationCRM. Only the fields you supply are changed. |
| Update Person Custom Field | `updatePersonCustomField` | Updates a custom field value on the given person in CentralStationCRM. Only the fields you supply are changed. |
| Update Person Historic Event | `updatePersonHistoricEvent` | Updates an existing historic event of the given person in CentralStationCRM. Only the fields you supply are changed. |
| Update Person Position | `updatePersonPosition` | Updates an existing position of the given person in CentralStationCRM, for example to change the job title or mark it former. Only the fields you supply are changed. |
| Update Person Tag | `updatePersonTag` | Updates an existing tag on the given person in CentralStationCRM, for example to rename it. Only the fields you supply are changed. |
| Update Project | `updateProject` | Updates an existing project in CentralStationCRM. Only the fields you supply are changed. |
| Update Protocol | `updateProtocol` | Updates an existing protocol in CentralStationCRM. Only the fields you supply are changed. |
| Update Task | `updateTask` | Updates an existing task in CentralStationCRM, for example to mark it finished. Only the fields you supply are changed. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Company Created | `company.create` | Fires when a company is created in CentralStationCRM. Registered as model Company, event create; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only, so follow it with Get Company. Set Object Type to 'api' for the full record, 'nested' for related records, or 'hook_with_structure_and_record' for both. |
| Company Deleted | `company.destroy` | Fires when a company is deleted in CentralStationCRM. Registered as model Company, event destroy; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only. The record no longer exists, so capture what you need from the payload. |
| Company Updated | `company.update` | Fires when a company is updated in CentralStationCRM. Registered as model Company, event update; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only, so follow it with Get Company. |
| Deal Created | `deal.create` | Fires when a deal is created in CentralStationCRM. Registered as model Deal, event create; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only, so follow it with Get Deal. Set Object Type to 'api' for the full record. |
| Deal Deleted | `deal.destroy` | Fires when a deal is deleted in CentralStationCRM. Registered as model Deal, event destroy; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only. The record no longer exists, so capture what you need from the payload. |
| Deal Updated | `deal.update` | Fires when a deal is updated in CentralStationCRM, for example when it moves to another stage. Registered as model Deal, event update; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only, so follow it with Get Deal to read the new stage. |
| Note Created | `protocol.create` | Fires when a protocol (note, call log or email record) is created in CentralStationCRM. Registered as model Protocol, event create; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only, so follow it with Get Protocol. |
| Note Deleted | `protocol.destroy` | Fires when a protocol (note, call log or email record) is deleted in CentralStationCRM. Registered as model Protocol, event destroy; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only. The record no longer exists, so capture what you need from the payload. |
| Note Updated | `protocol.update` | Fires when a protocol (note, call log or email record) is updated in CentralStationCRM. Registered as model Protocol, event update; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only, so follow it with Get Protocol. |
| Person Created | `person.create` | Fires when a person (contact) is created in CentralStationCRM. Registered through the CentralStationCRM hooks API as model Person, event create; each hook targets exactly one model and event pair, so routing is per subscription rather than by a discriminator field in the payload. The body below is the 'lean' shape confirmed against a real delivery captured on 2026-09-15: it carries only the identifier, so follow it with the matching Get action to read the record. Set the Object Type input to 'api' to receive the full record instead, to 'nested' to include related records, or to 'hook_with_structure_and_record' for both. |
| Person Deleted | `person.destroy` | Fires when a person (contact) is deleted in CentralStationCRM. Registered as model Person, event destroy; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only. The record no longer exists, so capture what you need from the payload. |
| Person Updated | `person.update` | Fires when a person (contact) is updated in CentralStationCRM. Registered as model Person, event update; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only, so follow it with Get Person. Set Object Type to 'api' for the full record, 'nested' for related records, or 'hook_with_structure_and_record' for both. |
| Project Created | `project.create` | Fires when a project is created in CentralStationCRM. Registered as model Project, event create; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only, so follow it with Get Project. |
| Project Deleted | `project.destroy` | Fires when a project is deleted in CentralStationCRM. Registered as model Project, event destroy; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only. The record no longer exists, so capture what you need from the payload. |
| Project Updated | `project.update` | Fires when a project is updated in CentralStationCRM. Registered as model Project, event update; routing is per subscription. The body is the 'lean' shape confirmed against a real delivery captured on 2026-09-15 - identifier only, so follow it with Get Project. |
