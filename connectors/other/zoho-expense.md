---
description: "Zoho Expense is Zoho's travel and expense management platform."
---

# Zoho Expense

Zoho Expense is Zoho's travel and expense management platform. This connector wraps the Zoho Expense REST API v1 (zohoapis.com/expense/v1): organizations, expenses, expense reports and their approval and reimbursement lifecycle, trips, employee advances, users, customers, projects, expense categories, currencies, taxes and reporting tags. Every request is scoped by an organization ID. OAuth 2.0 authorization code auth via the shared Zoho API Console app.

| | |
| --- | --- |
| **Category** | [Other](README.md) |
| **Website** | [expense.zoho.com](https://expense.zoho.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 81 |
| **Events** | 0 |
| **Slug** | `zohoExpense` |

## Use it

Add Zoho Expense from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.zohoExpense.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Project | `activateProject` | Mark a project as active in Zoho Expense so expenses can be booked against it again. |
| Activate User | `activateUser` | Reactivate a previously deactivated user in a Zoho Expense organization. |
| Add Expenses To Report | `addExpensesToReport` | Attach one or more existing expenses to a Zoho Expense expense report. |
| Approve Employee Advance | `approveEmployeeAdvance` | Approve a submitted employee advance request in Zoho Expense. |
| Approve Expense Report | `approveExpenseReport` | Approve a submitted Zoho Expense expense report. The connected user must be an approver on the report. |
| Approve Trip | `approveTrip` | Approve a submitted travel request in Zoho Expense. The connected user must be an approver on the trip. |
| Assign User Role | `assignUserRole` | Assign a specific role to a user in a Zoho Expense organization. |
| Cancel Trip | `cancelTrip` | Cancel a travel request in Zoho Expense, optionally recording why the trip is no longer going ahead. |
| Close Trip | `closeTrip` | Close a completed travel request in Zoho Expense once all its expenses have been accounted for. |
| Create Currency | `createCurrency` | Add a currency to a Zoho Expense organization so expenses can be recorded in it. |
| Create Customer | `createCustomer` | Create a customer in Zoho Expense that billable expenses and projects can be associated with. |
| Create Employee Advance | `createEmployeeAdvance` | Record an advance payment made to an employee in Zoho Expense, optionally linked to a trip, customer or project. |
| Create Expense | `createExpense` | Record a new expense in Zoho Expense. Each expense carries one or more line items describing the category and amount being claimed. |
| Create Expense Category | `createExpenseCategory` | Create an expense category in Zoho Expense, optionally with spending limits and a receipt threshold. |
| Create Expense Report | `createExpenseReport` | Create a new expense report in Zoho Expense covering a date range, optionally attaching existing expenses to it on creation. |
| Create Project | `createProject` | Create a project in Zoho Expense against a customer, so expenses and trips can be tracked and billed to it. |
| Create Reporting Tag | `createReportingTag` | Create a reporting tag in Zoho Expense used to classify expenses and reports for analysis. |
| Create Tax | `createTax` | Create a tax rate in a Zoho Expense organization that can be applied to expense line items. |
| Create Trip | `createTrip` | Create a travel request (trip) in Zoho Expense with a budget and travel type, ready to be submitted for approval. |
| Create User | `createUser` | Invite a new user into a Zoho Expense organization with a role, approver and optional employee profile details. |
| Deactivate Project | `deactivateProject` | Mark a project as inactive in Zoho Expense, preventing new expenses from being booked against it. |
| Deactivate User | `deactivateUser` | Deactivate a user in a Zoho Expense organization, preventing them from signing in while retaining their records. |
| Delete Currency | `deleteCurrency` | Remove a currency from a Zoho Expense organization. |
| Delete Customer | `deleteCustomer` | Delete a customer from a Zoho Expense organization. |
| Delete Employee Advance | `deleteEmployeeAdvance` | Delete an employee advance payment from Zoho Expense. |
| Delete Expense | `deleteExpense` | Delete a single expense from Zoho Expense, optionally keeping or removing its attached receipt. |
| Delete Expense Category | `deleteExpenseCategory` | Delete an expense category from a Zoho Expense organization. |
| Delete Expense Report | `deleteExpenseReport` | Delete a single expense report from Zoho Expense. The expenses it contained return to the unreported state. |
| Delete Expenses In Bulk | `deleteExpensesInBulk` | Delete several Zoho Expense expenses at once by passing a comma separated list of expense IDs. |
| Delete Project | `deleteProject` | Delete a project from a Zoho Expense organization. |
| Delete Reporting Tag | `deleteReportingTag` | Delete a reporting tag from a Zoho Expense organization. |
| Delete Tax | `deleteTax` | Delete a tax rate from a Zoho Expense organization. |
| Delete Trip | `deleteTrip` | Delete a travel request (trip) from Zoho Expense. |
| Delete User | `deleteUser` | Remove a user from a Zoho Expense organization. |
| Get Currency | `getCurrency` | Retrieve the details of a single currency configured in Zoho Expense. |
| Get Customer | `getCustomer` | Retrieve the full details of a single customer in Zoho Expense, including addresses and contact persons. |
| Get Employee Advance | `getEmployeeAdvance` | Retrieve the full details of a single employee advance payment in Zoho Expense. |
| Get Expense | `getExpense` | Retrieve the full details of a single expense in Zoho Expense, including its line items and receipt metadata. |
| Get Expense Category | `getExpenseCategory` | Retrieve the details of a single expense category in Zoho Expense. |
| Get Expense Report | `getExpenseReport` | Retrieve the full details of a single Zoho Expense expense report, including the expenses it contains. |
| Get Expense Report Approval History | `getExpenseReportApprovalHistory` | Retrieve the approval history of a Zoho Expense expense report, showing each approval step and who actioned it. |
| Get Organization | `getOrganization` | Retrieve the settings and profile of a single Zoho Expense organization. |
| Get Project | `getProject` | Retrieve the full details of a single project in Zoho Expense, including the users assigned to it. |
| Get Tax | `getTax` | Retrieve the details of a single tax rate configured in Zoho Expense. |
| Get Tax Group | `getTaxGroup` | Retrieve the details of a tax group in Zoho Expense, including the individual taxes it combines. |
| Get Trip | `getTrip` | Retrieve the full details of a single Zoho Expense trip, including its itineraries. |
| Get User | `getUser` | Retrieve the profile and settings of a single user in a Zoho Expense organization. |
| Hide Expense Category | `hideExpenseCategory` | Hide an expense category in Zoho Expense so users can no longer book new expenses to it. |
| List Currencies | `listCurrencies` | Retrieve the currencies configured in a Zoho Expense organization. |
| List Customers | `listCustomers` | Retrieve the customers defined in a Zoho Expense organization. |
| List Employee Advances | `listEmployeeAdvances` | Retrieve employee advance payments in a Zoho Expense organization, with optional filtering by status, user, trip or project. |
| List Expense Categories | `listExpenseCategories` | Retrieve the expense categories defined in a Zoho Expense organization. Category IDs are used as the account ID on expense line items. |
| List Expense Reports | `listExpenseReports` | Retrieve expense reports in a Zoho Expense organization, optionally filtered by status or a free-text search and paginated. |
| List Expenses | `listExpenses` | Retrieve expenses in a Zoho Expense organization, optionally filtered by status, date range, category, merchant, customer or project. |
| List Organizations | `listOrganizations` | Retrieve all Zoho Expense organizations the connected user belongs to. Use the organization ID returned here for every other action in this connector. |
| List Projects | `listProjects` | Retrieve the projects defined in a Zoho Expense organization. |
| List Reporting Tag Options | `listReportingTagOptions` | Retrieve the selectable options belonging to a reporting tag in Zoho Expense. |
| List Reporting Tags | `listReportingTags` | Retrieve the reporting tags defined in a Zoho Expense organization. |
| List Taxes | `listTaxes` | Retrieve the tax rates configured in a Zoho Expense organization. |
| List Trips | `listTrips` | Retrieve travel requests (trips) in a Zoho Expense organization, optionally filtered by status and paginated. |
| List Users | `listUsers` | Retrieve the users belonging to a Zoho Expense organization. User IDs from this action are used as approver IDs elsewhere. |
| Recall Employee Advance | `recallEmployeeAdvance` | Recall a submitted employee advance request in Zoho Expense, returning it to draft so it can be edited. |
| Reimburse Expense Report | `reimburseExpenseReport` | Mark an approved Zoho Expense expense report as reimbursed, closing out the claim. |
| Reject Employee Advance | `rejectEmployeeAdvance` | Reject a submitted employee advance request in Zoho Expense, optionally recording the reason. |
| Reject Expense Report | `rejectExpenseReport` | Reject a submitted Zoho Expense expense report, optionally recording the reason for the rejection. |
| Reject Trip | `rejectTrip` | Reject a submitted travel request in Zoho Expense, optionally recording the reason. |
| Remove Expenses From Report | `removeExpensesFromReport` | Detach one or more expenses from a Zoho Expense expense report, returning them to the unreported state. |
| Show Expense Category | `showExpenseCategory` | Make an expense category visible to users in Zoho Expense so expenses can be booked to it. |
| Submit Employee Advance | `submitEmployeeAdvance` | Submit an employee advance request in Zoho Expense for approval by a named approver. |
| Submit Expense Report | `submitExpenseReport` | Submit a Zoho Expense expense report for approval to a named approver, optionally copying other users on the notification. |
| Update Currency | `updateCurrency` | Update the symbol, precision or display format of a currency in Zoho Expense. |
| Update Customer | `updateCustomer` | Update an existing customer in Zoho Expense. Only the fields supplied are sent. |
| Update Employee Advance | `updateEmployeeAdvance` | Update an existing employee advance payment in Zoho Expense. Only the fields supplied are sent. |
| Update Expense | `updateExpense` | Update an existing expense in Zoho Expense. Only the fields supplied are sent, so omitted fields keep their current values. |
| Update Expense Category | `updateExpenseCategory` | Update an existing expense category in Zoho Expense. Only the fields supplied are sent. |
| Update Expense Report | `updateExpenseReport` | Update an existing Zoho Expense expense report. Only the fields supplied are sent, so omitted fields keep their current values. |
| Update Project | `updateProject` | Update an existing project in Zoho Expense. Only the fields supplied are sent. |
| Update Reporting Tag | `updateReportingTag` | Update an existing reporting tag in Zoho Expense. Only the fields supplied are sent. |
| Update Tax | `updateTax` | Update an existing tax rate in Zoho Expense. Only the fields supplied are sent. |
| Update Trip | `updateTrip` | Update an existing Zoho Expense trip, including its itineraries. Only the fields supplied are sent. |
| Update User | `updateUser` | Update a user's profile, role or spending limits in a Zoho Expense organization. Only the fields supplied are sent. |
