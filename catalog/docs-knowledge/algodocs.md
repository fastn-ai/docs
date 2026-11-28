---
description: "AlgoDocs extracts data from invoices, receipts and other documents. Upload documents and read the extracted data."
hidden: true
---

# AlgoDocs

<img src="../../.gitbook/assets/connectors/lg/algodocs.png" alt="AlgoDocs logo">

| | |
| --- | --- |
| **Category** | [Docs and knowledge](README.md) |
| **Website** | [algodocs.com](https://algodocs.com) |
| **Authentication** | API key, Username and password |
| **Slug** | `algodocs` |

## Setup

Your customers enter their API key or username and password for AlgoDocs when they connect. Nothing else needs setting up.

## Connect in Fastn

Your customers connect AlgoDocs from your widget. To connect an account yourself:

1. Go to **Build → Integrations → Connectors** and search for **AlgoDocs**.
2. Select **Connect** on the AlgoDocs card.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-search.png" alt="The Connectors page in Fastn with ServiceNow typed in the search box and the ServiceNow card showing a Connect button"><figcaption><p>Search for the connector, then select Connect on its card. ServiceNow is shown here.</p></figcaption></figure>

3. Fill in the fields the form asks for, using the values from [Setup](#setup) above. Then select **Connect**.

   <figure><img src="../../.gitbook/assets/connector-guides/fastn/connect-credentials.png" alt="The Connect ServiceNow dialog with an optional account name and the Instance, Username and Password fields, and Cancel and Connect buttons"><figcaption><p>A connect form that asks for credentials. Each connector asks for its own fields.</p></figcaption></figure>

4. Check that the connection appears under **Operate → Connections** with the status `Active`. Your workflows can now use AlgoDocs's actions.

For more detail, see [Connect an app](../../build/connectors/connect-an-app.md).

## Actions

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Delete Document</td><td><code>deleteDocument</code></td><td>Permanently removes an uploaded AlgoDocs document and its extraction results. Undocumented in the AlgoDocs API reference but proven live: POST is the only verb the route accepts, GET/PUT/DELETE return 405 while a nonsense sibling path returns the host 404. Deletion cannot be undone - confirm with Get Extracted Data By Document afterwards.</td></tr><tr><td>Download Document Output File</td><td><code>downloadDocumentOutput</code></td><td>Downloads one page of an AlgoDocs document in a chosen output format - the original file, or the Excel, JSON, XML, TXT or CSV rendering. The media token comes from the mediaOriginal/mediaExcel/mediaJson/mediaXml/mediaTxt/mediaCsv links on an extraction record. SECURITY: AlgoDocs serves this route without any credential, so anyone holding the link can read the document.</td></tr><tr><td>Get Current User</td><td><code>getCurrentUser</code></td><td>Returns the full name and email of the AlgoDocs account tied to the supplied credentials. Useful as a health check that authentication is wired up correctly.</td></tr><tr><td>Get Extracted Data By Document</td><td><code>getExtractedDataByDocument</code></td><td>Returns the extraction result for a single AlgoDocs document as a list - one record per page or split section, each with its own pageNumber out of totalPages. Extraction is asynchronous, so poll this action after an upload until the data object is populated. Note that a document whose type the classifier cannot recognise stillerror set instead of the extracted fields.</td></tr><tr><td>Get Extracted Data By Extractor</td><td><code>getExtractedDataByExtractor</code></td><td>Returns extraction results for every document processed by one AlgoDocs extractor, newest records included, optionally narrowed to a folder, to uploads after a given date, or to a maximum record count. Each record carries the extracted data object plus download links for the original file and the Excel, JSON, XML, TXT and CSV outputs.</td></tr><tr><td>List Extractors</td><td><code>listExtractors</code></td><td>Lists every extractor configured on the AlgoDocs account. An extractor is the trained configuration that decides which fields are pulled from a document type. Use the returned id as the extractor_id when uploading a document. Extractors can only be created in the AlgoDocs web dashboard - the API has no create route.</td></tr><tr><td>List Folders</td><td><code>listFolders</code></td><td>Lists the AlgoDocs folders on the account, with the document and page totals held in each. Use a returned folder id as the folder_id when uploading a document or as the folderId filter when listing extracted data. Folders can only be created in the AlgoDocs web dashboard - the API has no create route.</td></tr><tr><td>List Folders Including All Bucket</td><td><code>listFoldersIncludingAll</code></td><td>Undocumented AlgoDocs variant of the folder list that takes a numeric flag. Passing 1 prepends the synthetic "All" bucket (id "all") that aggregates every folder; any other number returns the same list as List Folders. Proven live against api.algodocs.com; a nonsense sibling path returns the host's 404, so this route is real.</td></tr><tr><td>Upload Document As Base64</td><td><code>uploadDocumentBase64</code></td><td>Submits a document to an AlgoDocs extractor as a base64-encoded string plus a filename. Returns the new document id, file size, MD5 checksum and upload timestamp. Extraction is asynchronous - poll Get Extracted Data By Document with the returned id until its data object is populated. Use this route when the file is not reachable by URL.</td></tr><tr><td>Upload Document From URL</td><td><code>uploadDocumentFromUrl</code></td><td>Submits a publicly reachable PDF or image URL to an AlgoDocs extractor for extraction. Returns the new document id, file size, MD5 checksum and upload timestamp. Extraction is asynchronous - poll Get Extracted Data By Document with the returned id until its data object is populated. This is the preferred upload route because it needs no binary file transfer.</td></tr></tbody></table>

<details>

<summary>View 1 more action</summary>

<table><thead><tr><th width="240">Action</th><th width="260">Slug</th><th>What it does</th></tr></thead><tbody><tr><td>Upload Local Document File</td><td><code>uploadLocalDocument</code></td><td>Uploads a document to an AlgoDocs extractor as a multipart file part. Returns the new document id, file size, MD5 checksum and upload timestamp; extraction is asynchronous, so poll Get Extracted Data By Document afterwards. LIMITATION: the Fastn engine can only carry text multipart parts, so this route works for text-safe payloads (for example an ASCII-only PDF) but not for raw binary PDF, PNG or JPEG bytes. For binary files use Upload Document As Base64 or Upload Document From URL instead.</td></tr></tbody></table>

</details>

