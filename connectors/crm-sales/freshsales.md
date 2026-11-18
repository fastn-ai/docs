---
description: "Freshsales (Freshworks CRM) connector — contacts, sales accounts, deals, tasks, appointments, notes, sales activities, phone calls, products, CPQ documents,…"
hidden: true
---

# Freshsales

Freshsales (Freshworks CRM) connector — contacts, sales accounts, deals, tasks, appointments, notes, sales activities, phone calls, products, CPQ documents, files/links, marketing lists, selectors, custom fields, filters, search and lookup. Auth via per-user API key in the Authorization: Token token=&lt;key&gt; header.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [freshworks.com](https://freshworks.com) |
| **Authentication** | API key |
| **Actions** | 79 |
| **Events** | 0 |
| **Slug** | `freshsales` |

## Use it

Add Freshsales from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.freshsales.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Products To Deal | `addProductsToDeal` | Attach product line items to a deal. Each product needs product_id, quantity and price fields. |
| Bulk Assign Contact Owner | `bulkAssignContactOwner` | Assign a new owner to many contacts at once. |
| Bulk Delete Contacts | `bulkDeleteContacts` | Soft-delete many contacts by id in one call. |
| Bulk Delete Deals | `bulkDeleteDeals` | Soft-delete many deals by id. |
| Bulk Delete Sales Accounts | `bulkDeleteSalesAccounts` | Soft-delete many sales accounts by id. |
| Bulk Upsert Contacts | `bulkUpsertContacts` | Create/update many contacts in one async job. Returns a job id trackable via getJobStatus. |
| Bulk Upsert Deals | `bulkUpsertDeals` | Create/update many deals in one async job. |
| Bulk Upsert Sales Accounts | `bulkUpsertSalesAccounts` | Create/update many sales accounts in one async job. |
| Clone Contact | `cloneContact` | Clone an existing contact into a new record. |
| Clone Deal | `cloneDeal` | Clone an existing deal into a new record. |
| Clone Sales Account | `cloneSalesAccount` | Clone an existing sales account into a new record. |
| Create Appointment | `createAppointment` | Create an appointment. title, from_date, end_date and time_zone are required; link to a record via targetable_type/targetable_id. |
| Create Contact | `createContact` | Create a contact. Provide fields under the contact object. At least one identifying field (first_name/last_name/email/mobile_number) should be supplied. |
| Create Deal | `createDeal` | Create a deal. name is required; deal_pipeline_id and deal_stage_id set the pipeline stage (from listDealPipelines). |
| Create Document Link | `createDocumentLink` | Attach an external URL/link to a record (Contact/Deal/SalesAccount). |
| Create Note | `createNote` | Create a note attached to a record. description plus targetable_type (Contact/Deal/SalesAccount) and targetable_id are required. |
| Create Phone Call | `createPhoneCall` | Log a manual phone call against a record. Provide targetable_type/targetable_id, call_direction (incoming/outgoing) and an optional note. |
| Create Product | `createProduct` | Create a CPQ product. name and pricing (product_pricings) are required. |
| Create Sales Account | `createSalesAccount` | Create a sales account (company). name is required. |
| Create Task | `createTask` | Create a task. title, due_date (ISO 8601) and owner_id are required; link to a record via targetable_type (Contact/Deal/SalesAccount) and targetable_id. |
| Delete Appointment | `deleteAppointment` | Delete an appointment by id. |
| Delete Contact | `deleteContact` | Soft-delete a contact (moves to Recycle Bin). Use forgetContact to permanently erase. |
| Delete Note | `deleteNote` | Delete a note by id. |
| Delete Product | `deleteProduct` | Delete (soft) a CPQ product by id. |
| Delete Task | `deleteTask` | Delete a task by id. |
| Filtered Search | `filteredSearch` | Advanced filtered search for an entity. entity is the path segment (contact/deal/sales_account). Provide filter_rule with attribute/operator/value conditions. |
| Forget Contact | `forgetContact` | Permanently delete (forget) a contact and its data. Irreversible. |
| Forget Deal | `forgetDeal` | Permanently delete (forget) a deal. Irreversible. |
| Forget Sales Account | `forgetSalesAccount` | Permanently delete (forget) a sales account. Irreversible. |
| Get Appointment | `getAppointment` | Fetch a single appointment by id. |
| Get Contact | `getContact` | Fetch a single contact by id. Optionally sideload associations via include. |
| Get Contact Fields | `getContactFields` | List all contact fields (including custom fields) and their metadata. |
| Get Deal | `getDeal` | Fetch a single deal by id. Use include=products to sideload line items. |
| Get Deal Fields | `getDealFields` | List all deal fields including custom fields. |
| Get Job Status | `getJobStatus` | Track the status of an async bulk job by its id (returned by bulk_upsert/bulk_destroy). |
| Get Product | `getProduct` | Fetch a single CPQ product by id. |
| Get Sales Account | `getSalesAccount` | Fetch a single sales account by id. |
| Get Sales Account Fields | `getSalesAccountFields` | List all sales account fields including custom fields. |
| Get Sales Activity | `getSalesActivity` | Fetch a single sales activity by id. |
| Get Sales Activity Fields | `getSalesActivityFields` | List all sales activity fields. |
| Get Task | `getTask` | Fetch a single task by id. |
| List Business Types | `listBusinessTypes` | List business types (for sales accounts). |
| List Campaigns | `listCampaigns` | List campaigns. |
| List Contact Documents | `listContactDocuments` | List files and links associated with a contact. |
| List Contact Filters | `listContactFilters` | List saved contact views (filters). Use the returned filter id as view_id in listContacts. |
| List Contacts | `listContacts` | List contacts in a saved view. Pass the view_id (from listContactFilters). Supports pagination and sorting. |
| List Currencies | `listCurrencies` | List currencies configured in the account. |
| List Deal Filters | `listDealFilters` | List saved deal views (filters). |
| List Deal Payment Statuses | `listDealPaymentStatuses` | List deal payment statuses. |
| List Deal Pipelines | `listDealPipelines` | List deal pipelines and their stages. |
| List Deal Reasons | `listDealReasons` | List deal lost/won reasons. |
| List Deal Stages | `listDealStages` | List deal stages. |
| List Deal Types | `listDealTypes` | List deal types. |
| List Deals | `listDeals` | List deals in a saved view. Pass view_id from listDealFilters. |
| List Industry Types | `listIndustryTypes` | List industry types (for sales accounts). |
| List Lifecycle Stages | `listLifecycleStages` | List contact lifecycle stages. |
| List Owners | `listOwners` | List users (owners) who can be assigned records. |
| List Products | `listProducts` | List CPQ products in the catalog. |
| List Sales Account Filters | `listSalesAccountFilters` | List saved sales account views (filters). |
| List Sales Accounts | `listSalesAccounts` | List sales accounts (companies) in a saved view. Pass view_id from listSalesAccountFilters. |
| List Sales Activities | `listSalesActivities` | List sales activities (system-logged interactions: tasks, meetings, calls, emails). |
| List Sales Activity Entity Types | `listSalesActivityEntityTypes` | List sales activity entity types. |
| List Sales Activity Outcomes | `listSalesActivityOutcomes` | List sales activity outcomes. |
| List Sales Activity Types | `listSalesActivityTypes` | List sales activity types (Task, Meeting, Phone, Email, etc.). |
| List Tasks | `listTasks` | List tasks filtered by status. filter is one of open, due today, overdue, completed. include sideloads owner/targetable etc. |
| List Territories | `listTerritories` | List territories. |
| Lookup | `lookup` | Lookup records by a specific field value. q is the value, f the field (e.g. email), entities the entity type(s). |
| Restore Product | `restoreProduct` | Restore a previously deleted CPQ product. |
| Search | `search` | Global full-text search across entities. q is the query; include is a comma list of entity types (contact,sales_account,deal,user,cpq_product). |
| Update Appointment | `updateAppointment` | Update an appointment by id. |
| Update Contact | `updateContact` | Update a contact by id. Provide only the fields to change under the contact object. |
| Update Deal | `updateDeal` | Update a deal by id (e.g. move stage, change amount). |
| Update Note | `updateNote` | Update a note's description by id. |
| Update Product | `updateProduct` | Update a CPQ product by id. |
| Update Sales Account | `updateSalesAccount` | Update a sales account by id. |
| Update Task | `updateTask` | Update a task by id. Set status to 1 to mark complete. |
| Upsert Contact | `upsertContact` | Create or update a contact matched by a unique identifier (e.g. email). unique_identifier selects the match key; contact carries the attributes. |
| Upsert Deal | `upsertDeal` | Create or update a deal matched by a unique identifier. |
| Upsert Sales Account | `upsertSalesAccount` | Create or update a sales account matched by a unique identifier (e.g. name or external_id). |
