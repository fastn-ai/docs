---
description: "ServiceM8 is a job management platform for trade and service businesses."
hidden: true
---

# ServiceM8

<img src="../../.gitbook/assets/connectors/servicem8.png" alt="ServiceM8 logo" width="64">

ServiceM8 is a job management platform for trade and service businesses. This connector covers the ServiceM8 REST API (api_1.0): jobs, clients, contacts, activities, allocations, materials, payments, checklists, queues, staff, assets, forms, templates, attachments, notes, tasks, messaging and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [servicem8.com](https://servicem8.com) |
| **Authentication** | API key, Basic auth |
| **Slug** | `servicem8` |

## Use it

Add ServiceM8 from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.servicem8.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Note To Inbox Message | `addNoteToInboxMessage` | Adds an internal note to a ServiceM8 inbox message. Requires Inbox to be available on the account. |
| Archive Inbox Message | `archiveInboxMessage` | Archives or unarchives a ServiceM8 inbox message. Set Archived to false to restore a message to the inbox. Requires Inbox to be available on the account. |
| Archive Staff Message | `updateStaffMessage` | Sets the Active flag on a ServiceM8 staff message. ServiceM8 treats staff messages as immutable once sent: message text, attached JSON, sent, delivered and read timestamps and both staff UUIDs are all rejected after creation with "Cannot change &lt;field&gt; after creation", so Active is the only field this endpoint will accept. |
| Attach Inbox Message To Job | `attachInboxMessageToJob` | Attaches a ServiceM8 inbox message to an existing job so the correspondence is filed against that job. Requires Inbox to be available on the account. |
| Convert Inbox Message To Job | `convertInboxMessageToJob` | Converts a ServiceM8 inbox message into a new job, optionally using a job template. Requires Inbox to be available on the account. |
| Create Allocation Window | `createAllocationWindow` | Creates a ServiceM8 allocation window. Start and end times are expressed in minutes from midnight, so 8am is 480 and 12pm is 720. |
| Create Asset Type | `createAssetType` | Creates an asset type in ServiceM8, which groups assets and defines the custom fields they carry. Requires the Asset Management add-on. |
| Create Asset Type Field | `createAssetTypeField` | Adds a custom field to a ServiceM8 asset type. Field Name is mandatory. Requires the Asset Management add-on. |
| Create Attachment | `createAttachment` | Creates an attachment record against a ServiceM8 job or client. This creates the metadata record only; ServiceM8 takes the file bytes through a separate binary upload endpoint that fastn cannot call today. |
| Create Availability | `createAvailability` | Creates a ServiceM8 availability record marking a block of time as available or unavailable. Requires the Availability add-on. |

<details>

<summary>See 207 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Badge | `createBadge` | Creates a badge in ServiceM8 that can then be applied to jobs and clients. Badge Name is mandatory. |
| Create Client | `createClient` | Creates a new client (company) in ServiceM8. Only Client Name is mandatory. ServiceM8 returns {"errorCode":0,"message":"OK"} and puts the new UUID in the x-record-uuid response header, which fastn cannot surface; find the new record with List Clients and a $filter on the name. |
| Create Client Contact | `createClientContact` | Creates a contact against a ServiceM8 client. Returns {"errorCode":0,"message":"OK"}; the new UUID is only in the x-record-uuid response header, so locate the record with List Client Contacts filtered on the client UUID. |
| Create Document Template | `createDocumentTemplate` | Creates a document template in ServiceM8. Document Name must be unique; ServiceM8 rejects a duplicate with "Document Name must be unique". Template Type is assigned by ServiceM8 and cannot be set through the API. |
| Create Email Template | `createEmailTemplate` | Creates an email template in ServiceM8. Template Name is mandatory and must be unique; ServiceM8 rejects a duplicate with "Template Name must be unique". |
| Create Event Webhook Subscription | `createEventWebhookSubscription` | Subscribes a callback URL to a named ServiceM8 event such as job.created or job.completed. ServiceM8 expects a form-encoded body and answers {"success":true} without returning the new subscription UUID - use List Webhook Subscriptions to find it before deleting. Your callback URL must return 2xx within 10 seconds or ServiceM8 eventually deactivates the subscription. ServiceM8 serves the webhook API only to API-key and OAuth credentials. |
| Create Feedback | `createFeedback` | Records customer feedback against a ServiceM8 job or the business itself. Rating is a 1-5 value where higher is better. Requires the Feedback add-on. |
| Create Form | `createForm` | Creates a form in ServiceM8. Requires the Forms add-on to be activated on the account. |
| Create Form Field | `createFormField` | Adds a question to a ServiceM8 form. The field's type, mandatory flag and choice list are carried in the Field Configuration JSON. Requires the Forms add-on. |
| Create Form Response | `createFormResponse` | Records a completed ServiceM8 form against a job or asset. The answers are supplied as a JSON array in Answers JSON. Requires the Forms add-on. |
| Create Inbox Message | `createInboxMessage` | Places a message into the ServiceM8 inbox, for example a lead captured on your website. Subject and Message Text are mandatory. Requires Inbox to be available on the account. |
| Create Job | `createJob` | Creates a new job in ServiceM8. Only Status is mandatory. ServiceM8 returns {"errorCode":"0","message":"OK"} and supplies the new record UUID in the x-record-uuid response header, which fastn cannot surface; retrieve the new job with List Jobs using a $filter on a field you set, such as purchase_order_number. |
| Create Job Activity | `createJobActivity` | Books a job activity in ServiceM8 - either a scheduled slot on the dispatch board or a recorded time entry. Was Scheduled and Was Recorded are mutually exclusive; setting both to 1 is rejected with "activity_was_recorded and activity_was_scheduled cannot both be true". |
| Create Job Allocation | `createJobAllocation` | Allocates a ServiceM8 job to a staff member within an allocation window. Allocation Window UUID is mandatory; ServiceM8 rejects the request with "allocation_window_uuid is mandatory" otherwise. |
| Create Job Category | `createJobCategory` | Creates a job category in ServiceM8. Category Name is mandatory. |
| Create Job Checklist Item | `createJobChecklistItem` | Adds a checklist item to a ServiceM8 job. Item Type and Reminder Type are validated server-side; an unsupported value is rejected with "Checklist Item Type is not valid" or "Reminder Type is not valid". |
| Create Job Contact | `createJobContact` | Adds a contact to a ServiceM8 job. Contact Type must be one of the three values ServiceM8 accepts; anything else is rejected with "type is not valid". |
| Create Job Diary Entry | `createJobDiaryEntry` | Adds an entry to a ServiceM8 job's diary. Diary entries are immutable once written - ServiceM8 provides no endpoint to edit or remove them - so treat this as an append-only audit trail. |
| Create Job From Template | `createJobFromTemplate` | Creates a new ServiceM8 job from a job template, optionally overriding the client, address and description. Supply either Client UUID or Client Name, not both. Requires the Job Templates add-on. |
| Create Job Material | `createJobMaterial` | Adds a material or labour line item to a ServiceM8 job. Quantity and a valid Material UUID are both required. Unit Price is tax-exclusive and Displayed Amount is the figure shown on the invoice: send Displayed Amount together with Displayed Amount Is Tax Inclusive, and the two must agree with the line's tax rate or ServiceM8 rejects the request with "inc-tax and ex-tax prices are inconsistent". |
| Create Job Material Bundle | `createJobMaterialBundle` | Adds a material bundle line to a ServiceM8 job's billing. Quantity must be greater than zero. Requires the Material Bundles add-on. |
| Create Job Payment | `createJobPayment` | Records a payment against a ServiceM8 job. This writes a payment record in ServiceM8 only - it does not capture funds through a payment gateway. |
| Create Job Queue | `createJobQueue` | Creates a job queue in ServiceM8 for grouping jobs that are waiting on a common step. |
| Create Knowledge Article | `createKnowledgeArticle` | Creates a knowledge base article in ServiceM8. Title is mandatory. Requires the Knowledge Base add-on. |
| Create Location | `createLocation` | Creates a business location in ServiceM8. Location Name and State are both mandatory, and the name must be unique across the account. |
| Create Material | `createMaterial` | Creates a material, product or labour rate in the ServiceM8 price book. Material Name is mandatory and Item Number must be unique across the account. |
| Create Material Bundle | `createMaterialBundle` | Creates a material bundle (kit) in ServiceM8. Item Number is mandatory, must be 30 characters or fewer and unique across the account. Requires the Material Bundles add-on. |
| Create Note | `createNote` | Adds a note to a ServiceM8 record. Related Object Type must name the object class (for example "job") and Related Object UUID must be a record of that class, otherwise ServiceM8 returns "Invalid object_name provided" or "Invalid object_uuid provided". |
| Create Object Webhook Subscription | `createObjectWebhookSubscription` | Subscribes a callback URL to field-level changes on a ServiceM8 object type, for example the status field on jobs. ServiceM8 expects a form-encoded body and answers {"success":true} without returning the new subscription UUID - use List Webhook Subscriptions to find it before deleting. ServiceM8 serves the webhook API only to API-key and OAuth credentials. |
| Create SMS Template | `createSmsTemplate` | Creates an SMS template in ServiceM8. Template Name is mandatory and must be unique; ServiceM8 rejects a duplicate with "Template Name must be unique". |
| Create Staff Member | `createStaffMember` | Adds a staff member to the ServiceM8 account. First Name and Last Name are mandatory, and Email doubles as the staff member's login name. Adding a staff member affects ServiceM8 subscription billing. |
| Create Staff Message | `createStaffMessage` | Sends an internal message from one ServiceM8 staff member to another. From Staff UUID and To Staff UUID are both mandatory. The message is delivered to the recipient's ServiceM8 app. |
| Create Supplier | `createSupplier` | Creates a supplier in ServiceM8 for purchasing and supplier invoice matching. Requires the Supplier add-on. |
| Create Task | `createTask` | Creates a to-do task in ServiceM8, optionally linked to another record. Task Name is mandatory; when you link the task, Related Object Type must name the object class (for example "job") and Related Object UUID must be a record of that class. |
| Create Tax Rate | `createTaxRate` | Creates a tax rate in ServiceM8 that can then be applied to clients, materials and job line items. Tax Rate Name is mandatory. |
| Delete Allocation Window | `deleteAllocationWindow` | Archives a ServiceM8 allocation window by UUID. ServiceM8 performs a soft delete. |
| Delete Asset | `deleteAsset` | Archives a ServiceM8 asset by UUID. ServiceM8 performs a soft delete. Requires the Asset Management add-on. |
| Delete Asset Type | `deleteAssetType` | Archives a ServiceM8 asset type by UUID. ServiceM8 performs a soft delete. Requires the Asset Management add-on. |
| Delete Asset Type Field | `deleteAssetTypeField` | Archives a ServiceM8 asset type field by UUID. ServiceM8 performs a soft delete. Requires the Asset Management add-on. |
| Delete Attachment | `deleteAttachment` | Archives a ServiceM8 attachment record by UUID. ServiceM8 performs a soft delete. |
| Delete Availability | `deleteAvailability` | Archives a ServiceM8 availability record by UUID. ServiceM8 performs a soft delete. Requires the Availability add-on. |
| Delete Badge | `deleteBadge` | Archives a ServiceM8 badge by UUID. ServiceM8 performs a soft delete. |
| Delete Client | `deleteClient` | Archives a ServiceM8 client (company) by UUID. ServiceM8 performs a soft delete, marking the record inactive rather than erasing it. |
| Delete Client Contact | `deleteClientContact` | Archives a ServiceM8 client contact by UUID. ServiceM8 performs a soft delete, marking the record inactive. |
| Delete Document Template | `deleteDocumentTemplate` | Archives a ServiceM8 document template by UUID. ServiceM8 performs a soft delete. |
| Delete Email Template | `deleteEmailTemplate` | Archives a ServiceM8 email template by UUID. ServiceM8 performs a soft delete. |
| Delete Feedback | `deleteFeedback` | Archives a ServiceM8 feedback record by UUID. ServiceM8 performs a soft delete. Requires the Feedback add-on. |
| Delete Form | `deleteForm` | Archives a ServiceM8 form by UUID. ServiceM8 performs a soft delete. Requires the Forms add-on to be activated on the account. |
| Delete Form Field | `deleteFormField` | Archives a ServiceM8 form field by UUID. ServiceM8 performs a soft delete. Requires the Forms add-on. |
| Delete Form Response | `deleteFormResponse` | Archives a ServiceM8 form response by UUID. ServiceM8 performs a soft delete. Requires the Forms add-on. |
| Delete Job | `deleteJob` | Archives a ServiceM8 job by UUID. ServiceM8 performs a soft delete, setting the job inactive rather than erasing it. Returns {"errorCode":"0","message":"OK"} on success. |
| Delete Job Activity | `deleteJobActivity` | Archives a ServiceM8 job activity by UUID, removing the booking from the dispatch board. ServiceM8 performs a soft delete. |
| Delete Job Allocation | `deleteJobAllocation` | Archives a ServiceM8 job allocation by UUID, unassigning the job from the staff member. ServiceM8 performs a soft delete. |
| Delete Job Category | `deleteJobCategory` | Archives a ServiceM8 job category by UUID. ServiceM8 performs a soft delete. |
| Delete Job Checklist Item | `deleteJobChecklistItem` | Archives a ServiceM8 job checklist item by UUID. ServiceM8 performs a soft delete. |
| Delete Job Contact | `deleteJobContact` | Archives a ServiceM8 job contact by UUID. ServiceM8 performs a soft delete, marking the record inactive. |
| Delete Job Material | `deleteJobMaterial` | Archives a ServiceM8 job material line item by UUID, removing it from the job's billing. ServiceM8 performs a soft delete. |
| Delete Job Material Bundle | `deleteJobMaterialBundle` | Archives a ServiceM8 job material bundle line by UUID, removing it from the job's billing. ServiceM8 performs a soft delete. Requires the Material Bundles add-on. |
| Delete Job Payment | `deleteJobPayment` | Archives a ServiceM8 job payment record by UUID. ServiceM8 performs a soft delete. |
| Delete Job Queue | `deleteJobQueue` | Archives a ServiceM8 job queue by UUID. ServiceM8 performs a soft delete. |
| Delete Knowledge Article | `deleteKnowledgeArticle` | Archives a ServiceM8 knowledge base article by UUID. ServiceM8 performs a soft delete. Requires the Knowledge Base add-on. |
| Delete Location | `deleteLocation` | Archives a ServiceM8 business location by UUID. ServiceM8 performs a soft delete. |
| Delete Material | `deleteMaterial` | Archives a ServiceM8 material by UUID, removing it from the price book. ServiceM8 performs a soft delete. |
| Delete Material Bundle | `deleteMaterialBundle` | Archives a ServiceM8 material bundle by UUID. ServiceM8 performs a soft delete. Requires the Material Bundles add-on. |
| Delete Note | `deleteNote` | Archives a ServiceM8 note by UUID. ServiceM8 performs a soft delete. |
| Delete Service | `deleteService` | Archives a ServiceM8 service template by UUID. ServiceM8 performs a soft delete. Requires Services to be activated on the account. |
| Delete SMS Template | `deleteSmsTemplate` | Archives a ServiceM8 SMS template by UUID. ServiceM8 performs a soft delete. |
| Delete Staff Member | `deleteStaffMember` | Archives a ServiceM8 staff member by UUID, removing their access to the account. ServiceM8 performs a soft delete. |
| Delete Staff Message | `deleteStaffMessage` | Archives a ServiceM8 staff message by UUID. ServiceM8 performs a soft delete. |
| Delete Supplier | `deleteSupplier` | Archives a ServiceM8 supplier by UUID. ServiceM8 performs a soft delete. Requires the Supplier add-on. |
| Delete Task | `deleteTask` | Archives a ServiceM8 task by UUID. ServiceM8 performs a soft delete. |
| Delete Tax Rate | `deleteTaxRate` | Archives a ServiceM8 tax rate by UUID. ServiceM8 performs a soft delete. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Removes a ServiceM8 webhook subscription by its UUID so the callback URL stops receiving events. ServiceM8 serves the webhook API only to API-key and OAuth credentials. |
| Get Account Settings | `getAccountSettings` | Retrieves a single ServiceM8 account (vendor) record by its UUID, including trading hours, currency, timezone and invoice terms. |
| Get Allocation Window | `getAllocationWindow` | Retrieves a single ServiceM8 allocation window by its UUID. |
| Get Asset | `getAsset` | Retrieves a single ServiceM8 asset by its UUID, including its custom field values and location. Requires the Asset Management add-on. |
| Get Asset Type | `getAssetType` | Retrieves a single ServiceM8 asset type by its UUID. Requires the Asset Management add-on. |
| Get Asset Type Field | `getAssetTypeField` | Retrieves a single ServiceM8 asset type field by its UUID. Requires the Asset Management add-on. |
| Get Attachment | `getAttachment` | Retrieves a single ServiceM8 attachment record by its UUID. ServiceM8 also exposes this record at /dboattachment/{uuid}.json. Returns metadata only, not the file bytes. |
| Get Availability | `getAvailability` | Retrieves a single ServiceM8 availability record by its UUID. Requires the Availability add-on. |
| Get Badge | `getBadge` | Retrieves a single ServiceM8 badge by its UUID. |
| Get Client | `getClient` | Retrieves a single ServiceM8 client (company) record by its UUID, including addresses, billing settings and tax rate. |
| Get Client Contact | `getClientContact` | Retrieves a single ServiceM8 client contact by its UUID. |
| Get Document Template | `getDocumentTemplate` | Retrieves a single ServiceM8 document template by its UUID. |
| Get Email | `getEmail` | Retrieves a single ServiceM8 email record by its UUID, including the plain text and HTML bodies. |
| Get Email Template | `getEmailTemplate` | Retrieves a single ServiceM8 email template by its UUID, including its subject and HTML body. |
| Get Feedback | `getFeedback` | Retrieves a single ServiceM8 feedback record by its UUID. Requires the Feedback add-on. |
| Get Form | `getForm` | Retrieves a single ServiceM8 form by its UUID. Requires the Forms add-on to be activated on the account. |
| Get Form Field | `getFormField` | Retrieves a single ServiceM8 form field by its UUID. Requires the Forms add-on. |
| Get Form Response | `getFormResponse` | Retrieves a single ServiceM8 form response by its UUID, including the captured answers. Requires the Forms add-on. |
| Get Inbox Message | `getInboxMessage` | Retrieves a single ServiceM8 inbox message by its UUID, including the full message body. Requires Inbox to be available on the account. |
| Get Job | `getJob` | Retrieves a single ServiceM8 job by its UUID, including addresses, status, scheduling dates, invoicing totals and geocoded location. |
| Get Job Activity | `getJobActivity` | Retrieves a single ServiceM8 job activity (a scheduled or recorded time booking) by its UUID. |
| Get Job Admin Activity | `getJobAdminActivity` | Retrieves a single ServiceM8 job administration time record by its UUID. |
| Get Job Allocation | `getJobAllocation` | Retrieves a single ServiceM8 job allocation by its UUID. |
| Get Job Category | `getJobCategory` | Retrieves a single ServiceM8 job category by its UUID. |
| Get Job Checklist Item | `getJobChecklistItem` | Retrieves a single ServiceM8 job checklist item by its UUID. |
| Get Job Contact | `getJobContact` | Retrieves a single ServiceM8 job contact by its UUID. |
| Get Job Material | `getJobMaterial` | Retrieves a single ServiceM8 job material line item by its UUID. |
| Get Job Material Bundle | `getJobMaterialBundle` | Retrieves a single ServiceM8 job material bundle by its UUID. Requires the Material Bundles add-on. |
| Get Job Payment | `getJobPayment` | Retrieves a single ServiceM8 job payment by its UUID. |
| Get Job Queue | `getJobQueue` | Retrieves a single ServiceM8 job queue by its UUID. |
| Get Job Template | `getJobTemplate` | Retrieves a single ServiceM8 job template by its UUID. Requires the Job Templates add-on. |
| Get Knowledge Article | `getKnowledgeArticle` | Retrieves a single ServiceM8 knowledge base article by its UUID. Requires the Knowledge Base add-on. |
| Get Location | `getLocation` | Retrieves a single ServiceM8 business location by its UUID. |
| Get Material | `getMaterial` | Retrieves a single ServiceM8 material, product or labour rate by its UUID. |
| Get Material Bundle | `getMaterialBundle` | Retrieves a single ServiceM8 material bundle by its UUID, including the materials it contains. Requires the Material Bundles add-on. |
| Get Note | `getNote` | Retrieves a single ServiceM8 note by its UUID. ServiceM8 also exposes this record at /dbonote/{uuid}.json; both paths return the same data. |
| Get Security Role | `getSecurityRole` | Retrieves a single ServiceM8 security role by its UUID. |
| Get Service | `getService` | Retrieves a single ServiceM8 service template by its UUID, including its questions, variations and staff capabilities. Requires Services to be activated on the account. |
| Get SMS Message | `getSmsMessage` | Retrieves a single ServiceM8 SMS record by its UUID. |
| Get SMS Template | `getSmsTemplate` | Retrieves a single ServiceM8 SMS template by its UUID. |
| Get Staff Member | `getStaffMember` | Retrieves a single ServiceM8 staff member by their UUID. |
| Get Staff Message | `getStaffMessage` | Retrieves a single ServiceM8 staff message by its UUID. |
| Get Supplier | `getSupplier` | Retrieves a single ServiceM8 supplier by its UUID. Requires the Supplier add-on. |
| Get Task | `getTask` | Retrieves a single ServiceM8 task by its UUID. |
| Get Tax Rate | `getTaxRate` | Retrieves a single ServiceM8 tax rate by its UUID. |
| List Account Settings | `listAccountSettings` | Returns the ServiceM8 account (vendor) record: business name, ABN, currency, timezone, trading hours, invoice terms and the default status for new jobs. Read-only through the API. |
| List Allocation Windows | `listAllocationWindows` | Returns the allocation windows configured in ServiceM8 - the named time bands (such as Morning or Afternoon) that job allocations are booked into. |
| List Asset Type Fields | `listAssetTypeFields` | Returns the custom fields defined on ServiceM8 asset types. Requires the Asset Management add-on. |
| List Asset Types | `listAssetTypes` | Returns the asset types defined in ServiceM8, which determine the custom fields each asset carries. Requires the Asset Management add-on. |
| List Assets | `listAssets` | Returns the assets recorded against ServiceM8 clients - equipment tracked by asset code and type. Requires the Asset Management add-on to be activated on the account. |
| List Attachments | `listAttachments` | Returns the attachment records held against ServiceM8 jobs and clients - photos, signatures, documents and generated PDFs. Use a $filter such as "related_object_uuid eq '01a0...'" to list the attachments on one record. This returns metadata only; the file bytes live behind a separate ServiceM8 download URL. |
| List Availabilities | `listAvailabilities` | Returns ServiceM8 availability records - the blocks of time staff are marked available or unavailable. Requires the Availability add-on to be activated on the account. |
| List Badges | `listBadges` | Returns the badges defined in ServiceM8. Badges are the coloured labels applied to jobs and clients for at-a-glance categorisation. |
| List Client Contacts | `listClientContacts` | Returns every client contact (company contact) in the ServiceM8 account. Use a $filter such as "company_uuid eq '01a0...'" to list the contacts of one client. |
| List Clients | `listClients` | Returns every client (company) record in the ServiceM8 account. Supply an OData-style $filter expression such as "name eq 'Acme Pty Ltd'" or "active eq 1" to narrow the results. |
| List Document Templates | `listDocumentTemplates` | Returns the document templates configured in ServiceM8, used to generate quotes, invoices and job reports. |
| List Email Templates | `listEmailTemplates` | Returns the email templates configured in ServiceM8 for quotes, invoices and job correspondence. |
| List Emails | `listEmails` | Returns the email history for ServiceM8 jobs, both inbound and outbound, including open and bounce status. Results are cursor-paginated. |
| List Feedback | `listFeedback` | Returns the customer feedback and ratings recorded in ServiceM8. Requires the Feedback add-on to be activated on the account. |
| List Form Fields | `listFormFields` | Returns the questions that make up ServiceM8 forms. Use a $filter such as "form_uuid eq '01a0...'" to list the fields of one form. Requires the Forms add-on. |
| List Form Responses | `listFormResponses` | Returns completed ServiceM8 form submissions, including the captured answers. Use a $filter such as "regarding_object_uuid eq '01a0...'" to list the forms completed on one job. Requires the Forms add-on. |
| List Forms | `listForms` | Returns the forms configured in ServiceM8. Requires the Forms add-on to be activated on the account; without it ServiceM8 answers "form requires addon activation on this account prior to use". |
| List Inbox Messages | `listInboxMessages` | Returns the messages in the ServiceM8 inbox - emails, SMS, online bookings, phone calls and supplier invoices awaiting triage. Requires Inbox to be available on the account; without it ServiceM8 answers "Inbox functionality is not available on this account". |
| List Job Activities | `listJobActivities` | Returns job activities - the scheduled and recorded time bookings that make up the ServiceM8 dispatch board. Use a $filter such as "job_uuid eq '01a0...'" or "staff_uuid eq '01a0...'" to narrow the results. |
| List Job Admin Activities | `listJobAdminActivities` | Returns the administration time recorded against ServiceM8 jobs - office time logged separately from on-site job activities. These records are read-only. |
| List Job Allocations | `listJobAllocations` | Returns job allocations - the assignments of ServiceM8 jobs to staff members within an allocation window. Use a $filter such as "staff_uuid eq '01a0...'" to narrow the results. |
| List Job Categories | `listJobCategories` | Returns the job categories defined in ServiceM8, used to classify jobs and colour-code them on the dispatch board. |
| List Job Checklist Items | `listJobChecklistItems` | Returns the checklist items attached to ServiceM8 jobs. Use a $filter such as "job_uuid eq '01a0...'" to list the checklist for one job. |
| List Job Contacts | `listJobContacts` | Returns every job contact in the ServiceM8 account. Use a $filter such as "job_uuid eq '01a0...'" to list the contacts attached to one job. |
| List Job Material Bundles | `listJobMaterialBundles` | Returns the material bundles billed on ServiceM8 jobs. Use a $filter such as "job_uuid eq '01a0...'" to list the bundles on one job. Requires the Material Bundles add-on. |
| List Job Materials | `listJobMaterials` | Returns the material and labour line items billed against ServiceM8 jobs. Use a $filter such as "job_uuid eq '01a0...'" to list the lines on one job. |
| List Job Payments | `listJobPayments` | Returns the payments recorded against ServiceM8 jobs. Use a $filter such as "job_uuid eq '01a0...'" to list the payments on one job. |
| List Job Queues | `listJobQueues` | Returns the job queues defined in ServiceM8, such as To Be Quoted or Awaiting Parts. |
| List Job Templates | `listJobTemplates` | Returns the job templates defined in ServiceM8. Job templates are read-only through the API and require the Job Templates add-on to be activated on the account. |
| List Jobs | `listJobs` | Returns every job record in the ServiceM8 account. Supply an OData-style $filter expression to narrow the result set, for example "status eq 'Work Order'" or "edit_date gt '2026-01-01 00:00:00'". |
| List Knowledge Articles | `listKnowledgeArticles` | Returns the knowledge base articles stored in ServiceM8. Requires the Knowledge Base add-on to be activated on the account. |
| List Locations | `listLocations` | Returns the business locations configured in ServiceM8, such as depots and branch offices. |
| List Material Bundles | `listMaterialBundles` | Returns the material bundles (kits) defined in ServiceM8 - groups of materials billed together as one line. Requires the Material Bundles add-on to be activated on the account. |
| List Materials | `listMaterials` | Returns the materials, products and labour rates in the ServiceM8 price book. |
| List Notes | `listNotes` | Returns the notes recorded in ServiceM8 against jobs, clients and other records. Use a $filter such as "related_object_uuid eq '01a0...'" to list the notes on one record. |
| List Security Roles | `listSecurityRoles` | Returns the security roles defined in ServiceM8, which control what each staff member can see and do. Security roles are read-only through the API. |
| List Services | `listServices` | Returns the ServiceM8 service templates used for customer online booking, including their questions, pricing variations and staff capabilities. Requires Services to be activated on the account; without it ServiceM8 answers "Services not activated for this Vendor". |
| List SMS Messages | `listSmsMessages` | Returns the SMS history for ServiceM8 jobs, both inbound and outbound. Results are cursor-paginated; pass the cursor returned by the previous page to continue. |
| List SMS Templates | `listSmsTemplates` | Returns the SMS templates configured in ServiceM8 for job notifications and customer updates. |
| List Staff Members | `listStaffMembers` | Returns the staff members in the ServiceM8 account, including their contact details, security role, schedule colour and last known location. |
| List Staff Messages | `listStaffMessages` | Returns the internal messages sent between ServiceM8 staff members. Use a $filter such as "to_staff_uuid eq '01a0...'" to narrow the results. |
| List Suppliers | `listSuppliers` | Returns the suppliers recorded in ServiceM8 for purchasing and supplier invoices. Requires the Supplier add-on to be activated on the account. |
| List Tasks | `listTasks` | Returns the to-do tasks recorded in ServiceM8, including those linked to jobs and clients. Use a $filter such as "assigned_to_staff_uuid eq '01a0...'" to narrow the results. |
| List Tax Rates | `listTaxRates` | Returns the tax rates configured in ServiceM8, such as GST or a zero-rated entry. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | Returns the webhook subscriptions registered on the ServiceM8 account. ServiceM8 serves the webhook API only to API-key and OAuth credentials; an email-and-password connection is answered with 401 "Authorization Required". |
| Mark Inbox Message As Read | `markInboxMessageAsRead` | Marks a ServiceM8 inbox message as read, stamping the read time and the staff member who read it. Requires Inbox to be available on the account. |
| Search All Records | `searchAllRecords` | Runs a free-text search across every searchable ServiceM8 object type and returns the matching records with their type and full data. |
| Search Jobs By Meaning | `searchJobsByMeaning` | Finds ServiceM8 jobs by semantic similarity rather than exact keyword match, using ServiceM8's job embedding search. Useful for questions such as "leaking hot water system" that will not match a job's wording exactly. |
| Search Records By Type | `searchRecordsByType` | Runs a free-text search restricted to one ServiceM8 object type, for example job, company or material. |
| Send Email | `sendEmail` | Sends an email through the ServiceM8 Messaging API. The From address is controlled by ServiceM8 and the account's own email address must be verified in ServiceM8 before any email can be sent. Supply at least one of HTML Body or Text Body. Set Regarding Job UUID to have the email appear in that job's diary and in the account's email history. |
| Send SMS Message | `sendSmsMessage` | Sends an SMS through the ServiceM8 Messaging API. Sending an SMS consumes ServiceM8 SMS credits and is charged to the account, and marketing or promotional SMS is not permitted. The sender ID is chosen by ServiceM8 unless the account has Premium SMS configured. Set Regarding Job UUID to have the message appear in that job's diary. |
| Send Staff Notification | `sendStaffNotification` | Sends a push notification to one or more ServiceM8 staff members. The message supports a limited HTML subset (b, i, br) and the destination URL may deep-link to a ServiceM8 record. |
| Snooze Inbox Message | `snoozeInboxMessage` | Snoozes a ServiceM8 inbox message until a given time, hiding it from the inbox until then. Requires Inbox to be available on the account. |
| Update Allocation Window | `updateAllocationWindow` | Updates a ServiceM8 allocation window. Only the fields you supply are changed. |
| Update Asset | `updateAsset` | Updates a ServiceM8 asset. Only the fields you supply are changed; Asset Code is assigned by ServiceM8 and cannot be set. Requires the Asset Management add-on. |
| Update Asset Type | `updateAssetType` | Updates a ServiceM8 asset type. Only the fields you supply are changed. Requires the Asset Management add-on. |
| Update Asset Type Field | `updateAssetTypeField` | Updates a ServiceM8 asset type field. Only the fields you supply are changed. Requires the Asset Management add-on. |
| Update Attachment | `updateAttachment` | Updates a ServiceM8 attachment record, for example to rename it or change its tags. Only the fields you supply are changed. |
| Update Availability | `updateAvailability` | Updates a ServiceM8 availability record. Only the fields you supply are changed. Requires the Availability add-on. |
| Update Badge | `updateBadge` | Updates a ServiceM8 badge. Only the fields you supply are changed. |
| Update Client | `updateClient` | Updates an existing ServiceM8 client (company). Only the fields you supply are changed; omitted fields keep their current values. Returns {"errorCode":0,"message":"OK"} on success. |
| Update Client Contact | `updateClientContact` | Updates a ServiceM8 client contact. Only the fields you supply are changed; omitted fields keep their current values. |
| Update Document Template | `updateDocumentTemplate` | Updates a ServiceM8 document template. Only the fields you supply are changed. |
| Update Email Template | `updateEmailTemplate` | Updates a ServiceM8 email template. Only the fields you supply are changed. |
| Update Feedback | `updateFeedback` | Updates a ServiceM8 feedback record. Only the fields you supply are changed. Requires the Feedback add-on. |
| Update Form | `updateForm` | Updates a ServiceM8 form. Only the fields you supply are changed. Requires the Forms add-on to be activated on the account. |
| Update Form Field | `updateFormField` | Updates a ServiceM8 form field. Only the fields you supply are changed. Requires the Forms add-on. |
| Update Form Response | `updateFormResponse` | Updates a ServiceM8 form response. Only the fields you supply are changed. Requires the Forms add-on. |
| Update Job | `updateJob` | Updates an existing ServiceM8 job. Only the fields you supply are changed; omitted fields keep their current values. Returns {"errorCode":"0","message":"OK"} on success. |
| Update Job Activity | `updateJobActivity` | Updates a ServiceM8 job activity, for example to reschedule it or reassign it to another staff member. Only the fields you supply are changed. |
| Update Job Allocation | `updateJobAllocation` | Updates a ServiceM8 job allocation, for example to reassign it or mark it complete. Only the fields you supply are changed. |
| Update Job Category | `updateJobCategory` | Updates a ServiceM8 job category. Only the fields you supply are changed. |
| Update Job Checklist Item | `updateJobChecklistItem` | Updates a ServiceM8 job checklist item, for example to mark it complete. Only the fields you supply are changed. |
| Update Job Contact | `updateJobContact` | Updates a ServiceM8 job contact. Only the fields you supply are changed; omitted fields keep their current values. |
| Update Job Material | `updateJobMaterial` | Updates a ServiceM8 job material line item, for example to change the quantity or price. Only the fields you supply are changed. |
| Update Job Material Bundle | `updateJobMaterialBundle` | Updates a ServiceM8 job material bundle line. Only the fields you supply are changed. Requires the Material Bundles add-on. |
| Update Job Payment | `updateJobPayment` | Updates a ServiceM8 job payment record. Only the fields you supply are changed. |
| Update Job Queue | `updateJobQueue` | Updates a ServiceM8 job queue. Only the fields you supply are changed. |
| Update Knowledge Article | `updateKnowledgeArticle` | Updates a ServiceM8 knowledge base article. Only the fields you supply are changed. Requires the Knowledge Base add-on. |
| Update Location | `updateLocation` | Updates a ServiceM8 business location. Only the fields you supply are changed. |
| Update Material | `updateMaterial` | Updates a ServiceM8 material, product or labour rate. Only the fields you supply are changed. |
| Update Material Bundle | `updateMaterialBundle` | Updates a ServiceM8 material bundle. Only the fields you supply are changed. Requires the Material Bundles add-on. |
| Update Note | `updateNote` | Updates a ServiceM8 note. Only the fields you supply are changed. ServiceM8 also exposes this record at /dbonote/{uuid}.json. |
| Update SMS Template | `updateSmsTemplate` | Updates a ServiceM8 SMS template. Only the fields you supply are changed. |
| Update Staff Member | `updateStaffMember` | Updates a ServiceM8 staff member, for example to change their job title, security role or schedule colour. Only the fields you supply are changed. |
| Update Supplier | `updateSupplier` | Updates a ServiceM8 supplier. Only the fields you supply are changed. Requires the Supplier add-on. |
| Update Task | `updateTask` | Updates a ServiceM8 task, for example to mark it complete or reassign it. Only the fields you supply are changed. |
| Update Tax Rate | `updateTaxRate` | Updates a ServiceM8 tax rate. Only the fields you supply are changed. |
| Upload Attachment File | `uploadAttachmentFile` | Uploads the file content for a ServiceM8 attachment that already exists as a metadata record. Create the record first with Create Attachment, then send its UUID here together with the text content. This endpoint takes a multipart body, so only text-based files (txt, csv, svg, json, xml) can be sent; binary formats such as JPEG and PDF are corrupted in transit and are not supported. |
| Upsert Service | `upsertService` | Creates or updates a ServiceM8 service template. Questions, variations and staff capabilities are applied sparsely - anything you omit is left untouched. Requires Services to be activated on the account. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Client Created | `company.created` | Fires when a new client is added. Payload shape modelled from ServiceM8's documented sample event data. |
| Client Updated | `company.updated` | Fires when a client's details change. Payload shape modelled from ServiceM8's documented sample event data. |
| Form Response Created | `form.response_created` | Fires when a form is completed. Requires the Forms add-on. Payload shape modelled from ServiceM8's documented sample event data. |
| Inbox Message Received | `inbox.message_received` | Fires when a new message arrives in the ServiceM8 inbox. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Badge Added | `job.badge_added` | Fires when a badge is applied to a job. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Badge Removed | `job.badge_removed` | Fires when a badge is removed from a job. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Completed | `job.completed` | Fires when a job is marked completed. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Created | `job.created` | Fires when a new job is created in ServiceM8. Payload shape modelled from ServiceM8's documented sample event data (developer.servicem8.com/docs/sample-event-data), not from a captured delivery. |
| Job Invoice Paid | `job.invoice_paid` | Fires when a job invoice is paid. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Invoice Sent | `job.invoice_sent` | Fires when an invoice is sent for a job. Payload shape modelled from ServiceM8's documented sample event data. |

<details>

<summary>See 15 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Job Note Added | `job.note_added` | Fires when a note is added to a job. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Photo Added | `job.photo_added` | Fires when a photo is attached to a job. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Queued | `job.queued` | Fires when a job is placed into a queue. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Quote Accepted | `job.quote_accepted` | Fires when a client accepts a quote. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Quote Sent | `job.quote_sent` | Fires when a quote is sent to the client. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Review Received | `job.review_received` | Fires when a client leaves a review on a job. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Status Changed | `job.status_changed` | Fires when a job moves between Quote, Work Order, Completed or Unsuccessful. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Updated | `job.updated` | Fires when an existing job is changed. Payload shape modelled from ServiceM8's documented sample event data. |
| Job Video Added | `job.video_added` | Fires when a video is attached to a job. Payload shape modelled from ServiceM8's documented sample event data. |
| Proposal Sent | `proposal.sent` | Fires when a proposal is sent to a client. Payload shape modelled from ServiceM8's documented sample event data. |
| Proposal Viewed | `proposal.viewed` | Fires when a client opens a proposal. Payload shape modelled from ServiceM8's documented sample event data. |
| Staff Checked In To Job | `job.checked_in` | Fires when a staff member checks in to a job on site. Payload shape modelled from ServiceM8's documented sample event data. |
| Staff Checked Out Of Job | `job.checked_out` | Fires when a staff member checks out of a job. Payload shape modelled from ServiceM8's documented sample event data. |
| Staff Clocked Off | `staff.clocked_off` | Fires when a staff member clocks off. Payload shape modelled from ServiceM8's documented sample event data. |
| Staff Clocked On | `staff.clocked_on` | Fires when a staff member clocks on. Payload shape modelled from ServiceM8's documented sample event data. |

</details>
