---
description: "Veryfi is a document AI / OCR platform."
hidden: true
---

# Veryfi OCR

<img src="../../.gitbook/assets/connectors/lg/veryfi-ocr.png" alt="Veryfi OCR logo">

Veryfi is a document AI / OCR platform. This connector wraps the Veryfi Data Extraction API v8: process and manage receipts and invoices, business cards, checks, contracts, W-2s, W-8BEN-Es, W-9s, bank statements, ∀Docs (any documents) and Parse (document-to-markdown); manage line items, tags and tax lines; classify and extract; document sets and PDF splitting; blueprints; OCR counts; fraud device blocklist; mTLS certificates; webhooks; and API/client key settings.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [veryfi.com](https://veryfi.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `veryfiOcr` |

## Use it

Add Veryfi OCR from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.veryfiOcr.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add a tag to a Business Card | `addBusinessCardTag` | Attach a single tag to a business card, creating the tag if it does not exist. Returns the tag id and name. |
| Add a tag to a Contract | `addContractTag` | Attach a single tag to a contract, creating the tag if it does not exist. Returns the tag id and name. |
| Add A Tag To A Document | `addTagToDocument` | Attach a single tag to a receipt or invoice, creating the tag if it does not exist. Returns the tag id and name. |
| Add a tag to a W-2 | `addW2Tag` | Attach a single tag to a W-2 form, creating the tag if it does not exist. Returns the tag id and name. |
| Add a tag to a W-8BEN-E | `addW8BenETag` | Attach a single tag to a W-8BEN-E form, creating the tag if it does not exist. Returns the tag id and name. |
| Add a tag to a W-9 | `addW9Tag` | Attach a single tag to a W-9 form, creating the tag if it does not exist. Returns the tag id and name. |
| Add A Webhook | `addWebhook` | Register a public HTTPS webhook URL and start Veryfi's verification handshake. Veryfi immediately POSTs {"event":"subscription","data":{"secret":...}} to that URL; pass the secret to Confirm A Webhook within 1 day. Answers 204 on success. Veryfi provides no API to remove a webhook once added. |
| Add Any Document Tag | `addAnyDocumentTag` | Attach a single tag to a ∀Docs document, creating the tag if it does not exist. Returns the tag id and name. |
| Add Any Document Tags | `addAnyDocumentTags` | Attach several tags at once to a ∀Docs document. Returns the document's full tag list. |
| Add Bank Statement Tag | `addBankStatementTag` | Attach a single tag to a bank statement, creating the tag if it does not exist. Returns the tag id and name. |

<details>

<summary>See 142 more actions</summary>

* **Add Bank Statement Tags** `addBankStatementTags`: Attach several tags at once to a bank statement. Returns the document's full tag list.
* **Add Check Tag** `addCheckTag`: Attach a single tag to a check, creating the tag if it does not exist. Returns the tag id and name.
* **Add Check Tags** `addCheckTags`: Attach several tags at once to a check. Returns the document's full tag list.
* **Add devices to blocklist** `blockDevice`: Add a device id to the account's fraud blocklist. Requires the Fraud Detection add-on.
* **Add tags to a Business Card** `addBusinessCardTags`: Attach several tags at once to a business card. Returns the document's full tag list.
* **Add tags to a Contract** `addContractTags`: Attach several tags at once to a contract. Returns the document's full tag list.
* **Add Tags To A Document** `addTagsToDocument`: Attach several tags at once to a receipt or invoice. Returns the document's full tag list.
* **Add tags to a W-2** `addW2Tags`: Attach several tags at once to a W-2 form. Returns the document's full tag list.
* **Add tags to a W-8BEN-E** `addW8BenETags`: Attach several tags at once to a W-8BEN-E form. Returns the document's full tag list.
* **Add tags to a W-9** `addW9Tags`: Attach several tags at once to a W-9 form. Returns the document's full tag list.
* **Bulk Process Multiple Documents** `bulkProcessDocuments`: Submit 1-100 publicly reachable document URLs for processing in one call. Results are delivered to your configured webhook, one request per document. Veryfi requires this endpoint to be enabled by support before use.
* **Check if a device is on the blocklist** `getBlockedDevice`: Check whether one device id is on the fraud blocklist. Requires the Fraud Detection add-on.
* **Classify and possibly extract data from a document** `extractDocument`: Classify a document against the given document_types and, when one matches, extract its fields in the same call. document_types is required (at least one) and accepts preset types such as "receipt" or any ∀Docs blueprint name from the Get Blueprints action. Returns the classification score plus an extraction object. Consumes one OCR credit.
* **Classify Document** `classifyDocument`: Classify an uploaded document, returning Veryfi's predicted document type and confidence score without running full extraction.
* **Confirm A Webhook** `confirmWebhook`: Complete the webhook handshake by returning the data.secret value Veryfi delivered to the webhook URL. Answers 204 once confirmed; secrets expire after one day.
* **Create A Line Item** `createLineItem`: Add a new line item to an existing receipt or invoice.
* **Create A Tax Line** `createTaxLine`: Add a tax line to a receipt or invoice. Veryfi answers 204 with no body on success.
* **Create API Key** `createApiKey`: Mint a new API key with the given name and permissions. The secret is returned once, on creation only. Requires a Veryfi Bearer API key.
* **Create Client Key** `createClientKey`: Create a new client key. Requires a Veryfi Bearer API key.
* **Delete A Document** `deleteDocument`: Permanently delete a processed receipt or invoice from Veryfi by its document ID.
* **Delete A Line Item** `deleteLineItem`: Delete one line item from a receipt or invoice.
* **Delete A Tax Line** `deleteTaxLine`: Delete one tax line from a receipt or invoice.
* **Delete a Tls Certificate** `deleteTlsCertificate`: Delete an mTLS client certificate from the account. Requires the mTLS add-on.
* **Delete All Document Line Items** `deleteAllDocumentLineItems`: Remove every line item from a receipt or invoice in one call.
* **Delete Any Document** `deleteAnyDocument`: Permanently delete a processed ∀Docs document from Veryfi by its document id.
* **Delete API Key** `deleteApiKey`: Permanently revoke one API key by id. Requires a Veryfi Bearer API key.
* **Delete Bank Statement** `deleteBankStatement`: Permanently delete a processed bank statement from Veryfi by its document id.
* **Delete Business Card** `deleteBusinessCard`: Permanently delete a processed business card from Veryfi by its document id.
* **Delete Check** `deleteCheck`: Permanently delete a processed check from Veryfi by its document id.
* **Delete Client Key** `deleteClientKey`: Delete one client key by id. Requires a Veryfi Bearer API key.
* **Delete Contract** `deleteContract`: Permanently delete a processed contract from Veryfi by its document id.
* **Delete Parse Document** `deleteParseDocument`: Permanently delete a processed parsed document from Veryfi by its document id.
* **Delete W-2** `deleteW2`: Permanently delete a processed W-2 form from Veryfi by its document id.
* **Delete W-8BEN-E** `deleteW8BenE`: Permanently delete a processed W-8BEN-E form from Veryfi by its document id.
* **Delete W-9** `deleteW9`: Permanently delete a processed W-9 form from Veryfi by its document id.
* **Get A Line Item** `getLineItem`: Retrieve one line item of a receipt or invoice by its line item ID.
* **Get A Tax Line** `getTaxLine`: Retrieve one tax line of a receipt or invoice by tax line ID.
* **Get Any Document** `getAnyDocument`: Retrieve one processed ∀Docs document by its Veryfi document id, with every extracted field.
* **Get Any Document Tags** `getAnyDocumentTags`: List the tags attached to a ∀Docs document.
* **Get API Key** `getApiKey`: Retrieve one API key's metadata and permissions by id. Requires a Veryfi Bearer API key.
* **Get API Key Permissions** `getApiKeyPermissions`: List every permission string that can be granted to an API key. Requires a Veryfi Bearer API key.
* **Get Bank Statement** `getBankStatement`: Retrieve one processed bank statement by its Veryfi document id, with every extracted field.
* **Get Bank Statement Set** `getBankStatementSet`: Retrieve one bank statement set by id. Requires the webhook/document-set feature to be enabled on the account.
* **Get Bank Statement Tags** `getBankStatementTags`: List the tags attached to a bank statement.
* **Get Blueprints** `getBlueprints`: List every ∀Docs blueprint (document type template) available to the account, with its id, document_type label and machine name.
* **Get Business Card** `getBusinessCard`: Retrieve one processed business card by its Veryfi document id, with every extracted field.
* **Get Business Card tags** `getBusinessCardTags`: List the tags attached to a business card.
* **Get Check** `getCheck`: Retrieve one processed check by its Veryfi document id, with every extracted field.
* **Get Check Tags** `getCheckTags`: List the tags attached to a check.
* **Get Contract** `getContract`: Retrieve one processed contract by its Veryfi document id, with every extracted field.
* **Get Contract tags** `getContractTags`: List the tags attached to a contract.
* **Get devices from blocklist** `listBlockedDevices`: List the device ids on the account's fraud blocklist. Requires the Fraud Detection add-on.
* **Get Document** `getDocument`: Retrieve one processed receipt or invoice by its Veryfi document ID, with all extracted fields, line items, tags and tax lines.
* **Get Document Line Items** `getDocumentLineItems`: List every extracted line item on a receipt or invoice.
* **Get Document Set** `getDocumentSet`: Retrieve one receipt/invoice set by id. Requires the webhook/document-set feature to be enabled on the account.
* **Get Document Tags** `getDocumentTags`: List the tags attached to a receipt or invoice.
* **Get OCR Counts** `getOcrCounts`: Report how many specialty OCR scans the account consumed in a date window, split by source (api vs lens). This is Veryfi's only usage-reporting endpoint; general document-OCR credit balance is visible only in the Veryfi Hub UI.
* **Get OpenAPI Schema** `getOpenApiSchema`: Return Veryfi's machine-readable OpenAPI 3.1 schema for the receipts and invoices (documents) API.
* **Get Parse Document** `getParseDocument`: Retrieve one processed parsed document by its Veryfi document id, with every extracted field.
* **Get Parse Set** `getParseSet`: Retrieve one parsed document set by id. Requires the webhook/document-set feature to be enabled on the account.
* **Get Release Notifications** `getReleaseNotifications`: List Veryfi platform release notifications (model and service version announcements), newest first, with paging.
* **Get Tls Certificates** `listTlsCertificates`: List the mTLS client certificates registered on the account. Requires the mTLS add-on.
* **Get W-2** `getW2`: Retrieve one processed W-2 form by its Veryfi document id, with every extracted field.
* **Get W-2 Set** `getW2Set`: Retrieve one W-2 set by id. Requires the webhook/document-set feature to be enabled on the account.
* **Get W-2 tags** `getW2Tags`: List the tags attached to a W-2 form.
* **Get W-8BEN-E** `getW8BenE`: Retrieve one processed W-8BEN-E form by its Veryfi document id, with every extracted field.
* **Get W-8BEN-E tags** `getW8BenETags`: List the tags attached to a W-8BEN-E form.
* **Get W-9** `getW9`: Retrieve one processed W-9 form by its Veryfi document id, with every extracted field.
* **Get W-9 tags** `getW9Tags`: List the tags attached to a W-9 form.
* **Get Webhooks** `getWebhooks`: List the account's pending and confirmed webhook URLs. Pending webhooks have been sent a verification secret but not yet confirmed.
* **List Any Documents** `listAnyDocuments`: List the ∀Docs documents previously processed by Veryfi, newest first, with date-range filters and paging. Returns a documents array plus a meta object with paging information.
* **List API Keys** `listApiKeys`: List the account's API keys and their permissions. Requires a Veryfi Bearer API key; the legacy 'apikey username:key' scheme is rejected on this route.
* **List Bank Statement Sets** `listBankStatementSets`: List the bank statement sets processed by Veryfi. Requires the webhook/document-set feature to be enabled on the account.
* **List Bank Statements** `listBankStatements`: List the bank statements previously processed by Veryfi, newest first, with date-range filters and paging. Returns a documents array plus a meta object with paging information.
* **List Business Cards** `listBusinessCards`: List the business cards previously processed by Veryfi, newest first, with date-range filters and paging. Returns a documents array plus a meta object with paging information.
* **List Checks** `listChecks`: List the checks previously processed by Veryfi, newest first, with date-range filters and paging. Returns a documents array plus a meta object with paging information.
* **List Client Keys** `listClientKeys`: List the account's client keys. Requires a Veryfi Bearer API key; the legacy 'apikey username:key' scheme is rejected on this route.
* **List Contracts** `listContracts`: List the contracts previously processed by Veryfi, newest first, with date-range filters and paging. Returns a documents array plus a meta object with paging information.
* **List Document Sets** `listDocumentSets`: List the receipt/invoice sets processed by Veryfi. Requires the webhook/document-set feature to be enabled on the account.
* **List Document Tax Lines** `listDocumentTaxLines`: List the tax lines extracted from a receipt or invoice. Veryfi returns a JSON array of tax-line objects, each with order, name, rate, base and total.
* **List Documents** `listDocuments`: List the receipts and invoices previously processed by Veryfi, newest first. Supports paging, free-text search, tag/owner/status filters and created/updated/date range filters. Returns a documents array plus a meta object with paging information.
* **List Parse Documents** `listParseDocuments`: List the parsed documents previously processed by Veryfi, newest first, with date-range filters and paging. Returns a documents array plus a meta object with paging information.
* **List Parse Sets** `listParseSets`: List the parsed document sets processed by Veryfi. Requires the webhook/document-set feature to be enabled on the account.
* **List W-2 Sets** `listW2Sets`: List the W-2 sets processed by Veryfi. Requires the webhook/document-set feature to be enabled on the account.
* **List W-2s** `listW2s`: List the W-2 forms previously processed by Veryfi, newest first, with date-range filters and paging. Returns a documents array plus a meta object with paging information.
* **List W-8BEN-Es** `listW8BenEs`: List the W-8BEN-E forms previously processed by Veryfi, newest first, with date-range filters and paging. Returns a documents array plus a meta object with paging information.
* **List W-9s** `listW9s`: List the W-9 forms previously processed by Veryfi, newest first, with date-range filters and paging. Returns a documents array plus a meta object with paging information.
* **Process a Check with a Document** `processCheckWithDocument`: Submit an image containing a check together with an accompanying document (e.g. an invoice paid by that check) and extract both in one call. The image must actually contain a check; Veryfi answers 400 'Failed to extract' otherwise. Consumes one OCR credit.
* **Process A Document** `processDocument`: Upload a receipt or invoice to Veryfi for OCR and data extraction, either as base64 file data or as a public file URL. Consumes one OCR credit. Returns the fully extracted document.
* **Process a Tls Certificate** `uploadTlsCertificate`: Upload an mTLS client certificate for the account. Requires the mTLS add-on.
* **Process Any Document** `processAnyDocument`: Upload a ∀Docs document to Veryfi for OCR and data extraction, as base64 file data, a public file URL, or an S3 package path. Consumes one OCR credit. Returns the fully extracted document.
* **Process Any Document Async** `processAnyDocumentAsync`: Submit a ∀Docs document for asynchronous OCR processing. Veryfi answers immediately with a job/document id and delivers the extracted result to the account webhook. Consumes one OCR credit. Requires the webhook feature to be enabled on the account.
* **Process Bank Statement** `processBankStatement`: Upload a bank statement to Veryfi for OCR and data extraction, as base64 file data, a public file URL, or an S3 package path. Consumes one OCR credit. Returns the fully extracted document.
* **Process Bank Statement Async** `processBankStatementAsync`: Submit a bank statement for asynchronous OCR processing. Veryfi answers immediately with a job/document id and delivers the extracted result to the account webhook. Consumes one OCR credit. Requires the webhook feature to be enabled on the account.
* **Process Bank Statement Set** `processBankStatementSet`: Submit a multi-document package as a bank statement set; results are delivered to the account webhook. Requires the webhook/document-set feature to be enabled on the account.
* **Process Business Card** `processBusinessCard`: Upload a business card to Veryfi for OCR and data extraction, as base64 file data, a public file URL, or an S3 package path. Consumes one OCR credit. Returns the fully extracted document.
* **Process Check** `processCheck`: Upload a check to Veryfi for OCR and data extraction, as base64 file data, a public file URL, or an S3 package path. Consumes one OCR credit. Returns the fully extracted document.
* **Process Check Async** `processCheckAsync`: Submit a check for asynchronous OCR processing. Veryfi answers immediately with a job/document id and delivers the extracted result to the account webhook. Consumes one OCR credit. Requires the webhook feature to be enabled on the account.
* **Process Contract** `processContract`: Upload a contract to Veryfi for OCR and data extraction, as base64 file data, a public file URL, or an S3 package path. Consumes one OCR credit. Returns the fully extracted document.
* **Process Document Set** `processDocumentSet`: Submit a multi-document package as a receipt/invoice set; results are delivered to the account webhook. Requires the webhook/document-set feature to be enabled on the account.
* **Process Parse Document** `processParseDocument`: Upload a parsed document to Veryfi for OCR and data extraction, as base64 file data, a public file URL, or an S3 package path. Consumes one OCR credit. Returns the fully extracted document.
* **Process Parse Document Async** `processParseDocumentAsync`: Submit a parsed document for asynchronous OCR processing. Veryfi answers immediately with a job/document id and delivers the extracted result to the account webhook. Consumes one OCR credit. Requires the webhook feature to be enabled on the account.
* **Process Parse Set** `processParseSet`: Submit a multi-document package as a parsed document set; results are delivered to the account webhook. Requires the webhook/document-set feature to be enabled on the account.
* **Process W-2** `processW2`: Upload a W-2 form to Veryfi for OCR and data extraction, as base64 file data, a public file URL, or an S3 package path. Consumes one OCR credit. Returns the fully extracted document.
* **Process W-2 Set** `processW2Set`: Submit a multi-document package as a W-2 set; results are delivered to the account webhook. Requires the webhook/document-set feature to be enabled on the account.
* **Process W-8BEN-E** `processW8BenE`: Upload a W-8BEN-E form to Veryfi for OCR and data extraction, as base64 file data, a public file URL, or an S3 package path. Consumes one OCR credit. Returns the fully extracted document.
* **Process W-9** `processW9`: Upload a W-9 form to Veryfi for OCR and data extraction, as base64 file data, a public file URL, or an S3 package path. Consumes one OCR credit. Returns the fully extracted document.
* **Remove a device from blocklist** `unblockDevice`: Remove a device id from the account's fraud blocklist. Requires the Fraud Detection add-on.
* **Reset Client Keys** `resetClientKeys`: Rotate/reset the account's client keys. Requires a Veryfi Bearer API key.
* **Rotate API Key** `rotateApiKey`: Rotate one API key, issuing a new secret and invalidating the old one. Requires a Veryfi Bearer API key.
* **Unlink a tag from a Business Card** `unlinkBusinessCardTag`: Detach one tag from a business card by tag id.
* **Unlink a tag from a Contract** `unlinkContractTag`: Detach one tag from a contract by tag id.
* **Unlink A Tag From A Document** `unlinkTagFromDocument`: Detach one tag from a receipt or invoice by tag ID.
* **Unlink a tag from a W-2** `unlinkW2Tag`: Detach one tag from a W-2 form by tag id.
* **Unlink a tag from a W-8BEN-E** `unlinkW8BenETag`: Detach one tag from a W-8BEN-E form by tag id.
* **Unlink a tag from a W-9** `unlinkW9Tag`: Detach one tag from a W-9 form by tag id.
* **Unlink All Any Document Tags** `unlinkAllAnyDocumentTags`: Detach every tag from a ∀Docs document.
* **Unlink All Bank Statement Tags** `unlinkAllBankStatementTags`: Detach every tag from a bank statement.
* **Unlink All Check Tags** `unlinkAllCheckTags`: Detach every tag from a check.
* **Unlink all tags from a Business Card** `unlinkAllBusinessCardTags`: Detach every tag from a business card.
* **Unlink all tags from a Contract** `unlinkAllContractTags`: Detach every tag from a contract.
* **Unlink All Tags From A Document** `unlinkAllTagsFromDocument`: Detach every tag from a receipt or invoice.
* **Unlink all tags from a W-2** `unlinkAllW2Tags`: Detach every tag from a W-2 form.
* **Unlink all tags from a W-8BEN-E** `unlinkAllW8BenETags`: Detach every tag from a W-8BEN-E form.
* **Unlink all tags from a W-9** `unlinkAllW9Tags`: Detach every tag from a W-9 form.
* **Unlink Any Document Tag** `unlinkAnyDocumentTag`: Detach one tag from a ∀Docs document by tag id.
* **Unlink Bank Statement Tag** `unlinkBankStatementTag`: Detach one tag from a bank statement by tag id.
* **Unlink Check Tag** `unlinkCheckTag`: Detach one tag from a check by tag id.
* **Update A Document** `updateDocument`: Correct or annotate an already-processed receipt or invoice. Returns the updated document.
* **Update A Line Item** `updateLineItem`: Correct one line item on a receipt or invoice.
* **Update A Tax Line** `updateTaxLine`: Correct one tax line on a receipt or invoice. The tax line is addressed by its `order` index, not by a separate id. The order itself cannot be changed.
* **Update Any Document** `updateAnyDocument`: Correct or annotate an already-processed ∀Docs document. Pass meta to set the document tags and external_id. Returns the updated document.
* **Update API Key** `updateApiKey`: Rename an API key or change its permissions. Requires a Veryfi Bearer API key.
* **Update Bank Statement** `updateBankStatement`: Correct or annotate an already-processed bank statement. Pass meta to set the document tags and external_id. Returns the updated document.
* **Update Business Card** `updateBusinessCard`: Correct or annotate an already-processed business card. Pass meta to set the document tags and external_id. Returns the updated document.
* **Update Check** `updateCheck`: Correct or annotate an already-processed check. Pass meta to set the document tags and external_id. Returns the updated document.
* **Update Contract** `updateContract`: Correct or annotate an already-processed contract. Pass meta to set the document tags and external_id. Returns the updated document.
* **Update Parse Document** `updateParseDocument`: Update a converted markdown document. Veryfi accepts exactly one field on this route: status. Returns the updated markdown document.
* **Update W-2** `updateW2`: Correct or annotate an already-processed W-2 form. Pass meta to set the document tags and external_id. Returns the updated document.
* **Update W-8BEN-E** `updateW8BenE`: Correct or annotate an already-processed W-8BEN-E form. Pass meta to set the document tags and external_id. Returns the updated document.
* **Update W-9** `updateW9`: Correct or annotate an already-processed W-9 form. Pass meta to set the document tags and external_id. Returns the updated document.
* **Verify API Key** `verifyApiKey`: Verify that the presented Bearer API key is valid and report its permissions. Requires a Veryfi Bearer API key.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Document Processed | `document.created` | An asynchronously submitted document finished processing and is ready to be retrieved. Fetch the full document with Get Document using data.id. Veryfi does not guarantee exactly-once delivery, so treat data.id as an idempotency key. |
| Document Processing Failed | `document.failed` | Processing of an asynchronously submitted document failed. data.id identifies the document that failed. |
| Webhook Verification | `subscription` | Sent once, immediately after Add A Webhook, to verify the URL. data.secret must be posted back via Confirm A Webhook within one day or the registration lapses. |
