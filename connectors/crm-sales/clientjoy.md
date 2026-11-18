---
description: "Clientjoy is an all-in-one client relationship suite for agencies and freelancers covering leads, clients, proposals, invoices and payments."
---

# Clientjoy

Clientjoy is an all-in-one client relationship suite for agencies and freelancers covering leads, clients, proposals, invoices and payments. This connector wraps the Clientjoy Public API v1: leads with stages and sources, customers, custom fields, items, taxes, currencies, workspace owners, proposals and proposal templates, invoices with payment modes and payment recording, cross-module search and webhook subscriptions.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [clientjoy.io](https://clientjoy.io) |
| **Authentication** | Credentials you enter |
| **Actions** | 34 |
| **Events** | 8 |
| **Slug** | `clientjoy` |

## Use it

Add Clientjoy from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.clientjoy.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Customer | `createCustomer` | Creates a customer in the connected Clientjoy workspace and returns the saved record. Currency, assignee and the primary contact name and email are mandatory. |
| Create Invoice | `createInvoice` | Creates a draft invoice in the connected Clientjoy workspace. The recipient is matched by email; when no contact matches, Clientjoy creates a new customer from the recipient name and email. Line item names and taxes are matched against the workspace's items and taxes. The invoice is not emailed - use Mark Invoice as Sent for that. |
| Create Lead | `createLead` | Creates a lead in the connected Clientjoy workspace and returns the saved lead. Currency, assignee and the primary contact name are mandatory; stage and source are matched by name against the workspace's lead stages and lead sources. |
| Create Proposal | `createProposal` | Creates a proposal in the connected Clientjoy workspace. The recipient is matched by email against the chosen module; when nothing matches, Clientjoy creates a new lead or customer. Set send_email to false to keep the proposal as a draft that is not emailed to the recipient. |
| Create Webhook | `createWebhook` | Registers a webhook in the connected Clientjoy workspace so Clientjoy POSTs a JSON payload to your URL when the chosen entity is created or updated. Returns the webhook id needed to delete it and a secret key you can use to verify payload signatures. The target URL must answer HTTP 200 to a GET. |
| Delete Customer | `deleteCustomer` | Permanently deletes a customer from the connected Clientjoy workspace. The customer id must belong to that workspace. Note a Clientjoy defect: the delete is applied but the API answers HTTP 500 with an HTML error page instead of a JSON envelope, so treat a 500 here as success and confirm with List Customers. A customer id that does not exist returns HTTP 400 with error_code internal_server_error and message 'response.Not found'. |
| Delete Invoice | `deleteInvoice` | Permanently deletes an invoice from the connected Clientjoy workspace, together with any payments recorded against it. The invoice id must belong to that workspace. |
| Delete Lead | `deleteLead` | Permanently deletes a lead from the connected Clientjoy workspace. The lead id must belong to that workspace. Note a Clientjoy defect: the delete is applied but the API answers HTTP 500 with an HTML error page instead of a JSON envelope, so treat a 500 here as success and confirm with List Leads. A lead id that does not exist returns HTTP 400 with error_code internal_server_error and message 'response.Not found'. |
| Delete Proposal | `deleteProposal` | Permanently deletes a proposal from the connected Clientjoy workspace. The proposal id must belong to that workspace. |
| Delete Webhook | `deleteWebhook` | Removes a webhook subscription from the connected Clientjoy workspace so it stops delivering events. Use the id returned by Create Webhook. |
| List Currencies | `listCurrencies` | Lists the currencies enabled in the connected Clientjoy workspace, flagging the default one. Use the ISO codes when creating leads, customers, proposals or invoices. |
| List Custom Fields | `listCustomFields` | Lists the custom fields defined for one module in the connected Clientjoy workspace. The returned ids are what you pass in the custom_fields array when creating or updating leads and customers. |
| List Customers | `listCustomers` | Lists the customers in the connected Clientjoy workspace with their contact, company, billing and shipping details. Results are paginated, ten customers per page. |
| List Invoices | `listInvoices` | Lists the invoices in the connected Clientjoy workspace with their numbering, recipient, line items, totals, status, payment records and public URL. Results are paginated, ten invoices per page. |
| List Items | `listItems` | Lists the products and services in the connected Clientjoy workspace with their rates, categories, taxes and custom fields. Use the item names on proposal and invoice line items. |
| List Lead Sources | `listLeadSources` | Lists the lead sources configured in the connected Clientjoy workspace. Use the source names when creating or updating a lead. |
| List Lead Stages | `listLeadStages` | Lists the lead pipeline stages configured in the connected Clientjoy workspace, in pipeline order. Use the stage names when creating or updating a lead. |
| List Leads | `listLeads` | Lists the leads in the connected Clientjoy workspace with their contact, company, stage, source, owner and deal details. Results are paginated, ten leads per page. |
| List Owners | `listOwners` | Lists the users of the connected Clientjoy workspace. Their email addresses are the valid values for the assignee field on leads and customers. |
| List Payment Modes | `listPaymentModes` | Lists the payment modes available in the connected Clientjoy workspace. Their ids are needed to attach payment options to an invoice and to record a payment. |
| List Proposal Templates | `listProposalTemplates` | Lists the proposal templates available to the connected Clientjoy workspace. Pass type 'custom' to return only the workspace's own templates instead of Clientjoy's standard library. The returned ids feed the template_id and custom_template_id fields on Create Proposal. |
| List Proposals | `listProposals` | Lists the proposals in the connected Clientjoy workspace with their recipient, status, line items, totals, expiry and public URL. Optionally filter by status. Results are paginated, ten proposals per page. |
| List Search Fields | `listSearchFields` | Lists the fields a module can be searched on in the connected Clientjoy workspace. Pass one of the returned field_value strings as the fieldName input of Search Records. Note that the Clientjoy reference documents this route as /v1/fields; the live API serves it at /v1/fields/{module}. |
| List Taxes | `listTaxes` | Lists the tax rates configured in the connected Clientjoy workspace. Use the tax names on proposal and invoice line items. |
| List Workspaces | `listWorkspaces` | Lists the Clientjoy workspaces the connected account belongs to, with the workspace id needed for the workspace header. Results are paginated, ten per page. |
| Login | `login` | Exchanges a Clientjoy email and password for the bearer token this connector authenticates with, and returns the signing user together with their default workspace id. Use it to mint or refresh the API Token credential; the token Clientjoy issues is valid for about six months. |
| Mark Invoice As Sent | `markInvoiceAsSent` | Marks an invoice in the connected Clientjoy workspace as sent, moving it out of draft so payment reminders apply. Clientjoy may deliver the invoice email to the recipient, so only run this against invoices you intend the client to receive. |
| Record Invoice Payment | `recordInvoicePayment` | Records a payment against an invoice in the connected Clientjoy workspace and returns the updated invoice with its new status and payment_records. The amount must not exceed the invoice total, and the payment mode id must come from List Payment Modes. Set do_not_send_mail to true to stop Clientjoy emailing a payment receipt to the client. |
| Search Records | `searchRecords` | Finds leads or customers in the connected Clientjoy workspace whose chosen field exactly matches a value. The entity name is singular - 'lead' or 'customer' - and the match is exact, so pass a full name or a full email address. |
| Update Customer | `updateCustomer` | Updates a customer in the connected Clientjoy workspace. Clientjoy replaces the customer with the object you send, so always submit the complete record: currency, assignee and the primary contact name and email are rejected when missing, and any other field you leave out is cleared. |
| Update Invoice | `updateInvoice` | Updates an invoice in the connected Clientjoy workspace. Clientjoy replaces the invoice with the object you send, so always submit the complete invoice - any field you leave out is cleared. Unlike Create Invoice, this endpoint also requires payment_modes to be present (send an empty array for none); omitting it makes Clientjoy return HTTP 500. |
| Update Lead | `updateLead` | Updates a lead in the connected Clientjoy workspace. Clientjoy replaces the lead with the object you send, so always submit the complete lead: currency, assignee and the primary contact name are rejected when missing, and any other field you leave out is cleared. |
| Update Proposal | `updateProposal` | Updates a proposal in the connected Clientjoy workspace. Clientjoy replaces the proposal with the object you send, so always submit the complete record - module, recipient, title, discount settings, adjustment and send_email are rejected when missing. |
| Update Proposal Status | `updateProposalStatus` | Changes the status of a proposal in the connected Clientjoy workspace, for example to mark it accepted, declined or expired. Setting the status to SENT can trigger Clientjoy's proposal email to the recipient. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Customer Created | `customer.CREATE` | Fires when a customer is created in the workspace. Clientjoy POSTs the customer record itself, with no envelope and no event-type field. Payload schema captured from a real Clientjoy delivery on 2026-09-16. |
| Customer Updated | `customer.UPDATE` | Fires when a customer is changed in the workspace. Clientjoy POSTs the customer record itself, with no envelope and no event-type field. Payload schema captured from a real Clientjoy delivery on 2026-09-16. |
| Invoice Created | `invoice.CREATE` | Registers a CREATE subscription on invoices. Set the status input (draft, unpaid, paid, overdue or partialy paid) - Clientjoy requires it for invoice events. Verified caveat: Clientjoy accepted this subscription but delivered nothing when an invoice was created, in every status tested; invoice.UPDATE does deliver. Payload schema captured from a real Clientjoy delivery on 2026-09-16. |
| Invoice Updated | `invoice.UPDATE` | Fires when an invoice is changed in the workspace. Set the status input (draft, unpaid, paid, overdue or partialy paid) - Clientjoy requires it for invoice events. Clientjoy POSTs the invoice record itself, with no envelope and no event-type field. Payload schema captured from a real Clientjoy delivery on 2026-09-16. |
| Lead Created | `lead.CREATE` | Fires when a lead is created in the workspace. Clientjoy POSTs the lead record itself, with no envelope and no event-type field. Payload schema captured from a real Clientjoy delivery on 2026-09-16. |
| Lead Updated | `lead.UPDATE` | Fires when a lead is changed in the workspace. Clientjoy POSTs the lead record itself, with no envelope and no event-type field. Payload schema captured from a real Clientjoy delivery on 2026-09-16. |
| Proposal Created | `proposal.CREATE` | Fires when a proposal is created in the workspace. Set the status input (draft, open, declined, accepted, sent, revised or expired) - Clientjoy requires it for proposal events. Clientjoy POSTs the proposal record itself, with no envelope and no event-type field. Payload schema captured from a real Clientjoy delivery on 2026-09-16. |
| Proposal Updated | `proposal.UPDATE` | Fires when a proposal is changed in the workspace, including a status change. Set the status input (draft, open, declined, accepted, sent, revised or expired) - Clientjoy requires it for proposal events. Clientjoy POSTs the proposal record itself, with no envelope and no event-type field. Payload schema captured from a real Clientjoy delivery on 2026-09-16. |
