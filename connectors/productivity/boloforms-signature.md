---
description: "BoloForms Signature (BoloSign) e-signature API."
hidden: true
---

# BoloForms Signature

<img src="../../.gitbook/assets/connectors/lg/boloforms-signature.png" alt="BoloForms Signature logo">

BoloForms Signature (BoloSign) e-signature API. List signature documents and PDF templates, send PDF/form templates for signing, fetch template respondents and form responses, void documents, and send reminders to pending signers.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [boloforms.com](https://boloforms.com) |
| **Authentication** | API key |
| **Slug** | `boloformsSignature` |

## Use it

Add BoloForms Signature from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.boloformsSignature.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Get Documents List | `getDocuments` | Retrieve BoloForms signature documents for the connected workspace. Returns single signature PDFs (documentType=PDF) or PDF templates (documentType=PDF_TEMPLATE), sorted by createdAt, with filtering by status, documentId, created-date range and archive flag, plus pagination. |
| Get Form Responses | `getFormResponses` | Retrieve submitted responses for a BoloForms signature form. Provide formId for a paginated list of responses, or responseId for a single response, including the answered fields and the finished PDF URL. |
| Get Template Respondents | `getTemplateRespondents` | Retrieve the respondent documents generated from a BoloForms PDF template, including each signer, their status and the signing history. Provide templateId for a paginated list, or respondentDocumentId for a single respondent document. |
| Send Form Template For Signing | `sendFormTemplateForSigning` | Send an existing BoloForms signature form template to receivers for completion and signing. Receivers need only a name and email; form templates have no roles. WARNING: this sends a real signature request email to every address in receiversList. |
| Send PDF Template For Signing | `sendPdfTemplateForSigning` | Create a signature document from an existing BoloForms PDF template and email it to the listed receivers. Each receiver's roleTitle must exactly match a role defined on the template. Optionally override the template PDF with base64 pdfData and substitute custom variables. WARNING: this sends a real signature request email to every address in receiversList. |
| Send Reminder To Signers | `sendReminder` | Email a signing reminder to every signer still pending on a BoloForms document. Pass the single signature PDF UUID with documentType PDF, or the template UUID together with the respondent responseId and documentType PDF_TEMPLATE. Rate limited by the vendor (HTTP 429). |
| Void Document | `voidDocument` | Void a BoloForms document so it can no longer be signed. Pass the single signature PDF UUID with documentType PDF, or the template UUID together with the respondent responseId and documentType PDF_TEMPLATE. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Form Response | `new_form_response` | A signer completed and submitted a signature form. Registration is UI-only: BoloForms Dashboard &gt; Settings &gt; Developers/Webhooks &gt; Add Webhook, enter your webhook URL, choose the Form Response event, and select the form(s) to track. Payload is an array of objects, one per selected document. Fields modelled from BoloSign docs (not captured from a live delivery). HMAC-SHA256 signature in x-bolosign-signature over `${x-bolosign-timestamp}.${JSON.stringify(payload)}`. |
| Signature Completed | `new_signature_pdf_completed` | All signers finished a single signature PDF (document fully completed). Registration is UI-only: Dashboard &gt; Webhooks &gt; Add Webhook, choose Signature Completed, select the PDF document(s). Fields modelled from BoloSign docs. |
| Signature PDF Individual Signed | `new_signature_pdf_individual_signed` | An individual signer completed their signature on a single signature PDF. Registration is UI-only (Dashboard &gt; Webhooks). Fields modelled from BoloSign docs. |
| Signature PDF Individual Viewed | `new_signature_pdf_individual_viewed` | An individual signer opened a single signature PDF. Registration is UI-only (Dashboard &gt; Webhooks &gt; Add Webhook, select a signature event and the PDF document(s)). Fields modelled from BoloSign docs. |
| Template Individual Signed | `new_template_response_individual_signed` | An individual signer completed their signature on a template-based document. Registration is UI-only (Dashboard &gt; Webhooks). Fields modelled from BoloSign docs. |
| Template Individual Viewed | `new_template_response_individual_viewed` | An individual signer opened a template-based document. Registration is UI-only (Dashboard &gt; Webhooks). Fields modelled from BoloSign docs. |
| Template Response | `new_template_response` | A response was received for a template-based document (e.g. a contract or agreement). Registration is UI-only: Dashboard &gt; Webhooks &gt; Add Webhook, choose Template Response, select the template(s). Fields modelled from BoloSign docs. |
