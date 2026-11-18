---
description: "SignWell is an electronic signature platform for sending, tracking and completing legally binding documents."
hidden: true
---

# SignWell

<img src="../../.gitbook/assets/connectors/lg/signwell.png" alt="SignWell logo">

SignWell is an electronic signature platform for sending, tracking and completing legally binding documents. This connector covers the SignWell v1 API: documents and document creation from files or templates, recipient and authentication updates, sending and reminders, completed PDF retrieval, document templates, bulk sends with CSV validation, API applications, webhooks and the connected account's credentials.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [signwell.com](https://signwell.com) |
| **Authentication** | API key |
| **Slug** | `signwell` |

## Use it

Add SignWell from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.signwell.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Bulk Send | `createBulkSend` | Sends one or more templates to many recipients at once, creating a separate document per row of the supplied CSV. Validate the CSV first with Validate Bulk Send CSV. |
| Create Document | `createDocument` | Creates a signature document from one or more files and sends it to the listed recipients. Set draft to true to create the document without sending it, and test_mode to true to create a free, non-binding test document. |
| Create Document from Template | `createDocumentFromTemplate` | Creates a signature document from an existing document template, filling its placeholder roles with real recipients and its fields with supplied values. Set draft to true to create the document without sending it. |
| Create Template | `createTemplate` | Creates a reusable document template from one or more files, defining the placeholder roles that real recipients are mapped onto when a document is created from it. |
| Create Webhook | `createWebhook` | Registers a callback URL that SignWell posts every document event to, such as when a document is viewed, signed, completed or declined. |
| Delete API Application | `deleteApiApplication` | Permanently deletes an API Application. Documents already created under it keep their branding, but no new documents can reference it. |
| Delete Document | `deleteDocument` | Permanently deletes a document and cancels any outstanding signature requests for it. |
| Delete Template | `deleteTemplate` | Permanently deletes a document template. Documents already created from the template are not affected. |
| Delete Webhook | `deleteWebhook` | Removes a registered webhook callback endpoint so SignWell stops posting events to it. |
| Get API Application | `getApiApplication` | Retrieves an API Application by its unique identifier. API Applications hold the branding and sender settings applied to documents created under them. |
| Get Bulk Send | `getBulkSend` | Retrieves a single bulk send by its unique identifier, including its processing status and how many documents it produced. |
| Get Bulk Send CSV Template | `getBulkSendCsvTemplate` | Generates a blank CSV whose columns match the placeholders and fields of the chosen templates. Fill one row per recipient and feed it back to Validate Bulk Send CSV and Create Bulk Send. |
| Get Bulk Send Documents | `getBulkSendDocuments` | Lists the documents that a bulk send produced, one per row of the uploaded CSV, with each document's signing status. |
| Get Completed PDF | `getCompletedPdf` | Retrieves the finished, signed document. Set url_only to true to receive a temporary download link instead of the file itself, which is the recommended way to fetch the PDF. |
| Get Credentials | `getCredentials` | Retrieves the SignWell user, account, workspace and contact that the API key belongs to, including the plan tier and what the account is entitled to create. |
| Get Document | `getDocument` | Retrieves a document and all of its associated data by its unique identifier, including every recipient with its delivery method and signing status, the uploaded files and the placed fields. |
| Get Template | `getTemplate` | Retrieves a document template and all of its associated data by its unique identifier, including its placeholder roles, files and field layout. |
| List Bulk Sends | `listBulkSends` | Lists the bulk sends on the account, each of which dispatched one template to many recipients from a CSV file. |
| List Contacts | `listContacts` | Lists the saved contacts on the account, which can be reused as document recipients. |
| List Documents | `listDocuments` | Lists the documents in the account with their recipients, files and signing status, using page-based pagination. SignWell throttles this API to 5 requests every 30 seconds. |
| List Templates | `listTemplates` | Lists the document templates in the account with their placeholder roles, using page-based pagination. |
| List Users | `listUsers` | Lists the users who belong to the SignWell account, with their roles and archived state. |
| List Webhooks | `listWebhooks` | Lists the webhook callback endpoints registered on the account. Each endpoint receives every SignWell event as a POST. |
| Send Reminder | `sendReminder` | Sends a signing reminder to the recipients of a document who have not yet completed it. SignWell allows one manual reminder per document per day. |
| Update and Send Document | `updateAndSendDocument` | Applies any final changes to a draft document and sends the signature request to its recipients. Only documents still in draft can be sent this way, and sending is irreversible. |
| Update Authentication | `updateAuthentication` | Updates the passcode authentication applied to recipients of a document, so signers must enter a code before they can open it. |
| Update Recipients | `updateRecipients` | Corrects the name, email address or phone number of recipients on a document that has already been sent, and reissues their signing request. |
| Update Template | `updateTemplate` | Updates a document template's settings. Only the fields supplied are changed, so the template can be renamed, taken out of draft or have its signing options adjusted independently. |
| Validate Bulk Send CSV | `validateBulkSendCsv` | Checks a filled-in bulk send CSV against the chosen templates and reports any row or column errors, without creating any documents. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Document Bounced | `document_bounced` | Fires when the signature request email to a recipient bounces, so the document will never reach that signer. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document Canceled | `document_canceled` | Fires when the sender cancels a document. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document Completed | `document_completed` | Fires when every recipient has signed and the document is complete. This is the event to bind when you want the finished PDF. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document Created | `document_created` | Fires when a document is created in SignWell. Registration is automatic: fastn calls SignWell's Create Webhook endpoint (POST /api/v1/hooks) with this trigger's URL. SignWell posts every event type to that one URL, so fastn routes on the payload's event.type field. Payload modelled from SignWell's documented Event Data sample, not from a captured delivery. |
| Document Declined | `document_declined` | Fires when a signer declines to sign. The signer is carried in event.related_signer. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document Error | `document_error` | Fires when SignWell hits an error creating or updating a document. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document Expired | `document_expired` | Fires when a document passes its expiry date without being completed. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document In Progress | `document_in_progress` | Fires once, when a document starts being completed and its status becomes in progress (returned as pending by the API). Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document Recipients Updated | `document_recipients_updated` | Fires when a document's recipients are corrected after it has already been sent. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document Sent | `document_sent` | Fires when a document is sent to its recipients for signature. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document Signed | `document_signed` | Fires each time one recipient signs, so a multi-signer document raises it once per signer. The signer is carried in event.related_signer. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document SMS Failed | `document_sms_failed` | Fires when an SMS notification to a recipient reaches a terminal failure, either undelivered or failed. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document SMS Opted Out | `document_sms_opted_out` | Fires when a recipient's phone number is newly added to the SMS suppression list, for example because they replied STOP. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Document Viewed | `document_viewed` | Fires each time a signer opens the document, so it can fire many times per document. The signer is carried in event.related_signer. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Template Created | `template_created` | Fires when a document template is created. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
| Template Error | `template_error` | Fires when SignWell hits an error creating or updating a template. Registration is automatic via POST /api/v1/hooks; fastn routes on event.type. Payload modelled from SignWell's documented Event Data sample. |
