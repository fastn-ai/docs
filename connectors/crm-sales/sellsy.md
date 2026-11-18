---
description: "Sellsy CRM, invoicing and sales platform via the Sellsy API v2."
hidden: true
---

# Sellsy

<img src="../../.gitbook/assets/connectors/lg/sellsy.png" alt="Sellsy logo">

Sellsy CRM, invoicing and sales platform via the Sellsy API v2. Manage companies, contacts, individuals, opportunities, estimates, orders, invoices, credit notes, payments, items, tasks, calendar events, comments, custom fields, files, staff and webhooks.

| | |
| --- | --- |
| **Category** | [CRM and sales](README.md) |
| **Website** | [sellsy.com](https://sellsy.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `sellsy` |

## Use it

Add Sellsy from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.sellsy.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate invoice conformity (Definitively) | `activateInvoicingConformity` | Definitively activate invoice conformity for the account. This change is irreversible. |
| Add payment installment for a subscription | `addSubscriptionPaymentInstallments` | Add a number of payment installments to an existing subscription. |
| Attach file to a company | `uploadCompanyFile` | Attaches a file to a company (open beta route; multipart upload). |
| Attach file to a contact | `uploadContactFile` | Attach file to a contact. |
| Attach file to a credit note | `uploadCreditNoteFile` | Attach file to a credit note. |
| Attach file to a deposit invoice | `uploadDepositInvoiceFile` | Attach file to a deposit invoice. |
| Attach file to a directory | `uploadDirectoryFile` | Attach file to a directory. |
| Attach file to an estimate | `uploadEstimateFile` | Attach a file to an estimate (open beta route). |
| Attach file to an individual | `uploadIndividualFile` | Attach file to an individual. |
| Attach file to an invoice | `uploadInvoiceFile` | Attach file to an invoice. |
| Attach file to an opportunity | `uploadOpportunityFile` | Attach file to an opportunity. |
| Attach file to an order | `uploadOrderFile` | Attach file to an order. |
| Batch request | `createBatch` | Run several API calls in one batch request. The body is newline-delimited JSON: a header line {uri, method, query, uuid} followed by a payload line, repeated. |
| Calendar events List | `getCalendarEvents` | Get a list of calendar events. |
| Cancel esign for estimate | `cancelEsignEstimate` | Cancel the electronic signature request of an estimate. |
| Cancel esign for order | `cancelEsignOrder` | Cancel electronic signature for order. |
| Cancel esign for proposal document | `cancelEsignProposalDocument` | Cancel electronic signature for proposal document. |
| Comments List | `getComments` | Get a list of comments. |
| Companies contact | `getContactCompanies` | Get the companies of a contact. |
| Companies List | `getCompanies` | Get a list of companies. |
| Company custom fields List | `getCompanyCustomFields` | Get list of custom fields for a company. |
| Company smart tags List | `getCompanySmartTags` | Get list of smart tags for a company. |
| Compute a credit note | `computeCreditNote` | Compute the totals of a credit note without saving it. |
| Compute a deposit invoice | `computeDepositInvoice` | Compute the totals of a deposit invoice without saving it. |
| Compute a progress invoice | `computeProgressInvoice` | Compute progress invoice rows and totals without saving. |
| Compute an estimate | `computeEstimate` | Compute the totals of an estimate without saving it. |
| Compute an invoice | `computeInvoice` | Compute the totals of an invoice without saving it. |
| Compute an order | `computeOrder` | Compute the totals of an order without saving it. |
| Contact custom fields List | `getContactCustomFields` | Get list of custom fields for a contact. |
| Contact smart tags List | `getContactSmartTags` | Get list of smart tags for a contact. |
| Contacts List | `getContacts` | Get a list of contacts. |
| Convert a document model into a document | `convertModel` | Build the request body expected by a document create endpoint, prefilled from the document model. Does not create the document. |
| Convert prospect company to client company | `convertCompany` | Convert prospect company to client company. |
| Convert prospect individual to client individual | `convertIndividual` | Convert prospect individual to client individual. |
| Create a calendar event | `createCalendarEvent` | Create a calendar event. External participants may receive invitations from a synced provider calendar. |
| Create a comment | `createComment` | Create a comment. |
| Create a company | `createCompany` | Create a company. |
| Create a company address | `createCompanyAddress` | Create a company address. |
| Create a contact | `createContact` | Create a contact. |
| Create a contact address | `createContactAddress` | Create a contact address. |
| Create a deposit invoice | `createDepositInvoice` | Create a draft deposit invoice from an estimate or order. Creating does not send it to the client. |
| Create a deposit invoice quickly | `quickCreateDepositInvoice` | Create a draft deposit invoice for a percentage of the parent document. Creating does not send it to the client. |
| Create a discount including taxes | `createDiscountInclTaxes` | Create a discount including taxes. |
| Create a document model | `createModel` | Create a document model (template). |
| Create a phonecall | `createPhoneCall` | Log a phone call. |
| Create a Progress invoice | `createProgressInvoice` | Create a progress invoice linked to a parent document. Creating does not send it to the client unless validation options request it. |
| Create a staff | `createStaff` | Create a staff member; Sellsy sends an invitation email to the new staff. |
| Create a subscription | `createSubscription` | Create a recurring-invoice subscription. Generated invoices may be emailed to the client according to the sending configuration. |
| Create a task | `createTask` | Create a task. |
| Create an accounting code | `createAccountingCode` | Create an accounting code. |
| Create an individual | `createIndividual` | Create an individual. |
| Create an individual address | `createIndividualAddress` | Create an individual address. |
| Create an item | `createItem` | Create an item (product or service). |
| Create an opportunity | `createOpportunity` | Create an opportunity. |
| Create an order | `createOrder` | Create an order. |
| Create credit note | `createCreditNote` | Create a draft credit note. Creating does not send it to the client. |
| Create Custom Activity | `createCustomActivity` | Create a custom activity. |
| Create Custom Activity Type | `createCustomActivityType` | Create a custom activity type. |
| Create directory | `createDirectory` | Create a new directory and attach it to the provided parent entity. |
| Create esign for estimate | `createEsignEstimate` | Create an electronic signature request for an estimate; sends signature requests to the listed people. The signature must be displayed on the document. |
| Create esign for order | `createEsignOrder` | Create an electronic signature request for an order; sends signature requests to the listed people. The signature must be displayed on the document. |
| Create esign for proposal document | `createEsignProposalDocument` | Create an electronic signature request for a proposal document; sends signature requests to the listed people. The document needs a signature block. |
| Create estimate | `createEstimate` | Creates an estimate (open beta route). Creating does not send it to the client. |
| Create invoice | `createInvoice` | Create a draft invoice. Creating does not send it to the client. |
| Create rate category | `createRateCategory` | Create a rate category. |
| Create tax | `createTax` | Create a tax. Due to e-invoicing regulations, tax creation with rate 0 is no longer allowed; use exempted tax types instead. |
| Create Webhook | `createWebhook` | Create a webhook. |
| Credit note custom fields List | `getCreditNoteCustomFields` | Get list of custom fields for a credit note. |
| Credit note payments list | `getCreditNotePayments` | Get list of payments for a credit note. |
| Credit note smart-tags list | `getCreditNoteSmartTags` | Get list of smart-tags for a credit note. |
| Credit notes List | `getCreditNotes` | Get a list of credit notes. |
| Custom Activity Types List | `getCustomActivityTypes` | Get a list of custom activity types. |
| Custom Fields List | `getCustomFields` | Get a list of custom fields. |
| Custom Fields Search | `searchCustomFields` | Search custom fields. |
| Customs Activities List | `getCustomActivities` | Get a list of custom activities. |
| Declinations List | `getItemDeclinations` | Get the declinations (variants) of an item. |
| Delete a comment | `deleteComment` | Remove a comment. |
| Delete a company address | `deleteCompanyAddress` | Delete a company address. |
| Delete a contact address | `deleteContactAddress` | Delete a contact address. |
| Delete a discount including taxes | `deleteDiscountInclTaxes` | Delete a discount including taxes. |
| Delete a payment installment for a subscription | `deleteSubscriptionPaymentInstallment` | Deletes a single pending payment installment. Only payment installments that have not yet generated an invoice can be deleted. |
| Delete a phoneCall | `deletePhoneCall` | Delete a phone call. |
| Delete a smart tags | `deleteSmartTags` | Deletes a smart tag and removes it from every object it was linked to. |
| Delete a subscription | `deleteSubscription` | Delete a subscription and all future payment installments. |
| Delete a task | `deleteTask` | Delete a task. |
| Delete an accounting code | `deleteAccountingCode` | Delete an accounting code. |
| Delete an individual address | `deleteIndividualAddress` | Delete an individual address. |
| Delete an Opportunity | `deleteOpportunity` | Delete an opportunity. |
| Delete calendar event | `deleteCalendarEvent` | Delete calendar event. |
| Delete company | `deleteCompany` | Remove a company. |
| Delete contact | `deleteContact` | Remove a contact. |
| Delete Custom Activity | `deleteCustomActivity` | Delete a custom activity. |
| Delete document model | `deleteModel` | Delete a document model. |
| Delete file | `deleteFile` | Delete a file. |
| Delete Individual | `deleteIndividual` | Remove an individual. |
| Delete item | `deleteItem` | Delete an item. |
| Delete licenses | `deleteStaffLicenses` | Remove all licenses from a staff member. |
| Delete notification | `deleteNotification` | Delete a notification. |
| Delete OAuth client | `deleteClient` | Delete an OAuth 2 client for the API. Deleting the client used by the connection revokes its access. |
| Delete payment | `deletePayment` | Delete a payment that is not linked to a document. |
| Delete Rate category | `deleteRateCategory` | Remove a rate category. |
| Delete tax | `deleteTax` | Remove a tax. |
| Delete the directory and all items attached | `deleteDirectory` | Delete the directory and all items attached. |
| Delete Webhook | `deleteWebhook` | Delete a webhook. |
| Deposit payments list | `getDepositInvoicePayments` | Get list of payments for a deposit invoice. |
| Estimate custom fields List | `getEstimateCustomFields` | Get list of custom fields for an Estimate. |
| Estimate payments list | `getEstimatePayments` | Get list of payments for an estimate (open beta route). |
| Estimate smart-tags list | `getEstimateSmartTags` | Get list of smart-tags for an estimate. |
| Export accounting journal | `exportAccountingJournal` | Export list of accounting journal entries. |
| Export companies | `exportCompanies` | Starts an asynchronous export of companies. |
| Export contacts | `exportContacts` | Starts an asynchronous export of contacts. |
| Export estimates | `exportEstimates` | Starts an asynchronous export of estimates. |
| Export invoices | `exportInvoices` | Starts an asynchronous export of invoices. |
| Export opportunities | `exportOpportunities` | Starts an asynchronous export of opportunities. |
| Export the CRM activity | `exportCrmActivities` | Export the CRM activity feed as a file. |
| Export the exports list | `exportExports` | Export the list of exports for the current user, ordered by creation date. |
| Fetch list of subscriptions | `getSubscriptions` | Fetch list of subscriptions. |
| Generate a proposal document | `generateProposalDocument` | Generate a proposal document from a proposal model. Does not send it to anyone. |
| Get a company address | `getCompanyAddress` | Get a company address. |
| Get a company contacts | `getCompanyContacts` | Get a company contacts. |
| Get a contact address | `getContactAddress` | Get a contact address. |
| Get a deposit invoice | `getDepositInvoice` | Get a deposit invoice. |
| Get a discount including taxes | `getDiscountInclTaxes` | Get a discount including taxes. |
| Get a payment | `getPayment` | Get a payment. |
| Get a phoneCall | `getPhoneCall` | Get a phone call. |
| Get a task | `getTask` | Get a task. |
| Get accounting charts settings | `getAccountingChartsSettings` | Get accounting charts settings. |
| Get accounting codes | `getAccountingCodes` | Get list of accounting codes. |
| Get accounting journal | `getAccountingJournal` | Get list of accounting journal entries. |
| Get all deliveries | `getDeliveries` | Get all Deliveries. |
| Get all document layouts | `getDocumentLayouts` | Get all document layouts. |
| Get all estimates | `getEstimates` | Get all estimates. |
| Get all orders | `getOrders` | Get all orders. |
| Get all payment installments of subscriptions | `getSubscriptionsPaymentInstallments` | Get all payment installments of subscriptions. |
| Get an estimate | `getEstimate` | Get an estimate. |
| Get an export status | `getListingExport` | Get the current status of the export by its Identifier. |
| Get an individual address | `getIndividualAddress` | Get an individual address. |
| Get an individual contacts | `getIndividualContacts` | Get the contacts of an individual. |
| Get an item | `getItem` | Get an item. |
| Get available tags for document models | `getModelTags` | Get the variable tags that can be used in a document model and are replaced when a concrete document is computed. |
| Get available tags for email signature settings | `getEmailSignatureTags` | Get available tags for email signature settings. |
| Get available tags for email templates | `getEmailTemplateTags` | Get the variable tags that can be used in an email template subject and message. |
| Get calendar event | `getCalendarEvent` | Get calendar event. |
| Get calendar events labels | `getCalendarEventsLabels` | Get all calendar events labels available. |
| Get comment details | `getComment` | Fetch comment details. |
| Get Company | `getCompany` | Fetch company informations. |
| Get company addresses | `getCompanyAddresses` | Get company addresses. |
| Get contact | `getContact` | Fetch contact informations. |
| Get contact addresses | `getContactAddresses` | Get contact addresses. |
| Get countries list | `getCountries` | Get a list of countries. |
| Get credit note | `getCreditNote` | Get a credit note by ID. |
| Get credit notes linked to a deposit invoice | `getDepositInvoiceCreditNotes` | Get credit notes linked to a deposit invoice. |
| Get credit notes linked to invoice | `getInvoiceCreditNotes` | Get list of credit notes linked to an invoice. |
| Get currencies | `getCurrencies` | Get all currencies of the account. |
| Get Current Staff | `getCurrentStaff` | Returns the Sellsy staff member linked to the API access used by this connection. |
| Get Custom Activity | `getCustomActivity` | Fetch custom activity informations. |
| Get Custom Activity Type | `getCustomActivityType` | Get a custom activity type. |
| Get custom field | `getCustomField` | Fetch a custom field informations. |
| Get delivery | `getDelivery` | Get a delivery by ID. |
| Get deposit invoice custom fields | `getDepositInvoiceCustomFields` | Get list of custom fields for a deposit invoice. |
| Get directory | `getDirectory` | Fetch directory informations. |
| Get document model | `getModel` | Get a document model. |
| Get Email | `getEmail` | Get an email. |
| Get email settings | `getEmailSettings` | Get email settings. |
| Get email template | `getEmailTemplate` | Get the details of your email template. |
| Get email's domain DNS data | `getEmailDomainDnsData` | Get DNS data for the domain extracted from the email. |
| Get Emails Thread | `getEmailThread` | Get the emails list of a thread. |
| Get esign for estimate | `getEsignEstimate` | Get the electronic signature request of an estimate. |
| Get esign for order | `getEsignOrder` | Get electronic signature for order. |
| Get esign for proposal document | `getEsignProposalDocument` | Get electronic signature for proposal document. |
| Get file | `getFile` | Get a file. |
| Get fiscal years | `getFiscalYears` | Get list of fiscal years of account. |
| Get GoCardless mandates | `getMandates` | Get the GoCardless direct debit mandates of the account. |
| Get Individual | `getIndividual` | Fetch individual informations. |
| Get individual addresses | `getIndividualAddresses` | Get individual addresses. |
| Get invoice | `getInvoice` | Get an invoice by ID. |
| Get invoices linked to credit note | `getCreditNoteInvoices` | Get list of invoices linked to a credit note. |
| Get item declination prices | `getItemDeclinationPrices` | Get prices list for an item declination. |
| Get item prices | `getItemPrices` | Get prices list (per rate category) for an item. |
| Get list of discounts including taxes | `getDiscountsInclTaxes` | Get discounts including taxes list. |
| Get list of primes | `getPrimes` | Get primes list. |
| Get list of your email templates | `getEmailTemplates` | Get list of your email templates. |
| Get meta informations for accounting journal | `metaAccountingJournal` | Get meta informations for accounting journal. |
| Get meta informations for activity | `metaCrmActivities` | Get CRM activity metadata needed to build the form (filter labels, static values and so on). |
| Get Metadata for purchase invoice OCR | `getOcrPurInvoiceMetas` | Get metadata (permissions) for purchase invoice OCR. |
| Get my Sellsy subscription informations | `getAccountSubscription` | Retrieve the details of my Sellsy subscription. |
| Get Notifications settings | `getNotificationsSettings` | Get notifications settings. |
| Get OAuth client | `getClient` | Fetch an OAuth 2 client for the API. |
| Get Opportunities | `getOpportunities` | Get list of opportunities. |
| Get Opportunities Categories List | `getOpportunitiesCategories` | Get list of opportunities categories. |
| Get Opportunities Category | `getOpportunitiesCategory` | Get an opportunities category. |
| Get Opportunity | `getOpportunity` | Get an opportunity. |
| Get Opportunity Category Sources | `getOpportunityCategorySources` | Get list of opportunity sources of a source category. |
| Get Opportunity Pipeline Steps | `getOpportunityPipelineSteps` | Get list of opportunity pipeline steps. |
| Get Opportunity Pipelines | `getOpportunityPipelines` | Get list of opportunity pipelines. |
| Get Opportunity Sources | `getOpportunitySources` | Get list of opportunity sources. |
| Get order | `getOrder` | Get an order by ID. |
| Get payments | `getPayments` | Get a list of payments. |
| Get proposal document | `getProposalDocument` | Get a proposal document. |
| Get proposal model | `getProposalModel` | Get a proposal model. |
| Get Quotas | `getQuotas` | Get quotas of the account (API rate limits, marketing, custom fields and more). |
| Get rate category | `getRateCategory` | Fetch a rate category. |
| Get Scopes Tree | `getScopesTree` | Get tree of scopes. |
| Get smart tags for a deposit invoice | `getDepositInvoiceSmartTags` | Get smart tags for a deposit invoice. |
| Get Staff | `getStaff` | Get a staff member. |
| Get Staffs | `getStaffs` | Get a list of staffs. The response may contain only your own staff, depending on your subscription plan. |
| Get subscription | `getSubscription` | Get a subscription. |
| Get system email template with content | `getSystemEmailTemplateWithContent` | Render the system email template for a context (document, proposal, reminder). Does not send anything. |
| Get tasks labels | `getTasksLabels` | Get all tasks labels available. |
| Get Tax | `getTax` | Fetch tax informations. |
| Get the account languages | `getLanguages` | Get the account languages. |
| Get the CRM activity | `getCrmActivities` | Get the CRM activity feed. |
| Get the payment method | `getPaymentMethod` | Get a payment method by id. |
| Get timeline of a GoCardless directdebit | `getGocardlessDirectdebitTimeline` | Get timeline of a GoCardless directdebit. |
| Get Units | `getUnits` | Get all units of the account. |
| Get User Notifications | `getNotifications` | Get notifications related to current user. |
| Get Webhook | `getWebhook` | Get a webhook. |
| Get Webhooks | `getWebhooks` | Get list of webhooks. |
| Get your email template with context | `getEmailTemplateWithContent` | Render email content (subject and body) from a template and context objects. Does not send anything. |
| Get your invoices and credit notes | `getAccountsDocuments` | Get the Sellsy subscription invoices and credit notes of your account. |
| Individual custom fields List | `getIndividualCustomFields` | Get list of custom fields for an individual. |
| Individual smart tags List | `getIndividualSmartTags` | Get list of smart tags for an individual. |
| Individuals List | `getIndividuals` | Get a list of individuals. |
| Invoice custom fields List | `getInvoiceCustomFields` | Get list of custom fields for an invoice. |
| Invoice payments list | `getInvoicePayments` | Get list of payments for an invoice. |
| Invoice smart-tags list | `getInvoiceSmartTags` | Get list of smart-tags for an invoice. |
| Invoices List | `getInvoices` | Get a list of invoices. |
| Items List | `getItems` | Get a list of items (products and services). |
| Link a contact at one company | `linkCompanyContact` | Link a contact at one company. |
| Link a credit note to an invoice | `linkCreditNoteToInvoice` | Link a credit note to an invoice for a specific amount. |
| Link an invoice to a credit note | `linkInvoiceToCreditNote` | Link an invoice to a credit note for a specific amount. |
| Link discount including taxes to credit note | `linkCreditNoteDiscountInclTaxes` | Link a discount including taxes to a credit note. |
| Link discount including taxes to estimate | `linkEstimateDiscountInclTaxes` | Link a discount including taxes to an estimate. |
| Link discount including taxes to invoice | `linkInvoiceDiscountInclTaxes` | Link a discount including taxes to an invoice. |
| Link discount including taxes to order | `linkOrderDiscountInclTaxes` | Link a discount including taxes to an order. |
| Link payment to credit note | `linkCreditNotePayment` | Link a payment to a credit note. |
| Link payment to deposit invoice | `linkDepositInvoicePayment` | Link a payment to a deposit invoice. |
| Link payment to estimate | `linkEstimatePayment` | Link a payment to an estimate (open beta route). |
| Link payment to invoice | `linkInvoicePayment` | Link a payment to an invoice. |
| Link payment to order | `linkOrderPayment` | Link a payment to an order. |
| Link prime to credit note | `linkCreditNotePrime` | Link a prime to a credit note. |
| Link prime to estimate | `linkEstimatePrime` | Link a prime to an estimate. |
| Link prime to invoice | `linkInvoicePrime` | Link a prime to an invoice. |
| Link prime to order | `linkOrderPrime` | Link a prime to an order. |
| Link smart tags to an order | `linkOrderSmartTags` | Link a list of smart tag to an order. |
| Link smart tags to company | `linkCompanySmartTags` | Link a list of smart tag to a company. |
| Link smart tags to contact | `linkContactSmartTags` | Link a list of smart tag to a contact. |
| Link smart tags to credit note | `linkCreditNoteSmartTags` | Link a list of smart-tags to a credit note. |
| Link smart tags to deposit invoice | `linkDepositInvoiceSmartTags` | Link a list of smart-tags to a deposit invoice. |
| Link smart tags to estimate | `linkEstimateSmartTags` | Link a list of smart-tags to an estimate. |
| Link smart tags to individual | `linkIndividualSmartTags` | Link a list of smart tag to an individual. |
| Link smart tags to invoice | `linkInvoiceSmartTags` | Link a list of smart-tags to an invoice. |
| Link smart tags to opportunity | `linkOpportunitySmartTags` | Link a list of smart-tags to an opportunity. |
| List account addresses | `getAddresses` | List all addresses of the account. |
| List assigned staff labels | `getAssignedStaffLabels` | List all assigned staff labels. |
| List bank accounts | `getBankAccounts` | List all bank accounts. |
| List check labels | `getCheckLabels` | List all check labels. |
| List companies favourite filters | `getCompanyFavouriteFilters` | Lists favourite filters that can be applied to company search endpoints. |
| List contacts favourite filters | `getContactFavouriteFilters` | List favourite filters for faster access to specific contacts; they can be applied directly to contact search endpoints. |
| List credit-notes favourite filters | `getCreditNoteFavouriteFilters` | List favourite filters for faster access to specific credit notes; they can be applied directly to credit note search endpoints. |
| List deposit invoices | `getDepositInvoices` | List all deposit invoices. |
| List directories and files in a directory | `getDirectoryFiles` | List directories and files belonging to a directory. |
| List directories and files of a company | `getCompanyFiles` | Lists directories and files attached to a company (open beta route). |
| List directories and files of a contact | `getContactFiles` | List directories and files attached to a contact. |
| List directories and files of a credit note | `getCreditNoteFiles` | List directories and files attached to a credit note. |
| List directories and files of a deposit invoice | `getDepositInvoiceFiles` | List directories and files attached to a deposit invoice. |
| List directories and files of an estimate | `getEstimateFiles` | List directories and files attached to an estimate (open beta route). |
| List directories and files of an individual | `getIndividualFiles` | List directories and files attached to an individual. |
| List directories and files of an invoice | `getInvoiceFiles` | List directories and files attached to an invoice. |
| List directories and files of an opportunity | `getOpportunityFiles` | List directories and files attached to an opportunity. |
| List directories and files of an order | `getOrderFiles` | List directories and files attached to an order. |
| List document models | `getModels` | Fetch a list of document models. |
| List estimates favourite filters | `getEstimateFavouriteFilters` | List favourite filters for faster access to specific estimates; they can be applied directly to estimate search endpoints. |
| List exports | `listListingExports` | List all exports for the current user, ordered by creation date. |
| List individuals favourite filters | `getIndividualFavouriteFilters` | List favourite filters for faster access to specific individuals; they can be applied directly to individual search endpoints. |
| List invoices favourite filters | `getInvoiceFavouriteFilters` | List favourite filters for faster access to specific invoices; they can be applied directly to invoice search endpoints. |
| List items favourite filters | `getItemFavouriteFilters` | List favourite filters for faster access to specific items; they can be applied directly to item search endpoints. |
| List OAuth clients | `listClients` | List the OAuth clients for API. |
| List of all payment methods | `getPaymentMethods` | List of all payment methods. |
| List opportunities favourite filters | `getOpportunityFavouriteFilters` | List favourite filters for faster access to specific opportunities; they can be applied directly to opportunity search endpoints. |
| List orders favourite filters | `getOrderFavouriteFilters` | List favourite filters for faster access to specific orders; they can be applied directly to order search endpoints. |
| List payment terms | `getPaymentTerms` | List all payment terms. |
| List proposal models | `getProposalsModels` | List all proposal models. |
| List provider calendars | `getCalendars` | Returns the list of calendars available on the authenticated user's synced provider (Google or Outlook). |
| List Webhook Events | `getWebhookEvents` | List all event names available for a webhook. |
| Mark all unread notifications as read | `markAllNotificationsAsRead` | Mark all unread notifications as read. |
| Mark notification as read | `markNotificationAsRead` | Mark a notification as read or unread. |
| Move a file to a new directory | `moveFile` | Move a file to a new directory. The target can be a folder or a direct entity such as a company. |
| Ocr List - Purchase invoices | `getOcrPurInvoice` | Get list of OCR documents for purchase invoices. |
| Opportunity custom fields List | `getOpportunityCustomFields` | Get list of custom fields for an opportunity. |
| Opportunity smart-tags list | `getOpportunitySmartTags` | Get list of smart-tags for an opportunity. |
| Order custom fields List | `getOrderCustomFields` | Get list of custom fields for an order. |
| Order payments list | `getOrderPayments` | Get list of payments for an order. |
| Order smart tags List | `getOrderSmartTags` | Get list of smart tags for an order. |
| Partially update opportunity | `patchOpportunity` | Partially update an opportunity on specific properties. Complex relationships (related, source, contacts, staffs) are not supported in PATCH. |
| PhoneCalls List | `getPhoneCalls` | Get a list of phone calls. |
| Prepare a deposit invoice | `prepareDepositInvoice` | Prepare the rows of a deposit invoice for a percentage of the parent document. Does not create anything. |
| Profiles list | `getProfiles` | Get profiles list. |
| Proforma Invoice custom fields List | `getProformaInvoiceCustomFields` | Get list of custom fields for a proforma invoice. |
| Put staff licenses | `updateStaffLicenses` | Replace the licenses of a staff member; pass all existing licenses to keep them. |
| Rate categories list | `getRateCategories` | Get list of rate categories. |
| Record payment on a company | `createCompanyPayment` | Records a payment on a company (open beta route). |
| Record payment on an individual | `createIndividualPayment` | Record a payment on an individual. |
| Reschedule an export | `rescheduleListingExport` | Reschedule a previously failed or completed export. This creates a new export with the same configuration and triggers it. |
| Retrieve invoicing conformity state | `getInvoicingConformityState` | Get invoicing conformity state. |
| Scopes List | `getScopes` | Get list of scopes. |
| Search | `globalSearch` | Global search across Sellsy objects (companies, contacts, opportunities, items, documents and more). |
| Search accounting codes | `searchAccountingCodes` | Search in list of accounting codes. |
| Search accounting journal | `searchAccountingJournal` | Search in list of accounting journal entries. |
| Search All Opportunity Pipeline Steps | `searchAllOpportunityPipelineSteps` | Search steps across all opportunity pipelines. |
| Search barcodes | `searchBarcodes` | Search item barcodes. |
| Search calendar event | `searchCalendarEvents` | Search calendar events. |
| Search comments | `searchComments` | Search through comments. |
| Search companies | `searchCompanies` | Search companies. |
| Search contacts | `searchContacts` | Search contacts. |
| Search credit notes | `searchCreditNotes` | Search credit notes. |
| Search Custom Activities | `searchCustomActivities` | Search Custom Activities. |
| Search Declinations | `searchItemDeclinations` | Search the declinations (variants) of an item. |
| Search deliveries | `searchDeliveries` | Search deliveries. |
| Search deposit invoices | `searchDepositInvoices` | Search deposit invoices. |
| Search document models | `searchModels` | Search document models. |
| Search estimates | `searchEstimates` | Search estimates. |
| Search exports | `searchListingExports` | Search exports for the current user, ordered by creation date. |
| Search GoCardless mandates | `searchMandates` | Search the GoCardless direct debit mandates of the account. |
| Search in activity | `searchActivities` | Search in activity. |
| Search in CRM activity | `searchCrmActivities` | Search the CRM activity feed. |
| Search individuals | `searchIndividuals` | Search individuals. |
| Search invoices | `searchInvoices` | Search invoices. |
| Search items | `searchItems` | Search items. |
| Search methods of payment | `searchPaymentMethods` | Search payment methods. |
| Search OCR - Purchase invoices | `searchOcrPurInvoice` | Search OCR documents of purchase invoices. |
| Search Opportunities | `searchOpportunities` | Search opportunities. |
| Search Opportunity Pipeline Steps | `searchOpportunityPipelineSteps` | Search the steps of an opportunity pipeline. |
| Search Opportunity Pipelines | `searchOpportunityPipelines` | Search opportunity pipelines. |
| Search Opportunity Sources | `searchOpportunitySources` | Search opportunity sources. |
| Search orders | `searchOrders` | Search orders. |
| Search payment installments of subscriptions | `searchSubscriptionsPaymentInstallments` | Search payment installments of subscriptions. |
| Search payments | `searchPayments` | Search through payments. |
| Search phoneCalls | `searchPhoneCalls` | Search a list of phone calls. |
| Search proposal models | `searchProposalsModels` | Search proposal models. |
| Search Staffs | `searchStaffs` | Search list of staffs. The response may contain only your own staff, depending on your subscription plan. |
| Search subscriptions | `searchSubscriptions` | Search subscriptions. |
| Search Tasks | `searchTasks` | Search tasks. |
| Search taxes | `searchTaxes` | Search taxes. |
| Search User Notifications | `searchNotifications` | Search notifications related to current user. |
| Search Webhooks | `searchWebhooks` | Search webhooks. |
| Send Email | `sendEmail` | Send an email to external recipients (available upon request only). This delivers a real email. |
| Smart tags autocomplete | `autocompleteSmartTags` | Autocomplete for smart tags. |
| Tasks List | `getTasks` | Get a list of tasks. |
| Tax accounting codes list | `getTaxAccountingChart` | Get tax accounting codes. |
| Taxes accounting codes list | `getTaxesAccountingCharts` | Get the accounting codes of all taxes. |
| Taxes list | `getTaxes` | Get list of taxes. |
| Team List | `getTeams` | Get a list of teams. |
| Timeline search | `searchTimeline` | Search in timeline activity of an object. |
| Unlink a contact of company | `unlinkCompanyContact` | Unlink a contact of company. |
| Unlink a credit note from an invoice | `unlinkCreditNoteFromInvoice` | Unlink a credit note from an invoice. |
| Unlink a discount including taxes from a credit note | `unlinkCreditNoteDiscountInclTaxes` | Unlink a discount including taxes from a credit note. |
| Unlink a discount including taxes from an estimate | `unlinkEstimateDiscountInclTaxes` | Unlink a discount including taxes from an estimate. |
| Unlink a discount including taxes from an invoice | `unlinkInvoiceDiscountInclTaxes` | Unlink a discount including taxes from an invoice. |
| Unlink a discount including taxes from an order | `unlinkOrderDiscountInclTaxes` | Unlink a discount including taxes from an order. |
| Unlink a prime from a credit note | `unlinkCreditNotePrime` | Unlink a prime from a credit note. |
| Unlink a prime from an estimate | `unlinkEstimatePrime` | Unlink a prime from an estimate. |
| Unlink a prime from an invoice | `unlinkInvoicePrime` | Unlink a prime from an invoice. |
| Unlink a prime from an order | `unlinkOrderPrime` | Unlink a prime from an order. |
| Unlink an invoice from a credit note | `unlinkInvoiceFromCreditNote` | Unlink an invoice from a credit note. |
| Unlink payment from credit note | `unlinkCreditNotePayment` | Unlink a payment from a credit note. |
| Unlink payment from deposit invoice | `unlinkDepositInvoicePayment` | Unlink a payment from a deposit invoice. |
| Unlink payment from estimate | `unlinkEstimatePayment` | Unlink a payment from an estimate. |
| Unlink payment from invoice | `unlinkInvoicePayment` | Unlink a payment from an invoice. |
| Unlink payment from order | `unlinkOrderPayment` | Unlink a payment from an order. |
| Update a comment | `updateComment` | Update a comment. |
| Update a company address | `updateCompanyAddress` | Update a company address. |
| Update a contact address | `updateContactAddress` | Update a contact address. |
| Update a contact of company link | `updateCompanyContact` | Update a contact of company link. |
| Update a deposit invoice | `updateDepositInvoice` | Update a draft deposit invoice. Updating does not send it to the client. |
| Update a discount including taxes | `updateDiscountInclTaxes` | Update a discount including taxes. |
| Update a payment installment for a subscription | `updateSubscriptionPaymentInstallment` | Updates the date and/or the sending mode of a pending payment installment. |
| Update a phoneCall | `updatePhoneCall` | Update a phone call. |
| Update a progress invoice | `updateProgressInvoice` | Update a draft progress invoice. Updating does not send it to the client unless validation options request it. |
| Update a rate category | `updateRateCategory` | Update a rate category. |
| Update a subscription | `updateSubscription` | Update a subscription. The fields model and conditions cannot be modified. |
| Update a task | `updateTask` | Update a task. |
| Update accounting charts settings | `updateAccountingChartsSettings` | Update accounting charts settings. |
| Update an export | `updateListingExport` | Update the export. |
| Update an individual address | `updateIndividualAddress` | Update an individual address. |
| Update an item | `updateItem` | Update an item. |
| Update an order | `updateOrder` | Update a given order. |
| Update calendar event | `updateCalendarEvent` | Update calendar event. |
| Update Company | `updateCompany` | Update Company informations. |
| Update Company custom fields | `updateCompanyCustomFields` | Update list of custom fields for a company. |
| Update contact | `updateContact` | Update contact informations. |
| Update contact custom fields | `updateContactCustomFields` | Update list of custom fields for a contact. |
| Update credit note | `updateCreditNote` | Update a draft credit note. Updating does not send it to the client. |
| Update credit note custom fields | `updateCreditNoteCustomFields` | Update list of custom fields for a credit note. |
| Update Custom Activity | `updateCustomActivity` | Edit a custom activity. |
| Update Custom Activity Type | `updateCustomActivityType` | Update a custom activity type. |
| Update Deposit Invoice custom fields | `updateDepositInvoiceCustomFields` | Update list of custom fields for a deposit invoice. |
| Update directory | `updateDirectory` | Update a directory. |
| Update document model | `updateModel` | Update a document model. |
| Update email settings | `updateEmailSettings` | Update email settings. |
| Update estimate | `updateEstimate` | Update an estimate (open beta route). |
| Update Estimate custom fields | `updateEstimateCustomFields` | Update list of custom fields for an estimate. |
| Update estimate status | `updateEstimateStatus` | Update an estimate status. Changing the status does not email the client. |
| Update Individual | `updateIndividual` | Update Individual informations. |
| Update Individual custom fields | `updateIndividualCustomFields` | Update list of custom fields for an individual. |
| Update invoice | `updateInvoice` | Update a draft invoice. Updating does not send it to the client. |
| Update Invoice custom fields | `updateInvoiceCustomFields` | Update list of custom fields for an invoice. |
| Update item prices | `updateItemPrices` | Update prices list (per rate category) for an item. |
| Update Notifications settings | `updateNotificationsSettings` | Update notifications settings. |
| Update Opportunity | `updateOpportunity` | Update Opportunity informations. |
| Update opportunity custom fields | `updateOpportunityCustomFields` | Update list of custom fields for an opportunity. |
| Update opportunity's rank and/or step | `updateOpportunityRank` | Update an opportunity's rank in its pipeline step or move it to a new step. |
| Update Order custom fields | `updateOrderCustomFields` | Update list of custom fields for an order. |
| Update Staff | `updateStaff` | Update staff informations. |
| Update tax | `updateTax` | Update tax informations. Due to e-invoicing regulations, rate 0 is no longer allowed; use exempted tax types instead. |
| Update tax accounting codes | `updateTaxAccountingChart` | Update tax accounting codes. |
| Update Webhook | `updateWebhook` | Update webhook informations. |
| Upload file for email | `uploadEmailAttachment` | Upload a file to attach to an outgoing email. |
| Validate credit note | `validateCreditNote` | Validate a draft credit note into due status; it can no longer be edited or deleted, and may be transmitted via e-invoicing. |
| Validate Deposit Invoice | `validateDepositInvoice` | Validate a draft deposit invoice into due status; it can no longer be edited or deleted, and may be transmitted via e-invoicing. |
| Validate email's DNS | `validateEmailDomainDns` | Validate the DNS configuration of an email sending domain. |
| Validate Invoice | `validateInvoice` | Validate a draft invoice into due status; it can no longer be edited or deleted, and may be transmitted via e-invoicing. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Calendar event created | `event.created` |  |
| Client created | `client.created` |  |
| Client deleted | `client.deleted` |  |
| Client updated | `client.updated` |  |
| Contact created | `people.created` |  |
| Contact updated | `people.updated` |  |
| Estimate created | `estimate.created` |  |
| Estimate status changed | `estimate.step` |  |
| Invoice created | `invoice.created` |  |
| Invoice payment added | `invoice.paymentadd` |  |
| Opportunity created | `opportunity.created` |  |
| Opportunity step changed | `opportunity.step` |  |
| Opportunity updated | `opportunity.updated` |  |
| Prospect created | `prospect.created` |  |
| Task created | `task.created` |  |
