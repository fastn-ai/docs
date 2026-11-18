---
description: "Moneybird is a Dutch online accounting and invoicing platform."
hidden: true
---

# Moneybird

<img src="../../.gitbook/assets/connectors/lg/moneybird.png" alt="Moneybird logo">

Moneybird is a Dutch online accounting and invoicing platform. This connector covers the Moneybird API v2: contacts and contact people, sales invoices, recurring sales invoices, estimates, external sales invoices, purchase invoices, receipts, general and general journal documents, subscriptions and subscription templates, products, projects, time entries, task lists and tasks, ledger accounts, tax rates, financial accounts, mutations and statements, payments, purchase transactions, identities, custom fields, document styles, users, verifications, reports, downloads, the customer contact portal, workflows and webhooks.

| | |
| --- | --- |
| **Category** | [Finance and payments](README.md) |
| **Website** | [moneybird.com](https://moneybird.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `moneybird` |

## Use it

Add Moneybird from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.moneybird.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Webhook | `activateWebhook` | Reactivates a previously deactivated Moneybird webhook so it resumes receiving event notifications. |
| Add Attachment To External Sales Invoice | `addExternalSalesInvoiceAttachment` | Attaches a file to an existing external sales invoice in a Moneybird administration, for example the original receipt or order confirmation. The file is sent as a multipart upload, so supply the file name, its media type and its text content. |
| Add Attachment To General Document | `addGeneralDocumentAttachment` | Uploads a text-based file and attaches it to a general document. Binary files such as PDFs and images cannot be sent through this action because the request body is transmitted as UTF-8 text. |
| Add Attachment To General Journal Document | `addAttachmentToGeneralJournalDocument` | Attaches a text file to a Moneybird general journal document, for example a CSV or a note supporting the booking. The file is sent as a multipart upload. Binary formats such as PDF or images cannot be sent through this integration and must be attached in the Moneybird interface. |
| Add Attachment To Purchase Invoice | `addPurchaseInvoiceAttachment` | Uploads a text-based file and attaches it to a purchase invoice. Binary files such as PDFs and images cannot be sent through this action because the request body is transmitted as UTF-8 text. |
| Add Attachment To Receipt | `addReceiptAttachment` | Uploads a text-based file and attaches it to a receipt. Binary files such as PDFs and images cannot be sent through this action because the request body is transmitted as UTF-8 text. |
| Add Attachment To Typeless Document | `addTypelessDocumentAttachment` | Uploads a text-based file and attaches it to a typeless document. Moneybird classifies a typeless document as a purchase invoice as soon as it receives an attachment, so the document moves out of the typeless document list after this call. Binary files such as PDFs and images cannot be sent through this action because the request body is transmitted as UTF-8 text. |
| Add Estimate Attachment | `addEstimateAttachment` | Attaches a text-based document, such as a CSV, XML or plain-text file, to a Moneybird estimate. The file is uploaded as multipart form data and Moneybird answers with an empty body; read the estimate back with Get Estimate to obtain the new attachment id. Binary formats such as PDF or images cannot be uploaded through this action because the request body is transmitted as text. |
| Add Note To Contact | `addNoteToContact` | Adds an internal note to a Moneybird contact. Setting todo, or assigning the note to a colleague, turns it into a to-do item. |
| Add Note To External Sales Invoice | `createExternalSalesInvoiceNote` | Adds a note to an external sales invoice in a Moneybird administration. Set todo to true, or assign the note to a user, to turn it into a to-do item instead of a plain note. |
| Add Note To General Journal Document | `addNoteToGeneralJournalDocument` | Adds an internal note to a Moneybird general journal document. A note can optionally be turned into a to-do and assigned to a colleague. |
| Add Sales Invoice Attachment | `addSalesInvoiceAttachment` | Attaches a text-based document, such as a CSV, XML or plain-text file, to a Moneybird sales invoice. The file is uploaded as multipart form data and Moneybird answers with an empty body; read the invoice back with Get Sales Invoice to obtain the new attachment id. Binary formats such as PDF or images cannot be uploaded through this action because the request body is transmitted as text. |
| Add Source To Asset | `createAssetSource` | Links the booking that paid for a fixed asset to that asset in a Moneybird administration. Supply either a document line or a general journal document entry, and it must sit on the same ledger account as the asset. Fixed-asset ledger accounts do not accept invoice or receipt lines, so in practice the source is normally a general journal document entry. |
| Archive Contact | `archiveContact` | Archives a Moneybird contact so it no longer appears in the default contact list while its documents and history are kept. Use this for contacts that cannot be deleted because they are linked to documents. |
| Assign Task | `assignTask` | Assigns a user to a Moneybird task list task. Moneybird returns 404 when the user has no permission to the task. |
| Bill Estimate | `billEstimate` | Creates a sales invoice from an accepted Moneybird estimate and returns the new invoice. The estimate itself moves to the billed state. |
| Cancel Subscription | `cancelSubscription` | Cancels a Moneybird subscription so it stops generating invoices. Moneybird records the cancellation date and closes the subscription with an end date rather than removing it, so the subscription and its recurring sales invoice remain readable afterwards. |
| Change Estimate State | `changeEstimateState` | Changes the state of a Moneybird estimate without performing the matching action, so nothing is sent or billed. Not every transition is allowed; for example open to billed is accepted while draft to open is not. |
| Complete Task | `completeTask` | Marks a Moneybird task list task and all its subtasks as completed. |
| Create Asset | `createAsset` | Records a fixed asset in a Moneybird administration. The ledger account must be a fixed-asset account; Moneybird rejects any other with a ledger account is invalid error. Every asset needs a depreciation plan except one booked on a land or building account, where the plan must be left out entirely. |
| Create Asset Arbitrary Value Change | `createAssetArbitraryValueChange` | Books an arbitrary value change against a fixed asset in a Moneybird administration, replacing the planned depreciation from that date onwards. Any linear value changes after the given date are removed, and Moneybird refuses the change with a 422 when the amount exceeds the asset's value on that date. |
| Create Asset Disposal | `createAssetDisposal` | Records the disposal of a fixed asset in a Moneybird administration. The asset must be fully depreciated, so its value at the disposal date must be zero, and it must not already have a disposal. The date has to fall after the purchase date, outside the locked period and not in the future. |
| Create Asset Divestment Value Change | `createAssetDivestmentValueChange` | Divests a fixed asset in a Moneybird administration on a given date. The asset's remaining value is taken off the balance sheet and the profit is booked as a book result. Moneybird sets the amount itself from the asset's value on that date. |
| Create Asset Full Depreciation Value Change | `createAssetFullDepreciationValueChange` | Writes a fixed asset down to zero in a Moneybird administration on a given date, taking its remaining value off the balance sheet. Moneybird sets the amount itself from the asset's value on that date. |
| Create Asset Manual Value Change | `createAssetManualValueChange` | Writes a chosen amount off a fixed asset in a Moneybird administration on a given date, on top of its depreciation plan. Moneybird refuses the change with a 422 when the amount is larger than the asset's value on that date. |
| Create Asset Reinvestment Reserve Purchase | `createAssetReinvestmentReservePurchase` | Records that part of a fixed asset's purchase value was funded from the reinvestment reserve, the Dutch herinvesteringsreserve, in a Moneybird administration. The amount cannot exceed the asset's depreciable value, which is its purchase value minus its residual value. |
| Create Asset Reinvestment Reserve Sale | `createAssetReinvestmentReserveSale` | Books the book result of a disposed fixed asset to the reinvestment reserve, the Dutch herinvesteringsreserve, in a Moneybird administration. The asset must already have a disposal, and that disposal date may not fall inside the locked period. |
| Create Asset Retroactive Linear Value Changes | `createAssetRetroactiveLinearValueChanges` | Creates the linear depreciation entries a fixed asset should already have in a Moneybird administration. Use it after recording a new asset with a past purchase date, or after an arbitrary value change, so the missing monthly entries are recalculated and booked. Moneybird answers with HTTP 204 and no content; read the asset back with Get Asset to see the entries it created. |
| Create Contact | `createContact` | Creates a contact in a Moneybird administration. At least one of company name, first name or last name must be supplied. An initial contact person can be created in the same call. Note that Moneybird stores the bank account but does not echo it back in the response. |
| Create Contact Additional Charge | `createContactAdditionalCharge` | Queues an additional charge on a contact. At the end of the current period Moneybird merges the contact's additional charges into an invoice and schedules it for sending on the first day of the next month, so only create a charge you intend to bill. There is no API route to remove an additional charge once created, and a contact holding an unbilled charge can only be archived, not deleted, so treat this call as irreversible. |
| Create Contact Moneybird Payments Mandate URL | `createContactMoneybirdPaymentsMandateUrl` | Returns a link the contact can use to set up a Moneybird Payments direct-debit mandate themselves, so you can deliver it over your own channel instead of Moneybird's email. The link is valid for 14 days and the contact must make a 15 cent verification payment. Requires Moneybird Payments to be enabled; without that entitlement Moneybird answers HTTP 403. |
| Create Contact Person | `createContactPerson` | Adds a contact person to an existing Moneybird contact. Moneybird expects at least a first name and a last name. |
| Create Estimate | `createEstimate` | Creates an estimate in a Moneybird administration. The estimate is created as a draft; use Send Estimate to issue it. Estimate lines are supplied as details, each with a description, price, quantity, tax rate and ledger account. |
| Create Estimate Note | `createEstimateNote` | Adds a note or to-do to a Moneybird estimate. Supplying an assignee turns the note into a to-do assigned to that user. |
| Create External Sales Invoice | `createExternalSalesInvoice` | Records an invoice that was billed by another system, such as a webshop or point of sale, in a Moneybird administration. Supply the invoice lines as details attributes, each with a description, price, amount, tax rate and ledger account. Unlike a sales invoice, an external sales invoice is booked immediately rather than created as a draft. |
| Create External Sales Invoice From Attachment | `createExternalSalesInvoiceFromAttachment` | Creates a new external sales invoice in a Moneybird administration straight from an uploaded document. The file is sent as a multipart upload, so supply the file name, its media type and its text content. Moneybird answers with HTTP 200 and an empty body, and names the new invoice after the uploaded file; read the list back with List External Sales Invoices to pick up its id. |
| Create Financial Statement | `createFinancialStatement` | Creates a financial statement on a Moneybird financial account and groups the supplied bank mutations into it. Use this to import bank transactions that no automatic bank link delivers. |
| Create General Document | `createGeneralDocument` | Creates a new general document in a Moneybird administration. A reference is required; optionally set a document date and a due date and link a contact. Moneybird's documented reminder fields are not exposed: the nested reminder object returns HTTP 500 and reminder_date is silently discarded, both reproduced directly against the Moneybird API. |
| Create General Document Note | `createGeneralDocumentNote` | Adds a note or to-do to a general document in a Moneybird administration. Supplying an assignee turns the note into a to-do assigned to that user. |
| Create General Journal Document | `createGeneralJournalDocument` | Creates a general journal document in a Moneybird administration - a manual double-entry booking. A reference is required despite being optional in Moneybird's published schema, and the total debit and total credit across the entries must balance. The date defaults to today when omitted. |
| Create Identity | `createIdentity` | Creates an additional sender identity in a Moneybird administration. Company name, address line 1, postcode, city, country and email are all required; bank details and custom field values are optional. |
| Create Ledger Account | `createLedgerAccount` | Creates a ledger account in a Moneybird administration. The name must be unique within the administration for the chosen account type, and Moneybird requires an RGS version 3.5 taxonomy code alongside the account itself. The general ledger code is assigned automatically when no account code is supplied. |
| Create Product | `createProduct` | Creates a product in a Moneybird administration so it can be added as a line to invoices, estimates and subscriptions. Moneybird requires a price and a ledger account, and rejects the product unless it also carries either a tax rate id or both a product type and a VAT rate type. |
| Create Product Sales Link | `createProductSalesLink` | Generates a one-hour online sales link for a Moneybird product, optionally with the buyer pre-filled on the checkout page. The product must be set up for online sales, which requires Moneybird Online Payment Methods to be active on the administration. |
| Create Project | `createProject` | Creates a project in a Moneybird administration. The project name must be unique within the administration. Projects are used to group invoice lines, estimates and time entries for reporting. |
| Create Purchase Invoice | `createPurchaseInvoice` | Creates a new purchase invoice in a Moneybird administration. Moneybird requires a supplier contact, a reference and at least one invoice line, and every line must carry a purchase tax rate. A ledger account is optional but must be an expense-type account when supplied. |
| Create Purchase Invoice Note | `createPurchaseInvoiceNote` | Adds a note or to-do to a purchase invoice in a Moneybird administration. Supplying an assignee turns the note into a to-do assigned to that user. |
| Create Purchase Invoice Payment | `createPurchaseInvoicePayment` | Registers a payment against a purchase invoice in a Moneybird administration. Bank transfers require a financial mutation, balance settlements a ledger account, and invoice settlements the id of the document to settle against. |
| Create Receipt | `createReceipt` | Creates a new receipt in a Moneybird administration. Moneybird requires a supplier contact, a reference and at least one receipt line, and every line must carry both a purchase tax rate and an expense-type ledger account. Supply a financial account under Payment to mark the receipt as paid from that account straight away. |
| Create Receipt Note | `createReceiptNote` | Adds a note or to-do to a receipt in a Moneybird administration. Supplying an assignee turns the note into a to-do assigned to that user. |
| Create Receipt Payment | `createReceiptPayment` | Registers a payment against a receipt in a Moneybird administration. Bank transfers require a financial mutation, balance settlements a ledger account, and invoice settlements the id of the document to settle against. |
| Create Recurring Sales Invoice | `createRecurringSalesInvoice` | Creates a recurring sales invoice in a Moneybird administration. It generates a new sales invoice on a fixed schedule, so it needs at least a contact, the invoice lines and a planning defined by the frequency, the frequency type and a future invoice date. Moneybird rejects a mergeable recurring invoice unless automatic sending is also enabled. The planning fields for limiting the number of invoices and for merging are accepted but are not returned in the response. |
| Create Recurring Sales Invoice Note | `createRecurringSalesInvoiceNote` | Adds a note or to-do to a Moneybird recurring sales invoice. Supplying an assignee turns the note into a to-do assigned to that user. |
| Create Sales Invoice | `createSalesInvoice` | Creates a sales invoice in a Moneybird administration. The invoice is created as a draft; use Send Invoice to issue it. Invoice lines are supplied as details, each with a description, price, quantity, tax rate and ledger account. |
| Create Sales Invoice Note | `createSalesInvoiceNote` | Adds a note or to-do to a Moneybird sales invoice. Supplying an assignee turns the note into a to-do assigned to that user. |
| Create Sales Invoice Payment | `createSalesInvoicePayment` | Registers a payment on a Moneybird sales invoice. The manual payment action decides which additional field is mandatory: a financial account for private and cash payments, a financial mutation for bank transfers, a ledger account for balance settlements and a document id for settlements against another invoice. |
| Create Scheduled One-Off Sales Invoice For Subscription | `createSubscriptionOneOffSalesInvoice` | Creates a separate sales invoice for a Moneybird subscription, such as usage-based costs, and schedules it to go out together with the next subscription invoice so the customer receives them as one document. Because the invoice is scheduled for sending, the contact must have an email address; WITH A REAL CONTACT THIS DELIVERS AN INVOICE TO THE CUSTOMER. |
| Create Subscription | `createSubscription` | Starts a subscription for a contact on a Moneybird product. The product carries the price, description and billing frequency, and Moneybird automatically creates a recurring sales invoice to bill the contact, returning its id on the subscription. |
| Create Subscription Additional Charge | `createSubscriptionAdditionalCharge` | Queues an extra charge on a Moneybird subscription, for example metered usage. At the end of the current subscription period the queued charges are merged where possible and invoiced together with the subscription invoice. |
| Create Subscription Template Sales Link | `createSubscriptionTemplateSalesLink` | Generates an online sales link for a Moneybird subscription template, so a customer can subscribe themselves. The contact, product and start date can be pre-set on the link. The link is valid for one hour. |
| Create Task | `createTask` | Creates a task inside a Moneybird task list group. A task can be assigned to a user, linked to a ledger account and generated from a report. |
| Create Task List | `createTaskList` | Creates a task list in a Moneybird administration. Supply a template id to generate the list's groups and tasks from an existing task list template. |
| Create Task List From Template | `createTaskListFromTemplate` | Creates a new Moneybird task list from an existing task list template, copying the template's groups and generating their tasks. Only the name and description can be overridden: the deadline and period are always derived from the template's own period, verified live. |
| Create Task List Group | `createTaskListGroup` | Adds a group to a Moneybird task list. Giving the group a report type makes Moneybird generate its tasks from that report. |
| Create Task List Template | `createTaskListTemplate` | Creates a task list template in a Moneybird administration. A template defines the recurrence period and deadline used when task lists are generated from it. Moneybird gives every new template one unnamed default group; the period defaults to P1M when it is not supplied. |
| Create Task List Template Group | `createTaskListTemplateGroup` | Adds a group to a Moneybird task list template. Giving the group a report type makes its tasks be generated from that report whenever a task list is created from the template. |
| Create Task Note | `createTaskNote` | Adds a note or to-do to a Moneybird task list task. |
| Create Time Entry | `createTimeEntry` | Records a time entry for an employee in a Moneybird administration. Start and end times are rounded down to whole minutes with a minimum of one minute between them. Omit the end time to start a running timer. The connected API user needs access to both time entries and sales invoices. |
| Create Time Entry Note | `createTimeEntryNote` | Adds a note or to-do to a Moneybird time entry. Supplying an assignee turns the note into a to-do assigned to that user. |
| Create Typeless Document | `createTypelessDocument` | Creates a new typeless document in a Moneybird administration. A typeless document holds an uploaded file that has not yet been classified; adding an attachment to it converts it into a purchase invoice. |
| Create Webhook | `createWebhook` | Registers a webhook on a Moneybird administration. Moneybird calls the supplied HTTPS URL once at creation and expects HTTP 200, then delivers a notification for every subscribed event. Leave the event list empty to receive every event. The signing secret is returned only in this response. |
| Deactivate Webhook | `deactivateWebhook` | Deactivates a Moneybird webhook. It stops receiving new event notifications while outstanding retries are still delivered, and it can be reactivated at any time. |
| Delete Asset | `deleteAsset` | Permanently removes a fixed asset from a Moneybird administration, together with its depreciation plan and value changes. |
| Delete Asset Reinvestment Reserve Purchase | `deleteAssetReinvestmentReservePurchase` | Removes the reinvestment reserve purchase from a fixed asset in a Moneybird administration, restoring the asset's full depreciable value. |
| Delete Asset Reinvestment Reserve Sale | `deleteAssetReinvestmentReserveSale` | Removes the reinvestment reserve sale from a disposed fixed asset in a Moneybird administration, returning the book result to ordinary profit. |
| Delete Asset Source | `deleteAssetSource` | Unlinks a funding booking from a fixed asset in a Moneybird administration. Neither the asset nor the underlying document line is deleted. |
| Delete Contact | `deleteContact` | Permanently deletes a contact from a Moneybird administration. Moneybird refuses the deletion when the contact is still linked to documents; archive the contact instead in that case. |
| Delete Contact Moneybird Payments Mandate | `deleteContactMoneybirdPaymentsMandate` | Deletes the stored Moneybird Payments mandate of a contact, so future invoices are no longer collected by direct debit. Requires Moneybird Payments to be enabled for the administration; without that entitlement Moneybird answers HTTP 403. |
| Delete Contact Person | `deleteContactPerson` | Permanently deletes a contact person from a Moneybird contact. |
| Delete Estimate | `deleteEstimate` | Permanently deletes a Moneybird estimate. Moneybird answers with an empty body on success. |
| Delete Estimate Attachment | `deleteEstimateAttachment` | Removes a file attached to a Moneybird estimate. Moneybird answers with an empty body on success. |
| Delete Estimate Note | `deleteEstimateNote` | Deletes a note or to-do from a Moneybird estimate. Moneybird answers with an empty body on success. |
| Delete External Sales Invoice | `deleteExternalSalesInvoice` | Permanently deletes an external sales invoice from a Moneybird administration, removing it and its lines from the bookkeeping. |
| Delete External Sales Invoice Attachment | `deleteExternalSalesInvoiceAttachment` | Removes a file attached to an external sales invoice in a Moneybird administration. |
| Delete External Sales Invoice Payment | `deleteExternalSalesInvoicePayment` | Removes a registered payment from an external sales invoice in a Moneybird administration, returning the invoice to its unpaid balance. |
| Delete Financial Statement | `deleteFinancialStatement` | Permanently deletes a Moneybird financial statement together with the bank mutations grouped into it. |
| Delete General Document | `deleteGeneralDocument` | Permanently deletes a general document from a Moneybird administration, together with its attachments and notes. |
| Delete General Document Attachment | `deleteGeneralDocumentAttachment` | Deletes a single attachment from a general document in a Moneybird administration. |
| Delete General Document Note | `deleteGeneralDocumentNote` | Deletes a note or to-do from a general document in a Moneybird administration. |
| Delete General Journal Document | `deleteGeneralJournalDocument` | Permanently deletes a general journal document and all of its entries from a Moneybird administration. This cannot be undone. |
| Delete General Journal Document Attachment | `deleteGeneralJournalDocumentAttachment` | Permanently removes an attachment from a general journal document. |
| Delete Identity | `deleteIdentity` | Permanently deletes an additional Moneybird sender identity. The administration's default identity cannot be deleted this way. |
| Delete Ledger Account | `deleteLedgerAccount` | Removes a ledger account from a Moneybird administration. Moneybird first tries to deactivate the account and only deletes it when deactivation is not possible, and it always answers with HTTP 204 even when the account could not be removed. Read the account back afterwards to see whether it was deleted or merely deactivated. |
| Delete Note From Contact | `deleteNoteFromContact` | Removes an internal note from a Moneybird contact. |
| Delete Note From External Sales Invoice | `deleteExternalSalesInvoiceNote` | Removes a note or to-do from an external sales invoice in a Moneybird administration. |
| Delete Note From General Journal Document | `deleteNoteFromGeneralJournalDocument` | Removes an internal note from a Moneybird general journal document. |
| Delete Product | `deleteProduct` | Removes a product from a Moneybird administration. A product that is still referenced by document lines, orders, subscriptions or subscription templates cannot be deleted and is deactivated instead, and Moneybird answers with HTTP 204 either way. Read the product back afterwards to see which happened. |
| Delete Project | `deleteProject` | Deletes a Moneybird project. A project with no linked sales invoices, estimates or time entries is removed permanently; a project that still has linked records is archived instead and keeps its history. |
| Delete Purchase Invoice | `deletePurchaseInvoice` | Permanently deletes a purchase invoice from a Moneybird administration, together with its lines, notes and attachments. |
| Delete Purchase Invoice Attachment | `deletePurchaseInvoiceAttachment` | Deletes a single attachment from a purchase invoice in a Moneybird administration. |
| Delete Purchase Invoice Note | `deletePurchaseInvoiceNote` | Deletes a note or to-do from a purchase invoice in a Moneybird administration. |
| Delete Purchase Invoice Payment | `deletePurchaseInvoicePayment` | Removes a registered payment from a purchase invoice in a Moneybird administration. |
| Delete Purchase Transaction | `deletePurchaseTransaction` | Deletes a Moneybird purchase transaction so the outgoing payment is no longer prepared. Moneybird answers 204 whether or not the transaction existed, so this is safe to retry. Delete Purchase Transaction By Delete Path reaches the same behaviour through Moneybird's alternative URL. |
| Delete Purchase Transaction By Delete Path | `deletePurchaseTransactionByDeletePath` | Deletes a Moneybird purchase transaction through Moneybird's alternative /delete URL. It behaves identically to Delete Purchase Transaction, including answering 204 when no such transaction exists; both routes are published by Moneybird and both are provided here so either documented form works. |
| Delete Receipt | `deleteReceipt` | Permanently deletes a receipt from a Moneybird administration, together with its lines, notes and attachments. |
| Delete Receipt Attachment | `deleteReceiptAttachment` | Deletes a single attachment from a receipt in a Moneybird administration. |
| Delete Receipt Note | `deleteReceiptNote` | Deletes a note or to-do from a receipt in a Moneybird administration. |
| Delete Receipt Payment | `deleteReceiptPayment` | Removes a registered payment from a receipt in a Moneybird administration. |
| Delete Recurring Sales Invoice | `deleteRecurringSalesInvoice` | Permanently deletes a Moneybird recurring sales invoice so it stops generating new invoices. Invoices it has already generated are kept. Moneybird answers with an empty body on success. |
| Delete Recurring Sales Invoice Note | `deleteRecurringSalesInvoiceNote` | Deletes a note or to-do from a Moneybird recurring sales invoice. Moneybird answers with an empty body on success. |
| Delete Sales Invoice | `deleteSalesInvoice` | Permanently deletes a Moneybird sales invoice, including invoices that have already been issued and numbered. Verified live against both a draft and an issued invoice. Deleting an issued invoice removes it from the bookkeeping, so prefer crediting it when an audit trail must be kept. |
| Delete Sales Invoice Attachment | `deleteSalesInvoiceAttachment` | Removes a file attached to a Moneybird sales invoice. Moneybird answers with an empty body on success. |
| Delete Sales Invoice Note | `deleteSalesInvoiceNote` | Deletes a note or to-do from a Moneybird sales invoice. Moneybird answers with an empty body on success. |
| Delete Sales Invoice Payment | `deleteSalesInvoicePayment` | Removes a registered payment from a Moneybird sales invoice, returning the invoice to its unpaid balance. Moneybird answers with an empty body on success. |
| Delete Task | `deleteTask` | Permanently deletes a Moneybird task list task and all its subtasks. Tasks that Moneybird generated from a report cannot be deleted. |
| Delete Task List | `deleteTaskList` | Permanently deletes a Moneybird task list together with all its groups and tasks. |
| Delete Task List Group | `deleteTaskListGroup` | Permanently deletes a Moneybird task list group and every task inside it. |
| Delete Task List Template | `deleteTaskListTemplate` | Permanently deletes a Moneybird task list template together with all the groups and tasks it contains. |
| Delete Time Entry | `deleteTimeEntry` | Permanently deletes a Moneybird time entry. |
| Delete Time Entry Note | `deleteTimeEntryNote` | Permanently removes a note or to-do from a Moneybird time entry. |
| Delete Typeless Document | `deleteTypelessDocument` | Permanently deletes a typeless document from a Moneybird administration. The document and its attachments are removed and cannot be recovered. |
| Delete Typeless Document Attachment | `deleteTypelessDocumentAttachment` | Deletes a single attachment from a typeless document in a Moneybird administration. |
| Delete Webhook | `deleteWebhook` | Removes a registered webhook from a Moneybird administration so it stops receiving event notifications. |
| Download Estimate Attachment | `downloadEstimateAttachment` | Downloads a file attached to a Moneybird estimate. Moneybird answers with a redirect to a temporary storage URL from which the file is retrieved, so the response is the file itself. |
| Download Estimate PDF | `downloadEstimatePdf` | Downloads a Moneybird estimate as a PDF document. Moneybird answers with a redirect to a temporary storage URL that stays valid for 30 seconds. |
| Download External Sales Invoice Attachment | `downloadExternalSalesInvoiceAttachment` | Downloads a file attached to an external sales invoice in a Moneybird administration. Moneybird answers with a redirect to a temporary storage URL, so the file content is fetched from the Location header of the response. |
| Download File | `downloadFile` | Fetches a prepared Moneybird export file. Moneybird answers with a redirect to the real storage URL, so the permission scope needed depends on the export type - documents exports need the documents scope, invoice exports the sales_invoices scope, and so on. |
| Download General Document Attachment | `downloadGeneralDocumentAttachment` | Downloads an attachment of a general document. Moneybird answers with a redirect to a temporary storage URL, which is followed automatically, so the action returns the file content itself. |
| Download General Journal Document Attachment | `downloadGeneralJournalDocumentAttachment` | Downloads an attachment of a general journal document. Moneybird answers with a redirect to a short-lived signed URL; the connector follows it and returns the file content. Text attachments come back readable; binary files such as PDFs come back as raw bytes and are best fetched from the download URL directly. |
| Download Purchase Invoice Attachment | `downloadPurchaseInvoiceAttachment` | Downloads an attachment of a purchase invoice. Moneybird answers with a redirect to a temporary storage URL, which is followed automatically, so the action returns the file content itself. |
| Download Receipt Attachment | `downloadReceiptAttachment` | Downloads an attachment of a receipt. Moneybird answers with a redirect to a temporary storage URL, which is followed automatically, so the action returns the file content itself. |
| Download Sales Invoice Attachment | `downloadSalesInvoiceAttachment` | Downloads a file attached to a Moneybird sales invoice. Moneybird answers with a redirect to a temporary storage URL from which the file is retrieved, so the response is the file itself. |
| Download Sales Invoice Packing Slip PDF | `downloadSalesInvoicePackingSlipPdf` | Downloads the packing slip of a Moneybird sales invoice as a PDF document. Moneybird answers with a redirect to a temporary storage URL that stays valid for 30 seconds. |
| Download Sales Invoice PDF | `downloadSalesInvoicePdf` | Downloads a Moneybird sales invoice as a PDF document. Moneybird answers with a redirect to a temporary storage URL that stays valid for 30 seconds. |
| Download Sales Invoice UBL | `downloadSalesInvoiceUbl` | Downloads a Moneybird sales invoice as a UBL electronic invoicing document. The response body is the UBL XML document itself, returned as raw text rather than as JSON. |
| Download Typeless Document Attachment | `downloadTypelessDocumentAttachment` | Downloads an attachment of a typeless document. Moneybird answers with a redirect to a temporary storage URL, which is followed automatically, so the action returns the file content itself. |
| Duplicate Sales Invoice To Credit Invoice | `duplicateSalesInvoiceToCreditInvoice` | Creates a new credit invoice that mirrors an existing Moneybird sales invoice with negative amounts. The credit invoice is created as a draft and references the original through its original sales invoice id. |
| Export Auditfile | `exportAuditfile` | Queues a Moneybird auditfile export in XAF XML format for a financial year. The file appears in the administration's downloads once it is ready. The administration must have no ledger accounts with a missing or duplicate account id. |
| Export Brugstaat | `exportBrugstaat` | Queues a Moneybird brugstaat XML export for a financial year. The file appears in the administration's downloads once it is ready. Every ledger account must have a valid RGS taxonomy code assigned. |
| Export Ledger Accounts | `exportLedgerAccounts` | Queues a Moneybird export of the ledger account cards to an Excel file for a financial year, containing every booking for manual audit. The file appears in the administration's downloads once it is ready. |
| Fetch Contacts By IDs | `fetchContactsByIds` | Returns the full contact records for a list of contact ids, for incremental synchronisation. Moneybird returns at most 100 contacts per call even when more ids are supplied. |
| Fetch Estimates By IDs | `fetchEstimatesByIds` | Returns the full estimate records for a list of estimate ids, for incremental synchronisation. Moneybird returns at most 100 estimates per call even when more ids are supplied. |
| Fetch External Sales Invoices By IDs | `fetchExternalSalesInvoicesByIds` | Returns the full external sales invoice records for a list of ids, for incremental synchronisation. Moneybird returns at most 100 invoices per call even when more ids are supplied. |
| Fetch Financial Mutations By IDs | `fetchFinancialMutationsByIds` | Returns the full bank mutation records for a list of mutation ids, for incremental synchronisation. Moneybird returns at most 100 mutations per call even when more ids are supplied. |
| Fetch General Documents By IDs | `fetchGeneralDocumentsByIds` | Fetches full general document records for a list of document ids. Moneybird returns at most 100 documents per call, even when more ids are supplied. |
| Fetch General Journal Documents By IDs | `fetchGeneralJournalDocumentsByIds` | Fetches full general journal documents for a list of ids, at most 100 per call. Use it after List General Journal Document Versions: compare each returned version with the one you stored and fetch only the documents that changed. |
| Fetch Purchase Invoices By IDs | `fetchPurchaseInvoicesByIds` | Fetches full purchase invoice records for a list of invoice ids. Moneybird returns at most 100 invoices per call, even when more ids are supplied. |
| Fetch Receipts By IDs | `fetchReceiptsByIds` | Fetches full receipt records for a list of receipt ids. Moneybird returns at most 100 receipts per call, even when more ids are supplied. |
| Fetch Recurring Sales Invoices By IDs | `fetchRecurringSalesInvoicesByIds` | Returns the full recurring sales invoice records for a list of ids, for incremental synchronisation. Moneybird returns at most 100 records per call even when more ids are supplied. |
| Fetch Sales Invoices By IDs | `fetchSalesInvoicesByIds` | Returns the full sales invoice records for a list of sales invoice ids, for incremental synchronisation. Moneybird returns at most 100 invoices per call even when more ids are supplied. |
| Fetch Typeless Documents By IDs | `fetchTypelessDocumentsByIds` | Fetches full typeless document records for a list of document ids. Moneybird returns at most 100 documents per call, even when more ids are supplied. |
| Filter Contacts | `filterContacts` | Returns a paginated list of Moneybird contacts narrowed by structured filter terms, optionally combined with a free-text search. Filter terms are comma-separated key:value pairs, for example first_name:henk,contact_type:company. |
| Get Asset | `getAsset` | Returns a single fixed asset from a Moneybird administration, including its depreciation plan, current book value, value changes, funding sources and any disposal. |
| Get Assets Report | `getAssetsReport` | Returns the Moneybird assets report for an administration: the fixed assets with their purchase value, depreciation and book value over the requested period. |
| Get Balance Sheet Report | `getBalanceSheetReport` | Returns the Moneybird balance sheet for an administration: the debit side with current and non-current assets, and the credit side with equity, provisions and liabilities, at the end of the requested period. |
| Get Cash Flow Report | `getCashFlowReport` | Returns the Moneybird cash flow report for an administration: the cash received and cash paid per ledger account during the period, with the opening and closing balances. Can be narrowed to a single financial account. |
| Get Contact | `getContact` | Returns all information about a single Moneybird contact, including its notes, custom field values, contact people and event history. |
| Get Contact By Customer ID | `getContactByCustomerId` | Returns all information about a Moneybird contact looked up by its customer number rather than its internal id. |
| Get Contact Moneybird Payments Mandate | `getContactMoneybirdPaymentsMandate` | Returns the stored Moneybird Payments direct-debit mandate of a contact, including the masked bank or card details. Requires Moneybird Payments to be enabled for the administration; without that entitlement Moneybird answers HTTP 403. |
| Get Contact Person | `getContactPerson` | Returns all information about a single contact person belonging to a Moneybird contact. |
| Get Creditors Aging Report | `getCreditorsAgingReport` | Returns the Moneybird creditors aging report: the outstanding payable per contact split into aging buckets up to the requested date. |
| Get Creditors Report | `getCreditorsReport` | Returns the Moneybird creditors report: the outstanding payable amount per contact at the end of the requested period. |
| Get Customer Portal Invoices Link | `getCustomerPortalInvoicesLink` | Generates a temporary link straight to the invoices section of the Moneybird customer contact portal for one contact. The link expires after one hour. Moneybird answers with a bare quoted URL string rather than a JSON object. |
| Get Customer Portal Link | `getCustomerPortalLink` | Generates a temporary sign-in link to the Moneybird customer contact portal for one contact, letting them see their own documents without a Moneybird account. The link expires after one hour. Moneybird answers with a bare quoted URL string rather than a JSON object. |
| Get Customer Portal Subscription Link | `getCustomerPortalSubscriptionLink` | Generates a temporary link into the Moneybird customer contact portal for one online subscription sales link. The link expires after one hour. The identifier is the online sales link created with Create Subscription Template Sales Link, not a subscription id. Moneybird answers with a bare quoted URL string rather than a JSON object. |
| Get Debtors Aging Report | `getDebtorsAgingReport` | Returns the Moneybird debtors aging report: the outstanding receivable per contact split into aging buckets up to the requested date. |
| Get Debtors Report | `getDebtorsReport` | Returns the Moneybird debtors report: the outstanding receivable amount per contact at the end of the requested period. |
| Get Default Identity | `getDefaultIdentity` | Returns the identity Moneybird uses by default as the sender on outgoing documents for this administration. |
| Get Estimate | `getEstimate` | Returns all information about a single Moneybird estimate, including its lines, tax totals, notes, attachments and event history. |
| Get Estimate By Estimate Number | `getEstimateByEstimateNumber` | Returns a Moneybird estimate looked up by its human-readable estimate number rather than its internal id. Only works for estimates that have left draft and been assigned a number. |
| Get Expenses By Contact Report | `getExpensesByContactReport` | Returns the Moneybird expenses by contact report: the expenses booked against each contact during the requested period. |
| Get Expenses By Project Report | `getExpensesByProjectReport` | Returns the Moneybird expenses by project report: the expenses booked against each project during the requested period. |
| Get External Sales Invoice | `getExternalSalesInvoice` | Returns a single external sales invoice from a Moneybird administration, including its lines, tax totals, payments, notes, attachments and event history. |
| Get Financial Mutation | `getFinancialMutation` | Returns all information about a single Moneybird bank mutation, including the amount still unallocated and the payments and ledger bookings it is linked to. |
| Get General Document | `getGeneralDocument` | Returns a single general document from a Moneybird administration by its id, including its attachments, notes and event history. |
| Get General Journal Document | `getGeneralJournalDocument` | Returns all information about a single Moneybird general journal document, including its debit and credit lines, notes, attachments and event history. |
| Get General Ledger Report | `getGeneralLedgerReport` | Returns the Moneybird general ledger report for an administration: the debit and credit sums plus the start and final balance of every ledger account over the requested period. |
| Get Identity | `getIdentity` | Returns all information about a single Moneybird sender identity, including its address, contact details, bank details and custom field values. |
| Get Journal Entries Report | `getJournalEntriesReport` | Returns the Moneybird journal entries report: every booking in the period on the requested ledger account, contact or project. At least one of contact, project or ledger account is required, and an account type filter only works alongside a contact or project. The period may span at most one month. This report replaces the deprecated ledger account report. |
| Get Ledger Account | `getLedgerAccount` | Returns a single ledger account from a Moneybird administration, including its account type, general ledger code, allowed document types and RGS taxonomy classification. |
| Get Ledger Account Report | `getLedgerAccountReport` | Returns the bookings on a single Moneybird ledger account for the requested period. Moneybird has deprecated this endpoint in favour of the journal entries report; use Get Journal Entries Report with a ledger account id instead. |
| Get Payment | `getPayment` | Returns information about a single payment recorded in a Moneybird administration, including which document it settles, how much was paid and how it was booked. |
| Get Product | `getProduct` | Returns a single product from a Moneybird administration, including its price, currency, tax rate, ledger account and subscription frequency. |
| Get Product By Identifier | `getProductByIdentifier` | Returns a Moneybird product looked up by its identifier, the product code you assign, rather than by its internal id. Useful for keeping an external catalogue in step with Moneybird. |
| Get Profit And Loss Report | `getProfitLossReport` | Returns the Moneybird profit and loss report for an administration, broken down per ledger account. Each section lists one entry per ledger account with bookings in the period; parent amounts exclude their child accounts. Optionally restricted to a single project. |
| Get Project | `getProject` | Returns the name, state and budget of a single Moneybird project. |
| Get Purchase Invoice | `getPurchaseInvoice` | Returns a single purchase invoice from a Moneybird administration by its id, including its lines, payments, notes, attachments and event history. |
| Get Purchase Transaction | `getPurchaseTransaction` | Returns all information about a single Moneybird purchase transaction, including the amount, the account being paid and where the payment has got to. |
| Get Receipt | `getReceipt` | Returns a single receipt from a Moneybird administration by its id, including its lines, payments, notes, attachments and event history. |
| Get Recurring Sales Invoice | `getRecurringSalesInvoice` | Returns all information about a single Moneybird recurring sales invoice, including its lines, planning, notes and tax totals. |
| Get Revenue By Contact Report | `getRevenueByContactReport` | Returns the Moneybird revenue by contact report: the revenue booked against each contact during the requested period. |
| Get Revenue By Project Report | `getRevenueByProjectReport` | Returns the Moneybird revenue by project report: the revenue booked against each project during the requested period. |
| Get Sales Invoice | `getSalesInvoice` | Returns all information about a single Moneybird sales invoice, including its lines, tax totals, payments, notes, attachments and event history. |
| Get Sales Invoice By Invoice Number | `getSalesInvoiceByInvoiceNumber` | Returns a Moneybird sales invoice looked up by its human-readable invoice number rather than its internal id. Only works for invoices that have left draft and been assigned a number. |
| Get Sales Invoice By Reference | `getSalesInvoiceByReference` | Returns a Moneybird sales invoice looked up by the free-text reference stored on the invoice rather than by its internal id. |
| Get Subscription | `getSubscription` | Returns all information about a single Moneybird subscription, including the product it bills, its billing frequency and the recurring sales invoice that generates its invoices. |
| Get Subscription Template Checkout Identifier | `getSubscriptionTemplateCheckoutIdentifier` | Generates an online sales link for a Moneybird subscription template through the legacy checkout identifier endpoint, optionally pre-setting the contact, product and start date. Moneybird marks this endpoint as deprecated and has replaced it with Create Subscription Template Sales Link. |
| Get Subscriptions Report | `getSubscriptionsReport` | Returns the Moneybird subscriptions report: monthly recurring revenue, annual run rate, churn rate and customer lifetime value for the requested period. |
| Get Task | `getTask` | Returns a single Moneybird task list task, including its subtasks, notes and event history. |
| Get Task List | `getTaskList` | Returns a single Moneybird task list, including its groups, tasks and subtasks. |
| Get Task List Group | `getTaskListGroup` | Returns a single Moneybird task list group, including the tasks it contains. |
| Get Task List Template | `getTaskListTemplate` | Returns a single Moneybird task list template, including the groups and tasks it contains. |
| Get Tax Report | `getTaxReport` | Returns the Moneybird tax report for an administration: the taxable amount and the tax due per tax rate over the requested period, ready for a VAT return. |
| Get Time Entry | `getTimeEntry` | Returns all information about a single Moneybird time entry, including the contact, user, project and sales invoice it is linked to. |
| Get Typeless Document | `getTypelessDocument` | Returns a single typeless document from a Moneybird administration by its id, including its attachments and event history. |
| Get Verifications | `getVerifications` | Returns everything Moneybird has verified for an administration: the verified email addresses and bank account numbers, and the verified chamber of commerce and tax numbers. |
| Get Workflow | `getWorkflow` | Returns all information about a single Moneybird workflow, including its reminder and due-date steps. |
| Link Financial Mutation To Booking | `linkFinancialMutationToBooking` | Books a Moneybird bank mutation against a document, ledger account or payment batch, which is how bank transactions are reconciled. A mutation can be split across several bookings by calling this more than once with different amounts. |
| List Administrations | `listAdministrations` | Lists the Moneybird administrations the connected token can access. The administration id returned here is required by every other action in this connector. |
| List Assets | `listAssets` | Returns a paginated list of the fixed assets in a Moneybird administration, with each asset's purchase value, current book value, depreciation plan and value changes. Narrow the results by ledger account or to active assets only. |
| List Contact Additional Charges | `listContactAdditionalCharges` | Returns the additional charges queued on a contact, which Moneybird merges into an invoice at the start of the next period. By default only unbilled charges are returned; set Include Billed to also see charges that have already been invoiced. |
| List Contact Versions | `listContactVersions` | Returns the id and version of every contact in a Moneybird administration. Compare each version with the one stored locally and fetch only the changed contacts with Fetch Contacts By IDs. |
| List Contacts | `listContacts` | Returns a paginated list of the contacts in a Moneybird administration. Free-text search matches company name, contact people, email, phone, customer id, tax number and chamber of commerce number. |
| List Custom Fields | `listCustomFields` | Returns the custom fields defined in a Moneybird administration. A custom field adds extra information to an entity, and its source says which entity it applies to: sales_invoices, contact or identity. Custom fields are created in the Moneybird web app, not through the API. |
| List Document Styles | `listDocumentStyles` | Returns the document styles of a Moneybird administration. A document style holds the layout, logo, fonts and metadata blocks used when rendering invoices, estimates and other documents as PDF. Use the returned id wherever an action accepts a document style id. |
| List Downloads | `listDownloads` | Returns a paginated list of the export files Moneybird has prepared for an administration, such as audit files and contact, document or invoice exports. Only downloads the connected user is permitted to see are returned. |
| List Duplicate Contacts | `listDuplicateContacts` | Returns groups of Moneybird contacts that are considered possible duplicates of each other. Pages are sized by the total number of contacts across the groups, and a group is never split across two pages. |
| List Estimate Versions | `listEstimateVersions` | Returns the id and version number of every estimate in a Moneybird administration. Compare each version with the one stored locally and fetch only the changed estimates with Fetch Estimates By IDs. |
| List Estimates | `listEstimates` | Returns a paginated list of the estimates in a Moneybird administration. Use the filter parameter with comma-separated key:value terms, for example period:this_year,state:all, to narrow the results. Any filter supplied replaces the defaults entirely, so always include an explicit period when looking beyond the current financial year. |
| List External Sales Invoice Versions | `listExternalSalesInvoiceVersions` | Returns the id and version of every external sales invoice in a Moneybird administration. Compare each version with the one stored locally and fetch only the changed invoices with Fetch External Sales Invoices By IDs. |
| List External Sales Invoices | `listExternalSalesInvoices` | Returns a paginated list of the external sales invoices in a Moneybird administration. External sales invoices record revenue billed by another system, such as a webshop or point of sale. The filter parameter takes comma-separated key:value terms; the keys Moneybird honours here are state, period and contact_id, for example state:open,period:this_year. Unknown filter keys are silently ignored and return every invoice. |
| List Financial Accounts | `listFinancialAccounts` | Lists the active financial accounts of a Moneybird administration, such as bank and credit card accounts. Archived accounts are not returned. |
| List Financial Mutation Versions | `listFinancialMutationVersions` | Returns the id and version of every bank mutation in a Moneybird administration. Compare each version with the one stored locally and fetch only the changed mutations with Fetch Financial Mutations By IDs. |
| List Financial Mutations | `listFinancialMutations` | Returns a paginated list of the bank mutations in a Moneybird administration, each with the amount, counterparty, whether it has been processed and which payments or ledger bookings it is linked to. |
| List General Document IDs And Versions | `listGeneralDocumentIdsAndVersions` | Returns the id and version of every general document in a Moneybird administration. Compare each version with the one you have stored locally and fetch only the changed documents with Fetch General Documents By IDs. |
| List General Documents | `listGeneralDocuments` | Returns a paginated list of general documents in a Moneybird administration. General documents hold paperwork that is neither a purchase invoice nor a receipt, such as contracts and bank statements. Supports Moneybird's comma-separated key:value filter syntax, for example period:this_year,state:new. |
| List General Journal Document Versions | `listGeneralJournalDocumentVersions` | Returns the id and version of every general journal document in a Moneybird administration. Compare each version with the one stored locally and fetch only the changed documents with Fetch General Journal Documents By IDs. |
| List General Journal Documents | `listGeneralJournalDocuments` | Returns a paginated list of the general journal documents in a Moneybird administration - the manual double-entry bookings used for corrections, accruals and year-end entries. |
| List Identities | `listIdentities` | Lists the identities of a Moneybird administration. An identity is a sender profile - the company name, address, email and bank details printed on outgoing documents - and one administration can hold several. |
| List Ledger Accounts | `listLedgerAccounts` | Returns every ledger account in a Moneybird administration, the chart of accounts used to book revenue, costs, assets and liabilities. Moneybird does not paginate this endpoint, so the full chart is returned in one response. |
| List Products | `listProducts` | Returns a paginated list of the products in a Moneybird administration. Moneybird returns ten products per page by default. Narrow the results with a free-text query or by currency, ledger account, active state or checkout availability. |
| List Projects | `listProjects` | Returns a paginated list of the projects in a Moneybird administration. Only active projects are returned unless a filter says otherwise; use the filter parameter with comma-separated key:value terms such as state:archived or state:all. |
| List Purchase Invoice IDs And Versions | `listPurchaseInvoiceIdsAndVersions` | Returns the id and version of every purchase invoice in a Moneybird administration. Compare each version with the one you have stored locally and fetch only the changed invoices with Fetch Purchase Invoices By IDs. |
| List Purchase Invoices | `listPurchaseInvoices` | Returns a paginated list of purchase invoices in a Moneybird administration. Supports Moneybird's comma-separated key:value filter syntax, for example period:this_year,state:open. |
| List Purchase Transactions | `listPurchaseTransactions` | Lists the purchase transactions of a Moneybird administration - the outgoing payments prepared for suppliers, normally created by uploading a SEPA credit transfer file. |
| List Receipt IDs And Versions | `listReceiptIdsAndVersions` | Returns the id and version of every receipt in a Moneybird administration. Compare each version with the one you have stored locally and fetch only the changed receipts with Fetch Receipts By IDs. |
| List Receipts | `listReceipts` | Returns a paginated list of receipts in a Moneybird administration. Supports Moneybird's comma-separated key:value filter syntax, for example period:this_year,state:open. |
| List Recurring Sales Invoice Versions | `listRecurringSalesInvoiceVersions` | Returns the id and version number of every recurring sales invoice in a Moneybird administration. Compare each version with the one stored locally and fetch only the changed records with Fetch Recurring Sales Invoices By IDs. |
| List Recurring Sales Invoices | `listRecurringSalesInvoices` | Returns a paginated list of the recurring sales invoices in a Moneybird administration. Use the filter parameter with comma-separated key:value terms. The supported keys are state (active or inactive, defaulting to active), frequency (all, day, week, month, quarter or year), auto_send, contact_id and workflow_id. Any filter supplied replaces the defaults entirely, and Moneybird ignores terms whose key it does not recognise. |
| List Sales Invoice Versions | `listSalesInvoiceVersions` | Returns the id and version number of every sales invoice in a Moneybird administration. Compare each version with the one stored locally and fetch only the changed invoices with Fetch Sales Invoices By IDs. |
| List Sales Invoices | `listSalesInvoices` | Returns a paginated list of the sales invoices in a Moneybird administration. Use the filter parameter with comma-separated key:value terms, for example period:this_year,state:all, to narrow the results. |
| List Subscription Additional Charges | `listSubscriptionAdditionalCharges` | Returns the additional charges queued on a Moneybird subscription. By default only charges that have not been invoiced yet are returned; include billed charges to see the ones already put on an invoice. |
| List Subscription Templates | `listSubscriptionTemplates` | Returns a paginated list of the subscription templates in a Moneybird administration, up to 100 per page. Subscription templates are created in the Moneybird web app; the API only reads them and turns them into online sales links. |
| List Subscriptions | `listSubscriptions` | Lists the subscriptions of a single Moneybird contact, including subscriptions that have already been cancelled. Moneybird offers no endpoint that returns the subscriptions of every contact at once, so a contact is always required. |
| List Task List Templates | `listTaskListTemplates` | Returns every task list template in a Moneybird administration, with the groups each template contains. Templates are the blueprints new task lists are generated from. |
| List Task Lists | `listTaskLists` | Returns a paginated list of the task lists in a Moneybird administration, each with its groups and tasks. Task lists are the recurring bookkeeping checklists shown in Moneybird. |
| List Tax Rates | `listTaxRates` | Returns the tax rates available in a Moneybird administration, such as the 21 percent and 9 percent VAT rates used on sales and purchase documents. Use the filter parameter with comma-separated key:value terms, for example percentage:21,tax_rate_type:sales_invoice, to narrow the results. |
| List Time Entries | `listTimeEntries` | Returns a paginated list of the time entries in a Moneybird administration. Narrow the results with comma-separated key:value filter terms such as period:this_year, state:all, contact_id, project_id or user_id. The free-text query matches the linked contact and project rather than the entry description. |
| List Typeless Document IDs And Versions | `listTypelessDocumentIdsAndVersions` | Returns the id and version of every typeless document in a Moneybird administration. Compare each version with the one you have stored locally and fetch only the changed documents with Fetch Typeless Documents By IDs. |
| List Typeless Documents | `listTypelessDocuments` | Returns a paginated list of typeless documents in a Moneybird administration. Typeless documents are uploaded documents that have not yet been classified as a purchase invoice, receipt or general document. Supports Moneybird's comma-separated key:value filter syntax, for example state:new. |
| List Users | `listUsers` | Lists the users with access to a Moneybird administration. By default only regular active users are returned. The three inclusion flags are presence-based in Moneybird: supplying one at all turns that inclusion on, even when set to false, so leave a flag out entirely to keep those users excluded. |
| List Webhooks | `listWebhooks` | Lists the webhooks registered on a Moneybird administration, with the endpoint URL, subscribed events and the result of the most recent delivery attempt for each. |
| List Workflows | `listWorkflows` | Lists the invoice and estimate workflows of a Moneybird administration. A workflow controls the currency, language, payment methods and reminder schedule applied to a document. |
| Mark External Sales Invoice As Dubious | `markExternalSalesInvoiceAsDubious` | Marks an external sales invoice as dubious in a Moneybird administration, recording that the money is unlikely to be collected while keeping the invoice open. Supply the date the invoice became dubious. |
| Mark External Sales Invoice As Uncollectible | `markExternalSalesInvoiceAsUncollectible` | Writes an external sales invoice off as uncollectible in a Moneybird administration. Supply the date of the write-off, and optionally the book method that decides how the loss is booked. |
| Mark Sales Invoice As Dubious | `markSalesInvoiceAsDubious` | Marks an issued Moneybird sales invoice as dubious, flagging it as unlikely to be collected while keeping it open. |
| Mark Sales Invoice As Uncollectible | `markSalesInvoiceAsUncollectible` | Writes off an issued Moneybird sales invoice as uncollectible so the outstanding amount is removed from the receivables. |
| Pause Sales Invoice | `pauseSalesInvoice` | Pauses a Moneybird sales invoice so the automatic workflow steps, such as reminders, are not executed while it is paused. The invoice must already have been issued. |
| Register Credit Invoice Settlement | `registerCreditInvoiceSettlement` | Settles an issued Moneybird credit invoice against the sales invoice it credits, booking one payment on each document on the settlements ledger account using today's date and the full credit amount. Moneybird marks this endpoint as deprecated; prefer Create Sales Invoice Payment with the invoices settlement action for new integrations. |
| Register External Sales Invoice Payment | `createExternalSalesInvoicePayment` | Registers a payment against an external sales invoice in a Moneybird administration. Which extra field is required depends on the manual payment action: private payment and cash payment need a financial account, bank transfers need a financial mutation, balance settlement needs a ledger account, and invoices settlement needs the id of the document to settle against. |
| Register Purchase Invoice Payment (Deprecated) | `registerPurchaseInvoicePayment` | Registers a payment for a purchase invoice through Moneybird's legacy register_payment endpoint. Moneybird has deprecated this endpoint and returns an empty body; use Create Purchase Invoice Payment instead, which returns the created payment. |
| Register Receipt Payment (Deprecated) | `registerReceiptPayment` | Registers a payment for a receipt through Moneybird's legacy register_payment endpoint. Moneybird has deprecated this endpoint and returns an empty body; use Create Receipt Payment instead, which returns the created payment. |
| Register Sales Invoice Payment | `registerSalesInvoicePayment` | Registers a payment on a Moneybird sales invoice through the legacy register payment endpoint. Moneybird marks this endpoint as deprecated and has replaced it with Create Sales Invoice Payment, which should be used for new integrations. |
| Reopen Task | `reopenTask` | Reopens a completed Moneybird task list task, and reopens its parent tasks where they had been completed too. |
| Request Contact Moneybird Payments Mandate | `requestContactMoneybirdPaymentsMandate` | Emails the contact a request to authorise direct debit through Moneybird Payments. The contact must make a 15 cent verification payment to complete the mandate. This sends a real email to the contact, so only call it for a contact that expects it. Requires Moneybird Payments to be enabled; without that entitlement Moneybird answers HTTP 403. |
| Resume Sales Invoice | `resumeSalesInvoice` | Resumes a paused Moneybird sales invoice so its automatic workflow steps, such as reminders, are executed again. |
| Resume Time Entry | `resumeTimeEntry` | Resumes a stopped Moneybird time entry so its timer runs again. Any other running entry is stopped first. Only entries that started today can be resumed. |
| Send Estimate | `sendEstimate` | Issues a Moneybird estimate, moving it out of draft and assigning its estimate number. With the Email delivery method this DELIVERS THE ESTIMATE TO THE CUSTOMER; use the Manual delivery method to mark the estimate as sent without contacting anyone. When no arguments are supplied the defaults of the contact and workflow are used. |
| Send Sales Invoice | `sendSalesInvoice` | Issues a Moneybird sales invoice, moving it out of draft and assigning its invoice number. With the Email or Peppol delivery method this DELIVERS THE INVOICE TO THE CUSTOMER; use the Manual delivery method to mark the invoice as sent without contacting anyone. Sending can also be scheduled for a future invoice date. |
| Send Sales Invoice Reminders | `sendSalesInvoiceReminders` | Sends payment reminders to contacts for their outstanding Moneybird sales invoices. One reminder can cover several invoices of the same contact, and reminders are grouped by workflow, identity and document style. With the Email delivery method this DELIVERS THE REMINDER TO THE CUSTOMER; use Manual to record the reminder without contacting anyone. |
| Stop Time Entry | `stopTimeEntry` | Stops a running Moneybird time entry and sets its end time to now. An entry that is already stopped is returned unchanged. |
| Unassign Task | `unassignTask` | Removes the current assignment from a Moneybird task list task, leaving it unassigned. |
| Unlink Financial Mutation Booking | `unlinkFinancialMutationBooking` | Removes a booking from a Moneybird bank mutation, returning the allocated amount to the mutation's open balance so it can be reconciled differently. |
| Update Asset | `updateAsset` | Updates a fixed asset in a Moneybird administration. Once the asset is active, meaning its purchase date has passed, Moneybird only allows the name to be changed; the other fields can be edited while the purchase date is still in the future. |
| Update Contact | `updateContact` | Updates an existing Moneybird contact. Only the fields supplied inside the contact envelope are changed; omitted fields keep their current values. |
| Update Contact Person | `updateContactPerson` | Updates a contact person on a Moneybird contact. Only the fields supplied inside the contact person envelope are changed. |
| Update Default Identity | `updateDefaultIdentity` | Updates the administration's default sender identity - the company details printed on outgoing documents. Only the fields supplied inside the envelope are changed. Unlike an additional identity, the default one also carries the legal entity type and chamber of commerce number. |
| Update Estimate | `updateEstimate` | Updates a Moneybird estimate. Only the fields supplied inside the envelope are changed. Estimate lines are edited by passing details with an existing line id, added by passing a line without an id, and removed by passing an existing line id together with destroy set to true. Note that Moneybird keeps the language an estimate was created with, so supplying a different language here has no effect. |
| Update External Sales Invoice | `updateExternalSalesInvoice` | Updates an external sales invoice in a Moneybird administration. Only the fields supplied inside the envelope are changed. Invoice lines are edited by passing details attributes with an existing line id, added by passing a line without an id, and removed by passing an existing line id together with destroy set to true. |
| Update Financial Statement | `updateFinancialStatement` | Updates a Moneybird financial statement. Only the fields supplied inside the envelope are changed. Bank mutations already in the statement can be edited by including their id, and new ones can be added. |
| Update General Document | `updateGeneralDocument` | Updates an existing general document in a Moneybird administration. Only the fields supplied are changed. Set Remove Contact to true to unlink the contact currently attached to the document. Moneybird's documented reminder fields are not exposed: the nested reminder object returns HTTP 500 and reminder_date is silently discarded, both reproduced directly against the Moneybird API. |
| Update General Journal Document | `updateGeneralJournalDocument` | Updates a Moneybird general journal document. Only the fields supplied inside the envelope are changed. Existing lines are edited by including their id, new lines are added by leaving the id out, and a line is removed by sending its id together with destroy set to true. The entry must still balance after the change. |
| Update Identity | `updateIdentity` | Updates an additional Moneybird sender identity. Only the fields supplied inside the envelope are changed. Use Update Default Identity for the administration's own default sender. |
| Update Ledger Account | `updateLedgerAccount` | Updates a ledger account in a Moneybird administration. Only the fields supplied inside the ledger account envelope are changed; omitted fields keep their current values. Supply an RGS code to reclassify the account under a different taxonomy item. |
| Update Product | `updateProduct` | Updates a product in a Moneybird administration. Only the fields supplied inside the product envelope are changed; omitted fields keep their current values. |
| Update Project | `updateProject` | Updates the name or budget of a Moneybird project. The name must stay unique within the administration. Requires the connected user to have permission to the administration settings. |
| Update Purchase Invoice | `updatePurchaseInvoice` | Updates an existing purchase invoice in a Moneybird administration. Only the fields supplied are changed. Supply an invoice line with its id to change it, with Remove Line set to true to delete it, or without an id to add a new line. |
| Update Receipt | `updateReceipt` | Updates an existing receipt in a Moneybird administration. Only the fields supplied are changed. Supply a receipt line with its id to change it, with Remove Line set to true to delete it, or without an id to add a new line. |
| Update Recurring Sales Invoice | `updateRecurringSalesInvoice` | Updates a Moneybird recurring sales invoice. Only the fields supplied inside the envelope are changed. Invoice lines are edited by passing details with an existing line id, added by passing a line without an id, and removed by passing an existing line id together with destroy set to true. Enabling merging here currently makes Moneybird answer with a server error instead of its validation message, so set merging when creating the recurring invoice, together with automatic sending. |
| Update Sales Invoice | `updateSalesInvoice` | Updates a Moneybird sales invoice. Only the fields supplied inside the envelope are changed. Invoice lines are edited by passing details with an existing line id, added by passing a line without an id, and removed by passing an existing line id together with destroy set to true. |
| Update Subscription | `updateSubscription` | Updates a Moneybird subscription, most commonly to move the contact to a different product. Moneybird works out the price difference and creates a one-off sales invoice for the extra charge over the remaining billing period. Only the fields supplied inside the envelope are changed, with one exception: Moneybird resets the discount to zero on every update that does not include it, so always send the current discount along with any other change. |
| Update Task | `updateTask` | Updates a Moneybird task list task. Only the fields supplied inside the envelope are changed. |
| Update Task List | `updateTaskList` | Updates the name, description or deadline of a Moneybird task list. Only the fields supplied inside the envelope are changed. |
| Update Task List Group | `updateTaskListGroup` | Updates the name or report type of a Moneybird task list group. Changing the report type destroys every task in the group and generates new tasks from the new report. |
| Update Task List Template | `updateTaskListTemplate` | Updates a Moneybird task list template. Only the fields supplied inside the envelope are changed. |
| Update Time Entry | `updateTimeEntry` | Updates a Moneybird time entry. Only the fields supplied inside the envelope are changed. Start and end times are rounded down to whole minutes with a minimum of one minute between them. |
| Upload SEPA Credit Transfer File | `uploadSepaCreditTransferFile` | Uploads a SEPA credit transfer (pain.001) file to Moneybird, which turns it into purchase transaction batches ready to be paid. Requires the SEPA credit transfer feature to be enabled on the administration. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Access Token Created | `access_token_created` | Fires when an API access token is created for the administration. |
| Administration Activated | `administration_activated` | Fires when the administration is activated. |
| Administration Automatic Bookers Activated | `administration_automatic_bookers_activated` | Fires when automatic bookers are activated. |
| Administration Automatic Bookers Deactivated | `administration_automatic_bookers_deactivated` | Fires when automatic bookers are deactivated. |
| Administration Deleted | `administration_deleted` | Fires when the administration is deleted. |
| Administration ID Verified For Banking Authorization Requirement Activated | `administration_id_verified_for_banking_authorization_requirement_activated` | Fires when the administration's identity verification for banking authorisation is activated. |
| Administration Legacy Tax Number Updated | `administration_legacy_tax_number_updated` | Fires when the administration's legacy tax number changes. |
| Administration Moneybird Banking Tax Information Sent | `administration_moneybird_banking_tax_information_sent` | Fires when banking tax information is sent. |
| Administration Moneybird Payments Activated | `administration_moneybird_payments_activated` | Fires when Moneybird Payments is activated for the administration. |
| Administration Payments Without Proof Activated | `administration_payments_without_proof_activated` | Fires when payments without proof are activated. |
| Administration Payments Without Proof Deactivated | `administration_payments_without_proof_deactivated` | Fires when payments without proof are deactivated. |
| Adyen Banking Bank Transfer Permission Created | `adyen_banking_bank_transfer_permission_created` | Fires when an Adyen banking transfer permission is created. |
| Adyen Payment Instrument Activated | `adyen_payment_instrument_activated` | Fires when an Adyen payment instrument is activated. |
| Adyen Payment Instrument Created | `adyen_payment_instrument_created` | Fires when an Adyen payment instrument is created. |
| Adyen Payment Instrument Network Token Created | `adyen_payment_instrument_network_token_created` | Fires when an Adyen network token is created. |
| Adyen Payment Instrument Network Token Updated | `adyen_payment_instrument_network_token_updated` | Fires when an Adyen network token is changed. |
| Adyen Payment Instrument Updated | `adyen_payment_instrument_updated` | Fires when an Adyen payment instrument is changed. |
| Booking Rule Created | `booking_rule_created` | Fires when a booking rule is created. |
| Booking Rule Destroyed | `booking_rule_destroyed` | Fires when a booking rule is removed. |
| Booking Rule Updated | `booking_rule_updated` | Fires when a booking rule is changed. |
| Company Asset Arbitrary Value Change Created | `company_assets_value_changes_arbitrary_created` | Fires when an arbitrary asset value change is created. |
| Company Asset Arbitrary Value Change Destroyed | `company_assets_value_changes_arbitrary_destroyed` | Fires when an arbitrary asset value change is removed. |
| Company Asset Created | `company_assets_asset_created` | Fires when a company asset is created. |
| Company Asset Destroyed | `company_assets_asset_destroyed` | Fires when a company asset is removed. |
| Company Asset Disposal Created | `company_assets_disposal_created` | Fires when a company asset disposal is created. |
| Company Asset Disposal Destroyed | `company_assets_disposal_destroyed` | Fires when a company asset disposal is removed. |
| Company Asset Divestment Value Change Created | `company_assets_value_changes_divestment_created` | Fires when a divestment value change is created. |
| Company Asset Divestment Value Change Destroyed | `company_assets_value_changes_divestment_destroyed` | Fires when a divestment value change is removed. |
| Company Asset Full Depreciation Created | `company_assets_value_changes_full_depreciation_created` | Fires when a full depreciation value change is created. |
| Company Asset Full Depreciation Destroyed | `company_assets_value_changes_full_depreciation_destroyed` | Fires when a full depreciation value change is removed. |
| Company Asset Linear Value Change Created | `company_assets_value_changes_linear_created` | Fires when a linear value change is created. |
| Company Asset Linear Value Change Destroyed | `company_assets_value_changes_linear_destroyed` | Fires when a linear value change is removed. |
| Company Asset Manual Value Change Created | `company_assets_value_changes_manual_created` | Fires when a manual value change is created. |
| Company Asset Manual Value Change Destroyed | `company_assets_value_changes_manual_destroyed` | Fires when a manual value change is removed. |
| Company Asset Source Created | `company_assets_source_created` | Fires when a company asset source is created. |
| Company Asset Source Destroyed | `company_assets_source_destroyed` | Fires when a company asset source is removed. |
| Company Asset Updated | `company_assets_asset_updated` | Fires when a company asset is changed. |
| Company Asset Value Change Plan Activated | `company_assets_value_change_plan_activated` | Fires when an asset value change plan is activated. |
| Company Asset Value Change Plan Created | `company_assets_value_change_plan_created` | Fires when an asset value change plan is created. |
| Company Asset Value Change Plan Deactivated | `company_assets_value_change_plan_deactivated` | Fires when an asset value change plan is deactivated. |
| Company Asset Value Change Plan Destroyed | `company_assets_value_change_plan_destroyed` | Fires when an asset value change plan is removed. |
| Company Asset Value Change Plan Updated | `company_assets_value_change_plan_updated` | Fires when an asset value change plan is changed. |
| Contact Activated | `contact_activated` | Fires when Moneybird records the contact_activated event. Same uniform envelope; entity holds the full contact. |
| Contact Archived | `contact_archived` | Fires when Moneybird records the contact_archived event. Same uniform envelope; entity holds the full contact. |
| Contact Created | `contact_created` | Fires when Moneybird records the contact_created event. Delivery envelope: administration_id, webhook_id, webhook_token, entity_type, entity_id, state, action (this event name) and entity (the full record). |
| Contact Destroyed | `contact_destroyed` | Fires when Moneybird records the contact_destroyed event. Same uniform envelope; entity holds the contact as it was before deletion. |
| Contact Mandate Destroyed | `contact_mandate_destroyed` | Fires when Moneybird records the contact_mandate_destroyed event. |
| Contact Mandate Request Failed | `contact_mandate_request_failed` | Fires when Moneybird records the contact_mandate_request_failed event. |
| Contact Person Created | `contact_person_created` | Fires when Moneybird records the contact_person_created event. |
| Contact Person Destroyed | `contact_person_destroyed` | Fires when Moneybird records the contact_person_destroyed event. |
| Contact Person Updated | `contact_person_updated` | Fires when Moneybird records the contact_person_updated event. |
| Contact Updated | `contact_updated` | Fires when Moneybird records the contact_updated event. Same uniform envelope as every Moneybird delivery; action carries this event name and entity holds the full contact. |
| Default Identity Updated | `default_identity_updated` | Fires when the administration's default identity changes. |
| Default Tax Rate Created | `default_tax_rate_created` | Fires when a default tax rate is created. |
| Direct Bank Link Activated | `direct_bank_link_activated` | Fires when a direct bank link is activated. |
| Direct Debit Incoming Mandate Created | `direct_debit_incoming_mandate_created` | Fires when an incoming direct debit mandate is created. |
| Direct Debit Incoming Mandate Updated | `direct_debit_incoming_mandate_updated` | Fires when an incoming direct debit mandate is changed. |
| Direct Debit Transaction Created | `direct_debit_transaction_created` | Fires when a direct debit transaction is created. |
| Direct Debit Transaction Deleted | `direct_debit_transaction_deleted` | Fires when a direct debit transaction is deleted. |
| Document Destroyed | `document_destroyed` | Fires when Moneybird records the document_destroyed event. |
| Document Style Created | `document_style_created` | Fires when Moneybird records the document_style_created event. |
| Document Style Destroyed | `document_style_destroyed` | Fires when Moneybird records the document_style_destroyed event. |
| Document Style Updated | `document_style_updated` | Fires when Moneybird records the document_style_updated event. |
| Document Updated | `document_updated` | Fires when Moneybird records the document_updated event. |
| Email Domain Deactivated | `email_domain_deactivated` | Fires when a sending email domain is deactivated. |
| Estimate Created | `estimate_created` | Fires when Moneybird records the estimate_created event. |
| Estimate Destroyed | `estimate_destroyed` | Fires when Moneybird records the estimate_destroyed event. |
| Estimate Mark Accepted | `estimate_mark_accepted` | Fires when an estimate is marked accepted. |
| Estimate Mark Archived | `estimate_mark_archived` | Fires when an estimate is archived. |
| Estimate Mark Billed | `estimate_mark_billed` | Fires when an estimate is marked billed. |
| Estimate Mark Rejected | `estimate_mark_rejected` | Fires when an estimate is marked rejected. |
| Estimate State Changed | `estimate_state_changed` | Fires on any estimate state change. The state field carries the new state. |
| Estimate State Changed To Late | `estimate_state_changed_to_late` | Fires when an estimate becomes late. |
| Estimate State Changed To Open | `estimate_state_changed_to_open` | Fires when an estimate becomes open. |
| Estimate Updated | `estimate_updated` | Fires when Moneybird records the estimate_updated event. |
| External Sales Invoice Created | `external_sales_invoice_created` | Fires when Moneybird records the external_sales_invoice_created event. |
| External Sales Invoice Destroyed | `external_sales_invoice_destroyed` | Fires when Moneybird records the external_sales_invoice_destroyed event. |
| External Sales Invoice Marked As Uncollectible | `external_sales_invoice_marked_as_uncollectible` | Fires when an external sales invoice is written off as uncollectible. |
| External Sales Invoice State Changed | `external_sales_invoice_state_changed` | Fires on any external sales invoice state change. |
| External Sales Invoice State Changed To Paid | `external_sales_invoice_state_changed_to_paid` | Fires when an external sales invoice is fully paid. |
| External Sales Invoice Updated | `external_sales_invoice_updated` | Fires when Moneybird records the external_sales_invoice_updated event. |
| Financial Account Activated | `financial_account_activated` | Fires when a financial account is activated. |
| Financial Account Bank Link Created | `financial_account_bank_link_created` | Fires when a bank link is created on a financial account. |
| Financial Account Bank Link Destroyed | `financial_account_bank_link_destroyed` | Fires when a bank link on a financial account is removed. |
| Financial Account Bank Link Updated | `financial_account_bank_link_updated` | Fires when a bank link on a financial account is changed. |
| Financial Account Created | `financial_account_created` | Fires when a financial account is created. |
| Financial Account Deactivated | `financial_account_deactivated` | Fires when a financial account is deactivated. |
| Financial Account Destroyed | `financial_account_destroyed` | Fires when a financial account is removed. |
| Financial Statement Created | `financial_statement_created` | Fires when a financial statement is imported or created. |
| Financial Statement Destroyed | `financial_statement_destroyed` | Fires when a financial statement is removed. |
| Financial Statement Updated | `financial_statement_updated` | Fires when a financial statement is changed. |
| Goal Completed | `goal_completed` | Fires when a goal is completed. |
| Identity Created | `identity_created` | Fires when an identity is created. |
| Identity Destroyed | `identity_destroyed` | Fires when an identity is removed. |
| Identity Updated | `identity_updated` | Fires when an identity is changed. |
| Ledger Account Activated | `ledger_account_activated` | Fires when a ledger account is activated. |
| Ledger Account Booking Created | `ledger_account_booking_created` | Fires when a booking is made on a ledger account. |
| Ledger Account Booking Destroyed | `ledger_account_booking_destroyed` | Fires when a ledger account booking is removed. |
| Ledger Account Created | `ledger_account_created` | Fires when a ledger account is created. |
| Ledger Account Deactivated | `ledger_account_deactivated` | Fires when a ledger account is deactivated. |
| Ledger Account Destroyed | `ledger_account_destroyed` | Fires when a ledger account is removed. |
| Ledger Account Updated | `ledger_account_updated` | Fires when a ledger account is changed. |
| Legal Terms Acceptation Created | `legal_terms_acceptation_created` | Fires when legal terms acceptance is recorded. |
| Legal Terms Acceptation Destroyed | `legal_terms_acceptation_destroyed` | Fires when legal terms acceptance is removed. |
| Legal Terms Acceptation Email Delivery Failed | `legal_terms_acceptation_email_delivery_failed` | Fires when a legal terms acceptance email fails to deliver. |
| Legal Terms Acceptation Email Sent | `legal_terms_acceptation_email_sent` | Fires when a legal terms acceptance email is sent. |
| Legal Terms Acceptation Updated | `legal_terms_acceptation_updated` | Fires when legal terms acceptance is changed. |
| Mobile App Authentication Factor Created | `mobile_app_authentication_factor_created` | Fires when a mobile app authentication factor is created. |
| Mobile App Authentication Factor Destroyed | `mobile_app_authentication_factor_destroyed` | Fires when a mobile app authentication factor is removed. |
| Mobile App Authentication Factor Updated | `mobile_app_authentication_factor_updated` | Fires when a mobile app authentication factor is changed. |
| Mollie Credential Created | `mollie_credential_created` | Fires when a Mollie credential is connected. |
| Mollie Credential Destroyed | `mollie_credential_destroyed` | Fires when a Mollie credential is removed. |
| Moneybird Banking Transfer Completed | `moneybird_banking_transfer_completed` | Fires when a Moneybird Banking transfer completes. |
| Moneybird Banking Transfer Failed | `moneybird_banking_transfer_failed` | Fires when a Moneybird Banking transfer fails. |
| Note Created | `note_created` | Fires when a note is added to a record. |
| Note Destroyed | `note_destroyed` | Fires when a note is removed. |
| Order Created | `order_created` | Fires when an order is created. |
| Payment Destroyed | `payment_destroyed` | Fires when a payment is removed. |
| Payment Method Limit Updated | `payment_method_limit_updated` | Fires when a payment method limit is changed. |
| Payment Registered | `payment_registered` | Fires when a payment is registered against a document. |
| Payment Transaction Batch Created | `payment_transaction_batch_created` | Fires when a payment transaction batch is created. |
| Payment Transaction Paid | `payment_transaction_paid` | Fires when a payment transaction is paid. |
| Payment Transaction Rejected | `payment_transaction_rejected` | Fires when a payment transaction is rejected. |
| Personal IBAN Created | `personal_iban_created` | Fires when a personal IBAN is added. |
| Personal IBAN Destroyed | `personal_iban_destroyed` | Fires when a personal IBAN is removed. |
| Personal IBAN Updated | `personal_iban_updated` | Fires when a personal IBAN is changed. |
| Ponto Direct Bank Link Activated | `ponto_direct_bank_link_activated` | Fires when a Ponto direct bank link is activated. |
| Product Activated | `product_activated` | Fires when a product is activated. |
| Product Created | `product_created` | Fires when a product is created. |
| Product Deactivated | `product_deactivated` | Fires when a product is deactivated. |
| Product Destroyed | `product_destroyed` | Fires when a product is removed. |
| Product Updated | `product_updated` | Fires when a product is changed. |
| Project Activated | `project_activated` | Fires when a project is activated. |
| Project Archived | `project_archived` | Fires when a project is archived. |
| Project Created | `project_created` | Fires when a project is created. |
| Project Destroyed | `project_destroyed` | Fires when a project is removed. |
| Project Updated | `project_updated` | Fires when a project is changed. |
| Purchase Transaction Batch Created | `purchase_transaction_batch_created` | Fires when a purchase transaction batch is created. |
| Purchase Transaction Created | `purchase_transaction_created` | Fires when a purchase transaction is created. |
| Purchase Transaction Deleted | `purchase_transaction_deleted` | Fires when a purchase transaction is deleted. |
| Purchase Transaction Paid | `purchase_transaction_paid` | Fires when a purchase transaction is paid. |
| Purchase Transaction Rejected | `purchase_transaction_rejected` | Fires when a purchase transaction is rejected. |
| Recurring Sales Invoice Created | `recurring_sales_invoice_created` | Fires when Moneybird records the recurring_sales_invoice_created event. |
| Recurring Sales Invoice Deactivated | `recurring_sales_invoice_deactivated` | Fires when a recurring sales invoice is deactivated. |
| Recurring Sales Invoice Destroyed | `recurring_sales_invoice_destroyed` | Fires when Moneybird records the recurring_sales_invoice_destroyed event. |
| Recurring Sales Invoice Invoice Created | `recurring_sales_invoice_invoice_created` | Fires when a recurring sales invoice produces a new invoice. |
| Recurring Sales Invoice Updated | `recurring_sales_invoice_updated` | Fires when Moneybird records the recurring_sales_invoice_updated event. |
| Sales Invoice Created | `sales_invoice_created` | Fires when Moneybird records the sales_invoice_created event. Same uniform envelope; entity holds the full sales invoice. |
| Sales Invoice Destroyed | `sales_invoice_destroyed` | Fires when Moneybird records the sales_invoice_destroyed event. |
| Sales Invoice Marked As Uncollectible | `sales_invoice_marked_as_uncollectible` | Fires when a sales invoice is written off as uncollectible. |
| Sales Invoice State Changed | `sales_invoice_state_changed` | Fires on any sales invoice state change. The state field carries the new state. |
| Sales Invoice State Changed To Late | `sales_invoice_state_changed_to_late` | Fires when a sales invoice becomes late. |
| Sales Invoice State Changed To Open | `sales_invoice_state_changed_to_open` | Fires when a sales invoice becomes open. |
| Sales Invoice State Changed To Paid | `sales_invoice_state_changed_to_paid` | Fires when a sales invoice is fully paid. |
| Sales Invoice State Changed To Pending Payment | `sales_invoice_state_changed_to_pending_payment` | Fires when a sales invoice moves to pending payment. |
| Sales Invoice State Changed To Reminded | `sales_invoice_state_changed_to_reminded` | Fires when a payment reminder has been sent for a sales invoice. |
| Sales Invoice State Changed To Scheduled | `sales_invoice_state_changed_to_scheduled` | Fires when a sales invoice is scheduled for sending. |
| Sales Invoice Updated | `sales_invoice_updated` | Fires when Moneybird records the sales_invoice_updated event. |
| SEPA Direct Debit Limit Updated | `sepa_direct_debit_limit_updated` | Fires when the SEPA direct debit limit changes. |
| Smart Transfer Rule Created | `smart_transfer_rule_created` | Fires when a smart transfer rule is created. |
| Smart Transfer Rule Updated | `smart_transfer_rule_updated` | Fires when a smart transfer rule is changed. |
| Smart Transfer Trigger Created | `smart_transfer_trigger_created` | Fires when a smart transfer trigger is created. |
| Smart Transfer Trigger Updated | `smart_transfer_trigger_updated` | Fires when a smart transfer trigger is changed. |
| Subgoal Completed | `subgoal_completed` | Fires when a subgoal is completed. |
| Subscription Created | `subscription_created` | Fires when a subscription is created. |
| Subscription Destroyed | `subscription_destroyed` | Fires when a subscription is removed. |
| Subscription Template Activated | `subscription_template_activated` | Fires when a subscription template is activated. |
| Subscription Template Created | `subscription_template_created` | Fires when a subscription template is created. |
| Subscription Template Deactivated | `subscription_template_deactivated` | Fires when a subscription template is deactivated. |
| Subscription Template Destroyed | `subscription_template_destroyed` | Fires when a subscription template is removed. |
| Subscription Template Updated | `subscription_template_updated` | Fires when a subscription template is changed. |
| Subscription Updated | `subscription_updated` | Fires when a subscription is changed. |
| Task Category Linked | `task_lists_task_category_linked` | Fires when a task is linked to a category. |
| Task Completed | `task_lists_task_completed` | Fires when a task is completed. |
| Task Created | `task_lists_task_created` | Fires when a task is created. |
| Task Destroyed | `task_lists_task_destroyed` | Fires when a task is removed. |
| Task List Completed | `task_lists_list_completed` | Fires when a task list is completed. |
| Task List Created | `task_lists_list_created` | Fires when a task list is created. |
| Task List Destroyed | `task_lists_list_destroyed` | Fires when a task list is removed. |
| Task List Template Created | `task_lists_list_template_created` | Fires when a task list template is created. |
| Task List Template Destroyed | `task_lists_list_template_destroyed` | Fires when a task list template is removed. |
| Task List Template Updated | `task_lists_list_template_updated` | Fires when a task list template is changed. |
| Task List Updated | `task_lists_list_updated` | Fires when a task list is changed. |
| Task Report Type Linked | `task_lists_task_report_type_linked` | Fires when a task is linked to a report type. |
| Task Unlinked | `task_lists_task_unlinked` | Fires when a task link is removed. |
| Task Updated | `task_lists_task_updated` | Fires when a task is changed. |
| Tax Rate Activated | `tax_rate_activated` | Fires when a tax rate is activated. |
| Tax Rate Created | `tax_rate_created` | Fires when a tax rate is created. |
| Tax Rate Deactivated | `tax_rate_deactivated` | Fires when a tax rate is deactivated. |
| Tax Rate Destroyed | `tax_rate_destroyed` | Fires when a tax rate is removed. |
| Tax Rate Updated | `tax_rate_updated` | Fires when a tax rate is changed. |
| Time Entry Created | `time_entry_created` | Fires when a time entry is created. |
| Time Entry Destroyed | `time_entry_destroyed` | Fires when a time entry is removed. |
| Time Entry Sales Invoice Created | `time_entry_sales_invoice_created` | Fires when a sales invoice is created from time entries. |
| Time Entry Updated | `time_entry_updated` | Fires when a time entry is changed. |
| Todo Completed | `todo_completed` | Fires when a todo is completed. |
| Todo Created | `todo_created` | Fires when a todo is created. |
| Todo Destroyed | `todo_destroyed` | Fires when a todo is removed. |
| Todo Opened | `todo_opened` | Fires when a todo is reopened. |
| Ultimate Beneficial Owner Created | `ultimate_benificial_owner_created` | Fires when an ultimate beneficial owner is recorded. Note that Moneybird spells the event name 'benificial'. |
| Ultimate Beneficial Owner Updated | `ultimate_benificial_owner_updated` | Fires when an ultimate beneficial owner is changed. Note that Moneybird spells the event name 'benificial'. |
| Verification Destroyed | `verification_destroyed` | Fires when a verification is removed. |
| Workflow Created | `workflow_created` | Fires when a workflow is created. |
| Workflow Deactivated | `workflow_deactivated` | Fires when a workflow is deactivated. |
| Workflow Destroyed | `workflow_destroyed` | Fires when a workflow is removed. |
| Workflow Updated | `workflow_updated` | Fires when a workflow is changed. |
