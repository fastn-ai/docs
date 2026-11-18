---
description: "Transloadit API2 — file uploading and encoding: Assemblies, Templates, Template Credentials, Auth Keys, DAM (Storage) assets, queues, billing, assembly…"
hidden: true
---

# Transloadit

<img src="../../.gitbook/assets/connectors/lg/transloadit.png" alt="Transloadit logo">

Transloadit API2 — file uploading and encoding: Assemblies, Templates, Template Credentials, Auth Keys, DAM (Storage) assets, queues, billing, assembly notifications and tus resumable uploads.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [transloadit.com](https://transloadit.com) |
| **Authentication** | Credentials you enter, OAuth 2.0 |
| **Slug** | `transloadit` |

## Use it

Add Transloadit from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.transloadit.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Bulk Delete Storage Assets | `bulkDeleteDamAssets` | Delete several Transloadit Storage assets in one call. POST https://api2.transloadit.com/dam/assets/bulk/delete. Scope dam:write. Irreversible. |
| Bulk Move Storage Assets | `bulkMoveDamAssets` | Move several Transloadit Storage assets to another folder in one call. POST https://api2.transloadit.com/dam/assets/bulk/move. Scope dam:write. |
| Cancel Assembly | `cancelAssembly` | Cancel a running Assembly and stop billing for it. DELETE https://{assembly_host}/assemblies/{assembly_id}, where assembly_host is the host of the Assembly's own assembly_ssl_url. IMPORTANT: sending this DELETE to api2.transloadit.com answers 200 but does NOT cancel - it must go to the assembly's own instance host. Returns ASSEMBLY_CANCELED. |
| Create Assembly | `createAssembly` | Create a new Assembly (an encoding job). POST https://api2.transloadit.com/assemblies. Pass Assembly Instructions as `steps` (a JSON string) and/or a `template_id`. Set num_expected_upload_files above 0 to hold the Assembly in ASSEMBLY_UPLOADING so files can be added with Create Resumable Upload; pass 0 to execute immediately. Returns the Assembly Status including assembly_id, assembly_ssl_url, update_stream_url and tus_url. Authenticated with the Workspace Auth Key inside the multipart `params` field. |
| Create Assembly With Supplied Id | `createAssemblyWithId` | Create an Assembly under an id you choose, so the status URL is known before the request completes. PUT https://api2.transloadit.com/assemblies/{assembly_id} with a 32-character hex id. Same params as Create Assembly. |
| Create Auth Key | `createAuthKey` | Create a new Auth Key for the Workspace. POST https://api2.transloadit.com/auth_keys. Scope auth_keys:write. The response contains the new key and its secret, so treat it as a credential. |
| Create Bearer Token | `createBearerToken` | Exchange the Workspace Auth Key and Auth Secret for a short-lived bearer token (OAuth 2.0 client_credentials). POST https://api2.transloadit.com/token. Pass basic_credentials as base64("authKey:authSecret"). A bearer token satisfies Signature Authentication, so use it instead of signing each request. Prefer the connector's "Bearer Token (Auth Key + Auth Secret)" auth method, which performs this exchange automatically. |
| Create Resumable Upload | `createResumableUpload` | Start a tus resumable upload into a waiting Assembly. POST to the Assembly's tus host with Upload-Length and an Upload-Metadata header carrying base64 values for assembly_url, filename and fieldname. Answers 201 with the upload URL in the Location header. The Assembly must have been created with num_expected_upload_files above 0, otherwise the server replies "no active Assembly found". |
| Create Template | `createTemplate` | Create a new Template. POST https://api2.transloadit.com/templates. Scope templates:write. `params` must contain name and template, e.g. {"name":"resize-images","template":{"steps":{...}}}. |
| Create Template Credential | `createTemplateCredential` | Store a new Template Credential (e.g. an S3 bucket's keys) so Templates can reference it by name. POST https://api2.transloadit.com/template_credentials. Scope template_credentials:write. |

<details>

<summary>See 27 more actions</summary>

* **Delete Auth Key** `deleteAuthKey`: Delete an Auth Key. DELETE https://api2.transloadit.com/auth_keys/{auth_key_id}. Scope auth_keys:write. DANGEROUS: deleting the Auth Key your own connection uses permanently locks this connection out of the Workspace. Never pass the api_auth_key_id returned by your own Assembly responses.
* **Delete Template** `deleteTemplate`: Delete a Template by id or name. DELETE https://api2.transloadit.com/templates/{template_id}. Scope templates:write. Irreversible.
* **Delete Template Credential** `deleteTemplateCredential`: Delete a Template Credential by id. DELETE https://api2.transloadit.com/template_credentials/{credentials_id}. Scope template_credentials:write. Irreversible.
* **Download Resumable Upload** `downloadResumableUpload`: Read back the bytes already stored for a tus upload. GET https://{upload_host}/resumable/files/{upload_id}. Answers 200 with the uploaded file content.
* **Get Assembly Statistics** `getAssemblyStats`: Retrieve aggregated Assembly statistics for the Workspace. GET https://api2.transloadit.com/assembly_stats. Scope assemblies:read. Pass {} in `params` with a bearer token.
* **Get Assembly Status** `getAssembly`: Retrieve the current status and results of one Assembly. GET https://api2.transloadit.com/assemblies/{assembly_id}. This is a capability URL - knowing the Assembly id is the authentication, no signature or token is needed.
* **Get Monthly Bill** `getBill`: Retrieve the Workspace's bill for one month. GET https://api2.transloadit.com/bill/{bill_year_month} with bill_year_month formatted YYYY-MM. Scope billing:read. Returns usage, invoice total and per-service breakdown.
* **Get Priority Job Slot Statistics** `getPriorityJobSlotStats`: Retrieve historical priority job slot usage statistics. GET https://api2.transloadit.com/priority_job_slot_stats. Scope queues:read.
* **Get Template** `getTemplate`: Retrieve one Template by id or name. GET https://api2.transloadit.com/templates/{template_id}. Scope templates:read.
* **Get Template Credential** `getTemplateCredential`: Retrieve one Template Credential. GET https://api2.transloadit.com/template_credentials/{credentials_id}. Scope template_credentials:read.
* **Get Used Job Slots** `getJobSlots`: Retrieve the priority job slots currently in use by the Workspace. GET https://api2.transloadit.com/queues/job_slots. Scope queues:read.
* **List Assemblies** `listAssemblies`: List the Workspace's Assemblies. GET https://api2.transloadit.com/assemblies. Scope assemblies:read. Supply `params` as a JSON string (supports page, pagesize, type, fromdate, todate, keywords, order_by). With the Bearer Token auth method pass {} ; with Auth Key auth the params must contain auth.key, auth.expires and a matching `signature`.
* **List Assembly Notifications** `listAssemblyNotifications`: List the notification webhook deliveries recorded for one Assembly, with each attempt's response code and body. GET https://api2.transloadit.com/assembly_notifications/{assembly_id}. Capability URL - the Assembly id is the authentication.
* **List Auth Key Scopes** `listAuthKeyScopes`: List every scope string an Auth Key or bearer token can be granted (assemblies:read, templates:write, billing:read, ...). GET https://api2.transloadit.com/auth_keys/scopes.
* **List Auth Keys** `listAuthKeys`: List the Workspace's Auth Keys (ids, labels and scopes only). GET https://api2.transloadit.com/auth_keys. Scope auth_keys:read.
* **List Template Credential Types** `listTemplateCredentialTypes`: List the storage/service types a Template Credential can be created for (s3, google_storage, ftp, sftp, ...). GET https://api2.transloadit.com/template_credentials/types.
* **List Template Credentials** `listTemplateCredentials`: List the Workspace's Template Credentials (stored third-party storage credentials). GET https://api2.transloadit.com/template_credentials. Scope template_credentials:read.
* **List Templates** `listTemplates`: List the Templates available to the Workspace. GET https://api2.transloadit.com/templates. Scope templates:read. `params` supports page, pagesize, sort, order, fromdate, todate, keywords.
* **Replay Assembly** `replayAssembly`: Re-run a finished Assembly, optionally with changed Steps. POST https://api2.transloadit.com/assemblies/{assembly_id}/replay. Scope assemblies:write. Replaying consumes encoding minutes again.
* **Replay Assembly Notification** `replayAssemblyNotification`: Re-deliver an Assembly's completion notification webhook. POST https://api2.transloadit.com/assembly_notifications/{assembly_id}/replay. Scope assemblies:write. Use after fixing a notify_url endpoint that failed.
* **Show Auth Key Secret** `showAuthKeySecret`: Reveal the Auth Secret belonging to an Auth Key. POST https://api2.transloadit.com/auth_keys/show_secret/{auth_key_id}. Scope auth_keys:read. SECURITY: the response body contains a live Workspace credential - anything that can run this action can read the secret that signs every other request.
* **Stream Assembly Updates** `streamAssemblyUpdates`: Open the Server-Sent-Events stream that pushes an Assembly's status as it changes. The Assembly response returns update_stream_url as https://{host}/{streamPath}?assembly={id} - pass those three parts. The response is an open-ended text/event-stream, so this action suits a client that reads incrementally; a plain request/response call will block until the stream closes.
* **Terminate Resumable Upload** `terminateResumableUpload`: Abandon a tus upload and free its storage. DELETE https://{upload_host}/resumable/files/{upload_id}. Answers 204; the upload URL then returns 404.
* **Update Auth Key** `updateAuthKey`: Edit an Auth Key's label or scopes. PUT https://api2.transloadit.com/auth_keys/{auth_key_id}. Scope auth_keys:write. Do not edit the Auth Key your own connection authenticates with.
* **Update Template** `updateTemplate`: Edit an existing Template. PUT https://api2.transloadit.com/templates/{template_id}. Scope templates:write. `params` may contain name and/or template.
* **Update Template Credential** `updateTemplateCredential`: Edit an existing Template Credential. PUT https://api2.transloadit.com/template_credentials/{credentials_id}. Scope template_credentials:write.
* **Upload Resumable File Bytes** `uploadResumableFileBytes`: Send file bytes to a tus upload. PATCH https://{upload_host}/resumable/files/{upload_id} with Content-Type application/offset+octet-stream and the byte offset to continue from. Answers 204 with the new Upload-Offset. Note: the fastn HTTP engine sends the body as text, so this action is reliable for text-like payloads; true binary chunks are an engine limitation.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Assembly canceled | `ASSEMBLY_CANCELED` | An Assembly was canceled before finishing (DELETE on its assembly_ssl_url). Same form-encoded transloadit + signature payload; the inner Assembly Status carries ok=ASSEMBLY_CANCELED. |
| Assembly Canceled | `ASSEMBLY_CANCELED` | An Assembly was canceled via Cancel Assembly before it finished. Delivered to the same notify_url as ASSEMBLY_COMPLETED; wire it the same way. |
| Assembly completed | `ASSEMBLY_COMPLETED` | An Assembly finished successfully. Delivered as an x-www-form-urlencoded POST whose transloadit field holds the serialized Assembly Status JSON and whose signature field holds its lowercase hex HMAC-SHA1, keyed with the Auth Secret of the Auth Key that created the Assembly. Register by setting notify_url on the Assembly. |
| Assembly Completed | `ASSEMBLY_COMPLETED` | An Assembly finished successfully. Delivered as an Assembly Notification: Transloadit POSTs the full Assembly Status to the notify_url. WIRING: pass the fastn webhook URL as the notify_url input of Create Assembly / Create Assembly With Supplied Id, or set Notify URL on a Template in the console (Templates &gt; edit &gt; Notify URL). There is no registration API. Use List Assembly Notifications to audit deliveries and Replay Assembly Notification to redeliver. |
| Assembly Executing | `ASSEMBLY_EXECUTING` | An Assembly moved into execution. Delivered to notify_url when execution-progress notifications are enabled on the workspace; wire it the same way as ASSEMBLY_COMPLETED. |
| Assembly failed | `ASSEMBLY_CRASHED` | An Assembly reached a terminal error state. Same form-encoded transloadit + signature payload; the inner Assembly Status carries an error field instead of a successful ok. |
| Assembly Replaying | `ASSEMBLY_REPLAYING` | An Assembly is being replayed via Replay Assembly. Delivered to notify_url; wire it the same way as ASSEMBLY_COMPLETED. |
| Assembly Uploading | `ASSEMBLY_UPLOADING` | An Assembly is still receiving its tus uploads. Delivered to notify_url when execution-progress notifications are enabled; wire it the same way as ASSEMBLY_COMPLETED. |
