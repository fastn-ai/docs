---
description: "PDFMonkey generates PDF and image documents from reusable Liquid or drag-and-drop templates."
hidden: true
---

# PDFMonkey

PDFMonkey generates PDF and image documents from reusable Liquid or drag-and-drop templates. This connector covers the PDFMonkey v1 API: document generation (asynchronous and synchronous), documents and document cards, document templates and template cards, template folders, snippets and snippet folders, PDF rendering engines, workspaces, invoices and the current user account.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [pdfmonkey.io](https://pdfmonkey.io) |
| **Authentication** | Bearer token |
| **Actions** | 36 |
| **Events** | 2 |
| **Slug** | `pdfmonkey` |

## Use it

Add PDFMonkey from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.pdfmonkey.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Document | `createDocument` | Creates a document from a document template and queues it for asynchronous generation. Set the status to 'pending' to start generating immediately, or 'draft' to store the document without rendering it. |
| Create Document Template | `createDocumentTemplate` | Creates a document template in a workspace. The template body is Liquid-flavoured HTML for code templates, and the SCSS style sheet controls its appearance. Returns the created template including its identifier and rendering engine. |
| Create Snippet | `createSnippet` | Creates a reusable code snippet in a workspace so that several document templates can share the same Liquid or HTML fragment. |
| Create Snippet Folder | `createSnippetFolder` | Creates a snippet folder in a workspace so that reusable code snippets can be grouped together. |
| Create Template Folder | `createTemplateFolder` | Creates a template folder in a workspace so that document templates can be grouped together. |
| Delete Document | `deleteDocument` | Permanently deletes a generated document and the file stored for it. Documents are also removed automatically once their template's retention period elapses. |
| Delete Document Template | `deleteDocumentTemplate` | Permanently deletes a document template by its unique identifier. Documents already generated from the template are not removed. |
| Delete Snippet | `deleteSnippet` | Deletes a reusable code snippet by its unique identifier. Templates that still reference the snippet will fail to render until they are updated. |
| Delete Snippet Folder | `deleteSnippetFolder` | Deletes a snippet folder by its unique identifier. Snippets inside the folder are not deleted; they are moved back to the workspace root. |
| Delete Template Folder | `deleteTemplateFolder` | Deletes a template folder by its unique identifier. Templates inside the folder are not deleted; they are moved back to the workspace root. |
| Generate Document Synchronously | `generateDocumentSync` | Generates a document and waits for rendering to finish before responding, returning a Document Card that already carries the download URL. Use this when the caller needs the finished file immediately rather than polling. |
| Get Current User | `getCurrentUser` | Retrieves the PDFMonkey account that owns the API key, including the current plan, document quota and remaining document allowance. |
| Get Document | `getDocument` | Retrieves a single generated document by its unique identifier, including the merge payload, generation logs and the download URL once rendering has succeeded. |
| Get Document Card | `getDocumentCard` | Retrieves a single generated document as a lightweight Document Card, which carries the status, filename and download URL without the merge payload or generation logs. Use it to poll for the result of an asynchronous generation. |
| Get Document Template | `getDocumentTemplate` | Retrieves a single document template by its unique identifier, including the published and draft body, SCSS styles, sample data and rendering settings. |
| Get Invoice | `getInvoice` | Retrieves a single billing invoice for the PDFMonkey subscription by its unique identifier. |
| Get Snippet | `getSnippet` | Retrieves a single reusable code snippet by its unique identifier, including its shared Liquid or HTML code. |
| Get Snippet Folder | `getSnippetFolder` | Retrieves a single snippet folder by its unique identifier. |
| Get Template Folder | `getTemplateFolder` | Retrieves a single template folder by its unique identifier. |
| Get Workspace | `getWorkspace` | Retrieves a single workspace by its unique identifier, including its invite token. |
| List Document Cards | `listDocumentCards` | Lists generated documents as lightweight Document Cards, which omit the payload and generation logs. Supports filtering by template, status, workspace, last-update time and a free-text search, plus page-based pagination. |
| List Document Template Cards | `listDocumentTemplateCards` | Lists document templates as lightweight Template Cards, which omit the body and styles but add the rendering engine name and the containing folder. Use this to populate template pickers. |
| List Document Templates | `listDocumentTemplates` | Lists the document templates in the account, returning the full template records including body, styles and rendering settings. |
| List Documents | `listDocuments` | Lists generated documents with their full records, including the merge payload and the stored file details. Use List Document Cards instead when only the summary fields are needed, or Get Document when the generation logs are required. |
| List Invoices | `listInvoices` | Lists the billing invoices issued for the PDFMonkey subscription. Accounts on a trial or free plan have no invoices and receive an empty list. |
| List PDF Engines | `listPdfEngines` | Lists the PDF rendering engines available to document templates, with their version numbers and deprecation dates. Use the returned identifier to pin a template to a specific engine. |
| List Snippet Folders | `listSnippetFolders` | Lists the snippet folders used to organise reusable code snippets within a workspace. |
| List Snippets | `listSnippets` | Lists the reusable code snippets available to templates in a workspace. Snippets hold shared Liquid or HTML fragments that templates include. |
| List Template Folders | `listTemplateFolders` | Lists the template folders used to organise document templates within a workspace. |
| List Workspace Cards | `listWorkspaceCards` | Lists the account's workspaces as summary cards, which add the current subscription plan and the last update time to the basic workspace details. |
| List Workspaces | `listWorkspaces` | Lists the workspaces the account can access. A workspace groups document templates, snippets and generated documents, and its identifier is required when creating a template. |
| Update Document | `updateDocument` | Updates a document. Change the merge payload or metadata while it is still a draft, or set the status to 'pending' to trigger generation of a document that was saved as a draft. |
| Update Document Template | `updateDocumentTemplate` | Updates a document template. Only the fields supplied are changed, so this can be used to publish a new body, adjust the SCSS styles, change the rendering engine or move the template into a folder. |
| Update Snippet | `updateSnippet` | Updates a reusable code snippet. Only the fields supplied are changed, so the snippet can be renamed, re-coded or moved into a different snippet folder independently. |
| Update Snippet Folder | `updateSnippetFolder` | Renames a snippet folder by its unique identifier. |
| Update Template Folder | `updateTemplateFolder` | Renames a template folder by its unique identifier. |

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Document Generated Successfully | `success` | Fires when PDFMonkey finishes generating a document and its download URL is available. PDFMonkey names this event documents.generation.success and delivers it through Svix, which carries the event name in the svix-event-type header rather than in the body, so fastn routes on the payload's own document.status field instead. SETUP - PDFMonkey has no webhook registration API, so the endpoint is added by hand: sign in at https://dashboard.pdfmonkey.io, click Webhooks in the main navigation, click + Add Endpoint, paste this trigger's fastn webhook URL into the Endpoint URL field, subscribe the endpoint to documents.generation.success, then save. |
| Document Generation Failed | `failure` | Fires when PDFMonkey fails to render a document; the failure_cause field describes what went wrong. PDFMonkey names this event documents.generation.failure and delivers it through Svix, which carries the event name in the svix-event-type header rather than in the body, so fastn routes on the payload's own document.status field instead. SETUP - PDFMonkey has no webhook registration API, so the endpoint is added by hand: sign in at https://dashboard.pdfmonkey.io, click Webhooks in the main navigation, click + Add Endpoint, paste this trigger's fastn webhook URL into the Endpoint URL field, subscribe the endpoint to documents.generation.failure, then save. |
