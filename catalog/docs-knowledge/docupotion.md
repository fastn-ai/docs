---
description: "DocuPotion generates PDF and image documents from templates. Create single documents or batch jobs and download the output."
hidden: true
---

# DocuPotion

<img src="../../.gitbook/assets/connectors/lg/docupotion.png" alt="DocuPotion logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [docupotion.com](https://docupotion.com) |
| **Authentication** | API key |
| **Slug** | `docupotion` |

## Setup

Your customers enter their API key for DocuPotion when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect DocuPotion from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **DocuPotion**.
2. Select **Connect** on the DocuPotion card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use DocuPotion's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Batch Job</td><td><code>createBatchJob</code></td><td>Start a bulk-generation batch job that renders one document per supplied row from a single DocuPotion template. Returns the job id to poll with Get Batch Job. Each row consumes one document from the plan quota. Not on the public API page; route confirmed in the DocuPotion web app code (api.docupotion.com/v1/batch client). The API validates templateId ("templateId is required") and rows ("rows must be a non-empty array of objects").</td></tr><tr><td>Download Batch Job Output</td><td><code>downloadBatchJob</code></td><td>Request the zip of all documents produced by a batch job. Returns ready=false while the zip is being prepared; poll until ready=true and url is set. Not on the public API page; route confirmed in the DocuPotion web app code (api.docupotion.com/v1/batch client).</td></tr><tr><td>Generate Document</td><td><code>createDocument</code></td><td>Generate a single PDF or PNG document from a DocuPotion template, merging the supplied data object into the template's variables. Returns the file either base64-encoded or as a time-limited presigned download URL, and can additionally upload the file to the account's connected S3 bucket. WARNING: every call consumes one document from the plan quota, including calls that fail validation.</td></tr><tr><td>Generate Document From Airtable Record</td><td><code>createFromAirtableRecord</code></td><td>Generate a document from a DocuPotion Airtable integration by pointing at one Airtable record: DocuPotion reads the record fields through the saved integration and renders its template. Requires an Airtable integration configured in the DocuPotion web app. Documented in the DocuPotion help center (Generate PDF from an Airtable Automation: POST https://api.docupotion.com/v1/airtable with integrationId and record_id).</td></tr><tr><td>Get Account Usage</td><td><code>getAccount</code></td><td>Retrieve the DocuPotion account attached to the API key, including the account username and the document generation quota (documents used so far and the plan's document limit). Use it to check remaining quota before generating documents.</td></tr><tr><td>Get Batch Job</td><td><code>getBatchJob</code></td><td>Retrieve a single bulk-generation batch job by its id, including its processing state and per-row results. Poll this after Create Batch Job until the job completes. Not on the public API page; route confirmed in the DocuPotion web app code (api.docupotion.com/v1/batch client).</td></tr><tr><td>List Batch Jobs</td><td><code>listBatchJobs</code></td><td>List the bulk-generation batch jobs in the DocuPotion account, optionally filtered by template, with cursor pagination. Not on the public API page; route and params taken from the DocuPotion web app code (GET https://api.docupotion.com/v1/batch?templateId=&amp;cursor=).</td></tr><tr><td>List Templates</td><td><code>listTemplates</code></td><td>List every document template in the DocuPotion account, returning each template's id and name. Use the returned templateId with Generate Document or Create Batch Job. Templates are authored in the DocuPotion web app; there is no API to create one.</td></tr><tr><td>Retry Batch Job</td><td><code>retryBatchJob</code></td><td>Re-run the failed rows of an existing bulk-generation batch job. Each retried row consumes one document credit again. Not on the public API page; route confirmed in the DocuPotion web app code (api.docupotion.com/v1/batch client).</td></tr></tbody></table>

