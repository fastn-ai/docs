---
description: "Moxie is a business management platform for freelancers and agencies."
hidden: true
---

# Moxie

<img src="../../.gitbook/assets/connectors/moxie.png" alt="Moxie logo" width="64">

Moxie is a business management platform for freelancers and agencies. This connector wraps the Moxie Public API to create and search clients, contacts, projects, tasks, opportunities, invoices, payments, expenses, time entries, tickets, form submissions, calendar events and attachments.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [withmoxie.com](https://withmoxie.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `moxie` |

## Use it

Add Moxie from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.moxie.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Apply Payment To Invoice | `applyPayment` | Applies a payment to an open Moxie invoice by invoice number. The amount must not exceed the balance owed. |
| Approve Deliverable | `approveDeliverable` | Approves a Moxie project task (deliverable) that is currently in a Client Approval status, identified by exact client, project and task names. |
| Attach File From URL | `attachFileFromUrl` | Downloads a file from an HTTPS URL and attaches it to a Moxie client, project, task, opportunity, expense or ticket. Returns a signed download URL that expires after 15 minutes. Moxie does not verify that the object ID exists, so an incorrect ID stores the file without attaching it to anything. |
| Create Client | `createClient` | Creates a client or prospect record in your Moxie CRM, optionally with contacts. The Moxie Public API has no endpoint to delete clients. |
| Create Contact | `createContact` | Creates a contact in your Moxie CRM and, when the client name exactly matches an existing client, adds it under that client. The Moxie Public API has no endpoint to delete contacts. |
| Create Expense | `createExpense` | Records an expense in your Moxie accounting, optionally allocated to a client and categorized under a vendor. The Moxie Public API has no endpoint to delete expenses. |
| Create Form Submission | `createFormSubmission` | Creates a form submission in your Moxie CRM, optionally linked to a form template and automatically creating a pipeline opportunity in a named stage. The Moxie Public API has no endpoint to delete form submissions. |
| Create Invoice | `createInvoice` | Creates an invoice with line items for an existing Moxie client. Without sendTo the invoice is staged as a draft; with sendTo.send true it is emailed to the listed contacts. The Moxie Public API has no endpoint to delete invoices. |
| Create Opportunity | `createOpportunity` | Creates an opportunity in your Moxie sales pipeline with lead details, to-dos and custom values. The Moxie Public API has no endpoint to delete opportunities. |
| Create Or Update Calendar Event | `createOrUpdateCalendarEvent` | Creates a calendar event on your Moxie homebase calendar, or replaces the existing event with the same event ID (fields you omit on an update are cleared). Useful for syncing calendars that have no native Moxie integration. |

<details>

<summary>See 19 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Project | `createProject` | Creates a project for an existing Moxie client, either from a project template or with an explicit fee schedule. The Moxie Public API has no endpoint to delete projects. |
| Create Task | `createTask` | Creates a task on your Moxie project management board under an existing client and project. The Moxie Public API has no endpoint to delete tasks. |
| Create Ticket | `createTicket` | Creates a support ticket in your Moxie workspace with an initial comment and optional structured answers. Although Moxie documents that unknown requester emails are rejected, the API creates the ticket and adds the email to its CC list, so pass a known contact email. The Moxie Public API has no endpoint to delete tickets. |
| Create Ticket Comment | `createTicketComment` | Adds a public or private comment to an existing Moxie ticket by ticket number. Private is ignored when the author is a client contact. |
| Create Time Entry | `createTimeEntry` | Creates a timesheet entry for a workspace user, optionally assigned to a client, project and task and optionally creating any of them when no exact match exists. The Moxie Public API has no endpoint to delete time entries. |
| Delete Calendar Event | `deleteCalendarEvent` | Deletes or cancels a calendar event previously added to your Moxie homebase calendar, identified by the event ID supplied when it was created. Moxie returns HTTP 200 with an empty body, including when no event has that ID. |
| List Clients | `listClients` | Lists all client and prospect records in your Moxie CRM, including their contacts and payment terms. |
| List Email Templates | `listEmailTemplates` | Lists the names of the email templates in your Moxie workspace, for use when sending invoices. |
| List Form Names | `listFormNames` | Lists the names of the form templates in your Moxie workspace. |
| List Invoice Templates | `listInvoiceTemplates` | Lists the names of the invoice templates in your Moxie workspace. |
| List Pipeline Stages | `listPipelineStages` | Lists the stages of your Moxie sales pipeline with their stage type and color. |
| List Project Task Stages | `listTaskStages` | Lists the statuses of your Moxie project management board, including which ones mark a task complete or awaiting client approval. |
| List Vendor Names | `listVendorNames` | Lists the names of the expense vendors in your Moxie workspace. |
| List Workspace Users | `listWorkspaceUsers` | Lists the users of your Moxie workspace with their user type, profile, and project or feature access. |
| Search Clients | `searchClients` | Searches Moxie client records where the client name starts with, a contact email starts with, or a contact full name contains the query. Omit the query to return all clients; returns an empty list when nothing matches. |
| Search Contacts | `searchContacts` | Searches Moxie contacts by first name, last name or email. Omit the query to return all contacts. |
| Search Payable Invoices | `searchPayableInvoices` | Searches Moxie invoices that are awaiting payment, optionally filtered to a single client by client name. |
| Search Projects | `searchProjects` | Searches Moxie projects, optionally filtered to a single client by client name. Omit the query to return all projects. |
| Upload Attachment | `uploadAttachment` | Uploads a text file as a multipart attachment to a Moxie client, project, task, opportunity, expense or ticket. Returns a signed download URL that expires after 15 minutes. Only text content is supported through this action; use Attach File From URL for binary files. Moxie does not verify that the object ID exists, so an incorrect ID stores the file without attaching it to anything. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Agreement Sent | `AgreementSent` | Sent with header X-Event-Type: AgreementSent. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for AgreementSent to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Agreement Signed | `AgreementSigned` | Sent with header X-Event-Type: AgreementSigned. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for AgreementSigned to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Agreement Viewed | `AgreementViewed` | Sent with header X-Event-Type: AgreementViewed. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for AgreementViewed to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Client Created | `ClientCreate` | Sent with header X-Event-Type: ClientCreate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for ClientCreate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Client Deleted | `ClientDelete` | Sent with header X-Event-Type: ClientDelete. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for ClientDelete to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Client Updated | `ClientUpdate` | Sent with header X-Event-Type: ClientUpdate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for ClientUpdate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Form Completed | `FormCompleted` | Sent with header X-Event-Type: FormCompleted. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for FormCompleted to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example; custom question keys vary per form. |
| Invoice Sent | `InvoiceSent` | Sent with header X-Event-Type: InvoiceSent. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for InvoiceSent to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Meeting Cancelled | `MeetingCancelled` | Sent with header X-Event-Type: MeetingCancelled. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for MeetingCancelled to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Meeting Scheduled | `MeetingScheduled` | Sent with header X-Event-Type: MeetingScheduled. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for MeetingScheduled to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |

<details>

<summary>See 23 more events</summary>

| Event | Id | When it fires |
| --- | --- | --- |
| Meeting Updated | `MeetingUpdated` | Sent with header X-Event-Type: MeetingUpdated. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for MeetingUpdated to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Opportunity Created | `OpportunityCreate` | Sent with header X-Event-Type: OpportunityCreate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for OpportunityCreate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Opportunity Deleted | `OpportunityDelete` | Sent with header X-Event-Type: OpportunityDelete. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for OpportunityDelete to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Opportunity Updated | `OpportunityUpdate` | Sent with header X-Event-Type: OpportunityUpdate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for OpportunityUpdate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Payment Received | `PaymentReceived` | Sent with header X-Event-Type: PaymentReceived. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for PaymentReceived to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Project Completed | `ProjectComplete` | Sent with header X-Event-Type: ProjectComplete. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for ProjectComplete to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Project Created | `ProjectCreate` | Sent with header X-Event-Type: ProjectCreate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for ProjectCreate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Project Updated | `ProjectUpdate` | Sent with header X-Event-Type: ProjectUpdate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for ProjectUpdate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Proposal Sent | `ProposalSent` | Sent with header X-Event-Type: ProposalSent. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for ProposalSent to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Proposal Signed | `ProposalSigned` | Sent with header X-Event-Type: ProposalSigned. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for ProposalSigned to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Proposal Viewed | `ProposalViewed` | Sent with header X-Event-Type: ProposalViewed. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for ProposalViewed to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Task Awaiting Approval | `DeliverableApproval` | Sent with header X-Event-Type: DeliverableApproval. Fires when a task enters a Client Approval status. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for DeliverableApproval to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Task Created | `DeliverableCreate` | Sent with header X-Event-Type: DeliverableCreate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for DeliverableCreate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Task Deleted | `DeliverableDelete` | Sent with header X-Event-Type: DeliverableDelete. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for DeliverableDelete to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Task Updated | `DeliverableUpdate` | Sent with header X-Event-Type: DeliverableUpdate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for DeliverableUpdate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Ticket Closed | `TicketClose` | Sent with header X-Event-Type: TicketClose. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for TicketClose to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Ticket Comment Added | `TicketComment` | Sent with header X-Event-Type: TicketComment. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for TicketComment to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Ticket Created | `TicketCreate` | Sent with header X-Event-Type: TicketCreate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for TicketCreate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Ticket Deleted | `TicketDelete` | Sent with header X-Event-Type: TicketDelete. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for TicketDelete to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Ticket Updated | `TicketUpdate` | Sent with header X-Event-Type: TicketUpdate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for TicketUpdate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Time Entry Created | `TimerCreate` | Sent with header X-Event-Type: TimerCreate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for TimerCreate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Time Entry Deleted | `TimerDelete` | Sent with header X-Event-Type: TimerDelete. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for TimerDelete to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |
| Time Entry Updated | `TimerUpdate` | Sent with header X-Event-Type: TimerUpdate. No registration API: in Moxie go to Workspace settings &gt; Connected Apps &gt; Integrations &gt; Custom Integration, set endpoint auth, then add an event mapping for TimerUpdate to its own fastn webhook URL (the type is only in the header). Payload from Moxie's webhook reference example. |

</details>
