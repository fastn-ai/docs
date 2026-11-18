---
description: "DocuPotion document automation API."
---

# DocuPotion

DocuPotion document automation API. Generate PDF or PNG documents from reusable DocuPotion templates with merged JSON data, run bulk/batch generation jobs, download batch output, and read account usage. Base URL https://api.docupotion.com/v1 with a Bearer API key.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [docupotion.com](https://docupotion.com) |
| **Authentication** | API key |
| **Actions** | 9 |
| **Events** | 0 |
| **Slug** | `docupotion` |

## Use it

Add DocuPotion from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.docupotion.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Batch Job | `createBatchJob` | Start a bulk-generation batch job that renders one document per supplied row from a single DocuPotion template. Returns the job id to poll with Get Batch Job. Each row consumes one document from the plan quota. Not on the public API page; route confirmed in the DocuPotion web app code (api.docupotion.com/v1/batch client). The API validates templateId ("templateId is required") and rows ("rows must be a non-empty array of objects"). |
| Download Batch Job Output | `downloadBatchJob` | Request the zip of all documents produced by a batch job. Returns ready=false while the zip is being prepared; poll until ready=true and url is set. Not on the public API page; route confirmed in the DocuPotion web app code (api.docupotion.com/v1/batch client). (POST /v1/batch/{jobId}/download). |
| Generate Document | `createDocument` | Generate a single PDF or PNG document from a DocuPotion template, merging the supplied data object into the template's variables. Returns the file either base64-encoded or as a time-limited presigned download URL, and can additionally upload the file to the account's connected S3 bucket. WARNING: every call consumes one document from the plan quota, including calls that fail validation. |
| Generate Document From Airtable Record | `createFromAirtableRecord` | Generate a document from a DocuPotion Airtable integration by pointing at one Airtable record: DocuPotion reads the record fields through the saved integration and renders its template. Requires an Airtable integration configured in the DocuPotion web app. Documented in the DocuPotion help center (Generate PDF from an Airtable Automation: POST https://api.docupotion.com/v1/airtable with integrationId and record_id). |
| Get Account Usage | `getAccount` | Retrieve the DocuPotion account attached to the API key, including the account username and the document generation quota (documents used so far and the plan's document limit). Use it to check remaining quota before generating documents. |
| Get Batch Job | `getBatchJob` | Retrieve a single bulk-generation batch job by its id, including its processing state and per-row results. Poll this after Create Batch Job until the job completes. Not on the public API page; route confirmed in the DocuPotion web app code (api.docupotion.com/v1/batch client). (GET /v1/batch/{jobId}). |
| List Batch Jobs | `listBatchJobs` | List the bulk-generation batch jobs in the DocuPotion account, optionally filtered by template, with cursor pagination. Not on the public API page; route and params taken from the DocuPotion web app code (GET https://api.docupotion.com/v1/batch?templateId=&cursor=). |
| List Templates | `listTemplates` | List every document template in the DocuPotion account, returning each template's id and name. Use the returned templateId with Generate Document or Create Batch Job. Templates are authored in the DocuPotion web app; there is no API to create one. |
| Retry Batch Job | `retryBatchJob` | Re-run the failed rows of an existing bulk-generation batch job. Each retried row consumes one document credit again. Not on the public API page; route confirmed in the DocuPotion web app code (api.docupotion.com/v1/batch client). (POST /v1/batch/{jobId}/retry). |
