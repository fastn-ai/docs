---
description: "DocuGenerate document automation API."
hidden: true
---

# DocuGenerate

<img src="../../.gitbook/assets/connectors/docugenerate.png" alt="DocuGenerate logo" width="64">

DocuGenerate document automation API. Create and manage document templates (.docx, .doc, .odt, .rtf, .txt, .sql) with merge tags, then generate documents from those templates by merging JSON data or spreadsheet rows, with output in .docx, .pdf, PDF/A, .odt, .txt, .html or .png, optional PDF merging and attachments.

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [docugenerate.com](https://docugenerate.com) |
| **Authentication** | API key |
| **Slug** | `docugenerate` |

## Use it

Add DocuGenerate from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.docugenerate.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Create Template | `createTemplate` | Create a DocuGenerate template from the text content of a template file. DocuGenerate extracts the merge tags from the uploaded content and returns the template with its id, tags, delimiters and download links. Supply plain-text template formats (.txt, .sql, .rtf, .html-like markup inside .txt); binary formats such as .docx cannot be uploaded through this action. |
| Delete Document | `deleteDocument` | Permanently delete a generated DocuGenerate document by its id, removing the stored file and its download link. Returns an empty body with HTTP 204 on success and 404 if no document with that id exists. The template used to generate it is not affected. |
| Delete Template | `deleteTemplate` | Permanently delete a DocuGenerate template by its id. Returns an empty body with HTTP 204 on success and 404 if no template with that id exists. Documents already generated from the template are not returned by this call. |
| Generate Document | `generateDocument` | Generate a document from a DocuGenerate template by merging a JSON data set into the template's tags. One document is produced per data row; rows are combined into a single file unless Single File is turned off, in which case a ZIP archive is returned. Supports output in .docx, .doc, .odt, .txt, .html, .png, .pdf and PDF/A formats, plus merging extra PDFs and attaching files. Returns the generated document with its download link. |
| Generate Document From Data File | `generateDocumentFromDataFile` | Generate a document from a DocuGenerate template using the rows of a delimited data file instead of inline JSON. The first row supplies the column names, which must match the template's merge tags, and one document is produced per remaining row. Use this variant for .csv or .tsv content; binary spreadsheets (.xlsx, .xls, .ods) cannot be uploaded through this action, and output quality is only configurable on the Generate Document action. Returns the generated document with its download link. |
| Get Document | `getDocument` | Retrieve a single generated DocuGenerate document by its id, including its name, output format, filename, the number of data rows it was generated from and the link to download the generated file. |
| Get Template | `getTemplate` | Retrieve a single DocuGenerate template by its id, including the merge tags extracted from it, its delimiters, folder, storage region and the download links for the template file, its PDF preview and a PNG of its first page. |
| List Documents | `listDocuments` | List every document generated from a given DocuGenerate template, ordered by creation time descending. Returns an array of document objects with id, name, format, filename, data row count and download link. |
| List Templates | `listTemplates` | List all DocuGenerate templates in the account, ordered by creation time descending. Optionally filter to one exact folder path by filling the folder level fields from root to leaf. Returns an array of template objects with id, name, merge tags, delimiters, format, region, folder and download links. |
| Rename Document | `renameDocument` | Change the logical name of a generated DocuGenerate document. The name is the only updatable field on a document; the generated file itself and its download link are unchanged. Returns the updated document. |

<details>

<summary>See 1 more action</summary>

| Action | Slug | What it does |
| --- | --- | --- |
| Update Template | `updateTemplate` | Update an existing DocuGenerate template by id. Any field left empty is unchanged. Supplying new template content replaces the stored template file and re-extracts the merge tags; supplying new delimiters re-processes the existing content. Returns the updated template. |

</details>
