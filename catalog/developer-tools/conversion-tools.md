---
description: "Conversion Tools converts files between 100+ formats. Upload files, run conversion tasks, check their status and download results."
hidden: true
---

# Conversion Tools

<img src="../../.gitbook/assets/connectors/lg/conversion-tools.png" alt="Conversion Tools logo">

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [conversiontools.io](https://conversiontools.io) |
| **Authentication** | Access token |
| **Slug** | `conversionTools` |

## Setup

Your customers enter their access token for Conversion Tools when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect Conversion Tools from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Conversion Tools**.
2. Select **Connect** on the Conversion Tools card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Conversion Tools's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Create Conversion Task</td><td><code>createConversionTask</code></td><td>Start a file conversion. Supply the conversion type (for example convert.xml_to_json, convert.pdf_to_text, convert.website_to_pdf) and an options object holding either file_id (from Upload File / Upload File To Session) or url for website conversions, plus any converter-specific options. Returns a task_id to poll with Get Conversion Task Status. WARNING: this is the only metered call in the API - it consumes one conversion from the plan allowance. Set options.sandbox to true to test without consuming quota; the task then returns mock data in 2-5 seconds. Optionally set callbackUrl to receive a completion webhook.</td></tr><tr><td>Create Temporary Download Link</td><td><code>createTemporaryDownloadLink</code></td><td>Mint a short-lived download_id for a file so a system that cannot send the API token can fetch it. SECURITY WARNING: the resulting URL https://api.conversiontools.io/v1/files/{download_id}/download serves the full file to ANYONE who has the id, with no Authorization header. Treat the download_id as a secret equivalent to the file itself and do not log or forward it. Does not consume quota.</td></tr><tr><td>Create Upload Session</td><td><code>createUploadSession</code></td><td>Mint a one-time upload URL for a large or binary file. Returns upload_url, the file_id the bytes will land under, and expires_in seconds (300). The bytes are then PUT to upload_url with no Authorization header - the session id in the URL is the credential - using Upload File To Session or any HTTP client. The window is short, so start the upload immediately. Does not consume quota.</td></tr><tr><td>Delete Task Files Now</td><td><code>deleteTaskFilesNow</code></td><td>Permanently delete every file associated with a task (source, result and artifacts) immediately instead of waiting for the retention window. Irreversible - afterwards the download endpoints return 410 Gone. Paid plans only; on a free plan the vendor Success is 202 with message "File deletion scheduled" and a dateDeleted timestamp. Does not consume quota.</td></tr><tr><td>Download File Content</td><td><code>downloadFileContent</code></td><td>Download a file by id using the account's API token - typically the result of a completed conversion task. Returns the raw file bytes as application/octet-stream with a Content-Disposition filename. Text results come back as text; binary results are returned as-is and may not render usefully inside a JSON workflow. Does not consume quota. Files are removed when the task's retention window expires (24 hours by default), after which this</td></tr><tr><td>Fetch File By Download Link</td><td><code>fetchFileByDownloadLink</code></td><td>Fetch a file using a download_id minted by Create Temporary Download Link. This endpoint requires NO authentication - the download_id alone grants access to the file contents, so treat it as a secret. Returns the raw bytes as application/octet-stream. Does not consume quota.</td></tr><tr><td>Get Account Email</td><td><code>getAccountEmail</code></td><td>Return the email address of the account the API token belongs to. Does not consume quota. Response: {"email": "user@example.com", "error": null}.</td></tr><tr><td>Get Conversion Task Status</td><td><code>getConversionTaskStatus</code></td><td>Poll a conversion task. Returns status (PENDING, RUNNING, SUCCESS or ERROR), conversionProgress, and, once SUCCESS, the result file_id to pass to Download File Content or Get File Metadata. On ERROR the error field carries the machine code, e.g. SOURCE_FILE_VALIDATION_ERROR. Poll every 5-10 seconds. Does not consume quota.</td></tr><tr><td>Get File Metadata</td><td><code>getFileMetadata</code></td><td>Return metadata for an uploaded or converted file: byte size, stored name, and for text files a short preview of the first lines. Useful for confirming what was actually stored when an extension lies about the contents. Does not consume quota.</td></tr><tr><td>Get Plan Configuration</td><td><code>getPlanConfiguration</code></td><td>Return the account's API configuration: the conversion types enabled for the plan, the subscription status, and whether the subscription can currently be paused or resumed. Does not consume quota.</td></tr></tbody></table>

<details>

<summary>View 6 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Usage And Quota</td><td><code>getUsageAndQuota</code></td><td>Return the account's current conversion allowance: plan name, pages used, page limit, pages remaining and the date the counter resets. Call this before running conversions to check the remaining budget. Does not consume quota. (Undocumented in the vendor OpenAPI spec but live and stable.)</td></tr><tr><td>List Conversion Tasks</td><td><code>listConversionTasks</code></td><td>List the account's most recent conversion tasks (up to 50), optionally filtered by status. Each row carries id, type, title, status, error, dateCreated, dateFinished, conversionProgress, retentionMode, dateExpires and the source/result file references. Does not consume quota.</td></tr><tr><td>Update Task Retention Mode</td><td><code>updateTaskRetentionMode</code></td><td>Change how long a task's files are kept. standard_24h (the default) deletes source and result 24 hours after conversion; ttl_15m shortens that to 15 minutes and requires a paid plan - on a free plan the vendor The response echoes the effective retentionMode and the recomputed dateExpires. Does not consume quota.</td></tr><tr><td>Upload File</td><td><code>uploadFile</code></td><td>Upload a TEXT file to Conversion Tools and receive a file_id to use as options.file_id in Create Conversion Task. Pass the file's contents as fileContent plus a filename. Uploading does not consume conversion quota; the maximum size is the plan's x-ratelimit-limit-filesize (20 MB on the free plan). LIMITATION: the Fastn engine cannot send binary multipart parts, so this action handles text formats only (XML, JSON, CSV, HTML, Markdown, TXT, SVG). For binary sources (PDF, Office, images, audio, video) use Create Upload Session and PUT the bytes to the returned upload_url from outside the engine, or supply a public url in the conversion options instead.</td></tr><tr><td>Upload File To Session</td><td><code>uploadFileToSession</code></td><td>PUT the file bytes to an upload session created by Create Upload Session. Pass the session id from the returned upload_url. The session id is the credential, so no Authorization header is sent. Returns file_id, filename and the stored size - always assert size is non-zero, because a request that carries no body still LIMITATION: the Fastn engine cannot send binary multipart parts, so through the engine this action carries text content only; binary bytes must be PUT to upload_url from outside the engine. Does not consume quota.</td></tr><tr><td>Verify API Token</td><td><code>verifyApiToken</code></td><td>Check that the stored Conversion Tools API token is valid. Calls the API root, which returns {"error": null} on success and 401 {"error": "Not authorized"} for a missing, malformed or unknown token. Does not consume quota.</td></tr></tbody></table>

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Conversion task failed</td><td><code>ERROR</code></td><td>Fired when a conversion task ends in ERROR. Registration is identical to the success event: there is no webhook registration API on Conversion Tools, so the Fastn webhook URL must be passed as the callbackUrl input of 'Create Conversion Task' for each task you want notified. The error field carries a machine code such as SOURCE_FILE_VALIDATION_ERROR.</td></tr><tr><td>Conversion task succeeded</td><td><code>SUCCESS</code></td><td>Fired when a conversion task finishes successfully. Conversion Tools has NO webhook registration API - there is no /webhooks endpoint and no subscription list. The only callback mechanism is the per-task callbackUrl field. REGISTRATION (manual, per task): copy this trigger's Fastn webhook URL and pass it as the callbackUrl input of the 'Create Conversion Task' action (or set Callback URL in the Conversion Tools web app under the task form at https://conversiontools.io/conversion). Conversion Tools then POSTs the task record to that URL once the task leaves the RUNNING state. To stop receiving deliveries, omit callbackUrl on subsequent tasks; existing tasks cannot be unsubscribed.</td></tr></tbody></table>
