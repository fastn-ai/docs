---
description: "Streamtime is a job management, time tracking and quoting platform for creative agencies and studios."
hidden: true
---

# Streamtime

Streamtime is a job management, time tracking and quoting platform for creative agencies and studios. This connector covers the Streamtime public API: jobs, job items, phases, milestones, roles and users, companies and contacts, quotes, invoices and payments, logged time and expenses, labels, rate cards, branches, reporting and the universal search API.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [streamtime.net](https://streamtime.net) |
| **Authentication** | Credentials you enter |
| **Actions** | 87 |
| **Events** | 0 |
| **Slug** | `streamtime` |

## Use it

Add Streamtime from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.streamtime.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Company | `createCompany` | Creates a company in Streamtime. Companies are the clients and suppliers that jobs, quotes and invoices are raised against. Streamtime has no company delete endpoint, so a company can only be archived afterwards by setting its status to Archived. |
| Create Company Contact | `createCompanyContact` | Creates a contact against a company. Streamtime has no contact delete endpoint, so a contact can only be deactivated afterwards by clearing its active flag. |
| Create Invoice Payment | `createInvoicePayment` | Records a payment against an invoice, reducing its outstanding balance. Invoices that are not synced to an external accounting platform also need the payment account the money was received into. |
| Create Job | `createJob` | Creates a job in Streamtime. Jobs are the unit of work that job items, quotes, invoices, logged time and expenses hang off. Streamtime has no job delete endpoint, so a job can only be completed or archived afterwards with Update Job Status. |
| Create Job Activity Entry | `createJobActivityEntry` | Adds a comment to a job's activity feed. The comment is attributed to the user the API token belongs to. |
| Create Job Item | `createJobItem` | Creates a job item on a job. Job items are the pieces of work that carry a sell rate, planned time, scheduled users and to-do sub-items. |
| Create Job Item Role | `createJobItemRole` | Allocates a role to a job item with a budget of planned minutes and a sell rate, so the item can be estimated by discipline rather than by named person. |
| Create Job Item Sub-Item | `createJobItemSubItem` | Adds a to-do sub-item to a job item, so the work can be broken into checkable steps. |
| Create Job Item User | `createJobItemUser` | Schedules a user onto a job item with a planned number of minutes, so the work appears on that person's schedule. A user can be scheduled onto a given job item only once; a second attempt is rejected with "Job item user already exists". |
| Create Job Milestone | `createJobMilestone` | Creates a milestone on a job, marking a key date such as a client presentation or delivery deadline. |
| Create Job Phase | `createJobPhase` | Creates a phase on a job. Job items can then be assigned to the phase to group them into a stage of work. |
| Create Label | `createLabel` | Attaches a label to a record, optionally also adding it to the master label list for that label type so it can be reused. |
| Create Logged Expense | `createLoggedExpense` | Records a cost against a job, either as an expense or as a purchase order line. Streamtime has no logged expense delete endpoint, so an expense can only be superseded by updating it. |
| Create Logged Time | `createLoggedTime` | Logs a block of time against a job item for a user, either as scheduled time or as completed work. |
| Create Logged Times In Bulk | `createLoggedTimeBulk` | Creates several logged time entries in a single call, for importing a timesheet or scheduling a block of work across days. |
| Delete Job Item User | `deleteJobItemUser` | Removes a user's allocation from a job item, taking the work off that person's schedule. Time already logged against the item is not affected. |
| Delete Job Milestone | `deleteJobMilestone` | Deletes a job milestone. The job itself and its items are unaffected. |
| Delete Job Phase | `deleteJobPhase` | Deletes a job phase. Job items that sat in the phase remain on the job but become unphased. |
| Delete Label | `deleteLabel` | Deletes a label, removing it from the record it was attached to. |
| Delete Logged Time | `deleteLoggedTime` | Deletes a logged time entry, removing it from the job's totals and the user's timesheet. |
| Download Invoice PDF | `getInvoicePdf` | Downloads an invoice as a PDF document, ready to send to the client. |
| Download Quote PDF | `getQuotePdf` | Downloads a quote as a PDF document, ready to send to the client. |
| Duplicate Job | `duplicateJob` | Creates a copy of an existing job, including its structure, and returns the new job. Streamtime has no job delete endpoint, so the copy can only be completed or archived afterwards with Update Job Status. |
| Get Branch | `getBranch` | Retrieves a single branch by its ID, including the external name shown to clients and the tax number used on invoices. |
| Get Company | `getCompany` | Retrieves a single company by its ID, including its branch, rate card, status, contact numbers and notes. |
| Get Contact | `getContact` | Retrieves a single contact by its ID, including the company it belongs to and its status. |
| Get Invoice | `getInvoice` | Retrieves a single invoice by its ID, including its status, dates, totals, balance and any accounting-platform link. |
| Get Invoice HTML | `getInvoiceHtml` | Retrieves the rendered HTML of an invoice, as the client would see it, for embedding in an email or a portal. |
| Get Job | `getJob` | Retrieves a single job by its ID, including its client, contact, lead user, status, budget and the rolled-up planned, logged and invoiced totals. |
| Get Job Item | `getJobItem` | Retrieves a single job item by its ID, including its rate, planned and logged time and the counts of scheduled users and sub-items. |
| Get Job Item Role | `getJobItemRole` | Retrieves a single job item role allocation by its ID, including its planned minutes and sell rate. |
| Get Job Item Sub-Item | `getJobItemSubItem` | Retrieves a single job item sub-item by its ID, including its completion state. |
| Get Job Item User | `getJobItemUser` | Retrieves a single job item user allocation by its ID, including the minutes planned, logged and still outstanding for that person. |
| Get Job Milestone | `getJobMilestone` | Retrieves a single job milestone by its ID, including the job it belongs to and its date. |
| Get Job Phase | `getJobPhase` | Retrieves a single job phase by its ID, including the job it belongs to and its position in that job. |
| Get Logged Expense | `getLoggedExpense` | Retrieves a single logged expense by its ID, including its cost and sell totals, supplier and invoicing state. |
| Get Logged Expense Purchase Order | `getLoggedExpensePurchaseOrder` | Retrieves the purchase order a logged expense belongs to, including its number, totals and payment state. |
| Get Logged Time | `getLoggedTime` | Retrieves a single logged time entry by its ID, including its minutes, status and the job and allocation it belongs to. |
| Get Organisation | `getOrganisation` | Retrieves the details of the Streamtime organisation the API token belongs to, including its name, Streamtime domain, base currency and country. |
| Get Quote | `getQuote` | Retrieves a single quote by its ID, including its status, totals, currency and approval details. |
| Get Quote HTML | `getQuoteHtml` | Retrieves the rendered HTML of a quote, as the client would see it, for embedding in an email or a portal. |
| Get Rate Card | `getRateCard` | Retrieves a single rate card by its ID, including the currency its rates are expressed in. |
| Get Report Setup | `getReportSetup` | Retrieves the grouping options, statistics and filters available for a given report view. Call this before Run Report to discover the valid groupBy and statistics values for that view. |
| Get Role | `getRole` | Retrieves a single role by its ID, including whether the role is still active. |
| Get Search Setup | `getSearchSetup` | Retrieves the filters, sort columns and additional data fields available for a given search view. Call this before Search Records to discover the valid query and sorting options for that view. |
| Get User | `getUser` | Retrieves a single Streamtime user by their ID, including their role, branch, rates and standard working hours. |
| List Branches | `listBranches` | Lists every branch in your Streamtime organisation. Branches represent the separate legal entities or offices that jobs, companies and invoices are raised against. |
| List Company Addresses | `listCompanyAddresses` | Lists the addresses recorded against a company, such as its physical and postal addresses. |
| List Company Contacts | `listCompanyContacts` | Lists the contacts belonging to a company, including their email, phone number and position. |
| List Filter Group Types | `listFilterGroupTypes` | Lists the grouped filter group types available for the given search views. These IDs are what the grouped column-series and time-series reports are bucketed by. |
| List Invoice Line Items | `getInvoiceLineItems` | Lists the line items on an invoice, with their quantities, unit rates, totals and tax treatment. |
| List Invoice Payments | `getInvoicePayments` | Lists the payments and payouts recorded against an invoice, with their dates and amounts. |
| List Invoice Tracked Line Items | `listInvoiceTrackedLineItems` | Lists the tracked line items behind an invoice, showing which job item, expense or quote line each invoice line was billed from. |
| List Job Activity Entries | `listJobActivityEntries` | Lists the activity entries recorded against a job, such as comments and system events, optionally filtered to a single activity type. |
| List Job Item Dependencies | `listJobItemDependencies` | Lists the scheduling dependencies between the job items on a job, showing which item must finish before another can start and by how many days. |
| List Job Item Roles | `listJobItemRoles` | Lists the roles allocated to a job item, with the planned minutes and sell rate budgeted against each role. |
| List Job Item Sub-Items | `listJobItemSubItems` | Lists the to-do sub-items on a job item, showing which are complete and who completed them. |
| List Job Item Users | `listJobItemUsers` | Lists the users scheduled on a job item, with the minutes planned, logged and still outstanding for each of them. |
| List Job Items | `listJobItems` | Lists the job items on a job. Job items are the individual pieces of work that carry rates, planned time, scheduled users and to-do sub-items. |
| List Job Milestones | `listJobMilestones` | Lists the milestones on a job. Milestones mark key dates such as a client presentation or a delivery deadline. |
| List Job Phases | `listJobPhases` | Lists the phases on a job. Phases group job items into stages of work such as Discovery, Design and Build. |
| List Labels | `listLabels` | Lists the master labels defined for a label type, or the labels attached to one specific record when an entity ID is supplied. |
| List Logged Expense Purchase Order Line Items | `listLoggedExpensePurchaseOrderLineItems` | Lists the line items on the purchase order a logged expense belongs to, with their quantities, unit rates and tax treatment. |
| List Quote Line Items | `listQuoteLineItems` | Lists the line items on a quote, with their quantities, unit rates, totals and tax treatment. |
| List Quote Tracked Line Items | `listQuoteTrackedLineItems` | Lists the tracked line items behind a quote, showing which job item or expense each quote line came from and where it was eventually invoiced. |
| List Rate Cards | `listRateCards` | Lists the rate cards defined in your Streamtime organisation. Rate cards set the sell rates applied to job items for a given client or branch. |
| List Roles | `listRoles` | Lists every role defined in your Streamtime organisation. Roles are the disciplines used to rate and schedule work, such as Designer or Account Manager. |
| List User Saved Segments | `listUserSavedSegments` | Lists the saved segments belonging to a user. Saved segments are the stored filter and column configurations a user has created for Streamtime's search and report views. |
| List Users | `listUsers` | Lists every user in your Streamtime organisation with their role, branch, cost and billable rates and standard working hours for each day of the week. |
| Run Column Series Report | `runColumnSeriesReport` | Runs a grouped column-series report, returning results bucketed by a grouped filter dimension. Use it to build bar and column breakdowns of Streamtime data. |
| Run Report | `runReport` | Runs a Streamtime report, returning aggregated statistics for a record type grouped by a chosen dimension and optionally split into time periods. Use Get Report Setup to discover the grouping options and statistics valid for the view. |
| Run Time Series Report | `runTimeSeriesReport` | Runs a grouped time-series report, returning results bucketed by a grouped filter dimension across the reporting period. Use it to build trend lines of Streamtime data over time. |
| Search Labels | `searchLabels` | Fetches the labels attached to many records in one call. The request is a map of Streamtime entity class names to the record IDs you want labels for, so several record types can be queried together. |
| Search Records | `searchRecords` | Searches individual Streamtime records of a chosen type using a filter query, with paging and sorting. Use Get Search Setup to discover the filters, sort columns and additional data available for the view, and use Run Report instead when you want summarised totals. |
| Update Company | `updateCompany` | Replaces an existing company. Streamtime requires the full company on update, so supply every required field including the ones you are not changing; a partial body is rejected and omitted text fields are cleared. Set the company status to Archived to retire a company, since Streamtime has no company delete endpoint. |
| Update Contact | `updateContact` | Replaces an existing contact. Streamtime requires the full contact on update, so supply every required field including the ones you are not changing; a partial body is rejected. Clear the active flag to retire a contact, since Streamtime has no contact delete endpoint. |
| Update Invoice | `updateInvoice` | Updates an invoice, changing its name, reference, dates, discount or status. Streamtime validates the full invoice, so send the fields you want to keep as well as the ones you are changing. |
| Update Job | `updateJob` | Replaces an existing job. Streamtime requires the full job on update, so supply every required field including the ones you are not changing. Use Update Job Status to move a job between statuses. |
| Update Job Item | `updateJobItem` | Replaces an existing job item. Streamtime requires the full item on update, so supply every required field including the ones you are not changing. |
| Update Job Item Role | `updateJobItemRole` | Updates a job item role allocation's sell rate. Streamtime validates the full allocation on update, so send every field, but it derives the stored planned minutes and active state from the job item's own schedule and ignores the values you send for those two. |
| Update Job Item Sub-Item | `updateJobItemSubItem` | Updates a job item sub-item, changing its description, position or completion state. Set the completion fields to tick the sub-item off. |
| Update Job Item User | `updateJobItemUser` | Updates a user's allocation on a job item, changing the planned minutes, sell rate, scheduling window or completion date. Streamtime validates the full allocation, so send every required field. The parent job item's time allocation method decides what actually persists: with Time By Item the item owns the planned time and the values you send here are derived and ignored, so set the item to a per-user allocation method first when you need to plan time per person. |
| Update Job Milestone | `updateJobMilestone` | Replaces a job milestone, renaming it or moving it to a different date. Streamtime requires the full milestone on update, so supply the anchoring job item as well. |
| Update Job Phase | `updateJobPhase` | Renames a job phase or changes its position within the job. |
| Update Job Status | `updateJobStatus` | Moves a job to a different status, for example from In Play to Complete or Archived. This is how a job is retired, since Streamtime has no job delete endpoint. A job must be completed before it can be archived, and an already-archived job is rejected with "This job can't be modified at the moment". |
| Update Logged Expense | `updateLoggedExpense` | Updates a logged expense, changing its quantity, rates, supplier or status. Streamtime validates the full record, so send every required field. |
| Update Logged Time | `updateLoggedTime` | Updates a logged time entry, changing its minutes, date, notes or status. Streamtime validates the full entry, so send every required field. |
