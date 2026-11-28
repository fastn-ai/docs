---
description: "Google Docs is an online document editor. Create documents, append and delete text, and add headers, footers, named ranges and table changes."
hidden: true
---

# Google Docs

<img src="../../.gitbook/assets/connectors/lg/google-docs.png" alt="Google Docs logo">

| | |
| --- | --- |
| **Category** | [Productivity](README.md) |
| **Website** | [docs.google.com](https://docs.google.com) |
| **Authentication** | OAuth 2.0 |
| **Slug** | `googleDocs` |

## Setup

Your customers sign in to Google Docs through Fastn's own OAuth app, so nothing needs setting up first. To show your own app on the consent screen instead, add your OAuth app on the connector's **Auth** tab under **Manage providers**.

## Connect in Fastn

Your customers connect Google Docs from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **Google Docs**.
2. Select **Connect** on the Google Docs card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Keep the **Default** auth provider, or choose your own OAuth app if you added one. Pick the **Scopes** you need, select **Authorize**, then sign in to Google Docs and approve access in the window that opens.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-oauth.png" alt="The Connect Salesforce dialog for OAuth 2.0 with the Default auth provider, an optional account name, the Scopes selector and an Authorize button"><figcaption><p>A connect form for OAuth 2.0. Salesforce is shown here.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use Google Docs's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Append Text</td><td><code>appendText</code></td><td>Appends text at the very end of the document body.</td></tr><tr><td>Batch Update (Raw)</td><td><code>batchUpdateRaw</code></td><td>Apply a full Google Docs batchUpdate requests array to a document in one call. The granular actions (insertText, updateTextStyle,...) each wrap a single request; this accepts the raw requests array so a caller can send an ordered mix of insertText and updateTextStyle operations whose character offsets depend on each other. Requests are applied in order and offsets are absolute, so compute them against the document's current end index (read it with getDocument first). Returns the batchUpdate reply including documentId and per-request replies.</td></tr><tr><td>Create Document</td><td><code>createDocument</code></td><td>Creates a new Google Document with the given title.</td></tr><tr><td>Create Footer</td><td><code>createFooter</code></td><td>Create a document footer using the batchUpdate API. Returns the footerId of the newly created footer.</td></tr><tr><td>Create Header</td><td><code>createHeader</code></td><td>Create a document header using the batchUpdate API. Returns the headerId of the newly created header.</td></tr><tr><td>Create Named Range</td><td><code>createNamedRange</code></td><td>Creates a named range for a segment of content in the document.</td></tr><tr><td>Delete Content Range</td><td><code>deleteContentRange</code></td><td>Deletes all content between startIndex and endIndex in the document.</td></tr><tr><td>Delete Document File</td><td><code>deleteDocumentFile</code></td><td>Permanently delete a Google Docs file through the Drive API. Authorised by the drive.file scope, which only grants access to files this OAuth client created.</td></tr><tr><td>Delete Named Range</td><td><code>deleteNamedRange</code></td><td>Deletes all named ranges with the given name from the document.</td></tr><tr><td>Delete Table Row</td><td><code>deleteTableRow</code></td><td>Delete a row from an existing table in the document using the batchUpdate API.</td></tr></tbody></table>

<details>

<summary>View 10 more actions</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Get Document</td><td><code>getDocument</code></td><td>Returns the full content and metadata of a Google Document.</td></tr><tr><td>Insert Page Break</td><td><code>insertPageBreak</code></td><td>Inserts a page break at the specified index in the document.</td></tr><tr><td>Insert Table</td><td><code>insertTable</code></td><td>Inserts a table with the specified number of rows and columns at the given index.</td></tr><tr><td>Insert Table Row</td><td><code>insertTableRow</code></td><td>Insert a new row into an existing table in the document using the batchUpdate API.</td></tr><tr><td>Insert Text</td><td><code>insertText</code></td><td>Inserts text at a specific index in the document body.</td></tr><tr><td>List Documents</td><td><code>listDocuments</code></td><td>Search and list Google Docs files. Uses Google Drive API to filter by mimeType. Returns a list of document files with id, name, and metadata.</td></tr><tr><td>Replace All Text</td><td><code>replaceAllText</code></td><td>Replaces all instances of searchText with replaceText throughout the document.</td></tr><tr><td>Update Document Style</td><td><code>updateDocumentStyle</code></td><td>Update a document's page style including margins, page size, and background color. Uses the batchUpdate API with updateDocumentStyle request.</td></tr><tr><td>Update Paragraph Style</td><td><code>updateParagraphStyle</code></td><td>Updates the paragraph alignment/style for content within startIndex to endIndex.</td></tr><tr><td>Update Text Style</td><td><code>updateTextStyle</code></td><td>Updates bold, italic, and underline styling for text within the given range.</td></tr></tbody></table>

</details>

