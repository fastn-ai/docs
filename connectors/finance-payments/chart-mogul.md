---
description: "ChartMogul is a subscription analytics and revenue reporting platform for SaaS businesses."
---

# ChartMogul

ChartMogul is a subscription analytics and revenue reporting platform for SaaS businesses. This connector covers the full ChartMogul REST API v1: account details, data sources, customers with custom attributes, tags, contacts and activities, plans and plan groups, invoices and invoice line items, transactions, subscriptions and subscription events, notes and call logs, opportunities, tasks, activities and activity exports, the Import API for pushing billing data, and all key metrics endpoints including MRR, ARR, ARPA, ASP, LTV, customer count and churn rates.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [chartmogul.com](https://chartmogul.com) |
| **Authentication** | Basic auth |
| **Actions** | 105 |
| **Events** | 1 |
| **Slug** | `chartMogul` |

## Use it

Add ChartMogul from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.chartMogul.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Contact to Customer | `addContactToCustomer` | Adds a contact person to an existing customer, identified by the customer's ChartMogul UUID. |
| Add Custom Attributes to Customer | `addCustomAttributesToCustomer` | Adds one or more custom attributes to a customer identified by its ChartMogul UUID. |
| Add Custom Attributes to Customers by Email | `addCustomAttributesToCustomersByEmail` | Adds custom attributes to every customer matching the given email address, across all data sources. |
| Add Custom Attributes to Subscription | `addCustomAttributesToSubscription` | Adds one or more custom attributes to a subscription. The Subscription UUID here is the uuid returned by List Customer Subscriptions prefixed with sub_ (for example sub_c4bb3592-...). The sub_ id returned inside an imported invoice's line items is a different identifier and is rejected by this endpoint. |
| Add Tags to Customer | `addTagsToCustomer` | Adds one or more tags to a customer identified by its ChartMogul UUID. |
| Add Tags to Customers by Email | `addTagsToCustomersByEmail` | Adds tags to every customer matching the given email address, across all data sources. |
| Connect Subscriptions | `connectSubscriptions` | Links two or more of a customer's subscriptions so ChartMogul treats the change between them as an upgrade or downgrade rather than a churn followed by new business. ChartMogul requires at least two distinct subscriptions, and at least one of them must already have the status Cancelled, otherwise it returns 422 at_least_one_subscription_must_be_canceled. |
| Create Activities Export | `createActivitiesExport` | Requests the creation of an activities export. The export is generated asynchronously, so save the returned export ID and poll Retrieve Activities Export until the download URL becomes available. |
| Create Contact | `createContact` | Creates a contact person against an existing ChartMogul customer. |
| Create Customer | `createCustomer` | Creates a customer in ChartMogul under the specified data source, optionally with tags, custom attributes and a primary contact. |
| Create Line Item | `createLineItem` | Adds a line item to an existing invoice identified by its ChartMogul UUID. |
| Create Line Item by External ID | `createLineItemByExternalId` | Adds a line item to an invoice identified by your own external invoice ID rather than its ChartMogul UUID. |
| Create Note or Call Log | `createNoteOrCallLog` | Creates a note or a call log against a customer in ChartMogul CRM. |
| Create Opportunity | `createOpportunity` | Creates a sales opportunity against a customer in ChartMogul CRM. |
| Create Plan | `createPlan` | Creates a subscription plan under a data source, defining its billing interval. |
| Create Plan Group | `createPlanGroup` | Creates a plan group that reports several subscription plans together as one product line. |
| Create Source | `createSource` | Creates a manual data source that billing data can be imported into through the ChartMogul Import API. |
| Create Subscription Event | `createSubscriptionEvent` | Records a subscription event such as a sign-up, plan change or cancellation, used to drive committed MRR reporting. |
| Create Task | `createTask` | Creates a task against a customer in ChartMogul CRM and assigns it to a team member. |
| Create Transaction | `createTransaction` | Records a payment or refund against an invoice identified by its ChartMogul UUID. |
| Create Transaction by External ID | `createTransactionByExternalId` | Records a payment or refund against an invoice identified by your own external invoice ID. |
| Delete All Customer Invoices | `deleteAllCustomerInvoices` | Permanently deletes every invoice a customer has in one data source. This cannot be undone. |
| Delete Contact | `deleteContact` | Permanently deletes a contact from ChartMogul. |
| Delete Customer | `deleteCustomer` | Permanently deletes a customer and all of its associated data from ChartMogul. This cannot be undone. |
| Delete Invoice | `deleteInvoice` | Permanently deletes an invoice along with its line items and transactions. |
| Delete Line Item | `deleteLineItem` | Permanently deletes an invoice line item. |
| Delete Note or Call Log | `deleteNoteOrCallLog` | Permanently deletes a note or call log. |
| Delete Opportunity | `deleteOpportunity` | Permanently deletes a sales opportunity. |
| Delete Plan | `deletePlan` | Permanently deletes a subscription plan. Plans with associated invoices or subscriptions cannot be deleted. |
| Delete Plan Group | `deletePlanGroup` | Deletes a plan group. The subscription plans it contained are not deleted. |
| Delete Source | `deleteSource` | Permanently deletes a data source and every customer, plan, invoice and subscription imported through it. This cannot be undone. |
| Delete Subscription Event | `deleteSubscriptionEvent` | Permanently deletes a subscription event, identified either by its ChartMogul ID or by data source UUID plus your external event ID. |
| Delete Task | `deleteTask` | Permanently deletes a CRM task. |
| Delete Transaction | `deleteTransaction` | Permanently deletes a payment or refund transaction. |
| Disable Invoice | `disableInvoice` | Disables or re-enables an invoice so that it is excluded from or included in ChartMogul metrics, without deleting it. This applies only to invoices from connected billing sources such as Stripe or Recurly; invoices in an Import API source return 422 "This operation is not allowed for this data source." Delete the invoice instead for Import API data. |
| Disable Line Item | `disableLineItem` | Disables or re-enables an invoice line item so that it is excluded from or included in ChartMogul metrics. This applies only to line items from connected billing sources such as Stripe or Recurly; line items in an Import API source return 422 "This operation is not allowed for this data source." Delete the line item instead for Import API data. |
| Disable Subscription Event | `disableSubscriptionEvent` | Disables or re-enables a subscription event so that it is excluded from or included in ChartMogul metrics. This applies only to events from connected billing sources such as Stripe or Recurly; events in an Import API source return 422 "This operation is not allowed for this data source." Delete the event instead for Import API data. |
| Disable Transaction | `disableTransaction` | Disables or re-enables a transaction so that it is excluded from or included in ChartMogul metrics. This applies only to transactions from connected billing sources such as Stripe or Recurly; transactions in an Import API source return 422 "This operation is not allowed for this data source." Delete the transaction instead for Import API data. |
| Disconnect Subscriptions | `disconnectSubscriptions` | Unlinks previously connected subscriptions so ChartMogul reports them independently again. |
| Get All Key Metrics | `getAllKeyMetrics` | Returns MRR, ARR, ARPA, ASP, customer count, customer churn rate and MRR churn rate over a date range, optionally segmented by plan, geography or tag. |
| Get ARR | `getArr` | Returns annual run rate over a date range. |
| Get Average Revenue Per Account | `getArpa` | Returns average revenue per account (ARPA) over a date range. |
| Get Average Sale Price | `getAsp` | Returns the average sale price (ASP) of new subscriptions over a date range. |
| Get Customer Churn Rate | `getCustomerChurnRate` | Returns the customer churn rate over a date range. |
| Get Customer Count | `getCustomerCount` | Returns the number of active paying customers over a date range. |
| Get LTV | `getLtv` | Returns customer lifetime value (LTV) over a date range. |
| Get MRR | `getMrr` | Returns monthly recurring revenue over a date range, broken down into new business, expansion, contraction, churn and reactivation movements. |
| Get MRR Churn Rate | `getMrrChurnRate` | Returns the net MRR churn rate over a date range. |
| Import CSV into Source | `importCsvIntoSource` | Uploads a UTF-8 encoded CSV file of customers, contacts, plans, invoices, line items, transactions or subscription events into a data source. ChartMogul requires multipart/form-data with a real file part, and CSV column headers must use the spaced names ChartMogul documents (for example "external id", not "external_id"). Note: the fastn HTTP executor always sends a JSON body, so this endpoint currently returns 500 when called through the connector; upload the CSV directly to ChartMogul until multipart file uploads are supported. |
| Import Data in Bulk | `importDataInBulk` | Imports or updates many ChartMogul objects in a single request. Supply any combination of customers, plans, invoices, line items, transactions, subscription events, contacts, notes, tasks, opportunities, tags and custom attributes. The import runs asynchronously; track it with Track Import Status using the external ID supplied here. |
| Import Invoices | `importInvoices` | Imports one or more invoices against a customer identified by ChartMogul UUID. Each invoice carries its line items and, optionally, its payment and refund transactions. |
| Import Invoices by External ID | `importInvoicesByExternalId` | Imports invoices identifying the customer by your own external ID rather than the ChartMogul customer UUID. |
| List Activities | `listActivities` | Returns a cursor-paginated list of MRR movement activities, optionally filtered by date range and movement type. |
| List Contacts | `listContacts` | Returns a cursor-paginated list of contacts, optionally filtered by customer, data source or email. |
| List Customer Activities | `listCustomerActivities` | Returns the MRR movement activities recorded for a single customer. |
| List Customer Invoices | `listCustomerInvoices` | Returns the invoices imported against a single customer, with their line items and transactions. |
| List Customer Subscriptions | `listCustomerSubscriptions` | Returns the subscriptions belonging to a single customer. |
| List Customers | `listCustomers` | Returns a cursor-paginated list of customers, optionally filtered by data source, external ID, email, status or billing system. |
| List Customers by Email | `listCustomersByEmail` | Searches for customers by email address across all data sources. |
| List Invoices | `listInvoices` | Returns a cursor-paginated list of invoices across the account, optionally filtered by customer, data source, external ID or validation status. |
| List Notes and Call Logs | `listNotesAndCallLogs` | Returns a cursor-paginated list of notes and call logs, optionally filtered by customer or type. |
| List Opportunities | `listOpportunities` | Returns a cursor-paginated list of sales opportunities, optionally filtered by customer, owner, pipeline and estimated close date. Note that ChartMogul ignores forecast_category and type as query filters, so they are not exposed here; filter on those fields in your own code after fetching. Pipeline Stage is only honoured when Pipeline is supplied alongside it. |
| List Plan Groups | `listPlanGroups` | Returns a cursor-paginated list of plan groups on the account. |
| List Plans | `listPlans` | Returns a cursor-paginated list of subscription plans, optionally filtered by data source, external ID or system. |
| List Plans in Plan Group | `listPlansInPlanGroup` | Returns the subscription plans that belong to a plan group. |
| List Sources | `listSources` | Returns the data sources configured on the ChartMogul account, optionally filtered by name or billing system. |
| List Subscription Events | `listSubscriptionEvents` | Returns a paginated list of subscription events, optionally filtered by data source, customer, subscription, event type or date. |
| List Tasks | `listTasks` | Returns a cursor-paginated list of CRM tasks, optionally filtered by customer, assignee, due date or completion state. |
| Merge Contacts | `mergeContacts` | Merges one contact into another. The source contact is removed and its details are folded into the destination contact. |
| Merge Customers | `mergeCustomers` | Merges one customer into another so their subscriptions and revenue are reported as a single customer. Identify each side by ChartMogul UUID, or by data source UUID plus your external ID. |
| Ping | `ping` | Verifies that the API key is valid and reports whether it grants read-only or read and write access. Useful as a connection health check. |
| Remove Custom Attributes from Customer | `removeCustomAttributesFromCustomer` | Removes the named custom attributes from a customer. |
| Remove Custom Attributes from Subscription | `removeCustomAttributesFromSubscription` | Removes the named custom attributes from a subscription. The Subscription UUID here is the uuid returned by List Customer Subscriptions prefixed with sub_ (for example sub_c4bb3592-...). The sub_ id returned inside an imported invoice's line items is a different identifier and is rejected by this endpoint. |
| Remove Tags from Customer | `removeTagsFromCustomer` | Removes the named tags from a customer. |
| Retrieve Account | `retrieveAccount` | Retrieves details of the ChartMogul account the API key belongs to, including the account name, currency and time zone. |
| Retrieve Activities Export | `retrieveActivitiesExport` | Retrieves the status of a previously requested activities export, returning the download URL once the export has finished generating. |
| Retrieve Contact | `retrieveContact` | Retrieves a single contact by its ChartMogul UUID. |
| Retrieve Customer | `retrieveCustomer` | Retrieves a single customer by its ChartMogul UUID, including MRR, ARR, status and attributes. |
| Retrieve Customer Tags and Attributes | `retrieveCustomerAttributes` | Returns all tags, custom attributes and Clearbit enrichment data stored against a customer. |
| Retrieve Invoice | `retrieveInvoice` | Retrieves a single invoice by its ChartMogul UUID, including its line items and transactions. |
| Retrieve Line Item | `retrieveLineItem` | Retrieves a single invoice line item by its ChartMogul UUID. |
| Retrieve Note or Call Log | `retrieveNoteOrCallLog` | Retrieves a single note or call log by its ChartMogul UUID. |
| Retrieve Opportunity | `retrieveOpportunity` | Retrieves a single sales opportunity by its ChartMogul UUID. |
| Retrieve Plan | `retrievePlan` | Retrieves a single subscription plan by its ChartMogul UUID. |
| Retrieve Plan Group | `retrievePlanGroup` | Retrieves a single plan group by its ChartMogul UUID. |
| Retrieve Source | `retrieveSource` | Retrieves a single data source by its ChartMogul UUID. |
| Retrieve Subscription Custom Attributes | `retrieveSubscriptionAttributes` | Returns the custom attributes stored against a subscription. The Subscription UUID here is the uuid returned by List Customer Subscriptions prefixed with sub_ (for example sub_c4bb3592-...). The sub_ id returned inside an imported invoice's line items is a different identifier and is rejected by this endpoint. |
| Retrieve Task | `retrieveTask` | Retrieves a single CRM task by its ChartMogul UUID. |
| Retrieve Transaction | `retrieveTransaction` | Retrieves a single payment or refund transaction by its ChartMogul UUID. |
| Track Import Status | `trackImportStatus` | Returns the progress and any errors of a bulk import previously submitted with Import Data in Bulk. |
| Unmerge Customers | `unmergeCustomers` | Separates a previously merged customer record back out of the merged customer it was folded into. |
| Update Contact | `updateContact` | Updates the supplied fields on an existing contact. Fields that are not sent are left unchanged. |
| Update Customer | `updateCustomer` | Updates the supplied fields on an existing customer. Fields that are not sent are left unchanged. Note that attributes.custom can only change custom attributes that already exist on the customer; use Add Custom Attributes to Customer to create new ones, or ChartMogul returns 422 only_existing_attributes. |
| Update Customer Custom Attributes | `updateCustomerCustomAttributes` | Updates the values of existing custom attributes on a customer. |
| Update Invoice | `updateInvoice` | Updates the supplied fields on an existing invoice. Fields that are not sent are left unchanged. |
| Update Invoice Status | `updateInvoiceStatus` | Voids or writes off an invoice, identified by data source UUID and your external invoice ID. Only voided and written_off are accepted; paid status is derived by ChartMogul from the invoice's transactions. |
| Update Line Item | `updateLineItem` | Updates the supplied fields on an existing invoice line item. Fields that are not sent are left unchanged. |
| Update Note or Call Log | `updateNoteOrCallLog` | Updates the supplied fields on an existing note or call log. |
| Update Opportunity | `updateOpportunity` | Updates the supplied fields on an existing sales opportunity, for example to advance it to a new pipeline stage. |
| Update Plan | `updatePlan` | Updates the supplied fields on an existing subscription plan. Fields that are not sent are left unchanged. |
| Update Plan Group | `updatePlanGroup` | Updates the name or plan membership of an existing plan group. |
| Update Subscription Custom Attributes | `updateSubscriptionCustomAttributes` | Updates the values of existing custom attributes on a subscription. The Subscription UUID here is the uuid returned by List Customer Subscriptions prefixed with sub_ (for example sub_c4bb3592-...). The sub_ id returned inside an imported invoice's line items is a different identifier and is rejected by this endpoint. |
| Update Subscription Event | `updateSubscriptionEvent` | Updates a subscription event, identified either by its ChartMogul ID or by data source UUID plus your external event ID. |
| Update Task | `updateTask` | Updates the supplied fields on an existing CRM task, for example to reassign it or mark it complete. |
| Update Transaction | `updateTransaction` | Updates the supplied fields on an existing payment or refund transaction. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| MRR Movement | `mrr_movement` | Fires whenever ChartMogul records a real-time customer-level MRR movement - new business, churn, expansion, contraction or reactivation. The specific movement is in the payload's movement_type field. SETUP (required, once per ChartMogul account): in ChartMogul go to Settings &gt; Destinations, click ADD DESTINATION, choose Webhook, enter a Name, paste this trigger's fastn URL into the URL field, optionally tick 'Include custom attributes in webhook payload', then click SAVE. ChartMogul delivers nothing until that destination is saved. Note that ChartMogul does NOT fire this event for MRR changes caused by historical edits, customer merges, App Store Connect or Google Play integrations, or changes that do not alter the MRR amount. Failed deliveries (any non-2xx response) are retried up to 17 times. |
