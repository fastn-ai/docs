---
description: "Google Docs API v1 — create, read, and edit Google Documents programmatically using batchUpdate operations."
hidden: true
---

# Google Docs

Google Docs API v1 — create, read, and edit Google Documents programmatically using batchUpdate operations.

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [docs.google.com](https://docs.google.com) |
| **Authentication** | OAuth 2.0 |
| **Actions** | 20 |
| **Events** | 0 |
| **Slug** | `googleDocs` |

## Use it

Add Google Docs from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.googleDocs.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Append Text | `appendText` | Appends text at the very end of the document body. |
| Batch Update (Raw) | `batchUpdateRaw` | Apply a full Google Docs batchUpdate requests array to a document in one call. The granular actions (insertText, updateTextStyle, ...) each wrap a single request; this accepts the raw requests array so a caller can send an ordered mix of insertText and updateTextStyle operations whose character offsets depend on each other. Requests are applied in order and offsets are absolute, so compute them against the document's current end index (read it with getDocument first). Returns the batchUpdate reply including documentId and per-request replies. |
| Create Document | `createDocument` | Creates a new Google Document with the given title. |
| Create Footer | `createFooter` | Create a document footer using the batchUpdate API. Returns the footerId of the newly created footer. |
| Create Header | `createHeader` | Create a document header using the batchUpdate API. Returns the headerId of the newly created header. |
| Create Named Range | `createNamedRange` | Creates a named range for a segment of content in the document. |
| Delete Content Range | `deleteContentRange` | Deletes all content between startIndex and endIndex in the document. |
| Delete Document File | `deleteDocumentFile` | Permanently delete a Google Docs file through the Drive API. Authorised by the drive.file scope, which only grants access to files this OAuth client created. |
| Delete Named Range | `deleteNamedRange` | Deletes all named ranges with the given name from the document. |
| Delete Table Row | `deleteTableRow` | Delete a row from an existing table in the document using the batchUpdate API. |
| Get Document | `getDocument` | Returns the full content and metadata of a Google Document. |
| Insert Page Break | `insertPageBreak` | Inserts a page break at the specified index in the document. |
| Insert Table | `insertTable` | Inserts a table with the specified number of rows and columns at the given index. |
| Insert Table Row | `insertTableRow` | Insert a new row into an existing table in the document using the batchUpdate API. |
| Insert Text | `insertText` | Inserts text at a specific index in the document body. |
| List Documents | `listDocuments` | Search and list Google Docs files. Uses Google Drive API to filter by mimeType. Returns a list of document files with id, name, and metadata. |
| Replace All Text | `replaceAllText` | Replaces all instances of searchText with replaceText throughout the document. |
| Update Document Style | `updateDocumentStyle` | Update a document's page style including margins, page size, and background color. Uses the batchUpdate API with updateDocumentStyle request. |
| Update Paragraph Style | `updateParagraphStyle` | Updates the paragraph alignment/style for content within startIndex to endIndex. |
| Update Text Style | `updateTextStyle` | Updates bold, italic, and underline styling for text within the given range. |
