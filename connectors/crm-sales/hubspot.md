---
description: "HubSpot CRM connector — full CRUD, search and batch operations across contacts, companies, deals, tickets, products, line items, quotes, and engagements…"
hidden: true
---

# HubSpot

<img src="../../.gitbook/assets/connectors/lg/hubspot.png" alt="HubSpot logo">

HubSpot CRM connector — full CRUD, search and batch operations across contacts, companies, deals, tickets, products, line items, quotes, and engagements (notes, tasks, calls, emails, meetings), plus owners, pipelines, properties, associations and lists. Webhooks via HubSpot app subscriptions.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [hubspot.com](https://hubspot.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `hubspot` |

## Use it

Add HubSpot from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.hubspot.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add List Members | `addListMembers` | Add records to a MANUAL list. Pass 'recordIds' as an array of record ID strings. |
| Archive Appointment | `archiveAppointment` | Archive (soft-delete) an appointment by record ID. Returns 204 No Content. Requires the crm.objects.appointments.write scope. |
| Archive Call | `archiveCall` | Archive (soft-delete) a call by record ID. Returns 204. |
| Archive Cart | `archiveCart` | Archive (soft-delete) a cart by record ID. Returns 204 No Content. Requires the crm.objects.carts.write scope. |
| Archive Commerce Payment | `archiveCommercePayment` | Archive a commerce payment record by ID (only payments recorded via the API or manually). Returns 204. Requires the crm.objects.commercepayments.write scope. |
| Archive Company | `archiveCompany` | Archive (soft-delete) a company by record ID. Returns 204. |
| Archive Contact | `archiveContact` | Archive (soft-delete) a contact by record ID. Returns 204 No Content on success. |
| Archive Course | `archiveCourse` | Archive (soft-delete) a course by record ID. Returns 204 No Content. Requires the crm.objects.courses.write scope. |
| Archive Deal | `archiveDeal` | Archive (soft-delete) a deal by record ID. Returns 204. |
| Archive Email | `archiveEmail` | Archive (soft-delete) an email engagement by record ID. Returns 204. |
| Archive Form | `archiveForm` | Archive a marketing form by ID. Returns 204. Requires the forms scope. |
| Archive Invoice | `archiveInvoice` | Archive (delete) an invoice by record ID. HubSpot only allows this for draft invoices, and for open invoices when enabled in account settings. Returns 204 No Content. Requires the crm.objects.invoices.write scope. |
| Archive Line Item | `archiveLineItem` | Archive (soft-delete) a line item by record ID. Returns 204. |
| Archive Listing | `archiveListing` | Archive (soft-delete) a listing by record ID. Returns 204 No Content. Requires the crm.objects.listings.write scope. |
| Archive Media Object | `archiveMediaObject` | Media Bridge: archive (delete) a media object by id. Returns 204. Requires media_bridge.write. |
| Archive Meeting | `archiveMeeting` | Archive (soft-delete) a meeting by record ID. Returns 204. |
| Archive Note | `archiveNote` | Archive (soft-delete) a note by record ID. Returns 204. |
| Archive Order | `archiveOrder` | Archive (soft-delete) an order by record ID. Returns 204 No Content. Requires the crm.objects.orders.write scope. |
| Archive Product | `archiveProduct` | Archive (soft-delete) a product by record ID. Returns 204. |
| Archive Project | `archiveProject` | Archive (soft-delete) a project by record ID. Returns 204 No Content. Requires the crm.objects.projects.write scope. |
| Archive Property | `archiveProperty` | Archive (delete) a custom property by name. Returns 204. |
| Archive Quote | `archiveQuote` | Archive (soft-delete) a quote by record ID. Returns 204. |
| Archive Service | `archiveService` | Archive (soft-delete) a service by record ID. Returns 204 No Content. Requires the crm.objects.services.write scope. |
| Archive Subscription | `archiveSubscription` | Archive (soft-delete) a commerce subscription record by ID. Returns 204 No Content. Requires the crm.objects.subscriptions.write scope. |
| Archive Task | `archiveTask` | Archive (soft-delete) a task by record ID. Returns 204. |
| Archive Ticket | `archiveTicket` | Archive (soft-delete) a ticket by record ID. Returns 204. |
| Batch Archive Calls | `batchArchiveCalls` | Archive multiple calls. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Archive Companies | `batchArchiveCompanies` | Archive multiple companies. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Archive Contacts | `batchArchiveContacts` | Archive multiple contacts in one request. Pass 'inputs' as an array of {id} objects. Returns 204 No Content. |
| Batch Archive Deals | `batchArchiveDeals` | Archive multiple deals. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Archive Emails | `batchArchiveEmails` | Archive multiple email engagements. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Archive Line Items | `batchArchiveLineItems` | Archive multiple line items. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Archive Meetings | `batchArchiveMeetings` | Archive multiple meetings. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Archive Notes | `batchArchiveNotes` | Archive multiple notes. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Archive Products | `batchArchiveProducts` | Archive multiple products. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Archive Quotes | `batchArchiveQuotes` | Archive multiple quotes. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Archive Tasks | `batchArchiveTasks` | Archive multiple tasks. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Archive Tickets | `batchArchiveTickets` | Archive multiple tickets. Pass 'inputs' = array of {id}. Returns 204. |
| Batch Create Calls | `batchCreateCalls` | Create multiple calls. Pass 'inputs' = array of {properties:{...}} (each needs hs_timestamp). |
| Batch Create Companies | `batchCreateCompanies` | Create multiple companies. Pass 'inputs' = array of {properties:{...}}. |
| Batch Create Contacts | `batchCreateContacts` | Create multiple contacts in one request. Pass 'inputs' as an array of objects each containing a 'properties' map. |
| Batch Create Deals | `batchCreateDeals` | Create multiple deals. Pass 'inputs' = array of {properties:{...}}. |
| Batch Create Emails | `batchCreateEmails` | Create multiple email engagements. Pass 'inputs' = array of {properties:{...}} (each needs hs_timestamp). |
| Batch Create Line Items | `batchCreateLineItems` | Create multiple line items. Pass 'inputs' = array of {properties:{...}}. |
| Batch Create Meetings | `batchCreateMeetings` | Create multiple meetings. Pass 'inputs' = array of {properties:{...}} (each needs hs_timestamp). |
| Batch Create Notes | `batchCreateNotes` | Create multiple notes. Pass 'inputs' = array of {properties:{...}} (each needs hs_timestamp). |
| Batch Create Products | `batchCreateProducts` | Create multiple products. Pass 'inputs' = array of {properties:{...}}. |
| Batch Create Quotes | `batchCreateQuotes` | Create multiple quotes. Pass 'inputs' = array of {properties:{...}}. |
| Batch Create Tasks | `batchCreateTasks` | Create multiple tasks. Pass 'inputs' = array of {properties:{...}} (each needs hs_timestamp). |
| Batch Create Tickets | `batchCreateTickets` | Create multiple tickets. Pass 'inputs' = array of {properties:{...}}. |
| Batch Read Calls | `batchReadCalls` | Read multiple calls by ID. Pass 'inputs' = array of {id} and 'properties' = array ([] for defaults). |
| Batch Read Companies | `batchReadCompanies` | Read multiple companies by ID. Pass 'inputs' = array of {id} and 'properties' = array of names ([] for defaults). |
| Batch Read Contacts | `batchReadContacts` | Read multiple contacts by ID in one request. Pass 'inputs' as an array of {id} objects, and optionally a 'properties' array and 'idProperty'. |
| Batch Read Deals | `batchReadDeals` | Read multiple deals by ID. Pass 'inputs' = array of {id} and 'properties' = array ([] for defaults). |
| Batch Read Emails | `batchReadEmails` | Read multiple email engagements by ID. Pass 'inputs' = array of {id} and 'properties' = array ([] for defaults). |
| Batch Read Line Items | `batchReadLineItems` | Read multiple line items by ID. Pass 'inputs' = array of {id} and 'properties' = array ([] for defaults). |
| Batch Read Meetings | `batchReadMeetings` | Read multiple meetings by ID. Pass 'inputs' = array of {id} and 'properties' = array ([] for defaults). |
| Batch Read Notes | `batchReadNotes` | Read multiple notes by ID. Pass 'inputs' = array of {id} and 'properties' = array ([] for defaults). |
| Batch Read Products | `batchReadProducts` | Read multiple products by ID. Pass 'inputs' = array of {id} and 'properties' = array ([] for defaults). |
| Batch Read Quotes | `batchReadQuotes` | Read multiple quotes by ID. Pass 'inputs' = array of {id} and 'properties' = array ([] for defaults). |
| Batch Read Tasks | `batchReadTasks` | Read multiple tasks by ID. Pass 'inputs' = array of {id} and 'properties' = array ([] for defaults). |
| Batch Read Tickets | `batchReadTickets` | Read multiple tickets by ID. Pass 'inputs' = array of {id} and 'properties' = array ([] for defaults). |
| Batch Update Calls | `batchUpdateCalls` | Update multiple calls. Pass 'inputs' = array of {id, properties}. |
| Batch Update Companies | `batchUpdateCompanies` | Update multiple companies. Pass 'inputs' = array of {id, properties}. |
| Batch Update Contacts | `batchUpdateContacts` | Update multiple contacts in one request. Pass 'inputs' as an array of {id, properties} objects. |
| Batch Update Deals | `batchUpdateDeals` | Update multiple deals. Pass 'inputs' = array of {id, properties}. |
| Batch Update Emails | `batchUpdateEmails` | Update multiple email engagements. Pass 'inputs' = array of {id, properties}. |
| Batch Update Line Items | `batchUpdateLineItems` | Update multiple line items. Pass 'inputs' = array of {id, properties}. |
| Batch Update Meetings | `batchUpdateMeetings` | Update multiple meetings. Pass 'inputs' = array of {id, properties}. |
| Batch Update Notes | `batchUpdateNotes` | Update multiple notes. Pass 'inputs' = array of {id, properties}. |
| Batch Update Products | `batchUpdateProducts` | Update multiple products. Pass 'inputs' = array of {id, properties}. |
| Batch Update Quotes | `batchUpdateQuotes` | Update multiple quotes. Pass 'inputs' = array of {id, properties}. |
| Batch Update Tasks | `batchUpdateTasks` | Update multiple tasks. Pass 'inputs' = array of {id, properties}. |
| Batch Update Tickets | `batchUpdateTickets` | Update multiple tickets. Pass 'inputs' = array of {id, properties}. |
| Batch Upsert Companies | `batchUpsertCompanies` | Create or update multiple companies keyed by a unique property (e.g. domain). Pass 'inputs' = array of {idProperty, id, properties}. |
| Batch Upsert Contacts | `batchUpsertContacts` | Create or update multiple contacts keyed by a unique property (e.g. email). Pass 'inputs' as an array of {idProperty, id, properties} objects. |
| Batch Upsert Deals | `batchUpsertDeals` | Create or update multiple deals keyed by a unique property. Pass 'inputs' = array of {idProperty, id, properties}. |
| Batch Upsert Line Items | `batchUpsertLineItems` | Create or update multiple line items keyed by a unique property. Pass 'inputs' = array of {idProperty, id, properties}. |
| Batch Upsert Products | `batchUpsertProducts` | Create or update multiple products keyed by a unique property. Pass 'inputs' = array of {idProperty, id, properties}. |
| Batch Upsert Tickets | `batchUpsertTickets` | Create or update multiple tickets keyed by a unique property. Pass 'inputs' = array of {idProperty, id, properties}. |
| Create Appointment | `createAppointment` | Create an appointment. Pass a 'properties' object of HubSpot appointment properties. Requires the crm.objects.appointments.write scope. |
| Create Association | `createAssociation` | Associate two records with specific association type(s). Pass 'types' as an array of {associationCategory, associationTypeId} objects. |
| Create Call | `createCall` | Log a call engagement. Pass a 'properties' object. 'hs_timestamp' (call time) is required. |
| Create Call Transcript | `createCallTranscript` | Attach a third-party transcript to a HubSpot call engagement (calling extensions transcripts API). Pass the call's engagementId and an array of utterances. Returns the transcript id. Requires crm.extensions_calling_transcripts.write. |
| Create Cart | `createCart` | Create a cart. Pass a 'properties' object of HubSpot cart properties. Requires the crm.objects.carts.write scope. |
| Create Commerce Payment | `createCommercePayment` | Record a commerce payment (for payments taken outside HubSpot). HubSpot requires hs_initiated_date. This records data only; it does not charge anyone. Requires the crm.objects.commercepayments.write scope. |
| Create Company | `createCompany` | Create a company. Pass a 'properties' object; 'name' and 'domain' are the most common identifiers. |
| Create Contact | `createContact` | Create a new contact. Pass a 'properties' object of HubSpot contact properties. 'email' is the recommended unique identifier. |
| Create Course | `createCourse` | Create a course. Pass a 'properties' object of HubSpot course properties. Requires the crm.objects.courses.write scope. |
| Create Deal | `createDeal` | Create a deal. Pass a 'properties' object. 'dealname' is required; 'pipeline' and 'dealstage' determine the stage. |
| Create Default Association | `createDefaultAssociation` | Associate two records using the default (HubSpot-defined) association type. No body required. |
| Create Email | `createEmail` | Log an email engagement. Pass a 'properties' object. 'hs_timestamp' is required. |
| Create Form | `createForm` | Create a HubSpot marketing form. Requires the forms scope. |
| Create Goal Target | `createGoalTarget` | Create a goal target (e.g. a revenue quota for a user over a period). Pass a 'properties' object of HubSpot goal properties. Requires the crm.objects.goals.write scope. |
| Create Invoice | `createInvoice` | Create a draft invoice. Pass a 'properties' object of HubSpot invoice properties (hs_currency is required by HubSpot). Associate a contact or company before moving the invoice out of draft. Requires the crm.objects.invoices.write scope. |
| Create Lead | `createLead` | Create a HubSpot Lead (object type 0-136). Pass properties (hs_lead_name, hs_pipeline, hs_pipeline_stage) and optionally associations to a contact (associationTypeId 578 = Primary). |
| Create Line Item | `createLineItem` | Create a line item. Pass a 'properties' object. Provide 'hs_product_id' to base it on a product, or 'name' + 'price' for a custom item. 'quantity' defaults to 1. |
| Create List | `createList` | Create a list. Requires name, objectTypeId (e.g. '0-1' for contacts) and processingType. |
| Create Listing | `createListing` | Create a listing. Pass a 'properties' object of HubSpot listing properties. Requires the crm.objects.listings.write scope. |
| Create Marketing Event | `createMarketingEvent` | Create a marketing event (e.g. a webinar from an external events tool). Requires the crm.objects.marketing_events.write scope. |
| Create Media Object | `createMediaObject` | Media Bridge: create a media object (video, audio, etc.) in HubSpot. objectType is the media type's objectTypeId from Get Media Type Definition. VIDEO/AUDIO need hs_title and hs_oembed_url; IMAGE also needs hs_file_url. Requires media_bridge.write. |
| Create Meeting | `createMeeting` | Create a meeting engagement. Pass a 'properties' object. 'hs_timestamp' is required. |
| Create Note | `createNote` | Create a note engagement. Pass a 'properties' object. 'hs_timestamp' (creation time) and 'hs_note_body' are required. |
| Create Note With Association | `createNoteWithAssociation` | Create a note and associate it to a CRM record (contact=202, deal=214, company=190) in one call. |
| Create Order | `createOrder` | Create an order. Pass a 'properties' object of HubSpot order properties. Requires the crm.objects.orders.write scope. |
| Create Order Pipeline | `createOrderPipeline` | Create an order pipeline with its stages. Requires the crm.pipelines.orders.write scope. |
| Create Pipeline | `createPipeline` | Create a pipeline with stages for an object type (e.g. 'services', 'projects', 'deals', 'tickets'). Requires write access to that object type. |
| Create Pipeline Stage | `createPipelineStage` | Add a stage to an existing pipeline (deals, tickets, services, etc.). For deals pass metadata {probability: '1.0'} for a won stage or {probability: '0.0'} for lost; for tickets pass metadata {ticketState: 'OPEN'\|'CLOSED'}. Returns the new stage with its id. |
| Create Product | `createProduct` | Create a product in the product library. Pass a 'properties' object. 'name' is required. |
| Create Project | `createProject` | Create a project. Pass a 'properties' object of HubSpot project properties; HubSpot requires hs_pipeline_stage, so the account needs a projects pipeline (use List Pipelines with objectType 'projects' to find stage IDs). Requires the crm.objects.projects.write scope. |
| Create Property | `createProperty` | Create a custom property on an object type. Requires name, label, type, fieldType and groupName. |
| Create Property Group | `createPropertyGroup` | Create a property group on an object type. Requires name and label. |
| Create Quote | `createQuote` | Create a sales quote. Pass a 'properties' object. 'hs_title' and 'hs_expiration_date' are required. A full quote usually also needs associations to a deal, line items and a quote template. |
| Create Service | `createService` | Create a service record. Pass a 'properties' object of HubSpot service properties; HubSpot requires hs_pipeline_stage, so the account needs a services pipeline (use List Pipelines with objectType 'services' to find stage IDs). Requires the crm.objects.services.write scope. |
| Create Subscription | `createSubscription` | Create a commerce subscription record. Pass a 'properties' object of HubSpot subscription properties. This records a subscription; it does not charge anyone. Requires the crm.objects.subscriptions.write scope. |
| Create Task | `createTask` | Create a task engagement. Pass a 'properties' object. 'hs_timestamp' (due date) is required. |
| Create Team | `createTeam` | Create a user team and optionally assign users to it. Requires the settings.users.teams.write scope. |
| Create Ticket | `createTicket` | Create a support ticket. Pass a 'properties' object. 'subject' is required; 'hs_pipeline' and 'hs_pipeline_stage' set the status. |
| Create User | `createUser` | Create (invite) a new account user (Settings Users API). Requires settings.users.write scope AND an available user seat — on this portal it returns 400 NO_SEAT_AVAILABLE_FOR_ROLE_COMBINATION (no free seats). Does not assign a paid seat. sendWelcomeEmail true sends the HubSpot invite email. |
| Delete Association | `deleteAssociation` | Remove all associations between two records. Returns 204. |
| Delete Call Transcript | `deleteCallTranscript` | Delete a third-party call transcript by id. Requires crm.extensions_calling_transcripts.write. |
| Delete File | `deleteFile` | Delete a file from HubSpot Files by id. Returns 204. Requires the files scope. |
| Delete List | `deleteList` | Delete a list by ID. Returns 204. |
| Delete Marketing Event | `deleteMarketingEvent` | Delete a marketing event by its HubSpot object ID. Returns 204. Requires the crm.objects.marketing_events.write scope. |
| Delete Order Pipeline | `deleteOrderPipeline` | Delete an order pipeline by ID. Returns 204. Requires the crm.pipelines.orders.write scope. |
| Delete Pipeline | `deletePipeline` | Delete a pipeline of an object type by ID. Returns 204. Requires write access to that object type. |
| Delete Team | `deleteTeam` | Delete a user team by ID. Users stay in the account. Requires the settings.users.teams.write scope. |
| Delete User | `deleteUser` | Remove an account user by ID (Settings Users API). Returns 204 No Content. Irreversible via API; CRM records owned by the user are NOT auto-reassigned. Requires settings.users.write scope. |
| Get Account Details | `getAccountDetails` | Get the connected HubSpot account's details: portal id, account type, time zone, company currency and data hosting location. No extra scope beyond oauth. |
| Get Analytics Report | `getAnalyticsReport` | Get a legacy analytics report broken down by a category (e.g. totals, sources, geolocation) over a time period. Requires the business-intelligence scope. |
| Get Appointment | `getAppointment` | Retrieve a single appointment by its record ID. Requires the crm.objects.appointments.read scope. |
| Get Audit Logs | `getAuditLogs` | Retrieve account audit log entries (who changed what in settings and content). Requires the account-info.security.read scope; audit logs need an Enterprise account. |
| Get Call | `getCall` | Retrieve a single call by record ID. |
| Get Call Transcript | `getCallTranscript` | Read a call transcript by id: engagementId, transcriptSource, utterances. Requires crm.extensions_calling_transcripts.read. |
| Get Cart | `getCart` | Retrieve a single cart by its record ID. Requires the crm.objects.carts.read scope. |
| Get Commerce Payment | `getCommercePayment` | Retrieve a single commerce payment record by ID. Requires the crm.objects.commercepayments.read scope. |
| Get Company | `getCompany` | Retrieve a single company by record ID. |
| Get Company Currency | `getCompanyCurrency` | Get the account's company (default) currency. Requires the settings.currencies.read scope. |
| Get Contact | `getContact` | Retrieve a single contact by its record ID (or by a custom unique property via idProperty). |
| Get Contact Subscriptions | `getContactSubscriptions` | Get an email address's subscription status for every subscription type. Requires the communication_preferences.read scope. |
| Get Course | `getCourse` | Retrieve a single course by its record ID. Requires the crm.objects.courses.read scope. |
| Get CRM User | `getCrmUser` | Retrieve a single CRM user record by record ID. Requires the crm.objects.users.read scope. |
| Get Deal | `getDeal` | Retrieve a single deal by record ID. |
| Get Domain | `getDomain` | Get one connected domain by ID. Requires the cms.domains.read scope. |
| Get Email | `getEmail` | Retrieve a single email engagement by record ID. |
| Get Export Status | `getExportStatus` | Check the status of an export task. When status is COMPLETE the result contains a temporary download URL. Requires the crm.export scope. |
| Get Feedback Submission | `getFeedbackSubmission` | Retrieve a single feedback survey submission by record ID. Requires the crm.objects.feedback_submissions.read scope. |
| Get File | `getFile` | Get a HubSpot Files file's metadata (name, size, type, url, folder) by id. Requires the files scope. |
| Get Form | `getForm` | Get a marketing form definition by ID. Requires the forms scope. |
| Get Form Uploaded File | `getFormUploadedFile` | Get a signed download for a file uploaded through a form submission. Take fileId, sign, conversionId and filename from the file URL stored in the submission. Requires the forms-uploaded-files scope. |
| Get Goal Target | `getGoalTarget` | Retrieve a single goal target by record ID. Requires the crm.objects.goals.read scope. |
| Get Import | `getImport` | Get the state and counts of one CRM import by ID. Requires the crm.import scope. |
| Get Import Errors | `getImportErrors` | List the row-level errors of a CRM import. Requires the crm.import scope. |
| Get Invoice | `getInvoice` | Retrieve a single invoice by its record ID. Requires the crm.objects.invoices.read scope. |
| Get Lead | `getLead` | Retrieve a single lead by its record ID. Requires the crm.objects.leads.read scope. |
| Get Line Item | `getLineItem` | Retrieve a single line item by record ID. |
| Get List | `getList` | Retrieve a list by its ID. |
| Get List Memberships | `getListMemberships` | Retrieve the record IDs that are members of a list. |
| Get Listing | `getListing` | Retrieve a single listing by its record ID. Requires the crm.objects.listings.read scope. |
| Get Login Activity | `getLoginActivity` | Retrieve user login history for the account (account activity API). Requires the account-info.security.read scope. |
| Get Marketing Event | `getMarketingEvent` | Get one marketing event by its HubSpot object ID. Requires the crm.objects.marketing_events.read scope. |
| Get Media Object | `getMediaObject` | Media Bridge: read one media object by id. Pass 'properties' (comma-separated) to choose fields, e.g. hs_title,hs_oembed_url. Requires media_bridge.read. |
| Get Meeting | `getMeeting` | Retrieve a single meeting by record ID. |
| Get Note | `getNote` | Retrieve a single note by record ID. |
| Get Order | `getOrder` | Retrieve a single order by its record ID. Requires the crm.objects.orders.read scope. |
| Get Owner | `getOwner` | Retrieve a single owner by ID. |
| Get Partner Client | `getPartnerClient` | Retrieve a single partner client by record ID. Requires the crm.objects.partner-clients.read scope. |
| Get Partner Service | `getPartnerService` | Retrieve a single partner service by record ID. Requires the crm.objects.partner-services.read scope. |
| Get Pipeline | `getPipeline` | Retrieve a single pipeline by object type and pipeline ID. |
| Get Pipeline Stage | `getPipelineStage` | Retrieve a single pipeline stage by ID. |
| Get Product | `getProduct` | Retrieve a single product by record ID. |
| Get Project | `getProject` | Retrieve a single project by its record ID. Requires the crm.objects.projects.read scope. |
| Get Property | `getProperty` | Retrieve a single property definition by object type and property name. |
| Get Quote | `getQuote` | Retrieve a single quote by record ID. |
| Get Security Activity | `getSecurityActivity` | Retrieve security-related account activity (e.g. password and 2FA changes). Requires the account-info.security.read scope. |
| Get Service | `getService` | Retrieve a single service by its record ID. Requires the crm.objects.services.read scope. |
| Get Subscription | `getSubscription` | Retrieve a single commerce subscription by its record ID. Requires the crm.objects.subscriptions.read scope. |
| Get Task | `getTask` | Retrieve a single task by record ID. |
| Get Thread | `getThread` | Get one conversation thread by ID. Requires the conversations.read scope. |
| Get Ticket | `getTicket` | Retrieve a single ticket by record ID. |
| Get User | `getUser` | Get a single account user by user ID, or by email when idProperty=EMAIL (Settings Users API). Requires settings.users.read scope. |
| Get User Token | `getUserToken` | Introspect the current OAuth access token (POST /oauth/v3/token/introspect). Returns the authenticated user's email, user_id, hub_id, hub_domain, granted scopes and token expiry — the 'who am I' call for the active connection. No input needed; the connection's token and the OAuth app's client id/secret are injected automatically. |
| List Appointments | `listAppointments` | Retrieve a page of appointments. Supports pagination (limit/after), property selection, and including associations. Requires the crm.objects.appointments.read scope. |
| List Association Labels | `listAssociationLabels` | List the available association types/labels between two object types (use to find valid associationTypeId values). |
| List Associations | `listAssociations` | List the records of one object type associated with a given record. |
| List Calls | `listCalls` | Retrieve a page of call engagements. |
| List Carts | `listCarts` | Retrieve a page of carts. Supports pagination (limit/after), property selection, and including associations. Requires the crm.objects.carts.read scope. |
| List Commerce Payments | `listCommercePayments` | Retrieve a page of commerce payment records. Supports pagination, property selection and associations. Requires the crm.objects.commercepayments.read scope. |
| List Companies | `listCompanies` | Retrieve a page of companies with pagination, property selection and associations. |
| List Contacts | `listContacts` | Retrieve a page of contacts. Supports pagination (limit/after), property selection, and including associations. |
| List Courses | `listCourses` | Retrieve a page of courses. Supports pagination (limit/after), property selection, and including associations. Requires the crm.objects.courses.read scope. |
| List CRM Users | `listCrmUsers` | Retrieve a page of CRM user records (the users object, with working hours, timezone and job title), not account seat settings. Requires the crm.objects.users.read scope. |
| List Deals | `listDeals` | Retrieve a page of deals with pagination, property selection and associations. |
| List Domains | `listDomains` | List the domains connected to the HubSpot account. Requires the cms.domains.read scope. |
| List Emails | `listEmails` | Retrieve a page of email engagements (logged emails). |
| List Feedback Submissions | `listFeedbackSubmissions` | Retrieve a page of feedback survey submissions (NPS, CSAT, CES). Read-only. Supports pagination, property selection and associations. Requires the crm.objects.feedback_submissions.read scope. |
| List Forms | `listForms` | List marketing forms. Requires the forms scope. |
| List Goal Targets | `listGoalTargets` | Retrieve a page of goal targets (sales goals and quotas). Supports pagination and property selection. Requires the crm.objects.goals.read scope. |
| List Imports | `listImports` | List recent CRM imports with their state. Requires the crm.import scope. |
| List Inboxes | `listInboxes` | List conversations inboxes (and help desk). Requires the conversations.read scope. |
| List Invoices | `listInvoices` | Retrieve a page of invoices. Supports pagination (limit/after), property selection, and including associations. Requires the crm.objects.invoices.read scope. |
| List Leads | `listLeads` | Retrieve a page of leads. Supports pagination (limit/after), property selection, and including associations. Requires the crm.objects.leads.read scope. |
| List Line Items | `listLineItems` | Retrieve a page of line items (products attached to deals/quotes). |
| List Listings | `listListings` | Retrieve a page of listings (property listings object). Supports pagination (limit/after), property selection, and including associations. Requires the crm.objects.listings.read scope. |
| List Marketing Events | `listMarketingEvents` | List marketing events (webinars, conferences) synced into HubSpot. Requires the crm.objects.marketing_events.read scope. |
| List Media Objects | `listMediaObjects` | Media Bridge: list media objects of one media type. Requires media_bridge.read. |
| List Meetings | `listMeetings` | Retrieve a page of meeting engagements. |
| List Notes | `listNotes` | Retrieve a page of note engagements. |
| List Orders | `listOrders` | Retrieve a page of orders. Supports pagination (limit/after), property selection, and including associations. Requires the crm.objects.orders.read scope. |
| List Owners | `listOwners` | List CRM owners (HubSpot users who can own records). Filter by email, paginate with limit/after. |
| List Partner Clients | `listPartnerClients` | Retrieve a page of partner clients (HubSpot Solutions Partner accounts only). Supports pagination and property selection. Requires the crm.objects.partner-clients.read scope. |
| List Partner Services | `listPartnerServices` | Retrieve a page of partner services (HubSpot Solutions Partner accounts only). Supports pagination and property selection. Requires the crm.objects.partner-services.read scope. |
| List Pipeline Stages | `listPipelineStages` | List all stages for a pipeline. |
| List Pipelines | `listPipelines` | List all pipelines for an object type (e.g. 'deals' or 'tickets'). |
| List Products | `listProducts` | Retrieve a page of products from the product library. |
| List Projects | `listProjects` | Retrieve a page of projects. Supports pagination (limit/after), property selection, and including associations. Requires the crm.objects.projects.read scope. |
| List Properties | `listProperties` | List all property definitions for an object type (e.g. 'contacts', 'companies', 'deals', 'tickets'). |
| List Property Groups | `listPropertyGroups` | List the property groups of an object type (GET /crm/v3/properties/{objectType}/groups). Returns results[] with name, label, displayOrder, archived. Requires the object's crm.schemas.*.read scope (or crm.objects.*.read for objects without schema scopes). Use it to check whether a group exists before creating it. |
| List Quotes | `listQuotes` | Retrieve a page of sales quotes. |
| List Roles | `listRoles` | List the account's user roles (Settings Users API). Use the returned role IDs as roleId in updateUser. Requires settings.users.read scope. |
| List Services | `listServices` | Retrieve a page of services. Supports pagination (limit/after), property selection, and including associations. Requires the crm.objects.services.read scope. |
| List Subscription Types | `listSubscriptionTypes` | List the account's email subscription types (definitions). Requires the communication_preferences.read scope. |
| List Subscriptions | `listSubscriptions` | Retrieve a page of commerce subscriptions. Supports pagination (limit/after), property selection, and including associations. Requires the crm.objects.subscriptions.read scope. |
| List Tasks | `listTasks` | Retrieve a page of task engagements. |
| List Tax Rates | `listTaxRates` | List the tax rates configured in the account's tax rate library. Requires the tax_rates.read scope. |
| List Teams | `listTeams` | List the account's teams (Settings Users API). Use the returned team IDs as primaryTeamId/secondaryTeamIds in updateUser. Requires settings.users.teams.read scope. |
| List Thread Messages | `listThreadMessages` | List the messages in a conversation thread. Requires the conversations.read scope. |
| List Threads | `listThreads` | List conversation threads, optionally filtered by inbox, contact or status. Requires the conversations.read scope. |
| List Tickets | `listTickets` | Retrieve a page of support tickets with pagination, property selection and associations. |
| List Users | `listUsers` | List account users (Settings Users API). Returns active portal users with id, email, role and team info. Paginate with limit/after. Requires settings.users.read scope. Note: owners (getOwner/listOwners) are CRM owner records; this returns actual account users. |
| Record Marketing Event Participation | `recordEventParticipation` | Record that contacts registered for, attended or cancelled a marketing event (by HubSpot event object ID). Pass the state and an array of contact ids. Requires the crm.objects.marketing_events.write scope. |
| Remove List Members | `removeListMembers` | Remove records from a MANUAL list. Pass 'recordIds' as an array of record ID strings. |
| Search Appointments | `searchAppointments` | Search appointments using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. Requires the crm.objects.appointments.read scope. |
| Search Calls | `searchCalls` | Search call engagements in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. |
| Search Carts | `searchCarts` | Search carts using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. Requires the crm.objects.carts.read scope. |
| Search Commerce Payments | `searchCommercePayments` | Search commerce payment records using filter groups, sorting and pagination. Every input is optional. Requires the crm.objects.commercepayments.read scope. |
| Search Companies | `searchCompanies` | Search companies in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. |
| Search Contacts | `searchContacts` | Search contacts in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. |
| Search Courses | `searchCourses` | Search courses using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. Requires the crm.objects.courses.read scope. |
| Search CRM Users | `searchCrmUsers` | Search CRM user records using filter groups, a full-text query, sorting and pagination. Every input is optional. Requires the crm.objects.users.read scope. |
| Search Deals | `searchDeals` | Search deals in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. |
| Search Emails | `searchEmails` | Search logged email engagements in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Requires an email read scope on the connected app. Every input is optional; omitted inputs are not sent. |
| Search Feedback Submissions | `searchFeedbackSubmissions` | Search feedback survey submissions using filter groups, sorting and pagination. Every input is optional. Requires the crm.objects.feedback_submissions.read scope. |
| Search Goal Targets | `searchGoalTargets` | Search goal targets using filter groups, sorting and pagination. Every input is optional. Requires the crm.objects.goals.read scope. |
| Search Invoices | `searchInvoices` | Search invoices using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. Requires the crm.objects.invoices.read scope. |
| Search Leads | `searchLeads` | Search leads using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. Requires the crm.objects.leads.read scope. |
| Search Line Items | `searchLineItems` | Search line items in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. |
| Search Listings | `searchListings` | Search listings using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. Requires the crm.objects.listings.read scope. |
| Search Lists | `searchLists` | Search HubSpot lists by name, with optional processing-type filtering and pagination. Every input is optional; omitted inputs are not sent. |
| Search Meetings | `searchMeetings` | Search meeting engagements in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. |
| Search Notes | `searchNotes` | Search note engagements in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. |
| Search Orders | `searchOrders` | Search orders using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. Requires the crm.objects.orders.read scope. |
| Search Partner Clients | `searchPartnerClients` | Search partner clients using filter groups, a full-text query, sorting and pagination. Every input is optional. Requires the crm.objects.partner-clients.read scope. |
| Search Partner Services | `searchPartnerServices` | Search partner services using filter groups, a full-text query, sorting and pagination. Every input is optional. Requires the crm.objects.partner-services.read scope. |
| Search Products | `searchProducts` | Search products in the HubSpot product library using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. |
| Search Projects | `searchProjects` | Search projects using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. Requires the crm.objects.projects.read scope. |
| Search Quotes | `searchQuotes` | Search quotes in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Requires a quotes read scope on the connected app. Every input is optional; omitted inputs are not sent. |
| Search Services | `searchServices` | Search services using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. Requires the crm.objects.services.read scope. |
| Search Subscriptions | `searchSubscriptions` | Search commerce subscriptions using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. Requires the crm.objects.subscriptions.read scope. |
| Search Tasks | `searchTasks` | Search task engagements in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. |
| Search Tickets | `searchTickets` | Search tickets in the HubSpot CRM using filter groups, a full-text query, sorting and pagination. Every input is optional; omitted inputs are not sent. |
| Send Thread Message | `sendThreadMessage` | Send a reply or internal comment on a conversation thread. A MESSAGE is delivered to the customer; a COMMENT stays internal. Requires the conversations.write scope. |
| Start Export | `startExport` | Start an asynchronous export of CRM records to CSV or XLSX. Returns a task ID; poll Get Export Status for the download URL. Requires the crm.export scope. |
| Subscribe Contact | `subscribeContact` | Subscribe an email address to a subscription type. HubSpot will not resubscribe someone who opted out. Requires the communication_preferences.write scope. |
| Unsubscribe Contact | `unsubscribeContact` | Unsubscribe an email address from a subscription type. This cannot be undone through the API. Requires the communication_preferences.write scope. |
| Update Appointment | `updateAppointment` | Update an appointment by record ID. Partial update: only the properties sent change. Requires the crm.objects.appointments.write scope. |
| Update Call | `updateCall` | Update a call by record ID. Pass a 'properties' object with fields to change. |
| Update Cart | `updateCart` | Update a cart by record ID. Partial update: only the properties sent change. Requires the crm.objects.carts.write scope. |
| Update Commerce Payment | `updateCommercePayment` | Update a commerce payment record by ID. Partial update. Payments processed by HubSpot Payments or Stripe cannot be edited. Requires the crm.objects.commercepayments.write scope. |
| Update Company | `updateCompany` | Update a company by record ID. Pass a 'properties' object with fields to change. |
| Update Company Currency | `updateCompanyCurrency` | Change the account's company (default) currency. This affects how amounts display across the account. Requires the settings.currencies.write scope (not available on every HubSpot plan). |
| Update Contact | `updateContact` | Update an existing contact by record ID. Pass a 'properties' object with the fields to change. |
| Update Course | `updateCourse` | Update a course by record ID. Partial update: only the properties sent change. Requires the crm.objects.courses.write scope. |
| Update CRM User | `updateCrmUser` | Update a CRM user record by record ID, e.g. working hours, timezone, extra phone or job title. Partial update: only the properties sent change. Requires the crm.objects.users.write scope. |
| Update Deal | `updateDeal` | Update a deal by record ID. Pass a 'properties' object with fields to change. |
| Update Email | `updateEmail` | Update an email engagement by record ID. Pass a 'properties' object with fields to change. |
| Update Invoice | `updateInvoice` | Update an invoice by record ID. Partial update: only the properties sent change. Set hs_invoice_status to move it between draft, open, paid and voided. Requires the crm.objects.invoices.write scope. |
| Update Lead | `updateLead` | Update a HubSpot Lead (object type 0-136), e.g. move it to another pipeline stage by setting hs_pipeline_stage. |
| Update Line Item | `updateLineItem` | Update a line item by record ID. Pass a 'properties' object with fields to change. |
| Update Listing | `updateListing` | Update a listing by record ID. Partial update: only the properties sent change. Requires the crm.objects.listings.write scope. |
| Update Marketing Event | `updateMarketingEvent` | Update a marketing event by its HubSpot object ID. Partial update. Requires the crm.objects.marketing_events.write scope. |
| Update Meeting | `updateMeeting` | Update a meeting by record ID. Pass a 'properties' object with fields to change. |
| Update Note | `updateNote` | Update a note by record ID. Pass a 'properties' object with fields to change. |
| Update Order | `updateOrder` | Update an order by record ID. Partial update: only the properties sent change. Requires the crm.objects.orders.write scope. |
| Update Order Pipeline | `updateOrderPipeline` | Rename or reorder an order pipeline. Partial update. Requires the crm.pipelines.orders.write scope. |
| Update Partner Client | `updatePartnerClient` | Update a partner client by record ID. Partial update: only the properties sent change. HubSpot does not allow creating or deleting partner clients. Requires the crm.objects.partner-clients.write scope. |
| Update Partner Service | `updatePartnerService` | Update a partner service by record ID. Partial update: only the properties sent change. HubSpot does not allow creating or deleting partner services. Requires the crm.objects.partner-services.write scope. |
| Update Product | `updateProduct` | Update a product by record ID. Pass a 'properties' object with fields to change. |
| Update Project | `updateProject` | Update a project by record ID. Partial update: only the properties sent change. Requires the crm.objects.projects.write scope. |
| Update Property | `updateProperty` | Update a property definition's label (and optionally other settings) by name. |
| Update Quote | `updateQuote` | Update a quote by record ID. Pass a 'properties' object with fields to change. |
| Update Service | `updateService` | Update a service by record ID. Partial update: only the properties sent change. Requires the crm.objects.services.write scope. |
| Update Subscription | `updateSubscription` | Update a commerce subscription by record ID. Partial update: only the properties sent change. Requires the crm.objects.subscriptions.write scope. |
| Update Task | `updateTask` | Update a task by record ID. Pass a 'properties' object with fields to change. |
| Update Team | `updateTeam` | Rename a user team or change its members. Requires the settings.users.teams.write scope. |
| Update Thread | `updateThread` | Open or close a conversation thread. Requires the conversations.write scope. |
| Update Ticket | `updateTicket` | Update a ticket by record ID. Pass a 'properties' object with fields to change. |
| Update User | `updateUser` | Update an account user by ID (Settings Users API). PUT replaces mutable fields — sends firstName/lastName. Role/team assignment (roleId, primaryTeamId, secondaryTeamIds) is NOT included: this portal tier has no roles access (listRoles → "Account doesn't have access to roles") and empty roleId is rejected (ROLE_ID_NOT_NUMERIC). Requires settings.users.write scope. |
| Upload Text File | `uploadTextFile` | Upload a text file (e.g. a .txt or .csv transcript) to HubSpot Files as multipart/form-data. Pass the file name, its text content, a folder path and access (PRIVATE by default). Returns the file id and URL to use as a note attachment (hs_attachment_ids). Requires the files scope. |
| uploadFile | `uploadFile` |  |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Company Association Changed | `company.associationChange` | An association to/from a company was added or removed. HubSpot delivers events as an array of notification objects. |
| Company Created | `company.creation` | A company was created. HubSpot delivers events as an array of notification objects. |
| Company Deleted | `company.deletion` | A company was deleted. HubSpot delivers events as an array of notification objects. |
| Company Property Changed | `company.propertyChange` | A specified property changed on a company. HubSpot delivers events as an array of notification objects. |
| Contact Association Changed | `contact.associationChange` | An association to/from a contact was added or removed. HubSpot delivers events as an array of notification objects. |
| Contact Created | `contact.creation` | A contact was created. HubSpot delivers events as an array of notification objects. |
| Contact Deleted | `contact.deletion` | A contact was deleted. HubSpot delivers events as an array of notification objects. |
| Contact Merged | `contact.merge` | A contact was merged with another contact. HubSpot delivers events as an array of notification objects. |
| Contact Property Changed | `contact.propertyChange` | A specified property changed on a contact. HubSpot delivers events as an array of notification objects. |
| Contact Restored | `contact.restore` | A previously deleted contact was restored. HubSpot delivers events as an array of notification objects. |
| Conversation Created | `conversation.creation` | A new conversation thread was started. HubSpot delivers events as an array of notification objects. |
| Conversation Deleted | `conversation.deletion` | A conversation thread was deleted. HubSpot delivers events as an array of notification objects. |
| Conversation New Message | `conversation.newMessage` | A new message was received on a conversation thread. HubSpot delivers events as an array of notification objects. |
| Conversation Property Changed | `conversation.propertyChange` | A property changed on a conversation thread. HubSpot delivers events as an array of notification objects. |
| Deal Association Changed | `deal.associationChange` | An association to/from a deal was added or removed. HubSpot delivers events as an array of notification objects. |
| Deal Created | `deal.creation` | A deal was created. HubSpot delivers events as an array of notification objects. |
| Deal Deleted | `deal.deletion` | A deal was deleted. HubSpot delivers events as an array of notification objects. |
| Deal Property Changed | `deal.propertyChange` | A specified property changed on a deal. HubSpot delivers events as an array of notification objects. |
| Line Item Created | `line_item.creation` | A line item was created. HubSpot delivers events as an array of notification objects. |
| Line Item Deleted | `line_item.deletion` | A line item was deleted. HubSpot delivers events as an array of notification objects. |
| Line Item Property Changed | `line_item.propertyChange` | A specified property changed on a line item. HubSpot delivers events as an array of notification objects. |
| Product Created | `product.creation` | A product was created. HubSpot delivers events as an array of notification objects. |
| Product Deleted | `product.deletion` | A product was deleted. HubSpot delivers events as an array of notification objects. |
| Product Property Changed | `product.propertyChange` | A specified property changed on a product. HubSpot delivers events as an array of notification objects. |
| Ticket Association Changed | `ticket.associationChange` | An association to/from a ticket was added or removed. HubSpot delivers events as an array of notification objects. |
| Ticket Created | `ticket.creation` | A ticket was created. HubSpot delivers events as an array of notification objects. |
| Ticket Deleted | `ticket.deletion` | A ticket was deleted. HubSpot delivers events as an array of notification objects. |
| Ticket Property Changed | `ticket.propertyChange` | A specified property changed on a ticket. HubSpot delivers events as an array of notification objects. |
