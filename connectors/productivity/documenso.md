---
description: "Documenso open-source e-signature platform."
hidden: true
---

# Documenso

<img src="../../.gitbook/assets/connectors/lg/documenso.png" alt="Documenso logo">

Documenso open-source e-signature platform. Covers the v1 REST API (documents, recipients, fields, templates) and the v2 API (documents, envelopes, folders, templates, attachments, embedding presign tokens).

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [documenso.com](https://documenso.com) |
| **Authentication** | API key |
| **Slug** | `documenso` |

## Use it

Add Documenso from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.documenso.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Cancel Envelope | `cancelEnvelope` | Documenso v2: cancel a pending envelope so it can no longer be signed. Recipients may be notified. |
| Create Document | `createDocument` | Documenso v2: create a DRAFT document and receive a presigned uploadUrl for the PDF. Nothing is emailed until the document is distributed. |
| Create Document Attachment | `createDocumentAttachment` | Documenso v2: attach a labelled link to a document. data = {label, data} where data is the URL. |
| Create Document Field | `createDocumentField` | Documenso v2: place one field on a document. field = {type, recipientId, pageNumber, pageX, pageY, width, height, fieldMeta?}. |
| Create Document Fields (Bulk) | `createDocumentFields` | Documenso v2: place several fields on a document in one call. |
| Create Document Recipient | `createDocumentRecipient` | Documenso v2: add one recipient to a document. recipient = {email, name, role, signingOrder?, accessAuth?, actionAuth?}. |
| Create Document Recipients (Bulk) | `createDocumentRecipients` | Documenso v2: add several recipients to a document in one call. |
| Create Document With File Upload | `createDocumentWithFile` | Documenso v2: create a document by posting the PDF directly (multipart/form-data: payload JSON string + one or more file parts). The connector engine cannot emit binary multipart parts, so the file part cannot be sent from here and the vendor rejects the call with "Input not instance of File". Use Create Document (JSON) instead and PUT the PDF to the uploadUrl it returns. |
| Create Embedding Presign Token | `createEmbeddingPresignToken` | Documenso v2: mint a short-lived presign token for the embedded signing/authoring widgets. WARNING: the response contains a live credential - handle and log with care. |
| Create Envelope Attachment | `createEnvelopeAttachment` | Documenso v2: attach a labelled link to an envelope. data = {label, data}. |

<details>

<summary>See 99 more actions</summary>

* **Create Envelope Fields** `createEnvelopeFields`: Documenso v2: place one or more fields on an envelope. data = [{type, recipientId, envelopeItemId, page, positionX, positionY, width, height}].
* **Create Envelope Items** `createEnvelopeItems`: Documenso v2: add documents to an envelope. multipart/form-data: payload is a JSON string {"envelopeId":"envelope_..."}. File parts are not supported by the connector engine, so this call adds no binary files; it returns the envelope's item list.
* **Create Envelope Recipients** `createEnvelopeRecipients`: Documenso v2: add one or more recipients to an envelope. data = [{email, name, role, signingOrder?}].
* **Create Envelope With File Upload** `createEnvelopeWithFile`: Documenso v2: create an envelope (DOCUMENT or TEMPLATE) via multipart/form-data. payload is a JSON string, e.g. {"title":"Contract","type":"TEMPLATE"}. File parts are optional here, so this works from the connector even though the engine cannot emit binary multipart parts - add the PDFs afterwards. Proven: 200 with a text-only payload part.
* **Create Folder** `createFolder`: Documenso v2: create a folder for documents or templates.
* **Create Template** `createTemplate`: Documenso v2: create a template and receive a presigned uploadUrl for its PDF.
* **Create Template Direct Link** `createTemplateDirectLink`: Documenso v2: create a public direct signing link for a template.
* **Create Template Field** `createTemplateField`: Documenso v2: place one field on a template. field = {type, recipientId, pageNumber, pageX, pageY, width, height}.
* **Create Template Fields (Bulk)** `createTemplateFields`: Documenso v2: place several fields on a template in one call.
* **Create Template Recipient** `createTemplateRecipient`: Documenso v2: add one recipient placeholder to a template. recipient = {email, name, role, signingOrder?}.
* **Create Template Recipients (Bulk)** `createTemplateRecipients`: Documenso v2: add several recipient placeholders to a template in one call.
* **Create Template With File Upload** `createTemplateWithFile`: Documenso v2: create a template by posting the PDF directly (multipart/form-data: payload JSON string + file part). The connector engine cannot emit binary multipart parts, so the vendor rejects the call with "Input not instance of File". Use Create Template (JSON) instead and PUT the PDF to the uploadUrl it returns.
* **Delete Document** `deleteDocument`: Documenso v2: delete a document by id.
* **Delete Document Attachment** `deleteDocumentAttachment`: Documenso v2: delete a document attachment by its id.
* **Delete Document Field** `deleteDocumentField`: Documenso v2: delete one field from a document by field id.
* **Delete Document Recipient** `deleteDocumentRecipient`: Documenso v2: remove a recipient from a document by recipient id.
* **Delete Envelope** `deleteEnvelope`: Documenso v2: delete an envelope by id.
* **Delete Envelope Attachment** `deleteEnvelopeAttachment`: Documenso v2: delete an envelope attachment by its id.
* **Delete Envelope Field** `deleteEnvelopeField`: Documenso v2: delete one envelope field by id.
* **Delete Envelope Item** `deleteEnvelopeItem`: Documenso v2: remove one document from an envelope.
* **Delete Envelope Recipient** `deleteEnvelopeRecipient`: Documenso v2: remove a recipient from an envelope by recipient id.
* **Delete Folder** `deleteFolder`: Documenso v2: delete a folder by id.
* **Delete Template** `deleteTemplate`: Documenso v2: delete a template by id.
* **Delete Template Direct Link** `deleteTemplateDirectLink`: Documenso v2: remove a template's direct signing link.
* **Delete Template Field** `deleteTemplateField`: Documenso v2: delete one template field by id.
* **Delete Template Recipient** `deleteTemplateRecipient`: Documenso v2: remove a recipient placeholder from a template.
* **Distribute Document To Recipients** `distributeDocument`: Documenso v2: move a DRAFT document to PENDING and EMAIL every recipient their signing link. IRREVERSIBLE - real emails go to real people.
* **Distribute Envelope To Recipients** `distributeEnvelope`: Documenso v2: send an envelope out for signature. EMAILS every recipient - irreversible.
* **Download Document** `downloadDocument`: Documenso v2: get a download URL for a document PDF. version=original or signed.
* **Download Document (Beta)** `downloadDocumentBeta`: Documenso v2: beta variant of the document download URL endpoint.
* **Download Envelope Audit Log PDF** `downloadEnvelopeAuditLog`: Documenso v2: get a download URL for the envelope's audit-log PDF.
* **Download Envelope Certificate PDF** `downloadEnvelopeCertificate`: Documenso v2: get a download URL for the envelope's signing certificate PDF.
* **Download Envelope Item** `downloadEnvelopeItem`: Documenso v2: get a download URL for one document inside an envelope. version=original or signed.
* **Duplicate Document** `duplicateDocument`: Documenso v2: copy an existing document into a new DRAFT.
* **Duplicate Envelope** `duplicateEnvelope`: Documenso v2: copy an envelope, optionally carrying its recipients and fields.
* **Duplicate Template** `duplicateTemplate`: Documenso v2: copy an existing template.
* **Find Document Attachments** `findDocumentAttachments`: Documenso v2: list the attachments of a document.
* **Find Documents** `findDocuments`: Documenso v2: search and page through documents. Filters: query, status, source, templateId, folderId, hasExpiredRecipients.
* **Find Envelope Attachments** `findEnvelopeAttachments`: Documenso v2: list the attachments of an envelope. Prefer this over Find Document Attachments, which the vendor currently mis-routes.
* **Find Envelopes** `findEnvelopes`: Documenso v2: search and page through envelopes (the unified document/template object).
* **Find Folders** `findFolders`: Documenso v2: list document or template folders, optionally under a parent.
* **Find Templates** `findTemplates`: Documenso v2: search and page through templates.
* **Get Document** `getDocument`: Documenso v2: get a document with its recipients, fields and envelope items.
* **Get Document Field** `getDocumentField`: Documenso v2: get a single document field by id.
* **Get Document Recipient** `getDocumentRecipient`: Documenso v2: get a single document recipient by id.
* **Get Envelope** `getEnvelope`: Documenso v2: get an envelope with its recipients, fields and items.
* **Get Envelope Audit Log** `getEnvelopeAuditLog`: Documenso v2: page through an envelope's audit trail (creation, opens, signatures, distribution).
* **Get Envelope Field** `getEnvelopeField`: Documenso v2: get a single envelope field by id.
* **Get Envelope Recipient** `getEnvelopeRecipient`: Documenso v2: get a single envelope recipient by id, with its fields.
* **Get Many Documents By Id** `getManyDocuments`: Documenso v2: fetch several documents in one call by their ids.
* **Get Many Envelopes By Id** `getManyEnvelopes`: Documenso v2: fetch up to 20 envelopes in one call. ids is an OBJECT: {"type":"envelopeId"|"documentId"|"templateId","ids":[...]} - a bare array is rejected.
* **Get Many Templates By Id** `getManyTemplates`: Documenso v2: fetch several templates in one call by their ids.
* **Get Template** `getTemplate`: Documenso v2: get a template with its recipients and fields.
* **Get Template Field** `getTemplateField`: Documenso v2: get a single template field by id.
* **Get Template Recipient** `getTemplateRecipient`: Documenso v2: get a single template recipient by id.
* **Redistribute Document To Recipients** `redistributeDocument`: Documenso v2: re-email the signing request to the listed recipient ids of a PENDING document. Sends real email.
* **Redistribute Envelope To Recipients** `redistributeEnvelope`: Documenso v2: re-email the signing request to the listed recipients of a pending envelope.
* **Reject Envelope On Behalf Of Recipient** `rejectEnvelopeRecipient`: Documenso v2: record a signing rejection on behalf of a recipient. This changes the legal record of a live envelope and notifies the owner - never call it on a document you did not intend to reject.
* **Toggle Template Direct Link** `toggleTemplateDirectLink`: Documenso v2: enable or disable a template's direct signing link.
* **Update Document** `updateDocument`: Documenso v2: update a document's data (title, externalId, visibility, folderId) and/or its meta (subject, message, redirectUrl, signing options).
* **Update Document Attachment** `updateDocumentAttachment`: Documenso v2: update a document attachment's label or target.
* **Update Document Field** `updateDocumentField`: Documenso v2: update one field on a document. field must include its id.
* **Update Document Fields (Bulk)** `updateDocumentFields`: Documenso v2: update several document fields in one call.
* **Update Document Recipient** `updateDocumentRecipient`: Documenso v2: update one recipient on a document. recipient must include its id.
* **Update Document Recipients (Bulk)** `updateDocumentRecipients`: Documenso v2: update several document recipients in one call.
* **Update Envelope** `updateEnvelope`: Documenso v2: update an envelope's data (title, externalId, visibility, folderId, templateType) and/or meta.
* **Update Envelope Attachment** `updateEnvelopeAttachment`: Documenso v2: update an envelope attachment's label or target.
* **Update Envelope Fields** `updateEnvelopeFields`: Documenso v2: update one or more envelope fields; each entry must carry its field id.
* **Update Envelope Items** `updateEnvelopeItems`: Documenso v2: rename or reorder the documents inside an envelope. data = [{envelopeItemId, title?, order?}].
* **Update Envelope Recipients** `updateEnvelopeRecipients`: Documenso v2: update one or more envelope recipients; each entry must carry its recipient id.
* **Update Folder** `updateFolder`: Documenso v2: rename, re-parent, pin or change the visibility of a folder.
* **Update Template** `updateTemplate`: Documenso v2: update a template's data (title, visibility, public title/description, type, folderId) and/or meta.
* **Update Template Field** `updateTemplateField`: Documenso v2: update one template field; field must carry its id.
* **Update Template Fields (Bulk)** `updateTemplateFields`: Documenso v2: update several template fields in one call.
* **Update Template Recipient** `updateTemplateRecipient`: Documenso v2: update one template recipient; recipient must carry its id.
* **Update Template Recipients (Bulk)** `updateTemplateRecipients`: Documenso v2: update several template recipients in one call.
* **Use Envelope Template** `useEnvelope`: Documenso v2: turn a TEMPLATE envelope into a document envelope. multipart/form-data: payload is a JSON string {"envelopeId":"...","recipients":[{"id":N,"email":"..."}],"distributeDocument":false}. Keep distributeDocument false or the result is emailed to every recipient.
* **Use Template To Create Document** `useTemplate`: Documenso v2: turn a template into a document. Leave distributeDocument false (the default) to keep the result a DRAFT; setting it true EMAILS every recipient immediately.
* **V1 Add Document Field** `v1CreateDocumentField`: Documenso v1: place a field (SIGNATURE, INITIALS, NAME, EMAIL, DATE, TEXT, NUMBER, RADIO, CHECKBOX, DROPDOWN, FREE_SIGNATURE) on a draft document page for a recipient.
* **V1 Add Document Recipient** `v1CreateDocumentRecipient`: Documenso v1: add a recipient (SIGNER, APPROVER, CC, VIEWER, ASSISTANT) to a draft document.
* **V1 Create Document** `v1CreateDocument`: Documenso v1: create a DRAFT document and get a presigned S3 uploadUrl for the PDF. Does NOT send anything to signers. Returns {uploadUrl, documentId, recipients[]}.
* **V1 Create Document From Template** `v1CreateDocumentFromTemplate`: Documenso v1: create a DRAFT document from a template. Does not distribute it to signers.
* **V1 Create Template** `v1CreateTemplate`: Documenso v1: create a template and get a presigned S3 uploadUrl for its PDF.
* **V1 Delete Document** `v1DeleteDocument`: Documenso v1: delete a document by id. Sends an empty JSON object body: the vendor returns 500 "Server Error" for a DELETE carrying Content-Type: application/json with no body.
* **V1 Delete Document Field** `v1DeleteDocumentField`: Documenso v1: remove a field from a draft document. Sends an empty JSON object body: the vendor returns 500 "Server Error" for a DELETE that carries Content-Type: application/json with no body at all.
* **V1 Delete Document Recipient** `v1DeleteDocumentRecipient`: Documenso v1: remove a recipient from a draft document. Sends an empty JSON object body: the vendor returns 500 "Server Error" for a DELETE carrying Content-Type: application/json with no body.
* **V1 Delete Template** `v1DeleteTemplate`: Documenso v1: delete a template by id. Sends an empty JSON object body: the vendor returns 500 "Server Error" for a DELETE carrying Content-Type: application/json with no body.
* **V1 Download Document** `v1DownloadDocument`: Documenso v1: get a time-limited download URL for a document's PDF.
* **V1 Generate Document From Template** `v1GenerateDocumentFromTemplate`: Documenso v1: generate a document from a template with prefilled fields. Created as DRAFT unless distributed separately.
* **V1 Get Current Team** `v1GetCurrentTeam`: Documenso v1: return the team the API token belongs to, e.g. {"name":"Personal Team"}. Undocumented - absent from the published OpenAPI spec but live (proven: 200, while /me ZZZ-suffixed 404s). Useful as a cheap credential check. Does not return the token itself.
* **V1 Get Document** `v1GetDocument`: Documenso v1: get a single document by id, with its recipients.
* **V1 Get Template** `v1GetTemplate`: Documenso v1: get a single template by id.
* **V1 List Documents** `v1ListDocuments`: Documenso v1: list documents for the team, paginated. Returns {documents, totalPages}.
* **V1 List Templates** `v1ListTemplates`: Documenso v1: list templates for the team, paginated.
* **V1 Resend Document To Recipients** `v1ResendDocument`: Documenso v1: re-email the signing request to the given recipient ids of a PENDING document. Sends real email.
* **V1 Send Document For Signing** `v1SendDocument`: Documenso v1: move a DRAFT document to PENDING and EMAIL every recipient a signing link. IRREVERSIBLE - real emails are sent to real people. Set sendEmail=false to change status without emailing.
* **V1 Update Document Field** `v1UpdateDocumentField`: Documenso v1: move, resize, retype or re-assign a field on a draft document. The vendor requires the COMPLETE field object (recipientId, type, pageNumber, pageX, pageY, pageWidth, pageHeight) - a partial patch is rejected with a misleading 401 "Unauthorized".
* **V1 Update Document Recipient** `v1UpdateDocumentRecipient`: Documenso v1: update a recipient's name, email, role or signing order on a draft document.
* **Verify Embedding Presign Token** `verifyEmbeddingPresignToken`: Documenso v2: check whether an embedding presign token is still valid.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Document Cancelled | `DOCUMENT_CANCELLED` | The document was cancelled by its owner. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event. |
| Document Completed | `DOCUMENT_COMPLETED` | Every recipient has signed. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event. |
| Document Created | `DOCUMENT_CREATED` | A document was created. REGISTRATION IS UI-ONLY: Documenso exposes no webhook API to API-token clients (POST /api/trpc/webhook.createWebhook answers 401 'Invalid session or API token.' while document.find on the same router answers 200 with the same token). To register: app.documenso.com &gt; avatar menu (top right) &gt; Team settings &gt; Webhooks tab &gt; Create Webhook &gt; paste the fastn webhook URL, tick this event, optionally set a Secret (returned verbatim in the X-Documenso-Secret header) &gt; Create Webhook. Webhooks are team-only; a personal account cannot configure them. |
| Document Opened | `DOCUMENT_OPENED` | A recipient opened the document. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event. |
| Document Recipient Completed | `DOCUMENT_RECIPIENT_COMPLETED` | One recipient finished their part of the document. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event. |
| Document Rejected | `DOCUMENT_REJECTED` | A recipient rejected the document. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event. |
| Document Reminder Sent | `DOCUMENT_REMINDER_SENT` | A signing reminder was emailed to a recipient. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event. |
| Document Sent | `DOCUMENT_SENT` | A document was distributed to its recipients. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event. No API registration exists for API tokens. |
| Document Signed | `DOCUMENT_SIGNED` | A recipient signed the document. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event. |
| Recipient Expired | `RECIPIENT_EXPIRED` | A recipient's signing window expired. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event. |

<details>

<summary>See 4 more events</summary>

* **Template Created** `TEMPLATE_CREATED`: A template was created. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event.
* **Template Deleted** `TEMPLATE_DELETED`: A template was deleted. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event.
* **Template Updated** `TEMPLATE_UPDATED`: A template was updated. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event.
* **Template Used** `TEMPLATE_USED`: A template was turned into a document. Register at app.documenso.com &gt; avatar menu &gt; Team settings &gt; Webhooks &gt; Create Webhook, paste the fastn URL and tick this event.

</details>
