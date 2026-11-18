---
description: "Conversion Tools is a file-conversion API covering 100+ formats (XML, JSON, CSV, Excel, PDF, Word, images, audio/video, OCR)."
hidden: true
---

# Conversion Tools

Conversion Tools is a file-conversion API covering 100+ formats (XML, JSON, CSV, Excel, PDF, Word, images, audio/video, OCR). This connector wraps the full api.conversiontools.io v1 API: token verification, account info, plan configuration and usage, direct and resumable (upload-session) file uploads, conversion task creation with sandbox mode, task listing and polling, retention control and immediate file deletion, file metadata, authenticated downloads and temporary unauthenticated download links.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [conversiontools.io](https://conversiontools.io) |
| **Authentication** | Bearer token |
| **Actions** | 16 |
| **Events** | 2 |
| **Slug** | `conversionTools` |

## Use it

Add Conversion Tools from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.conversionTools.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Conversion Task | `createConversionTask` | Start a file conversion. Supply the conversion type (for example convert.xml_to_json, convert.pdf_to_text, convert.website_to_pdf) and an options object holding either file_id (from Upload File / Upload File To Session) or url for website conversions, plus any converter-specific options. Returns a task_id to poll with Get Conversion Task Status. WARNING: this is the only metered call in the API - it consumes one conversion from the plan allowance. Set options.sandbox to true to test without consuming quota; the task then returns mock data in 2-5 seconds. Optionally set callbackUrl to receive a completion webhook. |
| Create Temporary Download Link | `createTemporaryDownloadLink` | Mint a short-lived download_id for a file so a system that cannot send the API token can fetch it. SECURITY WARNING: the resulting URL https://api.conversiontools.io/v1/files/{download_id}/download serves the full file to ANYONE who has the id, with no Authorization header. Treat the download_id as a secret equivalent to the file itself and do not log or forward it. Does not consume quota. |
| Create Upload Session | `createUploadSession` | Mint a one-time upload URL for a large or binary file. Returns upload_url, the file_id the bytes will land under, and expires_in seconds (300). The bytes are then PUT to upload_url with no Authorization header - the session id in the URL is the credential - using Upload File To Session or any HTTP client. The window is short, so start the upload immediately. Does not consume quota. |
| Delete Task Files Now | `deleteTaskFilesNow` | Permanently delete every file associated with a task (source, result and artifacts) immediately instead of waiting for the retention window. Irreversible - afterwards the download endpoints return 410 Gone. Paid plans only; on a free plan the vendor returns 403 {"error": "This feature requires a paid plan"}. Success is 202 with message "File deletion scheduled" and a dateDeleted timestamp. Does not consume quota. |
| Download File Content | `downloadFileContent` | Download a file by id using the account's API token - typically the result of a completed conversion task. Returns the raw file bytes as application/octet-stream with a Content-Disposition filename. Text results come back as text; binary results are returned as-is and may not render usefully inside a JSON workflow. Does not consume quota. Files are removed when the task's retention window expires (24 hours by default), after which this returns 410 Gone. |
| Fetch File By Download Link | `fetchFileByDownloadLink` | Fetch a file using a download_id minted by Create Temporary Download Link. This endpoint requires NO authentication - the download_id alone grants access to the file contents, so treat it as a secret. Returns the raw bytes as application/octet-stream. Does not consume quota. |
| Get Account Email | `getAccountEmail` | Return the email address of the account the API token belongs to. Does not consume quota. Response: {"email": "user@example.com", "error": null}. |
| Get Conversion Task Status | `getConversionTaskStatus` | Poll a conversion task. Returns status (PENDING, RUNNING, SUCCESS or ERROR), conversionProgress, and, once SUCCESS, the result file_id to pass to Download File Content or Get File Metadata. On ERROR the error field carries the machine code, e.g. SOURCE_FILE_VALIDATION_ERROR. Poll every 5-10 seconds. Does not consume quota. |
| Get File Metadata | `getFileMetadata` | Return metadata for an uploaded or converted file: byte size, stored name, and for text files a short preview of the first lines. Useful for confirming what was actually stored when an extension lies about the contents. Does not consume quota. |
| Get Plan Configuration | `getPlanConfiguration` | Return the account's API configuration: the conversion types enabled for the plan, the subscription status, and whether the subscription can currently be paused or resumed. Does not consume quota. |
| Get Usage And Quota | `getUsageAndQuota` | Return the account's current conversion allowance: plan name, pages used, page limit, pages remaining and the date the counter resets. Call this before running conversions to check the remaining budget. Does not consume quota. (Undocumented in the vendor OpenAPI spec but live and stable.) |
| List Conversion Tasks | `listConversionTasks` | List the account's most recent conversion tasks (up to 50), optionally filtered by status. Each row carries id, type, title, status, error, dateCreated, dateFinished, conversionProgress, retentionMode, dateExpires and the source/result file references. Does not consume quota. |
| Update Task Retention Mode | `updateTaskRetentionMode` | Change how long a task's files are kept. standard_24h (the default) deletes source and result 24 hours after conversion; ttl_15m shortens that to 15 minutes and requires a paid plan - on a free plan the vendor returns 403 {"error": "ttl_15m retention requires a paid plan"}. The response echoes the effective retentionMode and the recomputed dateExpires. Does not consume quota. |
| Upload File | `uploadFile` | Upload a TEXT file to Conversion Tools and receive a file_id to use as options.file_id in Create Conversion Task. Pass the file's contents as fileContent plus a filename. Uploading does not consume conversion quota; the maximum size is the plan's x-ratelimit-limit-filesize (20 MB on the free plan). LIMITATION: the fastn engine cannot send binary multipart parts, so this action handles text formats only (XML, JSON, CSV, HTML, Markdown, TXT, SVG). For binary sources (PDF, Office, images, audio, video) use Create Upload Session and PUT the bytes to the returned upload_url from outside the engine, or supply a public url in the conversion options instead. |
| Upload File To Session | `uploadFileToSession` | PUT the file bytes to an upload session created by Create Upload Session. Pass the session id from the returned upload_url. The session id is the credential, so no Authorization header is sent. Returns file_id, filename and the stored size - always assert size is non-zero, because a request that carries no body still returns 200 with size 0. LIMITATION: the fastn engine cannot send binary multipart parts, so through the engine this action carries text content only; binary bytes must be PUT to upload_url from outside the engine. Does not consume quota. |
| Verify API Token | `verifyApiToken` | Check that the stored Conversion Tools API token is valid. Calls the API root, which returns {"error": null} on success and 401 {"error": "Not authorized"} for a missing, malformed or unknown token. Does not consume quota. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Conversion task failed | `ERROR` | Fired when a conversion task ends in ERROR. Registration is identical to the success event: there is no webhook registration API on Conversion Tools, so the fastn webhook URL must be passed as the callbackUrl input of 'Create Conversion Task' for each task you want notified. The error field carries a machine code such as SOURCE_FILE_VALIDATION_ERROR. PAYLOAD IS MODELLED from the GET /v1/tasks/{task_id} response body, not captured from a live delivery - the vendor publishes no callback payload schema. |
| Conversion task succeeded | `SUCCESS` | Fired when a conversion task finishes successfully. Conversion Tools has NO webhook registration API - there is no /webhooks endpoint and no subscription list. The only callback mechanism is the per-task callbackUrl field. REGISTRATION (manual, per task): copy this trigger's fastn webhook URL and pass it as the callbackUrl input of the 'Create Conversion Task' action (or set Callback URL in the Conversion Tools web app under the task form at https://conversiontools.io/conversion). Conversion Tools then POSTs the task record to that URL once the task leaves the RUNNING state. To stop receiving deliveries, omit callbackUrl on subsequent tasks; existing tasks cannot be unsubscribed. PAYLOAD IS MODELLED, NOT CAPTURED - the vendor documents callbackUrl only as 'Webhook URL for task completion notification' (openapi.yaml TaskCreateRequest.callbackUrl) and publishes no payload schema; the fields below mirror the GET /v1/tasks/{task_id} response body, which is what the callback reports. |
