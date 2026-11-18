---
description: "Harvest time tracking, invoicing and project profitability API (v2)."
hidden: true
---

# Harvest

<img src="../../.gitbook/assets/connectors/lg/harvest.png" alt="Harvest logo">

Harvest time tracking, invoicing and project profitability API (v2). Covers clients and contacts, projects with task and user assignments, tasks, time entries including running timers, expenses and expense categories, invoices with payments, messages and item categories, estimates with messages and item categories, users with billable rates, cost rates, teammates and project assignments, roles, company settings, and the time, expense, project budget and uninvoiced reports. Authenticates with a Harvest personal access token sent as a Bearer token together with the Harvest account ID header.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [getharvest.com](https://getharvest.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `harvest` |

## Use it

Add Harvest from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.harvest.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Client | `createClient` | Create a client that projects, invoices and estimates can be billed to. |
| Create Contact | `createContact` | Create a contact person against an existing client. |
| Create Estimate | `createEstimate` | Create an estimate for a client from explicit line items. |
| Create Estimate Item Category | `createEstimateItemCategory` | Create an estimate item category for use as the kind of an estimate line item. |
| Create Expense | `createExpense` | Record an expense against a project. Supply units for unit-based expense categories, otherwise supply total cost. Receipt files must be uploaded through the Harvest web app. |
| Create Expense Category | `createExpenseCategory` | Create an expense category that expenses can be tracked against. |
| Create Free Form Invoice | `createFreeFormInvoice` | Create an invoice from explicit line items rather than from tracked time and expenses. |
| Create Invoice From Tracked Time And Expenses | `createInvoiceFromTrackedTime` | Create an invoice by importing uninvoiced tracked time and expenses from the client's projects. |
| Create Invoice Item Category | `createInvoiceItemCategory` | Create an invoice item category for use as the kind of an invoice line item. |
| Create Invoice Payment | `createInvoicePayment` | Record a payment against an invoice. |
| Create Project | `createProject` | Create a project for a client, including its billing and budgeting configuration. |
| Create Role | `createRole` | Create a business role and optionally assign users to it. |
| Create Task | `createTask` | Create a task that can be assigned to projects for time tracking. |
| Create Task Assignment | `createTaskAssignment` | Assign an existing task to a project so time can be tracked against it. |
| Create Time Entry By Duration | `createTimeEntryByDuration` | Log time against a project task by duration. Omitting hours starts a running timer. |
| Create Time Entry By Start And End Time | `createTimeEntryByStartEndTime` | Log time against a project task using clock times. Requires the company to be configured for timestamp timers. |
| Create User | `createUser` | Invite a new teammate to the Harvest account. |
| Create User Assignment | `createUserAssignment` | Assign a teammate to a project so they can track time against it. |
| Create User Billable Rate | `createUserBillableRate` | Record a new billable rate for a teammate, effective from a given date. |
| Create User Cost Rate | `createUserCostRate` | Record a new internal cost rate for a teammate, effective from a given date. |
| Delete Client | `deleteClient` | Permanently delete a client. Clients with associated projects, invoices or estimates cannot be deleted. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Contact | `deleteContact` | Permanently delete a client contact. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Estimate | `deleteEstimate` | Permanently delete an estimate. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Estimate Item Category | `deleteEstimateItemCategory` | Permanently delete an estimate item category. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Estimate Message | `deleteEstimateMessage` | Delete a message record from an estimate's message history. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Expense | `deleteExpense` | Permanently delete an expense. Invoiced expenses cannot be deleted. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Expense Category | `deleteExpenseCategory` | Permanently delete an expense category. Categories with tracked expenses cannot be deleted. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Invoice | `deleteInvoice` | Permanently delete an invoice. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Invoice Item Category | `deleteInvoiceItemCategory` | Permanently delete an invoice item category. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Invoice Message | `deleteInvoiceMessage` | Delete a message record from an invoice's message history. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Invoice Payment | `deleteInvoicePayment` | Delete a payment previously recorded against an invoice. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Project | `deleteProject` | Permanently delete a project along with its time entries and expenses. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Role | `deleteRole` | Permanently delete a business role. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Task | `deleteTask` | Permanently delete a task. Tasks with tracked time cannot be deleted. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Task Assignment | `deleteTaskAssignment` | Remove a task from a project. Assignments with tracked time cannot be deleted. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Time Entry | `deleteTimeEntry` | Permanently delete a time entry. Invoiced entries cannot be deleted. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete Time Entry External Reference | `deleteTimeEntryExternalReference` | Remove the external system reference attached to a time entry, leaving the entry itself in place. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete User | `deleteUser` | Permanently delete a teammate. Teammates with tracked time or expenses cannot be deleted and must be archived instead. The endpoint returns HTTP 200 with an empty response body on success. |
| Delete User Assignment | `deleteUserAssignment` | Remove a teammate from a project. Assignments with tracked time cannot be deleted. The endpoint returns HTTP 200 with an empty response body on success. |
| Get Client | `getClient` | Retrieve a single client by its Harvest client ID. |
| Get Company | `getCompany` | Retrieve the settings and enabled features of the Harvest company the token belongs to. |
| Get Contact | `getContact` | Retrieve a single client contact by its Harvest contact ID. |
| Get Current User | `getCurrentUser` | Retrieve the teammate the authenticating token belongs to. |
| Get Estimate | `getEstimate` | Retrieve a single estimate, including its line items, by estimate ID. |
| Get Estimate Item Category | `getEstimateItemCategory` | Retrieve a single estimate item category by its ID. |
| Get Expense | `getExpense` | Retrieve a single expense by its Harvest expense ID. |
| Get Expense Category | `getExpenseCategory` | Retrieve a single expense category by its ID. |
| Get Expense Report By Category | `getExpenseReportByCategory` | Report expense totals grouped by expense category over a date range. |
| Get Expense Report By Client | `getExpenseReportByClient` | Report expense totals grouped by client over a date range. |
| Get Expense Report By Project | `getExpenseReportByProject` | Report expense totals grouped by project over a date range. |
| Get Expense Report By Team | `getExpenseReportByTeam` | Report expense totals grouped by teammate over a date range. |
| Get Invoice | `getInvoice` | Retrieve a single invoice, including its line items, by invoice ID. |
| Get Invoice Item Category | `getInvoiceItemCategory` | Retrieve a single invoice item category by its ID. |
| Get Invoice Message Draft | `getInvoiceMessageDraft` | Retrieve the default subject and body Harvest would use for an invoice message, without sending anything. |
| Get Project | `getProject` | Retrieve a single project by its Harvest project ID. |
| Get Project Budget Report | `getProjectBudgetReport` | Report budget consumption and remaining budget for every project on the account. |
| Get Role | `getRole` | Retrieve a single role and the users assigned to it. |
| Get Task | `getTask` | Retrieve a single task by its Harvest task ID. |
| Get Task Assignment | `getTaskAssignment` | Retrieve a single task assignment on a project. |
| Get Time Entry | `getTimeEntry` | Retrieve a single time entry by its Harvest time entry ID. |
| Get Time Report By Client | `getTimeReportByClient` | Report tracked and billable hours grouped by client over a date range. |
| Get Time Report By Project | `getTimeReportByProject` | Report tracked and billable hours grouped by project over a date range. |
| Get Time Report By Task | `getTimeReportByTask` | Report tracked and billable hours grouped by task over a date range. |
| Get Time Report By Team | `getTimeReportByTeam` | Report tracked and billable hours grouped by teammate over a date range. |
| Get Uninvoiced Report | `getUninvoicedReport` | Report uninvoiced hours, fees and expenses per project over a date range. |
| Get User | `getUser` | Retrieve a single teammate by their Harvest user ID. |
| Get User Assignment | `getUserAssignment` | Retrieve a single user assignment on a project. |
| Get User Billable Rate | `getUserBillableRate` | Retrieve a single billable rate recorded for a teammate. |
| Get User Cost Rate | `getUserCostRate` | Retrieve a single internal cost rate recorded for a teammate. |
| List Clients | `listClients` | List every client on the Harvest account, most recently created first. |
| List Contacts | `listContacts` | List every client contact on the account, most recently created first. |
| List Estimate Item Categories | `listEstimateItemCategories` | List the estimate item categories available for estimate line items. |
| List Estimate Messages | `listEstimateMessages` | List the messages that have been sent for an estimate. |
| List Estimates | `listEstimates` | List estimates on the account, most recently issued first. |
| List Expense Categories | `listExpenseCategories` | List every expense category defined on the account. |
| List Expenses | `listExpenses` | List tracked expenses, most recently spent first. |
| List Invoice Item Categories | `listInvoiceItemCategories` | List the invoice item categories available for invoice line items. |
| List Invoice Messages | `listInvoiceMessages` | List the messages that have been sent for an invoice. |
| List Invoice Payments | `listInvoicePayments` | List the payments recorded against an invoice. |
| List Invoices | `listInvoices` | List invoices on the account, most recently issued first. |
| List My Project Assignments | `listMyProjectAssignments` | List the active project assignments of the teammate the authenticating token belongs to. |
| List Project Task Assignments | `listProjectTaskAssignments` | List the tasks assigned to a specific project. |
| List Project User Assignments | `listProjectUserAssignments` | List the people assigned to a specific project. |
| List Projects | `listProjects` | List every project on the account, most recently created first. |
| List Roles | `listRoles` | List the business roles defined on the account. |
| List Task Assignments | `listTaskAssignments` | List task assignments across every project on the account. |
| List Tasks | `listTasks` | List every task defined on the account, most recently created first. |
| List Time Entries | `listTimeEntries` | List tracked time entries, most recently spent first. |
| List User Assignments | `listUserAssignments` | List user assignments across every project on the account. |
| List User Billable Rates | `listUserBillableRates` | List the historical billable rates recorded for a teammate. |
| List User Cost Rates | `listUserCostRates` | List the historical internal cost rates recorded for a teammate. |
| List User Project Assignments | `listUserProjectAssignments` | List the active project assignments of a specific teammate. |
| List User Teammates | `listUserTeammates` | List the teammates assigned to a manager. |
| List Users | `listUsers` | List the teammates on the account, most recently created first. |
| Mark Estimate As Accepted | `markEstimateAsAccepted` | Mark an open estimate as accepted by the client. |
| Mark Estimate As Declined | `markEstimateAsDeclined` | Mark an open estimate as declined by the client. |
| Mark Estimate As Sent | `markEstimateAsSent` | Mark a draft estimate as sent without emailing anyone. |
| Mark Invoice As Closed | `markInvoiceAsClosed` | Close an open invoice as written off. |
| Mark Invoice As Draft | `markInvoiceAsDraft` | Return an open invoice to draft state. |
| Mark Invoice As Sent | `markInvoiceAsSent` | Mark a draft invoice as sent without emailing anyone. |
| Reopen Estimate | `reopenEstimate` | Reopen an accepted or declined estimate. |
| Reopen Invoice | `reopenInvoice` | Reopen a closed or paid invoice. |
| Restart Time Entry | `restartTimeEntry` | Restart a stopped time entry so its timer runs again. |
| Send Estimate Message | `sendEstimateMessage` | Email an estimate to its recipients. This delivers real email to every address supplied. |
| Send Invoice Message | `sendInvoiceMessage` | Email an invoice to its recipients. This delivers real email to every address supplied. |
| Stop Time Entry | `stopTimeEntry` | Stop a running time entry and record the elapsed hours. |
| Update Client | `updateClient` | Update the name, address, currency or archived state of an existing client. |
| Update Company | `updateCompany` | Update the company-wide timer style and weekly capacity settings. |
| Update Contact | `updateContact` | Update the details of an existing client contact. |
| Update Estimate | `updateEstimate` | Update the details or line items of an existing estimate. |
| Update Estimate Item Category | `updateEstimateItemCategory` | Rename an existing estimate item category. |
| Update Expense | `updateExpense` | Update the project, category, amount or notes of an existing expense. |
| Update Expense Category | `updateExpenseCategory` | Update the name, unit pricing or archived state of an expense category. |
| Update Invoice | `updateInvoice` | Update the details or line items of an existing invoice. |
| Update Invoice Item Category | `updateInvoiceItemCategory` | Rename an existing invoice item category. |
| Update Project | `updateProject` | Update the configuration, budget or archived state of an existing project. |
| Update Role | `updateRole` | Rename a role or replace the set of users assigned to it. |
| Update Task | `updateTask` | Update the name, rate or archived state of an existing task. |
| Update Task Assignment | `updateTaskAssignment` | Update the rate, budget or archived state of a project task assignment. |
| Update Time Entry | `updateTimeEntry` | Update the project, task, date, duration or notes of an existing time entry. |
| Update User | `updateUser` | Update a teammate's details, capacity, business roles or access roles. Archive a teammate by setting is active to false. |
| Update User Assignment | `updateUserAssignment` | Update the rate, budget or project manager flag of a project user assignment. |
| Update User Teammates | `updateUserTeammates` | Replace the full list of teammates assigned to a manager. |
