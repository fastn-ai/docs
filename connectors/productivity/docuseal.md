---
description: "DocuSeal is a document signing platform."
hidden: true
---

# DocuSeal

DocuSeal is a document signing platform. This connector covers the DocuSeal API: document templates built from PDF, DOCX or HTML, signature requests (submissions), submitters and their filled values, signed document downloads, and webhook endpoints for signing events.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [docuseal.com](https://docuseal.com) |
| **Authentication** | Credentials you enter |
| **Actions** | 30 |
| **Events** | 11 |
| **Slug** | `docuseal` |

## Use it

Add DocuSeal from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.docuseal.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Archive Submission | `archiveSubmission` | Archives a DocuSeal submission so it no longer appears in the active list and can no longer be signed. Use Update Submission with Archived set to false to restore it. |
| Archive Template | `archiveTemplate` | Archives a DocuSeal template so it no longer appears in the active list. Use Update Template with Archived set to false to restore it. |
| Clone Template | `cloneTemplate` | Copies an existing DocuSeal template into a new template, optionally under a different name and folder. DocuSeal appends "(Clone)" to the existing name when no name is given. |
| Create Submission | `createSubmission` | Creates a signature request from a DocuSeal template and, by default, emails it to every submitter. Set Send Email to false to create the request without notifying anyone and use the returned embed_src signing links instead. |
| Create Submission From DOCX | `createSubmissionFromDocx` | Creates a signature request directly from one or more Microsoft Word DOCX files, without first saving a template. By default DocuSeal emails every submitter; set Send Email to false to create the request silently. |
| Create Submission From Email List | `createSubmissionFromEmails` | Creates a signature request from a template for a plain list of email addresses, one submission per address, without having to build a submitters array. By default DocuSeal emails each address; set Send Email to false to create the requests silently. This endpoint is live on the DocuSeal API but is not listed in their published reference. |
| Create Submission From HTML | `createSubmissionFromHtml` | Creates a signature request directly from HTML content, without first saving a template. The HTML goes in the Documents array; a top-level html field alone is rejected with "template_ids or documents is required". By default DocuSeal emails every submitter; set Send Email to false to create the request silently. |
| Create Submission From PDF | `createSubmissionFromPdf` | Creates a signature request directly from one or more PDF files, without first saving a template. By default DocuSeal emails every submitter; set Send Email to false to create the request silently and use the returned signing links. |
| Create Template From DOCX | `createTemplateFromDocx` | Creates a fillable DocuSeal template from one or more Microsoft Word DOCX files. |
| Create Template From HTML | `createTemplateFromHtml` | Generates a DocuSeal PDF template from HTML content, with fillable fields declared as custom field tags such as &lt;text-field name="Full Name" role="First Party"&gt;. Use the Documents array to build a multi-document template, or the top-level HTML for a single document. |
| Create Template From PDF | `createTemplateFromPdf` | Creates a fillable DocuSeal template from one or more PDF files. Supply each file as base64 content or a public download URL. |
| Create Webhook URL | `createWebhookUrl` | Registers a webhook endpoint so DocuSeal posts signing events to your URL. New endpoints default to the four form.* events; pass Events to choose exactly which ones. This endpoint is live on the DocuSeal API but is not listed in their published reference. |
| Delete Webhook URL | `deleteWebhookUrl` | Permanently removes a DocuSeal webhook endpoint so DocuSeal stops posting events to it. This endpoint is live on the DocuSeal API but is not listed in their published reference. |
| Get Current User | `getCurrentUser` | Returns the DocuSeal account the API key belongs to. This endpoint is live on the DocuSeal API but is not listed in their published reference. |
| Get Submission | `getSubmission` | Retrieves one DocuSeal submission by id, including every submitter, the values they filled in, the signed documents and the audit log link. |
| Get Submission Documents | `getSubmissionDocuments` | Returns download links for the signed documents of a completed DocuSeal submission. |
| Get Submitter | `getSubmitter` | Retrieves one DocuSeal submitter by id, with their signing status, the values they filled in and their signed documents. |
| Get Template | `getTemplate` | Retrieves one DocuSeal template by id, including its documents, submitter roles, fields and field coordinates. |
| Get Webhook URL | `getWebhookUrl` | Retrieves one DocuSeal webhook endpoint by id, with the events it is subscribed to. This endpoint is live on the DocuSeal API but is not listed in their published reference. |
| Initialise Submission | `initSubmission` | Creates a signature request and returns just the submission id, its submitters and their signing links, instead of the full submission object. Useful for embedded signing flows. This endpoint is live on the DocuSeal API but is not listed in their published reference. |
| List Submissions | `listSubmissions` | Lists DocuSeal submissions (signature requests) with their submitters, template and signing status, filtered by template, status, folder or search text. |
| List Submitters | `listSubmitters` | Lists DocuSeal submitters (signers) with their status and the values they filled in, filtered by submission, search text or completion date. |
| List Templates | `listTemplates` | Lists the DocuSeal document templates available to the account, with their fields, submitter roles and attached documents. |
| List Webhook URLs | `listWebhookUrls` | Lists the webhook endpoints registered on the DocuSeal account, with the events each one is subscribed to. This endpoint is live on the DocuSeal API but is not listed in their published reference. |
| Merge Templates | `mergeTemplates` | Combines several DocuSeal templates, with all their documents and fields, into one new template. DocuSeal appends "(Merged)" to the first template's name when no name is given. The merged template starts with no submitter roles; set them afterwards with Update Template. |
| Update Submission | `updateSubmission` | Renames a DocuSeal submission, changes its expiration date, or archives and unarchives it. |
| Update Submitter | `updateSubmitter` | Updates a DocuSeal submitter: their contact details, pre-filled field values, or completion state. Setting Send Email to true re-sends the signature request email to this person, so leave it false unless you intend that. |
| Update Template | `updateTemplate` | Renames a DocuSeal template, moves it to a different folder, changes its submitter role names, or unarchives it. Only the fields you supply are changed. |
| Update Template Documents | `updateTemplateDocuments` | Adds, replaces or removes the documents attached to a DocuSeal template. Supply each document as a base64 file, a download URL or HTML content; pass an existing document position to replace it, or list the documents to keep. |
| Update Webhook URL | `updateWebhookUrl` | Changes the target URL or subscribed events of a DocuSeal webhook endpoint. The Events array replaces the existing subscription rather than adding to it. This endpoint is live on the DocuSeal API but is not listed in their published reference. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Signing Form Completed | `form.completed` | Fires when one submitter finishes signing. The data object is the submitter, with the values they entered and links to their signed documents. Envelope captured from a real DocuSeal delivery. |
| Signing Form Declined | `form.declined` | Fires when a submitter declines to sign. The data object is the submitter, with declined_at set. Envelope captured from a real DocuSeal delivery. |
| Signing Form Started | `form.started` | Fires when a submitter begins filling the form. The data object is the submitter. Envelope captured from a real DocuSeal delivery. |
| Signing Form Viewed | `form.viewed` | Fires the first time a submitter opens the signing form. The data object is the submitter, not the submission. Envelope captured from a real DocuSeal delivery. |
| Submission Archived | `submission.archived` | Fires when a submission is archived. Envelope captured from a real DocuSeal delivery. |
| Submission Completed | `submission.completed` | Fires when every party has signed the submission. The data object then carries the signed documents and the audit log URL. Envelope captured from a real DocuSeal delivery. |
| Submission Created | `submission.created` | Fires when a signature request is created. Payload schema captured from a real DocuSeal delivery. |
| Submission Expired | `submission.expired` | Fires when a submission passes its expiry date without being completed. Envelope captured from a real DocuSeal delivery. |
| Template Archived | `template.archived` | Fires when a document template is archived. The data object is the template, with archived_at set. Envelope captured from a real DocuSeal delivery. |
| Template Created | `template.created` | Fires when a document template is created. The data object is the template. Envelope captured from a real DocuSeal delivery. |
| Template Updated | `template.updated` | Fires when a document template is changed. The data object is the template. Envelope captured from a real DocuSeal delivery. |
