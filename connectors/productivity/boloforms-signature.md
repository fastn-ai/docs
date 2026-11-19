---
description: "BoloForms Signature (BoloSign) e-signature API."
hidden: true
---

# BoloForms Signature

<img src="../../.gitbook/assets/connectors/lg/boloforms-signature.png" alt="BoloForms Signature logo">

List signature documents and PDF templates, send PDF/form templates for signing, fetch template respondents and form responses, void documents, and send reminders to pending signers.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [boloforms.com](https://boloforms.com) |
| **Authentication** | API key |
| **Slug** | `boloformsSignature` |

## Use it

Add BoloForms Signature from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.boloformsSignature.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Documents List</td><td><code>getDocuments</code></td><td>Retrieve BoloForms signature documents for the connected workspace. Returns single signature PDFs (documentType=PDF) or PDF templates (documentType=PDF_TEMPLATE), sorted by createdAt, with filtering by status, documentId, created-date range and archive flag, plus pagination.</td></tr><tr><td>Get Form Responses</td><td><code>getFormResponses</code></td><td>Retrieve submitted responses for a BoloForms signature form. Provide formId for a paginated list of responses, or responseId for a single response, including the answered fields and the finished PDF URL.</td></tr><tr><td>Get Template Respondents</td><td><code>getTemplateRespondents</code></td><td>Retrieve the respondent documents generated from a BoloForms PDF template, including each signer, their status and the signing history. Provide templateId for a paginated list, or respondentDocumentId for a single respondent document.</td></tr><tr><td>Send Form Template For Signing</td><td><code>sendFormTemplateForSigning</code></td><td>Send an existing BoloForms signature form template to receivers for completion and signing. Receivers need only a name and email; form templates have no roles. WARNING: this sends a real signature request email to every address in receiversList.</td></tr><tr><td>Send PDF Template For Signing</td><td><code>sendPdfTemplateForSigning</code></td><td>Create a signature document from an existing BoloForms PDF template and email it to the listed receivers. Each receiver's roleTitle must exactly match a role defined on the template. Optionally override the template PDF with base64 pdfData and substitute custom variables. WARNING: this sends a real signature request email to every address in receiversList.</td></tr><tr><td>Send Reminder To Signers</td><td><code>sendReminder</code></td><td>Email a signing reminder to every signer still pending on a BoloForms document. Pass the single signature PDF UUID with documentType PDF, or the template UUID together with the respondent responseId and documentType PDF_TEMPLATE. Rate limited by the vendor (HTTP 429).</td></tr><tr><td>Void Document</td><td><code>voidDocument</code></td><td>Void a BoloForms document so it can no longer be signed. Pass the single signature PDF UUID with documentType PDF, or the template UUID together with the respondent responseId and documentType PDF_TEMPLATE.</td></tr></tbody></table>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

<table><thead><tr><th width="240">Event</th><th width="260">Id</th><th>When it fires</th></tr></thead><tbody><tr><td>Form Response</td><td><code>new_form_response</code></td><td>A signer completed and submitted a signature form. Registration is UI-only: BoloForms Dashboard &gt; Settings &gt; Developers/Webhooks &gt; Add Webhook, enter your webhook URL, choose the Form Response event, and select the form(s) to track. Payload is an array of objects, one per selected document. Fields modelled from BoloSign docs (not captured from a live delivery). HMAC-SHA256 signature in x-bolosign-signature over `${x-bolosign-timestamp}.${JSON.stringify(payload)}`.</td></tr><tr><td>Signature Completed</td><td><code>new_signature_pdf_completed</code></td><td>All signers finished a single signature PDF (document fully completed). Registration is UI-only: Dashboard &gt; Webhooks &gt; Add Webhook, choose Signature Completed, select the PDF document(s). Fields modelled from BoloSign docs.</td></tr><tr><td>Signature PDF Individual Signed</td><td><code>new_signature_pdf_individual_signed</code></td><td>An individual signer completed their signature on a single signature PDF. Registration is UI-only (Dashboard &gt; Webhooks). Fields modelled from BoloSign docs.</td></tr><tr><td>Signature PDF Individual Viewed</td><td><code>new_signature_pdf_individual_viewed</code></td><td>An individual signer opened a single signature PDF. Registration is UI-only (Dashboard &gt; Webhooks &gt; Add Webhook, select a signature event and the PDF document(s)). Fields modelled from BoloSign docs.</td></tr><tr><td>Template Individual Signed</td><td><code>new_template_response_individual_signed</code></td><td>An individual signer completed their signature on a template-based document. Registration is UI-only (Dashboard &gt; Webhooks). Fields modelled from BoloSign docs.</td></tr><tr><td>Template Individual Viewed</td><td><code>new_template_response_individual_viewed</code></td><td>An individual signer opened a template-based document. Registration is UI-only (Dashboard &gt; Webhooks). Fields modelled from BoloSign docs.</td></tr><tr><td>Template Response</td><td><code>new_template_response</code></td><td>A response was received for a template-based document (e.g. a contract or agreement). Registration is UI-only: Dashboard &gt; Webhooks &gt; Add Webhook, choose Template Response, select the template(s). Fields modelled from BoloSign docs.</td></tr></tbody></table>
