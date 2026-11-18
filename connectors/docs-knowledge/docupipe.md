---
description: "DocuPipe document parsing and structured data extraction API."
hidden: true
---

# DocuPipe

<img src="../../.gitbook/assets/connectors/lg/docupipe.png" alt="DocuPipe logo">

DocuPipe document parsing and structured data extraction API. Upload documents, run OCR/parsing, define extraction schemas, standardize documents into structured JSON, classify and split documents, run workflows, generate human reviews, and manage webhook endpoints.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [docupipe.ai](https://docupipe.ai) |
| **Authentication** | API key |
| **Slug** | `docupipe` |

## Use it

Add DocuPipe from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.docupipe.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Class | `createClass` | Create a document class (category) that the classifier can assign documents to. Returns the new classId. |
| Add New Schema | `createSchema` | Create a new extraction schema from a JSON Schema definition plus optional natural-language guidelines. The returned schemaId is used by the standardize endpoints to extract structured data from documents. |
| Analyze Document | `analyzeDocument` | Ask a list of free-form questions about one processed document and receive answers with confidence scores and citations. Returns an analysisId to retrieve. METERED: consumes credits. |
| Analyze Document Set | `analyzeData` | Ask questions across a set of documents (by id list, dataset or schema) rather than a single document, and receive aggregate answers with citations. METERED: consumes credits. |
| AutoGenerate Schema | `autogenerateSchema` | Have DocuPipe infer an extraction schema from one or more sample documents (or a whole dataset), optionally standardizing those documents with the new schema in the same call. METERED: consumes credits. |
| Bulk Download OCR PDFs | `bulkDownloadOcrPdfs` | Return a presigned URL for a zip archive containing the OCR PDFs of up to 100 documents. The URL expires after 24 hours. Only PDF and image documents are supported. |
| Bulk Download Original Documents | `bulkDownloadOriginals` | Return a presigned URL for a zip archive containing the original uploaded files of up to 100 documents. The URL expires after 24 hours. |
| Bulk Download Standardization Excels | `bulkDownloadStandardizationExcels` | Return a presigned URL for a zip archive containing one Excel file per requested standardization. |
| Bulk Download Standardization XMLs | `bulkDownloadStandardizationXmls` | Return a presigned URL for a zip archive containing one XML file per requested standardization. |
| Classify Documents | `classifyDocuments` | Assign document classes to a batch of processed documents using the AI classifier. Supports multi-class assignment and an "unknown" bucket. METERED: consumes credits. |

<details>

<summary>See 85 more actions</summary>

* **Copy Class To Another Workspace** `copyClassification`: Copy one document class into a different DocuPipe workspace. Requires the TARGET workspace's API key in the request body (targetWorkspaceApiKey) - supply a key you own for that workspace.
* **Copy Schema (Alias Route)** `copySchemaAlias`: Second live route for copying a schema into another workspace (POST /copy/schema). Behaves identically to Copy Schema To Another Workspace (POST /schema/copy); built because the route provably exists. SECURITY: requires the TARGET workspace's API key in the body, so the request body of every execution record will contain a live credential - prefer proving it out of band.
* **Copy Schema To Another Workspace** `copySchema`: Copy one extraction schema into a different DocuPipe workspace. Requires the TARGET workspace's API key in the request body (targetWorkspaceApiKey) - supply a key you own for that workspace.
* **Create On-Submit Workflow** `createWorkflow`: Define a workflow that runs automatically when a document is submitted with this workflowId. Supply exactly one step object: standardizeStep, standardizeReviewStep, classifyStandardizeStep, splitStandardizeStep or splitClassifyStandardizeStep. Returns the new workflowId.
* **Create Presigned Upload URL** `createPresignedUploadUrl`: Create a presigned S3 PUT URL for uploading a large file directly, plus the matching GET URL to pass as document.url to Submit Document For Processing. Use this instead of base64 for big files.
* **Create Workflow V2** `createWorkflowV2`: Create a V2 node-graph workflow (the newer visual workflow model). UNDOCUMENTED: this route is not in the DocuPipe OpenAPI spec but is live and returns 200; proven by live sweep. A new workflow starts in status "draft" with empty node buckets (input, split, merge, classify, standardize, redact, reasoning, output).
* **Delete Class** `deleteClass`: Permanently delete one document class by classId. Returns {"success": true}.
* **Delete Document** `deleteDocument`: Permanently delete one document and its parsed result by documentId. Returns {"success": true}.
* **Delete Jobs** `deleteJobs`: Permanently delete job records by passing a list of jobIds. This removes the job history entries, not the documents they produced.
* **Delete Multiple Analyses** `deleteAnalyses`: Permanently delete several analyses in one call by passing a list of analysisIds.
* **Delete Multiple Documents** `deleteDocuments`: Permanently delete several documents in one call by passing a list of documentIds. Returns {"success": true}.
* **Delete Multiple Standardizations** `deleteStandardizations`: Permanently delete several standardizations in one call by passing a list of standardizationIds.
* **Delete Redaction** `deleteRedaction`: Permanently delete one redaction record by id. Undocumented in DocuPipe's OpenAPI spec but live; an unknown id answers 404 {"detail":"Redaction not found"}.
* **Delete Reviews** `deleteReviews`: Permanently delete human reviews by passing a list of reviewIds.
* **Delete Schema** `deleteSchema`: Permanently delete one extraction schema by schemaId. Returns {"success": true}.
* **Delete Standardization** `deleteStandardization`: Permanently delete one standardization by id. Returns {"success": true}.
* **Delete Workflow** `deleteWorkflow`: Permanently delete one workflow by workflowId. Returns {"success": true}.
* **Delete Workflow V2** `deleteWorkflowV2`: Permanently delete one V2 node-graph workflow by workflowId. UNDOCUMENTED: not in the DocuPipe OpenAPI spec but live and returning 200 {"success": true}; proven by live sweep.
* **Deregister Webhook Endpoint** `deleteWebhookEndpoint`: Deregister a webhook endpoint by endpointId so it stops receiving events. Returns {"success": true}.
* **Download Merged Standardization Excel** `downloadMergedStandardizationExcel`: Combine several standardizations into a single Excel workbook and return a presigned download URL. Optionally add a source column identifying each row's origin.
* **Download OCR PDF URL** `getDocumentOcrUrl`: Generate a time-limited presigned URL to download the searchable OCR PDF for one document. Only PDF and image documents are supported.
* **Download Original Document URL** `getDocumentOriginalUrl`: Generate a time-limited presigned URL to download the original uploaded file for one document, or its PDF conversion, depending on the format parameter.
* **Download Public Document URL** `getDocumentPublicUrl`: Generate a long-lived public URL for one document. WARNING: anyone holding the returned URL can read the document without authentication.
* **Download Standardization Excel URL** `getStandardizationExcelUrl`: Generate a time-limited presigned URL for an Excel export of one standardization.
* **Edit Class** `editClass`: Rename a document class or change its description. Identify the class by classId.
* **Edit Schema** `editSchema`: Rename an existing extraction schema or change its description and extraction guidelines. Identify the schema by schemaId.
* **Generate Review Presigned URL** `getReviewPresignedUrl`: Generate a time-limited shareable URL that opens the visual review UI for one review, so a human reviewer can verify the extracted fields without a DocuPipe login.
* **Generate Visual Review** `generateReviewBatch`: Create human-in-the-loop visual reviews for a batch of standardizations, so a person can verify or correct the extracted fields against the source pages. METERED: consumes credits.
* **Get Account Information** `getAccount`: Retrieve the current DocuPipe workspace account: plan name, remaining credits, overage settings, renewal date, storage region and feature flags. Use this before running metered operations to check the credit balance.
* **Get Document Count** `getDocumentSummary`: Return the total number of documents in the workspace and the list of dataset names, optionally restricted to a creation-timestamp window.
* **Get Job Count** `getJobSummary`: Return all-time and recent job counts by status, the total visible job count, and optionally a daily usage breakdown.
* **Get Prometheus Metrics** `getMetrics`: Undocumented metrics endpoint (not in the DocuPipe OpenAPI spec, found by live route sweep). Returns Prometheus-format metrics on deployments where metrics are enabled. On DocuPipe cloud it is feature-gated and answers 404 {"detail":"Metrics are not enabled"} — distinct from the absent-route body {"detail":"Not Found"}.
* **Get Schema Count** `getSchemaSummary`: Return the total number of extraction schemas defined in the workspace.
* **Get Schema Proposals For Document** `getProposedSchemas`: Return AI-proposed extraction schemas for a processed document, plus a natural-language description of the document. SECURITY WARNING: DocuPipe returns the CALLING ACCOUNT'S OWN API KEY in every schemas[].userId field of this response - it is the only endpoint on the API that does. Strip or redact schemas[].userId before logging, storing or passing this response anywhere, and never expose it to an end user.
* **Get Service Version** `getServiceVersion`: Root endpoint. Returns a message containing the running DocuPipe server version string.
* **Get Standardization Count** `getStandardizationSummary`: Return the total number of standardizations in the workspace and the list of schema names they were produced with.
* **Get Webhook Portal Link** `getWebhookPortalLink`: Return a one-time magic link into the Svix app portal where webhook subscriptions, delivery logs and replays can be managed by hand. SECURITY: the returned URL embeds a one-time access token - treat it as a credential.
* **Health Check** `healthCheck`: Health check endpoint to confirm the DocuPipe service is operational. Returns {"success": true}.
* **Health Check (POST)** `healthCheckPost`: POST variant of the DocuPipe health check, for monitors that require a POST probe. Returns {"success": true}.
* **List Analyses** `listAnalyses`: List the analyses run in the workspace, with limit/offset paging. Each entry carries its questions, answers and source documents.
* **List Classes** `listClasses`: List the document classes defined in the workspace. Set include_unknown=true to also return the built-in "unknown" class.
* **List Dataset Names** `listDatasetNames`: List every dataset name in use in the workspace. Datasets are free-form string groupings assigned to documents at submission time.
* **List Documents** `listDocuments`: List documents submitted to DocuPipe, optionally filtered by dataset and creation-timestamp window, with limit/offset paging. Set exclude_payload=false to include the parsed result payload.
* **List Extractions** `listExtractions`: List extraction records (standardization and reasoning outputs), filterable by extraction id, schema, document or extraction type, with limit/offset paging.
* **List Jobs** `listJobs`: List processing jobs, filterable by date range, status, job type, schema or document, with limit/offset paging. Each job reports credits consumed.
* **List Redactions** `listRedactions`: List redaction records produced by DocuPipe redact workflow steps. Undocumented in DocuPipe's OpenAPI spec but live. Returns a paginated envelope { items, total }.
* **List Reviews** `listReviews`: List the human reviews in the workspace with limit/offset paging. Set include_data=true to include each review's extracted data payload.
* **List Schemas** `listSchemas`: List the extraction schemas defined in the workspace, with limit/offset paging. Set exclude_payload=true to omit the full jsonSchema body.
* **List Standardizations** `listStandardizations`: List standardizations (structured extraction results), optionally filtered by schema, document or explicit id list, with limit/offset paging.
* **List Webhook Endpoints** `listWebhookEndpoints`: List the webhook endpoints registered for this workspace, with their URLs, subscribed events and disabled flag. SECURITY: entries may carry the Svix signing secret - treat the response as sensitive.
* **List Workflows** `listWorkflows`: List the on-submit workflows defined in the workspace, with their step configuration and trigger definition.
* **List Workflows V2** `listWorkflowsV2`: List V2 node-graph workflows with their status, runnable flag, inputs, steps, schemaIds and outputs. UNDOCUMENTED: not in the DocuPipe OpenAPI spec but live and returning 200; proven by live sweep.
* **Match Standardization To Candidates** `matchStandardization`: Enterprise record-matching: given one standardization and a list of candidate records, return the matching records plus the model's reasoning. Useful for reconciling an extracted invoice against ERP rows.
* **Merge Documents** `mergeDocuments`: Merge several processed documents into a single new document under the given filename. Returns a jobId to poll. METERED: consumes credits.
* **Merge Standardizations** `mergeStandardizations`: Combine several standardizations of the same document into one merged standardization record. Returns the merged standardizationId, item count and credits consumed.
* **Query Standardizations** `queryStandardizations`: Ask a natural-language question over all standardizations produced with a given schema and receive the matching standardization records. Optionally scope to one dataset.
* **Register Webhook Endpoint** `registerWebhookEndpoint`: Register a webhook endpoint URL for this workspace and return its endpointId. Pass subscribedEvents to receive only those event types; omit it to receive all 18. Deliveries are Svix-signed (svix-id, svix-timestamp, svix-signature).
* **Retrieve Analysis** `getAnalysis`: Retrieve one analysis by analysisId: the questions asked, the answers, confidence scores and citations back to the source documents.
* **Retrieve Detailed OCR Result** `getDocumentDetailed`: Retrieve the low-level OCR result for a document: per-page word boxes, selections, tables, figures, signatures, handwriting detection, orientation and plaintext.
* **Retrieve Job** `getJob`: Retrieve one processing job by jobId: its type, status, progress, credits consumed, processing time and any error message. Use this to poll asynchronous operations.
* **Retrieve Processed Document** `getDocument`: Retrieve a single processed document by documentId, including its parsed text/markdown result, filename, dataset, class assignments and page count.
* **Retrieve Redaction** `getRedaction`: Retrieve one redaction record by id. Undocumented in DocuPipe's OpenAPI spec but live; an unknown id answers 404 {"detail":"Redaction not found"}.
* **Retrieve Review By ID** `getReview`: Retrieve one human review by reviewId, including the extracted data under review and its verification status.
* **Retrieve Review By Standardization** `getReviewByStandardization`: Look up a review by the standardization it belongs to (standardization_id), or by review_id, and return its current extracted data and review status.
* **Retrieve Schema** `getSchema`: Retrieve one extraction schema by schemaId, including its jsonSchema definition, guidelines, field preview and origin.
* **Retrieve Standardization As PDF** `getStandardizationPdf`: Render one standardization as a PDF report of the extracted fields.
* **Retrieve Standardization As Plaintext** `getStandardizationText`: Return one standardization rendered as plaintext instead of JSON.
* **Retrieve Standardization As XML** `getStandardizationXml`: Return one standardization rendered as XML instead of JSON.
* **Retrieve Standardization JSON** `getStandardization`: Retrieve one standardization by id: the extracted structured data, the source documentId, schema used, field metadata and citations.
* **Retrieve Webhook Endpoint** `getWebhookEndpoint`: Retrieve one webhook endpoint by endpointId. SECURITY: the response includes the endpoint's Svix SIGNING SECRET, used to verify svix-id / svix-timestamp / svix-signature on deliveries. Treat every response from this action as a secret and do not log it.
* **Retrieve Workflow V2** `getWorkflowV2`: Retrieve one V2 node-graph workflow by workflowId. UNDOCUMENTED: not in the DocuPipe OpenAPI spec but live and returning 200; proven by live sweep. Missing ids answer 404 {"detail":"Workflow not found"}.
* **Run Workflow** `runWorkflow`: Run a V2 workflow explicitly over a list of inputs. Each input supplies either an existing documentId or a new document (base64 or url) plus optional labels, pages, dataset and metadata. METERED: consumes credits.
* **Search Documents** `searchDocuments`: Full-text search across parsed documents in the workspace. Requires a query string; optionally restrict to one dataset and page with limit/offset.
* **Search Schemas** `searchSchemas`: Search extraction schemas in the workspace by name or field text. Requires a query string; supports limit/offset paging.
* **Search Standardizations** `searchStandardizations`: Search standardizations by free text, optionally narrowed to one schema or dataset, with limit/offset paging.
* **Split Document** `splitDocument`: Split one multi-page document into several new documents using AI boundary detection, optionally guided by instructions. Returns a jobId to poll. METERED: consumes credits.
* **Standardize Document V2** `standardizeV2`: Synchronously standardize ONE document with the v2 extraction engine and return the standardization inline. Undocumented in DocuPipe's OpenAPI spec but live. Use standardizeBatchV2 for many documents, or standardizeV3 for the newer engine. METERED: consumes credits per page.
* **Standardize Document V3** `standardizeV3`: Run structured extraction (standardization) on one processed document against a schema, producing a standardizationId with the extracted JSON. This is the current V3 single-document endpoint. METERED: consumes credits.
* **Standardize Documents Batch V2** `standardizeBatchV2`: Legacy V2 batch standardization: run structured extraction across several documents at once against one schema, with split-mode and effort-level controls. Prefer Standardize Document V3 for new work. METERED: consumes credits.
* **Submit Document For Processing** `submitDocument`: Upload a document to DocuPipe for OCR and parsing. Supply either document.file.contents (base64 of the file) or document.url (a publicly reachable URL). Returns documentId and jobId. Max 3000 pages / 3000 MB, metadata max 10KB. METERED: parsing consumes account credits.
* **Update Document Metadata** `updateDocumentsMetadata`: Replace the metadata object on a list of documents. Metadata is arbitrary JSON, max 10KB per document.
* **Update Documents Dataset** `updateDocumentsDataset`: Reassign a list of documents to a different dataset. Datasets are free-form string groupings.
* **Update Review** `updateReview`: Submit a human review decision: set reviewStatus to verified, rejected or unverified, optionally supplying corrected extracted data.
* **Update Workflow** `updateWorkflow`: Replace the step configuration of an existing on-submit workflow, identified by workflowId in the URL. Supply the same step objects accepted by Create On-Submit Workflow.
* **Wait For Jobs** `waitForJobs`: Block until the given jobs finish or maxWaitSeconds elapses, then return whether all completed, whether any errored, and each job's final status. Use instead of polling Retrieve Job in a loop.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Classification Completed | `classification.processed.success` | A document classification job finished successfully. payloadSchema MODELLED, not captured. |
| Classification Failed | `classification.processed.error` | A document classification job failed. payloadSchema MODELLED, not captured. |
| Document Processed | `document.processed.success` | A submitted document finished OCR/parsing successfully. payloadSchema MODELLED from the Svix envelope DocuPipe delivers (vendor publishes no delivery sample); not captured from a real delivery. |
| Document Processing Failed | `document.processed.error` | A submitted document failed OCR/parsing. payloadSchema MODELLED, not captured. |
| Merge Completed | `merge.processed.success` | A document merge job finished successfully. payloadSchema MODELLED, not captured. |
| Merge Failed | `merge.processed.error` | A document merge job failed. payloadSchema MODELLED, not captured. |
| Review Generated | `review.processed.success` | A visual review batch was generated successfully. payloadSchema MODELLED, not captured. |
| Review Generation Failed | `review.processed.error` | A visual review batch failed to generate. payloadSchema MODELLED, not captured. |
| Review Rejected | `review.rejected.success` | A human rejected a review. payloadSchema MODELLED, not captured. |
| Review Verified | `review.verified.success` | A human marked a review as verified. payloadSchema MODELLED, not captured. |

<details>

<summary>See 8 more events</summary>

* **Schema Generated** `schema.processed.success`: A schema (created or autogenerated) finished processing. payloadSchema MODELLED, not captured.
* **Schema Generation Failed** `schema.processed.error`: A schema job failed. payloadSchema MODELLED, not captured.
* **Split Completed** `split.processed.success`: A document split job finished successfully. payloadSchema MODELLED, not captured.
* **Split Failed** `split.processed.error`: A document split job failed. payloadSchema MODELLED, not captured.
* **Standardization Completed** `standardization.processed.success`: A standardization (schema extraction) finished successfully. payloadSchema MODELLED, not captured.
* **Standardization Failed** `standardization.processed.error`: A standardization job failed. payloadSchema MODELLED, not captured.
* **Workflow Run Completed** `workflow.processed.success`: A workflow run finished successfully. payloadSchema MODELLED, not captured.
* **Workflow Run Failed** `workflow.processed.error`: A workflow run failed. payloadSchema MODELLED, not captured.

</details>
