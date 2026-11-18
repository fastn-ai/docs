---
description: "Everhour time tracking, project management and billing API."
hidden: true
---

# Everhour

<img src="../../.gitbook/assets/connectors/lg/everhour.png" alt="Everhour logo">

Everhour time tracking, project management and billing API. Manage time records, timers, timecards, timesheets and approvals, projects, sections, tasks, custom fields, clients, invoices, expenses, resource planning schedules, time off, reports, team users and webhooks.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [everhour.com](https://everhour.com) |
| **Authentication** | API key |
| **Slug** | `everhour` |

## Use it

Add Everhour from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.everhour.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Attachment to Expense | `addAttachmentToExpense` | Upload a file and attach it to an existing expense. Only JPG, PNG and PDF files are supported. |
| Add Invoice Payment | `addInvoicePayment` | Record a payment against an invoice. The invoice status moves to partial once part of the total is paid and to paid once the full amount is covered. |
| Add Time | `addTime` | Log time against a task for a given date, optionally on behalf of another team member. |
| Approve or Reject Timesheet | `reviewTimesheetApproval` | Approve or reject a weekly timesheet submitted for approval, optionally for specific days of the week only. |
| Archive or Unarchive Project | `archiveProject` | Archive a project to hide it from active lists, or restore it by passing archived as false. |
| Clock In | `clockIn` | Clock a team member in, starting their working day. |
| Clock Out | `clockOut` | Clock a team member out, ending their working day. |
| Create Attachment | `createAttachment` | Upload a file that can then be attached to an expense or a time off request. Only JPG, PNG and PDF files are supported. |
| Create Client | `createClient` | Create a new client and optionally assign existing projects to it. |
| Create Expense | `createExpense` | Record an expense against a project, in a category, optionally billable to the client. |
| Create Expense Category | `createExpenseCategory` | Add an expense category, optionally unit-based with a price per unit such as mileage. |
| Create Invoice | `createInvoice` | Create an invoice for a client from the time and expenses tracked on its projects in a period. |
| Create Project | `createProject` | Create a native Everhour project and optionally assign team members to it. |
| Create Project Custom Field | `createProjectField` | Add a custom field to a project. Select fields support up to ten options. |
| Create Schedule Assignment | `createAssignment` | Schedule one or more team members on a project for a date range in the resource planner. |
| Create Section | `createSection` | Create a section in a project to group tasks. |
| Create Task | `createTask` | Create a task in a project section, optionally with labels, a description, a due date and assignees. |
| Create Time Off | `createTimeOff` | Book time off for a team member in the resource planner, with a type, period of the day and optional approval workflow. |
| Create Time Off Allocation | `createTimeOffAllocation` | Allocate a time off allowance to one or more team members for a period, with an accrual schedule. |
| Create Time Off Type | `createTimeOffType` | Add a time off type that team members can book against. |
| Create Webhook | `createWebhook` | Register a webhook so Everhour posts the selected events to your endpoint. Everhour first sends a verification POST carrying an X-Hook-Secret header, which your endpoint must echo back in its response for the webhook to become active. |
| Delete Attachment | `deleteAttachment` | Delete an attachment and its file. |
| Delete Client Budget | `deleteClientBudget` | Remove the budget configured on a client. |
| Delete Custom Field | `deleteField` | Delete a custom field and its values from the project. |
| Delete Expense | `deleteExpense` | Delete an expense from the team. |
| Delete Expense Category | `deleteExpenseCategory` | Delete an expense category, either moving its expenses to another category or removing them. |
| Delete Invoice | `deleteInvoice` | Permanently delete an invoice and release the time and expenses it covered. |
| Delete Project | `deleteProject` | Permanently delete a project along with its tasks and tracked time. |
| Delete Schedule Assignment | `deleteAssignment` | Remove an assignment from the resource planner. |
| Delete Section | `deleteSection` | Delete a section from its project. |
| Delete Task | `deleteTask` | Permanently delete a task and its tracked time. |
| Delete Task Estimate | `deleteTaskEstimate` | Remove the estimate configured on a task. |
| Delete Time Off Allocation | `deleteTimeOffAllocation` | Remove a time off allocation from a team member. |
| Delete Time Off Type | `deleteTimeOffType` | Delete a time off type from the team. |
| Delete Time Record | `deleteTimeRecord` | Delete a time record. |
| Delete Timecard | `deleteTimecard` | Delete the timecard of a team member for a specific date. |
| Delete Webhook | `deleteWebhook` | Remove a webhook so Everhour stops posting events to it. |
| Discard Timesheet Approval Request | `discardTimesheetApproval` | Withdraw an approval request you previously submitted for a weekly timesheet. |
| Download Attachment | `downloadAttachment` | Download the file content of an attachment using its download token. |
| Export Invoice to Accounting | `exportInvoice` | Export an invoice to the connected accounting integration, such as Xero, QuickBooks or FreshBooks. |
| Get Client | `getClient` | Retrieve a single client by ID, including its assigned projects, billing details and budget. |
| Get Clients Report | `getClientsReport` | Retrieve profitability and time metrics grouped by client. All times are in seconds and all amounts in cents. |
| Get Current User | `getCurrentUser` | Retrieve the profile of the Everhour user that owns the API token, including role, status, permissions and time tracking policy. |
| Get Estimates Report | `getEstimatesReport` | Retrieve estimates against tracked time for tasks due in a period. This legacy report is deprecated by Everhour in favour of the projects, clients and users reports. |
| Get Invoice | `getInvoice` | Retrieve a single invoice by ID, including its line items, discount, tax and totals. |
| Get Project | `getProject` | Retrieve a single project by ID, including its type, assigned users, billing, rate and budget configuration. |
| Get Projects Report | `getProjectsReport` | Retrieve profitability and time metrics grouped by project. All times are in seconds and all amounts in cents. |
| Get Running Timer | `getRunningTimer` | Retrieve the timer currently running for the token owner, including its task and elapsed duration. |
| Get Section | `getSection` | Retrieve a single section by ID. |
| Get Task | `getTask` | Retrieve a single task by ID, including its section, labels, estimate and tracked time. Pass Include Billing to also return billable rates and amounts. |
| Get Time Report | `getTimeReport` | Retrieve tracked time for a period grouped by the dimensions you choose. This legacy report is deprecated by Everhour in favour of the projects, clients and users reports. |
| Get Timecard | `getTimecard` | Retrieve the timecard of a team member for a specific date, including its clock-in, clock-out and change history. |
| Get Users Report | `getUsersReport` | Retrieve time, cost and profitability metrics grouped by team member, including time off. All times are in seconds and all amounts in cents. |
| Get Webhook | `getWebhook` | Retrieve a single webhook by ID, including its target URL, events and last delivery time. |
| List Clients | `listClients` | Retrieve all clients in the team, optionally filtered by name, including their projects and budget configuration. |
| List Expense Categories | `listExpenseCategories` | Retrieve the expense categories configured for the team, including unit-based categories and their unit prices. |
| List Expenses | `listExpenses` | Retrieve every expense recorded in the team, including its category, project, amount and attachments. |
| List Invoices | `listInvoices` | Retrieve every invoice in the team, including its client, line items, totals and status. |
| List Project Custom Fields | `listProjectFields` | Retrieve the custom fields configured on a project, including their type, format and options. |
| List Project Sections | `listProjectSections` | Retrieve all sections, columns or lists that belong to a project. |
| List Project Tasks | `listProjectTasks` | Retrieve the tasks of a project with pagination, optionally filtered by name or excluding closed tasks. |
| List Project Time Records | `listProjectTimeRecords` | Retrieve the time records logged against a single project for a date range. |
| List Projects | `listProjects` | Retrieve projects in the team, optionally filtered by name or source integration. |
| List Schedule Assignments | `listAssignments` | Retrieve resource planner assignments and time off, optionally filtered by type, project, task, client or date range. |
| List Task Time Records | `listTaskTimeRecords` | Retrieve the time records logged against a single task for a date range. |
| List Team Timers | `listTeamTimers` | Retrieve the timers currently running across every member of the team. |
| List Team Timesheets | `listTeamTimesheets` | Retrieve the weekly timesheets of the whole team, optionally for a specific week. |
| List Team Users | `listTeamUsers` | Retrieve every member of the Everhour team, including their role, status, capacity, cost and billable rates. |
| List Time Off Allocations | `listTimeOffAllocations` | Retrieve the time off allowances allocated to team members, including days accrued, carried over and used. |
| List Time Off Types | `listTimeOffTypes` | Retrieve the time off types configured for the team, such as paid, sick or unpaid leave. |
| List Time Records | `listTimeRecords` | Retrieve time records across the whole team for a date range, with pagination. Pass Include Billing to also return rates and amounts. |
| List Timecards | `listTimecards` | Retrieve the clock-in and clock-out timecards of the whole team for a date range. Defaults to the last two weeks. |
| List User Time Records | `listUserTimeRecords` | Retrieve the time records of a single team member for a date range. |
| List User Timecards | `listUserTimecards` | Retrieve the timecards of a single team member for a date range. Defaults to the last two weeks. |
| List User Timesheets | `listUserTimesheets` | Retrieve the most recent weekly timesheets of a team member, including tasks, daily totals, timecards and approval state. |
| List Webhooks | `listWebhooks` | Retrieve every webhook registered for the team, including the events each one is subscribed to. |
| Refresh Invoice Line Items | `refreshInvoiceLineItems` | Rebuild the line items of an invoice from the time and expenses currently tracked in the period, applying the given naming masks. |
| Reorder Project Custom Fields | `reorderProjectFields` | Set the display order of the custom fields on a project. |
| Search Project Tasks | `searchProjectTasks` | Search tasks by name within a single project. |
| Search Tasks | `searchTasks` | Search tasks by name across every project in the team. |
| Send Invoice | `sendInvoice` | Mark an invoice as sent to the client. Once every line item is paid the invoice status becomes paid. |
| Start Timer | `startTimer` | Start a timer on a task for the token owner. Any timer already running is stopped first. |
| Stop Timer | `stopTimer` | Stop the timer currently running for the token owner and convert the elapsed time into a time record. |
| Submit Timesheet for Approval | `submitTimesheetApproval` | Submit a weekly timesheet for approval, or approve it directly if you are an admin. The timesheet ID is the user ID followed by the week ID. |
| Sync Integration Project | `syncIntegrationProject` | Immediately import a project from a connected integration such as Asana, Trello or ClickUp into Everhour. Safe to call repeatedly - an already imported project is returned unchanged. |
| Update Client | `updateClient` | Update the name, assigned projects or business details of an existing client. Only the fields you provide are changed. |
| Update Client Budget | `updateClientBudget` | Set or replace the budget of a client, including its type, value, period and overbudget rules. |
| Update Custom Field | `updateField` | Update the name, type, format or options of a custom field. Only the fields you provide are changed. |
| Update Expense | `updateExpense` | Update the amount, category, date, project or other details of an expense. |
| Update Expense Category | `updateExpenseCategory` | Update the name, color or unit pricing of an expense category. Only the fields you provide are changed. To change unit pricing you must send Unit Based, Unit Name and Unit Price together - Unit Price is ignored when sent on its own. |
| Update Invoice | `updateInvoice` | Update the number, dates, reference, notes, discount, tax or line items of an invoice. |
| Update Project | `updateProject` | Update the name, type or assigned users of a project. Only the fields you provide are changed. |
| Update Project Billing and Budget | `updateProjectBilling` | Configure how a project is billed, which rates apply and what budget it is tracked against. |
| Update Schedule Assignment | `updateAssignment` | Update the dates, project, member or scheduled time of a resource planner assignment. |
| Update Section | `updateSection` | Rename, reposition or archive a section. Only the fields you provide are changed. |
| Update Task | `updateTask` | Update a task including its name, section, labels, description, due date, assignees, status and custom field values. Only the fields you provide are changed. |
| Update Task Estimate | `updateTaskEstimate` | Set the estimate of a task, either as one overall value or as per-member values. |
| Update Time Off Allocation | `updateTimeOffAllocation` | Update the period, days or accrual settings of a time off allocation. |
| Update Time Off Type | `updateTimeOffType` | Update the name, color, paid flag or description of a time off type. |
| Update Time Record | `updateTimeRecord` | Update the duration, date, task, member or comment of a time record. Only the fields you provide are changed. |
| Update Timecard | `updateTimecard` | Adjust the clock-in time, clock-out time or break duration recorded on a timecard. |
| Update Webhook | `updateWebhook` | Update the target URL, subscribed events or project scope of a webhook. Changing the target URL triggers the X-Hook-Secret verification again. |
