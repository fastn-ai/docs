---
description: "DocsAutomator document automation API: generate PDFs and Google Docs from Google Docs / Word / PDF templates, manage automations, inspect template…"
hidden: true
---

# DocsAutomator

<img src="../../.gitbook/assets/connectors/lg/docsautomator.png" alt="DocsAutomator logo">

DocsAutomator document automation API: generate PDFs and Google Docs from Google Docs / Word / PDF templates, manage automations, inspect template placeholders, monitor the generation queue and jobs, and manage e-signature signing sessions. Base URL https://api.docsautomator.co.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [docsautomator.co](https://docsautomator.co) |
| **Authentication** | Bearer token, OAuth 2.0 |
| **Slug** | `docsautomator` |

## Use it

Add DocsAutomator from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.docsautomator.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Signing Session | `cancelSigningSession` | Cancel an active eSign signing session, optionally recording a reason. Completed sessions cannot be cancelled. Returns { success: true, message: "Signing session has been cancelled" }. |
| Create Automation | `createAutomation` | Create a new automation. Requires title and dataSourceName (one of Airtable, API, ClickUp, Glide, Google Sheets, Make, n8n, Noloco, SmartSuite, Zapier). Optionally set docTemplateLink to a Google Doc template URL. Returns 201 { message, newAutomation } including newAutomation._id. |
| Create Document | `createDocument` | Generate a PDF / Google Doc from an automation's template. docId is the automation id. data holds the placeholder key-value pairs (line items as line_items_1, line_items_2 arrays). Set async true to get a jobId (HTTP 202) and poll Get Job Status. Requires a paid DocsAutomator plan - trial workspaces receive HTTP 402. |
| Delete Automation | `deleteAutomation` | Permanently delete an automation identified by docId. Irreversible - the automation and its template mapping are removed. Returns a success message. |
| Duplicate Automation | `duplicateAutomation` | Duplicate an existing automation, including its settings and template mapping. Returns { newAutomationId }. |
| Duplicate Google Doc Template | `duplicateGoogleDocTemplate` | Create a copy of the Google Doc template attached to an automation, optionally under a new name. Requires a linked Google account on the DocsAutomator workspace, otherwise HTTP 401 'No Google access permissions'. |
| Get Automation | `getAutomation` | Get a single automation by id. Supply automationId (or the alias docId). Returns { automation: {...} }. |
| Get Job Status | `getJobStatus` | Poll the status of an asynchronous document generation job created by Create Document with async=true. Returns the job state and, once finished, the generated document URLs. |
| Get Queue Statistics | `getQueueStats` | Get DocsAutomator document-generation queue counters: waiting, active, completed, failed and delayed jobs. |
| Get Signing Audit Trail | `getSigningAudit` | Get the legally relevant audit trail for an eSign session. Returns { sessionId, events[], reconstructed } where each event has eventType (session_created, invite_sent, invite_resent, document_opened, field_signed, document_accepted, signer_declined, session_completed, session_cancelled, session_expired, session_voided, reminder_sent, email_sent, email_send_failed), actor, metadata, ipAddress, userAgent, timestamp and geoLocation. |
| Get Signing Links | `getSigningLinks` | Get the per-signer signing URLs for an eSign session (used with deliveryMethod 'manual'). Returns { success, sessionId, documentName, deliveryMethod, status, signingLinks[] } with each link's expiry and signer status. SECURITY: a signing link embeds the signer's access token and lets the holder sign the document - treat the response as a secret and deliver each link only to its intended signer. |
| Get Signing Session | `getSigningSession` | Get full details of one eSign signing session: status, closeType, signingOrder, originalPdfUrl / signedPdfUrl, document hashes, esignFields, per-signer status with timestamps, IP and geolocation, and decline details. SECURITY: each signer object carries an accessToken that grants signing access, and the PDF URLs are unauthenticated file links - treat the response as sensitive. |
| List Automations | `listAutomations` | List all automations in the DocsAutomator workspace. Returns { automations: [...] } with each automation's _id, title, dataSource, template settings and options. |
| List Signing Sessions | `listSigningSessions` | List DocsAutomator eSign signing sessions, optionally filtered by status or signer email, with page/limit pagination. Returns { sessions, pagination }. |
| List Template Placeholders | `listPlaceholders` | List the placeholder names found in an automation's template (the v2 endpoint). Requires that a Google account be linked to the DocsAutomator workspace under Settings - otherwise the vendor returns HTTP 401 'No Google access permissions'. |
| List Template Placeholders (Legacy v1) | `listPlaceholdersLegacy` | Legacy v1 placeholder listing endpoint (undocumented but live). Takes docId rather than automationId. Prefer List Template Placeholders. Requires a linked Google account on the workspace, otherwise HTTP 401 'No Google access permissions'. |
| Resend Signing Invitation | `resendSigningInvite` | Re-send the signing invitation email to one signer of an eSign session. signerIndex is the signer's 1-based position as returned in the session's signers[].index (vendor docs: "indexed 1, 2, 3, etc."). Returns { success, message: "Invitation resent to &lt;email&gt;" }. Sends a real email to that signer. |
| Send Test Email | `sendTestEmail` | Send a test copy of an automation's configured 'send email' action to a recipient address. Rate limited by the vendor (the response carries rateLimit.remaining and resetAt). Sends a real email - only use an address you control. |
| Update Automation | `updateAutomation` | Update an automation's settings. docId identifies the automation and is sent in the query string. Any subset of title, docTemplateLink, newDocumentNameField, isActive, saveGoogleDoc, googleDocDestinationFolderUrl, locale, formatNumbersWithLocale, pdfExpiration, imageOptions may be supplied. Returns { message: 'Success', updatedAutomation }. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Document generated (Notify Webhook) | `document.generated` | Fires after a document is generated when the automation's 'Notify Webhook' action is configured. VENDOR LIMITATION: this payload carries NO 'event' field, so it does not match the connector's eventKey ('event') - identify it by the presence of pdfUrl. REGISTRATION IS UI-ONLY: app.docsautomator.co -&gt; open the automation -&gt; Actions card in the right rail -&gt; Add action -&gt; Notify Webhook -&gt; enter the fastn webhook URL -&gt; generate a preview document to test. |
| eSign email accepted by provider | `esign.email_sent` | Fires when a completion, progress, decline or expiration e-sign email is accepted by the mail provider. The delivery record is in metadata.delivery. REGISTRATION IS UI-ONLY: app.docsautomator.co -&gt; open the automation -&gt; eSign card -&gt; Signed PDF Delivery / Webhook -&gt; paste the fastn webhook URL -&gt; Save. |
| eSign email delivery failed | `esign.email_failed` | Fires when an e-sign email ends with delivery outcome failed or unknown. REGISTRATION IS UI-ONLY: app.docsautomator.co -&gt; open the automation -&gt; eSign card -&gt; Signed PDF Delivery / Webhook -&gt; paste the fastn webhook URL -&gt; Save. |
| eSign session completed (signed PDF ready) | `esign.session_completed` | Fires when all signers have finished and the signed PDF is ready. VENDOR LIMITATION: this payload carries NO 'event' field, so it does not match the connector's eventKey ('event') - identify it by signedPdfUrl plus status 'completed'. REGISTRATION IS UI-ONLY: app.docsautomator.co -&gt; open the automation -&gt; eSign card -&gt; Signed PDF Delivery -&gt; Send signed PDF to webhook -&gt; enter the fastn webhook URL -&gt; Save. |
| eSign session created (manual delivery) | `esign.session_created` | Fires when a signing session is created with deliveryMethod 'manual', carrying the signing links so you can distribute them yourself. REGISTRATION IS UI-ONLY - DocsAutomator exposes no webhook-registration API (probed: no /webhooks route, and updateAutomation silently discards notifyWebhook/webhookUrl). Click path: app.docsautomator.co -&gt; open the automation -&gt; eSign card -&gt; Signed PDF Delivery / Webhook -&gt; paste the fastn webhook URL -&gt; Save. |
| eSign session declined | `esign.session_declined` | Fires when a signer declines to sign or to accept. REGISTRATION IS UI-ONLY: app.docsautomator.co -&gt; open the automation -&gt; eSign card -&gt; Signed PDF Delivery / Webhook -&gt; paste the fastn webhook URL -&gt; Save. |
| eSign session expired | `esign.session_expired` | Fires when a signing session expires before all signers complete. Does not fire if the session was already declined, cancelled or completed. REGISTRATION IS UI-ONLY: app.docsautomator.co -&gt; open the automation -&gt; eSign card -&gt; Signed PDF Delivery / Webhook -&gt; paste the fastn webhook URL -&gt; Save. |
| eSign signer signed | `esign.signer_signed` | Fires once per signer as they complete their fields (or click Accept on an acceptance session), including the final signer. progress.allSigned is true for the last signer while the session status is still in_progress. REGISTRATION IS UI-ONLY: app.docsautomator.co -&gt; open the automation -&gt; eSign card -&gt; Signed PDF Delivery / Webhook -&gt; paste the fastn webhook URL -&gt; Save. |
