---
description: "Agile CRM - all-in-one CRM with sales, marketing and service automation."
hidden: true
---

# Agile CRM

Agile CRM - all-in-one CRM with sales, marketing and service automation. Full REST API coverage: contacts, companies, deals (opportunities), tasks, events, notes, tracks/milestones (pipelines), campaigns/workflows, documents and helpdesk tickets. HTTP Basic auth (account email + REST API key); per-account subdomain.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [agilecrm.com](https://agilecrm.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 77 |
| **Events** | 0 |
| **Slug** | `agilecrm` |

## Use it

Add Agile CRM from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.agilecrm.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact Tags | `addContactTags` | Add/update tags on a contact by ID. |
| Add Note By Email | `addNoteByEmail` | Add a note to a contact identified by email. note is a JSON string, e.g. {"subject":"x","description":"y"}. |
| Add Score By Email | `addScoreByEmail` | Change (increment/decrement) a contact's lead score by email. Use negative score to decrease. |
| Add Tags By Email | `addTagsByEmail` | Add tags to a contact identified by email. tags is a JSON array string, e.g. ["Lead"]. |
| Add Ticket Note | `addTicketNote` | Add a note/reply to a helpdesk ticket by ticket ID. note_type PUBLIC or PRIVATE. |
| Bulk Delete Deals | `bulkDeleteDeals` | Delete multiple deals in one call by their deal IDs. Warning: verified on 2026-09-12 that Agile CRM answers this endpoint with HTTP 204 but does not actually delete the deals - the same result was reproduced with a direct request outside fastn using every documented body shape. Use Delete Deal, which removes the record reliably, until Agile CRM fixes this endpoint. |
| Bulk Delete Notes | `bulkDeleteNotes` | Delete one or more DEAL notes in a single call by their note IDs. Despite the /contacts/notes/bulk path, Agile CRM documents this endpoint as "Delete notes from specific deal" (REST API reference section 4.8) and it only works for deal notes: verified live on 2026-09-15 that a deal note ID returns HTTP 204 and the note is gone from Get Deal Notes, while a contact note ID returns HTTP 500 "java.lang.IndexOutOfBoundsException" and an unquoted numeric array returns HTTP 500 "java.lang.NullPointerException". Pass ids as a JSON array string of quoted deal-note IDs, e.g. ["5720031100600320"]. To remove a note from a contact, use Delete Contact Note instead, which returns a clean 204. |
| Change Contact Owner | `changeContactOwner` | Reassign a contact to a different domain user by owner email. |
| Create Company | `createCompany` | Create a company. Set type to COMPANY. Provide properties (name is the company name via SYSTEM property 'name'). |
| Create Contact | `createContact` | Create a new contact. Provide contact properties (first_name is mandatory), plus optional tags, lead_score and star_value. |
| Create Deal | `createDeal` | Create a deal (opportunity). name, expected_value and milestone are mandatory. Optionally set pipeline_id, probability, close_date (epoch), owner_id, contact_ids and custom_data. |
| Create Deal For Contact By Email | `createDealForContactByEmail` | Create a deal and relate it to the contact with the given email (path). |
| Create Deal Note | `createDealNote` | Create a note and relate it to one or more deals. |
| Create Document | `createDocument` | Create a document (link) and relate it to contacts/deals. url is mandatory. |
| Create Event | `createEvent` | Create a calendar event. title, start and end (epoch seconds) are mandatory. color: red (high), #36C (normal), green (low). |
| Create Note | `createNote` | Create a note and relate it to contacts. |
| Create Task | `createTask` | Create a task. subject, type and priority_type are mandatory. type: CALL/EMAIL/FOLLOW_UP/MEETING/MILESTONE/SEND/TWEET/OTHER; priority_type: HIGH/NORMAL/LOW; status: YET_TO_START/IN_PROGRESS/COMPLETED. |
| Create Task For Contact By Email | `createTaskForContactByEmail` | Create a task and relate it to the contact with the given email (path). |
| Create Ticket | `createTicket` | Create a helpdesk ticket. requester_name, requester_email, subject, priority, status and groupID mandatory. |
| Create Track | `createTrack` | Create a track (pipeline). name must not be 'Default'. milestones is a comma-separated string; each milestone's first letter uppercase. Plan gate: multiple tracks are a paid-plan feature - on an account without it Agile CRM answers HTTP 403 with the plain-text body "Sorry, Your current plan does not have this option." (verified live 2026-09-15). The request is well-formed; upgrade the Agile CRM plan to use this action. |
| Delete Company | `deleteCompany` | Delete a company by ID (same endpoint as contacts). |
| Delete Contact | `deleteContact` | Delete a single contact by ID. |
| Delete Contact Note | `deleteContactNote` | Remove a specific note from a specific contact (breaks the note-contact relationship). |
| Delete Contact Tags | `deleteContactTags` | Delete one or more tags from a contact by ID. |
| Delete Deal | `deleteDeal` | Delete a deal by ID. |
| Delete Document | `deleteDocument` | Permanently delete a document from Agile CRM by its document ID. Returns an empty 204 response on success. |
| Delete Event | `deleteEvent` | Delete an event by ID. |
| Delete Tags By Email | `deleteTagsByEmail` | Remove tags from a contact identified by email. tags is a JSON array string. |
| Delete Task | `deleteTask` | Delete a task by ID. |
| Delete Ticket | `deleteTicket` | Delete a helpdesk ticket by ID. |
| Delete Track | `deleteTrack` | Delete a track by ID. |
| Enroll Contact In Campaign | `enrollContactInCampaign` | Add a contact (by email) to a campaign/workflow. |
| Get Company By ID | `getCompany` | Retrieve a company object by ID (same endpoint as contacts). |
| Get Contact By Email | `getContactByEmail` | Retrieve a contact by email address (path). |
| Get Contact By ID | `getContact` | Retrieve a single contact object by its ID. |
| Get Contact By Phone | `getContactByPhone` | Retrieve a contact by phone number (path). |
| Get Contact Deals | `getContactDeals` | Get deals related to a specific contact by contact ID. |
| Get Contact Documents | `getContactDocuments` | Get documents related to a specific contact. |
| Get Contact Events | `getContactEvents` | Get events related to a contact, sorted by date. |
| Get Contact Notes | `getContactNotes` | Get notes related to a specific contact. |
| Get Contact Tasks | `getContactTasks` | Get tasks related to a contact, sorted latest first. |
| Get Contacts By Dynamic Filter | `getContactsByDynamicFilter` | Search contacts/companies/deals by a dynamic filter. filterJson is a JSON string with rules/or_rules and contact_type (PERSON/COMPANY/OPPORTUNITY). |
| Get Deal By ID | `getDeal` | Get a deal (opportunity) by its ID. |
| Get Deal Notes | `getDealNotes` | Get notes related to a specific deal by deal ID. |
| Get Deals By Milestone | `getDealsByMilestone` | Get deals from the default track grouped by milestone. |
| Get Deals By Pipeline | `getDealsByPipeline` | Get deals for a particular track (pipeline) grouped by milestone. Pass pipeline_id (0 = default track). |
| Get Deals By Track | `getDealsByTrack` | Get deals from a particular track (flat list). pipeline_id: 0 = default track, 1 = all tracks. Supports page_size and cursor. |
| Get My Deals | `getMyDeals` | Get deals owned by the current authenticated user. |
| Get Pending Tasks | `getPendingTasks` | Get pending tasks for all users that are within the given number of days from the due date. |
| Get Task By ID | `getTask` | Get a task by its ID. |
| Get Tasks By Filter | `getTasksByFilter` | Get tasks by filters. criteria=CATEGORY (type EMAIL/CALL/FOLLOW_UP/MEETING/MILESTONE/SEND/TWEET/OTHER), STATUS (IN_PROGRESS/YET_TO_START/COMPLETED) or PRIORITY (HIGH/NORMAL/LOW). |
| Get Ticket Messages | `getTicketMessages` | Get all messages/notes within a ticket by ticket ID. |
| List Campaigns | `listCampaigns` | List campaigns (workflows) available in the domain. |
| List Companies | `listCompanies` | Fetch a paginated list of companies. Params sent as form fields. |
| List Contacts | `listContacts` | List all contacts in the domain, ordered by creation time. Supports paging via page_size and cursor query params. |
| List Deals | `listDeals` | List all deals (opportunities), ordered by created time. Supports page_size and cursor. |
| List Events | `listEvents` | List events within a time window. start and end are epoch seconds query params. |
| List Tasks | `listTasks` | List all tasks in the domain, ordered by created time. |
| List Ticket Filters | `listTicketFilters` | Get all helpdesk ticket filter IDs. |
| List Ticket Groups | `listTicketGroups` | List all helpdesk support groups in the Agile CRM account. Use the returned group id as the groupID input when creating a ticket. |
| List Tickets | `listTickets` | List helpdesk tickets for a given filter. filter_id from List Ticket Filters. page_size and global_sort_key optional. |
| List Tracks | `listTracks` | Get all tracks (pipelines). Each track has a comma-separated milestones string. |
| Remove Contact From Campaign | `removeContactFromCampaign` | Unsubscribe/remove a contact from a campaign by workflow ID and contact ID. |
| Remove Contacts From Deal | `removeContactsFromDeal` | Remove related contacts from a deal by deal ID and contact_ids. |
| Search Contacts And Companies | `searchContactsCompanies` | Search contacts or companies by keyword. All params mandatory: q (keyword), page_size, type (PERSON or COMPANY). |
| Search Contacts By Email | `searchContactsByEmail` | Search one or more contacts by email. email_ids is a JSON array string, e.g. ["a@b.com"]. |
| Update Company | `updateCompany` | Partial update of a company's property fields by company ID. |
| Update Contact Properties | `updateContactProperties` | Partial update of a contact's property fields by ID. Adds new or overrides existing properties. Does not update lead score, star value or tags (use dedicated actions). |
| Update Deal | `updateDeal` | Partial update of a deal by ID. Only provided fields are changed. |
| Update Deal Note | `updateDealNote` | Update an existing deal note by note ID. |
| Update Document | `updateDocument` | Update a document by ID. url is mandatory. |
| Update Event | `updateEvent` | Update an event. id must be provided, otherwise a new event is created. |
| Update Lead Score | `updateLeadScore` | Update the lead score of a contact by ID. |
| Update Property By Email | `updatePropertyByEmail` | Add/update a single property field of a contact identified by email (query param). Body is one property object. |
| Update Star Value | `updateStarValue` | Update the star rating (0-5) of a contact by ID. |
| Update Task | `updateTask` | Partial update of a task by ID. Only provided fields change. |
| Update Track | `updateTrack` | Update a track by ID. name must not be 'Default'. |
