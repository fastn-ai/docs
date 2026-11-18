---
description: "iLovePDF / iLoveAPI REST API v1 — PDF and image processing (merge, split, compress, OCR, convert, watermark, protect, edit, …) and electronic signature…"
hidden: true
---

# iLovePDF

<img src="../../.gitbook/assets/connectors/lg/ilovepdf.png" alt="iLovePDF logo">

iLovePDF / iLoveAPI REST API v1 — PDF and image processing (merge, split, compress, OCR, convert, watermark, protect, edit, …) and electronic signature requests. Two-stage auth: the stored project public key mints a short-lived (1 hour) JWT via POST /v1/auth; that JWT must be passed as the `jwt` input to every other action. Task work runs on a per-task worker host returned by Start, passed as the `server` input.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [ilovepdf.com](https://ilovepdf.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `ilovepdf` |

## Use it

Add iLovePDF from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.ilovepdf.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Connect Task | `connectTask` | Chains a new tool onto the output files of an already-processed task, without re-uploading. Returns the new task id and its files as { server_filename: filename } pairs to feed into Process. Requires the parent task to have produced output files; otherwise returns 400 TaskRestartError "No files found." |
| Create Signature Request | `createSignatureRequest` | Creates an electronic signature request on a task started with tool=sign and whose PDFs were already uploaded. BILLED: one e-signature credit per file, plus an SMS credit per signer given a phone. It also emails every receiver. Optional top-level fields (brand_name, brand_logo, subject_signer, message_signer, subject_cc, language, lock_order, expiration_days, signer_reminders, signer_reminder_days_cycle, uuid_visible, verify_enabled, certified, custom_int, custom_string) are forwarded verbatim. |
| Delete Task | `deleteTask` | Deletes a task and every file attached to it immediately (tasks otherwise self-delete after two hours). Returns { status: "TaskDeleted" }, or { upload_status: "UploadDeleted" } if the task had not been processed yet. |
| Delete Uploaded File | `deleteUploadedFile` | Removes a single already-uploaded file from a waiting task, by its server_filename. Returns { success: true }. |
| Download Signature Audit | `downloadSignatureAudit` | Downloads the audit trail PDF of a signature request. The request status must be completed. Binary body returns as a base64 envelope. Uses the worker host returned by Start Task with tool=sign. |
| Download Signature Original Files | `downloadSignatureOriginal` | Downloads the original (pre-signature) files of a signature request. A single uploaded file returns a PDF, several return a ZIP. Binary body returns as a base64 envelope. |
| Download Signed Files | `downloadSignedFiles` | Downloads the signed files of a signature request. Returns 400 unless the request status is completed. A single file returns a PDF, several return a ZIP. Binary body returns as a base64 envelope. |
| Download Task Files | `downloadTaskFiles` | STEP 4 of the processing workflow. Downloads the output of a processed task. A single output file is served directly; multiple outputs are served as a ZIP. Binary body is returned by the engine as a base64 envelope. Requires the task to be in TaskSuccess; a waiting or empty task returns 400 DownloadError. |
| Fix Receiver Email | `fixReceiverEmail` | Corrects a receiver's email address after a delivery failure and re-sends the invitation to the new address. Returns the updated receiver. |
| Fix Signer Phone | `fixSignerPhone` | Corrects a signer's mobile number after an SMS delivery failure. Digits only, international prefix first and no punctuation (e.g. 34737105892). Only applies to receivers of type signer. |

<details>

<summary>See 14 more actions</summary>

* **Get Account Info** `getAccountInfo`: Returns the project's remaining credit balance. Useful as a cheap connection health check.
* **Get Auth Token** `getAuthToken`: STEP 0 of every iLovePDF call. Exchanges the stored project public key for a short-lived signed JWT (valid 3660 seconds / ~1 hour). Returns { token }. Pass that token as the `jwt` input of every other action in this connector — the engine cannot chain calls, so the caller must carry it.
* **Get Receiver Info** `getReceiverInfo`: Returns one receiver (signer, validator or witness) of a signature request by that receiver's own token: name, email, phone, type, status and notes.
* **Get Signature Status** `getSignatureStatus`: Returns the full status of one signature request by its requester token: status (draft/sent/completed/voided/expired), files, signers/validators/witnesses with their individual statuses, expiry and reminder settings.
* **Get Task Status** `getTaskStatus`: Polls a single task on its worker host and returns its status (TaskWaiting, TaskProcessing, TaskSuccess, TaskSuccessWithWarnings, TaskError, TaskDeleted, TaskNotFound) plus file metadata once processed.
* **Increase Signature Expiration Days** `increaseSignatureExpirationDays`: Extends a signature request's expiry by the given number of days so receivers get extra time. Returns the full signature object with the new expires date.
* **List Signature Requests** `listSignatureRequests`: Lists the project's electronic signature requests, paginated. Returns [] when none exist. Page is 0-based.
* **List Tasks** `listTasks`: Lists the project's tasks and the metadata of their uploaded and result files, 50 per page. Authenticates with the stored project secret key (server-side only). Returns the string "Sorry, no tasks to show." when there are none.
* **Process Task** `processTask`: STEP 3 of the processing workflow. Runs the chosen tool over the uploaded files of a task. BILLED: consumes iLovePDF credits (varies by tool, file count and page count). Supply the files array exactly as returned by Upload ([{ server_filename, filename, password?, rotate? }]). Tool-specific options (e.g. compression_level, pages, rotate, watermark text, output_filename, packaged_filename, ignore_errors, custom_int, custom_string, webhook) are passed as additional top-level inputs and forwarded verbatim.
* **Send Signature Reminder** `sendSignatureReminder`: Emails a reminder to every receiver who has not finished their action. SENDS REAL EMAIL. Only works when the signature status is sent and mode is multiple (API-created requests always are). Vendor limit: 2 calls per day per request.
* **Start Task** `startTask`: STEP 1 of the processing workflow. Reserves a task for a given tool and returns the worker host (`server`) and the `task` id to use for Upload / Process / Download. Consumes no credits. Run Get Auth Token first and pass its token as `jwt`.
* **Start Task In Region** `startTaskInRegion`: Same as Start Task but pins the task to a data-residency region (eu or us). Returns the regional worker host and task id.
* **Upload File From URL** `uploadFileFromUrl`: STEP 2 of the processing workflow. Adds a file to an existing task by fetching it from a publicly reachable URL (`cloud_file`). Returns the `server_filename` to reference in Process. Consumes no credits. NOTE: the same route also accepts a local binary multipart upload (fields file / chunk / chunks); the fastn engine cannot emit binary multipart parts, so use a public URL instead.
* **Void Signature Request** `voidSignatureRequest`: Voids a signature request that is currently in progress. Once voided it is no longer accessible to any receiver. Returns the full signature object with status voided.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Signature request created | `signature.created` | Fires when an electronic signature request is created. UI-only registration: https://www.iloveapi.com/user/projects -&gt; project -&gt; Webhooks -&gt; Add webhook -&gt; paste the fastn trigger URL -&gt; tick 'signature.created' -&gt; Save. Requires an e-signature entitlement on the project. |
| Signer completed | `signature.signer.completed` | Fires when an individual signer finishes signing. UI-only registration: https://www.iloveapi.com/user/projects -&gt; project -&gt; Webhooks -&gt; Add webhook -&gt; paste the fastn trigger URL -&gt; tick 'signature.signer.completed' -&gt; Save. Payload carries both `signature` (as Get Signature Status) and `signer` (as Get Receiver Info). |
| Task completed | `task.completed` | Fires when a PDF/image processing task finishes successfully. REGISTRATION IS UI-ONLY — iLovePDF exposes no webhook-registration API. Click path: sign in at https://www.iloveapi.com/user/projects -&gt; open your project -&gt; Webhooks -&gt; Add webhook -&gt; paste the fastn trigger URL -&gt; tick the event 'task.completed' -&gt; Save. A per-call alternative exists: pass the `webhook` input on the Process Task action to receive this same payload at an already-registered URL. |
| Task failed | `task.failed` | Fires when a PDF/image processing task ends in error (status TaskError). Same UI-only registration: https://www.iloveapi.com/user/projects -&gt; project -&gt; Webhooks -&gt; Add webhook -&gt; paste the fastn trigger URL -&gt; tick 'task.failed' -&gt; Save. |
