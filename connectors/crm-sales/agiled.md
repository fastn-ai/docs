---
description: "Agiled is an all-in-one business management platform for agencies and service businesses."
---

# Agiled

Agiled is an all-in-one business management platform for agencies and service businesses. This connector wraps the Agiled Public REST API v1 (https://api.agiled.ai/public/v1): CRM contacts, accounts, deals and pipelines with stages; support tickets; projects, tasks and time entries; invoices, estimates, expenses, payments and products; documents and document templates; forms and form submissions; scheduling event types, booking pages, appointments (book, cancel, reschedule); files; users and token context; plus webhook subscriptions and delivery logs for real-time events such as contact.created, deal.status_changed and invoice.paid. Authentication uses a Public API token from Settings &gt; API, sent as a Bearer token.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [agiled.app](https://agiled.app) |
| **Authentication** | Credentials you enter |
| **Actions** | 109 |
| **Events** | 45 |
| **Slug** | `agiled` |

## Use it

Add Agiled from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.agiled.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Book Appointment | `bookAppointment` | Books an appointment in Agiled through a booking page and event type (booking_page_slug and event_type_slug) at a start time for an invitee. Agiled may send booking confirmation emails to the invitee and host. |
| Cancel Appointment | `cancelAppointment` | Cancels a scheduled Agiled appointment, optionally with a reason. Agiled may notify the invitee. |
| Create Account | `createAccount` | Creates a CRM account (company) in Agiled with name, email, phone, parent account and assigned user. |
| Create Booking Page | `createBookingPage` | Creates a public scheduling booking page in Agiled with title, description, slug, welcome and thank-you messages, theme color, redirect URL and active flag. The public API has no delete endpoint for booking pages. |
| Create Contact | `createContact` | Creates a CRM contact in Agiled with name, email, phone, role, status and assigned user. |
| Create Deal | `createDeal` | Creates a CRM deal in Agiled in a pipeline stage, with value, currency, account, assignee and expected close date. The pipeline must have at least one stage. |
| Create Document | `createDocument` | Creates a draft document (proposal or contract) in Agiled with title, type, content and dates. Agiled assigns the document number; nothing is sent until Send Document is called. |
| Create Document Template | `createDocumentTemplate` | Creates a reusable proposal or contract document template in Agiled with name, type, description, category, content and active flag. The public API has no delete endpoint for templates. |
| Create Estimate | `createEstimate` | Creates a draft estimate (quote) in Agiled for an account, with optional contact, issue and expiry dates, currency and reference. Agiled assigns the estimate number. |
| Create Event Type | `createEventType` | Creates a scheduling event type (bookable meeting type) in Agiled with name, duration, description, location type, price, timezone and slug. Default weekday 09:00-17:00 availability is applied. The public API has no delete endpoint for event types. |
| Create Expense | `createExpense` | Records an expense in Agiled with amount, date (defaults to today), description, category (defaults to Uncategorized), currency, reference, payment method and billable flag. |
| Create File | `createFile` | Creates a file entry in the Agiled file manager. The JSON request schema is not published; live calls with name, content or URL payloads returned a server error and multipart uploads are rejected (Request body must be JSON), so this endpoint is currently not usable through the public API. |
| Create Form | `createForm` | Creates a lead capture or intake form in Agiled with a title, name and field definitions. Sending a fields array is required in practice (a form without fields fails with a server error). |
| Create Form Submission | `createFormSubmission` | Submits an entry to an Agiled form. data holds the values keyed by the form field IDs. The form's submission action runs (by default a CRM contact is created) and a notification email may be sent to the form's notification address. |
| Create Invoice | `createInvoice` | Creates a draft invoice in Agiled for an account, with optional contact, project, issue and due dates, currency, reference, notes and terms. Agiled assigns the invoice number. |
| Create Payment | `createPayment` | Records a payment in Agiled for an account (amount required), optionally applied to an invoice, with payment date, method, currency, transaction reference and notes. This records an offline payment and does not charge anyone. |
| Create Pipeline | `createPipeline` | Creates a CRM deal pipeline in Agiled with a name, description and ordered stages. Include at least one stage; a pipeline created without stages cannot hold deals and the API returns a server error even though the pipeline is saved. |
| Create Product | `createProduct` | Creates a product or service in Agiled with name, price, type (service or product), description, SKU, currency, unit, tax rate and active state. |
| Create Project | `createProject` | Creates a project in Agiled with name, description, status, dates, budget, visibility, owner and optional parent project. |
| Create Task | `createTask` | Creates a task in Agiled with title, description, status, priority, project, assignee, dates, estimated hours and optional parent task or milestone flag. |
| Create Ticket | `createTicket` | Creates a support ticket in Agiled with subject, description, priority, status, type and optional links to an account, contact, project and assignee. |
| Create Time Entry | `createTimeEntry` | Logs a time entry in Agiled between start_time and end_time (both required), optionally linked to a project, task and user, with description, notes and billable flag. |
| Create Webhook Subscription | `createWebhookSubscription` | Creates an active Agiled webhook subscription that POSTs the selected events (e.g. contact.created, deal.status_changed, invoice.paid) to target_url. Each delivery carries event, id, occurred_at, organization_id and data, signed with the X-Agiled-Webhook-Signature header. The signing secret is returned only once. |
| Delete Account | `deleteAccount` | Permanently deletes a CRM account from Agiled. |
| Delete Contact | `deleteContact` | Permanently deletes a CRM contact from Agiled. |
| Delete Deal | `deleteDeal` | Permanently deletes a CRM deal from Agiled. |
| Delete Document | `deleteDocument` | Permanently deletes a document (proposal or contract) from Agiled. |
| Delete Estimate | `deleteEstimate` | Permanently deletes an estimate (quote) from Agiled. |
| Delete Expense | `deleteExpense` | Permanently deletes an expense from Agiled. |
| Delete File | `deleteFile` | Deletes a file from the Agiled file manager. |
| Delete Form | `deleteForm` | Permanently deletes an Agiled form. |
| Delete Form Submission | `deleteFormSubmission` | Permanently deletes an Agiled form submission. Entities it created (such as contacts) are not deleted. |
| Delete Invoice | `deleteInvoice` | Permanently deletes an invoice from Agiled. |
| Delete Payment | `deletePayment` | Permanently deletes a recorded payment from Agiled. |
| Delete Pipeline | `deletePipeline` | Permanently deletes a CRM deal pipeline (and its stages) from Agiled. |
| Delete Product | `deleteProduct` | Deletes a product or service from Agiled. |
| Delete Project | `deleteProject` | Permanently deletes a project from Agiled. |
| Delete Task | `deleteTask` | Permanently deletes a task from Agiled. |
| Delete Ticket | `deleteTicket` | Permanently deletes a support ticket from Agiled. |
| Delete Time Entry | `deleteTimeEntry` | Permanently deletes a time entry from Agiled. |
| Delete Webhook Subscription | `deleteWebhookSubscription` | Deletes an Agiled webhook subscription so no further events are delivered to it. |
| Get Account | `getAccount` | Retrieves a single CRM account by ID from Agiled, optionally including contacts and assigned users. |
| Get Appointment | `getAppointment` | Retrieves a single scheduled appointment (booking) by ID from Agiled. |
| Get Booking Page | `getBookingPage` | Retrieves a single scheduling booking page by ID from Agiled, including its event types and messaging. |
| Get Contact | `getContact` | Retrieves a single CRM contact by ID from Agiled, optionally including related accounts and assigned users. |
| Get Deal | `getDeal` | Retrieves a single CRM deal by ID from Agiled, optionally including related records. |
| Get Document | `getDocument` | Retrieves a single document (proposal or contract) by ID from Agiled, including status, recipients and activity timestamps. |
| Get Document Template | `getDocumentTemplate` | Retrieves a single proposal or contract document template by ID from Agiled, including its content, settings and theme. |
| Get Estimate | `getEstimate` | Retrieves a single estimate (quote) by ID from Agiled. |
| Get Event Type | `getEventType` | Retrieves a single scheduling event type by ID from Agiled, including weekly availability, buffers, booking limits and host. |
| Get Expense | `getExpense` | Retrieves a single expense by ID from Agiled, including tax, billing, recurrence and attachment details. |
| Get File | `getFile` | Retrieves a single file from the Agiled file manager by ID. |
| Get Form | `getForm` | Retrieves a single Agiled form by ID, including its fields, submission action, public link and embed code. |
| Get Form Submission | `getFormSubmission` | Retrieves a single Agiled form submission, including submitted values and the entity it created. |
| Get Invoice | `getInvoice` | Retrieves a single invoice by ID from Agiled, including totals, amounts paid and due, and optionally related records. |
| Get Payment | `getPayment` | Retrieves a single payment by ID from Agiled. |
| Get Pipeline | `getPipeline` | Retrieves a single CRM deal pipeline by ID from Agiled, including its ordered stages. |
| Get Product | `getProduct` | Retrieves a single product or service by ID from Agiled, including pricing, tax, checkout settings and images. |
| Get Project | `getProject` | Retrieves a single project by ID from Agiled, optionally including related records. |
| Get Task | `getTask` | Retrieves a single task by ID from Agiled, optionally including its project and assignee. |
| Get Ticket | `getTicket` | Retrieves a single support ticket by ID from Agiled, optionally including account, contact, assigned user, project, related task and invoice. |
| Get Time Entry | `getTimeEntry` | Retrieves a single time entry by ID from Agiled. |
| Get Token Context | `getTokenContext` | Returns the organization, user and abilities (scopes) of the Agiled API token in use. Useful to verify a connection and discover granted permissions. |
| Get User | `getUser` | Retrieves a single team member (user) of the Agiled organization by ID. |
| List Accounts | `listAccounts` | Lists CRM accounts (companies) in Agiled with pagination (page, per_page up to 100), sorting and filters by name or email. Supported sort fields: created_at, updated_at, name, email. |
| List Appointments | `listAppointments` | Lists scheduled appointments (bookings) in Agiled with pagination (page, per_page up to 100), sorting and filters by host user, event type or status. |
| List Booking Pages | `listBookingPages` | Lists public scheduling booking pages in Agiled with pagination (page, per_page up to 100), sorting and filters by active state or search text. |
| List Contacts | `listContacts` | Lists CRM contacts in Agiled with pagination (page, per_page up to 100), sorting (created_at, updated_at, first_name, last_name, email), includes and filters by email or full name. |
| List Deals | `listDeals` | Lists CRM deals in Agiled with pagination (page, per_page up to 100), sorting and filters by name or status (open, won, lost). |
| List Document Templates | `listDocumentTemplates` | Lists proposal and contract document templates in Agiled. Returns all templates without pagination metadata; the documented search and type filters are currently ignored by the Agiled API (live-verified), so filter client-side on type. |
| List Documents | `listDocuments` | Lists documents (proposals and contracts) in Agiled with pagination (page, per_page up to 100), sorting and filters by status, type or search text. |
| List Estimates | `listEstimates` | Lists estimates (quotes) in Agiled with pagination (page, per_page up to 100), sorting and filters by estimate number, status or account. |
| List Event Types | `listEventTypes` | Lists scheduling event types (bookable meeting types) in Agiled with pagination (page, per_page up to 100), sorting and filters by active state, user or search text. |
| List Expenses | `listExpenses` | Lists expenses in Agiled with pagination (page, per_page up to 100), sorting and filters by account, status or vendor. Note: the category parameter is accepted but currently not applied by the Agiled API (live-verified). |
| List Files | `listFiles` | Lists files and folders in the Agiled file manager with pagination, sorting and filters by file type, parent folder, uploader or search text. Returns files, folders, pagination and storage quota. |
| List Form Submissions | `listFormSubmissions` | Lists submissions received by an Agiled form, with pagination and sorting. Each submission includes the submitted values and the CRM entity (for example a contact) it created. |
| List Forms | `listForms` | Lists lead capture and intake forms in Agiled with pagination (page, per_page up to 100), sorting (created_at, updated_at, name, title, status) and filters by search text or status. |
| List Invoices | `listInvoices` | Lists invoices in Agiled with pagination (page, per_page up to 100), sorting and filters by invoice number or status. |
| List Payments | `listPayments` | Lists payments recorded in Agiled with pagination (page, per_page up to 100), sorting and filters by invoice, status or payment method. |
| List Pipelines | `listPipelines` | Lists CRM deal pipelines in Agiled with their stages (ID, name, order, probability, color). Returns all pipelines without pagination metadata; the documented search parameter is currently ignored by the API. |
| List Products | `listProducts` | Lists products and services in Agiled with pagination (page, per_page up to 100), sorting and filters by category, active state, pricing mode, type or search text. |
| List Projects | `listProjects` | Lists projects in Agiled with pagination (page, per_page up to 100), sorting and filters by name or status. |
| List Tasks | `listTasks` | Lists tasks in Agiled with pagination (page, per_page up to 100), sorting and filters by title, status or project. |
| List Tickets | `listTickets` | Lists support tickets in Agiled with pagination (page, per_page up to 100), sorting and filters by subject, status, priority, account or contact. Supported sort fields: created_at, updated_at, subject, status, priority, due_date. |
| List Time Entries | `listTimeEntries` | Lists time entries in Agiled with pagination (page, per_page up to 100), sorting and filters by user, project, task and date range (date_from, date_to). |
| List Users | `listUsers` | Lists team members (users) of the Agiled organization with their email, role and admin flag. |
| List Webhook Deliveries | `listWebhookDeliveries` | Lists recent Agiled webhook delivery attempts with event type, delivery status, attempt count, target response status and error message. |
| List Webhook Subscriptions | `listWebhookSubscriptions` | Lists webhook subscriptions registered in Agiled with their target URL, subscribed events, status and last delivery time. |
| Reschedule Appointment | `rescheduleAppointment` | Moves a scheduled Agiled appointment to a new time slot. Both start_time and end_time are required and must match an available slot for the event type. Agiled may notify the invitee. |
| Send Document | `sendDocument` | Emails an Agiled document (proposal or contract) to its recipients so they can view, accept or sign it. This sends real email to the recipients. |
| Update Account | `updateAccount` | Updates a CRM account in Agiled. Only the fields sent are changed. |
| Update Booking Page | `updateBookingPage` | Updates a scheduling booking page in Agiled (title, description, slug, messages, theme color, redirect URL, active flag). Only the fields sent are changed. |
| Update Contact | `updateContact` | Updates a CRM contact in Agiled. Only the fields sent are changed. |
| Update Deal | `updateDeal` | Updates a CRM deal in Agiled, for example moving it to another stage, changing its value or marking it won or lost. Only the fields sent are changed. |
| Update Document | `updateDocument` | Updates a document (proposal or contract) in Agiled (title, type, content, dates, status). Only the fields sent are changed. |
| Update Document Template | `updateDocumentTemplate` | Updates a proposal or contract document template in Agiled (name, type, description, category, content, active flag). Only the fields sent are changed. |
| Update Estimate | `updateEstimate` | Updates an estimate (quote) in Agiled (dates, currency, contact, reference, status). Only the fields sent are changed. |
| Update Event Type | `updateEventType` | Updates a scheduling event type in Agiled (name, duration, description, location type, price, active state, timezone, slug). Only the fields sent are changed. |
| Update Expense | `updateExpense` | Updates an expense in Agiled (amount, date, description, category, currency, reference, payment method, billable flag, status). Only the fields sent are changed. |
| Update File | `updateFile` | Updates a file in the Agiled file manager (rename or move to another folder). Only the fields sent are changed. |
| Update Form | `updateForm` | Updates an Agiled form (title, name, description, fields, status, notification email, redirect URL, success message). Only the fields sent are changed. |
| Update Invoice | `updateInvoice` | Updates an invoice in Agiled (dates, currency, contact, project, reference, notes, terms, status). Only the fields sent are changed. |
| Update Payment | `updatePayment` | Updates a recorded payment in Agiled (amount, date, method, reference, notes, status, invoice). Only the fields sent are changed. |
| Update Pipeline | `updatePipeline` | Updates a CRM deal pipeline in Agiled (name, description, stages). Only the fields sent are changed. |
| Update Product | `updateProduct` | Updates a product or service in Agiled (name, price, type, description, SKU, currency, unit, tax rate, active state). Only the fields sent are changed. |
| Update Project | `updateProject` | Updates a project in Agiled (name, description, status, dates, budget, visibility, owner, parent). Only the fields sent are changed. |
| Update Task | `updateTask` | Updates a task in Agiled (title, description, status, priority, project, assignee, dates, estimated hours). Only the fields sent are changed. |
| Update Ticket | `updateTicket` | Updates a support ticket in Agiled (subject, description, status, priority, type, links, assignee, due date). Only the fields sent are changed. |
| Update Time Entry | `updateTimeEntry` | Updates a time entry in Agiled (times, description, notes, project, task, billable flag). Only the fields sent are changed. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Account Created | `account.created` | Agiled account.created event. Delivery body: event, id, occurred_at, organization_id and the full account record in data. |
| Account Updated | `account.updated` | Agiled account.updated event. Delivery body: event, id, occurred_at, organization_id and the full account record in data. |
| Contact Created | `contact.created` | Agiled contact.created event. Delivery body: event, id, occurred_at, organization_id and the full contact record in data. |
| Contact Deleted | `contact.deleted` | Agiled contact.deleted event. Delivery body: event, id, occurred_at, organization_id and the full contact record in data. |
| Contact Updated | `contact.updated` | Agiled contact.updated event. Delivery body: event, id, occurred_at, organization_id and the full contact record in data. |
| Deal Created | `deal.created` | Agiled deal.created event. Delivery body: event, id, occurred_at, organization_id and the full deal record in data. |
| Deal Deleted | `deal.deleted` | Agiled deal.deleted event. Delivery body: event, id, occurred_at, organization_id and the full deal record in data. |
| Deal Status Changed | `deal.status_changed` | Agiled deal.status_changed event. Delivery body: event, id, occurred_at, organization_id and the full deal record in data. |
| Deal Updated | `deal.updated` | Agiled deal.updated event. Delivery body: event, id, occurred_at, organization_id and the full deal record in data. |
| Document Created | `document.created` | Agiled document.created event. Delivery body: event, id, occurred_at, organization_id and the full document record in data. |
| Estimate Created | `estimate.created` | Agiled estimate.created event. Delivery body: event, id, occurred_at, organization_id and the full estimate record in data. |
| Estimate Deleted | `estimate.deleted` | Agiled estimate.deleted event. Delivery body: event, id, occurred_at, organization_id and data.id of the deleted estimate. |
| Estimate Updated | `estimate.updated` | Agiled estimate.updated event. Delivery body: event, id, occurred_at, organization_id and the full estimate record in data. |
| Expense Created | `expense.created` | Agiled expense.created event. Delivery body: event, id, occurred_at, organization_id and the full expense record in data. |
| Expense Deleted | `expense.deleted` | Agiled expense.deleted event. Delivery body: event, id, occurred_at, organization_id and the full expense record in data. |
| Expense Updated | `expense.updated` | Agiled expense.updated event. Delivery body: event, id, occurred_at, organization_id and the full expense record in data. |
| Form Created | `form.created` | Agiled form.created event. Delivery body: event, id, occurred_at, organization_id and the full form record in data. |
| Form Deleted | `form.deleted` | Agiled form.deleted event. Delivery body: event, id, occurred_at, organization_id and the full form record in data. |
| Form Submission Received | `form_submission.received` | Agiled form_submission.received event. Delivery body: event, id, occurred_at, organization_id and the full form submission record in data. |
| Form Updated | `form.updated` | Agiled form.updated event. Delivery body: event, id, occurred_at, organization_id and the full form record in data. |
| Invoice Created | `invoice.created` | Agiled invoice.created event. Delivery body: event, id, occurred_at, organization_id and the full invoice record in data. |
| Invoice Deleted | `invoice.deleted` | Agiled invoice.deleted event. Delivery body: event, id, occurred_at, organization_id and the full invoice record in data. |
| Invoice Paid | `invoice.paid` | Agiled invoice.paid event. Delivery body: event, id, occurred_at, organization_id and the full invoice record in data. |
| Invoice Updated | `invoice.updated` | Agiled invoice.updated event. Delivery body: event, id, occurred_at, organization_id and the full invoice record in data. |
| Payment Completed | `payment.completed` | Agiled payment.completed event. Delivery body: event, id, occurred_at, organization_id and the full payment record in data. |
| Payment Created | `payment.created` | Agiled payment.created event. Delivery body: event, id, occurred_at, organization_id and the full payment record in data. |
| Payment Deleted | `payment.deleted` | Agiled payment.deleted event. Delivery body: event, id, occurred_at, organization_id and data with the deleted payment id and invoice_id. |
| Payment Updated | `payment.updated` | Agiled payment.updated event. Delivery body: event, id, occurred_at, organization_id and the full payment record in data. |
| Pipeline Created | `pipeline.created` | Agiled pipeline.created event. Delivery body: event, id, occurred_at, organization_id and the full pipeline record in data. |
| Product Created | `product.created` | Agiled product.created event. Delivery body: event, id, occurred_at, organization_id and the full product record in data. |
| Product Deleted | `product.deleted` | Agiled product.deleted event. Delivery body: event, id, occurred_at, organization_id and the full product record in data. |
| Product Updated | `product.updated` | Agiled product.updated event. Delivery body: event, id, occurred_at, organization_id and the full product record in data. |
| Project Created | `project.created` | Agiled project.created event. Delivery body: event, id, occurred_at, organization_id and the full project record in data. |
| Project Deleted | `project.deleted` | Agiled project.deleted event. Delivery body: event, id, occurred_at, organization_id and the full project record in data. |
| Project Updated | `project.updated` | Agiled project.updated event. Delivery body: event, id, occurred_at, organization_id and the full project record in data. |
| Stage Created | `stage.created` | Agiled stage.created event. Delivery body: event, id, occurred_at, organization_id and the full pipeline stage record in data. |
| Task Created | `task.created` | Agiled task.created event. Delivery body: event, id, occurred_at, organization_id and the full task record in data. |
| Task Deleted | `task.deleted` | Agiled task.deleted event. Delivery body: event, id, occurred_at, organization_id and the full task record in data. |
| Task Status Changed | `task.status_changed` | Agiled task.status_changed event. Delivery body: event, id, occurred_at, organization_id and the full task record in data. |
| Task Updated | `task.updated` | Agiled task.updated event. Delivery body: event, id, occurred_at, organization_id and the full task record in data. |
| Ticket Created | `ticket.created` | Agiled ticket.created event. Delivery body: event, id, occurred_at, organization_id and the full ticket record in data. |
| Ticket Deleted | `ticket.deleted` | Agiled ticket.deleted event. Delivery body: event, id, occurred_at, organization_id and the full ticket record in data. |
| Ticket Updated | `ticket.updated` | Agiled ticket.updated event. Delivery body: event, id, occurred_at, organization_id and the full ticket record in data. |
| Time Entry Created | `time_entry.created` | Agiled time_entry.created event. Delivery body: event, id, occurred_at, organization_id and the full time entry record in data. |
| Time Entry Updated | `time_entry.updated` | Agiled time_entry.updated event. Delivery body: event, id, occurred_at, organization_id and the full time entry record in data. |
