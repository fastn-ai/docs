---
description: "FreshBooks cloud accounting and invoicing platform."
hidden: true
---

# FreshBooks

<img src="../../.gitbook/assets/connectors/freshbooks.png" alt="FreshBooks logo" width="64">

FreshBooks cloud accounting and invoicing platform. Manage clients and contacts, invoices, recurring invoice profiles, estimates and proposals, payments and checkout links, credit notes, expenses and recurring expenses, expense categories, bills and vendors, items and services, taxes, projects, tasks, time entries, retainers, staff and team members, ledger accounts, journal entries, other income, financial reports, and webhook callbacks via the FreshBooks REST API (https://api.freshbooks.com). OAuth 2.0 authorization code auth.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [freshbooks.com](https://freshbooks.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `freshbooks` |

## Use it

Add FreshBooks from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.freshbooks.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Accept Estimate | `acceptEstimate` | Mark a FreshBooks estimate as accepted by the client. |
| Create Client | `createClient` | Create a new client on a FreshBooks account, including optional billing and shipping addresses and secondary contacts. |
| Create Estimate | `createEstimate` | Create a new estimate or rich proposal for a client on a FreshBooks account, including its line items. |
| Create Expense | `createExpense` | Record a new expense on a FreshBooks account, optionally assigning it to a client or project for rebilling. |
| Create Expense Category | `createExpenseCategory` | Create a custom expense category on a FreshBooks account, optionally nested under a parent category. |
| Create Invoice | `createInvoice` | Create a new invoice for a client on a FreshBooks account, including its line items and optional presentation styling. |
| Create Item | `createItem` | Create a new inventory item on a FreshBooks account that can be added to invoice lines. |
| Create Payment | `createPayment` | Record a payment against an invoice on a FreshBooks account. |
| Create Project | `createProject` | Create a new project on a FreshBooks business, optionally attaching the services that can be tracked against it. |
| Create Tax | `createTax` | Create a tax on a FreshBooks account so it can be applied to invoice and expense lines. |

<details>

<summary>See 49 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Create Time Entry | `createTimeEntry` | Log a time entry against a project and service on a FreshBooks business. |
| Delete Client | `deleteClient` | Delete a client on a FreshBooks account. FreshBooks performs a soft delete by setting the client's visibility state to deleted. |
| Delete Client Contact | `deleteClientContact` | Delete a secondary contact belonging to a client on a FreshBooks account. |
| Delete Estimate | `deleteEstimate` | Delete an estimate on a FreshBooks account. FreshBooks performs a soft delete by setting the estimate's visibility state to deleted. |
| Delete Expense | `deleteExpense` | Delete an expense on a FreshBooks account. FreshBooks performs a soft delete by setting the expense's visibility state to deleted. |
| Delete Invoice | `deleteInvoice` | Delete an invoice on a FreshBooks account. FreshBooks performs a soft delete by setting the invoice's visibility state to deleted. |
| Delete Item | `deleteItem` | Delete an inventory item on a FreshBooks account. FreshBooks performs a soft delete by setting the item's visibility state to deleted. |
| Delete Payment | `deletePayment` | Delete a payment on a FreshBooks account. FreshBooks performs a soft delete by setting the payment's visibility state to deleted. |
| Delete Project | `deleteProject` | Permanently delete a project from a FreshBooks business. |
| Delete Tax | `deleteTax` | Permanently delete a tax from a FreshBooks account. Unlike most FreshBooks resources, taxes use a real DELETE rather than a visibility-state soft delete. |
| Delete Time Entry | `deleteTimeEntry` | Permanently delete a time entry from a FreshBooks business. |
| Delete Webhook Callback | `deleteWebhookCallback` | Delete a webhook callback registration from a FreshBooks account, stopping event delivery to its URL. |
| Get Client | `getClient` | Retrieve a single client on a FreshBooks account by its client user ID. |
| Get Current User | `getCurrentUser` | Retrieve the authenticated user's identity profile, including every business membership. Use this first to discover the Account ID and Business ID required by all other FreshBooks actions. |
| Get Estimate | `getEstimate` | Retrieve a single estimate on a FreshBooks account by its estimate ID. |
| Get Expense | `getExpense` | Retrieve a single expense on a FreshBooks account by its expense ID. |
| Get Invoice | `getInvoice` | Retrieve a single invoice on a FreshBooks account by its invoice ID. |
| Get Invoice Share Link | `getInvoiceShareLink` | Retrieve a shareable client link for an invoice. The invoice must already be marked as sent; a draft invoice returns a 422. |
| Get Item | `getItem` | Retrieve a single inventory item on a FreshBooks account by its item ID. |
| Get Payment | `getPayment` | Retrieve a single payment on a FreshBooks account by its payment ID. |
| Get Project | `getProject` | Retrieve a single project on a FreshBooks business by its project ID. |
| Get Tax | `getTax` | Retrieve a single tax on a FreshBooks account by its tax ID. |
| List Clients | `listClients` | List all clients on a FreshBooks account, with optional search filters and paging. Returns a paged collection of client records. |
| List Estimates | `listEstimates` | List estimates on a FreshBooks account, with optional search filters and paging. |
| List Expense Categories | `listExpenseCategories` | List the expense categories available on a FreshBooks account. Use a category ID when creating an expense. |
| List Expenses | `listExpenses` | List expenses on a FreshBooks account, with optional search filters and paging. |
| List Invoices | `listInvoices` | List invoices on a FreshBooks account, with optional search filters and paging. Returns a paged collection of invoice records. |
| List Items | `listItems` | List the inventory items available on a FreshBooks account, with optional paging. |
| List Payments | `listPayments` | List payments recorded on a FreshBooks account, with optional search filters and paging. |
| List Projects | `listProjects` | List projects on a FreshBooks business, with optional filters and paging. Note this endpoint is business-scoped, not account-scoped. |
| List Taxes | `listTaxes` | List the taxes configured on a FreshBooks account. Tax names are referenced on invoice and expense lines. |
| List Time Entries | `listTimeEntries` | List time entries on a FreshBooks business, with optional filters and paging. Note this endpoint is business-scoped, not account-scoped. |
| List Webhook Callbacks | `listWebhookCallbacks` | List the webhook callbacks registered on a FreshBooks account, including their verification state. |
| Register Webhook Callback | `registerWebhookCallback` | Register a webhook callback on a FreshBooks account for a given event. FreshBooks then POSTs a verifier code to the callback URL, which must be confirmed via Verify Webhook Callback before events are delivered. |
| Resend Webhook Verification Code | `resendWebhookVerificationCode` | Ask FreshBooks to re-send the verifier code for an unverified webhook callback to its callback URL. |
| Search Time Entries | `searchTimeEntries` | Search time entries on a FreshBooks business, for example to find all time logged by a specific team member on a specific project. |
| Send Estimate by Email | `sendEstimateByEmail` | Email an existing FreshBooks estimate to one or more recipients, optionally with a customized subject and body. |
| Send Invoice by Email | `sendInvoiceByEmail` | Email an existing FreshBooks invoice to one or more recipients, optionally with a customized subject and body. |
| Update Client | `updateClient` | Update an existing client on a FreshBooks account. Only the fields supplied in the client object are changed. |
| Update Client Contact | `updateClientContact` | Update a secondary contact belonging to a client on a FreshBooks account. |
| Update Estimate | `updateEstimate` | Update an existing estimate on a FreshBooks account. Only the fields supplied in the estimate object are changed. |
| Update Expense | `updateExpense` | Update an existing expense on a FreshBooks account. Only the fields supplied in the expense object are changed. |
| Update Invoice | `updateInvoice` | Update an existing invoice on a FreshBooks account. Only the fields supplied in the invoice object are changed. |
| Update Item | `updateItem` | Update an inventory item on a FreshBooks account. Only the fields supplied in the item object are changed. |
| Update Payment | `updatePayment` | Update a payment recorded on a FreshBooks account. Only the fields supplied in the payment object are changed. |
| Update Project | `updateProject` | Update an existing project on a FreshBooks business. Only the fields supplied in the project object are changed. |
| Update Tax | `updateTax` | Update a tax on a FreshBooks account. Only the fields supplied in the tax object are changed. |
| Update Time Entry | `updateTimeEntry` | Update a time entry on a FreshBooks business. Only the fields supplied in the time entry object are changed. |
| Verify Webhook Callback | `verifyWebhookCallback` | Verify a FreshBooks webhook callback using the verifier code FreshBooks POSTed to the callback URL. FreshBooks only delivers events to verified callbacks. |

</details>
