---
description: "Extracta.ai (Extracta LABS) AI document data extraction and document classification."
hidden: true
---

# Extracta.ai

<img src="../../.gitbook/assets/connectors/extracta-ai.png" alt="Extracta.ai logo" width="64">

Extracta.ai (Extracta LABS) AI document data extraction and document classification. Define extraction templates with typed fields, upload documents (PDF, DOCX, TXT, JPEG/PNG/TIFF/BMP), and poll for structured JSON results; plus a document classification API that predicts a document type per file and can chain into an extraction template. Also exposes the account credit balance (1 credit = 1 page).

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [extracta.ai](https://extracta.ai) |
| **Authentication** | API key |
| **Slug** | `extractaAi` |

## Use it

Add Extracta.ai from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.extractaAi.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Check Api Availability | `checkApiHealth` | Health probe for the Extracta.ai API, returning {"status":"ok"} when the service is reachable. Undocumented route discovered on the api.extracta.ai root host; it is served without authentication, so it reports service availability only and says nothing about whether your API key is valid. Use Get Credit Balance for an authenticated check. |
| Create Classification Template | `createClassification` | Creates a document classification template that sorts uploaded documents into the document types you define. Each document type is described by a name, a description and a list of uniqueWords the classifier keys on, and may optionally name an extractionId so that a classified document is automatically passed to that extraction template. Returns the classificationId. Costs no credits. |
| Create Extraction Template | `createExtraction` | Creates a new Extracta.ai extraction template that defines which fields to pull out of a document and how to process it. Returns the extractionId used by Upload File For Extraction, View Extraction Template and Get Batch Extraction Results. Creating a template costs no credits; credits are consumed only when pages are processed. |
| Delete Classification Batch | `deleteClassificationBatch` | Permanently deletes a single batch from a document classification template, together with every result and file inside that batch. The classification template itself and its other batches are left untouched. Irreversible. |
| Delete Classification Files | `deleteClassificationFiles` | Permanently deletes one or more specific files, and their classification results, from a batch inside a document classification template. The rest of the batch and the template are left untouched. Irreversible. |
| Delete Classification Template | `deleteClassification` | Permanently deletes an entire document classification template together with every batch, result and uploaded file belonging to it. Irreversible. Use Delete Classification Batch or Delete Classification Files instead when you only need to remove part of the data. |
| Delete Extraction Data | `deleteExtraction` | Permanently deletes Extracta.ai extraction data. The scope depends on which ids you supply: extractionId alone removes the whole extraction template with every batch and file under it; extractionId plus batchId removes that batch and all its files; extractionId plus batchId plus fileId removes a single file. This is irreversible and cannot be undone. |
| Get Batch Extraction Results | `getBatchResults` | Retrieves the extracted data for a batch of documents, or the batch's current processing status while it is still running. Extraction is asynchronous: poll this action after Upload File For Extraction until every file reports status 'processed'. Leave at least 2 seconds between consecutive calls to avoid vendor rate limiting. Supply fileId to narrow the response to a single document. Costs no credits. |
| Get Billing Diagnostics | `getBillingDiagnostics` | Returns the billingData and errorData diagnostics block used by the Extracta.ai web dashboard. Undocumented route discovered on the api.extracta.ai root host. WARNING: this route is served WITHOUT authentication and returns an identical response for every caller, so it is not scoped to your account and should not be treated as your billing record. Prefer Get Credit Balance for account usage. Included for completeness of the API surface. |
| Get Classification Results | `getClassificationResults` | Retrieves the predicted document type for each file in a classification batch, or the batch's current status while it is still running. Classification is asynchronous: poll this action after Upload File For Classification until every file is processed. Leave at least 2 seconds between consecutive calls to avoid vendor rate limiting. Supply fileId to narrow the response to a single document. Costs no credits. |

<details>

<summary>See 7 more actions</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Get Credit Balance | `getCredits` | Returns the number of processing credits currently available on the Extracta.ai account. Credits are consumed per document page processed (1 credit = 1 page), so call this before uploading a large batch. Takes no input. |
| Update Classification Template | `updateClassification` | Updates an existing document classification template: rename it, change its description, or replace its document type definitions and their uniqueWords without recreating the classifier. The vendor requires name, description and documentTypes to all be supplied inside classificationDetails. Costs no credits. |
| Update Extraction Template | `updateExtraction` | Updates an existing Extracta.ai extraction template: rename it, change its description or language, or replace its processing options and field definitions without recreating the template. NOTE: the vendor documents omitted keys as unchanged, but in testing an update carrying only name and description also reset the options block to its defaults. Send the full options and fields you want to keep. Costs no credits. |
| Upload File For Classification | `uploadClassificationFiles` | Uploads a single text-based document to a document classification template and starts classifying it in a new batch. Returns the classificationId, the new batchId and the fileId for use with Get Classification Results. CONSUMES CREDITS: 1 credit per processed page. Carries the document as a text/plain multipart part, so it accepts plain-text documents; binary formats (PDF, DOCX, PNG, JPEG, TIFF, BMP) are supported by the vendor but cannot be sent through this action. |
| Upload File For Extraction | `uploadFiles` | Uploads a single text-based document to an Extracta.ai extraction template and starts processing it in a new batch. Returns the extractionId, the new batchId and the fileId, which you pass to Get Batch Extraction Results to poll for the extracted data. CONSUMES CREDITS: 1 credit per processed page. Carries the document as a text/plain multipart part, so it accepts plain-text documents; binary formats (PDF, DOCX, PNG, JPEG, TIFF, BMP) are supported by the vendor but cannot be sent through this action. |
| View Classification Template | `viewClassification` | Retrieves the stored definition of a document classification template by its classificationId, including its name, description, configured document types, their uniqueWords and any linked extraction templates. Use it to verify or audit a classifier setup. Costs no credits. |
| View Extraction Template | `viewExtraction` | Retrieves the full definition of an existing Extracta.ai extraction template by its extractionId, including its name, language, processing options and the field definitions being extracted. Useful for verifying or auditing a template. Costs no credits. |

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Extraction Confirmed | `extraction.confirmed` | Fires when a user manually confirms extracted data in the Extracta.ai web interface, marking it finally approved. Use it to finalize a workflow or persist results. SETUP IS MANUAL - Extracta.ai has no webhook registration API. Log in at https://app.extracta.ai, open the /api page in the dashboard, paste this trigger's fastn webhook URL into the webhook listener field, save, and copy the generated secret. Requires the current (non-legacy) webhook listener. |
| Extraction Edited | `extraction.edited` | Fires when a user manually edits extracted data in the Extracta.ai web interface. Use it to sync corrections downstream or trigger quality checks. SETUP IS MANUAL - Extracta.ai has no webhook registration API. Log in at https://app.extracta.ai, open the /api page in the dashboard, paste this trigger's fastn webhook URL into the webhook listener field, save, and copy the generated secret. Requires the current (non-legacy) webhook listener; the legacy listener does not send event types. |
| Extraction Failed | `extraction.failed` | Fires when a file fails to process, for example because it is corrupt, in an unsupported format, or hit an internal error. Use it to alert, retry, or ask for a new upload. SETUP IS MANUAL - Extracta.ai has no webhook registration API. Log in at https://app.extracta.ai, open the /api page in the dashboard, paste this trigger's fastn webhook URL into the webhook listener field, save, and copy the generated secret. Requires the current (non-legacy) webhook listener. |
| Extraction Processed | `extraction.processed` | Fires when every file in an upload has been successfully processed and its data extracted. SETUP IS MANUAL - Extracta.ai has no webhook registration API. Log in at https://app.extracta.ai, open the /api page in the dashboard, paste this trigger's fastn webhook URL into the webhook listener field, save, and copy the generated secret. Deliveries are signed with the header x-webhook-signature, computed as base64(HMAC-SHA256(secret with the leading 'E_AI_K_' stripped, JSON.stringify(body.result))). |
