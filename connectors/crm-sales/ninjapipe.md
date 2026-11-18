---
description: "NinjaPipe is an all-in-one CRM for small businesses."
hidden: true
---

# NinjaPipe

<img src="../../.gitbook/assets/connectors/lg/ninjapipe.png" alt="NinjaPipe logo">

NinjaPipe is an all-in-one CRM for small businesses. This connector wraps the NinjaPipe REST API to manage contacts and contact activities, client portal access, deals, products, projects and tasks, general tasks, orders, budgets and expenses, lists and list members, and workspace members.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [ninjapipe.com](https://ninjapipe.com) |
| **Authentication** | Bearer token |
| **Slug** | `ninjapipe` |

## Use it

Add NinjaPipe from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ninjapipe.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add To List | `addToList` | Adds a contact to a Contact-type NinjaPipe list or a company to a Company-type list. Pass exactly one of contact_id or company_id. |
| Create Budget | `createBudget` | Creates a budget in NinjaPipe with an allocated amount, category, period and date range. |
| Create Budget Expense | `createBudgetExpense` | Records an expense against a NinjaPipe budget. |
| Create Contact | `createContact` | Creates a contact in NinjaPipe with optional owner, assignee, company and custom fields such as address, social profiles and contact preferences. |
| Create Contact Activity | `createContactActivity` | Adds a note or a task activity to a NinjaPipe contact timeline. A task activity also creates a linked task in a per-contact project named "Tasks for &lt;contact name&gt;", which NinjaPipe creates automatically if it does not exist. |
| Create Deal | `createDeal` | Creates a deal in NinjaPipe, optionally linked to a contact or company. The owner defaults to the API key owner. |
| Create General Task | `createGeneralTask` | Creates a NinjaPipe general task (not tied to a project), or a subtask when parent_id is set. |
| Create List | `createList` | Creates a contact or company list in NinjaPipe. |
| Create Order | `createOrder` | Creates an order in NinjaPipe for a customer, optionally linked to a contact, with totals, status, payment status, dates and line items. |
| Create Product | `createProduct` | Creates a product or service in the NinjaPipe catalog. The SKU must be unique within the workspace. |
| Create Project | `createProject` | Creates a project in NinjaPipe with status, priority, due date, team, tags and optional metadata such as a linked contact. |
| Create Project Task | `createProjectTask` | Creates a task, or a subtask when parent_id is set, inside a NinjaPipe project. |
| Delete Budget | `deleteBudget` | Deletes a NinjaPipe budget by its ID. |
| Delete Budget Expense | `deleteBudgetExpense` | Deletes an expense from a NinjaPipe budget. |
| Delete Contact | `deleteContact` | Deletes a NinjaPipe contact by its ID. |
| Delete Contact Activity | `deleteContactActivity` | Deletes an activity from a NinjaPipe contact timeline. |
| Delete Deal | `deleteDeal` | Deletes a NinjaPipe deal by its ID. |
| Delete General Task | `deleteGeneralTask` | Deletes a NinjaPipe general task by its ID. |
| Delete List | `deleteList` | Deletes a NinjaPipe list by its ID. |
| Delete Order | `deleteOrder` | Deletes a NinjaPipe order by its ID. |
| Delete Product | `deleteProduct` | Deletes a NinjaPipe product by its ID. |
| Delete Project | `deleteProject` | Deletes a NinjaPipe project by its ID. |
| Delete Project Task | `deleteProjectTask` | Deletes a task from a NinjaPipe project. |
| Disable Client Portal | `disableClientPortal` | Disables the client portal account of a NinjaPipe contact so it can no longer sign in. |
| Enable Client Portal | `enableClientPortal` | Creates or re-enables a client portal account for a NinjaPipe contact, using the contact email unless another is given and auto-generating a password unless one is supplied. |
| Get Budget | `getBudget` | Retrieves a single NinjaPipe budget by its ID, including spent and remaining amounts. |
| Get Budget Expense | `getBudgetExpense` | Retrieves a single expense of a NinjaPipe budget. |
| Get Contact | `getContact` | Retrieves a single NinjaPipe contact by its ID, including custom fields. |
| Get Contact Activity | `getContactActivity` | Retrieves one activity from a NinjaPipe contact timeline. The activity must belong to the contact. |
| Get Deal | `getDeal` | Retrieves a single NinjaPipe deal by its ID. |
| Get General Task | `getGeneralTask` | Retrieves a single NinjaPipe general task by its ID. |
| Get List | `getList` | Retrieves a single NinjaPipe list by its ID. |
| Get Order | `getOrder` | Retrieves a single NinjaPipe order by its ID. |
| Get Product | `getProduct` | Retrieves a single NinjaPipe product by its ID. |
| Get Project | `getProject` | Retrieves a single NinjaPipe project by its ID. |
| Get Project Task | `getProjectTask` | Retrieves a single task within a NinjaPipe project. |
| List Budget Expenses | `listBudgetExpenses` | Lists the expenses recorded against a NinjaPipe budget with pagination, search, category filter and sorting. As of 2026-09-15 NinjaPipe returns HTTP 500 "Internal server error" for this documented route on existing budgets (single expenses can still be read with Get Budget Expense). |
| List Budgets | `listBudgets` | Lists NinjaPipe budgets with pagination, search, filters by status, category and period, and sorting. |
| List Contact Activities | `listContactActivities` | Lists the timeline activities (notes and task-linked activities) of a NinjaPipe contact, optionally filtered by type. |
| List Contacts | `listContacts` | Lists NinjaPipe contacts with pagination, search across name, email and phone, filters by status, owner or assignee, and sorting. |
| List Deals | `listDeals` | Lists NinjaPipe deals with pagination, name search, status and owner filters, and sorting. Note that NinjaPipe reports pagination.total as the unfiltered deal count even when filters narrow the data array. |
| List General Tasks | `listGeneralTasks` | Lists NinjaPipe general tasks that are not tied to a project, filterable by status, priority and parent task. |
| List List Members | `listListMembers` | Lists the contacts or companies in a NinjaPipe list, optionally expanding member details. |
| List Lists | `listLists` | Lists NinjaPipe contact and company lists with pagination, search, type and status filters, and sorting. |
| List Orders | `listOrders` | Lists NinjaPipe orders with pagination, search across order number and customer details, status and payment status filters, and sorting. |
| List Products | `listProducts` | Lists NinjaPipe products with pagination, search by name, description or SKU, filters by status, category and type, and sorting. |
| List Project Tasks | `listProjectTasks` | Lists the tasks of a NinjaPipe project, filterable by status, priority and parent task, and sortable by order or date. |
| List Projects | `listProjects` | Lists NinjaPipe projects with pagination, search, status and priority filters, and sorting. |
| List Workspace Members | `listWorkspaceMembers` | Lists the team members of the NinjaPipe workspace tied to the API key. Use the returned account IDs as owner_id, assigned_to or assignee_id values. |
| Remove List Member | `removeListMember` | Removes a member from a NinjaPipe list. The contact or company itself is not deleted. |
| Reorder General Tasks | `reorderGeneralTasks` | Batch-updates the order index of sibling NinjaPipe general tasks, up to 500 updates per request. |
| Reorder Project Tasks | `reorderProjectTasks` | Batch-updates the order index of sibling tasks within a NinjaPipe project. |
| Update Budget | `updateBudget` | Updates a NinjaPipe budget. Only the fields you pass are changed. |
| Update Budget Expense | `updateBudgetExpense` | Updates an expense of a NinjaPipe budget. Only the fields you pass are changed. |
| Update Contact | `updateContact` | Updates a NinjaPipe contact. Only the top-level fields you pass are changed, but a fields object replaces all existing custom fields, so send the complete set. Pass assigned_to as null to unassign. |
| Update Contact Activity | `updateContactActivity` | Partially updates a note or task-linked activity on a NinjaPipe contact; for task activities the linked task is updated too. |
| Update Deal | `updateDeal` | Updates a NinjaPipe deal's name, value, status, owner, linked contact or company, or custom fields. Only the fields you pass are changed, but a fields object replaces the existing custom fields. Priority, description and expected close date listed in the NinjaPipe reference are not stored by the API; keep them in custom fields instead. |
| Update General Task | `updateGeneralTask` | Updates a NinjaPipe general task. Setting parent_id to a descendant returns a TASK_PARENT_CYCLE conflict. |
| Update List | `updateList` | Updates a NinjaPipe list. The list type cannot be changed while the list has members. |
| Update List Member | `updateListMember` | Updates a member of a NinjaPipe list, such as flagging it as important. |
| Update Order | `updateOrder` | Updates a NinjaPipe order, such as its status, payment status, tracking number or line items. Only the fields you pass are changed. |
| Update Product | `updateProduct` | Updates a NinjaPipe product. Only the fields you pass are changed. |
| Update Project | `updateProject` | Updates a NinjaPipe project. All fields are optional; pass due_date as null to clear it. |
| Update Project Task | `updateProjectTask` | Updates a task within a NinjaPipe project. Setting parent_id to a descendant returns a TASK_PARENT_CYCLE conflict. |
