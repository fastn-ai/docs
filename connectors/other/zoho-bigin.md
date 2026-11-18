---
description: "Zoho Bigin is a pipeline-centric CRM for small businesses."
---

# Zoho Bigin

Zoho Bigin is a pipeline-centric CRM for small businesses. This connector provides full access to Bigin's REST API v2: contacts, companies (Accounts module), pipelines and deals, products, tasks, events, calls, notes, tags, users, roles, profiles, and module/field metadata.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [bigin.com](https://bigin.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 79 |
| **Events** | 0 |
| **Slug** | `zohoBigin` |

## Use it

Add Zoho Bigin from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoBigin.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Tags To Record | `addTagsToRecord` | Attaches one or more existing tags to a specific record in Bigin. |
| Change Record Owner | `changeRecordOwner` | Transfers ownership of a record in Bigin to a different user. The correct endpoint and body shape (owner.id, notify) were confirmed from the live Bigin API docs, correcting an earlier incorrect transfer_ownership/owner-string guess. |
| Create Bulk Read Job | `createBulkReadJob` | Starts an asynchronous bulk export job that reads a large number of records from a Bigin module. Only query.module is required; poll the returned job id with Get Bulk Read Job Status. |
| Create Bulk Write Job | `createBulkWriteJob` | Starts an asynchronous bulk write job to insert or update a large number of records in a Bigin module from a previously uploaded CSV file. Wiring confirmed correct: a real request against Bigin returns the business-logic error FILE_NOT_FOUND for a nonexistent file_id (not a parse/schema error), proving the request shape is accepted. |
| Create Call | `createCall` | Creates one or more call log records in Bigin, up to 100 per call. Call Type, Call Start Time, and Call Duration are required for every call. |
| Create Company | `createCompany` | Creates one or more company records (the Accounts module, Bigin's organizations/businesses) in Bigin, up to 100 per call. Company Name is required for every record. |
| Create Contact | `createContact` | Creates one or more contact records in Bigin (up to 100 per call). Last Name is required for every contact. |
| Create Event | `createEvent` | Creates one or more event (meeting) records in Bigin, up to 100 per call. Event Title, Start DateTime, and End DateTime are required for every event. |
| Create Note | `createNote` | Adds a note to a Contact, Company, or Pipeline record in Bigin. |
| Create Pipeline Record | `createPipelineRecord` | Creates one or more pipeline records (deals) in Bigin, up to 100 per call. Deal Name, Stage, and Sub Pipeline are required for every record. |
| Create Product | `createProduct` | Creates one or more product records in Bigin, up to 100 per call. Product Name is required for every record. |
| Create Tags | `createTags` | Creates one or more new tags for a specific Bigin module. The module is passed as a URL query parameter, not the body. |
| Create Task | `createTask` | Creates one or more task records in Bigin, up to 100 per call. Subject is required for every task. Note: linking a task to a Contact/Company/Pipeline via Related_To at creation requires an internal $se_module discriminator whose accepted values could not be confirmed live; use Get Related Records / the module's own related-list APIs to associate a task with a parent record instead. |
| Delete Attachment | `deleteAttachment` | Deletes a file attachment from a record in Bigin. |
| Delete Call | `deleteCall` | Deletes a single call log record from Bigin by its record id. |
| Delete Company | `deleteCompany` | Deletes a single company record (Accounts module) from Bigin by its record id. |
| Delete Contact | `deleteContact` | Deletes a single contact record from Bigin by its record id. |
| Delete Event | `deleteEvent` | Deletes a single event record from Bigin by its record id. |
| Delete Note | `deleteNote` | Deletes a single note record from Bigin by its record id. |
| Delete Pipeline Record | `deletePipelineRecord` | Deletes a single pipeline record (deal) from Bigin by its record id. |
| Delete Product | `deleteProduct` | Deletes a single product record from Bigin by its record id. |
| Delete Task | `deleteTask` | Deletes a single task record from Bigin by its record id. |
| Disable Notifications | `disableNotifications` | Disables and removes one or more notification channels, deleting all notifications enabled for those channels. |
| Disable Specific Notification Events | `disableSpecificNotificationEvents` | Removes only the specified events from an existing notification channel, leaving the rest of the channel's subscription intact. |
| Enable Notifications | `enableNotifications` | Enables real-time webhook notifications for Bigin record events by registering one or more channels, each with its own notify URL and list of module.operation events to watch. |
| Get Bulk Read Job Status | `getBulkReadJobStatus` | Retrieves the status and result-download link of a bulk read job in Bigin. |
| Get Bulk Write Job Status | `getBulkWriteJobStatus` | Retrieves the status and result details of a bulk write job in Bigin. Wiring confirmed correct: a realistically-formatted but nonexistent job id returns the business-logic error RESOURCE_NOT_FOUND (not a parse/schema error). A real 2xx requires a genuine job id from Create Bulk Write Job, which itself is blocked on the binary-upload limitation of Upload Bulk Write File - see that action's notes. |
| Get Call | `getCall` | Retrieves a single call log record from Bigin by its record id. |
| Get Company | `getCompany` | Retrieves a single company record (Accounts module) from Bigin by its record id. |
| Get Contact | `getContact` | Retrieves a single contact record from Bigin by its record id. |
| Get Event | `getEvent` | Retrieves a single event record from Bigin by its record id. |
| Get Note | `getNote` | Retrieves a single note record from Bigin by its record id. |
| Get Notification Details | `getNotificationDetails` | Retrieves the list of enabled notification channels, or details for one channel or module when filtered. |
| Get Organization | `getOrganization` | Retrieve the connected Bigin organization's details, including the zgid needed as the organization id for bulk write file uploads. |
| Get Pipeline Record | `getPipelineRecord` | Retrieves a single pipeline record (deal) from Bigin by its record id. |
| Get Product | `getProduct` | Retrieves a single product record from Bigin by its record id. |
| Get Related Records | `getRelatedRecords` | Lists the records in a related list (e.g. Tasks, Events, Calls, Attachments, or Associated Products) attached to a specific parent record in Bigin. |
| Get Task | `getTask` | Retrieves a single task record from Bigin by its record id. |
| List Attachments | `listAttachments` | Lists the file attachments on a specific record in Bigin. The API requires the fields parameter for this endpoint. |
| List Calls | `listCalls` | Lists call log records from Bigin with optional field selection, sorting, and pagination. |
| List Companies | `listCompanies` | Lists company records (Accounts module) from Bigin with optional field selection, sorting, and pagination. |
| List Contacts | `listContacts` | Lists contact records from Bigin with optional field selection, sorting, and pagination. |
| List Custom Views | `listCustomViews` | Retrieves the custom views (saved filters) defined for a specific Bigin module. |
| List Events | `listEvents` | Lists event records from Bigin with optional field selection, sorting, and pagination. |
| List Layouts | `listLayouts` | Retrieves the layout metadata (sections, fields, and their order) configured for a specific Bigin module. |
| List Module Fields | `listModuleFields` | Retrieves the metadata of all fields defined on a specific Bigin module, including field API names, data types, and picklist values. |
| List Modules | `listModules` | Retrieves the list of modules available in the connected Bigin organization, including each module's API name, labels, and supported capabilities. |
| List Notes | `listNotes` | Lists note records in Bigin. Fetching Notes requires an administrator-level connection. |
| List Notes For Record | `listNotesForRecord` | Lists the notes attached to a specific Contact, Company, or Pipeline record in Bigin. The API requires the fields parameter for this endpoint. |
| List Pipeline Records | `listPipelineRecords` | Lists pipeline records (deals) from Bigin with optional field selection, sorting, and pagination. |
| List Products | `listProducts` | Lists product records from Bigin with optional field selection, sorting, and pagination. |
| List Profiles | `listProfiles` | Lists the profiles defined in the connected Bigin organization. |
| List Related Lists | `listRelatedLists` | Retrieves the related lists (child relationships) configured for a specific Bigin module, such as which modules can be linked to it. |
| List Roles | `listRoles` | Lists the roles defined in the connected Bigin organization. |
| List Tags | `listTags` | Lists the tags defined for a specific Bigin module. |
| List Tasks | `listTasks` | Lists task records from Bigin with optional field selection, sorting, and pagination. |
| List Users | `listUsers` | Retrieves the list of users who have access to the connected Bigin organization, including their role, profile, and contact details. Supports filtering by user status. |
| Remove Tags From Record | `removeTagsFromRecord` | Detaches one or more tags from a specific record in Bigin. |
| Run COQL Query | `runCoqlQuery` | Runs a Bigin Query Language (COQL) SELECT statement to fetch records with SQL-like syntax, including joins across related modules. |
| Search Calls | `searchCalls` | Searches call log records in Bigin by a field criteria expression, a phone number, or a free-text word. Provide exactly one of criteria, phone, or word. |
| Search Companies | `searchCompanies` | Searches company (Accounts module) records in Bigin by a field criteria expression, a phone number, or a free-text word. Provide exactly one of criteria, phone, or word. |
| Search Contacts | `searchContacts` | Searches contact records in Bigin by a field criteria expression, an email address, a phone number, or a free-text word. Provide exactly one of criteria, email, phone, or word. |
| Search Events | `searchEvents` | Searches event records in Bigin by a field criteria expression or a free-text word. Provide exactly one of criteria or word. |
| Search Pipeline Records | `searchPipelineRecords` | Searches pipeline (deal) records in Bigin by a field criteria expression or a free-text word. Provide exactly one of criteria or word. |
| Search Products | `searchProducts` | Searches product records in Bigin by a field criteria expression or a free-text word. Provide exactly one of criteria or word. |
| Search Tasks | `searchTasks` | Searches task records in Bigin by a field criteria expression or a free-text word. Provide exactly one of criteria or word. |
| Update Call | `updateCall` | Updates an existing call log record in Bigin by its record id. Only the fields supplied are changed. |
| Update Company | `updateCompany` | Updates an existing company record (Accounts module) in Bigin by its record id. Only the fields supplied are changed. |
| Update Contact | `updateContact` | Updates an existing contact record in Bigin by its record id. Only the fields supplied are changed. |
| Update Event | `updateEvent` | Updates an existing event record in Bigin by its record id. Only the fields supplied are changed. |
| Update Note | `updateNote` | Updates an existing note record in Bigin by its record id. Only the fields supplied are changed. |
| Update Notification Details | `updateNotificationDetails` | Overwrites the full details of one or more existing notification channels (events, notify URL, token, expiry). Values you omit are cleared, not preserved - use Update Specific Notification Details to append instead. |
| Update Pipeline Record | `updatePipelineRecord` | Updates an existing pipeline record (deal) in Bigin by its record id, such as moving it to a new stage. Only the fields supplied are changed. |
| Update Product | `updateProduct` | Updates an existing product record in Bigin by its record id. Only the fields supplied are changed. |
| Update Specific Notification Details | `updateSpecificNotificationDetails` | Appends events or updates individual fields on an existing notification channel while retaining its other existing details. |
| Update Task | `updateTask` | Updates an existing task record in Bigin by its record id. Only the fields supplied are changed. |
| Upload Attachment | `uploadAttachment` | Attaches a plain-text file to a record in Bigin. Only text content is supported - the underlying HTTP engine can corrupt binary file bytes, so this action cannot be used for images, PDFs, or other binary formats. |
| Upload Bulk Write File | `uploadBulkWriteFile` | Uploads a zipped CSV file of records for a subsequent bulk write job, returning a file id. Requires the org's X-CRM-ORG id. The uploaded file must be a real zip archive; the connector engine's binary-upload path is unverified for zip content. |
| Upsert Contacts | `upsertContacts` | Inserts or updates contact records in Bigin in a single call, matching existing records by the given duplicate-check fields (defaults to Email). |
